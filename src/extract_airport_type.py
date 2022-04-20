import pandas as pd
import numpy as np

data_1 = pd.read_csv('../data/AP_Data/airports.csv', delimiter = ',')
df1 = pd.DataFrame(data_1)

data_2 = pd.read_csv('../data/AP_Data/airport-frequencies.csv', delimiter = ',')
df2 = pd.DataFrame(data_2)

df1['Large Airport'] = np.where(df1['type'] == 'small_airport', True, False)
df1['Medium Airport'] = np.where(df1['type'] == 'medium_airport', True, False)
df1['Small Airport'] = np.where(df1['type'] == 'small_airport', True, False)

df1.drop(df1.index[df1['type'] == 'closed'], inplace=True)

#if np.where(df1['id'] == '6528'):
#    print(df2.loc[[6528]])

#print (df1[1:2]['id'] == df2.iloc[1:2]['id2'])
#some_date = df.iloc[1:2]['Date']  #
print (df1['id'])
