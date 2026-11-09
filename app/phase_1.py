from models import model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma


#   DOCUMENT LOADER:
book1=PyPDFLoader('data/book-2.pdf').load()
book2=PyPDFLoader('data/guideline-170-en.pdf').load()
book3=PyPDFLoader('data/guideline-339-en.pdf').load()
book4=PyPDFLoader('data/hesperian_where_there_is_no_doctor.pdf').load()

loader=book1+book2+book3+book4


