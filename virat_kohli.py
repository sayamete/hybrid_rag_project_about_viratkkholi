import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import langchain_community

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from rank_bm25 import BM25Okapi

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


# =========================================================
# STREAMLIT FRONTEND
# =========================================================

st.set_page_config(
    page_title="Virat Kohli Hybrid RAG",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Virat Kohli Hybrid RAG")
st.write("Ask your questions about Virat Kohli")


# =========================================================
# LOAD PDF
# =========================================================

loder = PyPDFLoader(
    'Virat_Kohli_Complete_With_Personal_Life.pdf'
)

pages = loder.load()


# =========================================================
# SPLIT TEXT
# =========================================================

spliter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

text = spliter.split_documents(pages)

chunk = []

for i in text:
    chunk.append(i.page_content)


metadata = []

for i in text:
    metadata.append(i.metadata)


# =========================================================
# CHROMADB
# =========================================================

embedding_function = SentenceTransformerEmbeddingFunction()

client = chromadb.PersistentClient(
    path="./database-3"
)

collection = client.get_or_create_collection(
    name="Collection",
    embedding_function=embedding_function
)


try:

    if collection.count() == 0:

        collection.add(
            documents=chunk,
            ids=[str(i) for i in range(len(chunk))],
            metadatas=metadata
        )

except Exception as e:

    st.error(str(e))


# =========================================================
# BM25
# =========================================================

def token_create(i):

    i = i.lower()
    i = i.split()

    return i


token = [token_create(i) for i in chunk]

token_for_keyword_search = BM25Okapi(token)


# =========================================================
# HYBRID RETRIEVAL
# =========================================================

def retrival(query: str):

    query_lower_case = query.lower()

    # -------------------------
    # Vector Search
    # -------------------------

    response = collection.query(
        query_texts=[query_lower_case],
        n_results=5
    )

    document = response['documents'][0]
    distance = response['distances'][0]

    thresold = 1.6

    near_chunk = []

    for i, j in zip(distance, document):

        if thresold > i:

            near_chunk.append(j)


    # -------------------------
    # BM25 Search
    # -------------------------

    score = token_for_keyword_search.get_scores(
        token_create(query_lower_case)
    )


    def near_index_find(score, k=10):

        index = list(enumerate(score))

        index_sorted = sorted(
            index,
            key=lambda x: x[1],
            reverse=True
        )

        return [
            inx
            for inx, sc in index_sorted[:k]
        ]


    get_index = near_index_find(score, k=10)

    index_to_chunk = []

    for i in get_index:

        index_to_chunk.append(chunk[i])


    # -------------------------
    # RRF
    # -------------------------

    rrf_item = {}

    for rank, doc in enumerate(near_chunk):

        rrf_item[doc] = (
            rrf_item.get(doc, 0)
            + 1 / (rank + 60)
        )


    for rank, doc in enumerate(index_to_chunk):

        rrf_item[doc] = (
            rrf_item.get(doc, 0)
            + 1 / (rank + 60)
        )


    merge = sorted(
        rrf_item.items(),
        key=lambda x: x[1],
        reverse=True
    )


    top_related_doc = []

    for doc, _ in merge:

        top_related_doc.append(doc)


    if not top_related_doc:

        return "NOT RELATED CONTENT"


    return "\n\n".join(top_related_doc)


# =========================================================
# GROQ
# =========================================================

load_dotenv()

api = os.getenv('GROQ_API_KEY')

groq_llm_model = ChatGroq(
    model='openai/gpt-oss-120b',
    api_key=api
)


# =========================================================
# STREAMLIT QUESTION
# =========================================================

question = st.text_input(
    "Ask your question about Virat Kohli:",
    placeholder="Example: What is Virat Kohli's birthday?"
)


# =========================================================
# GENERATE ANSWER
# =========================================================

if st.button("Ask Question"):

    if question:

        with st.spinner("Searching the document..."):

            content = retrival(question)


        prompt = """
You are a realiable ai assistent so provide user asking qustions based on only the local document

content = {content}

qustion = {question}
"""


        final_prompt = prompt.format(
            content=content,
            question=question
        )


        with st.spinner("Generating answer..."):

            answer = groq_llm_model.invoke(
                final_prompt
            ).content


        st.subheader("🤖 Answer")

        st.write(answer)


        # Optional: show retrieved content
        with st.expander("🔍 Retrieved Content"):

            st.write(content)

    else:

        st.warning("Please enter a question.")