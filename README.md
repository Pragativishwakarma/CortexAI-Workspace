# 🚀 AI Student Learning Assistant

> **An Agentic AI-powered learning platform that generates personalized learning roadmaps, retrieves educational resources using RAG, leverages MCP tools, and maintains long-term conversational memory with PostgreSQL and LangGraph.**

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-green)
![LangChain](https://img.shields.io/badge/LangChain-Framework-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Memory-blue)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![License](https://img.shields.io/badge/License-MIT-success)

---

# 📚 Overview

**AI Student Learning Assistant** is a full-stack Agentic AI application designed to create intelligent and personalized learning experiences.

The application combines **LangGraph**, **LangChain**, **Model Context Protocol (MCP)**, **Retrieval-Augmented Generation (RAG)**, **PostgreSQL Memory**, and **Streamlit** to generate structured learning plans, retrieve relevant educational resources, and maintain persistent user conversations.

Unlike a traditional chatbot, the assistant coordinates multiple AI components through an agentic workflow to provide accurate, context-aware, and memory-enabled responses.

---

# ✨ Features

* 🤖 Agentic AI Workflow using LangGraph
* 🧠 Supervisor Agent Orchestration
* 📚 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Search using FAISS
* 📄 PDF Knowledge Base Support
* 🛠 Model Context Protocol (MCP) Tool Integration
* 💾 Persistent Memory with PostgreSQL
* 🧠 LangGraph Checkpointing
* 🎯 Personalized Learning Roadmaps
* 📖 Resource Recommendations
* ❓ Quiz Generation
* 📑 Final Learning Reports
* 🎨 Interactive Streamlit Dashboard

---

# 🏗 System Architecture

```text
                      User
                        │
                        ▼
               Streamlit Frontend
                        │
                        ▼
               LangGraph Supervisor
                        │
      ┌──────────┬──────────┬──────────┐
      │          │          │
      ▼          ▼          ▼
   RAG Agent   MCP Agent   Memory Agent
      │          │          │
      ▼          ▼          ▼
 FAISS Index   External   PostgreSQL
Embeddings      Tools     Checkpointer
      │
      ▼
 Sentence Transformers
```

---

# 🚀 Tech Stack

| Category         | Technologies                    |
| ---------------- | ------------------------------- |
| Language         | Python                          |
| AI Framework     | LangGraph                       |
| LLM Framework    | LangChain                       |
| LLM              | Groq                            |
| Agent Framework  | LangGraph Supervisor            |
| Tool Integration | MCP                             |
| Vector Database  | FAISS                           |
| Embeddings       | Sentence Transformers           |
| Database         | PostgreSQL                      |
| Memory           | LangGraph Postgres Checkpointer |
| Frontend         | Streamlit                       |
| Document Loader  | PyPDF                           |
| Environment      | python-dotenv                   |

---

# 📂 Project Structure

```text
AI_Student_Learning_Assistant/

│
├── frontend.py
├── requirements.txt
├── .env
│
├── rag/
│   ├── ingest.py
│   ├── vector_store.py
│   ├── documents/
│   └── faiss_index/
│
├── agents/
│
├── graph/
│
├── database/
│
├── utils/
│
└── README.md
```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Pragativishwakarma/CortexAI-Workspace.git

cd CortexAI-Workspace
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If any dependency fails:

```bash
pip install "psycopg[binary]"
```

Install PyTorch separately if required:

```bash
pip install torch torchvision torchaudio
```

---

# 📄 Build the Vector Database

After placing your PDF documents inside the **documents** folder:

```bash
python -m rag.ingest
```

or

```bash
python rag/ingest.py
```

This command:

* Loads PDFs
* Splits text
* Creates embeddings
* Builds the FAISS vector database

---

# 🗄 PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE learning_assistant;
```

Update your `.env`

```env
GROQ_API_KEY=your_api_key

DATABASE_URL=postgresql://username:password@localhost:5432/learning_assistant
```

The application automatically creates checkpoint tables:

* checkpoints
* checkpoint_blobs
* checkpoint_writes
* checkpoint_migrations

---

# ▶ Running the Application

```bash
streamlit run frontend.py
```

The application will be available at

```
http://localhost:8501
```

---

# 🧠 Application Workflow

### User enters a learning topic

↓

Supervisor Agent receives request

↓

RAG searches knowledge base

↓

MCP tools retrieve additional information

↓

LLM generates learning roadmap

↓

Resources are recommended

↓

Quiz is generated

↓

Conversation is stored in PostgreSQL

↓

Future conversations continue from previous memory

---

# 📷 Application Preview

## Dashboard

* Personalized learning roadmap generation
* Supervisor Agent orchestration
* RAG-enabled document retrieval
* PostgreSQL persistent memory
* MCP Tool integration
* Interactive learning interface

---

## PostgreSQL Memory

The application stores persistent conversation checkpoints inside PostgreSQL using LangGraph's checkpointing mechanism.

Generated tables include:

```
checkpoints

checkpoint_blobs

checkpoint_writes

checkpoint_migrations
```

This enables:

* Persistent conversations
* Resume previous sessions
* Long-term memory
* Agent state checkpointing

---

# 📦 Requirements

```
langgraph
langchain
langchain-groq
langchain-community
langchain-mcp-adapters
langgraph-checkpoint-postgres

mcp

psycopg[binary]

streamlit

faiss-cpu

sentence-transformers

torch

torchvision

torchaudio

python-dotenv

pypdf
```

---

# 💡 Web App

<img width="1438" height="704" alt="Screenshot 2026-07-10 at 12 08 25 PM" src="https://github.com/user-attachments/assets/8b0534df-8753-4002-add2-d6c5afc583a7" />

# Database

<img width="990" height="812" alt="Screenshot 2026-07-10 at 12 22 21 PM" src="https://github.com/user-attachments/assets/0555384c-985c-4a96-9ffd-0c0e93960ee1" />

*

---

# 👩‍💻 Author

**Pragati Vishwakarma**

---

