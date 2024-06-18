class Data:
    valid_login = 'Kosmo2020'
    valid_password = '1234'
    valid_name = 'Kosmo'
    valid_courier = {'login': 'Kosmo2020', 'password': '1234', 'name': 'Kosmo'}
    no_name_courier = {'login': 'Kosmo2020', 'password': '1234'}
    wrong_password = {'login': 'Kosmo2020', 'password': '123456789'}

    Url_main_page = 'https://qa-scooter.praktikum-services.ru/'
    Url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    Url_create_login = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    Url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
class OrderData:
    order_1_scooter_black = {
        'name': 'Альбус',
        'lastName': 'Дамблдор',
        'address': 'Беговая улица, 5',
        'metroStation': 'Беговая',
        'phone': '+79998887766',
        'rentTime': '3',
        'deliveryDate': '25-06-2024',
        'comment': 'До Хогвартса доеду?',
        'color': ['BLACK']
    }

    order_2_scooter_grey = {
        'name': 'Том',
        'lastName': 'Ридл',
        'address': 'проспект Малиновского, 5',
        'metroStation': 'Динамо',
        'phone': '+79998886677',
        'rentTime': '4',
        'deliveryDate': '20-06-2024',
        'comment': 'Ну, Дамблдор! Ну, погоди!!',
        'color': ['GREY']
    }

    order_3_scooter_grey_and_black = {
        'name': 'Гарри',
        'lastName': 'Поттер',
        'address': 'проспект Буденова, 5',
        'metroStation': 'Сокол',
        'phone': '+79998885588',
        'rentTime': '5',
        'deliveryDate': '30-06-2024',
        'comment': 'Ну вы там пока катайтесь, а я, пожалуй, огневиски бахну, главное сбежать от Джинни',
        'color': ['BLACK', 'GREY']
    }

    order_4_scooter_no_color = {
        'name': 'Джинни',
        'lastName': 'Уизли',
        'address': 'проспект Жукова, 5',
        'metroStation': 'Хорошово',
        'phone': '+79998883322',
        'rentTime': '6',
        'deliveryDate': '29-06-2024',
        'comment': 'Гарри, подожди, а как же я!!',
        'color': []
    }