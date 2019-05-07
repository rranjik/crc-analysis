import pandas as pd

feature_cols = ['age','Otu0918','Otu0302','Otu0915','Otu0772','Otu0776','Otu0552','Otu0309','Otu0777','Otu1947','Otu0753','Otu0917','Otu1895','Otu1717','Otu1978','Otu0669','Otu0664','Otu0304','Otu0805','Otu0774','Otu0798','Otu0691','Otu1659','Otu0030','Otu1854','Otu0303','Otu0804','Otu1807','Otu1841','Otu0618','Otu1702','Otu0802','Otu1131','Otu0553','Otu0593','Otu0849','Otu0688','Otu0561','Otu0303','Otu0164','Otu0314','Otu0778','Otu1898','Otu1413','Otu1854','Otu0703','Otu1530','Otu0691','label']

data = pd.read_csv("..//..//data//multi-cohortd.csv", skiprows=[1], header= None, names=feature_cols, low_memory=False)
data.head()


X = data.iloc[:,-1]
y = data.label


from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)

from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

cnf_matrix

