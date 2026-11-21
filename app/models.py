from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0
)

model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

