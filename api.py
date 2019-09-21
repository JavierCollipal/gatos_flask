from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)
todos = []


class TodoSimple(Resource):
    def get(self):
        return jsonify(todos)

    def post(self):
        todos.append(request.json)
        return request.json


api.add_resource(TodoSimple, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
