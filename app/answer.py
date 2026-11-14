from app.models import llm,model
from langchain_chroma import Chroma

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


def ask_question(question):
    context=retriever.invoke(question)

    formatted_context=[]
    for i in context:
        source=i.metadata.get('source')
        content=i.page_content
        page_number=i.metadata.get('page')+1
        items={'source':source,
            'content':content,
            'page_number':page_number}

        formatted_context.append(items)


    prompt=f'''
You are a medical document assistant. Answer ONLY using the context below.

Rules:
- If the context does not contain the answer, reply with exactly this one line and nothing else: Not found in sources.
- In that case, do not write any source, file name or page.
- Otherwise, answer in short, simple English.
- Never guess and never use outside knowledge.
- Copy numbers, doses and units exactly from the context.
- After the answer, add the sources you used as: (file name, page). Use the real file name and page_number from the context.

Context:
{formatted_context}

Question: {question}

Answer:
'''

    answer=llm.invoke(prompt).content

    return {
        'answer':answer,
        'sources': formatted_context
    }