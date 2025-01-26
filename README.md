# Deepseek-r1 Knowledge Agent Chatbot


This project is a straightforward chatbot application built using Streamlit, designed to answer your questions using the Deepseek-r1:7b model, a powerful language model running locally via Ollama. It leverages the innovative Knowledge Augmented Generation (KAG) framework, which combines knowledge graph reasoning with traditional retrieval methods to enhance accuracy and logical coherence. To provide relevant context, the chatbot also uses a vector database (Chroma) to store and retrieve information, similar to a personal research assistant that can quickly scan and synthesize information from documents you provide. The KAG framework, as implemented in Deepseek-r1:7b, allows the model to perform complex reasoning tasks and reduces the likelihood of inaccurate or "hallucinated" responses, particularly in specialized domains.
## What It Does

The chatbot currently uses the DeepSeek-R1 model, but you can configure it to use other models available in Ollama. It's designed to be simple and easy to use:

1. **Chat Interface:**  A clean chat interface lets you type in your questions.
2. **Local LLM:** The brains of the operation is an LLM running locally on your machine thanks to Ollama. No need to send your data to external APIs.
3. **Knowledge Base:** You can provide PDF documents to the chatbot, which are then stored in a vector database to allow the chatbot to find and use relevant information from those documents when answering your questions.

## Getting Started

### Prerequisites

1. **Python 3.10 or higher:**  Make sure you have a compatible version of Python installed.
2. **Ollama:** Download and install Ollama from [https://ollama.ai/](https://ollama.ai/).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/branley1/deepseek-r1/
    cd deepseek-r1
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    Or install the libraries listed in the Prerequisites section manually.

4. **Download the LLM models:**

    ```bash
    ollama pull deepseek-r1:7b
    ollama pull nomic-embed-text:latest
    ```

5. **Start the Ollama server:**

    ```bash
    ollama serve
    ```

### Running the Chatbot

1. **Launch the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

  There's also two test files with different models that can be tried out: 
   ```bash
    streamlit run test.py
   ```

  ```bash
    streamlit run test2.py
   ```

  

2. **Open your web browser and go to the URL provided by Streamlit (usually [http://localhost:8501](http://localhost:8501)).**

## Configuration

You can tweak how the chatbot works by changing the settings in the `init_agent()` function within `app.py`. The main settings are in the `config` dictionary:

*   **`vector_store`:**
    *   `provider`: Right now, it's set to `chroma` (the vector database).
    *   `config`:  Specific settings for Chroma, including where to store the data.

*   **`llm`:**
    *   `provider`: Set to `ollama` to use your local LLM.
    *   `config`:
        *   `model`: The name and tag of the Ollama model (e.g., `deepseek-r1:7b`).
        *   `temperature`: Controls how random the answers are (0.0 is the most predictable, higher values are more creative).
        *   `max_tokens`: Limits the length of the response.
        *   `base_url`:  The address of your Ollama server (usually `http://localhost:11434`).

*   **`embedder`:**
    *   `provider`: Also set to `ollama`.
    *   `config`:
        *   `model`: The Ollama model used to create vector embeddings of your documents.
        *   `base_url`: The address of your Ollama server.
        *   `embedding_dims`: The dimensions of the vector embeddings.

## Adding Your Own Knowledge

1. **Put your PDF documents in the same folder as the script.**
2. **Update the `knowledge` list in `init_agent()`:**

    ```python
    agent = Agent(
        # ... other settings ...
        knowledge=["your_document.pdf", "another_document.pdf"],
        # ... other settings ...
    )
    ```

## Known Issues

*   **Ollama Configuration:** There's a known issue where the app might try to connect to OpenAI's API even though it's configured to use Ollama. This is actively being investigated.
*   **Resource Warnings:** You might see some warnings about unclosed files. These are generally harmless for now but should be fixed eventually.

## Future Plans

*   **Fix the Ollama configuration bug.** This is the top priority.
*   **Make the UI more responsive.**  Right now, the app might freeze a bit while it's generating responses.
*   **Improve error handling.** Make the app more robust and user-friendly when things go wrong.
*   **Add streaming support.**  This would let you see the chatbot's response as it's being generated, making it feel more interactive.
*   **UI/UX improvements:**  Allow users to select models, change settings, and manage knowledge directly through the interface.

## Troubleshooting

*   **"Incorrect API Key" error:**  Double-check your configuration and make sure it's set to use `ollama`, not `openai`.
*   **"ResourceWarning: unclosed file":** You can ignore this for now, but it should be fixed eventually.
*   **Ollama connection problems:** Ensure the Ollama server is running (`ollama serve`) and that the `base_url` in your config is correct.
*   **Model not found:** Run `ollama pull <model_name>:<tag>` to download the models you need.

## Contributing

Feel free to submit pull requests or open issues on the project's GitHub page!

## License

This project is licensed under the MIT License.

## Authors
Branley Mmasi
