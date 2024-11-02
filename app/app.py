from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import uvicorn

import os

# setting up env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# setting up the app
app = FastAPI(
    title="Amit's LangServe", version="1.0", description="A simple project of Langserve"
)

add_routes(app, ChatOpenAI(), path="/openai")

openai_model = ChatOpenAI()

llama_model = OllamaLLM(model="llama3.2")

# we'll use our openai_model for prompt1
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

# we'll use llama_model from prompt2
prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} with 100 words"
)

add_routes(app, prompt1 | openai_model, path="/essay")

add_routes(app, prompt2 | llama_model, path="/poem")

# running app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
