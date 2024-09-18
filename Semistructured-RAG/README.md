# Introduction

In many documents, content often consists of a mixture of text and tables, leading to challenges when performing retrieval-augmented generation (RAG) on semi-structured data. This presents two primary difficulties:

	1.	Text splitting may fragment tables, distorting their structure and corrupting data during retrieval.
	2.	Embedding tables for semantic similarity search can be problematic, as conventional methods may struggle to capture the nuanced relationships within tabular data.

To address these challenges, we employ a structured approach for RAG on semi-structured documents. 
- First, we utilize `Unstructured` to accurately parse both text and tables from documents, such as PDFs.
- Then, a `multi-vector retriever` is used to store raw tables and text, alongside table summaries that are optimized for retrieval.
- Finally, `LCEL` is implemented to manage the necessary retrieval and processing chains for this mixed-content data.

This methodology enhances the effectiveness of RAG in handling documents with complex, semi-structured formats.

# Architecture

![image](https://github.com/user-attachments/assets/fbdb853c-0168-4fc4-86b1-8d0f4e8661cd)

Source: LangChain

# Libraries

- `pypi langchain`
- `pypi langchain-chroma`
- `pypi unstructured`
- `pypi pydantic`
- `pypi lxml`
- `pypi langchainhub`

# Repository


