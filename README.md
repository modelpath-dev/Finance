# AI Agent System for Web Search and Financial Data

This project implements a multi-agent system using Flask, FastAPI, and various AI tools to query the web for information and provide financial data insights. The system is powered by multiple agents that interact with web search and finance tools, providing human-like responses with sources.

# Project Overview 

The system consists of two main agents:

1. Web Search Agent: This agent searches the web using DuckDuckGo for relevant information based on the query provided.
2. Finance AI Agent: This agent fetches financial data, including stock prices, analyst recommendations, and financial news, using Yahoo Finance tools.
The agents work together as a Multi-Agent System to handle a variety of user queries.

# Features 

* Web search functionality using DuckDuckGo.
* Financial data retrieval using Yahoo Finance API.
* Multi-agent coordination to handle complex queries.
* API integration with OpenAI for natural language processing.
* Responses displayed in markdown format with relevant sources.

# Dependencies

* flask: A micro web framework for Python.
* fastapi: A modern web framework for building APIs with Python.
* groq: A machine learning model for natural language processing.
* openai: OpenAI's API for accessing language models.
* yfinance: Yahoo Finance API to retrieve stock market data.
* duckduckgo-search: DuckDuckGo search tool.
* python-dotenv: To load environment variables from a .env file.
* packaging: For packaging the project.
* uvicorn: For serving FastAPI applications.

# Contribution 

Contributions to this project are welcome! If you'd like to contribute, please fork the repository and create a pull request.


