
# step 1 : load data
import numpy as np
import urllib
# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
# separate the data from the target attributes
#print raw_data
#print type(raw_data)
#print type(dataset)
X = dataset[:,0:7]
y = dataset[:,8]


# step 2 : data format
#from sklearn import preprocessing
#normalized_X = preprocessing.normalize(X)
#standardized_X = preprocessing.scale(X)
#print standardized_X

#step 3 : choose feature
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X,y)
print model.feature_importances_
#
##step 3-2: compare feature
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
#model = LogisticRegression()
## create the RFE model and select 3 attributes
#rfe = RFE(model, 3)
#rfe = rfe.fit(X, y)
## summarize the selection of the attributes
#print(rfe.support_)
#print(rfe.ranking_)
#
#
#step 4 : protocal
from sklearn import metrics
from sklearn.svm import SVC
# fit a SVM model to the data
model = SVC()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
#print expected
#print predicted
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
