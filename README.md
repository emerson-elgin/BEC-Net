# BEC-Net: Dynamic Quantum Reservoirs Using Bose-Einstein Condensates

## Overview

**BEC-Net** simulates dynamic quantum reservoirs using **Bose-Einstein Condensates (BECs)**. This project models a quantum system using a reservoir computing architecture, where BECs act as the dynamic medium for information processing. The system is trained using a readout layer to predict time-series data.

---

## Project Structure

- **`src/`**: Contains all source code files.
  - `bec_simulation.py`: Simulates the evolution of BECs.
  - `input_encoder.py`: Encodes the input signal.
  - `feature_extractor.py`: Extracts features from simulated densities.
  - `readout_layer.py`: Implements the training and prediction of the readout layer.

- **`data/`**: Contains input data files (e.g., `sine_wave_data.npy`).

- **`main.py`**: Main script that runs the entire simulation.

---

## Installation

To install the required dependencies for this project, follow these steps:

### Prerequisites:
Make sure you have Python 3.7+ installed.

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/your-repository/BEC-Net.git
cd BEC-Net


---


Equations
This project uses several key equations for simulating the BEC dynamics and encoding the input signal.

1. BEC Dynamics
The time evolution of the BEC is governed by the Gross-Pitaevskii equation, which describes the behavior of the condensate wave function:

iℏ ∂ψ(r,t) / ∂t = (-ℏ² / 2m) ∇²ψ(r,t) + V(r)ψ(r,t) + g |ψ(r,t)|²ψ(r,t)

Where:

ψ(r,t) is the wave function of the BEC.
∇² is the Laplacian operator (spatial derivatives).
V(r) is the external potential.
g is the interaction strength.
|ψ(r,t)|² is the particle density.
2. Input Encoding
The input signal is encoded onto a 2D grid by tiling the input data to fill the grid. The encoding function uses spatial coordinates X and Y:

encoded_input(X,Y) = scale × input_signal_reshaped × (X² + Y²)

Where:

X, Y are the 2D coordinates in the grid.
input_signal_reshaped is the reshaped input signal.
3. Readout Layer
The readout layer uses a linear regression model that maps the extracted features to the target signal:

y(t) = wᵀ x(t) + b

Where:

y(t) is the predicted output.
w is the weight vector.
x(t) are the extracted features at time t.
b is the bias term.



Usage
Prepare Input Data
Generate a sample sine wave signal:

python
Copy code
import numpy as np

# Generate a sample sine wave as the input signal
input_signal = np.sin(np.linspace(0, 10 * np.pi, 500))
Run the Simulation
After installing the dependencies, run the simulation with the main.py script:

bash
Copy code
python main.py
Example Plots
1. Input Signal
Plotting the original sine wave input signal:

python
Copy code
import matplotlib.pyplot as plt

# Plot input signal
plt.plot(input_signal)
plt.title("Original Input Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
2. Encoded Input Signal
Visualizing the encoded input signal as a heatmap:

python
Copy code
encoded_input = np.random.rand(128, 128)  # Placeholder data
plt.imshow(encoded_input, cmap='viridis', origin='lower')
plt.title("Encoded Input Signal")
plt.colorbar(label="Amplitude")
plt.show()
License
This project is licensed under the MIT License. See the LICENSE file for details.

markdown
Copy code

### Explanation of Key Sections:
1. **Equations**: The equations are formatted using LaTeX for clarity. These will be rendered properly in Markdown viewers (like GitHub).
2. **Installation Instructions**: The steps are provided for cloning the repository, installing dependencies, and running the project.
3. **Usage Instructions**: A guide to prepare the input data and run the simulation. Example Python code is provided for clarity.
4. **Example Plots**: Shows how to visualize the input and encoded signal using `matplotlib`.




































