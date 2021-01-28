import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris.data[:, [1,3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.8, random_state=0) 

classifier = DecisionTreeClassifier(criterion="entropy")
classifier.fit(X_train, y_train)

y_hat = classifier.predict(X_test)

correct = len([1 for act, pred in zip(y_test, y_hat) if act == pred])

print correct, "/", len(y_hat)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))


cs = plt.contourf(xx, yy, classifier)

plt.scatter(X[:, 0], X[:, 1], c=y.astype(np.float))

# Label axes
plt.xlabel( iris.feature_names[1], fontsize=10 )
plt.ylabel( iris.feature_names[3], fontsize=10 )

plt.show()
