import numpy as np

def encode_input(input_signal, grid_size):
    # Ensure input_signal has enough elements
    required_size = grid_size**2
    if input_signal.shape[0] < required_size:
        # Pad the signal with zeros if it's smaller than required size
        input_signal_reshaped = np.pad(input_signal, (0, required_size - input_signal.shape[0]), mode='constant')
    else:
        # Truncate the signal if it's larger than required size
        input_signal_reshaped = input_signal[:required_size]

    # Reshape to the grid size
    input_signal_reshaped = input_signal_reshaped.reshape(grid_size, grid_size)

    # Generate the meshgrid for X and Y
    X, Y = np.meshgrid(np.linspace(-1, 1, grid_size), np.linspace(-1, 1, grid_size))
    
    # Apply the input signal element-wise with X^2 + Y^2
    scale = 1  # Adjust scale as needed
    return scale * input_signal_reshaped * (X**2 + Y**2)

# Example usage
input_signal = np.load('data/sine_wave_data.npy')

# Check the shape of input_signal
print(f"Shape of input_signal: {input_signal.shape}")

# Parameters
grid_size = 128

# Encode input
encoded_input = encode_input(input_signal, grid_size)

# Check the shape of encoded_input
print(f"Shape of encoded_input: {encoded_input.shape}")
