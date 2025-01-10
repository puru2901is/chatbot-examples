from dotenv import load_dotenv
import os
from fastapi import FastAPI
from langchain_groq import ChatGroq
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

print(os.getenv("GROQ_API_KEY"))

llm = ChatGroq(
    temperature=0,
    model_name="mixtral-8x7b-32768"
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = llm.invoke(request.message)
    return {"response": response.content}