import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE
from sklearn import datasets
data = pd.read_csv("..//..//data//multi-cohortd.csv") 
X = data.iloc[:,-1]
y = data.label
svm = LinearSVC()
# create the RFE model for the svm classifier 
# and select attributes
rfe = RFE(svm, 130)
rfe = rfe.fit(X, y)
# print summaries for the selection of attributes
print(rfe.support_)
print(rfe.ranking_)
