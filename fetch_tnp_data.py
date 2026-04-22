# fetch_tnp_data.py

import requests
import json

# Configuration for Socrata API
API_ENDPOINT = "https://data.cityofchicago.org/resource/your_endpoint_here.json"
API_KEY = "your_api_key_here"

def fetch_data():
    headers = {
        'X-App-Token': API_KEY
    }
    response = requests.get(API_ENDPOINT, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == '__main__':
    data = fetch_data()
    if data:
        with open('tnp_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print("Data successfully written to tnp_data.json")
