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

```
.
├── README.md
├── data
│   └── document.pdf
├── data_extraction.py
├── main.py
├── prompts.py
├── summarizer.py
└── vector_store.py
```

# Data Extraction

The script `data_extraction.py` is designed to extract both `Texts` and `Tables` from the provided PDF document, which in this case is located at `data/document.pdf`. To achieve this, the `unstructured` library is utilized, offering effective parsing of PDFs by splitting the content into structured text and table components. This enables seamless processing of semi-structured data by separating different content types while preserving their context for downstream tasks such as retrieval and analysis.

# Summarizer

The script `summarizer.py` is responsible for generating summaries of both the `Text` and `Tables` extracted during the `Data Extraction` phase. This is accomplished using the `OpenAI GPT-3.5-Turbo` large language model, which processes the retrieved content to create concise and informative summaries.

# Prompts

The script `prompts.py` contains the necessary prompts used for processing user queries as well as for summarizing the extracted texts and tables. These prompts serve as the input instructions for interacting with the language model, guiding it to perform tasks such as query-based retrieval and generating concise summaries of the document’s content. 
