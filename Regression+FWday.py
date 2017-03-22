import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.svm import SVR
import pandas as pd
from sklearn.cross_validation import train_test_split


#features (reaction time, FWday)

x_positive_std=[[59.94005187375116,1],[89.37063178677337,1], [65.14588799166182,1], [70.28568796171628,1],[ 79.10286618744689,1],[129.59342708013912,1], [211.52142114913923,1], [121.46420582880066,1], [128.2542316535773,1],[ 93.4380053027291,1],[68.80804926528751,1],[104.87259871922338,1], [58.941566506339996,1],[51.505947604242294,1],[99.27666945589066,1], [144.48294787887113,1], [176.9527417366297,1], [222.23193523274233,1], [334.48041707166425,1],[761.0325866155475,1], [645.7754691063918,1], [929.0248656382593,1],[ 2411.9747735484216,1],[134.28349895468773,1], [116.48014785529688,1], [98.95901685909556,1], [128.2269881794274,1], [72.56552617277993,1],[90.31651637318411,0],[61.67265531823114,0], [69.84650443091064,0], [279.08396509602574,0],[ 307.29376902853386,0], [62.8701315331063,0],[58.23208266526869,0] ,[109.95905874747018,0],[ 79.83399868767428,0],[370.30257512679106,0],[287.9721778570193,0], [106.10044033264896,0], [102.39663413928513,0], [148.48986133877816,0], [222.0233481840947,0], [228.1004374850501,0], [164.40327361144168,0], [264.03089184148814,0], [416.36615923741647,0],[658.8028541535055,0], [1906.3582565770146,0], [121.21552122000091,0],[190.1972670232341,0], [256.2588985072848,0]]


x_q90_mean=[[472.30499999999995,1], [543.5250000000001,1], [471.3888888888889,1], [478.0071428571428,1], [525.1583333333333,1],[703.3333333333334,1], [974.5041666666666,1], [673.4849999999999,1], [716.7045454545454,1], [653.1333333333333,1],[483.7666666666667,1], [611.12,1], [440.43333333333334,1], [436.92333333333335,1], [590.0142857142857,1], [676.2416666666667,1], [822.2833333333333,1], [916.8833333333333,1], [1238.9166666666667,1],[2366.8300000000004,1], [2315.6388888888887,1], [3014.785714285714,1], [6984.0,1],[670.0,1], [589.2125,1], [586.8,1], [704.5833333333334,1], [538.5625,1],[543.3625,0], [474.7,0], [494.70714285714286,0], [1132.639393939394,0], [1217.259090909091,0], [474.4125,0], [446.32,0], [534.9,0], [528.4166666666666,0], [1323.65,0], [1018.6666666666666,0], [569.8111111111111,0], [613.18125,0], [737.2357142857143,0], [914.6071428571429,0], [989.0500000000001,0], [816.9416666666666,0], [1090.4833333333333,0], [1091.286111111111,0], [2610.7,0], [5270.75,0], [654.53,0], [817.0625,0], [1031.2375,0]]

x_q95_mean=[[504.9,1], [640.4166666666667,1], [509.98148148148147,1], [546.0,1], [594.1944444444445,1],[834.9871794871796,1], [1193.5416666666667,1], [849.9833333333333,1], [841.8181818181819,1], [728.2407407407409,1],[534.6944444444445,1], [702.5666666666667,1], [497.9166666666667,1], [470.8666666666666,1],[691.8333333333334,1], [835.75,1], [962.0,1], [1108.2777777777778,1], [1580.777777777778,1], [3343.8,1],[3051.222222222222,1], [3920.8809523809527,1], [9927.833333333334,1],[753.5,1], [705.0,1], [704.6,1], [807.8333333333334,1], [597.625,1],[633.75,0], [502.7777777777778,0], [544.2142857142857,0], [1410.090909090909,0], [1504.469696969697,0], [526.6666666666667,0],[ 494.9666666666667,0], [676.1666666666666,0], [583.1666666666666,0],[1788.9666666666667,0], [1402.388888888889,0],[660.2592592592594,0], [701.0,0], [891.3095238095239,0], [1114.357142857143,0], [1239.611111111111,0], [979.375,0], [1347.388888888889,0], [1467.4166666666667,0],[3052.6,0], [8249.0,0], [778.9333333333333,0], [1064.0,0], [1312.4375,0]]




X=pd.DataFrame(data=x_q95_mean)

# Mid-sleep point MS, MSW then MSF
y=[3.75,3.375,	3.125,	5,1.125,3,3.875,4, 3.25,	3.25,	4.5,	6.125,	4.875,		5.625,	3.75,3.75,	2.75,	4,	4,
3.75,			4,	3.875,3.125,	3.875,	3.125,	3.5,	3.375,	3.375,4.5,	6.625,	4.75,	3.25,	3.75,	6.5,	7.5,	8.125,	8.375,	7.25,	6.375,	3.75,	4.75,	3.625,	3.5,	6,	6.25,	5,	2.5,	4.125,	4.75,	4.625,	4.125,	3.5]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)


# Create regression object

regr = linear_model.LinearRegression()
#regr = SVR(kernel='rbf', C=1e3, gamma=0.1)

# Train the model using the training sets
regr.fit(X_train, y_train)

# The coefficients for linear model
#print('Coefficients: \n', regr.coef_)

# The root mean squared error
print("root mean squared error: %.2f"
      % np.sqrt((regr.predict(X_test)-0.7- y_test) ** 2).mean())

