import joblib
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
data= joblib.load('features_fourishing.pkl')#读取feature
y=joblib.load('output_flourishing.pkl')#读取output（flourishing）
y=np.array(y)
data=np.array(data)
data=data.T

#分割训练集
x_train=data[:35]
y_train=y[:35]
x_test=data[35:]
y_test=y[35:]

DT = tree.DecisionTreeClassifier(criterion='entropy',random_state=0)
DT.fit(x_train,y_train)
predict_dt=DT.predict(x_test)
#预测

acc=accuracy_score(y_test,predict_dt)
print(acc)



