from fastapi import FastAPI, UploadFile, File
import io
import os
import tempfile
import mimetypes
import fitz  # PyMuPDF for PDFs
import docx  # python-docx for DOCX files
import docx2txt  # docx2txt for TXT files

app = FastAPI()

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(pdf_file)
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text += page.get_text()
    pdf_document.close()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_txt(txt_file):
    with open(txt_file, "r", encoding="utf-8") as txt:
        text = txt.read()
    return text

@app.post("/upload/")
async def upload_and_extract_text(file: UploadFile = File(...)):
    # Create a temporary directory to store the uploaded file
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, file.filename)
        
        # Save the uploaded file to the temporary directory
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
        # Determine the file type using mimetypes
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # Extract text based on the file type
        if mime_type == "application/pdf":
            extracted_text = extract_text_from_pdf(file_path)
        elif mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            extracted_text = extract_text_from_docx(file_path)
        elif mime_type == "text/plain":
            extracted_text = extract_text_from_txt(file_path)
        else:
            return {"error": "Unsupported file type"}
        
        return {"extracted_text": extracted_text}

