#!/usr/bin/env python3
"""C6_check part C: illustrations for the registration lemma (not proofs).

(1) A different ffiid block-centre rule (coding radius 2): x is a centre iff its iid label is the strict
    maximum of its l_inf radius-2 window.  The superlattice (5Z^3) Bragg amplitude max_Q |S(Q)| should
    scale like N_c^(-1/2) (no registration), i.e. sqrt(N_c) max_Q |S(Q)| = O(1) as L grows.
(2) Controls showing which hypotheses are load-bearing (both are inside Definition 1 of the B3 note but
    outside its ffiid corollary): (a) a deterministic periodic start slice B = 5Z^3 of planted centres
    with the same exclusion rule gives perfect registration |S(Q)| = 1; (b) a position-dependent
    (non-covariant) rule F_y depending on y mod 5 does the same with coding radius 0.
(3) Exact: dimension of the centre of the even part of Cl(2n) is 2 (n = 1..4), so a faithful
    representation of the even algebra of n complex modes needs 2 * 2^(n-1) = 2^n dimensions = n qubits.
"""
import itertools
import numpy as np
from scipy.ndimage import maximum_filter

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(7)
Qs = [2 * np.pi * np.array(q) / 5 for q in itertools.product(range(5), repeat=3) if any(q)]
Qs = np.array(Qs)


def bragg(pts):
    ph = np.exp(1j * pts @ Qs.T)
    return np.abs(ph.mean(0)).max()


rows = []
for L in (20, 40, 60, 80):
    vals = []
    for trial in range(3):
        x = rng.random((L, L, L))
        mx = maximum_filter(x, size=5, mode='wrap')
        pts = np.argwhere(x == mx).astype(float)
        vals.append((len(pts), bragg(pts)))
    Nc = np.mean([v[0] for v in vals]); S = np.mean([v[1] for v in vals])
    rows.append((L, Nc, S, S * np.sqrt(Nc)))
    print(f"  L={L}: N_c ~ {Nc:.0f}, mean max_Q |S(Q)| = {S:.4f}, sqrt(N_c) * that = {S*np.sqrt(Nc):.2f}", flush=True)
r = [x[3] for x in rows]
check("ffiid rule: sqrt(N_c) * max_Q|S(Q)| stays O(1) (within [1, 4]) from L = 20 to 80 while |S| falls (no Bragg peak)",
      all(1 <= v <= 4 for v in r) and rows[-1][2] < rows[0][2] / 2.5, f"{[round(v,2) for v in r]}")

# controls
L = 40
cent = np.zeros((L, L, L), bool)
cent[::5, ::5, ::5] = True   # planted start slice (deterministic, periodic)
pts = np.argwhere(cent).astype(float)
check("control (a): deterministic periodic start slice B = 5Z^3 registers perfectly (|S| = 1): Definition 1 allows it, the lemma needs B = empty",
      abs(bragg(pts) - 1) < 1e-12)
y = np.indices((L, L, L)).reshape(3, -1).T
pts = y[(y % 5 == 0).all(1)].astype(float)
check("control (b): a position-dependent rule F_y (y mod 5) registers with coding radius 0: the lemma needs translation covariance",
      abs(bragg(pts) - 1) < 1e-12)


# (3) centre of the even Clifford algebra
def majoranas(n):
    X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
    out = []
    for k in range(n):
        for P in (X, Y):
            ops = [Z] * k + [P] + [I2] * (n - k - 1)
            m = ops[0]
            for o in ops[1:]:
                m = np.kron(m, o)
            out.append(m)
    return out


ok = True
for n in range(1, 5):
    g = majoranas(n)
    basis = []
    for S in itertools.chain.from_iterable(itertools.combinations(range(2 * n), r) for r in range(0, 2 * n + 1, 2)):
        m = np.eye(2 ** n, dtype=complex)
        for s in S:
            m = m @ g[s]
        basis.append(m)
    # centre: elements of the even algebra commuting with all even generators g_a g_b
    gens = [g[a] @ g[b] for a in range(2 * n) for b in range(a + 1, 2 * n)]
    B = np.array([b.ravel() for b in basis]).T                     # columns = even basis
    rowsC = []
    for h in gens:
        rowsC.append(np.array([(h @ b - b @ h).ravel() for b in basis]).T)
    C = np.vstack(rowsC)
    centre_dim = len(basis) - np.linalg.matrix_rank(C, tol=1e-9)
    ok &= centre_dim == 2 and len(basis) == 2 ** (2 * n - 1)
    print(f"  n={n} modes: even algebra dim {len(basis)} = 2*(2^{n-1})^2, centre dim {centre_dim}")
check("even algebra of n modes = M_{2^(n-1)} + M_{2^(n-1)} (dim and 2-dim centre), so a faithful rep needs n qubits (n = 12 for a corner site)", ok)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
