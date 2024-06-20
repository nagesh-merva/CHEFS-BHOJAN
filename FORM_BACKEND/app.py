from flask import Flask, make_response, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os
import random

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "https://chefs-bhojan.vercel.app"}}, supports_credentials=True)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secure_default_key')

client = MongoClient(
    'mongodb+srv://nagesh:nagesh2245@mywebsites.btvk61i.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['Crob_orders']
Deatils = db['orders']

@app.route('/', methods=['GET', 'POST'])
def index():
    response = make_response(render_template('index.html'))
    response.headers['Permissions-Policy'] = 'interest-cohort=()'
    return response

@app.route('/api/save_form_data', methods=['POST', 'OPTIONS'])
def save_form_data():

    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'https://chefs-bhojan.vercel.app')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        print("Handled OPTIONS request with CORS headers.")
        return response, 200

    data = request.get_json()
    print("Received form data:", data)

    new_order = {
        'name': data['name'],
        'phone': data['phone'],
        'date_created': datetime.utcnow(),
    }
    Deatils.insert_one(new_order)
    response = jsonify({'message': 'Data saved successfully'})
    response.headers.add('Access-Control-Allow-Origin', 'https://chefs-bhojan.vercel.app')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def get_weighted_value():
    values = [10, 20, 40]
    probabilities = [0.5, 0.4, 0.1]
    return random.choices(values, probabilities)[0]

@app.route('/api/get_discount_value', methods=['GET'])
def get_value():
    value = get_weighted_value()
    response = jsonify({'value': value})
    response.headers.add('Access-Control-Allow-Origin', 'https://chefs-bhojan.vercel.app')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

if __name__ == '__main__':
    app.run()
