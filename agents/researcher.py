from .base_agent import BaseAgent

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