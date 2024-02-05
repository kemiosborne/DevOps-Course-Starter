from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import add_item, complete_item, get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    cards = get_items()

    return render_template("index.html", items = cards)


@app.route('/add-item', methods = ["POST"])
def create():
    todo_title = request.form.get('todo-name')

    add_item(todo_title)
    return redirect('/')

  
@app.route('/complete-item/<item_id>', methods = ["POST"])
def complete(item_id):
    complete_item(item_id)

    return redirect('/')
