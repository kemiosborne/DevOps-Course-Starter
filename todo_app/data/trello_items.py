import requests

import os

def get_items():
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
            card['status'] = trello_list['name']
            cards.append(card)

    return cards


def add_item(title):
    reqUrl = f"https://api.trello.com/1/cards"

    query_parameters = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_TODO_LIST_ID"),
        "name": title,
    }  

    response = requests.post(reqUrl, params = query_parameters)

    print(response.status_code)
    print(response.text)


def complete_item(item_id):
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"

    query_parameters = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_DONE_LIST_ID"),
    }  

    response = requests.put(reqUrl, params = query_parameters)

    print(response.status_code)
    print(response.text)
