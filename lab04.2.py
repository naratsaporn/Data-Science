import pandas as pd 
brics = pd.read_csv('brics.csv', index_col = 0)


#list
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] 
dr=[True, False, False, False, True, True, True]
cpc= [809, 731, 588, 18, 200, 70, 45]
#dictionary
my_dict = {'country' : names ,
           'drives_right' : dr ,
           'cars_per_cap' : cpc
           }

cars = pd.DataFrame(my_dict)
row_labels= ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

cars[0:3]
cars[:3]
cars[:-4]

cars.loc['RU']
cars.iloc[4]
cars.loc[['RU','AUS']]

cars.loc['IN','cars_per_cap']
cars.loc[['IN','RU'], 'cars_per_cap']
cars.iloc[[3,4],2]
cars.loc[['IN','RU'], ['cars_per_cap','country']]

cars.loc[:,'cars_per_cap','country']

type(cars.loc[:,'cars_per_cap']) #serise
type(cars.loc[:,['cars_per_cap']]) #array

test1 = cars.loc[:,['cars_per_cap']]

