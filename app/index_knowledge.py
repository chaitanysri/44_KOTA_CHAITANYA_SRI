from app.agents.retrieval_agent import RetrievalAgent

docs = []

files = [
    "data/knowledge_base/stress.txt",
    "data/knowledge_base/anxiety.txt",
    "data/knowledge_base/general_support.txt"
]

for file in files:
    with open(file, "r") as f:
        docs.append(f.read())

agent = RetrievalAgent()
agent.build_index(docs)

print("Knowledge base indexed successfully")
