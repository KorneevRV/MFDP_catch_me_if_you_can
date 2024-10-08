import pytest
import requests
from datetime import datetime

from tests.cases import user_cases


# Адрес API
api_url = 'http://app:8080/'
# Определение тестовых юзеров
users = user_cases()


# Тестирование регистрации и авторизации
class TestAuth:

    @pytest.mark.parametrize(
        ['username', 'email', 'password'],
        [
            (user['username'], user['email'], user['password'])
            for user in users
        ]
    )
    def test_signup(self, username, email, password):
        endpoint_url = '/user/signup'
        url = api_url + endpoint_url
        response = requests.post(
            url,
            params={
                "username": username,
                "email": email,
                "password": password
            }
        )
        assert response.status_code == 200
        assert response.json() == {"message": "User successfully registered!"}

    @pytest.mark.parametrize(
        ['email', 'password'],
        [
            (user['email'], user['password'])
            for user in users
        ]
    )
    def test_signin(self, email, password):
        endpoint_url = '/user/signin'
        url = api_url + endpoint_url
        response = requests.post(
            url,
            params={
                "email": email,
                "password": password
            }
        )
        response_json = response.json()
        assert response.status_code == 200
        assert "access_token" in response_json
        assert "token_type" in response_json
        assert response_json["token_type"] == "Bearer"


# Тестирование эндпоинтов, полагающихся на токен
@pytest.mark.parametrize(
    'token',
    [(user['token']) for user in users]
)
class TestTokenRelated:

    def test_auth(self, token):
        endpoint_url = '/user/auth/'
        url = api_url + endpoint_url + token
        response = requests.get(url)
        assert response.status_code == 200
        assert isinstance(response.json(), int)

    def test_get_history(self, token):
        endpoint_url = '/user/get_history/'
        url = api_url + endpoint_url + token
        response = requests.get(url)
        assert response.status_code == 200
        history = response.json()
        assert isinstance(history, list)
        for item in history:
            assert isinstance(item.get("request_id"), int)
            assert isinstance(item.get("vacancy_name"), str)
            assert isinstance(item.get("vacancy_description"), str)
            assert isinstance(item.get("salary_from"), (int, float, type(None)))
            assert isinstance(item.get("salary_to"), (int, float, type(None)))
            assert isinstance(item.get("timestamp"), str)
            try:
                datetime.fromisoformat(item["timestamp"])
            except ValueError:
                assert False, "timestamp format is invalid"

    def test_process_request(self, token):
        endpoint_url = '/ml/process_request/'
        url = api_url + endpoint_url
        response = requests.post(
            url,
            params={
                "token": token,
                "name": "Data Scientist",
                "description": "We are looking for a Data Scientist"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "salary_from" in data
        assert "salary_to" in data
        assert isinstance(data["salary_from"], (int, float))
        assert isinstance(data["salary_to"], (int, float))
