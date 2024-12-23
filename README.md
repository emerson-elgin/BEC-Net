# BEC-Net: Dynamic Quantum Reservoirs Using Bose-Einstein Condensates

**BEC-Net** is a cutting-edge scientific tool designed to simulate and analyze dynamic quantum reservoirs based on Bose-Einstein Condensates (BECs). This tool explores the unique properties of BECs to address challenges in quantum computing, machine learning, and nonlinear system modeling.

---

## Features
- **Simulations** of quantum reservoirs using BEC-inspired dynamics.
- Implements **reservoir computing** for tasks such as signal processing and classification.
- Modular architecture for easy experimentation and expansion.
- Visualizes input-output dynamics and performance metrics.

---

## Mathematical Framework

### Bose-Einstein Condensate Dynamics
The dynamics of a Bose-Einstein Condensate are governed by the **Gross-Pitaevskii Equation (GPE)**, a nonlinear Schrödinger equation:
$$
i\hbar \frac{\partial \psi(\mathbf{r}, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}) + g|\psi(\mathbf{r}, t)|^2 \right) \psi(\mathbf{r}, t)
$$

Where:
- \( \psi(\mathbf{r}, t) \): Wavefunction of the condensate.
- \( \hbar \): Reduced Planck's constant.
- \( m \): Mass of the particles in the condensate.
- \( V(\mathbf{r}) \): External potential.
- \( g \): Interaction strength.

### Reservoir Computing
Reservoir computing processes input signals through a high-dimensional dynamical system. The reservoir state is represented as:
$$
\mathbf{h}(t+1) = f(\mathbf{W}_{in}\mathbf{u}(t) + \mathbf{W}\mathbf{h}(t)),
$$
where:
- \( \mathbf{h}(t) \): State of the reservoir at time \( t \).
- \( \mathbf{u}(t) \): Input signal at time \( t \).
- \( \mathbf{W}_{in} \): Input weight matrix.
- \( \mathbf{W} \): Reservoir weight matrix.
- \( f \): Nonlinear activation function.

---

## Simulations

### Example Input Signal
The tool processes various input signals such as sine waves or chaotic signals. For example, a sine wave:
$$
u(t) = \sin(\omega t)
$$
can be generated and visualized.

### Simulation Outputs
The following visualizations are generated:
1. **Input Signal**: Plots of the original signal.
2. **Reservoir States**: High-dimensional states produced by the BEC reservoir.
3. **Output Signal**: Mapped outputs from the reservoir.

### Visualization Example
Below is a sample simulation output:

| Input Signal | Reservoir State Evolution | Output Signal |
|--------------|----------------------------|---------------|
| ![Input Signal](https://via.placeholder.com/200) | ![Reservoir State](https://via.placeholder.com/200) | ![Output Signal](https://via.placeholder.com/200) |

---

## Installation

### Prerequisites
- Python 3.8+
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/itveryeasy/BEC-Net.git
