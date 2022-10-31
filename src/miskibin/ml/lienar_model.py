import numpy as np
from numpy.linalg import LinAlgError
from miskibin.utils import get_logger


class LinearModel:
    def __init__(self, method: str = "analitical", logger=get_logger()):
        self.logger = logger
        self.fit_func = method
        self.params = None

    @property
    def fit_func(self):
        return self._fit_func  # can not be changed outside class

    @fit_func.setter
    def fit_func(self, method):
        if method not in ["analitical", "numerical"]:
            raise ValueError("Unknown method")
        if method == "analitical":
            self._fit_func = self.__fit_analitical
        else:
            self._fit_func = self.__fit_numerical
        self.logger.info(f"Set fit method to {method}")

    def __fit_analitical(self, X: np.ndarray, Y: np.ndarray):
        if X.shape[0] < X.shape[1]:
            print(
                f"To fit model with {X.shape[0]} params,  You  have to provide at least {X.shape[1]} samples"
            )
        X_ext = np.hstack((np.ones((X.shape[0], 1)), X))  # add ones on left
        self.logger.debug(f"Fitting model with {X_ext.shape[1]} params")
        try:
            self.params = Y.T @ X_ext @ np.linalg.pinv(X_ext.T @ X_ext)
        except LinAlgError as err:
            self.logger.error(err)
            print(f"Can not fit model to data det of X = 0")
            raise err

    def __fit_numerical(self, X: np.ndarray, Y: np.ndarray):
        pass

    def fit(self, X, Y):
        self.fit_func(X, Y)

    def predict(self, X):
        X_ext = np.hstack((np.ones((X.shape[0], 1)), X))  # add bias
        Y_pred = X_ext @ self.params.T
        return Y_pred

    def mse(self, X, Y):
        Y_pred = self.predict(X)
        return np.mean((Y_pred[0].argmax() - Y) ** 2)

    def __str__(self) -> str:
        data = f"Linear model with {self.fit_func.__name__.split('_')[-1]} method\n"
        if self.params is not None:
            data += f" and {len(self.params)} parameters "
        else:
            data += " not fitted to fit use `fit` method "
        return data
