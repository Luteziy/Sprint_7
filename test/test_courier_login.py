import requests
import allure
import pytest
from data import Data, ResponseRequestMessage
from helpers import create_random_courier_login, create_random_courier_password


class TestCourierLogin:
    @allure.title('Проверка авторизации курьера')
    @allure.description('Код ответа 200, успешный запрос возвращает id')
    def test_courier_login(self, generate_new_courier):
        payload = generate_new_courier
        requests.post(Data.Url_create_courier, data=payload)
        response = requests.post(Data.Url_create_login, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка ошибки авторизации курьера, при невалидных данных')
    @allure.description('Код ответа 404, запрос с несуществующей парой логин пароль')
    @pytest.mark.parametrize('wrong_pass', [
        {'login': create_random_courier_login(), 'password': create_random_courier_password()}, Data.wrong_password
    ])
    def test_courier_login_no_valid_data(self, wrong_pass):
        response = requests.post(Data.Url_create_login, data=wrong_pass)
        assert response.status_code == 404, response.json() == ResponseRequestMessage.account_not_found

    @allure.title('Проверка ошибки авторизации курьера, при незаполненных полях логина и пароля')
    @allure.description('Код ответа 400')
    @pytest.mark.parametrize('empty', [
        {'login': '', 'password': create_random_courier_password()},
        {'login': create_random_courier_login(), 'password': ''}
    ])
    def test_courier_login_no_valid_data(self, empty):
        response = requests.post(Data.Url_create_login, data=empty)
        assert response.status_code == 400, response.json() == ResponseRequestMessage.not_enough_to_login