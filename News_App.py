import requests
import json
query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-09&sortBy=publishedAt&apiKey=28cac576bb6c411a9c12103a141e34c2"
r= requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("___________________________________________________________________________________________________")


# import requests

# try:
#     response = requests.get('https://www.google.com')
#     if response.status_code == 200:
#         print("Request successful")
#     else:
#         print("Request failed with status code:", response.status_code)
# except requests.exceptions.RequestException as e:
#     print("An error occurred:", e)

