# Gemini PDF Talk
# Retrieval Augmented Generation using Gemini and Data from a PDF

This project demonstrates how to use Retrieval Augmented Generation (RAG) with the Gemini API to extract and process data from PDF documents. The application allows users to upload PDFs, extract text, and interact with the content using a conversational interface.

## Features

- Extract text from PDF documents
- Chunk extracted text for better processing
- Generate embeddings for text chunks
- Find the most relevant passage based on user queries
- Generate responses using the Gemini API

## Requirements

- Python 3.7+
- Streamlit
- Google Generative AI (Gemini API)
- Pandas
- NumPy
- Unstructured
- ONNX 1.16.1 (Higher versions lead to DLL errors)
- Tesseract
- Poppler

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/agilarasu/gemini_pdf_rag.git
    cd gemini_pdf_rag
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gemini API key in .env file:
    ```
    GEMINI_API_KEY='Your api key'
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Upload your PDF documents using the sidebar.

3. Ask questions based on the content of the uploaded PDFs.

# Installing Dependencies

## 1. Poppler
To install **Poppler** PDF rendering library.

### 1. **For Windows:**
You need to download a precompiled version of Poppler and add it to your system’s PATH:

- Download Poppler from [here](https://github.com/oschwartz10612/poppler-windows/releases).
- Extract the files to a directory (e.g., `C:\Program Files\poppler-xx_x_x`).
- Add Poppler's `Library/bin` folder to the system’s PATH:
  1. Right-click on **This PC** or **My Computer**, and go to **Properties**.
  2. Click **Advanced system settings**, then **Environment Variables**.
  3. Under **System variables**, find **Path** and click **Edit**.
  4. Click **New** and add the path to the Poppler `bin` folder (e.g., `C:\Program Files\poppler-xx_x_x\Library\bin`).
  5. Press **OK** to save and close.

### 2. **For macOS:**
You can install Poppler using **Homebrew**:
1. Open the Terminal.
2. Run the following commands:
   ```bash
   brew install poppler
   ```

### 3. **For Linux (Ubuntu/Debian):**
Poppler can be installed via the package manager:
1. Open the Terminal and run:
   ```bash
   sudo apt update
   sudo apt install poppler-utils
   ```

## 2. Tesseract

### 1. **For Windows:**
You need to download a precompiled version of Tesseract and add it to your system’s PATH:

- Download Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- Install with the installer file
- Add Tesseract's `C:\Program Files\Tesseract-OCR` folder to system's PATH:
  1. Right-click on **This PC** or **My Computer**, and go to **Properties**.
  2. Click **Advanced system settings**, then **Environment Variables**.
  3. Under **System variables**, find **Path** and click **Edit**.
  4. Click **New** and add the path to the Tesseract `bin` folder (e.g., `C:\Program Files\Tesseract-OCR`).
  5. Press **OK** to save and close.


## References

- [Streamlit](https://streamlit.io/)
- [Gemini Docs](https://ai.google.dev/gemini-api/docs)
- [Unstructured Docs](https://docs.unstructured.io/open-source)
- [Poppler install](https://github.com/oschwartz10612/poppler-windows/releases)
- [Tesseract binary](https://github.com/UB-Mannheim/tesseract/wiki)

