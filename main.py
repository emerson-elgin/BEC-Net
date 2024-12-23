import numpy as np
import matplotlib.pyplot as plt
from src.bec_simulation import BECReservoir
from src.feature_extractor import train_readout

# Load synthetic dataset (sine wave)
input_signal = np.load('data/sine_wave_data.np')

# Step 1: Run BEC simulation
reservoir = BECReservoir(time_steps=len(input_signal))
output_features = reservoir.simulate(input_signal)

# Step 2: Train Readout Layer
model, predictions, mse = train_readout(output_features, input_signal)

# Step 3: Visualize Results
plt.plot(input_signal, label="True Input")
plt.plot(predictions, label="Predicted Output")
plt.legend()
plt.title(f"Prediction with Ridge Regression (MSE: {mse:.5f})")
plt.show()
