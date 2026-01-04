from app.agents.retrieval_agent import RetrievalAgent
from app.agents.conversation_agent import ConversationAgent

# Step 1: Initialize agents
retriever = RetrievalAgent()
chat_agent = ConversationAgent()

# Step 2: Load knowledge base documents
docs_data = []

files = [
    "data/knowledge_base/stress.txt",
    "data/knowledge_base/anxiety.txt",
    "data/knowledge_base/general_support.txt"
]

for file in files:
    with open(file, "r") as f:
        docs_data.append(f.read())

# Step 3: Build vector index (IMPORTANT)
retriever.build_index(docs_data)

# Step 4: Sample user input
user_query = "I feel stressed and anxious lately"

# Step 5: Retrieve relevant context
retrieved_docs = retriever.retrieve(user_query)

# Step 6: Generate final response (guardrails applied internally)
final_response = chat_agent.generate(retrieved_docs)

print(final_response)
