from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS , cross_origin
import os
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secure_default_key')

cors = CORS(app, resources= {r'/*':{'origins' : 'https://chefs-bhojan.vercel.app'}})

client = MongoClient(
    'mongodb+srv://crob0008:GYfLnhxdJgeiOTPO@chefsbhojan.oxsu9gm.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['FORMDATACOLLECTION']
Deatils = db['CONTACTS']

@app.route('/api/save_form_data', methods=['POST', 'OPTIONS'])
@cross_origin()
def save_form_data():

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': 'https://chefs-bhojan.vercel.app',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return ('', 204, headers)
    
    data = request.get_json()
    print("Received form data:", data)

    new_order = {
        'name': data['name'],
        'phone': data['phone'],
        'date_created': datetime.utcnow(),
    }
    Deatils.insert_one(new_order)
    return jsonify({'status': 'success', 'message': 'Form data saved successfully'}), 200

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/api/get_discount_value', methods=['GET'])
@cross_origin()
def get_value():
    value = get_weighted_value()
    return jsonify({'value': value})
