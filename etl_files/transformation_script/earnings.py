import json
import pandas as pd
from pandas_gbq import to_gbq

with open('/home/revson/Projects/Invest_Wise/project_directory/json_files/EARNINGS.json') as json_file:
  data = json.load(json_file)
  data = data['quarterlyEarnings']
  df = pd.DataFrame(data)
  
for col in df.columns:
  if col == 'fiscalDateEnding' or col == 'reportedDate':
    pass
  else:
    df[col] = df[col].astype(float)
    
project_id = 'investwise-417720'
table_id = 'company_data.earnings'

to_gbq(
    df,
    project_id=project_id,
    destination_table=table_id,
    if_exists='append'
)
