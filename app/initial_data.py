"""
Initialization Script for Database and Initial Data

This script initializes the database by creating tables and optionally
populating initial data. It provides functions for initializing the database
structure and a main entry point for execution.

"""

import logging
from core.database import create_tables

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """
    Initialize the database by creating necessary tables.

    This function calls the create_tables function imported from core.database
    to create database tables required for the application's operation.
    """
    create_tables()


def main() -> None:
    """
    Main function to initialize the database and log the process.

    This function logs the start and completion of the database
    initialization process. It calls the init() function to
    perform database initialization.
    """
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
