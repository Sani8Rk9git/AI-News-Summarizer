import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def answer(question,article):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            {question}
            answer the question in context
            of the 
            article: {article}
            """
        )

        return response.text

    except Exception:
        return "Error generating AI response."