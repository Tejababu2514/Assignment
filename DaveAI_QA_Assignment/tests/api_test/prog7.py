import requests
import pytest

BASE_URL = "https://reqres.in/api"
def test_invalid_user():
    response = requests.get(
        f"{BASE_URL}/users/23",
        timeout=15
    )

    assert response.status_code == 404

    print("Test 3 passed: Invalid user handled correctly")
