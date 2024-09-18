'''
Author: Balaguru Sivasambagupta
Github: https://github.com/bala1802
'''

from os.path import dirname, join
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough

from data_extraction import extract_table_and_text_data
from summarizer import summarize_tables, summarize_texts
from vector_store import initialize_vector_store
from vector_store import initialize_parent_document_storage
from vector_store import initialize_retriever
from vector_store import store_text_and_summary
from vector_store import store_table_and_summary

from prompts import summarizer_prompt
from prompts import conversation_prompt

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

'''
Initialize Large Language Model - Open AI
'''
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

'''
Data Ingestion: Extract Tables and Texts from the Pdf document
'''
tables, texts = extract_table_and_text_data(files=["data/document.pdf"])

'''
Create Summaries for both the Table and Text data
'''
summarizer_prompt = ChatPromptTemplate.from_template(summarizer_prompt)
summarize_chain = {"element": lambda x: x} | summarizer_prompt | model | StrOutputParser()

table_summaries = summarize_tables(summarize_chain=summarize_chain, table_elements=tables)
text_summaries = summarize_texts(summarize_chain=summarize_chain, text_elements=texts)

'''
Create and Store the emebeddings inside the Vector database
'''
vectorstore = initialize_vector_store()
store, id_key = initialize_parent_document_storage()
retriever = initialize_retriever(id_key=id_key, store=store, vectorstore=vectorstore)

retriever = store_text_and_summary(id_key=id_key, text_summaries=text_summaries, texts=texts, retriever=retriever)
retriever = store_table_and_summary(id_key=id_key, table_summaries=table_summaries, tables=tables, retriever=retriever)

'''
Retrieval Augmented Generation Pipeline
'''
conversation_prompt = ChatPromptTemplate.from_template(conversation_prompt)
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | conversation_prompt
    | model
    | StrOutputParser()
)

chain.invoke("What is the age and occupation of Alice Johnson?")