import numpy as np
features_train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
labels_train = np.array([1, 1, 1, 2, 2, 2])
features_test = np.array([[-4, -5], [-0.5, -0.3], [-1.2, -0.2],
                          [0.5, 0.6], [1, 3], [0.1, 0.2]])
labels_test = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)
print(prediction)

accuracy = clf.score(features_test, labels_test)
print(accuracy)
