import pandas as pd
import joblib
import time


def minmax(list):#标准化
	minv=min(list)
	maxv=max(list)
	for i in range(len(list)):
		list[i]=(list[i]-minv)/(maxv-minv)



def conversation_frequency():
	conv_fre_list=[]
	for i in range(0,60):
		try:
			data=pd.read_csv('data/conversation/conversation_u'+str(i).zfill(2)+'.csv',header=0)
		except:
			continue
		start=data['start_timestamp'].iloc[0]
		end=data['start_timestamp'].iloc[-1]
		period=(end-start)/604800#day:86400 week:604800 month:2629743
		fre=data.shape[0]/period
		conv_fre_list.append(fre)

	print(conv_fre_list)
	#data['start_timestamp']=data['start_timestamp'].apply(lambda a: time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a)))
	#data['end']=data['end'].apply(lambda a: time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a)))



def conversation_duration():
	list=[]
	output_l=[25,41,54]
	for i in range(0,60):
		if i in output_l:
			continue
		try:
			data=pd.read_csv('data/conversation/conversation_u'+str(i).zfill(2)+'.csv',header=0)
		except:
			continue
		data['end_start']=data[' end_timestamp']-data['start_timestamp']
		total_time=data['end_start'].sum()
		start=data['start_timestamp'].iloc[0]
		end=data['start_timestamp'].iloc[-1]
		period=(end-start)/604800#day:86400 week:604800 month:2629743
		duration=total_time/period/60/60
		list.append(duration)
	return list


def conversation_duration_evening():
	list = []
	output_l=[25,41,54]
	for i in range(0,60):
		if i in output_l:
			continue
		try:
			data=pd.read_csv('data/conversation/conversation_u'+str(i).zfill(2)+'.csv',header=0)
		except:
			continue
		start = data['start_timestamp'].iloc[0]
		end = data['start_timestamp'].iloc[-1]
		period = (end - start) / 604800  # day:86400 week:604800 month:2629743
		data['end_start'] = data[' end_timestamp'] - data['start_timestamp']
		total_time=0
		for index, row in data.iterrows():
			if row['start_timestamp']%86400 < 18000 or row['start_timestamp']%86400>64800:
				total_time+=row['end_start']
		list.append(total_time/period/60/60)
	return list

def co_location_bt():
	list_total=[]
	list_mean=[]
	output_l=[25,41,54]
	for i in range(0, 60):
		if i in output_l:
			continue
		try:
			data_bt=open('data/bluetooth/bt_u' + str(i).zfill(2) + '.csv')
		except:
			continue
		group=[]
		tem=-1
		for data in data_bt:
			if data=='\n':
				group.append(tem)
				tem=0
			tem+=1
		total_mumber=sum(group)
		mean_mumber=total_mumber/len(group)
		list_total.append(total_mumber)
		list_mean.append(mean_mumber)
	return list_total,list_mean

def co_location_wifi():
	list_total=[]
	list_mean=[]
	output_l=[25,41,54]
	for i in range(0, 60):
		if i in output_l:
			continue
		try:
			data_bt=open('data/wifi/wifi_u' + str(i).zfill(2) + '.csv')
		except:
			continue
		group=[]
		tem=-1
		for data in data_bt:
			if data=='\n':
				group.append(tem)
				tem=0
			tem+=1
		total_mumber=sum(group)
		mean_mumber=total_mumber/len(group)
		list_total.append(total_mumber)
		list_mean.append(mean_mumber)
	return list_total,list_mean



cover_du=conversation_duration()
cover_dueve=conversation_duration_evening()
co_total_bt,co_mean_bt=co_location_bt()
co_total_wifi,co_mean_wifi=co_location_wifi()


list=[]
list.append(cover_du)
list.append(cover_dueve)
list.append(co_total_bt)
list.append(co_mean_bt)
list.append(co_total_wifi)
list.append(co_mean_wifi)
for e in list:
	minmax(e)

joblib.dump(list, 'features_fourishing.pkl')#把feature 存进文件，反复计算feature很浪费时间

