import requests
import dotenv
import os

dotenv.load_dotenv()

board_id = os.getenv("TRELLO_BOARD_ID")

reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"


query_parameters = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "cards": "open",
    "card_fields": "id,name",
}

response = requests.get(reqUrl, params=query_parameters)
response_json = response.json()

cards = []
for trello_list in response_json:
  for card in trello_list['cards']:
    cards.append(card)

print(cards)