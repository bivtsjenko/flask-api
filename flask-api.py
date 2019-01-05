from flask import Flask, request
from flask_restful import Resource, Api
from security import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    @jwt_required
    def get(self, name):
        item = next(list(filter(lambda x: x['name'] == name, items)), None)
        return {'item' : item}, 200 if Item else 404
    
    def post(self, name):
        if next(list(filter(lambda x: x['name'] == name, items)), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return{'items': items}
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5001, debug=True)