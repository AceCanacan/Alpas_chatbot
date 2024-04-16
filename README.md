# 🚀 Project ALEQS - Advanced Legal Exploration Query System

Project ALEQS is a cutting-edge legal research tool leveraging the power of retrieval-augmented generation and the Llama Index library. Designed to consolidate and make accessible Supreme Court decisions relating to violence against women and children, ALEQS provides an innovative way for researchers, legal professionals, and the general public to explore legal documents through natural language queries.

## 📌 Overview

ALEQS is not just a search tool; it's a comprehensive legal exploration system. By combining the sophisticated indexing capabilities of Llama Index with the nuanced understanding of large language models (LLMs), ALEQS offers unparalleled access to legal information. Whether you're conducting academic research, seeking precedents, or exploring legal scenarios, ALEQS provides insightful responses to complex queries, making legal research more intuitive and accessible than ever before.

### Key Features:
- **🔍 Retrieval-Augmented Generation**: Dynamically retrieves information from a curated database of Supreme Court decisions to generate relevant, context-rich responses.
- **🧠 Semantic Search Capabilities**: Utilizes advanced embeddings to understand and process natural language queries, delivering precise search results.
- **🌐 Streamlit Integration**: A user-friendly web interface allowing interactive querying and exploration of legal documents.
- **💾 ChromaDB Storage**: Leverages the robustness of ChromaDB for efficient data management and retrieval.

## ⚠️ Disclaimer

While ALEQS provides detailed information and insights into legal documents, it is not a substitute for professional legal advice. It is designed for informational and educational purposes, offering a new avenue for legal exploration using LLMs.

## 🛠 Data Processing Pipeline

The backbone of ALEQS is its sophisticated data processing pipeline, which includes:

- **📥 Loading/Ingesting**: Supreme Court decisions related to violence against women and children are systematically consolidated.
- **🔎 Indexing & Embedding**: Documents are indexed using the Llama Index library, with embeddings generated through OpenAI's Text Embedding 3 Small model to capture deep semantic meanings.
- **💾 Storing**: The indexed data is stored in ChromaDB, ensuring efficient retrieval.
- **🔍 Querying**: ALEQS processes natural language queries, utilizing both keyword search and semantic understanding to fetch relevant documents.
- **🌐 Streamlit Web Application**: The front end of ALEQS, where users can interact with the system, ask questions, and receive information extracted and generated from the legal documents.

## 📝 Usage

1. **🌟 Start the Streamlit Application**: Launch the ALEQS web interface through Streamlit to begin querying.
2. **❓ Query**: Enter natural language queries related to violence against women and children in the Supreme Court decisions. For example, "What are the legal precedents for domestic violence cases?"
3. **🔍 Explore Results**: Browse through the retrieved documents, summaries, and generated insights based on your query.
4. **🔄 Refine and Repeat**: Refine your queries as needed to explore different aspects of the legal documents.

## 🌱 Future Directions

Project ALEQS is an ongoing initiative with plans for expansion and enhancement. Future updates aim to broaden the database to include a wider range of legal documents, improve the semantic search capabilities, and refine the user interface for an even more intuitive research experience.

## 🤝 Contribution

Your feedback and contributions are welcome. Please feel free to fork the repository, submit pull requests, or reach out with suggestions and improvements.

