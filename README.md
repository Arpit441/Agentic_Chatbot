**Landgraph AI Agent — Concept**
This project builds an AI Chatbot Agent system using FastAPI (backend) and Streamlit (frontend).

The frontend (Streamlit app) allows users to define a custom system prompt, choose an AI model (from Groq or OpenAI), decide whether to allow web search, and ask questions.

The backend (FastAPI server) receives the user's request, dynamically creates an AI agent using LangGraph's ReAct agent, and uses LLM models to generate intelligent responses.
If allowed, it uses Tavily Search to fetch real-time web results for better answers.

The agent can switch between different LLMs based on user input and customize behavior based on the system prompt.

The whole system enables flexible, dynamic, and interactive conversations with AI, optionally enhanced by live web searches.











