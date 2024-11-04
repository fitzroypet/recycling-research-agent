from models.recycling_data import RecyclingData, RecyclingFacility
from datetime import datetime
import re

class DataParser:
    @staticmethod
    def parse_facilities_from_text(text: str) -> RecyclingData:
        facilities = []
        
        # Look for facility information in the text
        # This regex pattern looks for facility-like information
        facility_pattern = r"(?i)(?:facility|center|location):\s*(.*?)(?=(?:facility|center|location):|$)"
        facility_matches = re.finditer(facility_pattern, text, re.DOTALL)
        
        for match in facility_matches:
            facility_text = match.group(1).strip()
            
            # Extract facility details
            name_match = re.search(r"(?i)name:\s*(.*?)(?=\n|$)", facility_text)
            address_match = re.search(r"(?i)address:\s*(.*?)(?=\n|$)", facility_text)
            contact_match = re.search(r"(?i)contact:\s*(.*?)(?=\n|$)", facility_text)
            materials_match = re.search(r"(?i)materials accepted:\s*(.*?)(?=\n|$)", facility_text)
            hours_match = re.search(r"(?i)hours:\s*(.*?)(?=\n|$)", facility_text)
            
            if name_match and address_match:
                facility = RecyclingFacility(
                    name=name_match.group(1).strip(),
                    address=address_match.group(1).strip(),
                    contact=contact_match.group(1).strip() if contact_match else None,
                    materials_accepted=materials_match.group(1).split(',') if materials_match else [],
                    operating_hours=hours_match.group(1).strip() if hours_match else None,
                    requirements=None,  # Could add more regex patterns for these
                    website=None
                )
                facilities.append(facility)
        
        return RecyclingData(
            location=text.split('\n')[0].replace('Recycling Services Analysis:', '').strip(),
            facilities=facilities,
            last_updated=datetime.now().strftime("%Y-%m-%d")
        ) 