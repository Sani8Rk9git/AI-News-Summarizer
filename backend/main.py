from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.summary import summary_chain
from backend.rag import create_vector_store, answer_question

app = FastAPI()

vector_store = None

class SummaryRequest(BaseModel):
    article:str

class QuestionRequest(BaseModel):
    question:str





@app.post("/summary")
def summary(data: SummaryRequest):
    response = summary_chain.invoke({
        "article" : data.article
    })

    global vector_store

    vector_store = create_vector_store(data.article)

    if not response:
        raise HTTPException(status_code=500, detail="AI could not generate the response.")

    return {"response" : response}

@app.post("/ask")
def ask_question(data: QuestionRequest):
    if vector_store is None:
        return {"answer": "Please submit an article first"}

    answer = answer_question(vector_store, data.question)

    if not answer:
        raise HTTPException(status_code=500, detail="AI could not generate the response.")

    return {"answer" : answer}
