import pandas as pd
raw_df = pd.read_hdf('data.h5', 'labels')
#print (raw_df)

list_participant = []
for i in range(1,9):
	sleep = 0
	dict1 = []
	Observation = raw_df[raw_df['Participant_ID']==i]
	Observation = Observation.sort_values('Time', ascending=True)
	for index, row in Observation.iterrows():
		if (row['Sleep']!= sleep):
			try:
				row1 = Observation.loc[[index+4]]
				if row1['Sleep'] == row['Sleep']:
					continue
				
			except:
				pass
			dict1.append(row['Time'])
			sleep = row['Sleep']
			#print (row['Time'])
	list_participant.append(dict1)
	
for i in range(0, len(list_participant)):
	print ("**********************************")
	print ("Participant N:"+str(i))
	for j in range(0, len(list_participant[i])-1,2):
		
		test = list_participant[i][j]+(list_participant[i][j+1]-list_participant[i][j])/2
		print (test)

	print (list_participant[i])
#print (dict1[4]+(dict1[5]-dict1[4])/2)
