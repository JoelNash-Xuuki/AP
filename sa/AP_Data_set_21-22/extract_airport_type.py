import pandas as pd
import numpy as np

df = pd.read_csv('airports.csv', delimiter = ',')
df['Large Airport'] = np.where(df['type'] == 'small_airport', True, False)
df['Medium Airport'] = np.where(df['type'] == 'medium_airport', True, False)
df['Small Airport'] = np.where(df['type'] == 'small_airport', True, False)
print(df.head())


