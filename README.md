# Selenium-Pytest Automation Framework

## Overview
A robust automation framework for web applications using Selenium and Pytest. Implements Page Object Model (POM), data-driven testing via JSON, and generates detailed HTML reports with screenshots on test failure.

## Features
- Pytest-based test execution
- Page Object Model (POM) structure
- Data-driven tests (JSON)
- HTML reports and screenshots on failure
- Parallel execution support
- Test markers for suite selection (smoke, regression, etc.)
- Supports Chrome and Firefox browsers, including headless mode

## Directory Structure
- `POM/` - Page Object Model classes
- `TestCases/` - Test scripts
- `StepDefinitions/` - BDD step definitions
- `Data/` - Test data files
- `Reports/` - Test reports and screenshots
- `utils/` - Utility functions
- `conftest.py` - Pytest fixtures and hooks
- `pytest.ini` - Pytest configuration

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run Tests
Run smoke tests on Chrome:
```bash
pytest -m smoke --browser_name chrome
