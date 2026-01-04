from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.retrieval_agent import RetrievalAgent
from app.agents.conversation_agent import ConversationAgent

# Initialize FastAPI app
app = FastAPI(
    title="Mental Health Support Chatbot API",
    description="Agentic AI chatbot with RAG and guardrails to prevent hallucinations",
    version="1.0"
)

# Initialize agents once (important)
retriever = RetrievalAgent()
chat_agent = ConversationAgent()

# Load and index knowledge base at startup
@app.on_event("startup")
def load_knowledge_base():
    documents = []
    files = [
        "data/knowledge_base/stress.txt",
        "data/knowledge_base/anxiety.txt",
        "data/knowledge_base/general_support.txt"
    ]

    for file in files:
        with open(file, "r") as f:
            documents.append(f.read())

    retriever.build_index(documents)


# Request schema
class ChatRequest(BaseModel):
    query: str


# Response schema
class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    docs = retriever.retrieve(request.query)
    final_response = chat_agent.generate(docs)
    return {"response": final_response}
