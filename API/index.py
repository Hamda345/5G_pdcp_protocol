from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['pdcp_database']
collection = db['pdcp_logs']

@app.route('/log', methods=['POST'])
def log_data():
    """Endpoint to log PDCP data."""
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    collection.insert_one(data)
    return jsonify({"message": "Data logged successfully"}), 201

@app.route('/log', methods=['GET'])
def get_logs():
    """Endpoint to retrieve PDCP logs."""
    logs = list(collection.find({}, {'_id': 0}))
    return jsonify(logs), 200

if __name__ == '__main__':
    app.run(debug=True)
