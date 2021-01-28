import matplotlib.pyplot as plt

a = 3

errors = []
X_train = [1]
y_train = [1]

def predict_arr(X):
    return X

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

plot_model_and_input()    

b = 3
