# LLM-Security-Lab-2026

## 🛡️ LLM Security Lab: Prompt Injection Defenses

Welcome to the LLM Security Lab! In this lab, you will explore the fascinating and critical area of Large Language Model (LLM) security, specifically focusing on **prompt injection** and **jailbreaking** techniques. Your mission, should you choose to accept it, is to build and implement robust defenses to protect a chatbot from malicious user inputs.

### 🎯 Your Goal

Your primary goal is for this lab is to play with jailbreaks and, more importantly, to develop effective countermeasures. You will be tasked with modifying the `defense.py` file to sanitize user inputs and prevent the chatbot from revealing sensitive information or behaving in unintended ways.

### 🚀 Getting Started

Follow these steps to set up your local development environment and get the chatbot running:

#### Prerequisites

Before you begin, ensure you have the following installed:

1.  **Docker Desktop**: This lab uses `docker-compose` to manage the application and its dependencies. Download and install Docker Desktop from docker.com.
2.  **Ollama**: We will be running a local LLM using Ollama. Download and install Ollama from ollama.com.
    - After installation, pull a model. For example: `llama3.2`. Open your terminal and run:
      ```bash
      ollama pull llama3.2
      ```
    - Other models are available, we recommend you take a smaller model to start with. You will most definitely be able to run smaller models on your own device and they are sometimes more easier to jailbreak.

#### Setup Instructions

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/Tomjg14/LLM-Security-Lab-2026.git
    cd LLM-Security-Lab-2026
    ```

2.  **Configure Environment Variables**:
    The project uses a `.env` file for configuration.
    - Copy the example environment file:
      ```bash
      cp .env.example .env
      ```
    - Open the newly created `.env` file.
    - If you want to make use of Ollama:
        - **Uncomment** the lines below "When using Ollama" and ensure `BASE_URL` points to your local Ollama instance (default is `http://localhost:11434/v1`).
    - If you want to make use of the [Radboud On-Premise LLM service](https://cncz.science.ru.nl/en/news/2026-02-05_local_llm_chat/):
        - **Uncomment** the lines for "When using chat.science.ru.nl".
        - Go to [chat.science.ru.nl](https://chat.science.ru.nl/) and log in using your science credentials.
        - In the top right hand corner click on your profile and go to settings.
        - Within Settings go to Account and in the bottom you can create your own API keys.
        - Inside the .env file replace the "your_api_key_here" part with your own API keys.

    Your `.env` file should look similar to this for local Ollama usage:

    ```dotenv
    # Uncomment one of the two options below
    # Either use the models on chat.science.ru.nl
    # Or use any local Ollama model

    # When using chat.science.ru.nl
    # API_KEY=your_api_key_here
    # MODEL_NAME=gpt-oss:120b
    # BASE_URL=https://chat.science.ru.nl/api

    # When using Ollama
    MODEL_NAME=llama3.2
    BASE_URL=http://localhost:11434/v1
    ```

3.  **Run the Application with Docker Compose**:
    Navigate to the root directory of the project (where `docker-compose.yml` is located) in your terminal and run:

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker image, set up the container, and start the Streamlit application.

4.  **Access the Chatbot**:
    Once the application is running, open your web browser and navigate to `http://localhost:8501`.

### 💻 Project Structure

- `app.py`: The main Streamlit application that hosts the chatbot UI and interacts with the LLM.
- `defense.py`: **This is where you will implement your defenses!** Contains the `sanitize_input` function.
- `system_prompt.txt`: Defines the initial instructions and persona for the chatbot, including a hidden "secret" password.
- `.env.example` / `.env`: Configuration for API keys and LLM endpoints.
- `docker-compose.yml`: Defines the Docker services for the application.

### 😈 Attacker's Goal (and how to test your defenses)

The chatbot is designed to be a helpful customer support agent. However, it has a secret administrative override password embedded in its system prompt. Your task as an "attacker" (to test your defenses) is to craft prompts that trick the LLM into revealing this secret password.

As a "defender," your job is to modify the `sanitize_input` function in `defense.py` to detect and neutralize these malicious prompts before they reach the LLM. Experiment with different injection techniques and see if your defenses hold up!

Good luck, and happy hacking (defensively)!
