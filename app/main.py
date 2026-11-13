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


prompt=f'''You are a medical document assistant. Answer ONLY using the context below.

Rules:
- If the context does not contain the answer, reply exactly: "Not found in sources."
- Never guess and never use outside knowledge.
- Keep the answer short and in simple English.
- Do not change numbers, doses or units. Copy them exactly from the context.
- End with the sources you used, as: (file name, page).

Context:
{context}

Question: {question}

Answer:'''






answer=llm.invoke(prompt).content
print(answer,'\n\nEducational only, not medical advice.')

# print(context)