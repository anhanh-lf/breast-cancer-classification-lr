import numpy as np


class LogisticRegressionScratch:
    def __init__(self, lr=0.1, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.losses = []
        self.w = None
        self.b = 0

    def _sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def _compute_loss(self, y, y_hat):
        epsilon = 1e-15
        bce = -(
            y * np.log(y_hat + epsilon)
            + (1 - y) * np.log(1 - y_hat + epsilon)
        )
        return np.mean(bce)

    def fit(self, X, y):
        n_sample, n_feature = X.shape
        self.w = np.zeros(n_feature)
        self.b = 0
        self.losses = []

        for _ in range(self.n_iters):
            z = X @ self.w + self.b
            y_hat = self._sigmoid(z)
            self.losses.append(self._compute_loss(y, y_hat))
            dw = (1 / n_sample) * np.dot(X.T, y_hat - y)
            db = np.mean(y_hat - y)
            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict_proba(self, X):
        if self.w is None:
            raise RuntimeError("Call fit before predict_proba.")
        return self._sigmoid(X @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)
