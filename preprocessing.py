# download the data into np.arrays
from mnist import MNIST
import numpy as np
def download_data(source):
    mndata = MNIST(source)
    X_train, y_train=mndata.load_training()
    X_test, y_test=mndata.load_testing()
    X_train=np.array(X_train)
    y_train=np.array(y_train)
    X_test= np.array(X_test)
    return print(X_train.shape, y_train.shape,X_test.shape, y_test.shape)

#