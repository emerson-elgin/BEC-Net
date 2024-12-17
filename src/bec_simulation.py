import numpy as np
from scipy.fftpack import fft2, ifft2

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
m = 1.44e-25          # Mass of rubidium atom (kg)
g = 1e-3              # Nonlinear interaction strength
dx = 0.5e-6           # Spatial step (m)
dt = 1e-4             # Time step (s)

class BECReservoir:
    def __init__(self, L=50, time_steps=500):
        self.L = L
        self.time_steps = time_steps
        self.x = np.linspace(-L/2, L/2, L)
        self.X, self.Y = np.meshgrid(self.x, self.x)
        self.psi = np.exp(-((self.X**2 + self.Y**2)/(2 * (L/10)**2)))  # Initial Gaussian
        self.psi = self.psi / np.linalg.norm(self.psi)  # Normalize
        self.kx = 2 * np.pi * np.fft.fftfreq(L, d=dx)
        self.kx, self.ky = np.meshgrid(self.kx, self.kx)
        self.K = (hbar**2 / (2 * m)) * (self.kx**2 + self.ky**2)

    def dynamic_potential(self, t, amplitude=0.1, frequency=0.05):
        """Dynamic Gaussian input perturbation."""
        return amplitude * np.exp(-((self.X - 5*np.sin(frequency*t))**2 + self.Y**2)/2)

    def simulate(self, input_signal):
        outputs = []
        for t in range(self.time_steps):
            V_dynamic = self.dynamic_potential(t) * input_signal[t]
            self.psi *= np.exp(-1j * dt * (V_dynamic + g * np.abs(self.psi)**2) / hbar)
            psi_k = fft2(self.psi)
            psi_k *= np.exp(-1j * dt * self.K / hbar)
            self.psi = ifft2(psi_k)
            self.psi /= np.linalg.norm(self.psi)
            outputs.append(np.abs(self.psi).flatten())  # Save output density
        return np.array(outputs)
