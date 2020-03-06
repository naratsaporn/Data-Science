import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
col_names = ['att1','att2','att3','att4','att5','att6','att7','att8','label']
pima = pd.read_csv("D:/2562/Data Science (DTI 511)/exam_ml_04.csv",header=None,names=col_names)

#select เฉพาะบาง columns มาเป็น traning data
att_cols = ['att5','att6','att7','att8']

#select date in pima ด้วย att_cols มาเป็น train data
X = pima[att_cols] #ใช้ X ใหญ่เพราะเป็น matrix
#select column ที่เป็นผลเฉลย
y = pima['label']

#เราจะแบ่ง X y เป็น traning data และ test data

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=1)

#clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=5)
clf = clf.fit(X_train, y_train)

#เมื่อได้ classifier clf มาแล้วเอามา classify X_test เก็บผลใน y_pred
y_pred = clf.predict(X_test)
#ตอนนี้ ai บอกว่าคน 231 คนใน X_test มีคนไหนเป็น หรือ ไม่เป็นเบาหวานแล้ว
#คำถามคือ เมื่อเทียบกับผลเฉลย ถูกเท่าไหร่

from sklearn import metrics
print("Accuracy : ", metrics.accuracy_score(y_test, y_pred))

#ในกรณีที่อยากรู้ค่า evaluation metric หลายตัววัด
from sklearn.metrics import classification_report,confusion_matrix
print('Classificaiton Report : ')
print(classification_report(y_test,y_pred))

print('Confusion Matrix Report : ')
print(confusion_matrix(y_test,y_pred))