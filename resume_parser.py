import re
import pdfplumber
from docx import Document

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        return extract_pdf_text(filepath)
    elif filepath.endswith(".docx"):
        return extract_docx_text(filepath)
    return ""

def extract_pdf_text(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_docx_text(filepath):
    doc = Document(filepath)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else "Not found"

def extract_phone(text):
    pattern = r"(\+91[\s-]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group() if match else "Not found"

def extract_education(text):
    education_keywords = [
        "B.E", "BE", "B.Tech", "BTech", "Bachelor",
        "M.E", "M.Tech", "MBA", "MCA",
        "Diploma", "HSC", "SSLC", "School", "College", "University"
    ]

    found = []
    lines = text.split("\n")

    for line in lines:
        for keyword in education_keywords:
            if keyword.lower() in line.lower():
                found.append(line.strip())

    return found if found else ["Not found"]
