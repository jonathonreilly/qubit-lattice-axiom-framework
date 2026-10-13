"""R18-10 s3: fragmentation indicators for the registered LOCAL dipole-conserving move set at L = 4, 6.
States are exact canonical samples (N-biased GC chain, kept only at N_ab = V/2). For each, count the balanced
(dD = 0) local flips available (out of 4V) and how many of them do not raise sum gamma^2.
A state with 0 balanced flips is a frozen singleton class (exact fragmentation)."""
import numpy as np, sys
from mc import *
from mc10 import counts
from mcpair import sweeps_bias, flip
L_list = [4, 6]
def balanced(n, g, L, S, GE, GN):
    nb = 0; nlow = 0; dN = np.zeros(6, dtype=np.int64); dum = np.zeros(6, dtype=np.int64)
    for a in range(S.shape[0]):
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    dN[:] = 0; dE = flip(n, g, L, S, GE, GN, a, x, y, z, dN); flip(n, g, L, S, GE, GN, a, x, y, z, dum)
                    if np.all(dN == 0):
                        nb += 1; nlow += int(dE <= 0)
    return nb, nlow
for L in L_list:
    V = L**3; S, GE, GN = move_tables(L); half = V//2
    for bU in [0.0, 2.0, 3.0, 4.0]:
        n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S, GE, GN, 50, 3, 1)
        Nc = counts(n); sweeps_bias(n, g, Nc, L, bU, 0.3, half, S, GE, GN, 3000, 5, 1)
        res = []; it = 0
        while len(res) < 30 and it < 20000:
            sweeps_bias(n, g, Nc, L, bU, 0.3, half, S, GE, GN, 20, 100 + it, it % 2); it += 1
            if np.any(Nc != half): continue
            nb, nlow = balanced(n, g, L, S, GE, GN); res.append((nb, nlow, (g**2).sum()/4/(3*V)))
        r = np.array(res)
        print("L=%d bU=%.1f: %d canonical samples; balanced local flips per state: min %d mean %.1f (of %d); non-raising: min %d mean %.1f; frozen states %d; E/edge mean %.4f"
              % (L, bU, len(r), r[:, 0].min(), r[:, 0].mean(), 4*V, r[:, 1].min(), r[:, 1].mean(), int((r[:, 0] == 0).sum()), r[:, 2].mean()), flush=True)
