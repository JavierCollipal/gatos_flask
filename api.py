from flask import Flask
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)
CORS(app)


class Todo:
    def __init__(self, id, text, done):
        self.id = id
        self.text = text
        self.done = done


class TodoSchema(Schema):
    id = fields.Int()
    text = fields.Str()
    done = fields.Bool()


todos = []


def get_todo_index(id: int):
    for i, e in enumerate(todos):
        if e.id == id:
            return i
    return False


class TodoSimple(Resource):
    def get(self, todo_id):
        pass

    def delete(self, todo_id):
        todo_index = get_todo_index(todo_id)
        if todo_index is False:
            return 'no existe el todo'

        return 204

    def put(self, todo_id):
        data = request.get_json()
        todo_index = get_todo_index(todo_id)
        if todo_index is False:
            return 'no existe el todo'
        todos[todo_index] = Todo(data['id'], data['text'], data['done'])
        return 200


class TodoList(Resource):
    def get(self):
        schema = TodoSchema()
        result = schema.dump(todos, many=True)
        return result

    def post(self):
        test = request.get_json()
        todo = Todo(test['id'], test['text'], test['done'])
        todos.append(todo)
        schema = TodoSchema()
        result = schema.dump(todo)
        return result, 201

    def delete(self):
        todos = []
        return 200


api.add_resource(TodoSimple, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)
