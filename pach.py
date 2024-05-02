import requests

url = 'http://127.0.0.1:8000/api/register/'


data = {
    "user": {
        "username": "newuse12r",
        "email": "newuser@example.com",
        "password": "securepassword123",
        "first_name": "New",
        "last_name": "User"
    },
    "bio": "Short biography here",
    "city": "YourCity"
}

# Отправка POST запроса с JSON данными
response = requests.post(url, json=data)

# Вывод текста ответа
print(response.text)

# Проверка кода состояния, чтобы определить результат запроса
if response.status_code == 201:
    print("Запрос успешно отправлен. Код состояния:", response.status_code)
else:
    print("Ошибка при отправке запроса. Код состояния:", response.status_code)
