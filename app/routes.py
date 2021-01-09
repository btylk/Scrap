from app import app
from flask_restful import Api, Resource

@app.route('/')
@app.route('/index')
def index():
    return "Hello Flask World!"


