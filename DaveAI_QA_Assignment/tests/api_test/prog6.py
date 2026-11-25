import requests
import pytest

BASE_URL = "https://reqres.in/api"
def test_get_single_user():
    response = requests.get(
        f"{BASE_URL}/users/2",
        timeout=15
    )

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == 2
    assert body["data"]["email"] == "janet.weaver@reqres.in"

    print("Test 2 passed: Single user retrieved successfully")
