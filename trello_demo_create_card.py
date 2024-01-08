import requests
import dotenv
import os

dotenv.load_dotenv()


reqUrl = f"https://api.trello.com/1/cards"

query_parameters = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": "6579d6eb8b2f72513c4a97cc",
    "name": "Giftshop",
}  

response = requests.post(reqUrl, params = query_parameters)

print(response.status_code)
print(response.text)