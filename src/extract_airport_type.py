import pandas as pd
import numpy as np

print("Programe start")

#Load data from files 
data_1 = pd.read_csv('../data/AP_Data/airports_test.csv', delimiter = ',')
df1 = pd.DataFrame(data_1)
data_2 = pd.read_csv('../data/AP_Data/airport_frequencies_test.csv', delimiter = ',')
df2 = pd.DataFrame(data_2)

#Extract each 'type of airport into its own column and create a list for those columns
df1['Large Airport'] = np.where(df1['type'] == 'large_airport', True, False)
large_airports= df1['Large Airport'].tolist()
df1['Medium Airport'] = np.where(df1['type'] == 'medium_airport', True, False) 
medium_airports= df1['Medium Airport'].tolist()
df1['Small Airport'] = np.where(df1['type'] == 'small_airport', True, False)
small_airports= df1['Small Airport'].tolist()

#Remove closed airports
df1.drop(df1.index[df1['type'] == 'closed'], inplace=True)

#create two lists of ids
airportWithComFreqIDs= df2['id'].tolist()
airportIDs= df1['id'].tolist()

id= []

#Remove airports not on the list of communication freqs
for idf2, rowIdf2 in df2.iterrows(): 
  for idf1, rowIdf1 in df1.iterrows(): 
    if rowIdf1['id'] == rowIdf2['id']:
      id.append(rowIdf1['id'])


newData= {
  "id": id,
  "Small Airports": small_airports,
  "Medium Airports": medium_airports, 
  "Large Airports": large_airports
}


df3= pd.DataFrame(newData)

df3['Comfreq'] = np.where((df3['id'] == df2['id'])


df3.to_csv("data3.csv")

#f3 = pd.DataFrame() 



# Build new data

#df3 = pd.DataFrame(df1['Small Airport'], df1['Medium Airport']) 


# Match each airport in all catagories with its communication freq

#communicationFreq= []

#for index, row in df2.iterrows():
#  idWithComFreq= df2.iloc[index][1]
#  for index, row in df1.iterrows(): 
#    idToMatchIdWithComFreq= idWithComFreq= df1.iloc[index][0]
#    if idWithComFreq == idToMatchIdWithComFreq:
#      communicationFreq.append(df2.iloc[index])

print("Programe end")
