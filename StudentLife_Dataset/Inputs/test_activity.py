import pandas as pd
import time

#count the frequency of tester activity
def activity_frequency():
	act_fre_list = []
	for i in range(0,60):
		try:
			data = pd.read_csv('data/activity/activity_u'+str(i).zfill(2)+'.csv',header = 0)
		except:
			continue
		count_z = 0 # the number of Stationary
		count_act = 0 # the number of activity
		time_stamp = data['timestamp']
		#change time type
		time_week = time_stamp/604800#day:86400 week:604800 month:2629743
		# stamp_jug = data[' activity inference']
		for p, j in enumerate(data.itertuples()):
  			if data.loc[p, ' activity inference'] == 0:
  				count_z = count_z + 1
  			else:
  				count_act = count_act + 1
		fre = count_act/data.shape[0] # shape[0]: return the number of row
		act_fre_list.append(fre)

	print(act_fre_list)


activity_frequency()