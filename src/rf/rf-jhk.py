import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree

import matplotlib.pyplot as plt

dataset = pd.read_csv("/Users/errant/Google Drive/NYU/Spring 19/Machine Learning/project/crc-analysis/data/multi-cohortd_j.csv")
#dataset = pd.read_csv("/Users/errant/Google Drive/NYU/Spring 19/Machine Learning/project/crc-analysis/data/multi-cohort-17-selected.csv")

X = dataset.iloc[:, 0:-1]
y = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling - not necessary for RF
# from sklearn.preprocessing import StandardScaler
#
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
# Fit the random search model


from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 10, stop = 2000, num = 100)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(3, 50, num = 15)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4, 8]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

classifier = RandomForestClassifier(n_estimators=391, random_state=0, min_samples_split=4, min_samples_leaf=4, max_features='sqrt', max_depth=16, bootstrap=False)

# Code for Hyperparameter Tuning
# rf_random = RandomizedSearchCV(estimator = classifier, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=0, n_jobs = -1)
# rf_random.fit(X_train, y_train)
# print("Best Params")
# print(rf_random.best_params_)
#
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

# print("Trained Model :: ", classifier)

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