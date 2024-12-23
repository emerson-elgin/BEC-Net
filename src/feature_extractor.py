from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def train_readout(features, targets):
    """Train a Ridge Regression readout layer."""
    model = Ridge(alpha=1e-3)
    model.fit(features, targets)
    predictions = model.predict(features)
    mse = mean_squared_error(targets, predictions)
    return model, predictions, mse
