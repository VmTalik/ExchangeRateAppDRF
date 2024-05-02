import requests
import json


def fetch_exchange_rate():
    response = None
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    except requests.ConnectionError as err:
        print('Ошибка подключения', err)
    except requests.Timeout as err:
        print('Ошибка таймаута', err)
    except requests.RequestException as err:
        print('Ошибка запроса', err)

    l = []
    date = response.json()['Timestamp'].split('T1')[0]
    valutes = response.json()['Valute']
    for valute in valutes:
        l.append({"charcode": valute, "date": date, "rate": valutes[valute]["Value"]})
    json_data = json.dumps(l)

    try:
        requests.post('http://localhost:8000/rate/', headers={'Content-Type': 'application/json'}, data=json_data)
    except requests.RequestException as err:
        print('Ошибка при отправлении данных\n', err)
