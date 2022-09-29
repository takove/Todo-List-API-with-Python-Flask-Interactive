from flask import Flask, jsonify, request, json

app = Flask(__name__)

todos = [
    {"label": "First Task", "done": False},
    {"label": "Second Task", "done": False},
    {"label": "Third Task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position-1)
    json_text = jsonify(todos)
    print('This is the position to delete: ', position)
    return json_text



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)