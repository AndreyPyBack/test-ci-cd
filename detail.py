import requests
url_login = 'http://127.0.0.1:8000/api/token/'
# Учетные данные пользователя
credentials = {
    'username': 'admin',
    'password': 'admin'
}

# Отправка POST запроса для получения токена
response = requests.post(url_login, data=credentials)
tokens = response.json()
print(tokens)
# Вывод ответа сервера
access_token = tokens['access']  # Получаем access токен
print(access_token)
# Заголовки для последующих запросов
headers = {
    'Authorization': f'Bearer {access_token}'
}
# URL API, который вы определили
url = 'http://127.0.0.1:8000/api/comments/create/'

# Данные для отправки в POST-запросе
data = {
    'product': 1,  # ID продукта, к которому относится комментарий
    'text': 'Отличный товар!'  # Текст комментария
}

# Заголовки запроса

# Отправка POST-запроса
response = requests.post(url, json=data, headers=headers)

# Вывод ответа от сервера
print(response.status_code)
print(response.json())
