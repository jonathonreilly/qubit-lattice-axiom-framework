"""R18-10 s8: the declared second family (pattern hops, ext.py) with the dN = 0 filter.
(i) L = 2 exact: filtered classes vs N-sectors (as s2, on the same 1024-state coset);
(ii) L = 3 is skipped (coset dim 78); (iii) L = 6: do the diagonal plane profiles (Lemma P) now change?"""
import numpy as np, itertools
from common import *
from mc import charges, sweeps
from mc10 import sweeps_c, counts
from ext import EXT, move_tables_ext
L = 2; V = L**3; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); d = B.shape[0]
states = np.array([(np.array(c) @ B) % 2 for c in itertools.product([0, 1], repeat=d)])
idx = {s.tobytes(): i for i, s in enumerate(states.astype(np.int8))}
Ns = np.array([[s[t*V:(t+1)*V].sum() for t in range(6)] for s in states])
vecs = []
for p in EXT:
    for x in itertools.product(range(L), repeat=3):
        v = np.zeros(6*V, dtype=np.int64)
        for (dd, t) in p:
            y = np.mod(np.array(x) + np.array(dd), L); s = (y[0]*L + y[1])*L + y[2]; v[t*V + s] ^= 1
        vecs.append(v)
Pd = np.unique(np.array(vecs) % 2, axis=0)
assert all((G @ v) .__mod__(2).sum() == 0 for v in Pd)
inspan = all(((np.array(v) + 0) % 2).tobytes() in {(np.array(s) % 2).astype(np.int64).tobytes() for s in states} for v in Pd)
parent = list(range(len(states)))
def find(a):
    while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
    return a
for i, s in enumerate(states):
    for p in Pd:
        t2 = (s + p) % 2; sgn = t2.astype(int) - s.astype(int)
        if any(sgn[t*V:(t+1)*V].sum() for t in range(6)): continue
        k = idx.get(t2.astype(np.int8).tobytes())
        if k is None: continue
        a, b = find(i), find(k)
        if a != b: parent[a] = b
comp = np.array([find(i) for i in range(len(states))])
split = sum(1 for Nv in set(map(tuple, Ns)) if len(set(comp[(Ns == np.array(Nv)).all(1)])) > 1)
from collections import Counter
print("(i) L=2, extended family: hop moves stay in the coset: %s; classes %d (registered family: 511); N-sectors %d, split: %d; singleton classes %d"
      % (inspan, len(set(comp)), len(set(map(tuple, Ns))), split, sum(1 for c, k in Counter(comp).items() if k == 1)))
L = 6; V = L**3; S, GE, GN = move_tables_ext(L); half = V//2
from mc import move_tables
S0, GE0, GN0 = move_tables(L)
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S0, GE0, GN0, 50, 9, 1)
Nc = counts(n); fl = np.zeros_like(n); dd = 0
while np.abs(Nc - half).sum() > 0 and dd < 2000: sweeps_c(n, g, Nc, L, 0.0, S0, GE0, GN0, 1, 20 + dd, dd % 2, 1, half, fl); dd += 1
prof = lambda n: (n[0].sum(axis=(1, 2)), n[1].sum(axis=(0, 2)), n[2].sum(axis=(0, 1)))
P0 = prof(n)
sweeps_c(n, g, Nc, L, 1.0, S, GE, GN, 2000, 77, 1, 0, half, fl)
P1 = prof(n)
assert np.array_equal(g, charges(n, L)) and np.array_equal(Nc, counts(n))
print("(iii) L=6, extended family, 2000 sweeps at bU = 1: N_xx(x), N_yy(y), N_zz(z) unchanged: %s; N_zz(z) before %s after %s; N_ab - V/2 = %s"
      % (tuple(bool(np.array_equal(a, b)) for a, b in zip(P0, P1)), P0[2], P1[2], counts(n) - half))
