import numpy as np
from src.bec_simulation import simulate_bec
from src.input_encoder import encode_input
from src.feature_extractor import extract_features
from src.readout_layer import train_readout, predict

# Parameters
grid_size = 128
dx = 0.1
time_steps = 100
dt = 0.01
g = 1.0

# Load input data
input_signal = np.load('data/sine_wave_data.npy')

# Check the shape of input_signal
print(f"Shape of input_signal: {input_signal.shape}")

# Encode input
encoded_input = encode_input(input_signal, grid_size)

# Check the shape of encoded_input
print(f"Shape of encoded_input: {encoded_input.shape}")

# Initial state
initial_state = np.exp(-(np.linspace(-1, 1, grid_size)**2))

# Simulate BEC
densities = simulate_bec(initial_state, lambda t: encoded_input, time_steps, dt, grid_size, dx, g)

# Extract features
features = extract_features(densities)

# Train Readout
targets = np.sin(np.linspace(0, 10 * np.pi, len(features)))  # Dummy targets
model = train_readout(features.reshape(-1, 1), targets)

# Predict
predictions = predict(model, features.reshape(-1, 1))
print("Predictions:", predictions)
