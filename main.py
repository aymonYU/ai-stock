from fastapi import FastAPI
from langchain_core import LangChain

app = FastAPI()
lc = LangChain()

@app.post("/ask")
async def ask(question: str):
    return {"answer": lc.invoke(question)}
