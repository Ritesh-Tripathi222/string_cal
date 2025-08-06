# String Calculator TDD Kata

This repository contains a Python implementation of the String Calculator TDD Kata. The goal of this exercise is to practice Test-Driven Development (TDD) by building a simple string calculator with an incremental, test-first approach.

## Features

The String Calculator supports the following features:
1.  Handles an empty string, returning 0.
2.  Handles a single number.
3.  Handles two comma-separated numbers.
4.  Handles any amount of comma-separated numbers.
5.  Handles newlines as a delimiter between numbers (e.g., "1\n2,3").
6.  Supports custom delimiters. The format is `//[delimiter]\n[numbers...]` (e.g., `//;\n1;2`).
7.  Throws an exception for negative numbers. The exception message includes all the negative numbers found.

## Setup and Usage

### Prerequisites
*   Python 3.x

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ritesh-Tripathi222/string_cal.git
    cd string_cal
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    *On Windows, use `venv\Scripts\activate`*

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Tests

To run the tests, execute the following command from the root of the project:
```bash
pytest
```

This will run the full test suite and confirm that all features are working correctly.
