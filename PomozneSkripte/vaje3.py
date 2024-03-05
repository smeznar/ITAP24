import numpy as np


def create_data():
    x = np.random.random((1000, 10))
    y = x[:, 0] * x[:, 1] - 3 * x[:, 2] +  6*x[:, 3] - 3 * x[:, 4] * x[:, 3] * x[:, 2] + np.random.normal(0, 0.2, size=1000)
    indices = np.argsort(y)
    x = x[indices]
    y = y[indices]
    y[:799] = 0
    y[799:] = 1
    return x, y
    

if __name__ == '__main__':
    x, y = create_data()
    np.savez("Podatki/vaje3_2", x=x, y=y)