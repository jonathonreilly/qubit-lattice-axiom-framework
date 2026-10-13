"""R19-7 s5: are the registered moves (cube + 3 mu8) linearly dependent over F2 with LOCAL (non-wrapping) support?
Embed in an L=10 torus, keep only moves whose base site lies in a b x b x b block (no wrap), count rank deficiency.
A deficiency means XOR-zero products of distinct local moves exist: odd-multiplicity world lines in a path integral,
which pair-insertion QMC updates cannot reach (an ergodicity requirement for any QMC of H(v,bU))."""
import numpy as np, sys, itertools
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
L = 10; V = L**3
for b in [1, 2, 3, 4]:
    vecs = []
    for p in PATTERNS:
        for x in itertools.product(range(b), repeat=3):
            v = np.zeros(6*V, dtype=np.uint8)
            for (d, t) in p:
                y = np.array(x) + np.array(d) + 2   # offset; max extent < 10, no wrap
                assert np.all(y < L)
                s = (y[0]*L + y[1])*L + y[2]; v[t*V + s] ^= 1
            vecs.append(v)
    M = np.array(vecs); r = f2_rank(M)
    print("block %d^3: moves %d  F2 rank %d  local dependencies (nullity) %d" % (b, len(M), r, len(M) - r))
# the single relation in a 3^3 block: which moves (pattern type, base) enter it
b = 3; vecs = []; lab = []
for a, p in enumerate(PATTERNS):
    for x in itertools.product(range(b), repeat=3):
        v = np.zeros(6*V, dtype=np.uint8)
        for (d, t) in p:
            y = np.array(x) + np.array(d) + 2; s = (y[0]*L + y[1])*L + y[2]; v[t*V + s] ^= 1
        vecs.append(v); lab.append((a, x))
M = np.array(vecs); n = len(M)
A = np.concatenate([M, np.eye(n, dtype=np.uint8)], axis=1)
# row-reduce on the first 6V columns; rows that become zero there carry the relation in the identity part
r = 0
for c in range(6*V):
    piv = None
    for i in range(r, n):
        if A[i, c]: piv = i; break
    if piv is None: continue
    A[[r, piv]] = A[[piv, r]]
    nz = np.nonzero(A[:, c])[0]; nz = nz[nz != r]; A[nz] ^= A[r]; r += 1
rel = [i for i in range(n) if not A[i, :6*V].any()]
for i in rel:
    mv = np.nonzero(A[i, 6*V:])[0]
    from collections import Counter
    print("relation: %d moves; by pattern type (0=cube, 1-3=mu8 orientations): %s" % (len(mv), dict(Counter(lab[j][0] for j in mv))))
    X = np.zeros(6*V, dtype=np.uint8)
    for j in mv: X ^= M[j]
    print("   XOR of the relation's moves is zero:", not X.any())
