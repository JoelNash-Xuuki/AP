import pandas as pd



# Read the csv file
data = pd.read_csv('data/PeopleTrainingDate.csv')
pd.set_option('display.max_rows', data.shape[0]+1)

dataSorted = pd.to_datetime(data['Updated'],format='%d/%m/%Y')
#data.sort_values(by = 'Updated', ascending = True, inplace = True)

# Print it out if you want
print(dataSorted)




