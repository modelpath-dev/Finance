from flask import Flask, request, jsonify
from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai

from dotenv import load_dotenv
openai.api_key=os.getenv("OPENAI_API_KEY")


websearch_agent=Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True , technical_indicators=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True, 
)

multi_ai_agent=Agent(
    team=[websearch_agent, finance_agent],
    instructions=["Always include the sources","Use tables to show the data"],
    show_tools_calls=True,
    markdown=True,
)

query=input("Enter your query: \n")

multi_ai_agent.print_response(f"{query}", stream=True)