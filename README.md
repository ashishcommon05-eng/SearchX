# SearchX – Information Retrieval System

**SearchX** is a web-based Information Retrieval System developed as an academic project for the **Web Search Mining** course.

It allows users to upload, index, search, and retrieve information from a collection of local documents through a responsive web interface.

The system implements information retrieval techniques including **Inverted Indexing, TF-IDF, BM25, Boolean Retrieval, and Phrase Searching**.

---

## Features

### 1. Document Management
- Upload TXT, PDF, and DOCX documents.
- Extract text from uploaded documents.
- Index documents for efficient retrieval.
- View available documents.

### 2. Information Retrieval
- Inverted Index for document indexing.
- TF-IDF-based ranked retrieval.
- BM25-based relevance ranking.
- Boolean search using AND, OR, and NOT.
- Exact phrase searching.
- Query processing and stop-word removal.

### 3. Web Interface
- Responsive Flask-based website.
- Search results with relevance scores.
- Document snippets.
- Search history.
- SQLite database integration.

### 4. Testing and Evaluation
- Automated unit testing using Python unittest.
- Code coverage measurement.
- Evaluation metrics including Precision, Recall, F1-score, Precision@K, Recall@K, Average Precision, MAP, and MRR.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework |
| HTML5 | Website structure |
| CSS3 | Website styling |
| JavaScript | Frontend functionality |
| SQLite | Database |
| TF-IDF | Information retrieval |
| BM25 | Relevance ranking |
| unittest | Automated testing |
| Coverage.py | Code coverage |

---

## Project Requirements

- Python 3.10 or newer
- pip
- Visual Studio Code (recommended)
- Modern web browser

---

## Installation and Setup

### Step 1: Clone the repository

```powershell
git clone https://github.com/ashishcommon05-eng/SearchX.git
```

### Step 2: Open the project folder

```powershell
cd SearchX
```

### Step 3: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 4: Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### Step 5: Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 6: Start the application

```powershell
python app.py
```

### Step 7: Open SearchX

Open your browser and visit:

http://127.0.0.1:5000

---

## Search Methods

### 1. TF-IDF Ranking

TF-IDF (Term Frequency–Inverse Document Frequency) calculates the importance of a term in a document relative to the document collection.

### 2. BM25 Ranking

BM25 is a probabilistic ranking algorithm that estimates document relevance based on query terms, term frequency, document length, and collection statistics.

### 3. Boolean Retrieval

Supports basic Boolean operators:

- AND
- OR
- NOT

Example:

```text
artificial AND intelligence
```

### 4. Phrase Searching

Allows users to search for an exact sequence of words.

Example:

```text
"information retrieval"
```

---

## Document Upload

SearchX supports:

| Format | Supported |
|---|---|
| TXT | Yes |
| PDF | Yes |
| DOCX | Yes |

Maximum upload size: **15 MB**.

Note: PDF documents must contain selectable text. OCR-based extraction of scanned documents is not currently implemented.

---

## Running Automated Tests

SearchX includes automated tests for its backend components.

Run the complete test suite:

```powershell
python -m unittest backend.tests backend.test_evaluation backend.test_document_loader backend.test_query_processor backend.test_text_processing backend.test_search_engine
```

Run tests with code coverage:

```powershell
python -m coverage run -m unittest backend.tests backend.test_evaluation backend.test_document_loader backend.test_query_processor backend.test_text_processing backend.test_search_engine
```

Generate the coverage report:

```powershell
python -m coverage report -m
```

Generate an HTML coverage report:

```powershell
python -m coverage html
```

Open the report:

```powershell
start htmlcov/index.html
```

**Current testing results:**
- 93 automated tests passed.
- 99% overall measured code coverage.
- 100% coverage across all five main backend modules.

---

## GitHub Repository

Source code and project updates:

https://github.com/ashishcommon05-eng/SearchX

---

## Academic Scope

SearchX is a **local document Information Retrieval System**, not a full-scale web search engine.

It does not crawl or index the entire public internet. Instead, it focuses on retrieving relevant information from a user-provided collection of documents.

The project demonstrates fundamental concepts of Information Retrieval and Web Search Mining, including document processing, indexing, query processing, ranking algorithms, and retrieval evaluation.

---

## Author

**Ashish Gain**

Computer Science and Engineering  
IIIT Bhubaneswar

Academic Project – Web Search Mining