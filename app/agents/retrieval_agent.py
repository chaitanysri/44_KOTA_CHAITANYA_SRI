from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


class RetrievalAgent:
    """
    Retrieves relevant mental health support content using ChromaDB.
    """

    def __init__(self, persist_dir="chroma_db"):
        self.embeddings = OpenAIEmbeddings()
        self.persist_dir = persist_dir

    def build_index(self, documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )
        chunks = splitter.split_text("\n".join(documents))

        vectordb = Chroma.from_texts(
            chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
        vectordb.persist()

    def retrieve(self, query: str):
        vectordb = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embeddings
        )
        return vectordb.similarity_search(query, k=2)
