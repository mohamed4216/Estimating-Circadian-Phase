import pandas as pd
import matplotlib.pyplot as plt
raw_df = pd.read_hdf('data.h5', 'raw')
def get_quantile(data, q):
	"""Takes series of values and returns quantile limit as well as the mean of the values above the quantile.
	data: Data as pandas Series.
	q: Quantile (0.75 -> 75%)
	returns: quantile limit, mean value of elements above quantile limit
	"""
	quantile_limit = data.quantile(q=q)
	quantile_mean = data[data >= quantile_limit].mean()
	return quantile_limit, quantile_mean

def compute_features(test_df, verbose=False):
	""" Takes PVT test results and returns feature vector as a result.
	test_df: Dataframe containing PVT test results.
	Returns: Series containing the feature vector.
	"""
	test_time = test_df.timestamp.iloc[0]
	n = test_df.shape[0]
	positive_data = test_df[test_df.response_time > 0] # drop all "too early samples"
	n_positive = positive_data.shape[0]
	positive_mean = positive_data.response_time.mean()
	positive_median = positive_data.response_time.median()
	positive_std = positive_data.response_time.std()
	q50_lim, q50_mean = get_quantile(positive_data.response_time, 0.50)
	q75_lim, q75_mean = get_quantile(positive_data.response_time, 0.75)
	q90_lim, q90_mean = get_quantile(positive_data.response_time, 0.90)
	q95_lim, q95_mean = get_quantile(positive_data.response_time, 0.95)
	features = pd.Series({'Test_time' : test_time,
	'Subject' : test_df.subject.iloc[0],
	'Test_nr' : test_df.test.iloc[0],
	'n_total' : n,
	'n_positive' : n_positive,
	'positive_mean' : positive_mean,
	'positive_median' : positive_median,
	'positive_std' : positive_std,
	'q50_lim' : q50_lim,
	'q75_lim' : q75_lim,
	'q90_lim' : q90_lim,
	'q95_lim' : q95_lim,
	'q50_mean' : q50_mean,
	'q75_mean' : q75_mean,
	'q90_mean' : q90_mean,
	'q95_mean' : q95_mean})
	
	if verbose:
		print(features)
	return features

feature_df = pd.DataFrame()
for subject_id, subject_df in raw_df.groupby(raw_df.subject):
	for test_id, test_df in subject_df.groupby(subject_df.test):
		feature_df = feature_df.append(compute_features(test_df), ignore_index=True)
feature_df.reset_index(inplace=True, drop=True)
# Compute the time of day as a float
h = feature_df.Test_time.apply(lambda x: x.hour)
m = feature_df.Test_time.apply(lambda x: x.minute)
feature_df['time_of_day'] = h + (m/60.0)

list1 = list(set(feature_df.Test_time))
set1 = set()
for element in list1:
	set1.add(element.date().strftime("%Y-%m-%d"))
set1 = sorted(set1)

list_name=["positive_mean", "positive_median", "positive_std", "q50_mean", "q75_lim", "q75_mean", "q90_lim", "q90_mean", "q95_lim", "q95_mean"]
for string in list_name:
	print (string+":")
	value=[]
	for i in range(1,9):
		value_participant = []
		#print (feature_df['Test_time'][0].date())
		for time in set1:
			featureDB = feature_df.loc[ (feature_df['Test_time'] >= time +' 00:00:00') & (feature_df['Test_time'] <= time+' 23:59:59') & (feature_df['Subject']==i)]
			value_participant.append(featureDB["positive_median"].mean())
			##break
		value.append(value_participant)

	print (value)
