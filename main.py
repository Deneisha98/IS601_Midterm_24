import os
import logging
import importlib
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.plugins = {}
        self.load_plugins()

    def add(self, a, b):
        result = a + b
        self._save_history("add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history("subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history("multiply", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            logger.error("Division by zero error")
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save_history("divide", a, b, result)
        return result

    def _save_history(self, operation, a, b, result):
        new_record = {"operation": operation, "operand1": a, "operand2": b, "result": result}
        self.history = self.history.append(new_record, ignore_index=True)

    def save_history(self, file_name="history.csv"):
        self.history.to_csv(file_name, index=False)
        logger.info(f"History saved to {file_name}")

    def load_history(self, file_name="history.csv"):
        self.history = pd.read_csv(file_name)
        logger.info(f"History loaded from {file_name}")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        logger.info("History cleared")

    def show_history(self):
        print(self.history)

    def load_plugins(self):
        plugin_folder = 'plugins'
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                plugin_name = filename[:-3]  # Strip off '.py'
                module = importlib.import_module(f'plugins.{plugin_name}')
                self.plugins[plugin_name] = module
                logger.info(f"Loaded plugin: {plugin_name}")

    def execute_plugin(self, plugin_name, *args):
        if plugin_name in self.plugins:
            try:
                result = self.plugins[plugin_name].run(*args)
                return result
            except Exception as e:
                logger.error(f"Error in plugin {plugin_name}: {e}")
        else:
            logger.error(f"Plugin {plugin_name} not found")
            return None

def repl():
    calculator = Calculator()
    logger.info("Starting REPL")
    while True:
        command = input("Enter a command ('exit' to quit, 'history' to show, 'save' to save history, 'load' to load history, 'clear' to clear history): ").strip().lower()
        if command == 'exit':
            logger.info("Exiting REPL")
            break
        elif command == 'history':
            calculator.show_history()
        elif command == 'save':
            calculator.save_history()
        elif command == 'load':
            calculator.load_history()
        elif command == 'clear':
            calculator.clear_history()
        elif command.startswith('plugin'):
            parts = command.split()
            plugin_name = parts[1]
            args = parts[2:]
            result = calculator.execute_plugin(plugin_name, *args)
            if result is not None:
                print(f"Plugin result: {result}")
        else:
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
