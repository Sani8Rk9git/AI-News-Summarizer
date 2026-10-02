from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash"
)

prompt = PromptTemplate(
    template="""
    You are a professional news editor. Your task is to summarize the news article provided below.
    
    Guidelines:
    Tone: Maintain a professional, neutral, and objective tone.
    Clarity & Accessibility: Write in clear, straightforward language that is easy for anyone in the general public to understand, avoiding unnecessary jargon.
    Accuracy: Base your summary strictly on the information provided in the source text. Do not include outside knowledge, assumptions, or personal opinions.
    News Article: {article}
    """,
    input_variables=["article"]
)

parser = StrOutputParser()

summary_chain = prompt | model | parser





