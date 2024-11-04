from .base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            llm=llm,
            role='Recycling Services Researcher',
            goal='Find and structure detailed information about recycling facilities and services',
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
        Contact: [Phone and/or Email]
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