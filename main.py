from fastapi import FastAPI
from pydantic import BaseModel
import engine as en

app = FastAPI()

print("Startup: Initializing RAG Chain...")
bot = en.rag_chain()

class ChatRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request: ChatRequest):
    response = bot.invoke(request.question)
    return {"answer": response}