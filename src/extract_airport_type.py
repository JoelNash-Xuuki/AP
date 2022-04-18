import pandas as pd
import numpy as np

df = pd.read_csv('../data/AP_Data/airports.csv', delimiter = ',')
df2 = pd.read_csv('../data/AP_Data/airport-frequencies.csv', delimiter = ',')

df['Large Airport'] = np.where(df['type'] == 'small_airport', True, False)
df['Medium Airport'] = np.where(df['type'] == 'medium_airport', True, False)
df['Small Airport'] = np.where(df['type'] == 'small_airport', True, False)

df.drop(df.index[df['type'] == 'closed'], inplace=True)

if np.where(df['id'] == '6528' && df2['id'] == '6528'):
  print ('SAME')

