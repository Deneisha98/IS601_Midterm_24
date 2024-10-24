import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            logger.error("Division by zero error")
            raise ValueError("Cannot divide by zero")
        return a / b

def repl():
    calculator = Calculator()
    logger.info("Starting REPL")
    while True:
        command = input("Enter a command ('exit' to quit): ").strip().lower()
        if command == 'exit':
            logger.info("Exiting REPL")
            break
        try:
            parts = command.split()
            if len(parts) == 3:
                a, operation, b = float(parts[0]), parts[1], float(parts[2])
                if operation == '+':
                    result = calculator.add(a, b)
                elif operation == '-':
                    result = calculator.subtract(a, b)
                elif operation == '*':
                    result = calculator.multiply(a, b)
                elif operation == '/':
                    result = calculator.divide(a, b)
                else:
                    print("Unknown operation")
                    continue
                print(f"Result: {result}")
                logger.info(f"Performed {operation} on {a} and {b} with result {result}")
            else:
                print("Invalid command format")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
