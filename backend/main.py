from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.
import os

app = FastAPI()

g.generativeai.configure(api_key=os.environ[GOOGLE_API_KEY])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Trading Agent API is running"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/gemini")
async def gemini():
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content("How does AI work?")
    return response.text