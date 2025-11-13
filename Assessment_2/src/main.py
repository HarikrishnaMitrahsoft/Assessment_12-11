from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from src.chatbot import query_rag

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.get("/api/health")
def health():
    return {"response": 'Health is ok'}

@app.get("/api/ask-faq")
def chat(request: ChatRequest):
    return {"response": query_rag(request.query)}