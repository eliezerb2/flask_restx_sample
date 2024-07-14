"""
Sample hello world REST application with Swagger
http://127.0.0.1:5000/hello?name=Your
Only works with classes
"""

# app.py
from flask import Flask, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='My API', description='A simple API')

item_model = api.model('Item', {
    'id': fields.Integer(description='The item unique identifier'),
    'name': fields.String(description='The item name')
})

@api.route('/api/items')
@api.doc(description="Get all items")
@api.marshal_with(item_model, as_list=True)
def get_items():
    """
    Get all items
    """
    items = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'}
    ]
    return items

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, request, jsonify
from flask_restx import Api, Namespace

app = Flask(__name__)
api = Api(app)

# Create a namespace
ns = Namespace('example', description='Example Namespace')

@api.route('/hello') #, methods=['GET']) # The main route
@ns.doc(description='Example Hello Endpoint', responses={200: 'OK'})
def hello():
    """Return hello to the name of the requester"""

    # name = request.args.get('name')
    # if not name:
    #     return jsonify({"error": "Name parameter is required"}), 400
    # return jsonify({"message": f"Hello, {name}!"})
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
'''