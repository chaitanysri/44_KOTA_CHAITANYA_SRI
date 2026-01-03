**Mental Health Risk Screening Chatbot using Generative AI**<br>

**Problem Statement**
Mental health concerns such as stress, anxiety, and depressive symptoms are increasingly prevalent. However, early identification of emotional distress is often delayed due to stigma, lack of awareness, and limited access to simple and private screening tools. Many individuals lack an accessible, non-judgmental way to reflect on their mental well-being or understand potential risk levels at an early stage.
The problem addressed in this project is the absence of an ethical, accessible, and structured mental health risk screening system that can support early awareness without attempting medical diagnosis or treatment.

**Solution Overview**
This project implements a Generative AI–enabled mental health risk screening chatbot that combines standardized psychological screening methods with modern AI techniques. The system focuses on structured screening, transparent risk scoring, and retrieval of supportive guidance grounded in a curated knowledge base.
The solution is intentionally designed as a screening and awareness tool, not a diagnostic or clinical decision-making system. Ethical constraints and modular design principles are applied to ensure safety, clarity, and extensibility.

**Current Implementation Status**
The following components have been implemented and validated:
Standardized Mental Health Screening
Implemented PHQ-9 for depression risk screening
Implemented GAD-7 for anxiety risk screening
User responses are scored numerically and categorized into clinically accepted risk levels
Outputs are explicitly framed as screening results, not diagnoses

**Screening Agent**
A dedicated ScreeningAgent processes questionnaire responses
Computes total scores and maps them to risk categories
Produces structured, explainable output suitable for downstream AI components
Does not provide medical advice or diagnostic conclusions

**Knowledge Base**
Curated text-based support content covering:
Stress management
Anxiety support
General emotional well-being practices
Content stored in plain text to ensure transparency and auditability

**Retrieval-Augmented Generation (RAG) Setup**
Implemented ChromaDB as a vector database
Knowledge base content is embedded and indexed
Relevant support content is retrieved based on screening interpretations
Indexing and retrieval pipeline successfully tested

**System Architecture**
The system follows a modular, agent-based architecture, where each component has a clearly defined responsibility. This design improves safety, interpretability, and future extensibility.

**Core Components**
**Screening Agent**
Accepts user responses to PHQ-9 and GAD-7 questionnaires
Performs scoring and risk categorization
Generates structured screening outputs with disclaimers
Acts as the primary decision-free analytical layer

**Knowledge Base**
Stores curated, non-clinical mental health support content
Maintained in a human-readable text format
Serves as the grounding source for AI-generated responses

**Retrieval Agent**
Converts knowledge base content into vector embeddings
Stores and queries embeddings using ChromaDB
Retrieves semantically relevant support material based on screening outcomes
Ensures AI responses remain grounded in predefined content

**Context Preparation Layer**
Combines screening results with retrieved support content
Prepares bounded and safe context for AI response generation
Prevents speculative or harmful outputs

**Ethical and Safety Considerations**
The system does not perform medical diagnosis
No treatment or medication advice is provided
Outputs are framed as risk indications and supportive guidance only
Screening results include explicit non-diagnostic disclaimers
User data is not persistently stored

**Technology Stack (Implemented So Far)**
Python 3.x
Standardized psychological questionnaires (PHQ-9, GAD-7)
ChromaDB (Vector Database)
LangChain ecosystem (embeddings and retrieval)
Modular agent-based design

**Scope and Limitations**
The system provides screening and awareness support only
Results depend on user-provided responses
AI components are constrained to non-diagnostic outputs
This project is not a replacement for professional mental health care

**Planned Enhancements**
Safety agent for response validation
Conversational LLM agent for empathetic response generation
Backend API integration
Frontend interface integration
Evaluation metrics and guardrails documentation
