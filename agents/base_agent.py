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
        return ""

class AnalyzerAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            llm=llm,
            role='Recycling Data Analyzer',
            goal='Analyze and structure recycling service information',
            backstory="""You are an expert at analyzing and organizing information about recycling services.
            You excel at identifying patterns, gaps, and key insights.""",
            allow_delegation=False,
            verbose=True
        ) 

class ResearcherAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            llm=llm,
            role='Recycling Services Researcher',
            goal='Find detailed information about recycling services in different locations',
            backstory="""You are an expert at finding and analyzing information about recycling 
            services. You're thorough and always verify the information you collect.""",
            allow_delegation=False,
            verbose=True
        )

# Export the agents
__all__ = ['BaseAgent', 'ResearcherAgent', 'AnalyzerAgent']