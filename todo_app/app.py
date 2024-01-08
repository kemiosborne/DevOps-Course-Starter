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
    return render_template("index.html", items = items)

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


  
