# gemini_pdf_rag
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

## References

- [Streamlit](https://streamlit.io/)
- [Gemini Docs](https://ai.google.dev/gemini-api/docs)
- [Unstructured Docs](https://docs.unstructured.io/open-source)

