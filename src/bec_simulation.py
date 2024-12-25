import numpy as np
from scipy.fftpack import fftn, ifftn

def simulate_bec(initial_state, potential_fn, time_steps, dt, grid_size, dx, g):
    kx = np.fft.fftfreq(grid_size, d=dx) * 2 * np.pi
    ky = np.fft.fftfreq(grid_size, d=dx) * 2 * np.pi
    KX, KY = np.meshgrid(kx, ky)
    K2 = KX**2 + KY**2

    psi = initial_state
    densities = []
    for t in range(time_steps):
        V = potential_fn(t * dt)
        psi = psi * np.exp(-1j * V * dt / 2)
        psi_k = fftn(psi)
        psi_k = psi_k * np.exp(-1j * K2 * dt)
        psi = ifftn(psi_k)
        psi = psi * np.exp(-1j * V * dt / 2)
        densities.append(np.abs(psi)**2)
    return densities

