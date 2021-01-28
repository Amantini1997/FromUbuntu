import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.preprocessing import PolynomialFeatures


def plot_model(x, y, model, transformer):
    x_poly = transformer.fit_transform(x)
    model.fit(x_poly, y)

    x_range = np.linspace(min(x) - 1, max(x) + 1, 100)
    x_range_poly = transformer.fit_transform(x_range)
    y_pred = model.predict(x_range_poly)

    print(model.coef_)

    plt.figure()
    plt.scatter(x, y)
    plt.plot(x_range, y_pred)
    plt.ylim(min(y) - 10, max(y) + 10)
    plt.show()


x, y = make_regression(n_samples=20, n_features=1, noise=10)
transformer = PolynomialFeatures(degree=10)
x_anomaly = np.append(x, 1)[:, None]
y_anomaly = np.append(y, max(y) + 10)[:, None]


lr = linear_model.LinearRegression()
plot_model(x, y, lr, transformer)
plot_model(x_anomaly, y_anomaly, lr, transformer)

ridge = linear_model.Ridge(alpha=2)
plot_model(x, y, ridge, transformer)
plot_model(x_anomaly, y_anomaly, ridge, transformer)
