"""R18-10 s3b: per canonical state (L = 6), available moves that do not raise sum gamma^2:
unfiltered registered flips (the GC chain's), balanced registered flips (local chain), balanced flips of the extended family."""
import numpy as np
from mc import *
from mc10 import counts
from mcpair import sweeps_bias, flip
from ext import move_tables_ext
L = 6; V = L**3; S, GE, GN = move_tables(L); SX, GEX, GNX = move_tables_ext(L); half = V//2
def count(n, g, S, GE, GN):
    tot = 0; bal = 0; balnr = 0; nr = 0; dN = np.zeros(6, dtype=np.int64); dum = np.zeros(6, dtype=np.int64)
    for a in range(S.shape[0]):
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    dN[:] = 0; dE = flip(n, g, L, S, GE, GN, a, x, y, z, dN); flip(n, g, L, S, GE, GN, a, x, y, z, dum)
                    tot += 1; nr += int(dE <= 0)
                    if np.all(dN == 0): bal += 1; balnr += int(dE <= 0)
    return tot, nr, bal, balnr
for bU in [1.0, 2.0, 3.0]:
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S, GE, GN, 50, 3, 1)
    Nc = counts(n); sweeps_bias(n, g, Nc, L, bU, 0.3, half, S, GE, GN, 3000, 5, 1)
    R = []; it = 0
    while len(R) < 15 and it < 20000:
        sweeps_bias(n, g, Nc, L, bU, 0.3, half, S, GE, GN, 20, 100 + it, it % 2); it += 1
        if np.any(Nc != half): continue
        a = count(n, g, S, GE, GN); b = count(n, g, SX, GEX, GNX); R.append(a + b)
    R = np.array(R, float).mean(0)
    print("bU=%.1f (15 canonical states, L=6): registered: %d proposals, non-raising %.1f (GC chain); balanced %.1f, balanced non-raising %.1f | extended family: %d proposals, balanced %.1f, balanced non-raising %.1f"
          % (bU, R[0], R[1], R[2], R[3], R[4], R[6], R[7]), flush=True)
