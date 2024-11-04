from crewai import Agent
from tools.web_scraper import RecyclingWebScraper
from tools.search_tool import CustomSearchTool
import logging
from langchain_openai import ChatOpenAI

class BaseAgent(Agent):
    def __init__(self, llm=None, *args, **kwargs):
        tools = [
            RecyclingWebScraper(),
            CustomSearchTool()
        ]
        
        if 'tools' not in kwargs:
            kwargs['tools'] = tools
            
        if llm:
            kwargs['llm'] = llm
            
        logging.debug(f"Initializing agent with LLM: {kwargs.get('llm', 'No LLM specified')}")
        super().__init__(*args, **kwargs)

def structured_output_format(self):
        """Base method that should be overridden by child classes"""
        raise NotImplementedError("Subclasses should implement this method.")