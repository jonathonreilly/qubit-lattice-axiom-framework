"""Independent phase-quadrature/direct charge-photon comparison helper."""
import numpy as np
from scipy.linalg import eigh

AUDIT_TIMEOUT_SEC = 600


def independent_cavity(c, flux, EL, N=24, K=7):
    n = np.arange(-N, N + 1)
    EC, J, asymmetry = c['params']
    phi = np.arange(1024) * 2 * np.pi / 1024
    left, right = J * (1 + asymmetry), J * (1 - asymmetry)
    potential = -left * np.cos(phi) - right * np.cos(phi + 2*np.pi*flux)
    potential += (left**2 * np.cos(2*phi) + right**2 * np.cos(2*phi + 4*np.pi*flux)) / (4*EL)
    F = np.exp(1j * phi[:, None] * n) / np.sqrt(len(phi))
    Hq = (F.conj().T * potential) @ F + np.diag(4*EC*(n-c['ng'])**2)
    _, U = eigh(Hq)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    H = np.kron(Hq, np.eye(K)) + np.kron(np.eye(len(n)), np.diag(c['Omega_GHz']*np.arange(K)))
    H += c['G_GHz'] * np.kron(np.diag(n), 1j*(a.T-a))
    energies, V = eigh(H)
    bare = np.zeros((len(energies), 2), complex)
    bare[::K, 0] = U[:, 0]
    bare[1::K, 1] = U[:, 0]
    weights = abs(bare.conj().T @ V)**2
    labels = np.argmax(weights, axis=1)
    if labels[0] == labels[1]:
        raise ValueError('Independent cavity labels collided')
    return float(energies[labels[1]] - energies[labels[0]] - c['Omega_GHz'])
