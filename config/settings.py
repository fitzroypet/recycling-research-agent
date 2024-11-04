import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Installing now...")
    import subprocess
    subprocess.check_call(["pip", "install", "python-dotenv"])
    # Add a small delay to ensure the package is fully installed
    import time
    time.sleep(1)
    from dotenv import load_dotenv
    load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Scraping Settings
REQUEST_TIMEOUT = 30  # seconds
RATE_LIMIT_DELAY = 2  # seconds between requests

# Data Storage
DATA_DIR = "data"

# Verify API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")