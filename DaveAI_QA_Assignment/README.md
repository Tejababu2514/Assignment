# DaveAI QA Engineer Assignment

## Project Overview

This project contains automated API and website UI tests developed using Python.

### Part 1 – API Testing

- API tested: ReqRes
- Framework: Pytest
- HTTP library: Requests
- Coverage: Successful responses, response content validation and error handling.

### Part 2 – Website UI Testing

- Website: https://www.iamdave.ai/
- Automation tool: Selenium WebDriver
- Framework: Pytest
- Browser: Google Chrome
- Coverage: Homepage loading, heading validation, Book Demo navigation and form interactions.

## Project Structure

```text
DaveAI_QA_Assignment/
│
├── tests/
│   ├── api_tests.py
│   └── ui_tests.py
│
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3
- Google Chrome
- PyCharm or another Python IDE

## Installation

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## How to Run API Tests

```bash
python -m pytest tests/api_tests.py -v -s
```

## How to Run UI Tests

```bash
python -m pytest tests/ui_tests.py -v -s
```

## How to Run All Tests

```bash
python -m pytest tests/ -v -s
```

## Test Design Choices

- Pytest is used to organize and execute test cases.
- Requests is used for HTTP API testing.
- Selenium WebDriver is used for browser automation.
- Assertions validate expected results.
- Pytest fixtures manage browser setup and teardown.
- Explicit waits are used to handle dynamic website elements.

## Test Execution Results

Actual execution results will be recorded after running the test suite.
