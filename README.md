# API - тесты для сервиса "Яндекс самокат"

[Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

## Структура проекта </summary>

<details> <summary> О проекте  </summary>
Яндекс самокат позволяет арендовать самокат в Москве и МО.
</details>

<details> <summary>Структура репозитория</summary>
Директория test - файлы с тестами. Для каждой проверки свой файл

Файл data - данные тестовые данные

Файл url - адреса сервисов

Файл helpers - генерация рандомных тестовых данных

Директория allure - JSON-файлы с результатами тестов

Файл requirements - внешние зависимости тестов

Файл README - руководство
</details>

<details> <summary> Покрытие   </summary>
test_courier_login.py - аутентификация курьера

test_create_courier.py - проверка создания аккаунта курьера

test_new_order.py - проверка создания заказа

test_order_list.py - проверка списка заказов
</details>

<details> <summary> Запуск тестов </summary>
pip install -r requirments.txt - запуск зависимостей

pytest -v - Запуск всех тестов
</details>

<details> <summary> Отчет тесторования </summary>
allure serve allure_results - Allure-отчет
</details>