import pandas as pd
import numpy as np
brics = pd.read_csv("D:/2562/Data Science (DTI 511)/brics.csv" , index_col = 0)
 

brics["area"]     
brics.loc[:,"area"]
brics.iloc[: , "area"]
brics.iloc[:,2]

# selected data compare wiht condition
brics["area"] > 8
is_huge = brics["area"] > 8
brics[is_huge]    
    
# เชื่อมสองนิพธน์
brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)]
    
cars = pd.read_csv("D:/2562/Data Science (DTI 511)/cars.csv" , index_col = 0)   
dr = cars["drives_right"]    
sel = cars[dr]    
#8
sel = cars[cars["dvives_right"]]

cpc = cars["cars_per_cap"]
many_cars = cpc > 500
cars_maniac = cars[many_cars]
cars_maniac


between = np.logical_and(cpc > 100 , cpd < 500)
medium = cars[between]

error = 50
while error > 1 :
    error = error /4
    print(error)
    
offset = 8 
while offset ==0:
    print('correcting')
    offsrt = offset-1
    print('offset')
    
fam = [1.73 , 1.68 , 1.71 , 1.89]
fam[0]
for height in fam:
    print(height)
#index ชี้ตำแหน่ง
for index, height in enumerate(fam) :
    print("index is" + str(index) + ":" + height))
    #argument เป็น string ต้อง cast เป็น string
#13
areas = [11.2,18.0,20.0,10.75,9.50]
    for area in areas :
        print(area)
#14
    for index , a in enumerate(areas):
        print("room is" + str(index) + ":" + str(a))
        
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
    
house = [[ "hallway" , hall] ,
         [ "kitchen" , kit] ,
         [ "living room" , liv] ,
         [ "bedroom" , bed] ,
         [ "bathroom" , bath] ,
        ]]    
for room in house:
    print(room[0]+ "is" + str(room[1]) + "sqm" )

for room in house:
    for x in room:
        print(x)

world = {"afganistan" : 30.55 ,
         "albania" : 2.77,
         "algeria" : 39.21}

for name,pop  in world.items() :
    print(name + "--" + str(pop))
    
np_height = np.array([1.73,1.68,1.71,1.89])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])

meas = np.array([np_height,np_weight])

for val in meas:
    print(val)
    print("---")
    
for val in np.nditer(meas):
    print(val)
    print("--")

europe = {'spain' : 'madrid' , 'france' : 'paris'}

for key , value in europe.items() :
    print("the capital fo " + key + "is" + value)

np_baseball = np.transpose(meas)

for x in np.nditer(np_baseball) :
    print(x)
    print("-")


for lab , row in brics.iterrows() :
    print(lab)
    print(row)
    
row['capital']

for lab , row in brics.iterrows() :
    print(lab + ':' + row['cappital'])
    
for lab , row in brics.iterrows() :
    brics.loc[lab , 'name =_length'] = len(row['country'])
    
