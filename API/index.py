from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import subprocess
import sys

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['pdcp_database']
collection = db['pdcp_logs']

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Data logged successfully"}), 201

@app.route('/log', methods=['GET'])
def get_logs():
    logs = list(collection.find({}, {'_id': 0}))
    return jsonify(logs), 200

@app.route('/process_packet', methods=['POST'])
def process_packet():
    data = request.json
    if not data or 'ip_packet' not in data or 'sn_length' not in data:
        return jsonify({"error": "Invalid data provided"}), 400

    ip_packet = data['ip_packet']
    sn_length = data['sn_length']

    try:
        result = subprocess.run(
            [sys.executable, '../main.py', ip_packet, str(sn_length)],
            capture_output=True,
            text=True,
            check=True
        )
        return jsonify({"message": "Packet processed successfully", "output": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error processing packet: {e.stderr}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
