import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

epsilon = 0.1
alpha = 0.01
errors = []
W = [0.0, 0.0]

X = [1, 3, 3, 5, 2]
y = [1, 3, 2, 3, 2.5]
M = len(X)

def get_sum_error():
    return sum([y[i] - predict(X[i]) for i in range(M)])

def update_weights_batch(x):
    error = get_sum_error()
    for degree in range(len(W)):
        W[degree] += alpha * error * pow(x, degree)
    errors.append(abs(error))

def update_weights_stochastic(y, y_hat, x):
    error = y - y_hat
    for degree in range(len(W)):
        W[degree] += alpha * error * pow(x, degree)
    errors.append(abs(error))
        
def predict(x):
    return sum([W[degree] * pow(x, degree) for degree in range(len(W))])

def predict_arr(X):
    return [predict(x) for x in X]

def get_avg_error(X, y):
    return abs(sum(sum(predict(X) - y)) / M)

def batch_gradient_descent():
    errors = []
    W = [0.0, 0.0]
    for i in range(2 * M):
        update_weights_batch(X[i % M])
    print metrics.mean_absolute_error(y, predict_arr(X))

def stochastic_gradient_descent():
    errors = []
    W = [0.0, 0.0]
    for i in range(M):
        update_weights_stochastic(X[i])
    print metrics.mean_absolute_error(y, predict_arr(X))

plt.figure()
plt.plot(X, y, "r.", label="train")
batch_gradient_descent()
plt.plot(X, predict_arr(X), "b-", label="pred")
stochastic_gradient_descent()
plt.plot(X, predict_arr(X), "k-", label="pred")
plt.legend()
plt.show()
plt.close()