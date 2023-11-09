
# Sony Assignment readme
## Purpose

This script is user were spending lot of time for looking for Country code in the api data goal is to fetch more details in less time. 

## API Endpoint

The program uses an API to fetch country data, including other information. The default API endpoint is `https://www.travel-advisory.info/api`, but users can provide a different endpoint if required.

## Data Storage

The program saves the API response to a JSON file named `data.json`. If the file is not found, it prompts the user to make a new API call to fetch fresh data.

## User Input

Users can choose to input country codes manually or load them from a CSV file. The program validates the input and displays the corresponding country names based on the provided country codes.

## Requirements 
Make sure you have python packages like requests, CSV, json installed, if not run. 
```shell
pip install <Package Name>
```
## Usage

1. Run the program, in python or use shell command ```python3 craft demo.py```
2. Choose either manual input (`M`) or file input (`F`).
3. If selecting manual input, enter the country codes separated by commas.
4. If selecting file input, enter the name of the CSV file.
5. The program will display the country names based on the provided country codes and the selected language.

Feel free to modify the code and customize it according to your needs.

