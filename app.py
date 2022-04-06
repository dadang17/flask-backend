import json
from os import abort
from flask import Flask, jsonify, request

app = Flask(__name__)

db = [
    {
        'id': '101',
        'title': 'Brainstorm Platform',
        'detail': 'First step to implement your charming plan',
        'from': 'irfams',
    },
    {
        'id': '102',
        'title': 'What the food?!',
        'detail': 'Show us iftar schedule',
        'from': 'irfams',
    },
]


@app.route('/')
def index():
   response = db
   return jsonify({'response': response})


@app.route('/<id>', methods=['GET'])
def fetch_by_id(id):
   idea = [row for row in db if (row['id'] == id)]

   if len(idea) == 0:
      abort(404)

   response = idea
   return jsonify({'response': response})


@app.route('/add', methods=['POST'])
def create():
   record = {
       'id': request.json['id'],
       'title': request.json['title'],
       'detail': request.json['detail'],
       'from': request.json['from'],
   }

   db.append(record)
   response = record
   return jsonify({'response': response})


@app.route('/<id>', methods=['PUT'])
def edit(id):
   idea = [row for row in db if (row['id'] == id)]

   if 'title' in request.json:
      idea[0]['title'] = request.json['title']

   if 'title' in request.json:
      idea[0]['detail'] = request.json['detail']

   if 'title' in request.json:
      idea[0]['from'] = request.json['from']

   response = idea[0]
   return jsonify({'response': response})


@app.route('/<id>', methods=['DELETE'])
def delete(id):
   idea = [row for row in db if (row['id'] == id)]

   if len(idea) == 0:
      abort(404)

   db.remove(idea[0])
   response = {
       'msg': "delete success!",
       'idea': idea[0]
   }
   return jsonify({'response': response})


app.run()
