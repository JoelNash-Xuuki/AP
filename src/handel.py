#import numpy as np
import pandas as pd

data = pd.read_csv('data/PeopleTrainingDate.csv', delimiter = ',')

data['Updated'] = pd.to_datetime(data['Updated'])

pd.set_option('display.max_rows',data.shape[0]+1)
data = data.sort_values(by='Updated',ascending=False)

print(data.Updated)
