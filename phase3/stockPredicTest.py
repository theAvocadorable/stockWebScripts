
# pip install quandl, pip install -U scikit-learn
import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#Get stock data
fileName = 'currentDay.txt'
file = open(fileName, "r")
rawList = file.read().split()
file.close()
normalList = []
tenList = []
for x in rawList:
	hold = []
	hold.append(float(x))
	normalList.append(hold)
lenNormal = len(normalList)

#df = quandl.get("WIKI/FB")



#Get adjusted 
#df = df[['Adj. Close']]

targetValues = normalList

#Predicting N days into the future
forecast_out = 60
#created another column shifted n days - Dependent Varible

Prediction = []

for x in range(lenNormal - forecast_out):
	Prediction.append(targetValues[x+forecast_out][0])


#Create independent varible X
# convert data frame to numpy array
X = np.array(targetValues) # must be the input. appears to be list of lists, does it matter?
#remove last n rows

X = X[:-forecast_out]


#Create dependent data set
# convert to numpy array
y = np.array(Prediction)
#Grab all but last n rows

#Split data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#create and train Support Vector Machine (Regressor)
svr_rbf = SVR(kernel='rbf',C=1e3,gamma=0.1)
svr_rbf.fit(x_train, y_train )

#testing Model with score being coeffeicent of determination R^2
svm_confidence = svr_rbf.score(x_test, y_test)
print("SVM confidence: ", svm_confidence)

#Create and train Linear Regression Model
lr = LinearRegression()
#train it
lr.fit(x_train, y_train)

#testing Model with score being coeffeicent of determination R^2. Best is 1
lr_confidence = lr.score(x_test, y_test)
print('LR confidence: ', lr_confidence)

#set x_forcast to last 30 rows of orfginla data
x_forecast = np.array(targetValues[len(targetValues)-forecast_out:])

#print prediction for next n days regression model
lr_prediction = lr.predict(x_forecast)
#print(lr_prediction)

#print prediction for next n days - support vector 
svm_prediction = svr_rbf.predict(x_forecast)
#print(svm_prediction)

Max = 0
Min = 0 
if lr_confidence > svm_confidence:
	print ("Going with Linear regression")	
	for x in range(len(lr_prediction)):
		if(lr_prediction[x] > lr_prediction[Max]):
			Max = x
		if(lr_prediction[x] < lr_prediction[Min]):
			Min = x
		
	if(lr_prediction[Max]/103 > lr_prediction[Min]/100):
		print("Money can be made")
		if(Min + 5 < Max):
			print("Simply buy and offload")	
		else:
			temMin = 0
			for x in range(Max):
				if(lr_prediction[x] < lr_prediction[temMin]):
					temMin = x
			if(lr_prediction[Max]/103 > lr_prediction[temMin]/100) and temMin + 5<max:
				print("Buy at temp Min")
	else:
		print("No money to be made")			
		

else:
	print("Going with Support Vector")
	for x in range(len(svm_prediction)):
		if(svm_prediction[x] > svm_prediction[Max]):
			Max = x
		if(svm_prediction[x] < svm_prediction[Min]):
			Min = x
		
	if(svm_prediction[Max]/103 > svm_prediction[Min]/100):
		print("Money can be made")
		if(Min + 5 < Max):
			print("Simply buy and offload")	
		else:
			temMin = 0
			for x in range(Max):
				if(svm_prediction[x] < svm_prediction[temMin]):
					temMin = x
			if(svm_prediction[Max]/103 > svm_prediction[temMin]/100) and temMin + 5<Max:
				print("Buy at temp Min")
	else:
		print("No money to be made")			
