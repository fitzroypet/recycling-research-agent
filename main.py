import logging
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from crewai import Crew, Task
from agents.base_agent import ResearcherAgent, AnalyzerAgent

# Configure more detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# More robust env loading
env_path = find_dotenv()
if not env_path:
    raise ValueError("No .env file found")

logger.debug(f"Found .env file at: {env_path}")

# Force reload environment variables
load_dotenv(env_path, override=True)

# Get API key with detailed logging
api_key = os.getenv("OPENAI_API_KEY")
logger.debug(f"Raw API key from env: {api_key[:10]}... (length: {len(api_key) if api_key else 0})")

# Validate API key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
elif not api_key.startswith("sk-"):
    raise ValueError(f"Invalid API key format. Key should start with 'sk-', got: {api_key[:10]}...")

def create_tasks(researcher, analyzer, location):
    research_task = Task(
        description=f"""Research recycling services and programs in {location}.
        Focus on:
        1. Available recycling programs
        2. Types of materials accepted
        3. Collection schedules
        4. Special waste handling
        5. Contact information
        
        Use the web_search tool to find relevant websites and the web_scraper to gather detailed information.
        Provide comprehensive information with specific details and verified sources.""",
        expected_output="""A detailed report containing:
        1. List of available recycling programs
        2. Accepted materials and their categories
        3. Collection schedules and procedures
        4. Special waste handling instructions
        5. Verified contact information and sources""",
        agent=researcher
    )

    analysis_task = Task(
        description=f"""Analyze the research findings for {location} and create a structured report.
        Include:
        1. Summary of available services
        2. Comparison with best practices
        3. Identification of unique programs
        4. Gaps in service
        5. Recommendations for improvement
        
        Format the information in a clear, organized manner with main points and supporting details.""",
        expected_output="""A structured analysis report containing:
        1. Executive summary of services
        2. Comparative analysis with best practices
        3. Highlighted unique programs
        4. Identified service gaps
        5. Specific recommendations for improvement""",
        agent=analyzer
    )

    return [research_task, analysis_task]

def main():
    try:
        logger.info("Starting application...")
        
        # Initialize the LLM
        llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.7
        )
        
        # Initialize agents
        researcher = ResearcherAgent(llm=llm)
        analyzer = AnalyzerAgent(llm=llm)
        
        # Set the location to research
        location = "Boston, MA"  # You can modify this or make it a parameter
        
        # Create tasks
        tasks = create_tasks(researcher, analyzer, location)
        
        # Create the crew
        crew = Crew(
            agents=[researcher, analyzer],
            tasks=tasks,
            verbose=True
        )
        
        # Run the crew
        logger.info(f"Starting research for {location}")
        result = crew.kickoff()
        
        logger.info("Research completed successfully")
        logger.info("Results:")
        print(result)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()