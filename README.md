# BEC-Net: Dynamic Quantum Reservoirs Using Bose-Einstein Condensates

## Overview

BEC-Net is a project designed to simulate dynamic quantum reservoirs using **Bose-Einstein Condensates (BECs)**, which can be applied to neuromorphic computing and quantum machine learning. This project models a quantum system using the concept of a reservoir computing architecture, with BECs acting as the dynamic medium for information processing. The system is trained using a readout layer to predict time-series data.

The input data to the system is encoded and fed into the BEC simulation, where the time evolution of the system is computed. The features extracted from this simulation are then used to train a readout layer that predicts output signals.

---

## Project Structure

The project is organized as follows:

- **`src/`**: Contains all the source code files:
  - `bec_simulation.py`: Simulates the evolution of BECs over time.
  - `input_encoder.py`: Encodes the input signal for the simulation.
  - `feature_extractor.py`: Extracts features from the simulated densities.
  - `readout_layer.py`: Implements the training and prediction of the readout layer.
  
- **`data/`**: Contains the input signal data (`sine_wave_data.npy`).

- **`main.py`**: The main script that runs the entire simulation, including encoding the input, simulating the BEC, extracting features, training the readout layer, and making predictions.

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





















## Installation

To set up this project, make sure you have the following dependencies installed:

```bash
pip install numpy matplotlib




















