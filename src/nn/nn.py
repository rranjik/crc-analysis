import pandas as pd
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("/Users/errant/Google Drive/NYU/Spring 19/Machine Learning/project/crc-analysis/data/multi-cohortd_j.csv")

X = dataset.iloc[:, 0:-1]
y = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(activation = 'relu', alpha= 0.01, hidden_layer_sizes=(5,5), learning_rate='adaptive', solver='adam', max_iter=1000)

# parameter_space = {
#     'hidden_layer_sizes': [(5,),(10,),(15,)(20,)(25,)],
#     'activation': ['logistic', 'relu'],
#     'solver': ['sgd', 'adam'],
#     'alpha': [0.0001, 0.01, 0.05],
#     'learning_rate': ['constant','adaptive'],
# }

# from sklearn.model_selection import RandomizedSearchCV
#
# clf = RandomizedSearchCV(mlp, parameter_space, n_jobs=-1, cv=5)
# clf.fit(X_train, y_train)

# Best parameters set
# print('Best parameters found:\n', clf.best_params_)
#
# # All results
# means = clf.cv_results_['mean_test_score']
# stds = clf.cv_results_['std_test_score']
# for mean, std, params in zip(means, stds, clf.cv_results_['params']):
#     print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))
#
# y_true, y_pred = y_test , clf.predict(X_test)
#
# from sklearn.metrics import classification_report
# print('Results on the test set:')
# print(classification_report(y_true, y_pred))



mlp.fit(X_train,y_train)

predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))