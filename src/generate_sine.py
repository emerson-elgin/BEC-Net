import numpy as np

# Generate a sine wave dataset
x = np.linspace(0, 10 * np.pi, 500)  # 500 points over 10π
y = np.sin(x)

# Save the dataset as a .npy file in the 'data' folder
np.save('data/sine_wave_data.npy', y)

print("Dataset saved to 'data/sine_wave_data.npy'")
