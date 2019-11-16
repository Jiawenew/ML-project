import pandas as pd
import time

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
		fre=data.shape[0]/period #?????????
		conv_fre_list.append(fre)

	print(conv_fre_list)
	#data['start_timestamp']=data['start_timestamp'].apply(lambda a: time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a)))
	#data['end']=data['end'].apply(lambda a: time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a)))



def conversation_length():
	list=[]
	for i in range(0,60):
		try:
			data=pd.read_csv('data/conversation/conversation_u'+str(i).zfill(2)+'.csv',header=0)
		except:
			continue
		data['end_start']=data[' end_timestamp']-data['start_timestamp']
		total_time=data['end_start'].sum()
		start=data['start_timestamp'].iloc[0]
		end=data['start_timestamp'].iloc[-1]
		period=(end-start)/604800#day:86400 week:604800 month:2629743
		length=total_time/period/60/60
		list.append(length)
	print(list)


conversation_frequency()
