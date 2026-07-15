import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def summary(article):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Generate a professional summary
            of the article:{article}
            """
        )

        return response.text

    except Exception:
        return "Error generating AI response."