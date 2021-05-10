import numpy as np
import sklearn
from sklearn.datasets import fetch_openml
import joblib
import pickle
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

# TODO: prikazi nekoliko ulaznih slika
img = X[0, :]
img = img.reshape((28, 28))
plt.imshow(img, cmap='gray')
plt.show()


# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier
mlp_mnist = MLPClassifier(random_state=1, max_iter=20, verbose=True).fit(X_train, y_train)

# TODO: evaluirajte izgradenu mrezu
print('Train score: ', mlp_mnist.score(X_train, y_train))
print('Test score: ', mlp_mnist.score(X_test, y_test))

# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)

plot_confusion_matrix(mlp_mnist, X_test, y_test)
plt.show()