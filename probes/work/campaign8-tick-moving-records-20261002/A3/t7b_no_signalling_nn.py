"""Check 7b: two-tick no-signalling when the one-site-per-tick limit actually binds.

Record A lives on sites 0..3 (active bonds (0,1),(2,3)), record B on sites 4..7 (bonds
(4,5),(6,7)); linked possibilities Psi(a,b), 16 configurations.  A's setting s picks the two
gates in A's region; B's setting r picks B's gates.  Allowed transitions: each record stays
in its active bond (so the 'redraw from the odds' coupling is NOT allowed).

LP questions per random instance:
  (NS)  does some equivariant, one-site coupling exist for all four setting pairs whose
        two-tick statistics at B ignore s and at A ignore r?
  (LOC) does such a coupling exist whose two-tick statistics at A equal A's own minimal
        bond rule (computed from A's own odds) and likewise at B?
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from common import haar_unitary, rand_state

rng = np.random.default_rng(31)
nA = nB = 4
pairsA = [(0, 1), (2, 3)]


def region_gate(gates):
    U = np.zeros((4, 4), complex)
    for (a, b), G in zip(pairsA, gates):
        U[np.ix_([a, b], [a, b])] = G
    return U


allowed_1 = np.zeros((4, 4), bool)
for (a, b) in pairsA:
    for i in (a, b):
        for j in (a, b):
            allowed_1[i, j] = True
allowed = np.kron(allowed_1, allowed_1).astype(bool)      # config index 4a+b


def local_min_coupling(p, pn):
    """A single record's own minimal bond rule on its 4 sites (bonds (0,1),(2,3))."""
    pi = np.zeros((4, 4))
    for (a, b) in pairsA:
        f = p[a] - pn[a]
        if f >= 0:
            pi[a, b] = f; pi[a, a] = p[a] - f; pi[b, b] = p[b]
        else:
            pi[b, a] = -f; pi[b, b] = p[b] + f; pi[a, a] = p[a]
    return pi


def solve(Psi, UA, UB, mode):
    P = np.abs(Psi) ** 2
    pairs = [(i, j) for i in range(16) for j in range(16) if allowed[i, j]]
    m = len(pairs)
    nv = 4 * m
    A, b = [], []
    def var(s, r, k):
        return (2 * s + r) * m + k
    for s, r in itertools.product(range(2), repeat=2):
        Pn = np.abs(np.kron(UA[s], UB[r]) @ Psi) ** 2
        for i in range(16):
            row = np.zeros(nv)
            for k, (x, y) in enumerate(pairs):
                if x == i:
                    row[var(s, r, k)] = 1
            A.append(row); b.append(P[i])
        for j in range(15):
            row = np.zeros(nv)
            for k, (x, y) in enumerate(pairs):
                if y == j:
                    row[var(s, r, k)] = 1
            A.append(row); b.append(Pn[j])
    pA = P.reshape(4, 4).sum(1); pB = P.reshape(4, 4).sum(0)
    for r in range(2):
        for (bb, bb2) in itertools.product(range(4), repeat=2):
            if not allowed_1[bb, bb2]:
                continue
            if mode == 'NS':
                row = np.zeros(nv)
                for k, (x, y) in enumerate(pairs):
                    if x % 4 == bb and y % 4 == bb2:
                        row[var(0, r, k)] += 1; row[var(1, r, k)] -= 1
                A.append(row); b.append(0.0)
            else:
                pBn = (np.abs(np.kron(UA[0], UB[r]) @ Psi) ** 2).reshape(4, 4).sum(0)
                target = local_min_coupling(pB, pBn)[bb, bb2]
                for s in range(2):
                    row = np.zeros(nv)
                    for k, (x, y) in enumerate(pairs):
                        if x % 4 == bb and y % 4 == bb2:
                            row[var(s, r, k)] = 1
                    A.append(row); b.append(target)
    for s in range(2):
        for (aa, aa2) in itertools.product(range(4), repeat=2):
            if not allowed_1[aa, aa2]:
                continue
            if mode == 'NS':
                row = np.zeros(nv)
                for k, (x, y) in enumerate(pairs):
                    if x // 4 == aa and y // 4 == aa2:
                        row[var(s, 0, k)] += 1; row[var(s, 1, k)] -= 1
                A.append(row); b.append(0.0)
            else:
                pAn = (np.abs(np.kron(UA[s], UB[0]) @ Psi) ** 2).reshape(4, 4).sum(1)
                target = local_min_coupling(pA, pAn)[aa, aa2]
                for r in range(2):
                    row = np.zeros(nv)
                    for k, (x, y) in enumerate(pairs):
                        if x // 4 == aa and y // 4 == aa2:
                            row[var(s, r, k)] = 1
                    A.append(row); b.append(target)
    res = linprog(np.zeros(nv), A_eq=np.array(A), b_eq=np.array(b), bounds=(0, None), method='highs')
    return res.status == 0


trials = 200
ns_ok, loc_ok, born_ok = 0, 0, 0
for tr in range(trials):
    Psi = rand_state(16, rng)
    UA = [region_gate([haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]
    UB = [region_gate([haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]
    ns_ok += solve(Psi, UA, UB, 'NS')
    loc_ok += solve(Psi, UA, UB, 'LOC')
print(f"{trials} random instances (linked Psi on 16 configurations, two settings each side)")
print(f"  (NS)  two-tick no-signalling both ways achievable : {ns_ok}/{trials}")
print(f"  (LOC) each record's two-tick statistics = its own minimal bond rule : {loc_ok}/{trials}")
