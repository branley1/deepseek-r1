import streamlit as st
import requests
import json

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1:latest",
        "prompt": prompt,
        "stream": True 
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Assuming the response is JSON (adjust if needed)
        response_json = response.json()

        # Extract the response content (adjust the key based on Ollama's response format)
        if response_json['done']:
            return response_json['response']
        else:
            return "Response not found"

    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Ollama: {e}")
        return None
    except json.JSONDecodeError as e:
        st.error(f"Error decoding Ollama response: {e}")
        return None

st.title("Direct Ollama Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "messages" in st.session_state:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Ask a question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = ask_ollama(prompt)
        if response:
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})