import requests
import allure
import pytest
from data import Data
from helpers import create_random_courier_login, create_random_courier_password, create_random_courier_name


class TestCreateCourier:

    @allure.title('Проверка создания курьера с валидными данными')
    @allure.description('Проверяем, что код ответа 201')
    def test_create_courier(self):
        payload = {
            'login': create_random_courier_login(),
            'password': create_random_courier_password(),
            'name': create_random_courier_name()
        }
        response = requests.post(Data.Url_create_courier, data=payload)
        assert response.status_code == 201, response.json() == {'ok': 'True'}

    @allure.title('Проверка создания курьера с логином, который уже есть')
    @allure.description('Проверяем, что код ответа 409')
    def test_create_courier_same_login(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_courier_password(),
            'name': create_random_courier_name()
        }
        response = requests.post(Data.Url_create_courier, data=payload)
        response_2 = requests.post(Data.Url_create_courier, data=payload)
        assert response_2.status_code == 409, response.json() == {'message': 'Этот логин уже используется'}

    @allure.title('Проверка создания курьера, если обязательные поля не заполнены')
    @allure.description('Передаем данные с пустым логином и паролем(поочередно). Проверяем, что код ответа 400')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'pasword': create_random_courier_password(), 'name': create_random_courier_name()},
        {'login': create_random_courier_login(), 'pasword': '', 'name': create_random_courier_name()}
    ])
    def test_create_courier_with_empty_fields(self, empty_fields):
        response = requests.post(Data.Url_create_courier, data=empty_fields)
        assert response.status_code == 400, response.json() == {'message': 'Недостаточно данных для создания учетной записи'}