import logging
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from crewai import Crew, Task
from agents.base_agent import ResearcherAgent, AnalyzerAgent
from formatters.document_formatter import DocumentFormatter
from formatters.excel_formatter import ExcelFormatter
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)]
)

console = Console()
logger = logging.getLogger("recycling-research")

def create_tasks(researcher, analyzer, location):
    research_task = Task(
        description=f"""Research recycling services and facilities in {location}.
        
        Required Information:
        1. Identify all recycling facilities and drop-off centers
        2. Document their exact locations, contact details, and operating hours
        3. List accepted materials for each facility
        4. Note any special requirements or restrictions
        5. Find information about collection schedules and procedures
        
        {researcher.structured_output_format()}
        
        Use the web_search tool to find facilities and the web_scraper to gather detailed information.
        Verify all information and provide complete details for each facility.""",
        expected_output="""A comprehensive list of recycling facilities and services, 
        with complete details formatted according to the specified structure.""",
        agent=researcher
    )

    analysis_task = Task(
        description=f"""Analyze the research findings for {location} and create a structured report.
        
        {analyzer.structured_output_format()}
        
        Ensure all facility information is preserved and properly formatted in the analysis.
        Include specific metrics and data points where available.""",
        expected_output="""A detailed analysis report following the specified format,
        including facility details, comparative analysis, and specific recommendations.""",
        agent=analyzer
    )

    return [research_task, analysis_task]

def main():
    try:
        # Initialize Progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            # Setup task
            setup_task = progress.add_task("[yellow]Setting up application...", total=6)
            
            # Load environment variables
            env_path = find_dotenv()
            if not env_path:
                raise ValueError("No .env file found")
            load_dotenv(env_path, override=True)
            progress.update(setup_task, advance=1)
            
            # Initialize the LLM
            progress.update(setup_task, description="[yellow]Initializing LLM...")
            llm = ChatOpenAI(
                model="gpt-4-turbo-preview",
                temperature=0.7
            )
            progress.update(setup_task, advance=1)
            
            # Initialize agents
            progress.update(setup_task, description="[yellow]Initializing agents...")
            researcher = ResearcherAgent(llm=llm)
            analyzer = AnalyzerAgent(llm=llm)
            progress.update(setup_task, advance=1)
            
            # Set location and create tasks
            location = "Lagos, Nigeria"
            progress.update(setup_task, description="[yellow]Creating research tasks...")
            tasks = create_tasks(researcher, analyzer, location)
            progress.update(setup_task, advance=1)
            
            # Create and run the crew
            progress.update(setup_task, description=f"[blue]Researching {location}...")
            crew = Crew(
                agents=[researcher, analyzer],
                tasks=tasks,
                verbose=True
            )
            result = crew.kickoff()
            
            # Convert CrewOutput to string
            result_text = str(result)
            
            # Create output directory
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)
            
            # Save results
            progress.update(setup_task, description="[cyan]Saving results...")
            
            # Format and save Word document
            doc_formatter = DocumentFormatter(location)
            doc = doc_formatter.format_report(result_text)
            doc_formatter.save(f"{output_dir}/recycling_analysis_{location.replace(', ', '_')}.docx")
            
            # Format and save Excel file
            excel_formatter = ExcelFormatter(location)
            excel_formatter.format_data(result_text)
            excel_formatter.save(f"{output_dir}/recycling_metrics_{location.replace(', ', '_')}.xlsx")
            
            progress.update(setup_task, advance=1)
            
            # Complete all tasks
            progress.update(setup_task, description="[green]Research completed!")
            
            # Print results
            console.print("\n[bold]Results:[/bold]")
            console.print(result)
            
            console.print("\n[bold green]Files saved:[/bold green]")
            console.print(f"- Word document: recycling_analysis_{location.replace(', ', '_')}.docx")
            console.print(f"- Excel spreadsheet: recycling_metrics_{location.replace(', ', '_')}.xlsx")
            
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}", style="red")
        raise

if __name__ == "__main__":
    main()