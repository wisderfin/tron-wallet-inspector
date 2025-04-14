import requests
from time import sleep
from settings import settings

def test_post_and_get_wallet_info():
    sleep(5)
    wallet_data = {'address': 'THyaBXgRJpBGYdeGpdVktXDmqEmDgY2vMV'} # адрес валиден
    url = f'http://api:{settings.API_PORT}/'

    # Отправляем POST запрос
    response = requests.post(url, json=wallet_data)
    assert response.status_code == 200
    assert 'address' in response.json()
    assert 'balance' in response.json()
    assert 'energy' in response.json()
    assert 'bandwidth' in response.json()


    # Тестируем GET запрос
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
