import streamlit as st
from praisonaiagents import Agent

def init_agent():
    config = {
        "llm": {
            "provider": "ollama",
            "config": {
                "model": "deepseek-r1:latest",
                "ollama_base_url": "http://localhost:11434",
            },
        },
        "embedder": {
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text:latest",
                "ollama_base_url": "http://localhost:11434",
            },
        },
    }

    try:
        agent = Agent(
            name="Test Agent",
            instructions="Answer with 'OK'",
            knowledge=[],
            knowledge_config=config,
            user_id="testuser",
            llm="deepseek-r1"
        )
        return agent
    except Exception as e:
        st.error(f"Error initializing agent: {e}")
        return None

st.title("Minimal Agent Test")

agent = init_agent()

if agent:
    try:
        response = agent.start("Test query")
        st.write(f"Agent response: {response}")
    except Exception as e:
        st.error(f"Error during interaction: {e}")
        if hasattr(e, 'error'):
            st.write(f"Error details: {e.error}")
        else:
            st.write(str(e))