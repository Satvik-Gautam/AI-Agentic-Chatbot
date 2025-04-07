import os
from dotenv import load_dotenv
load_dotenv()

#Setting up API Key's of Groq , OPENAI and Tavily
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
 

# Setup LLM and Tools Related to it 
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults


groq_llm=ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearchResults(max_results=2)


# Setting up AI Agent with Search Tavily one 
from langchain_core.messages.ai import AIMessage
from langgraph.prebuilt import create_react_agent

system_prompt = "Act as an AI Chatbot Who is Smart and friendly"

def get_response_from_ai_agent(llm_id ,messages ,allow_search,system_prompt , provider):
    if provider == "Groq":
        llm =ChatGroq(model=llm_id)


    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model= llm,
        tools =tools,
        state_modifier=system_prompt
        
    )


    
    state = {"messages": messages}
    response = agent.invoke(state)
    response_messages = response.get("messages" ,[])
    ai_messages = [message.content  for message in response_messages if isinstance(message , AIMessage)]
    return ai_messages[-1]