import requests
import pytest
from data import Data
from helpers import *


@pytest.fixture
def generate_new_courier():
    login = create_random_courier_login(),
    password = create_random_courier_password(),
    name = create_random_courier_name()
    new_courier = {
        'login': login,
        'password': password,
        'name': name
    }
    return new_courier