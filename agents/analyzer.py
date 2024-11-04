from .base_agent import BaseAgent

class AnalyzerAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            llm=llm,
            role='Recycling Data Analyzer',
            goal='Analyze and structure recycling service information with clear facility details',
            backstory="""You are an expert at analyzing and organizing recycling services data.
            You structure information about facilities and services in a clear, consistent format,
            and provide insights about service coverage and gaps.""",
            allow_delegation=False,
            verbose=True
        )

    def structured_output_format(self):
        return """
        Please analyze the data and provide output in this format:
        
        **Recycling Services Analysis: [Location]**

        **1. Executive Summary of Services**
        [Overview of available services, including number of facilities and key programs]

        **2. Facility Details**
        [For each facility, include:
        - Name
        - Address
        - Contact Information
        - Materials Accepted
        - Operating Hours
        - Special Requirements]

        **3. Comparative Analysis with Best Practices**
        [Analysis of services compared to industry standards]

        **4. Unique Programs**
        [Description of special or innovative programs]

        **5. Service Gaps**
        [Bullet points of identified gaps in service]

        **6. Recommendations**
        [Bullet points of specific improvements]
        """