import requests



response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirects_count = len(response.history)
final_url = response.url

print(f"Количество редиректов: {redirects_count}")
print(f"Конечный URL: {final_url}")