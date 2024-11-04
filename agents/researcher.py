from .base_agent import BaseAgent
import logging

class ResearcherAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            llm=llm,
            role='Recycling Services Researcher',
            goal='Research and document recycling facilities and services',
            backstory="""You are an expert at finding and structuring information about recycling 
            services. For each location, you identify and document recycling facilities, their 
            services, and operational details in a structured format.""",
            allow_delegation=False,
            verbose=True
        )

    def structured_output_format(self):
        return """
        Please provide the information in this structured format:
        
        FACILITY INFORMATION:
        Name: [Facility Name]
        Address: [Full Address]
        Contact: [Phone and Email]
        Materials Accepted: [List of materials, comma-separated]
        Hours: [Operating Hours]
        Requirements: [Any special requirements or restrictions]
        Website: [Facility Website if available]
        
        [Repeat for each facility found]
        
        Additional Services:
        [List any citywide or special recycling programs]
        
        Collection Information:
        [Details about collection schedules and procedures]
        """

    def handle_tool_failure(self, error):
        logging.error(f"Error encountered: {error}")
        # Implement logic to adjust search queries or fallback mechanisms
        if 'scraping' in str(error).lower():
            # Attempt a web search as a fallback
            logging.info("Scraping failed, switching to web search.")
            # Implement web search logic here
