"""Check the temporal wave-function term omitted from cls1_loop4's speeds."""

import itertools

import numpy as np


pi = np.pi
s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.diag([1.0, -1.0]).astype(complex)
sigma = [sx, sy, sz]
light = [
    np.array([pi, 0.0, 0.0]),
    np.array([0.0, pi, 0.0]),
    np.array([0.0, 0.0, pi]),
]
carriers = [
    np.zeros(3),
    np.array([0.0, pi, pi]),
    np.array([pi, 0.0, pi]),
    np.array([pi, pi, 0.0]),
]


def same_corner(a, b):
    delta = (a - b) / (2 * pi)
    return np.allclose(delta, np.round(delta))


def self_energy(n, mass, y0, y1, q):
    grid = 2 * pi * (np.arange(n) + 0.5) / n
    ell = np.stack(np.meshgrid(grid, grid, grid, indexing="ij"), -1).reshape(-1, 3)
    omega = np.sqrt(mass**2 + (4 * np.sin(ell / 2) ** 2).sum(1))
    couplings = [y0, y1, y1, y1]
    spatial = np.zeros((6, 6), dtype=complex)
    temporal = np.zeros((6, 6), dtype=complex)
    for c, qc in enumerate(light):
        for cp, qcp in enumerate(light):
            for i1, k1 in enumerate(carriers):
                for i2, k2 in enumerate(carriers):
                    if not same_corner(k1 + k2, qc + qcp):
                        continue
                    internal = k1 - qc - q - ell
                    sine = np.sin(internal)
                    energy = np.sqrt((sine**2).sum(1))
                    factor = couplings[i1] * np.conj(couplings[i2])
                    weight = 1 / (2 * omega * energy * (omega + energy))
                    vector = (sine * weight[:, None]).mean(0)
                    block = sum(sigma[a] * vector[a] for a in range(3))
                    spatial[2 * cp : 2 * cp + 2, 2 * c : 2 * c + 2] += factor * block
                    temporal[2 * cp : 2 * cp + 2, 2 * c : 2 * c + 2] += (
                        factor * np.mean(1 / (2 * omega * (omega + energy) ** 2)) * s0
                    )
    return spatial, temporal


def inv_sqrt(matrix):
    values, vectors = np.linalg.eigh(matrix)
    return (vectors / np.sqrt(values)) @ vectors.conj().T


corner_diagonal = np.kron(np.eye(3), np.ones((2, 2))).astype(bool)
h0 = [
    np.kron(np.diag([np.cos(corner[b]) for corner in light]), sigma[b])
    for b in range(3)
]
rng = np.random.default_rng(17)
directions = [x / np.linalg.norm(x) for x in rng.normal(size=(80, 3))]

for phase in (0.0, 0.07):
    n = 48
    delta = 0.01
    y0 = 0.33 * np.exp(1j * phase)
    y1 = 0.33
    derivatives = []
    for b in range(3):
        step = delta * np.eye(3)[b]
        plus, _ = self_energy(n, 0.1, y0, y1, step)
        minus, _ = self_energy(n, 0.1, y0, y1, -step)
        derivatives.append((plus - minus) / (2 * delta))
    _, temporal = self_energy(n, 0.1, y0, y1, np.zeros(3))

    spatial_off = [matrix.copy() for matrix in derivatives]
    for matrix in spatial_off:
        matrix[corner_diagonal] = 0
    temporal_off = temporal.copy()
    temporal_off[corner_diagonal] = 0
    normalize = inv_sqrt(np.eye(6) + temporal_off)

    spreads = {"spatial_only": 0.0, "temporal_only": 0.0, "both": 0.0}
    for direction in directions:
        bare = sum(h0[b] * direction[b] for b in range(3))
        ds = sum(spatial_off[b] * direction[b] for b in range(3))
        cases = {
            "spatial_only": bare + ds,
            "temporal_only": normalize @ bare @ normalize,
            "both": normalize @ (bare + ds) @ normalize,
        }
        for name, matrix in cases.items():
            speeds = np.sort(np.abs(np.linalg.eigvalsh(matrix)))
            spreads[name] = max(spreads[name], speeds[-1] - speeds[0])
    print(
        "phase", phase,
        "max|Z_off|", np.max(np.abs(temporal_off)),
        "spreads", spreads,
    )
