import requests
import pytest

BASE_URL = "https://reqres.in/api"
def test_login_without_password():
    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": "peter@klaven"},
        timeout=15
    )

    assert response.status_code == 400

    body = response.json()

    assert "error" in body

    print("Test 4 passed: Missing password handled correctly")
