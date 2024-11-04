import pandas as pd
import logging
from typing import Dict, List

class ExcelFormatter:
    def __init__(self, location, recycling_data=None):
        self.location = location
        self.recycling_data = recycling_data
        self.sheets_data = {}
        
    def extract_metrics(self, content: str) -> Dict[str, List]:
        metrics = {
            'Programs': [],
            'Materials': [],
            'Gaps': [],
            'Recommendations': []
        }
        
        # Extract programs and materials
        sections = content.split('**')
        for i in range(0, len(sections), 2):
            if i + 1 < len(sections):
                section_title = sections[i].strip()
                section_content = sections[i + 1].strip()
                
                if "Executive Summary" in section_title:
                    # Extract programs and materials
                    for line in section_content.split('\n'):
                        if 'programs' in line.lower():
                            metrics['Programs'].append(line.strip())
                        if 'materials' in line.lower():
                            metrics['Materials'].append(line.strip())
                
                elif "Service Gaps" in section_title:
                    # Extract gaps
                    for line in section_content.split('\n'):
                        if line.strip().startswith('-'):
                            metrics['Gaps'].append(line.strip()[1:].strip())
                
                elif "Recommendations" in section_title:
                    # Extract recommendations
                    for line in section_content.split('\n'):
                        if line.strip().startswith('-'):
                            metrics['Recommendations'].append(line.strip()[1:].strip())
        
        return metrics
    
    def format_data(self, content: str):
        metrics = self.extract_metrics(content)
        
        # Create standard sheets
        self.sheets_data = {
            'Summary': pd.DataFrame({
                'Category': ['Programs', 'Materials', 'Gaps', 'Recommendations'],
                'Count': [
                    len(metrics['Programs']),
                    len(metrics['Materials']),
                    len(metrics['Gaps']),
                    len(metrics['Recommendations'])
                ]
            }),
            'Details': pd.DataFrame({
                'Category': ['Programs'] * len(metrics['Programs']) +
                           ['Materials'] * len(metrics['Materials']) +
                           ['Gaps'] * len(metrics['Gaps']) +
                           ['Recommendations'] * len(metrics['Recommendations']),
                'Description': metrics['Programs'] +
                             metrics['Materials'] +
                             metrics['Gaps'] +
                             metrics['Recommendations']
            })
        }
        
        # Add facilities sheet if we have structured data
        if self.recycling_data and self.recycling_data.facilities:
            facilities_data = []
            for facility in self.recycling_data.facilities:
                facilities_data.append({
                    'Name': facility.name,
                    'Address': facility.address,
                    'Contact': facility.contact or 'N/A',
                    'Materials': ', '.join(facility.materials_accepted),
                    'Hours': facility.operating_hours or 'N/A'
                })
            self.sheets_data['Facilities'] = pd.DataFrame(facilities_data)
    
    def save(self, filename: str) -> bool:
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                for sheet_name, df in self.sheets_data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            logging.info(f"Excel file saved successfully: {filename}")
            return True
        except Exception as e:
            logging.error(f"Error saving Excel file: {str(e)}")
            return False 