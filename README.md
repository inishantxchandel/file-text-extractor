# File Upload and Text Extraction API using FastAPI

This repository contains a simple FastAPI application that allows you to upload files (PDF, DOC, DOCX, TXT) and extract text content from them. It demonstrates how to handle various file types and perform text extraction using relevant libraries.

## Setup

1. Clone the repository:

git clone https://github.com/your-username/your-fastapi-project.git
cd your-fastapi-project
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required dependencies:
pip install -r requirements.txt
2. Usage
Run the FastAPI application:
uvicorn main:app --host 0.0.0.0 --port 8000
Access the API documentation at http://localhost:8000/docs in your web browser. You can use this documentation to understand the available endpoints and test them.
Use the /upload/ endpoint to upload files and extract text content from them. You can use tools like curl or API clients like Postman to test the API.
API Endpoints
Upload and Extract Text
Endpoint: /upload/
Method: POST
Parameters:
file: The file to upload (PDF, DOC, DOCX, or TXT)
Response:
If successful, the API will return extracted text content from the uploaded file.
Supported File Types
PDF files: Text extraction using PyMuPDF.
DOCX files: Text extraction using python-docx.
TXT files: Text extraction using docx2txt.
License
This project is licensed under the MIT License.
Remember to replace `"your-username"` and `"your-fastapi-project"` with your actual GitHub username and project repository name. Also, ensure that you have the `requirements.txt` file in your repository with the necessary library dependencies.
