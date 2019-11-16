import pandas as pd
import time

#count the frequency of tester activity
def activity_frequency():
	act_fre_list = []
	# for i in range(0,60):
	# 	try:
	# 		data = pd.read_csv('activity/activity_u'+str(i).zfill(2)+'.csv',header = 0)
	# 	except:
	# 		continue
	 	# data = pd.read_csv('activity/activity_u'+str(i).zfill(2)+'.csv',header = 0)
	data = pd.read_csv('data/activity/activity_u00.csv',header = 0)
	count_z = 0 # the number of Stationary
	count_act = 0 # the number of activity
	# time_stamp = data['timestamp']
	data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
	# print(data['2013-03-27'])
	index_list=[]
	every_day_list=[]
	activ_list=[]
	# data = data.set_index('timestamp',drop =True)
	# print(data[' activity inference'])
	activ_list= list(data[' activity inference'])
	# print(activ_list)

	#rebuild a data set
	ts = pd.Series(activ_list, index=data['timestamp']) #series is a data structure to index data

	# print(ts['2013-03-28'])

	time_index=pd.date_range('2013-03-27','2013-06-01', freq='D')
	for i in time_index:
		i = pd.datetime.strftime(i,'%Y-%m-%d')
		# print(i)
		# print(data[i])
		index_list.append(i)
	# print(index_list)
	# 	# print(ts[i])
	for i in index_list:
	# 	for i
		# print(ts[i])
		for index in ts[i].index:
			# print(ts[index])
			if ts[index] == 0:
				count_z = count_z + 1
			else:
				count_act = count_act + 1
		fre = count_act / ts[i].shape[0]
		every_day_list.append(fre)
		fre = 0
	# data = data[index_list[1]]
	# print(data)
	# [row, col] = data.shape
	# for i in range(row):
	# 	print(data[0][col])
		# print(m)
		# for m in data[i]:
		#
		# 	print(m)
		# 	# print(f'sss')
		# 	print(data[i][m])
		# 	if data[i][m][' activity inference'] == 0:
		# 	# 	# print(f'shawo')
		# 		count_z = count_z + 1
		# 	else:
		# 		# print(f'wujin')
		# 		count_act = count_act + 1
		# fre = count_act/data[i].shape[0] # shape[0]: return the number of row
		# every_day_list.append(fre)
	# print(g)
		#change time type
		# time_week = time_stamp/604800#day:86400 week:604800 month:2629743
		# stamp_jug = data[' activity inference']
		print(every_day_list)

# activity_frequency()

activity_frequency()
