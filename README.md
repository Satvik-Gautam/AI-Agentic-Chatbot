<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge">
  <img src="https://img.shields.io/badge/Groq-00C4B4?style=for-the-badge&logoColor=white" alt="Groq Badge">
</p>

# 🤖 AI Chatbot Agent

Welcome to **AI Chatbot Agent**—a powerful, interactive chatbot powered by Groq’s advanced language models and a sleek Streamlit frontend! This project combines a FastAPI backend with LangGraph and Tavily search capabilities to deliver smart, friendly, and context-aware responses. Whether you're asking questions, seeking insights, or exploring the web, this chatbot is your go-to companion.

![image_alt](https://github.com/Satvik-Gautam/AI-Chatbot/blob/d7ca70f9b266564ec293274f47df27023acb3477/pic.png)

---

## 🌟 Features
- **Dynamic AI**: Customize your chatbot’s personality with a system prompt.
- **Groq Models**: Choose from models like `llama-3.3-70b-versatile`, `mistral-saba-24b`, and more.
- **Web Search**: Enable Tavily-powered search for real-time answers.
- **Modern UI**: A clean Streamlit interface with intuitive controls.
- **Scalable Backend**: FastAPI powers the API, ready for cloud deployment.

---

## 🛠️ Project Structure
AI-Chatbot/
- backend.py         # FastAPI backend for API endpoints
- ai_agent.py        # LangGraph AI agent with Groq and Tavily integration
- frontend.py        # Streamlit UI for user interaction
- requirements.txt   # Dependencies for backend and AI agent


---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+** 🐍
- **Git** 📂
- **API Keys**:
  - Groq API Key (for models)
  - Tavily API Key (for search)

### Installation
1. **Clone the Repository**:
   git clone https://github.com/Satvik-Gautam/AI-Chatbot.git
   cd AI-Chatbot
2. **Install Dependencies**:
   pip install -r requirements.txt
3. **Set Environment Variables**:
   GROQ_API_KEY=your-groq-api-key
   TAVILY_API_KEY=your-tavily-api-key

## Usage
Start the Backend: Ensure backend.py is running.

Open the UI: Launch frontend.py in Streamlit.

Configure the Agent:
Enter a system prompt (e.g., "Be a friendly tech assistant").

Select a Groq model (e.g., gemma2-9b-it).

Toggle "Allow Web Search" for enriched responses.

Ask Away: Type a query (e.g., "What’s Python?") and click "Ask Agent!"

Get Answers: See the response in the UI.

## Author
Satvik Gautam
GitHub: Satvik-Gautam
A project fueled by curiosity and code! 
<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Made with Python">
</p>

## Visual Representation
https://github.com/user-attachments/assets/493a280e-2ca8-4e36-abb5-d2068a1c27b9

