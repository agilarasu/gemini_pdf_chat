import os
import textwrap
import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np

from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title

import os

# Load your Gemini API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Creating custom template to guide llm model
custom_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""


# Extracting text from pdf (without unstructured package)
def extract_data(docs):
    # Partition the PDF
    elements = partition_pdf(docs[0], strategy="hi_res")
    
    # Chunk the partitioned elements
    chunked_elements = chunk_by_title(
        elements,
        max_characters=500,
        new_after_n_chars=1500,
        combine_under_n_chars=200,
        multipage_sections=True
    )

    # Process the chunked elements
    for chunk in chunked_elements:
        print(f"Chunk Type: {chunk.type}")
        print(f"Chunk Text: {chunk.text[:100]}...")  # Print first 100 characters
        print(f"Page Number: {chunk.metadata.get('page_number')}")
        print("---")
        
    return chunked_elements

# Get the embeddings of each text and add to an embeddings column in the dataframe
def embed_fn(text):
    return genai.embed_content(model="models/embedding-001",
                             content=text,
                             task_type="retrieval_document")["embedding"]

def find_best_passage(query, text_embeddings):
    """
    Compute the distances between the query and each document in the dataframe
    using the dot product.
    """
    query_embedding = genai.embed_content(model="models/embedding-001", content=query, task_type="retrieval_query")["embedding"]
    similarities = np.dot(text_embeddings['embeddings'].tolist(), query_embedding)
    best_passage_index = np.argmax(similarities)
    best_passage = text_embeddings.iloc[best_passage_index]['text']
    print(best_passage)
    return best_passage

def make_prompt(query, relevant_passage):
    relevant_passage = " ".join(relevant_passage)
    prompt = textwrap.dedent("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
    However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
    strike a friendly and converstional tone. \
    If the passage is irrelevant to the answer, you may ignore it.
    QUESTION: '{query}'
    PASSAGE: '{relevant_passage}'

      ANSWER:
    """).format(query=query, relevant_passage=relevant_passage)

    return prompt

def handle_question(question, dataframe):
    relevant_passage = find_best_passage(question, dataframe)
    prompt = make_prompt(question, relevant_passage)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    answer = model.generate_content(prompt)
    print(answer)
    return answer

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.markdown(
        """
    <style>
    .user-message {
        background-color: #f0f0f0;
        color: black;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .bot-message {
        background-color: #121212;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    question = st.text_input("Ask question from your document:")
    if question and "embeddings" in st.session_state:
        answer = handle_question(question, st.session_state.embeddings)
        answer=answer.text
        # Update chat history
        st.session_state.conversation.append({"role": "user", "content": question})
        st.session_state.conversation.append({"role": "bot", "content": answer})

    st.markdown("## Chat History:")
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "bot":
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader(
            "Upload your PDF here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                texts = extract_data(docs)
                df = pd.DataFrame({'text': texts, 'embeddings': [embed_fn(text) for text in texts]})
                st.session_state.embeddings = df

if __name__ == "__main__":
    main()