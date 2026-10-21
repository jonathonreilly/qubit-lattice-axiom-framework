"""C9 review / r02: reviewer checks of Step D (geometry + sign), Step G (site elimination),
and the 6-cycle witness of Step (1).  Exact / linear-algebra checks; runs in seconds.

usage: python3 r02_steps.py LOG
"""
from __future__ import annotations

import itertools
import sys

import numpy as np

out = open(sys.argv[1], "x")
npass = nfail = 0


def log(s):
    print(s, flush=True)
    out.write(s + "\n")


def check(ok, msg):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    log(("PASS " if ok else "FAIL ") + msg)


rng = np.random.default_rng(5)

# ---------------- Step D geometry: reviewer's proof is: if q,q' in S with v = q'-q, then for every
# generic l, |l(v)| <= width_l(S) = |l(e)|; by continuity for all l, so v = +-e or 0.
# Test the equivalence "extremal difference = +-e for every generic l  <=>  S is an e-bond"
# on random sets S (|S| = 2..6) in a 5^3 box, plus all 2-point sets, with 60 generic l.
ells = rng.normal(size=(60, 3)) * np.array([1, np.sqrt(2), np.sqrt(3)])
e = np.array([1, 0, 0])


def passes(S):
    S = np.array(S)
    for l in ells:
        v = S @ l
        t = S[np.argmax(v)] - S[np.argmin(v)]
        if not (np.array_equal(t, e) or np.array_equal(t, -e)):
            return False
    return True


box = [np.array(p) for p in itertools.product(range(5), repeat=3)]
bad = 0
cnt = 0
for size in range(2, 7):
    for _ in range(4000):
        idx = rng.choice(len(box), size=size, replace=False)
        S = [box[i] for i in idx]
        isbond = size == 2 and abs(S[0] - S[1]).tolist() in ([1, 0, 0],)
        if passes(S) != isbond:
            bad += 1
        cnt += 1
pairs_ok = sum(passes([box[i], box[j]]) for i, j in itertools.combinations(range(len(box)), 2))
check(bad == 0, f"D geometry: {cnt} random sets, 'all generic extremal differences = +-e' iff e-bond (bad={bad})")
check(pairs_ok == 4 * 25, f"D geometry: among all 2-point sets in 5^3, exactly the 100 x-bonds pass (got {pairs_ok})")

# ---------------- Step D sign: a + bP self-adjoint unitary non-scalar with tr/4 = 1/2
P = np.zeros((4, 4))
for i, j in itertools.product(range(2), repeat=2):
    P[2 * j + i, 2 * i + j] = 1
sols = []
for a, b in itertools.product([-1, -0.5, 0, 0.5, 1], repeat=2):
    M = a * np.eye(4) + b * P
    if np.allclose(M @ M, np.eye(4)) and abs(b) > 0 and abs(np.trace(M) / 4 - 0.5) < 1e-12:
        sols.append((a, b))
check(sols == [(0, 1)], f"D sign: a+bP self-adjoint unitary, non-scalar, tau=1/2 -> {sols} (expect only (0,1))")

# ---------------- Step G site elimination, exact nullspace:
# vector operators W on sites {0,1,2} (x) 1_3 that commute with P_yz for all y,z in {1,2,3}
# (site 3 plays the 'z outside supp W').  Expect the space to be spanned by sigma_0 (dim 1).
I2 = np.eye(2, dtype=complex)
PA = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]),
      np.array([[1, 0], [0, -1]], dtype=complex)]
EPS = np.zeros((3, 3, 3))
for (a, b, c), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    EPS[a, b, c] = s


def op(o, k, n):
    m = np.array([[1.0 + 0j]])
    for i in range(n):
        m = np.kron(m, o if i == k else I2)
    return m


