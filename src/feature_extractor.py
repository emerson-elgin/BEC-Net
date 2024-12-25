import numpy as np

def extract_features(densities):
    return np.array([np.mean(density) for density in densities])
