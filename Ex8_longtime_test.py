import requests
import time

BASE_URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1. Создаём задачу (без токена)
response = requests.get(BASE_URL)
data = response.json()

token = data["token"]
seconds = data["seconds"]

print(f"Задача создана. Токен: {token}, ждать: {seconds} сек.")

# 2. Запрос ДО готовности задачи
response = requests.get(BASE_URL, params={"token": token})
data = response.json()

print(f"Статус ДО: {data['status']}")
assert data["status"] == "Job is NOT ready", "Ожидали 'Job is NOT ready'!"

# 3. Ждём нужное количество секунд
time.sleep(seconds)

# 4. Запрос ПОСЛЕ готовности задачи
response = requests.get(BASE_URL, params={"token": token})
data = response.json()

print(f"Статус ПОСЛЕ: {data['status']}")
assert data["status"] == "Job is ready", "Ожидали 'Job is ready'!"
assert "result" in data, "Поле result отсутствует!"

print(f"Результат: {data['result']}")