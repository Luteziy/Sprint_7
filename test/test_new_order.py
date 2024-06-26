import requests
import allure
import pytest
from data import Data
import json
from data import OrderData


class TestNewOrder:
    @allure.title('Проверка создания заказов с самокатом разного цвета')
    @allure.description(
        'Успешное создание заказа, код 201. Должна быть возможность заказать самокат одного/двух цветов или не указывая цвет')
    @pytest.mark.parametrize('order', [
        OrderData.order_1_scooter_black, OrderData.order_2_scooter_grey,
        OrderData.order_3_scooter_grey_and_black, OrderData.order_4_scooter_no_color
    ])
    def test_new_order(self, order):
        orders = json.dumps(order)
        response = requests.post(Data.Url_create_order, data=orders)
        assert response.status_code == 201 and 'track' in response.text
