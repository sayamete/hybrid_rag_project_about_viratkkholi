# 🏏 Virat Kohli Hybrid RAG

A **Hybrid Retrieval-Augmented Generation (RAG)** project built around a comprehensive knowledge base about **Virat Kohli**.

This project combines **semantic/vector search** and **keyword-based retrieval** to provide more accurate and relevant answers from a collection of documents related to Virat Kohli's **career, statistics, achievements, records, personal life, and cricket journey**.

## 🚀 Project Overview

The system retrieves relevant information from the knowledge base based on the user's query and then passes the retrieved context to a Large Language Model (LLM) to generate a natural-language response.

Unlike a basic RAG system that relies only on vector similarity, this project uses a **hybrid retrieval approach**, combining different retrieval techniques to improve the relevance and accuracy of the retrieved information.

### 🔍 Hybrid Retrieval

The project combines:

* **Vector/Semantic Search** – Finds documents based on the meaning of the query.
* **Keyword Search** – Finds documents using exact or important keywords.
* **Combined Retrieval** – Uses both approaches to improve context retrieval.
* **LLM Generation** – Generates the final answer using the retrieved context.

## 🧠 Knowledge Base

The knowledge base contains information about:

* Virat Kohli's biography
* Childhood and early cricket career
* Under-19 World Cup
* International debut
* ODI career
* Test career
* T20I career
* IPL career
* Captaincy
* World Cup performances
* Major records and milestones
* Awards and achievements
* Batting style
* Fitness and discipline
* Personal life
* Family background
* Business ventures
* Charity and social initiatives
* Career timeline

## 🛠️ Technologies Used

* Python
* LangChain
* ChromaDB
* Vector Embeddings
* Hybrid Retrieval
* Large Language Model (LLM)
* RAG Architecture
* PDF Document Processing
* Streamlit

## ⚙️ How It Works

```text
User Query
    ↓
Query Processing
    ↓
 ┌───────────────────┐
 │  Hybrid Retriever │
 └───────────────────┘
       ↓       ↓
 Vector Search  Keyword Search
       ↓       ↓
       └───┬───┘
           ↓
     Relevant Context
           ↓
        LLM Model
           ↓
     Generated Answer
```

## 🎯 Objective

The main objective of this project is to demonstrate how **Hybrid RAG architecture** can improve information retrieval by combining semantic understanding with keyword-based matching.

It also serves as a practical implementation of **Retrieval-Augmented Generation using real-world documents**.

## 💡 Example Questions

The system can answer questions such as:

* Who is Virat Kohli?
* When did Virat Kohli make his international debut?
* How many Test runs did Virat Kohli score?
* What are Virat Kohli's major records?
* When did Virat Kohli win the T20 World Cup?
* What was Virat Kohli's role in the 2023 World Cup?
* Tell me about Virat Kohli's captaincy.
* What is Virat Kohli's IPL career?
* Tell me about Virat Kohli's personal life.

## 🔮 Future Improvements

* Add more reliable cricket datasets
* Improve hybrid retrieval and ranking
* Add conversation memory
* Add source citations to generated answers
* Improve chunking and metadata filtering
* Add reranking models
* Deploy the application online
* Support multiple cricket players and teams

---

### 👨‍💻 Project Type

**Hybrid RAG | Generative AI | NLP | Information Retrieval | LLM Application**

This project demonstrates the practical use of **Retrieval-Augmented Generation and Hybrid Search** to build a domain-specific AI question-answering system.
