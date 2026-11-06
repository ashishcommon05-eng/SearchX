# SearchX — Information Retrieval System

SearchX is an educational Web Search Mining project. It searches a local collection of TXT, PDF and DOCX documents.

## Features
- Document indexing using an inverted index
- Ranked retrieval with TF-IDF and BM25
- Basic Boolean search (AND, OR, NOT)
- Exact phrase search
- TXT, PDF and DOCX upload
- Search history stored in SQLite
- Responsive Flask website

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows (PowerShell)
Open PowerShell in the SearchX project folder, then run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, run this once in that terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Open http://127.0.0.1:5000 in your browser.

## Search modes
- Ranked: select BM25 or TF-IDF.
- Boolean: enter expressions such as `artificial AND intelligence` or `healthcare OR diagnosis`.
- Exact phrase: enter a phrase such as `information retrieval`.

Boolean mode is intentionally a simple teaching implementation. It supports word terms joined by AND, OR and NOT; it is not a complete Boolean query parser.

## Upload
Use the Documents page to upload TXT, PDF or DOCX files (maximum 15 MB). PDF files must contain selectable text; OCR is not included.

## GitHub
Create an empty GitHub repository, then from the project folder run:
```powershell
git init
git add .
git commit -m "Initial SearchX information retrieval system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/SearchX.git
git push -u origin main
```
Replace the remote URL with your own repository URL.

## Academic note
This is a local document retrieval system, not a crawler that indexes the entire public web. Explain this distinction in your report and viva.
