from langchain_community.tools import DuckDuckGoSearchRun
from config.settings import RATE_LIMIT_DELAY
import time
from pydantic import BaseModel, Field

class SearchSchema(BaseModel):
    query: str = Field(..., description="The search query to look up")

class CustomSearchTool(DuckDuckGoSearchRun):
    name: str = "web_search"
    description: str = "Search the web for recycling information"
    args_schema: type[BaseModel] = SearchSchema

    def _run(self, query: str) -> str:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        return super()._run(query) 