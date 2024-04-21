__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import openai

from llama_index.core import Document, VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

import chromadb

# Load environment variables from .env file
load_dotenv(dotenv_path='../.env')

# Accessing the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
chroma_server_host = os.getenv("CHROMA_SERVER_HOST")
chroma_server_http_port = os.getenv("CHROMA_SERVER_HTTP_PORT")
embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# load from disk
db2 = chromadb.HttpClient(host=chroma_server_host, port=chroma_server_http_port)
chroma_collection = db2.get_or_create_collection("lumad_laws_rag")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)

# Create a vector store from the Chroma collection
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Create the LlamaIndex from the vector store
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)

# -------------------------------------------- #

import streamlit as st

st.image('app/border.png')

st.markdown("""
    <h1 style='text-align: center';>⛰️ Alpas ⛰️</h1>
    <p style='text-align: center;'>👋 Welcome to the Alpas, an AI-driven chatbot focused on providing 💡 insights and answers related to the 📚 rights of indigenous peoples in the Philippines. 🇵🇭</p>
    <p style='text-align: center;'><strong>Sample questions you can ask:</strong></p>
    <ul style='list-style: none; padding: 0; text-align: center; margin: 10px 0;'>
        <li style='font-size: 12px;'>What steps must an indigenous community take to process their CADT?</li>
        <li style='font-size: 12px;'>How are indigenous rights to intellectual property protected under IPRA?</li>
        <li style='font-size: 12px;'>What are the qualifications for a community to be considered as indigenous?</li>
    </ul>
    <p style='font-size: small;text-align: center;'>This chatbot employs Retrieval-Augmented Generation to inform on legal topics, specifically indigenous rights in the Philippines—note, it's not for legal advice, does not collect personal data, and demonstrates AI's potential in legal information accessibility.</p>
    <hr style="border:1px solid #3c9394; margin: 10px 0;">
    """, unsafe_allow_html=True)
# -------------------------------------------- #

chat_engine = index.as_chat_engine(chat_mode="openai", verbose=True)


if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Please begin by sharing your question or concern about Indigenous peoples' rights."}
    ]

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history


# -------------------------------------------- #

st.image('app/border.png')
