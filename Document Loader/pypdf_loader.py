from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI()

loader = PyPDFLoader("Building Machine Learning Systems with Python - Second Edition.pdf")

docs = loader.load()

#print(docs[20].page_content)

print(len(docs))
print(docs[20].metadata)

print(docs[15].page_content)

for i in range(15, 25):
    print(f"\n--- Page Index {i} ---")
    print(docs[i].page_content[:500])