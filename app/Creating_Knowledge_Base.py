from models import model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma


#   DOCUMENT LOADER:
book1=PyPDFLoader('data/book-2.pdf').load()
book2=PyPDFLoader('data/guideline-170-en.pdf').load()
book3=PyPDFLoader('data/guideline-339-en.pdf').load()
book4=PyPDFLoader('data/hesperian_where_there_is_no_doctor.pdf').load()

print('\n\n1. Loading Books...')
books= book1+book2+book3+book4

#   To check the length of all the books :
# print(len(book1),'\n')
# print(len(book2),'\n')
# print(len(book3),'\n')
# print(len(book4),'\n')
# print(len(books),'\n')


#   Text Splitter:
splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=250
)
print('\n2. Chunking...')
chunks=splitter.split_documents(books)
print('\n3. Created Chunks...now creating Knowledge Base !!')


#   VectorStore:
store=Chroma.from_documents(
    documents=chunks,
    embedding=model,
    persist_directory='Knowledge_Base'
)

