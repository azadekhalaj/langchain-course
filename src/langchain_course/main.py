from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query (str): search query
    Returns:
        str: search result
    """
    print(f"Searching {query}")
    return tavily.search(query)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage("Search for three job postings for an ai engineer using langchain in Bay area in LinkedIn and list their details.")})
    print(result)

if __name__ == "__main__":
    main()