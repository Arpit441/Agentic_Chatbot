import os 

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")


from langchain_groq import ChatGroq

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage 

groq_llm = ChatGroq(model ="deepseek-r1-distill-llama-70b")




from langgraph.prebuilt import create_react_agent
#system_prompt = "Act as an AI chatbot  who is smart and give accurate results"

def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider =="Groq":
        llm = ChatGroq(model = llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model = llm_id)

    search_tool = [TavilySearchResults(max_results = 2)] if allow_search else []
    agent = create_react_agent(
    model = groq_llm,
    tools = search_tool,
    state_modifier = system_prompt
    )
    
    state ={"messages" : query}
    response = agent.invoke(state) 
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance (message, AIMessage)]
    return (ai_messages[-1])
