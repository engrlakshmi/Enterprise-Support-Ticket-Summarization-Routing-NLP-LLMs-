
# 📨 Enterprise Support Ticket Summarization & Routing (NLP + LLMs)

This project demonstrates how **Large Language Models (LLMs)** and **multi-agent orchestration** can be used to **automatically summarize, classify, and route IT support tickets**.  
The system reduces manual triage work and speeds up issue resolution by intelligently processing incoming support tickets.

---

## 🚀 Features
This project demonstrates an **LLM-powered multi-agent pipeline** for IT support automation:
- **Summarizer**: Generates concise ticket summaries (BART / Pegasus).
- **Classifier**: Detects issue type & urgency via zero-shot classification.
- **Router**: Assigns the ticket to the correct IT team using rules.
- **Pipeline**: Orchestrates the agents and processes tickets end-to-end.

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

- **Hugging Face Transformers (BART, Zero-Shot models)

- **Pandas

- **Multi-agent orchestration via modular design (Summarizer, Classifier, Router)

---

