# 🌟 Alpas Application Documentation

## 🌐 Overview

**Alpas** is a specialized application designed to facilitate access to a large dataset of legal information concerning the rights of indigenous peoples in the Philippines. It leverages AI technologies like OpenAI's embeddings and llama_index for efficient querying and data retrieval, strictly providing information without offering legal advice. This focus ensures that users can explore and retrieve legal content relevant to indigenous rights, aiding in informed discussions and personal understanding. [Visit the App](https://alpas-chatbot.streamlit.app/)



<img width="1350" alt="Screenshot 2024-04-18 at 12 43 32 PM" src="https://github.com/AceCanacan/Alpas_chatbot/assets/110709199/c943f53a-4375-4d41-a9fb-3b52d8d84cef">

## ⚙️ Detailed Workflow of Alpas Application

### Overview

Alpas is engineered to provide a streamlined and informative user experience, focusing on delivering precise legal information regarding the rights of indigenous peoples in the Philippines. The workflow described below outlines the step-by-step process from data acquisition to user engagement, detailing how each component contributes to the overall functionality of the system.

### 1. **Data Collection and Ingestion**

- **Link Collection**: A comprehensive list of URLs linking to relevant legal documents is manually compiled and stored in `links.csv`.
- **Automated Scraping**:
  - **Setup**: Python scripts utilizing libraries like `requests` and `BeautifulSoup` initiate the scraping process.
  - **Execution**: Each URL in `links.csv` is accessed sequentially. The HTML content is downloaded and parsed to extract the text.
  - **Data Handling**: Scripts are designed to manage errors gracefully (e.g., handling empty responses or connection issues) and continue operation.
  - **Data Storage**: The processed text, free from metadata and unnecessary formatting, is stored in `downloaded_content.csv`.
  - **Progress Tracking**: The `progress_tracker.txt` file logs the last processed URL to enable interruption recovery.

### 2. **Data Processing and Index Creation**

- **Data Loading**: The application loads the cleaned data for further processing.
- **Embedding Generation**:
  - **Transformation**: Using `llama_index` with OpenAI's model `text-embedding-3-small`, textual data is transformed into semantic embeddings, enhancing the understanding beyond simple keyword searches.
- **Vector Storage**:
  - **ChromaDB Integration**: Embeddings are stored in ChromaDB on an AWS EC2 instance, optimizing the retrieval processes for user queries.

### 3. **Cloud Setup and Vector Store Management**

- **AWS Configuration**:
  - **Resource Deployment**: Utilizing AWS CloudFormation, the necessary infrastructure, including the EC2 instance for ChromaDB, is deployed.
  - **Security and Maintenance**: Basic security measures are suggested, and maintenance practices are outlined to ensure data integrity and accessibility.

### 4. **Query Processing**

- **User Interface Interaction**:
  - **Interface Design**: Users interact with a Streamlit-based interface that is straightforward and user-friendly, designed to encourage engagement.
  - **Query Submission**: Users submit their legal inquiries via the interface.
- **Query Handling and Response Generation**:
  - **Document Retrieval**: When a query is received, llama_index’s vector store index assesses the semantic similarity between the query and stored document embeddings to retrieve the most relevant documents.
  - **Response Synthesis**: A retrieval-augmented generation approach is employed, where the system synthesizes information from both the retrieved documents and pre-encoded AI knowledge to generate detailed and contextually relevant responses.
  - **Infrastructure Utilization**: This process leverages AWS's scalable resources, ensuring efficient handling of concurrent user queries.
<img width="1050" alt="Screenshot 2024-04-18 at 12 41 29 PM" src="https://github.com/AceCanacan/Alpas_chatbot/assets/110709199/8fba51b8-55b0-49ed-bc60-abdbc90abc5d">

## 🛠 Detailed Explanation of System Architecture and Technologies for Alpas

### Scalable Data Collection

- **Python and BeautifulSoup Usage**:
  - **Python**: Chosen for its extensive library support and ease of integration, Python is pivotal for scripting complex data collection tasks. Its robust handling of network operations and file management makes it ideal for interfacing with the judiciary's online repository.
  - **BeautifulSoup**: This library is particularly effective for the judiciary's website, which may not follow consistent HTML standards across different document types. BeautifulSoup provides the resilience needed to extract clean text from poorly structured HTML, ensuring reliable data capture from a variety of legal document formats.

### Advanced AI Integration

- **Llama Index and OpenAI Technologies**:
  - **Llama Index**: Selected for its sophisticated data handling and vector storage capabilities, the llama_index library excels in managing the high-dimensional data involved in semantic search applications. It is particularly adept at handling the large volumes of legal document embeddings, facilitating rapid indexing and retrieval which are crucial for responsive user experiences.
  - **OpenAI's Text Embedding Models**: The "text-embedding-3-small" model from OpenAI is utilized for its ability to transform complex legal language into high-quality vector representations. This model supports the nuanced understanding and processing of legal text, making it possible to accurately match user queries with relevant legal documents.

### Robust Cloud Infrastructure

- **AWS EC2 and ChromaDB Configuration**:
  - **AWS EC2**: We chose AWS EC2 due to its scalability and reliability for hosting applications with variable loads. For Alpas, handling potentially large fluctuations in user demand and data volume efficiently is critical. EC2's ability to scale processing power and memory in response to application needs ensures that the application remains responsive and stable.
  - **ChromaDB**: This vector database is crucial for its efficient handling of vector data, which underpins the semantic search capabilities of Alpas. Hosted on AWS, ChromaDB facilitates the rapid retrieval of vectors, making the search process both fast and accurate. The choice of AWS as the hosting solution is also strategic for its comprehensive integration with other AWS services, enhancing overall system resilience and data durability.

### User-Focused Query System

- **Streamlit Interface**:
  - **Streamlit**: The selection of Streamlit for the user interface is based on its ease of setup and impressive capabilities for creating interactive applications. For Alpas, which aims to demystify legal information, Streamlit provides a straightforward interface that allows users to input queries and receive information without navigating complex processes. Its capacity to handle real-time data processing and updates seamlessly makes it particularly suited for applications like Alpas, where user engagement and simplicity are key.


