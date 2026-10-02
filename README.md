# AI News Summarizer

An AI-powered news analysis application that summarizes news articles and allows users to ask questions about the article using Retrieval-Augmented Generation (RAG).

The project is built using **Streamlit, FastAPI, LangChain, Gemini, and ChromaDB.**

## Features
- Generate concise summaries of news articles
- Chat with the article using a RAG-based question-answering system

## Tech Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Backend
- FastAPI
- Pydantic

### AI/LLM
- LangChain
- Google Gemini

### RAG
- Using LangChain implemented
    - Document Loader
    - Text Splitter
    - Vector store
    - Retriever 

## Working
### 1. Article Summarization
- User paste the article into the Streamlit interface.
- Article is sent to FastAPI backend and summary is generated and shown to the user.

### 2. Article Processing for RAG
- When the article is submitted, it is converted into a LangChain ```Document```

- The Document is then divided into smaller chunks using ```RecursiveCharacterTextSplitter```

### 3. Creating and Storing Embeddings 
- Each article chunk is converted into numerical vector using Google's embeddings model.
- There vectors are stored in Vector store called ChromaDB.

### 4. Asking Questions
- When the user ask question related to the article, the **LangChain Retriever** fetched the relevant article context and sent it to the LLM.
- The LLM then answers the user's query from the context only.
- If the required information cannot be found in the article, the application tells the user that the answer could not be found in the article.

## Project Structure
```
AI_news_summarizer
    - backend
        - main.py
        - rag.py
        - summary.py
    - frontend
        - app.py
    - .env
    - .env.example
    - .gitignore
    - requirements.txt
    - README.md
```

## Installation

### 1. Clone the repository
```
git clone https://github.com/Sani8Rk9git/AI-News-Summarizer.git

cd AI-News-Summarizer
```

### 2. Create a virtual environment
```
python -m venv venv

Activate it on Windows:
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Configure the API key
```
Create a .env file:
GOOGLE_API_KEY=your_google_api_key

Do not upload your actual API key to GitHub.
```

### 5. Running the Application
- Start the FastAPI backend
```
From the project root:
uvicorn backend.main:app --reload
```
- Start the Streamlit frontend
```
Open another terminal and run:
streamlit run frontend/app.py
```

## Author
**Sanidhya Sharma**

- Github: [Sani8Rk9git](https://github.com/Sani8Rk9git)
- LinkedIn: [Sanidhya Sharma](https://www.linkedin.com/in/sanidhya-sharma-2354303a8)
