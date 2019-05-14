import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

dataset = pd.read_csv("/Users/errant/Google Drive/NYU/Spring 19/Machine Learning/project/crc-analysis/data/multi-cohortd_j.csv")

X = dataset.iloc[:, 0:-1]
y = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling - not necessary for RF
# from sklearn.preprocessing import StandardScaler
#
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=5000, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


# Feature Importance
importances = classifier.feature_importances_
std = np.std([tree.feature_importances_ for tree in classifier.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
# plt.figure()
# plt.title("Feature importances")
# plt.bar(range(X.shape[1]), importances[indices],
#        color="r", yerr=std[indices], align="center")
# plt.xticks(range(X.shape[1]), indices)
# plt.xlim([-1, X.shape[1]])
# plt.show()

print("Trained Model :: ", classifier)

# For Regression
# from sklearn import metrics
#
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# For Classification
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("Train Accuracy :: ", accuracy_score(y_train, classifier.predict(X_train)))
print("Test Accuracy  :: ", accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))