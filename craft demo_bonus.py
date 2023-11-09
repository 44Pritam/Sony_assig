import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

url = "https://www.travel-advisory.info/api"

@app.route('/health', methods=['GET'])
def health_check():
    return "API is up and running!"

@app.route('/diag', methods=['GET'])
def trigger_health_check():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'Health check triggered, Looks Good ', 200
        else:
            return f'Health check failed with status code: {response.status_code}', 500
    except requests.exceptions.RequestException as e:
        return f'An error occurred during the health check: {str(e)}', 500

@app.route('/convert', methods=['GET'])
def print_iso_alpha2_and_name():
    with open('data.json') as file:
        data = json.load(file)
    result = []
    for country_code, country_data in data.items():
        iso_alpha2 = country_data.get('iso_alpha2')
        name = country_data.get('name')
        result.append({"iso_alpha2": iso_alpha2, "name": name})

    return jsonify(result)

if __name__ == '__main__':
    app.run()
