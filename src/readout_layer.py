from sklearn.linear_model import Ridge

def train_readout(features, targets, alpha=1.0):
    model = Ridge(alpha=alpha)
    model.fit(features, targets)
    return model

def predict(model, features):
    return model.predict(features)
