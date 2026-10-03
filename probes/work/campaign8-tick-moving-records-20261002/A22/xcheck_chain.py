#!/usr/bin/env python3
"""Independent cross-check of the identical-excitation ('chain') result: two excitations on a ring of S qubit sites,
evolved with the exact qubit gates of A19's round (exp(-i theta SWAP) per bond, applied to the local occupancy
(n_s, n_s+1) in the 2-excitation basis x1 < x2), collision of two band packets (A19 core1d convention), then the
doubled weight = weight with both cell momenta within pi/2 of K = pi (packets start near K = 0)."""
import sys, numpy as np, scipy.sparse as sp
from core1d import packet, PI
S = 256; Mc = S // 2; m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3; k0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
w = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0; T = int(sys.argv[4]) if len(sys.argv) > 4 else 70
pairs = [(a, b) for a in range(S) for b in range(a + 1, S)]
index = {p: i for i, p in enumerate(pairs)}; D = len(pairs)
G = lambda th: np.cos(th) * np.eye(4) - 1j * np.sin(th) * np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
def layer(th, parity):
    g = G(th); rows, cols, vals = [], [], []
    bond_of = lambda x: (x - parity) // 2          # bond id containing site x for this layer
    for i, (a, b) in enumerate(pairs):
        ba, bb = bond_of(a) % (S // 2), bond_of(b) % (S // 2)
        sites = lambda bid: ((2 * bid + parity) % S, (2 * bid + parity + 1) % S)
        if ba == bb:   # both on one bond: local state |11>
            rows.append(i); cols.append(i); vals.append(g[3, 3]); continue
        # independent one-excitation bond blocks (|10>,|01>) for each particle; other bonds empty (vacuum, global phase dropped together with the same factor)
        outs = []
        for x, bid in ((a, ba), (b, bb)):
            s0, s1 = sites(bid)
            loc = 2 if x == s0 else 1                # |n_s0 n_s1> index: |10> = 2, |01> = 1
            outs.append([(s0, g[2, loc]), (s1, g[1, loc])])
        for (x1, v1) in outs[0]:
            for (x2, v2) in outs[1]:
                p = (min(x1, x2), max(x1, x2))
                rows.append(index[p]); cols.append(i); vals.append(v1 * v2 / g[0, 0])   # relative to emptiness: divide one vacuum-bond factor
    return sp.csr_matrix((vals, (rows, cols)), shape=(D, D))
Le, Lo = layer(PI / 2, 0), layer(PI / 2 - m, 1)
# check unitarity
v = np.random.default_rng(0).normal(size=D) + 0j; v /= np.linalg.norm(v)
print(f"S={S} m={m} k0={k0} w={w} T={T}: |U v| = {np.linalg.norm(Lo @ (Le @ v)):.12f}")
# initial state: symmetrised product of packets A (K=+k0, left) and B (K=-k0, right)
aA, bA = packet(Mc, m, k0, w, Mc // 2 - 22); aB, bB = packet(Mc, m, -k0, w, Mc // 2 + 22)
pA = np.empty(S, complex); pA[0::2] = aA; pA[1::2] = bA
pB = np.empty(S, complex); pB[0::2] = aB; pB[1::2] = bB
psi2 = np.outer(pA, pB); psi2 = psi2 + psi2.T
x = np.array([psi2[a, b] for (a, b) in pairs]); x /= np.linalg.norm(x)
for t in range(T):
    x = Lo @ (Le @ x)
M2 = np.zeros((S, S), complex)
for i, (a, b) in enumerate(pairs):
    M2[a, b] = M2[b, a] = x[i] / np.sqrt(2)
F = {(c1, c2): np.fft.fft2(M2[c1::2, c2::2]) / Mc for c1 in (0, 1) for c2 in (0, 1)}
Wt = sum(np.abs(F[k]) ** 2 for k in F)
K = 2 * PI * np.arange(Mc) / Mc
dbl = np.abs(((K - PI) + PI) % (2 * PI) - PI) < PI / 2
Dw = Wt[np.ix_(dbl, dbl)].sum() / Wt.sum()
print(f"doubled weight (both cell momenta near pi) = {Dw:.4f}; total {Wt.sum():.6f}")
