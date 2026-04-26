import requests

BASE_URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
METHODS = ["GET", "POST", "PUT", "DELETE"]

# 1. HTTP-запрос БЕЗ параметра method

print("1. GET-запрос без параметра method")

response = requests.get(BASE_URL)
print(f"Статус: {response.status_code}")
print(f"Ответ:  {response.text}")

# 2. HTTP-запрос не из списка — HEAD

print("2. HEAD-запрос (метод не из списка)")

response = requests.head(BASE_URL, params={"method": "HEAD"})
print(f"Статус: {response.status_code}")
print(f"Ответ:  '{response.text}'")

# 3. Запрос с правильным значением method

print("3. POST-запрос с правильным method='POST'")

response = requests.post(BASE_URL, data={"method": "POST"})
print(f"Статус: {response.status_code}")
print(f"Ответ:  {response.text}")

# 4. Перебор всех сочетаний метод × значение параметра

print("4. Перебор всех сочетаний реального метода и параметра method")
print(f"{'Реальный метод':<16} {'Параметр method':<16} {'Статус':<8} {'Ответ'}")

anomalies = []

for real_method in METHODS:
    for param_method in METHODS:


        if real_method == "GET":
            response = requests.get(BASE_URL, params={"method": param_method})
        elif real_method == "POST":
            response = requests.post(BASE_URL, data={"method": param_method})
        elif real_method == "PUT":
            response = requests.put(BASE_URL, data={"method": param_method})
        elif real_method == "DELETE":
            response = requests.delete(BASE_URL, data={"method": param_method})

        result_line = (
            f"{real_method:<16} {param_method:<16} "
            f"{response.status_code:<8} {response.text}"
        )
        print(result_line)

        methods_match = (real_method == param_method)
        server_ok = "success" in response.text.lower() or '"' + param_method + '"' in response.text

        if methods_match and not server_ok:
            anomalies.append(f"[АНОМАЛИЯ] {real_method} + '{param_method}' — совпадают, но сервер против!")
        elif not methods_match and server_ok:
            anomalies.append(f"[АНОМАЛИЯ] {real_method} + '{param_method}' — НЕ совпадают, но сервер доволен!")

print("Найденные аномалии:")

if anomalies:
    for a in anomalies:
        print(a)
else:
    print("Аномалий не обнаружено (проверьте ответы вручную выше)")