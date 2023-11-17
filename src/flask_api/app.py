import json
from flask import Flask, jsonify

f = open('todos.json')
todos = json.load(f)
f.close()

f = open('users.json')
user_list = json.load(f)
f.close()

app = Flask(__name__)

@app.route("/")
@app.route("/users/")
def default():
    return jsonify(user_list)

@app.route("/users/<int:userid>")
def user(userid):
    return jsonify(user_list[userid-1])

@app.route("/users/<int:userid>/todos")
def usertodos(userid):
    filtered = []
    for todo in todos:
        if (todo["userId"]==userid-1):
            filtered.append(todo)
    return jsonify(filtered)

@app.route('/users/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    print(record)
    new_records = []
    return jsonify(record)

if __name__ == "__main__":
    app.run()
