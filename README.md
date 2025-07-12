# Python API Test Automation Framework
Hi this is Sayantan Mukherjee. Thank you for visiting to my GitHub repository. This project is a robust **Pytest-based API automation framework** built in Python.  
It supports parameterized testing, JSON-based data management, logging, and dynamic HTML report generation.

## Project Structure
PythonFrameworkAPI/
├── tests/
│ ├── test_weather_api.py # Weather API tests
│ └── test_user_api.py # User API tests
├── data/
│ ├── test_data.json # Test input data (currently I have kept weather and users)
│ └── config.json # Configuration (base URLs, api key and other important data)
├── reports/
│ └── report_<timestamp>.html # Auto-generated HTML report
├── logs/
│ └── test_run_<timestamp>.log # Execution logs
├── conftest.py # Fixtures, logging setup, test data helpers
├── api_client.py # Custom HTTP client using requests
├── pytest.ini # Pytest configuration
└── README.md # Project documentation

## Features
- **Pytest + Parametrization** for clean, data-driven tests
- **API Client Abstraction** (GET, POST, etc.) via `api_client.py`
- **Fixtures** for setup/teardown and shared utilities
- **JSON-driven test data & config** loading from `data/`
- **Automatic HTML Report Generation**
- **Timestamped Logs** stored under `logs/`
- **Graceful Assertion Handling** with optional xfail
- **Test Dependencies** via `pytest-dependency`

## How to Run Tests
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run all tests:
   ```bash
   pytest
   
5. Run specific test:
   ```bash
   pytest tests/test_weather_api.py

## Logging & Reports
Logs saved in logs/test_run_<timestamp>.log
HTML reports in reports/report_<timestamp>.html

## Requirements
Python 3.7+
pytest
requests
pytest-html
pytest-dependency

You can install them via:
   ```bash
      pip install -r requirements.txt
```

## Future Enhancements
 CI Integration (GitHub Actions, Jenkins)
 Response schema validation
 Token-based authentication support
 Retry logic on failures

## Contributing
Feel free to raise issues or PRs for improvements, bug fixes, or new test scenarios.

## Author
- Name: Sayantan Mukherjee
- GitHub: https://github.com/sayantanviky
- LinkedIn: https://www.linkedin.com/in/sayantan-mukherjee-9975b3b7
- YouTube: @sayantanmukherjee8294
