from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

def create_vector_store(article):
    document = Document(page_content=article)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents([document])

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding=embeddings
    )

    return vector_store

model = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash"
)


qa_prompt = PromptTemplate(
    template="""
    Answer the user's question using only the information provided
    in the article context.
    If the answer is not present in the article, say:
    "I could not find the answer in the article."
    Article context:
    {context}

    Question:
    {question}
    """,
    input_variables=["context","question"]
)

parser = StrOutputParser()

qa_chain = qa_prompt | model | parser


def answer_question(vector_store, question):
    retriever = vector_store.as_retriever(
        search_kwargs={"k":3}
    )

    documents = retriever.invoke(question)

    context = "\n\n".join(document.page_content for document in documents)

    answer = qa_chain.invoke({
        "context" : context,
        "question": question
    })

    return answer









    