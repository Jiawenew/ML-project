import pandas as pd
import time

#count the frequency of tester activity
def activity_frequency():
	act_fre_list = []
	# for i in range(0,60):
	# 	try:
	# 		data = pd.read_csv('StudentLife_Dataset/Inputs/data/activity/activity_u'+str(i).zfill(2)+'.csv',header = 0)
	# 	except:
	# 		continue
	data = pd.read_csv('StudentLife_Dataset/Inputs/data/activity/activity_u00.csv',header = 0)

	##pre_processing data
	data1 = data.groupby([' activity inference'])
	data_act = data.drop(data1.get_group(0).index) # remove 'activity inference = 0'
	data_timestamp = data_act['timestamp']
	count_time = 0 # storage the activity duration
	for i in range(len(data_timestamp)):
		if data_timestamp.iloc[i+1]-data_timestamp.iloc[i] == 3:
			count_time = count_time + 3
		if data_timestamp.iloc[i+1]-data_timestamp.iloc[i] == 2:
			count_time = count_time + 2
		if data_timestamp.iloc[i+1]-data_timestamp.iloc[i] == 1:
			count_time = count_time + 1
		else:
			continue
	
	# time_stamp = data['timestamp']
	# #change time type
	# # time_week = time_stamp/604800#day:86400 week:604800 month:2629743
	# # stamp_jug = data[' activity inference']
	# for p, j in enumerate(data.itertuples()):
 #  		if data.loc[p, ' activity inference'] == 0:
 #  			count_z = count_z + 1
 #  		else:
 #  			count_act = count_act + 1
	# fre = count_act/data.shape[0] # shape[0]: return the number of row
	# act_fre_list.append(fre)

	print(count_time)


activity_frequency()