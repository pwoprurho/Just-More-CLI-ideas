from sklearn.datasets import load_iris 
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
iris = load_iris()
x = iris.data
y = iris.target

y_names = iris.target_names

test_ids = np.random.permutation(len(x))
x_train = x[test_ids[:-10]]
x_test = x[test_ids[-10:]]

y_train = y[test_ids[:-10]]
y_test = y[test_ids[-10:]]

clf = tree.DecisionTreeClassifier()
clf.fit(x_train, y_train)
pred = clf.predict(x_test)

#print(pred)
#print(y_test)

result = accuracy_score(pred, y_test)*100 
print(f"machine able to achieve {result}% accuracy in testing")
