import requests
import streamlit as st
import os

# using URLs from environment variables
openai_url = os.getenv("OPENAI_URL", "http://localhost:8080/essay/invoke")
llama_url = os.getenv("LLAMA_URL", "http://localhost:8080/poem/invoke")


def fetch_openai_response(topic):
    response = requests.post(openai_url, json={"input": {"topic": topic}})
    return response.json()["output"]["content"]


def fetch_llama_response(topic):
    response = requests.post(llama_url, json={"input": {"topic": topic}})
    return response.json()["output"]


st.title("Langchain demo with OpenAI and Llama")
essay_input_text = st.text_input("Write an essay on")
poem_input_text = st.text_input("Write a poem on")

if essay_input_text:
    st.write(fetch_openai_response(essay_input_text))

if poem_input_text:
    st.write(fetch_llama_response(poem_input_text))
