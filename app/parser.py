import fitz  
import docx
import os
from typing import Union
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return text


def extract_text_from_docx(file: BytesIO) -> str:
    text = ""
    document = docx.Document(file)
    for para in document.paragraphs:
        text += para.text + "\n"
    return text

def parse_resume(file_bytes, filename):
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    else:
        return "Unsupported file format"
