import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression 
from sklearn.linear_model import LinearRegression



def plot(X, y, color="b", shape="."):
    plt.figure()
    plt.plot(X, y, color + shape, size=0.1)
    plt.show()
    plt.close()

X, y = make_regression(n_samples=100, n_features=1, noise=3)

X_test, y_test, X_train, y_train = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression().fit(X_train, y_train)

y_hat = model.predict(X_test)

## Solution With SciKit
plt.figure()

min_x = min(X) - 0.2
max_x = max(X) + 0.2

regression_line = [min_x, max_x]


plt.plot(regression_line, model.predict(regression_line), "r-")

plt.plot(X_train, y_train, "g.", label="Train set")
plt.plot(X_test, y_hat, "k.", label="predict set")

plt.show()
plt.close()


print "MSE:\t\t", np.mean((y_test - y_hat) ** 2)
print "Variance score:", model.score(X_test, y_test)


## Without SKLearn
alpha = 0.01
epsilon = 0.3
degree = 1
W = np.zeros(degree + 1)
M = len(X)

errors = []

def update_weights(y, y_hat, x):
    error = y - y_hat
    for degree in range(len(W)):
        W[degree] += alpha * error * pow(x, degree)
    errors.append(error)
        
def predict(x):
    return sum([W[degree] * pow(x, degree) for degree in range(len(W))])

def get_avg_error(X, y):
    return abs(sum(sum(predict(X) - y)) / M)

def update_E(X, y):
    E.pop(0)
    E.append(get_avg_error(X, y))
    error_index.append(E[-1])

    M = len(X_train)

counter = M*3


USE_ERROR = True
sindex = 0
while counter > 0:
    if USE_ERROR:
        if E[-1] > epsilon:
            print counter, E[-1], "\n"
            counter = M
        
            x = X_train[index]
            y = y_train[index]

            y_hat = predict(x)
            update_weights(y, y_hat, x)
        else:
            counter -= 1
    else:
        counter -= 1
        
        x = X_train[index]
        y = y_train[index]

        y_hat = predict(x)
        update_weights(y, y_hat, x)


    index = (index + 1) % M
    
print E[-3:]    

plt.figure()
plt.plot(X_train, y_train, "b.")
plt.plot(X_train, predict(y_train), "r.")
plt.show()
plt.close()

print W

def plot_model_and_input():
    ## DATA PLOT
    plt.figure()
    plt.plot(X_train, y_train, "b.")
    plt.plot(X_train, predict_arr(X_train), "r.")
    plt.show()
    plt.close()

    ## ERROR PLOT
    plt.figure()
    plt.plot(range(len(errors)), errors)
    plt.show()
    plt.close()