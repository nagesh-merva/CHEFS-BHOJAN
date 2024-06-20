from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secure_default_key')

CORS(app, resources={r"/api/*": {"origins": "https://chefs-bhojan.vercel.app", "supports_credentials": True}})

client = MongoClient(
    'mongodb+srv://crob0008:GYfLnhxdJgeiOTPO@chefsbhojan.oxsu9gm.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['FORMDATACOLLECTION']
Deatils = db['CONTACTS']

@app.route('/save_form_data', methods=['POST', 'OPTIONS'])
def save_form_data():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': 'https://example.com',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Credentials': 'true'
        }
        return '', 200, headers
    data = request.get_json()
    print("Received form data:", data)

    new_order = {
        'name': data['name'],
        'phone': data['phone'],
        'date_created': datetime.utcnow(),
    }
    Deatils.insert_one(new_order)
    response = jsonify({'status': 'success', 'message': 'Form data saved successfully'})
    response.headers.add('Access-Control-Allow-Origin', 'https://chefs-bhojan.vercel.app')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response, 200

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/get_discount_value', methods=['GET'])
def get_value():
    value = get_weighted_value()
    return jsonify({'value': value})
