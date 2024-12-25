import numpy as np

def encode_input(input_signal, grid_size, scale=1.0):
    x = np.linspace(-1, 1, grid_size)
    X, Y = np.meshgrid(x, x)
    return scale * input_signal * (X**2 + Y**2)
