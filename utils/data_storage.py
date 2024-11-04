import json
import os
from datetime import datetime
from config.settings import DATA_DIR
from models.recycling_data import RecyclingData

class DataStorage:
    @staticmethod
    def save_results(location: str, data: dict):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            
        filename = f"{DATA_DIR}/recycling_data_{location.lower().replace(' ', '_')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_results(location: str) -> RecyclingData:
        filename = f"{DATA_DIR}/recycling_data_{location.lower().replace(' ', '_')}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return RecyclingData(**json.load(f))
        return None 