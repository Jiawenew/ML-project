import joblib
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
# from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
# from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
data= joblib.load('features_fourishing.pkl')#读取feature
y=joblib.load('output_flourishing.pkl')#读取output（flourishing）
input_feature = np.array(data)
input_feature = input_feature.T
output_label = np.array(y)
# print(input_feature.shape)
# print(output_label.shape)


#part1 : use svm
# clf = svm.SVC(kernel='linear', C=1)

# clf_models=[KNeighborsClassifier(),SVC(),DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier()]
clf_model1 = KNeighborsClassifier()
# for model in clf_models:
cv_score = cross_val_score(clf_model1, input_feature, output_label, cv=5)
print(cv_score)
print(f'KNeighborsClassifier accuracy: {cv_score.mean():8.4f} (+/-{cv_score.std() * 2:8.4f})')

clf_model2 = SVC(kernel='linear', C=1)
cv_score = cross_val_score(clf_model2, input_feature, output_label, cv=5)
print(cv_score)
print(f'SVC accuracy: {cv_score.mean():8.4f} (+/-{cv_score.std() * 2:8.4f})')

clf_model3 = DecisionTreeClassifier(criterion='entropy',random_state=0)
cv_score = cross_val_score(clf_model3, input_feature, output_label, cv=5)
print(cv_score)
print(f'DecisionTreeClassifier accuracy: {cv_score.mean():8.4f} (+/-{cv_score.std() * 2:8.4f})')

clf_model4 = RandomForestClassifier(n_estimators=100, criterion='entropy',random_state=0)
cv_score = cross_val_score(clf_model4, input_feature, output_label, cv=5)
print(cv_score)
print(f'RandomForestClassifier accuracy: {cv_score.mean():8.4f} (+/-{cv_score.std() * 2:8.4f})')

clf_model5 = AdaBoostClassifier(n_estimators=100, random_state=0)
cv_score = cross_val_score(clf_model5, input_feature, output_label, cv=5)
print(cv_score)
print(f'AdaBoostClassifier accuracy: {cv_score.mean():8.4f} (+/-{cv_score.std() * 2:8.4f})')

#part2 : use iterators
# kf = KFold(n_splits = 5)
# for train, test in kf.split(input_feature):
#     print(f'{train.shape, test.shape}')
