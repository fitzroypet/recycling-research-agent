# Recycling Services Research Agent

An AI-powered research tool that collects and analyzes information about recycling services in different locations using Crew AI. The tool generates detailed reports in both Word and Excel formats.

## Features

- **AI-Powered Research**: Uses GPT-4 to gather and analyze recycling service information
- **Multi-Agent System**: Employs specialized agents for research and analysis
- **Automated Report Generation**: Creates structured Word documents and Excel spreadsheets
- **Location-Based Research**: Can research any specified location
- **Data Validation**: Ensures accuracy and completeness of collected information
- **Rich Formatting**: Professional document formatting with custom styles and sections

## Project Structure

```
recycling-research-agent/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── researcher.py
│   └── analyzer.py
├── formatters/
│   ├── __init__.py
│   ├── document_formatter.py
│   └── excel_formatter.py
├── tools/
│   ├── __init__.py
│   ├── web_scraper.py
│   └── search_tool.py
├── utils/
│   ├── __init__.py
│   └── data_parser.py
├── output/
│   ├── recycling_analysis_*.docx
│   └── recycling_metrics_*.xlsx
├── main.py
├── requirements.txt
└── .env
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/fitzroypet/recycling-research-agent.git
cd recycling-research-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the application:
```bash
python main.py
```

## Usage

The agent will:
1. Research recycling services for the specified location
2. Analyze the collected information
3. Generate a detailed Word document report
4. Create an Excel spreadsheet with structured data
5. Save both files in the `output` directory

## Output Files

The tool generates two types of files:
- **Word Document** (`recycling_analysis_[Location].docx`): 
  - Comprehensive analysis report
  - Executive summary
  - Facility details
  - Recommendations
  - Comparative analysis

- **Excel Spreadsheet** (`recycling_metrics_[Location].xlsx`):
  - Structured facility data
  - Contact information
  - Operating hours
  - Accepted materials
  - Special requirements

## Dependencies

- crewai>=0.14.1
- langchain>=0.1.0
- langchain-openai>=0.0.2
- python-docx>=0.8.11
- openpyxl>=3.1.2
- pandas>=2.0.0
- rich>=13.7.0
- python-dotenv>=1.0.0
- (See requirements.txt for complete list)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Crew AI](https://github.com/joaomdmoura/crewAI)
- Powered by OpenAI's GPT-4
- Uses DuckDuckGo for web searches

## Author

Fitzroy Petgrave

## Support

For support, please open an issue in the GitHub repository. 