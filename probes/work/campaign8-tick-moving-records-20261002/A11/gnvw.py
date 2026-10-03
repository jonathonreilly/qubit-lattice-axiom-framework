#!/usr/bin/env python3
"""GNVW index (comparator) on a ring of n qubits via the Choi-state mutual-information form
   log2 ind = (1/2) [ I(a_in : b_out) - I(b_in : a_out) ],  a = sites (c-k+1..c), b = (c+1..c+k).
Checked on known cases, then on the 4x4-island edge orbit of the 2D cycle (angular order),
bare and dressed with random local circuits."""
import numpy as np, math, time
from cyc2d import *

t0 = time.time()
rng = np.random.default_rng(3)

def haar2():
    z = (rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))

def apply2(U, n, i, j, G):
    T = U.reshape([2] * n + [2 ** n])
    T = np.tensordot(G.reshape(2, 2, 2, 2), T, axes=([2, 3], [i, j]))
    T = np.moveaxis(T, [0, 1], [i, j])
    return T.reshape(2 ** n, 2 ** n)

def brickwork(n, depth):
    U = np.eye(2 ** n, dtype=complex)
    for layer in range(depth):
        for i in range(layer % 2, n - (n % 2 == 1 and layer % 2 == 0), 2):
            U = apply2(U, n, i, (i + 1) % n, haar2())
    return U

def perm_unitary(n, f):           # content of ring site i goes to ring site f[i]
    idx = np.arange(2 ** n)
    bits = (idx[:, None] >> (n - 1 - np.arange(n))[None, :]) & 1
    newbits = np.zeros_like(bits)
    newbits[:, f] = bits
    new = (newbits << (n - 1 - np.arange(n))[None, :]).sum(1)
    P = np.zeros((2 ** n, 2 ** n))
    P[new, idx] = 1.0
    return P

def entropy(psi, axes, n2):
    rest = [a for a in range(n2) if a not in axes]
    M = np.transpose(psi, list(axes) + rest).reshape(2 ** len(axes), -1)
    ev = np.linalg.eigvalsh(M @ M.conj().T)
    ev = ev[ev > 1e-14]
    return float(-(ev * np.log2(ev)).sum())

def log2ind(U, n, c, k=2):
    psi = (U / math.sqrt(2 ** n)).reshape([2] * (2 * n))      # axes: out_0..out_{n-1}, in_0..in_{n-1}
    a = [(c - t) % n for t in range(k)]
    b = [(c + 1 + t) % n for t in range(k)]
    out = lambda S: [s for s in S]
    inn = lambda S: [n + s for s in S]
    I = lambda A, B: entropy(psi, A, 2 * n) + entropy(psi, B, 2 * n) - entropy(psi, A + B, 2 * n)
    return 0.5 * (I(inn(a), out(b)) - I(inn(b), out(a)))

n = 10
right = perm_unitary(n, [(i + 1) % n for i in range(n)])
cases = {"identity": np.eye(2 ** n), "right shift": right, "left shift": right.T,
         "brickwork depth 2": brickwork(n, 2),
         "layer o shift o layer (range 3)": brickwork(n, 1) @ right @ brickwork(n, 1)}
for name, U in cases.items():
    vals = [log2ind(U, n, c, k=3) for c in range(n)]
    print(f"[ring n={n}, k=3] {name}: log2 ind at all {n} cuts = {np.round(vals, 10).tolist()}")

# edge orbit of the 4x4 island, ring in ccw angular order around the island centre
L = 24
lk = box(L, 10, 10, 4, 4); cc = (11.5, 11.5)
pi, path = run_cycle(L, lk)
orb = orbits(pi)
assert len(orb) == 1
sites = np.array(orb[0])
x, y = rel(L, sites, cc)
order = sites[np.argsort(np.arctan2(y, x))]                 # ccw order
posn = {int(s): i for i, s in enumerate(order)}
f = [posn[int(pi[s])] for s in order]                       # ring position i -> f[i]
m = len(order)
steps = [((f[i] - i + m // 2) % m) - m // 2 for i in range(m)]
print(f"[edge] 4x4 island orbit: {m} sites; ring displacement of each item per cycle (ccw +): {steps}")
E = perm_unitary(m, f)
vals = [log2ind(E, m, c) for c in range(m)]
print(f"[edge] bare edge unitary: log2 ind at all {m} cuts = {np.round(vals, 10).tolist()}")
Ed = brickwork(m, 1) @ E @ brickwork(m, 1)
vals = [log2ind(Ed, m, c, k=3) for c in range(m)]
print(f"[edge] dressed (random layer before and after, range 3): log2 ind (k=3) = {np.round(vals, 8).tolist()}")
print(f"time {time.time()-t0:.1f}s")