n = 4
d = 2 ** n
dsub = 8
S = [sum(op(p, k, n) for k in range(n)) / 2 for p in PA]
Id = np.eye(d)
swaps = []
for y, z in itertools.combinations([1, 2, 3], 2):
    swaps.append((Id + sum(op(p, y, n) @ op(p, z, n) for p in PA)) / 2)
# parametrise W^j = X^j (x) 1_2, X^j arbitrary 8x8 (complex): unknowns 3*64
E = np.kron(np.eye(dsub), np.kron(np.eye(1), np.eye(1)))


def embed_vec():
    # map vec(X) (64) -> vec(X (x) 1_2) (256), row-major
    T = np.zeros((d * d, dsub * dsub), dtype=complex)
    for i, j in itertools.product(range(dsub), repeat=2):
        Xij = np.zeros((dsub, dsub)); Xij[i, j] = 1
        T[:, i * dsub + j] = np.kron(Xij, I2).ravel()
    return T


T = embed_vec()
rows = []
Z = np.zeros((d * d, dsub * dsub), dtype=complex)


def adj(A):
    return np.kron(A, Id) - np.kron(Id, A.T)


for a in range(3):
    for j in range(3):
        blk = [Z.copy(), Z.copy(), Z.copy()]
        blk[j] = blk[j] + adj(S[a]) @ T
        for k in range(3):
            if EPS[a, j, k]:
                blk[k] = blk[k] - 1j * EPS[a, j, k] * T
        rows.append(np.hstack(blk))
for Pm in swaps:
    for j in range(3):
        blk = [Z.copy(), Z.copy(), Z.copy()]
        blk[j] = adj(Pm) @ T
        rows.append(np.hstack(blk))
M = np.vstack(rows)
sv = np.linalg.svd(M, compute_uv=False)
null = int((sv < 1e-9 * sv[0]).sum()) + (3 * 64 - len(sv))
check(null == 1, f"G site elimination: vector ops on {{0,1,2}} commuting with all swaps among {{1,2,3}}: dim = {null} (expect 1, sigma_0)")
# without site 3 (only swaps among {1,2}) the space is larger: elimination genuinely needs z outside
rows2 = rows[:9] + rows[9:12]  # vector condition + only P_12
sv2 = np.linalg.svd(np.vstack(rows2), compute_uv=False)
null2 = int((sv2 < 1e-9 * sv2[0]).sum()) + (3 * 64 - len(sv2))
check(null2 > 1, f"G control: commuting only with P_12 (no outside site) leaves dim {null2} > 1")

# ---------------- Step (1) witness: 6-cycle
V = [np.array(v) for v in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1), (1, -1, 0)]]
edges = [(V[i], V[(i + 1) % 6]) for i in range(6)]
vecs = [tuple(b - a) for a, b in edges]
pm_distinct = len({tuple(sorted([v, tuple(-np.array(v))])) for v in vecs}) == 6
# S^- psi: coefficient of each vertex
coef = {}
for i, (a, b) in enumerate(edges):
    for x in (a, b):
        coef[tuple(x)] = coef.get(tuple(x), 0) + (-1) ** i
check(pm_distinct and all(c == 0 for c in coef.values()) and len({tuple(v) for v in V}) == 6,
      f"(1) 6-cycle: distinct vertices, edge vectors pairwise +-distinct, S^- psi = 0")
# orthonormal translates: overlap <psi_0|psi_t> over t in a box
def pairs(t):
    return {frozenset([tuple(a + t), tuple(b + t)]): (-1) ** i for i, (a, b) in enumerate(edges)}
p0 = pairs(np.zeros(3, int))
mx = 0
for t in itertools.product(range(-3, 4), repeat=3):
    if t == (0, 0, 0):
        continue
    pt = pairs(np.array(t))
    mx = max(mx, len(set(p0) & set(pt)))
check(mx == 0, "(1) translates of psi share no pair state (exact, |t|_inf <= 3; disjoint beyond)")

log(f"TOTAL: PASS={npass} FAIL={nfail}")
