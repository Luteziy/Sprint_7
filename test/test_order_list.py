import requests
import allure
from data import Data


class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order_list(self):
        response = requests.get(Data.Url_create_order)
        r = response.json()
        assert (r['orders'][0]['id'])