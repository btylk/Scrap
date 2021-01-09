from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
CORS(app)

class testResource(Resource):
    def get(self):
        return {"data": "Hello World"}
api.add_resource(testResource, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)

from app import routes