import requests
import json

# Finance statements endpoints list
FUNCTIONS = ['BALANCE_SHEET', 'CASH_FLOW', 'EARNINGS', 'INCOME_STATEMENT', 'TIME_SERIES_DAILY']

# For loop through each finance statement within the list to extract API data and save it as json file
for item in FUNCTIONS:
    try:
        url = f'https://www.alphavantage.co/query?function={item}&symbol=GOOG&apikey=E1CXMWH297VO9QOF' # type: ignore
        response = requests.get(url)
        data = response.json()
    except:
        print('Error: ', response.status_code)

    with open(f'./json_files/{item}.json', 'x') as json_file:
        json.dump(data, json_file, indent=4)
