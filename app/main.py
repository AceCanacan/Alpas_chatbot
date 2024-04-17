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

query_engine = index.as_query_engine()

import streamlit as st

st.image('border.png')

st.markdown("""
    <h1 style='text-align: center';>Legal Querying System</h1>
    <p style='text-align: center;'>👋 Welcome to the Legal Querying System, an AI-driven chatbot focused on providing 💡 insights and answers related to the 📚 rights of indigenous peoples in the Philippines. 🇵🇭</p>
    <p style='text-align: center;'><strong>Sample questions you can ask:</strong></p>
    <ul style='list-style: none; padding: 0; text-align: center; margin: 10px 0;'>
        <li style='font-size: 12px;'>What steps must an indigenous community take to process their CADT?</li>
        <li style='font-size: 12px;'>How are indigenous rights to intellectual property protected under IPRA?</li>
        <li style='font-size: 12px;'>What are the qualifications for a community to be considered as indigenous?</li>
    </ul>
    <hr style="border:1px solid #3c9394; margin: 10px 0;">
    """, unsafe_allow_html=True)

user_query = st.text_input("Enter your query here:", "", help="Type your question about indigenous people's rights in the Philippines and press enter. The chatbot will provide the information you need.")

submit_button = st.button("Submit")


if submit_button:
    # Update the session state to indicate the query has been submitted
    st.session_state.submitted = True

# Once the query has been submitted
if st.session_state.get('submitted', False):
    # Reset the 'submitted' state for next input
    st.session_state.submitted = False
    
    if user_query:  # making sure the input is not empty
        response_object = query_engine.query(user_query)
        
        response_text = response_object.response
        st.write(response_text)
    else:
        st.write("Please enter a query to get a response.")

st.markdown("""
   <hr style="border:1px solid #3c9394; margin: 10px 0;">
    """, unsafe_allow_html=True)

st.markdown("""
    <p style='font-size: small;text-align: center;margin-bottom: 50px;'>This chatbot employs Retrieval-Augmented Generation to inform on legal topics, specifically indigenous rights in the Philippines—note, it's not for legal advice, does not collect personal data, and demonstrates AI's potential in legal information accessibility.</p>
    """, unsafe_allow_html=True)

st.image('border.png')