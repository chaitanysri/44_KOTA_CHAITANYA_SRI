**Mental Health Risk Screening Chatbot using Generative AI**<br>

**Problem Statement**<br>
Mental health concerns such as stress, anxiety, and depressive symptoms are increasingly prevalent. However, early identification of emotional distress is often delayed due to stigma, lack of awareness, and limited access to simple and private screening tools. Many individuals lack an accessible, non-judgmental way to reflect on their mental well-being or understand potential risk levels at an early stage.
The problem addressed in this project is the absence of an ethical, accessible, and structured mental health risk screening system that can support early awareness without attempting medical diagnosis or treatment.<br>

**Solution Overview**<br>
This project implements a Generative AI–enabled mental health risk screening chatbot that combines standardized psychological screening methods with modern AI techniques. The system focuses on structured screening, transparent risk scoring, and retrieval of supportive guidance grounded in a curated knowledge base.
The solution is intentionally designed as a screening and awareness tool, not a diagnostic or clinical decision-making system. Ethical constraints and modular design principles are applied to ensure safety, clarity, and extensibility.<br>

**Current Implementation Status**<br>
The following components have been implemented and validated:<br>
Standardized Mental Health Screening<br>
Implemented PHQ-9 for depression risk screening<br>
Implemented GAD-7 for anxiety risk screening<br>
User responses are scored numerically and categorized into clinically accepted risk levels<br>
Outputs are explicitly framed as screening results, not diagnoses<br>

**Screening Agent**<br>
A dedicated ScreeningAgent processes questionnaire responses<br>
Computes total scores and maps them to risk categories<br>
Produces structured, explainable output suitable for downstream AI components<br>
Does not provide medical advice or diagnostic conclusions<br>

**Knowledge Base**<br>
Curated text-based support content covering:<br>
Stress management<br>
Anxiety support<br>
General emotional well-being practices<br>
Content stored in plain text to ensure transparency and auditability<br>

**Retrieval-Augmented Generation (RAG) Setup**<br>
Implemented ChromaDB as a vector database<br>
Knowledge base content is embedded and indexed<br>
Relevant support content is retrieved based on screening interpretations<br>
Indexing and retrieval pipeline successfully tested<br>

**System Architecture**<br>
The system follows a modular, agent-based architecture, where each component has a clearly defined responsibility. This design improves safety, interpretability, and future extensibility.<br>

**Core Components**<br>
**Screening Agent**<br>
Accepts user responses to PHQ-9 and GAD-7 questionnaires<br>
Performs scoring and risk categorization<br>
Generates structured screening outputs with disclaimers<br>
Acts as the primary decision-free analytical layer<br>

**Knowledge Base**<br>
Stores curated, non-clinical mental health support content<br>
Maintained in a human-readable text format<br>
Serves as the grounding source for AI-generated responses<br>

**Retrieval Agent**<br>
Converts knowledge base content into vector embeddings<br>
Stores and queries embeddings using ChromaDB<br>
Retrieves semantically relevant support material based on screening outcomes<br>
Ensures AI responses remain grounded in predefined content<br>

**Context Preparation Layer**<br>
Combines screening results with retrieved support content<br>
Prepares bounded and safe context for AI response generation<br>
Prevents speculative or harmful outputs<br>

**Ethical and Safety Considerations**<br>
The system does not perform medical diagnosis<br>
No treatment or medication advice is provided<br>
Outputs are framed as risk indications and supportive guidance only<br>
Screening results include explicit non-diagnostic disclaimers<br>
User data is not persistently stored<br>

**Technology Stack (Implemented So Far)**<br>
Python 3.x<br>
Standardized psychological questionnaires (PHQ-9, GAD-7)<br>
ChromaDB (Vector Database)<br>
LangChain ecosystem (embeddings and retrieval)<br>
Modular agent-based design<br>

**Scope and Limitations**<br>
The system provides screening and awareness support only<br>
Results depend on user-provided responses<br>
AI components are constrained to non-diagnostic outputs<br>
This project is not a replacement for professional mental health care<br>

**Planned Enhancements**<br>
Safety agent for response validation<br>
Conversational LLM agent for empathetic response generation<br>
Backend API integration<br>
Frontend interface integration<br>
Evaluation metrics and guardrails documentation<br>
