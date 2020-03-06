from sklearn import tree
import pandas as pd
#Create the dataset
#create empty data frame
sport_df = pd.DataFrame()
#add outlook
sport_df['Outlook'] = ['sunny', 'sunny',
'overcast', 'rainy', 'rainy', 'rainy',
'overcast', 'sunny', 'sunny', 'rainy',
'sunny', 'overcast', 'overcast', 'rainy']
#add temperature
sport_df['Temperature'] = ['hot', 'hot',
'hot', 'mild', 'cool', 'cool', 'cool', 'mild',
'cool', 'mild', 'mild', 'mild', 'hot', 'mild']

#add humidity
sport_df['Humidity'] = ['high', 'high', 'high',
'high', 'normal', 'normal', 'normal', 'high',
'normal', 'normal', 'normal', 'high', 'normal',
'high']
#add windy
sport_df['Windy'] = ['false', 'true', 'false', 'false',
'false', 'true', 'true', 'false', 'false', 'false', 'true',
'true', 'false', 'true']
#finally add play
sport_df['Play'] = ['no', 'no', 'yes', 'yes', 'yes',
'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

#Print/show the new data
#print(sport_df)
#อยากรู้ว่า df มีชื่อ column อะไรบ้าง
dc = sport_df['Outlook']

df2 = sport_df.ix[:, 'Temperature':'Humidity']

df3 = sport_df.iloc [0:3, 1:4]

dc4 = sport_df[['Outlook', 'Humidity', 'Play']]

dc5 = sport_df[(sport_df['Outlook']=='sunny') & ((sport_df['Temperature']=='hot') | (sport_df['Windy']=='false'))]

sport_df.columns
sport_df.keys
sport_df.info()
sport_df.describe()
#เปลี่ยนเป็นตัวเลข -> dummies
one_hot_data = pd.get_dummies(sport_df[ ['Outlook', 'Temperature', 'Humidity', 'Windy'] ])
one_hot_data = pd.get_dummies(sport_df.iloc[:, 0:4])

clf = tree.DecisionTreeClassifier()
# ใช้ผลเฉลย Play
clf_train = clf.fit(one_hot_data , one_hot_data['Play'])
# outlook sun temp = hot himo norm wind false
#ป้อนข้อมูลให้ตรงกับ clf_train
#แต่ต้องจัด format ให้ตรงกับ traing 1 แถว มีกี่ column one_hot_data
unlabed_day = [0,0,1,0,1,0,1,1,1,0]
prediction = clf_train.predict([unlabed_day])
#prediction = clf_train.predict([[0,0,1,0,1,0,0,1,1,0], [0,1,0,1,0,0,0,1,1,0], [0,0,1,1,0,0,1,0,1,0]])
prediction


 import pydotplus
 from IPython.display import Imag
Export/Print a decision tree in DOT format. 
 print(tree.export_graphviz(clf_train, None))
Create Dot Data 
 dot_data= tree.export_graphviz(clf_train, out_file=None, feature_names=list(one_hot_data.columns.values), class_names=['Not_Play', 'Play'], rounded=True, filled=True) #Gini decides which attribute/feature should be placed at the root node, which features will act as internal nodes or leaf nodes #Create Graph from DOT data graph = pydotplus.graph_from_dot_data(dot_data)
 Show graph 
Image(graph.create_png())








