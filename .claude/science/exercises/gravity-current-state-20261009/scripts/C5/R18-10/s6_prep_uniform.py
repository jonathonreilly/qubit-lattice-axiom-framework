"""R18-10 s6 preparation: half-filled states (all N_ab = V/2) whose diagonal planar profiles are uniform
(N_aa(plane) = L^2/2 for every plane): the most favourable Krylov sector of the registered local chain, where the
frozen scalar-longitudinal channel S_aa(k || e_a) vanishes for every axis k != 0. Usage: L bprep seed out.npy"""
import numpy as np, sys
from mc import *
from mc10 import counts
from mcpair import drive_planar
L, bprep, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
V = L**3; S, GE, GN = move_tables(L)
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S, GE, GN, 50, seed, 1)
sweeps(n, g, L, bprep, S, GE, GN, 300, seed + 1, 1)
obj = -1; it = 0
while obj != 0 and it < 400:
    obj = drive_planar(n, g, L, bprep, S, GE, GN, 5, seed + 10 + it, it % 2); it += 1
assert np.array_equal(g, charges(n, L))
print("L=%d prep bU=%.1f: objective %d after %d blocks; N - V/2 = %s; zz profile %s; E/edge %.4f" % (L, bprep, obj, it, counts(n) - V//2, n[2].sum(axis=(0, 1)), (g**2).sum()/4/(3*V)))
np.save(out, n.astype(np.int8))
