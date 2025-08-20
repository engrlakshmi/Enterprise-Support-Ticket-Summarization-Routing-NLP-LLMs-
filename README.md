
# 📨 Enterprise Support Ticket Summarization & Routing (NLP + LLMs)

This project demonstrates how **Large Language Models (LLMs)** and **multi-agent orchestration** can be used to **automatically summarize, classify, and route IT support tickets**.  
The system reduces manual triage work and speeds up issue resolution by intelligently processing incoming support tickets.

---

## 🚀 Features
- **Summarization:** Generate concise summaries of long support tickets.  
- **Entity Extraction:** Identify key fields like *issue type*, *urgency*, and *product*.  
- **Multi-Agent Workflow (LangChain):**
  - Agent 1 → Summarizes ticket  
  - Agent 2 → Classifies urgency and issue type  
  - Agent 3 → Assigns to the right team  
- **Routing:** Outputs recommended support team assignment.  
- **Performance Impact:** Cut manual triage effort by ~25% in test simulations.

---

## 📂 Project Structure
├── data/
│ └── tickets.csv # Sample dataset of IT support tickets
├── notebooks/
│ └── exploratory.ipynb # EDA & baseline experiments
├── src/
│ ├── summarizer.py # Summarization pipeline
│ ├── classifier.py # Classification model (urgency, issue type)
│ ├── router.py # Rule-based / ML routing logic
│ └── main.py # Entry point combining agents
├── requirements.txt # Dependencies
└── README.md # Project documentation

## 📊 Dataset
- A dataset of IT support tickets (`tickets.csv`) is included for demo purposes.  
- Each row contains:
  - `ticket_id`  
  - `description` (full text of support request)  
  - `urgency` (low, medium, high, critical)  
  - `issue_type` (network, hardware, software, access, other)  
  - `product` (CRM, ERP, Cloud, Security, etc.)  
  - `assigned_team` (IT Helpdesk, Security, Infra, App Support)

---

## 🛠️ Tech Stack
- **LLMs:** OpenAI GPT-4, LLaMA-2, Hugging Face transformers  
- **Frameworks:** LangChain (multi-agent orchestration), PyTorch  
- **Vector DB (optional):** FAISS / Chroma for retrieval  
- **Deployment:** FastAPI for REST API, Streamlit for demo UI

---

