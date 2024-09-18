'''
Author: Balaguru Sivasambagupta
Github: https://github.com/bala1802
'''

import os
from typing import Any

from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf

class Element(BaseModel):
    type: str
    text: Any

def extract_pdf_elements(files):
    file = files[0]
    directory, file_name = os.path.split(file)

    raw_pdf_elements = partition_pdf(
        filename=file,
        extract_images_in_pdf=False,
        infer_table_structure=True,
        chunking_strategy="by_title",
        max_characters=4000,
        new_after_n_chars=3800,
        combine_text_under_n_chars=2000,
        image_output_dir_path=directory)

    return raw_pdf_elements

def examine_elements(raw_pdf_elements):
    category_counts = {}
    for element in raw_pdf_elements:
        category = str(type(element))
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    unique_categories = set(category_counts.keys())
    print("Category Counts are : ")
    print(unique_categories)

def extract_table_and_text_data(files):
    raw_pdf_elements = extract_pdf_elements(files=files)
    examine_elements(raw_pdf_elements=raw_pdf_elements)

    categorized_elements = []
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            categorized_elements.append(Element(type="table", text=str(element)))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            categorized_elements.append(Element(type="text", text=str(element)))

    # Tables
    table_elements = [e for e in categorized_elements if e.type == "table"]
    print(len(table_elements))

    # Text
    text_elements = [e for e in categorized_elements if e.type == "text"]
    print(len(text_elements))

    return table_elements, text_elements