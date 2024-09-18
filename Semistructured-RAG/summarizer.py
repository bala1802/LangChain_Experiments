'''
Author: Balaguru Sivasambagupta
Github: https://github.com/bala1802
'''

def summarize_texts(summarize_chain, text_elements):
    texts = [i.text for i in text_elements]
    text_summaries = summarize_chain.batch(texts, {"max_concurrency": 5})
    return text_summaries

def summarize_tables(summarize_chain, table_elements):
    tables = [i.text for i in table_elements]
    table_summaries = summarize_chain.batch(tables, {"max_concurrency": 5})
    return table_summaries