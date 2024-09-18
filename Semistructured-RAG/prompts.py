'''
Author: Balaguru Sivasambagupta
Github: https://github.com/bala1802
'''

summarizer_prompt = '''
You are an assistant tasked with summarizing tables and text. 
Give a concise summary of the table or text. Table or text chunk: {element} 
'''

conversation_prompt = '''
Answer the question based only on the following context, which can include text and tables: {context}
Question: {question}
'''