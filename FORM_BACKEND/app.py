from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os
import random

app = Flask(__name__)

CORS(app ,allow_headers="*", resources={r"/api/*": {"origins": "https://chefs-bhojan.vercel.app"}} , supports_credentials=True)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secure_default_key')

client = MongoClient(
    'mongodb+srv://crob0008:GYfLnhxdJgeiOTPO@chefsbhojan.oxsu9gm.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['FORMDATACOLLECTION']
Deatils = db['CONTACTS']

@app.route('/api/save_form_data', methods=['POST', 'OPTIONS'])
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
    Deatils.insert_one(new_order)
    response = jsonify({'message': 'Data saved successfully'})
    return response

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/api/get_discount_value', methods=['GET'])
def get_value():
    value = get_weighted_value()
    return jsonify({'value': value})
