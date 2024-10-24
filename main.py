import os
import logging
from dotenv import load_dotenv

# Loading environment variables from .env
load_dotenv()

# Configure logging based on env variable 
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

# Simple REPL
def repl():
    logger.info("Starting calculator REPL")
    while True:
        command = input("Enter a command ('exit' to quit): ").strip().lower()
        if command == 'exit':
            logger.info("Exiting REPL")
            break
        else:
            logger.info(f"Command received: {command}")
            print(f"Command: {command}")

if __name__ == "__main__":
    repl()
