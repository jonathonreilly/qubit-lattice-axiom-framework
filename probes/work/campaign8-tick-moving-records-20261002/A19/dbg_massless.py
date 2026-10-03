import numpy as np
from core1d import step, packet, plus_band, vgroup
M=64
for K0 in (0.3, -0.3):
    a,b = packet(M, 0.0, K0, 5.0, 20)
    print("K0",K0,"weight on a (right sublattice):", np.sum(np.abs(a)**2).round(6), " v(K0) =", vgroup(K0,0.0))
K = np.array([0.3, -0.3, 2.0])
print("plus_band(K, m=0):", plus_band(K, 0.0))
print("plus_band(K, m=1e-9):", plus_band(K, 1e-9))
