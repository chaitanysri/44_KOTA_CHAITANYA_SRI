from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


class RetrievalAgent:
    """
    FAISS + HuggingFace embeddings (offline, no API key).
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectordb = None

    def build_index(self, documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )
        chunks = splitter.split_text("\n".join(documents))

        self.vectordb = FAISS.from_texts(
            chunks,
            embedding=self.embeddings
        )

    def retrieve(self, query: str):
        return self.vectordb.similarity_search(query, k=2)

