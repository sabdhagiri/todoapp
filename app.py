from flask import Flask, render_template, request, jsonify, redirect
from config import Config
from models import db, TodoModel
import os
import datetime

app = Flask(__name__)
app.config.from_object(Config())


db.init_app(app)

@app.route('/')
def index():
    todos = todo()
    print(todos)
    return render_template('index.html', todos=todos)

@app.route('/todo', methods=['GET','POST'])
def todo():
    if request.method == "GET":
        todos = {"todos": []}
        result = TodoModel.query.all()
        for todo in result:
            todos['todos'].append(todo.json())
        print(jsonify(todos))
        return todos
    elif request.method == "POST":
        post_body = request.form
        print(type(post_body))
        print(post_body)
        todo = TodoModel(title=post_body.get('title'), description=post_body.get('description'))
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

@app.route('/healthz')
def health(foo):
    return datetime.datetime.now()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 