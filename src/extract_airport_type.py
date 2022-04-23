import pandas as pd
import numpy as np

print("Programe start")

data_1 = pd.read_csv('../data/AP_Data/airports.csv', delimiter = ',')
df1 = pd.DataFrame(data_1)

data_2 = pd.read_csv('../data/AP_Data/airport-frequencies.csv', delimiter = ',')
df2 = pd.DataFrame(data_2)

df1['Large Airport'] = np.where(df1['type'] == 'small_airport', True, False)
df1['Medium Airport'] = np.where(df1['type'] == 'medium_airport', True, False)
df1['Small Airport'] = np.where(df1['type'] == 'small_airport', True, False)

df1.drop(df1.index[df1['type'] == 'closed'], inplace=True)
df1 = df1.reset_index()  # make sure indexes pair with number of rows

for index, row in df1.iterrows():
  airportID= row['id']
  for index, row in df2.iterrows():
    airportFreqRow= row['id2']
    if airportID == airportFreqRow: 
      print("Test")
      df1['Com Freq']= row['frequency_mhz']
      exit()

print("Programe end")

#index = df1.index
#number_of_rows = len(index) 

#for x in range(0, number_of_rows):

#df2ids= df2['id2'].to_string(index = False)


