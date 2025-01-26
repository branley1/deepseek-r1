import os, sys
import streamlit as st
import traceback
from praisonaiagents import Agent

def init_agent():
    try:
        config = {
            "vector_store": {
                "provider": "chroma",
                "config": {
                    "collection_name": "praison",
                    "path": ".praison"
                }
            },
            "llm": {
                "provider": "ollama",
                "config": {
                    "model": "deepseek-r1:latest",
                    "temperature": 0,
                    "max_tokens": 8000,
                    "ollama_base_url": "http://localhost:11434",
                },
            },
            "embedder": {
                "provider": "ollama",
                "config": {
                    "model": "nomic-embed-text:latest",
                    "ollama_base_url": "http://localhost:11434",
                    "embedding_dims": 1536
                },
            },
        }

        pdf_path = "kag-research-paper.pdf"
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        agent = Agent(
            name="Knowledge Agent",
            instructions="You answer questions based on the provided knowledge.",
            knowledge=[pdf_path],
            knowledge_config=config,
            user_id="user1",
            llm="deepseek-r1"
        )

        print("Agent intialized successfully")
        return agent

    except Exception as e:
        print(f"Agent initialization error: {e}")
        print(traceback.format_exc())
        raise

st.title("Knowledge Agent Chat")

try:
    if "agent" not in st.session_state:
        st.session_state.agent = init_agent()
        st.session_state.messages = []
except Exception as init_error:
    st.error(f"Failed to initialize agent: {init_error}")
    st.error(traceback.format_exc())
    st.stop

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
        try:
            print(f"Processing prompt: {prompt}")
            import pdb; pdb.set_trace()
            response = st.session_state.agent.start(prompt)

            print("Response generated successfully")
            st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            print(f"Interaction error: {e}")
            print(traceback.format_exc())
            
            st.error(f"Error during interaction: {e}")
            st.error(traceback.format_exc())