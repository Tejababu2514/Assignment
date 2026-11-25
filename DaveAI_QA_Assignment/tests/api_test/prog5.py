
import requests
import pytest

BASE_URL = "https://reqres.in/api"


def test_get_all_users():
    response = requests.get(
        f"{BASE_URL}/users",
        params={"page": 2},
        timeout=15
    )

    # Validate status code
    assert response.status_code == 200

    # Convert response into JSON
    body = response.json()

    # Validate response content
    assert body["page"] == 2
    assert len(body["data"]) > 0
    assert "email" in body["data"][0]

    print("Test 1 passed: Users retrieved successfully")
