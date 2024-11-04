from langchain.tools import BaseTool
import time
import requests
from typing import Optional
from pydantic import BaseModel, Field

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup4 not installed. Installing now...")
    import subprocess
    subprocess.check_call(["pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

from config.settings import REQUEST_TIMEOUT, RATE_LIMIT_DELAY

class WebScraperSchema(BaseModel):
    url: str = Field(..., description="The URL of the website to scrape")

class RecyclingWebScraper(BaseTool):
    name: str = "recycling_web_scraper"
    description: str = "Scrapes websites for recycling service information"
    args_schema: type[BaseModel] = WebScraperSchema

    def _run(self, url: str) -> str:
        try:
            time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=REQUEST_TIMEOUT, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract relevant information
            content = {
                'title': soup.title.string if soup.title else '',
                'main_content': ' '.join([p.text for p in soup.find_all('p')])
            }
            
            return str(content)
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"

    async def _arun(self, url: str) -> str:
        raise NotImplementedError("Async not implemented")