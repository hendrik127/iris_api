"""
Tests for the Iris API endpoints.
"""

from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


def test_read_data_not_found():
    """
    Test case for GET /v1/iris endpoint when no data is found.

    This test checks that the endpoint returns a 404 status
    code when attempting to retrieve iris data that doesn't
    exist (e.g., endpoint `/v1/iris` not defined).
    """
    response = client.get("/v1/iris")
    assert response.status_code == 404


def test_get_outlier_irises():
    """
    Test case for GET /v1/iris/outliers endpoint.

    This test checks that the endpoint returns
    a list of irises marked as outliers
    with a 200 status code, and verifies that all
    returned irises have `is_outlier` set to True.
    """
    response = client.get("/v1/iris/outliers")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for iris in data:
        assert iris.get('is_outlier') is True, f"Iris with id {iris.get('id')} is not marked as an outlier"


def test_get_cleaned_irises():
    """
    Test case for GET /v1/iris/cleaned endpoint.

    This test checks that the endpoint returns a list of irises
    that are not marked as outliers
    with a 200 status code, and verifies that all returned
    irises have `is_outlier` set to False or None.
    """
    response = client.get("/v1/iris/cleaned")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for iris in data:
        assert iris.get('is_outlier') in [False, None], f"Iris with id {iris.get('id')} is marked as an outlier"


def test_get_irises_by_species():
    """
    Test case for GET /v1/iris/{species} endpoint.

    This test checks that the endpoint returns
    a list of irises of a specified species
    or all species with a 200 status code,
    and verifies that all returned irises match the specified species.
    """
    # Test for a specific species
    species = "setosa"
    response = client.get(f"/v1/iris/{species}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for iris in data:
        species_actual = iris.get('species').lower()
        species_expected = species.lower()
        assert species_actual == species_expected, f"Iris with id {iris.get('id')} does not belong to species {species}"

    # Test for all species
    response = client.get("/v1/iris/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for iris in data:
        assert iris.get('species'), "Species information missing"
