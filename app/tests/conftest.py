"""
Test Setup for FastAPI Application

This module sets up fixtures for testing a FastAPI application using pytest.
It imports necessary modules and defines a fixture `client` that provides
a `TestClient` instance for making HTTP requests to the
FastAPI application defined in `main.app`.
"""
from collections.abc import Generator
from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """Fixture for FastAPI test client.

    This fixture sets up a `TestClient` instance using the FastAPI application
    defined in `main.app`. It yields the client instance,
    allowing HTTP request to be made to the FastAPI application during tests.

    Yields:
        TestClient: A `TestClient` instance configured with `main.app`.

    """
    with TestClient(app) as c:
        yield c
