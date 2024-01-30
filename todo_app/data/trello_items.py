import requests

import os



def add_item(title):
    reqUrl = f"https://api.trello.com/1/cards"

    query_parameters = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_TODO_LIST_ID"),
        "name": title
        }  

    response = requests.post(reqUrl, params = query_parameters)

    print(response.status_code)
    print(response.text)