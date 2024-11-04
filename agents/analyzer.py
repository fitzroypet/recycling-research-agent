from .base_agent import BaseAgent

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