from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items
import requests
import dotenv
import os

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()

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

    return render_template("index.html", items = cards)



@app.route('/add-item', methods = ["POST"])
def create():
    todo_title = request.form.get('todo-name')

    reqUrl = f"https://api.trello.com/1/cards"

    query_parameters = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": "6579d6eb8b2f72513c4a97cc",
        "name": todo_title,
    }  

    response = requests.post(reqUrl, params = query_parameters)

    add_item(todo_title)
    return redirect('/')


  
