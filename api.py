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


class TodoSimple(Resource):
    def get(self, todo_id):
        pass

    def delete(self, todo_id):
        return '', 204


class TodoList(Resource):
    def get(self):
        schema = TodoSchema()
        result = schema.dump(todos, many=True)
        return result

    def post(self):
        test = request.get_json();
        todo = Todo(test['id'], test['text'], test['done'])
        todos.append(todo)
        schema = TodoSchema()
        result = schema.dump(todo)
        return result


api.add_resource(TodoSimple, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')
if __name__ == '__main__':
    app.run(debug=True)
