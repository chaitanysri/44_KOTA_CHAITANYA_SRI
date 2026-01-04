# Mental Health Risk Screening Chatbot using Generative AI

## Problem Statement
Mental health concerns such as stress, anxiety, and depressive symptoms are increasingly prevalent. However, early identification of emotional distress is often delayed due to stigma, lack of awareness, and limited access to simple and private screening tools. Many individuals lack an accessible, non-judgmental way to reflect on their mental well-being or understand potential risk levels at an early stage.

The problem addressed in this project is the absence of an ethical, accessible, and structured mental health risk screening and support system that enables early awareness without attempting medical diagnosis or treatment.

---

## Solution Overview
This project implements a **Generative AI–enabled mental health support chatbot** using an **agentic, retrieval-augmented architecture**. The system combines standardized psychological screening, a curated knowledge base, and controlled AI response generation with guardrails to prevent hallucinations and unsafe outputs.

The solution is intentionally designed as a **screening and awareness tool**, not a diagnostic or clinical decision-making system. Ethical constraints, modular design, and safety mechanisms are applied throughout the system.

---

## Current Implementation Status

### 1. Standardized Mental Health Screening
- Implemented **PHQ-9** for depression risk screening  
- Implemented **GAD-7** for anxiety risk screening  
- User responses are numerically scored and mapped to clinically accepted risk levels  
- Outputs are clearly framed as **screening results**, not diagnoses  

---

### 2. Screening Agent
- Dedicated `ScreeningAgent` processes questionnaire responses  
- Computes total scores and maps them to risk categories  
- Produces structured, explainable screening outputs  
- Explicitly avoids medical advice or diagnostic conclusions  

---

### 3. Knowledge Base
- Curated, non-clinical mental health support content covering:
  - Stress management
  - Anxiety support
  - General emotional well-being practices
- Stored as plain text for transparency and auditability  

---

### 4. Retrieval-Augmented Generation (RAG)
- Knowledge base is embedded using **HuggingFace sentence-transformer embeddings**
- Vector search implemented using **FAISS**
- Relevant support content is retrieved based on semantic similarity
- Ensures responses are grounded in predefined knowledge (no free-form hallucination)

---

### 5. Guardrails and Safety Controls
To prevent hallucinations and unsafe outputs, multiple guardrails are implemented:
- **Context Guardrail** – blocks responses when no reliable knowledge is retrieved  
- **Medical Safety Guardrail** – prevents diagnosis, treatment, or medication advice  
- **Confidence Guardrail** – flags low-context responses  
- **Mandatory Disclaimer** – appended to all outputs  

This ensures the chatbot remains ethical, safe, and non-clinical.

---

### 6. Conversation Agent
- Query-aware response generation (not static responses)
- Uses retrieved context and user query for controlled response variation
- Rule-based reasoning to ensure consistency and explainability
- Designed to avoid speculative or authoritative medical claims

---

### 7. Backend API (FastAPI)
- Implemented a **FastAPI-based backend service**
- Exposed endpoints:
  - `/` → Health check and API discovery
  - `/chat` → Chat interaction endpoint (POST)
  - `/docs` → Swagger UI (OpenAPI documentation)
- Swagger UI used as an **API consumer**, not a frontend
- Enables easy testing without building a UI

---

## System Architecture
The system follows a **modular, agent-based architecture**:

- Screening Agent (PHQ-9, GAD-7)
- Retrieval Agent (FAISS-based vector search)
- Conversation Agent (controlled response generation)
- Guardrails Pipeline (hallucination and safety prevention)
- FastAPI Layer (API exposure and documentation)

This architecture improves interpretability, safety, and extensibility.

---

## Ethical and Safety Considerations
- No medical diagnosis or treatment is provided
- No medication or clinical recommendations are generated
- Outputs are framed as supportive guidance only
- Mandatory non-diagnostic disclaimers are included
- User data is not persistently stored

---

## Technology Stack
- Python 3.x
- FastAPI (Backend API)
- Swagger UI (OpenAPI Documentation)
- FAISS (Vector similarity search)
- HuggingFace Sentence Transformers (Embeddings)
- Modular Agent-based Design
- Rule-based Guardrails for AI safety

---

## Scope and Limitations
- The system provides screening and awareness support only
- Responses depend on user-provided input
- AI output is constrained to predefined, non-clinical knowledge
- This project is **not a replacement for professional mental health care**

---

## Planned Enhancements
- Sentiment-based scoring improvements
- Advanced evaluation metrics for hallucination detection
- Frontend client integration (optional)
- Expanded multilingual support
