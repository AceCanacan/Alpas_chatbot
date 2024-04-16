import pandas as pd
import openai
import llama_index
import streamlit as st

import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from IPython.display import Markdown, display
import chromadb

import os
from dotenv import load_dotenv
import openai

import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv(dotenv_path='../.env')

# Accessing the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

chroma_server_host = os.getenv("CHROMA_SERVER_HOST")
chroma_server_http_port = os.getenv("CHROMA_SERVER_HTTP_PORT")
embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# load from disk
db2 = chromadb.HttpClient(host=chroma_server_host, port=chroma_server_http_port)
chroma_collection = db2.get_or_create_collection("LumadAI_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)


query_engine = index.as_query_engine()
st.title("Legal Querying System")

user_query = st.text_input("Enter your query here:", "")

submit_button = st.button("Submit")

if submit_button:
    # Update the session state to indicate the query has been submitted
    st.session_state.submitted = True

# Once the query has been submitted
if st.session_state.get('submitted', False):
    if user_query:  # making sure the input is not empty
        response_object = query_engine.query(user_query)
        
        response_text = response_object.response
        st.write(response_text)
        
        if st.button("New Query"):
            st.session_state.submitted = False
            user_query = "" 
    else:
        st.write("Please enter a query to get a response.")
