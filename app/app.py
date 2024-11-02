from dotenv import load_dotenv;
from fastapi import FastAPI

import os;

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app=FastAPI(
  title="Amit's LangServe",
  version="1.0",
  description="A simple project of Langserve"
)

