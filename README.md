# langchain-ai-assistant
A flexible AI assistant built using LangChain that enables seamless switching between different LLM providers with standardized code structure, deployed using Gradio on Hugging Face Spaces. 🤖✨

## 🚀 Project Overview

Initially, the AI assistant was developed using **Google Generative AI libraries** with **Gradio** for deployment. However, switching between different Large Language Model (LLM) providers required modifying significant portions of the code due to differences in APIs.

To solve this challenge, the project was rebuilt using **LangChain**, a framework that provides a standardized interface for interacting with multiple LLM providers.

With LangChain, the assistant can easily adapt to different models with minimal code changes, making development more scalable and flexible.

---

## ✨ Features

- 🔄 Easily switch between different LLM providers
- 🧠 Standardized structure for model integration
- ⚡ Fast and flexible development workflow
- 🎛 Interactive UI built with Gradio
- 🌐 Deployed using Hugging Face Spaces
- 🧩 Modular and beginner-friendly code
- 📦 Easy dependency management

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 🐍 | Core programming language |
| LangChain 🔗 | LLM orchestration framework |
| Gemini API 🤖 | Language model provider |
| Gradio 🎛 | Web interface |
| Hugging Face Spaces 🤗 | Deployment platform |
| python-dotenv 🔑 | Environment variable management |

---

## 📂 Project Structure
langchain-ai-assistant/
│
├── app.py # Main application file
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── .env.example # Example environment variables
└── .gitignore # Ignored files

---

## 💻 Usage

1. Enter your question in the textbox
2. Click submit
3. AI assistant generates response using LLM
4. Modify model provider easily using LangChain

---

## 🌐 Deployment

This project is deployed using **Hugging Face Spaces**.

You can deploy easily by:
- Uploading repository files
- Setting environment variables in Space settings
- Selecting Gradio SDK

---

## 🔄 Why LangChain?

Using LangChain allows:

- Standardized interaction across multiple LLM providers
- Reduced code complexity
- Easy experimentation with different models
- Future scalability

Example supported providers:
- Google Gemini
- OpenAI GPT models
- Anthropic Claude
- HuggingFace models
- Local LLMs

---

## 📌 Future Improvements

- Add support for multiple LLM providers
- Add conversation memory
- Add streaming responses
- Add API endpoint support
- Add authentication
- Improve UI design

---

## 📷 Preview

Simple chatbot interface built using Gradio.
