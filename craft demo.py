import requests
import json
import csv

DEFAULT_API_ENDPOINT = "https://www.travel-advisory.info/api"
DATA_FILE = "data.json"

def save_api_response(url, filename):
    response = requests.get(url)  # Doing API call

    if response.status_code == 200:  # Checking if the call was successful
        data = response.json()  # Extract the response as JSON

        with open(filename, 'w') as file:
            json.dump(data, file)  # Dumping JSON data to file
        print(f"API response saved to {filename} successfully.")
    else:
        print("API call failed, Error Code.", response.status_code)

def query_data(filename):
    try:
        with open(filename, 'r') as file:
            data_dict = json.load(file)  # Load the data from JSON file
    except FileNotFoundError:
        data_dict = None

    if not data_dict:
#       print("Unable to locate data file, Making a new API call.")
        choice = input("Unable to locate data file, Making a new API call to get new data? (y/n): ")

        if choice.lower() == "y":
            api_url = input("Enter the API endpoint URL (or press Enter for default): ")
            api_url = api_url if api_url else DEFAULT_API_ENDPOINT
            save_api_response(api_url, filename)

query_data(DATA_FILE)

with open('data.json') as file:
    data = json.load(file)
while True:
    method = input("Enter 'M' to input manually or 'F' to load from a file: ").strip().lower()
    if method == 'm':
        # Manual input
        iso_alpha2_list = input("Enter country codes (separated by commas): ").split(",")
        break
    elif method == 'f':
        # File input
        filename_csv = input("Enter the name of your CSV file: ")
        try:
            with open(filename_csv, 'r') as file:
                reader = csv.reader(file)
                iso_alpha2_list = list(reader)
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
    else:
        print("Invalid input. Please try again.")

# Find and print the country names
for iso_alpha2 in iso_alpha2_list:
    iso_alpha2 = iso_alpha2.strip().upper()
    if iso_alpha2 in data['data']:
        country_name = data['data'][iso_alpha2]['name']
        print(f"{iso_alpha2}: {country_name}")
    else:
        print(f"{iso_alpha2}: Country not found, Please check if country code is correct")