from flask import Flask
from flask_restful import Api
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
api = Api(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5001)