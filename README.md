# IS601_Midterm_24: Advanced Python Calculator

## Project Overview 
This is an advanced Python-based calculator application built for my IS601 midterm project. It supports arithmetic operations, history management, and dynamic plugin loading for extended functionalities via a command-line REPL interface.

## Calculator Feautures
- Basic Operations: Add, Subtract, Multiply, Divide.
- History Management: Calculation history stored using Pandas, with options to load, save, and clear history.
- Plugin System: Dynamically load commands (e.g., custom math functions) without modifying core code.
- Extendable Command System: Commands for operations like `add`, `subtract`, and more are modularized in the `commands` folder.

## Project Structure
- calculator/: Core functionality and REPL.
- commands/: Additional operations as plugins (e.g., `add`, `subtract`).
- tests/: Unit tests for the calculator and plugins.
- data/: Stores history in CSV format.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the REPL 
    python calculator/main.py

## Calculator function example: 
- Run commands like 3 + 5 or use plugin sqrt 16.
- Manage history with save, load, history, and clear commands.

## Running tests and Generating Coverage Report
- Run the following command to execute tests: 
    pytest
- To run the tests and generate a coverage report:  
    pytest --cov=calculator 
    
## Calculator Design Pattern
- Facade Pattern: Simplifies Pandas data management.
- Command Pattern: Structure for REPL commands.
- Plugin Pattern: Dynamically load plugins for extensibility.

## Environment Variables
Environment variables, configured through .env, control logging levels:
LOG_LEVEL: Sets log verbosity.
Example: LOG_LEVEL=INFO
    https://github.com/Deneisha98/IS601_Midterm_24/blob/main/calculator/main.py#L9 

## Logging Feature 
Logging is dynamically configured using environment variables. Logs include informational messages and error handling for debugging.
    https://github.com/Deneisha98/IS601_Midterm_24/blob/main/calculator/main.py#L36


## Error Handling
Implements LBYL and EAFP error-handling strategies:
LBYL: Checks for conditions like file existence before operations.
EAFP: Wraps potentially erroneous plugin loads in try/except blocks.
    https://github.com/Deneisha98/IS601_Midterm_24/blob/main/calculator/main.py#L66

## Video Demonstration
A short video demonstration that shows calculator usage, features, and REPL functionality.






