import json
import datetime
import pandas as pd
from pandas_gbq import to_gbq

with open('/home/revson/Projects/Invest_Wise/project_directory/json_files/TIME_SERIES_DAILY.json') as json_file:
  data = json.load(json_file)
  daily_data = data['Time Series (Daily)']
  df_data = []

  for date, daily_data in daily_data.items():
    row = {
        'stock_price_date': date,
        'open': daily_data['1. open'],
        'high': daily_data['2. high'],
        'low': daily_data['3. low'],
        'close': daily_data['4. close'],
        'volume': daily_data['5. volume']
    }

    df_data.append(row)

df = pd.DataFrame(df_data)

# Data types definition
def set_columns_dtypes():
  df['stock_price_date'] = pd.to_datetime(df['stock_price_date'])
  df['stock_price_date'] = df['stock_price_date'].apply(lambda x: x.strftime("%Y-%m-%d"))
  df['open'] = df['open'].astype(float)
  df['high'] = df['high'].astype(float)
  df['low'] = df['low'].astype(float)
  df['close'] = df['close'].astype(float)
  df['volume'] = df['volume'].astype(int)

set_columns_dtypes()

# Upload table to GBQ
project_id = 'investwise-417720'
table_id = 'stock_data.time_series_daily'
to_gbq(
    df,
    table_id,
    project_id,
    if_exists='append'
)
