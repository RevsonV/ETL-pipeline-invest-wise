import pandas as pd
import sqlite3
import json

with open('/home/revson/Projects/Invest_Wise/project_directory/json_files/BALANCE_SHEET.json') as json_file:
  data = json.load(json_file)
  data = data['quarterlyReports']
  df = pd.DataFrame(data)

for col in df.columns:
  if col == 'fiscalDateEnding' or col == 'reportedCurrency':
    pass
  else:
    df[col] = df[col].apply(lambda x: x.replace('None', '0')).astype(int)

conn = sqlite3.connect('/home/revson/Projects/Invest_Wise/project_directory/database.db')

df.to_sql(
    'balance_sheet',
    conn,
    if_exists='append'
)
