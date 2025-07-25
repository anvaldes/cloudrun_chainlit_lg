# 🤖 Chainlit Gemini Agent UI

This project implements a conversational interface deployed on **Cloud Run**, powered by an intelligent agent built using **Gemini**, **LangGraph**, and **LangChain**. It is designed for natural interactions with generative models in a scalable and modular architecture.

---

## 🚀 Technologies Used

| Tool              | Description |
|-------------------|-------------|
| [Gemini](https://deepmind.google/technologies/gemini/) | Google's generative model, accessed via the official API (`generativelanguage.googleapis.com`). |
| [LangGraph](https://www.langgraph.dev/) | A framework for building agents with structured decision flows and state persistence. |
| [LangChain](https://www.langchain.com/) | A library for building LLM-powered agents and toolchains. |
| [Cloud Run](https://cloud.google.com/run) | GCP’s serverless container service for automatic and scalable deployments. |

---

## 🧠 Agent Architecture

The conversation flow is built using **LangGraph**, with custom tools and logic to process user input, make decisions, and respond via the **Gemini** model.

---

## 🐳 CI/CD with GitHub Actions

This project includes a GitHub Actions workflow that:

1. Builds the Docker image.
2. Pushes it to Artifact Registry.
3. Deploys the service to Cloud Run.
4. Injects a secure API key for Gemini at runtime.

---

## 📦 Local Development (optional)

```bash
# Clone the repository
git clone https://github.com/your_username/your_repository.git
cd your_repository

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally with Chainlit
chainlit run main.py
