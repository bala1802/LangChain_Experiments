'''
Author: Balaguru Sivasambagupta
Github: https://github.com/bala1802
'''

import uuid

from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

def initialize_vector_store():
    vectorstore = Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings())
    return vectorstore

def initialize_parent_document_storage():
    store = InMemoryStore()
    id_key = "doc_id"
    return store, id_key

def initialize_retriever(vectorstore, store, id_key):
    retriever = MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key=id_key
    )
    return retriever

def store_text_and_summary(texts, text_summaries, retriever, id_key):
    doc_ids = [str(uuid.uuid4()) for _ in texts]
    summary_texts = [
        Document(page_content=s, metadata={id_key: doc_ids[i]})
        for i, s in enumerate(text_summaries)
    ]
    retriever.vectorstore.add_documents(summary_texts)
    retriever.docstore.mset(list(zip(doc_ids, texts)))
    return retriever

def store_table_and_summary(tables, table_summaries, retriever, id_key):
    table_ids = [str(uuid.uuid4()) for _ in tables]
    summary_tables = [
        Document(page_content=s, metadata={id_key: table_ids[i]})
        for i, s in enumerate(table_summaries)
    ]
    retriever.vectorstore.add_documents(summary_tables)
    retriever.docstore.mset(list(zip(table_ids, tables)))
    return retriever

