import requests
import json

FUNCTIONS = ['BALANCE_SHEET', 'CASH_FLOW', 'EARNINGS', 'INCOME_STATEMENT', 'TIME_SERIES_DAILY']

for item in FUNCTIONS:
    try:
        url = f'https://www.alphavantage.co/query?function={item}&symbol=GOOG&apikey=E1CXMWH297VO9QOF' # type: ignore
        response = requests.get(url)
        data = response.json()
    except:
        print('Error: ', response.status_code)

    with open(f'/home/revson/Projects/Invest_Wise/project_directory/json_files/{item}.json', 'x') as json_file:
        json.dump(data, json_file, indent=4)
