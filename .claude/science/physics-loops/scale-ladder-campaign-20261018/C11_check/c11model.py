"""C11 checker model: own from-scratch build of the 12-mode corner model.  Imports no repo / campaign code.

Definitions (from the campaign docs, B7_check/B18_check conventions):
  modes |v,c>, v in Z^3, c = {d,e} perpendicular unit directions (12 corners)
  on-site edges {a,b}@v -- {a,f}@v (f perp a,b);  link edges {a,b}@v -- {-a,b}@v+a
  Z2 fluxes: square = pi, octant triangle = 0, cube-face plaquette = pi, tube = pi
  hopping amplitude -(-1)^{u_e};  G_g|v,c> = (-1)^{lam.v + tau(c)} |Rv, Rc>
  translation-invariant X|v,c> = sum_a |v+a> X_a |c>
  ** Bloch convention here: X(k) = sum_a X_a exp(-i k.a)  (OPPOSITE sign to C11 / B26_check) **
  covariance: U_R X(R^T k + pi lam) U_R^T = chi(g) X(k).

Differences from C11's model path (B26_check/mymodel.py): S and A0 are built by twisted group averaging of a
single seed entry (not orbit propagation); PSG by brute force over GF(2)^15; letter derivatives analytic
(Daleckii-Krein for exp(iH)), not finite differences.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_v] = "2"
import itertools
import numpy as np

AX = [(1,0,0),(0,1,0),(0,0,1)]
DIRS = AX + [tuple(-x for x in d) for d in AX]
def ip(a, b): return sum(x*y for x, y in zip(a, b))
def ng(a): return tuple(-x for x in a)
def ad(a, b): return tuple(x+y for x, y in zip(a, b))
CORN = [frozenset((d, e)) for i, d in enumerate(DIRS) for e in DIRS[i+1:] if ip(d, e) == 0]
assert len(CORN) == 12
CI = {c: i for i, c in enumerate(CORN)}
FC = np.array([ad(*tuple(c)) for c in CORN])          # f_c = d+e
ANTI = [CI[frozenset(ng(x) for x in c)] for c in CORN]
O3 = (0, 0, 0)

# ---------------------------------------------------------------- edge types, canonical (i,j,s) with i<j or (i==j...)
def canon(i, j, s):
    return (i, j, tuple(s)) if (i, tuple(s)) <= (j, ng(s)) else (j, i, ng(s))
EDGE = {}   # canon -> (index, kind)
for c in CORN:
    for x in c:
        y = [z for z in c if z != x][0]
        for f in DIRS:
            if ip(f, x) == 0 and ip(f, y) == 0:
                key = canon(CI[c], CI[frozenset((x, f))], O3); EDGE.setdefault(key, (len(EDGE), 'on'))
        key = canon(CI[c], CI[frozenset((ng(x), y))], x); EDGE.setdefault(key, (len(EDGE), 'link'))
NE = len(EDGE); assert NE == 36
def eidx(c1, c2, s): return EDGE[canon(CI[c1], CI[c2], s)][0]

def gf2(A, b):
    A = np.array(A, dtype=np.int64) % 2; b = np.array(b, dtype=np.int64) % 2
    M = np.concatenate([A, b[:, None]], axis=1); m, n1 = M.shape; n = n1 - 1; r = 0; piv = []
    for col in range(n):
        p = next((i for i in range(r, m) if M[i, col]), None)
        if p is None: continue
        M[[r, p]] = M[[p, r]]
        for i in range(m):
            if i != r and M[i, col]: M[i] = (M[i] + M[r]) % 2
        piv.append(col); r += 1
    if any(M[i, n] for i in range(r, m)): return None
    x = np.zeros(n, dtype=np.int64)
    for i, col in enumerate(piv): x[col] = M[i, n]
    return x

def loop(seq):
    row = np.zeros(NE, dtype=np.int64)
    for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]):
        row[eidx(c1, c2, tuple(b - a for a, b in zip(p1, p2)))] ^= 1
    return row
LOOPS = []
for d in DIRS:
    perp = [f for f in DIRS if ip(f, d) == 0]; a0 = perp[0]; b0 = [f for f in perp if ip(f, a0) == 0][0]
    rg = [a0, b0, ng(a0), ng(b0)]
    LOOPS.append((loop([(frozenset((d, r)), O3) for r in rg]), 1))
    for i in range(4):
        p, q = rg[i], rg[(i+1) % 4]
        LOOPS.append((loop([(frozenset((d, p)), O3), (frozenset((ng(d), p)), d), (frozenset((ng(d), q)), d), (frozenset((d, q)), O3)]), 1))
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = [tuple(sg[i] * (j == i) for j in range(3)) for i in range(3)]
    LOOPS.append((loop([(frozenset((x, y)), O3), (frozenset((y, z)), O3), (frozenset((z, x)), O3)]), 0))
for d in DIRS:
    for e in DIRS:
        if ip(d, e) == 0:
            LOOPS.append((loop([(frozenset((d, e)), O3), (frozenset((ng(d), e)), d), (frozenset((ng(d), ng(e))), ad(d, e)), (frozenset((d, ng(e))), e)]), 1))
U_E = gf2([r for r, _ in LOOPS], [f for _, f in LOOPS]); assert U_E is not None
assert all(int(r @ U_E) % 2 == f for r, f in LOOPS)

# ---------------------------------------------------------------- proper rotations and PSG (brute force)
ROTM = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3): M[i, p[i]] = s[i]
        if round(np.linalg.det(M)) == 1: ROTM.append(M)
assert len(ROTM) == 24
def rdir(M, d): return tuple(int(x) for x in M @ np.array(d))
def rcor(M, c): return frozenset(rdir(M, d) for d in c)
def a2char(M):
    # A2 of O: -1 on C4 and C2' classes, +1 on E, C3, C2(=C4^2); classify via trace and order
    tr = int(np.trace(M));
    if tr == 3: return 1            # E
    if tr == 0: return 1            # C3
    if tr == 1: return -1           # C4 (trace 1)
    # tr == -1: C2 (about axis, diagonal) or C2' (off-diagonal)
    return 1 if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else -1
ALLB = np.array(list(itertools.product((0, 1), repeat=15)), dtype=np.int64)
EL = sorted(EDGE.items(), key=lambda kv: kv[1][0])
GRP = []
for M in ROTM:
    ok = np.ones(len(ALLB), bool)
    for (i, j, s), (ix, _) in EL:
        im = eidx(rcor(M, CORN[i]), rcor(M, CORN[j]), rdir(M, s))
        rhs = (U_E[ix] + U_E[im]) % 2
        lhs = (ALLB[:, :3] @ np.array(s) + ALLB[:, 3 + i] + ALLB[:, 3 + j]) % 2
        ok &= lhs == rhs
    sols = ALLB[ok]; assert len(sols) == 2
    lam, tau = sols[0][:3], sols[0][3:]
    U = np.zeros((12, 12))
    for c in CORN: U[CI[rcor(M, c)], CI[c]] = (-1.0) ** tau[CI[c]]
    GRP.append(dict(M=M, lam=lam, tau=tau, U=U, chi=a2char(M)))

def conj_g(g, X):
    return {rdir(g['M'], a): (-1.0) ** int(np.dot(g['lam'], a)) * (g['U'] @ B @ g['U'].T) for a, B in X.items()}
def avg(X, twisted=False):
    out = {}
    for g in GRP:
        w = g['chi'] if twisted else 1
        for a, B in conj_g(g, X).items(): out[a] = out.get(a, 0) + w * B / 24
    return {a: B for a, B in out.items() if np.abs(B).max() > 1e-13}
def bl(X, k):
    k = np.asarray(k, float); out = np.zeros((12, 12), complex)
    for a, B in X.items(): out = out + B * np.exp(-1j * np.dot(k, a))
    return out
def bl_d(X, k):
    k = np.asarray(k, float)
    return [sum((-1j * a[i]) * B * np.exp(-1j * np.dot(k, a)) for a, B in X.items()) for i in range(3)]
def dagx(X): return {ng(a): B.conj().T for a, B in X.items()}

# ---------------------------------------------------------------- Hamiltonian pieces
def ham(kind):
    X = {}
    for (i, j, s), (ix, kd) in EDGE.items():
        if kd != kind: continue
        t = -(-1.0) ** U_E[ix]
        X.setdefault(tuple(s), np.zeros((12, 12), complex))[j, i] += t
        X.setdefault(ng(s), np.zeros((12, 12), complex))[i, j] += t
    return X
HON = ham('on')[O3]; HLX = ham('link')
RLX = {a: B / np.sqrt(2) for a, B in HLX.items()}
LAMB = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = [tuple(sg[i] * (j == i) for j in range(3)) for i in range(3)]
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for t in range(3):
        q, r = cy[t], cy[(t + 1) % 3]
        amp = 1j * (-1.0) ** U_E[eidx(q, r, O3)]
        LAMB[CI[r], CI[q]] += amp; LAMB[CI[q], CI[r]] += np.conj(amp)

# S and A0 by group averaging of one seed entry
c0 = CI[frozenset(((1,0,0),(0,1,0)))]
seed = {tuple(FC[c0]): np.zeros((12, 12), complex)}; seed[tuple(FC[c0])][c0, c0] = 1
SX = {a: 12 * B for a, B in avg(seed).items()}
seedA = {O3: np.zeros((12, 12), complex)}; seedA[O3][ANTI[c0], c0] = 1
A0 = 12 * avg(seedA, twisted=True)[O3]
SDIAG = np.array([SX[tuple(FC[c])][c, c] for c in range(12)])
assert np.allclose(np.abs(SDIAG), 1)
def Sk(k, p=1): return np.diag(SDIAG ** p * np.exp(-1j * p * (FC @ np.asarray(k, float))))
def dSk(k, p=1):
    D = Sk(k, p); return [D * (-1j * p * FC[:, i])[None, :] for i in range(3)]   # diag scaling (columns)
RTX = {a: A0 @ B @ A0.conj().T for a, B in RLX.items()}

# D+ = {H_on = 2, Lambda = -2 sqrt2}, D- = {H_on = 2, Lambda = +2 sqrt2}
def esp(M, val, B=None):
    if B is None: B = np.eye(M.shape[0])
    w, V = np.linalg.eigh(B.conj().T @ M @ B); return B @ V[:, np.abs(w - val) < 1e-8]
_H2 = esp(HON, 2.0)
DP = esp(LAMB, -2 * np.sqrt(2), _H2); DM = esp(LAMB, 2 * np.sqrt(2), _H2)
assert DP.shape[1] == 2 and DM.shape[1] == 2
DOUB = {+1: DP, -1: DM}
KST = np.array([1, -1, 1]) * np.pi / 2
KP = {'+k*': KST, '-k*': -KST}

# symmetric on-site algebra by averaging random matrices
def sym_onsite(rng):
    X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    return avg({O3: X})[O3]
def wrapk(x): return (np.asarray(x) + np.pi) % (2 * np.pi) - np.pi
