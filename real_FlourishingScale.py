## this document is used to deal the FlourishingScale of Output
# Step 1: fill the data(use 0 to fill in the gap of data) -- Success
# Step 2: compute the scores of flourishing  -- Success
# Step 3: classify users and use mean value as threshold -- Success

import pandas as pd

def flourishing_Scale():
	data = pd.read_csv('StudentLife_Dataset/Outputs/FlourishingScale.csv')
	data_pre = data.iloc[0:46].copy() # select the data which type is 'pre' # if not copy, there is Hidden chaining
	#problem: why data_pre = data_pre.fillna(0, inplace =Ture) input  None --- inplace = True is 
	data_pre = data_pre.fillna(value = 0) #fill all Nan value with zero
	# data_pre1 = data_pre.replace('', 0, inplace =True)
	# print(data_pre.iloc[:, 2:9])

	# calculate the sum of score
	Sum_value = data_pre.iloc[:,2]
	for i in range(3,10):
		# data_pre['Sum_value'] = data_pre['Sum_value'] + data_pre.iloc[:,i]
		Sum_value = Sum_value + data_pre.iloc[:,i]
	data_pre['Sum_value'] = Sum_value # create new column Sum_value
	# print(data_pre['Sum_value'])

	## Min-max Scale
	data_sum = data_pre['Sum_value']
	sum_max = data_sum.loc[data_sum.idxmax()]
	sum_min = data_sum.loc[data_sum.idxmin()]
	# print(sum_max)
	valueD = sum_max-sum_min
	for i in range(0, 46):
		value_Scale = ((data_pre['Sum_value']-sum_min)/valueD)
	print(value_Scale)

	## the lost tester
	lose_tester = []
	tester = data_pre['uid']
	p = 0
	for i in range(0,60):
		if i<10:
			t1 = 'u0' + str(i)
		else:
			t1 = 'u' + str(i)
		#judge
		if tester.iat[p] != t1:
			lose_tester.append(t1)
		else:
			p = p+1
	print(lose_tester)

	## classification
	average = value_Scale.mean() # get the mean as threshold  ---- use median value as threshold??
	class_Num = [] # store the classification of each user
	for i in range(len(value_Scale)):
		if value_Scale[i] <= average:
			class_Num.append(0)
		else:
			class_Num.append(1)

	print(class_Num)


flourishing_Scale()