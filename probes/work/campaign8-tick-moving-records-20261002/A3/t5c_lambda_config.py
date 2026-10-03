"""Is the lambda (Im K) flow non-zero on the configuration space of two records (brickwork)?"""
import numpy as np
import t5_two_records as m
from common import mh_split
m.rng = np.random.default_rng(4)
worst = 0.0
for k in range(50):
    Psi = m.rng.normal(size=m.nc) + 1j * m.rng.normal(size=m.nc); Psi /= np.linalg.norm(Psi)
    gates = m.layer_gates(m.bondsA if k % 2 == 0 else m.bondsB)
    U = np.eye(m.nc, dtype=complex)
    for G in gates: U = G @ U
    pi, K, _ = mh_split(U, Psi, m.nc, 1)
    worst = max(worst, float(np.abs(K.imag - K.imag.T).max()))
print(f"two records, brickwork layer: max |Im K - Im K^T| over 50 random linked states = {worst:.3e}")
