## This document is used to classify the value of PANAS which be collected by survey.
#Positive Affect Score: Add the scores on items 1, 3, 5, 9, 10, 12, 14, 16, 17, and 19. 
#Scores can range from 10 – 50, with higher scores representing higher levels of positive affect.
#Mean Scores: 33.3 (SD±7.2)
#Negative Affect Score: Add the scores on items 2, 4, 6, 7, 8, 11, 13, 15, 18, and 20. 
#Scores can range from 10 – 50, with lower scores representing lower levels of negative affect.
#Mean Score: 17.4 (SD ± 6.2)

import pandas as pd
import matplotlib.pyplot as plt

def real_PANAS_score():
	data = pd.read_csv('StudentLife_Dataset/Outputs/panas.csv')
	data = data.fillna(value = 0) # Use 0 to fill the Nan

	### Select type of 'pre'
	data1 = data.groupby(['type']) # use groupby to group 'type' column
	data_pre = data1.get_group('pre') # get_group to select elements of 'pre'
	# input the number of users which haven't the data
	lose_pre = []
	tester_pre = data_pre['uid']
	p_pre = 0
	for i in range(0,60):
		if i<10:
			t1 = 'u0' + str(i)
		else:
			t1 = 'u' + str(i)
		#judge
		if tester_pre.iat[p_pre] != t1:
			lose_pre.append(t1)
		else:
			p_pre = p_pre+1
	# print(lose_pre)

	##Positive Affect and Negative Affect of pre
	# list the column names of two elements (not all elements in paper exist in dataset-- 18 out of 20)
	positive_list = ['Interested','Strong','Enthusiastic','Proud','Alert','Inspired','Determined ','Attentive','Active ']
	negative_list = ['Distressed','Upset','Guilty','Scared','Hostile ','Irritable','Nervous','Jittery','Afraid ']
	positive_score = data_pre[positive_list].sum(axis =1)
	negative_score = data_pre[negative_list].sum(axis =1)
	# data_pre['positive_score'] = data_pre[positive_list].sum(axis =1) --insert to dataframe will result in SettingWithCopyWarning
	# data_pre['negative_score'] = data_pre[negative_list].sum(axis =1)
	posi_thd = positive_score.median() # use median value as threshold
	nega_thd = negative_score.median()

	class_Positive = [] # store the classification of each user
	for i in range(len(positive_score)):
		if positive_score[i] <= posi_thd:
			class_Positive.append(0)
		else:
			class_Positive.append(1)
	# print(class_Positive)
	class_Negative = [] # store the classification of each user
	for i in range(len(negative_score)):
		if negative_score[i] <= nega_thd:
			class_Negative.append(0)
		else:
			class_Negative.append(1)
	# print(class_Negative)

	#Positive
	# plt.plot(data_pre['uid'], positive_score,'o')
	# plt.hlines(posi_thd, 0, len(data_pre['uid']), colors = 'r')
	# plt.title('Positive Affect Score')
	# plt.xlabel('uid')
	# plt.ylabel('The score of Positive')
	# plt.show()

	# Negative 
	plt.plot(data_pre['uid'], negative_score,'o')
	plt.hlines(nega_thd, 0, len(data_pre['uid']), colors = 'r')
	plt.title('Negative Affect Score')
	plt.xlabel('uid')
	plt.ylabel('The score of Negative')
	plt.show()

real_PANAS_score()