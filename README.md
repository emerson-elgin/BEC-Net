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

## Installation

To set up this project, make sure you have the following dependencies installed:

```bash
pip install numpy matplotlib


