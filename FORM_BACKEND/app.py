from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from datetime import datetime
import os
import random

app = Flask(__name__)

# Enable CORS for all routes with credentials support
CORS(app, supports_credentials=True)

client = MongoClient(
    'mongodb+srv://crob0008:GYfLnhxdJgeiOTPO@chefsbhojan.oxsu9gm.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['FORMDATACOLLECTION']
Details = db['CONTACTS']

# Example of allowing specific origins dynamically
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin', '*'))
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/api/save_form_data', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def save_form_data():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200
    
    data = request.get_json()
    print("Received form data:", data)

    new_order = {
        'name': data['name'],
        'phone': data['phone'],
        'date_created': datetime.utcnow(),
    }
    Details.insert_one(new_order)
    return jsonify({'status': 'success', 'message': 'Form data saved successfully'}), 200

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/api/get_discount_value', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_value():
    value = get_weighted_value()
    return jsonify({'value': value})

