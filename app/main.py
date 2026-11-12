from models import llm,model
from langchain_chroma import Chroma


question=input('Question: ')


#   load the vector store:
vector_store = Chroma(
    persist_directory="Knowledge_Base",
    embedding_function=model
)


#   Retriever:
retriever=vector_store.as_retriever(
    search_kwargs={
        'k':4
    }
)

context=retriever.invoke(question)



# print(context)