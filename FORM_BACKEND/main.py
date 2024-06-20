from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secure_default_key')

CORS(app, supports_credentials=True, allow_headers="*", origins="*", methods=["OPTIONS", "POST"])

client = MongoClient(
    'mongodb+srv://nagesh:nagesh2245@mywebsites.btvk61i.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['Crob_orders']
orderslist = db['orders']

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
    orderslist.insert_one(new_order)
    print(data)
    return jsonify({'status': 'success', 'message': 'Form data saved successfully'}), 200

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/api/get_discount_value', methods=['GET'])
def get_value():
    value = get_weighted_value()
    return jsonify({'value': value})
