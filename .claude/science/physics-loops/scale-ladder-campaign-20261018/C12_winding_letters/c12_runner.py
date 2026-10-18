#!/usr/bin/env python3
"""C12 (scale-ladder campaign): W3 for O-covariant translation-invariant letters of the corner fermion.

Supplied model only. No physical identification. Same-family worker, unchecked.
Model build (Sections 0-2) is COPIED verbatim from
  /home/user/wt-lanes/scripts/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18.py
(lines 33-410: imports, gauge solve, PSG lifts, S, A0, R_L, D+-, T1 frames tau^(b)); nothing is imported.
New sections (C12):
  A  symmetry rules for W3 (orientation, transpose/conjugate/inverse; I.K search and letter types; O_h test)
  B  construction: Dirac-twist letter D^(b) on the invariant doublet D_b; covariance, unitarity; W3 = +-1 by
     (i) midpoint integral with analytic derivatives under grid refinement, (ii) exact preimage count, (iii) control
  C  finite-range letters: distance >= 2 from D (consistency check of the K1 argument)
  D  consequences: the step D^(b) at E = pi; steps D^(b) x (S, R_L, ...) screened with the B20 criterion
Usage: python3 c12_runner.py   (3 threads)
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import itertools, sys, time
import numpy as np
from scipy.linalg import schur

SLOW = '--slow' in sys.argv
T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(20261018)

# =====================================================================================================================
# Section 0: model build (ported from the campaign's independent build)
# =====================================================================================================================
print("=== 0. model build ===", flush=True)
DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def add(a, b): return tuple(x + y for x, y in zip(a, b))
CORN = sorted({frozenset((d, e)) for d in DIRS for e in DIRS if dot(d, e) == 0},
              key=lambda c: tuple(-x for x in add(*tuple(c))))
CI = {c: i for i, c in enumerate(CORN)}
FACE = np.array([add(*tuple(c)) for c in CORN])
ANTI = [CI[frozenset(neg(x) for x in c)] for c in CORN]
Z0 = (0, 0, 0)
def other(c, x): return [y for y in c if y != x][0]
def perp2(a, b): return [f for f in DIRS if dot(f, a) == 0 and dot(f, b) == 0]


def ekey(c1, c2, s):
    a = (CI[c1], CI[c2], tuple(s)); b = (CI[c2], CI[c1], neg(s)); return min(a, b)


ET = {}; ONSITE = []; LINK = []
for c in CORN:
    for x in c:
        y = other(c, x)
        for f in perp2(x, y):
            k_ = ekey(c, frozenset((x, f)), Z0)
            if k_ not in ET: ET[k_] = len(ET); ONSITE.append(k_)
        k_ = ekey(c, frozenset((neg(x), y)), x)
        if k_ not in ET: ET[k_] = len(ET); LINK.append(k_)
NT = len(ET)


def gf2_solve(A, b):
    A = np.array(A, np.uint8) % 2; b = np.array(b, np.uint8) % 2
    m, n = A.shape; M = np.concatenate([A, b[:, None]], 1); piv = []; r = 0
    for col in range(n):
        nz = [i for i in range(r, m) if M[i, col]]
        if not nz: continue
        M[[r, nz[0]]] = M[[nz[0], r]]
        for i in range(m):
            if i != r and M[i, col]: M[i] ^= M[r]
        piv.append(col); r += 1
        if r == m: break
    if M[r:, n].any(): return None, r, None
    x = np.zeros(n, np.uint8)
    for i, col in enumerate(piv): x[col] = M[i, n]
    kern = []
    for f in [j for j in range(n) if j not in piv]:
        v = np.zeros(n, np.uint8); v[f] = 1
        for i, col in enumerate(piv): v[col] = M[i, f]
        kern.append(v)
    return x, r, kern


def loop_row(seq):
    row = np.zeros(NT, np.uint8)
    for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]):
        row[ET[ekey(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]] ^= 1
    return row


def ring(d):
    a0 = [f for f in DIRS if dot(f, d) == 0][0]; b0 = [f for f in DIRS if dot(f, d) == 0 and dot(f, a0) == 0][0]
    return [a0, b0, neg(a0), neg(b0)]


LOOPS = []   # (row, flux in units of pi)
for d in DIRS:
    rg = ring(d)
    LOOPS.append((loop_row([(frozenset((d, r)), Z0) for r in rg]), 1))                                  # square
    for i in range(4):
        p, q = rg[i], rg[(i + 1) % 4]
        LOOPS.append((loop_row([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]), 1))             # tube
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
    LOOPS.append((loop_row([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]), 0))  # triangle
for d in DIRS:
    for e in DIRS:
        if dot(d, e) != 0: continue
        LOOPS.append((loop_row([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                (frozenset((neg(d), neg(e))), add(d, e)), (frozenset((d, neg(e))), e)]), 1))  # plaquette
u, _, _ = gf2_solve([r for r, _ in LOOPS], [f for _, f in LOOPS])
check("0.1 12 corners, 36 edge types (24 on-site, 12 link); flux system (square = plaquette = tube = pi, triangle = 0) "
      "has a translation-invariant Z2 gauge solution", len(CORN) == 12 and NT == 36 and len(ONSITE) == 24 and len(LINK) == 12
      and u is not None and all((r @ u) % 2 == f for r, f in LOOPS))


def all_oh():
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = sg[i]
            out.append(M)
    return out


OH = all_oh()
def rd(M, d): return tuple(int(x) for x in M @ np.array(d))
def rc(M, c): return frozenset(rd(M, d) for d in c)


def chiA2(M):
    p = [int(np.nonzero(M[i])[0][0]) for i in range(3)]
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])


def psg(M):
    A = []; b = []
    for (i1, i2, s), t in ET.items():
        row = np.zeros(15, np.uint8); row[:3] = np.array(s) % 2; row[3 + i1] ^= 1; row[3 + i2] ^= 1
        A.append(row); b.append(u[t] ^ u[ET[ekey(rc(M, CORN[i1]), rc(M, CORN[i2]), rd(M, s))]])
    x, _, kern = gf2_solve(A, b)
    return x, kern


PSG = []; psg_ok = True
for M in OH:
    x, kern = psg(M); psg_ok &= x is not None
    PSG.append(dict(M=M, lam=x[:3].astype(int), tau=x[3:].astype(int)))
for g in PSG:
    U = np.zeros((12, 12))
    for c in CORN: U[CI[rc(g['M'], c)], CI[c]] = (-1.0) ** g['tau'][CI[c]]
    g['U'] = U; g['chi'] = chiA2(g['M']) if round(np.linalg.det(g['M'])) == 1 else None
PROPER = [g for g in PSG if round(np.linalg.det(g['M'])) == 1]
check("0.2 every one of the 48 O_h elements has a gauge-dressed lift (lam_R, tau_R) solving the PSG equations over GF(2)",
      psg_ok and len(PROPER) == 24)


def conjG(g, X):
    return {rd(g['M'], a): (-1.0) ** int(np.dot(g['lam'], a)) * g['U'] @ B @ g['U'].T for a, B in X.items()}


def bloch(X, k):
    k = np.asarray(k, float); out = np.zeros((12, 12), complex)
    for a, B in X.items(): out += B * np.exp(1j * np.dot(k, a))
    return out


def bloch_grad(X, k):
    k = np.asarray(k, float)
    return [sum(B * 1j * a[j] * np.exp(1j * np.dot(k, a)) for a, B in X.items()) for j in range(3)]


def mul(X, Y):
    Z = {}
    for a, A in X.items():
        for b, B in Y.items():
            c = add(a, b); Z[c] = Z.get(c, 0) + A @ B
    return {a: B for a, B in Z.items() if np.abs(B).max() > 1e-13}


def dag(X): return {neg(a): B.conj().T for a, B in X.items()}


def ham(kind):
    X = {}
    for (i1, i2, s) in (ONSITE if kind == 'on' else LINK):
        amp = -(-1.0) ** u[ET[(i1, i2, s)]]
        X.setdefault(s, np.zeros((12, 12), complex))[i2, i1] += amp
        X.setdefault(neg(s), np.zeros((12, 12), complex))[i1, i2] += amp
    return X


HON = ham('on'); HLINK = ham('link')
RL = {a: B / np.sqrt(2) for a, B in HLINK.items()}
LAM = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q, r = cy[a_], cy[(a_ + 1) % 3]
        amp = 1j * (-1.0) ** u[ET[ekey(q, r, Z0)]]
        LAM[CI[r], CI[q]] += amp; LAM[CI[q], CI[r]] += np.conj(amp)


def orbit_solve(target_of, chi_fn, c0=0):
    """Monomial letter: column c -> (row target_of(c)[0], displacement target_of(c)[1]), coefficient fixed by covariance."""
    z = {c0: 1.0 + 0j}; changed = True
    while changed:
        changed = False
        for g in PROPER:
            for c in list(z):
                i, a = target_of(c); Rc = CI[rc(g['M'], CORN[c])]
                val = (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c] + g['tau'][i]) * z[c] / chi_fn(g)
                i2, a2 = target_of(Rc)
                if (CI[rc(g['M'], CORN[i])], rd(g['M'], a)) != (i2, a2): return None
                if Rc in z:
                    if abs(z[Rc] - val) > 1e-12: return None
                else: z[Rc] = val; changed = True
    X = {}
    for c, zc in z.items():
        i, a = target_of(c); X.setdefault(a, np.zeros((12, 12), complex))[i, c] += zc
    return X


c_xy = CI[frozenset(((1, 0, 0), (0, 1, 0)))]
S1 = orbit_solve(lambda c: (c, tuple(FACE[c])), lambda g: 1, c0=c_xy)          # diagonal shift {d,e}@v -> v+d+e
A0X = orbit_solve(lambda c: (ANTI[c], Z0), lambda g: g['chi'], c0=c_xy)          # antipodal on-site map (A2)
SDIAG = np.array([S1[tuple(FACE[c])][c, c] for c in range(12)])
def Sk(k, p=1): return np.diag(SDIAG ** p * np.exp(1j * p * FACE @ np.asarray(k, float)))
def dSk(k, p=1):
    d = SDIAG ** p * np.exp(1j * p * FACE @ np.asarray(k, float))
    return [np.diag(1j * p * FACE[:, i] * d) for i in range(3)]
A0 = A0X[Z0]
RTX = mul(mul({Z0: A0}, RL), {Z0: A0.conj().T})


def eigsp(M, lam):
    w, V = np.linalg.eigh(M); return V[:, np.abs(w - lam) < 1e-6]


HON0 = bloch(HON, np.zeros(3))
DPM = eigsp(HON0, 2.0)
DP = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, -2 * np.sqrt(2))
DM = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, 2 * np.sqrt(2))
DOUB = {+1: DP, -1: DM}

kr = rng.uniform(-np.pi, np.pi, 3)
evon = np.sort(np.linalg.eigvalsh(HON0)); evl = np.sort(np.linalg.eigvalsh(LAM))
s3 = np.sqrt(3); s2 = np.sqrt(2)
ok_on = all(np.sum(np.abs(evon - t) < 1e-9) > 0 for t in (-1 - s3, s3 - 1, 2.0)) and np.all(np.min(np.abs(evon[:, None] - np.array([-1 - s3, s3 - 1, 2.0])[None]), 1) < 1e-9)
ok_l = np.all(np.min(np.abs(evl[:, None] - np.array([-2 * s2, -s2, s2, 2 * s2])[None]), 1) < 1e-9)
ok_hl = np.allclose(bloch(HLINK, kr) @ bloch(HLINK, kr), 2 * np.eye(12), atol=1e-12)
check("0.3 H_on has spectrum {-1-sqrt3, sqrt3-1, 2}, Lambda has {+-sqrt2, +-2sqrt2}, H_link(k)^2 = 2 (random k)",
      ok_on and ok_l and ok_hl)
ok_S = np.allclose(Sk(kr) @ Sk(kr).conj().T, np.eye(12)) and np.allclose(A0 @ A0, -np.eye(12)) and DP.shape == (12, 2) and DM.shape == (12, 2)
check("0.4 S is a unitary diagonal shift with signs fixed by covariance; A0^2 = -1; D+ = {H_on = 2, Lambda = -2sqrt2} and "
      "D- = {H_on = 2, Lambda = +2sqrt2} are 2-dimensional", ok_S)

KST = np.array([1, -1, 1]) * np.pi / 2
KPTS = {'+k*': KST, '-k*': -KST}
EPS = np.zeros((3, 3, 3))
for i, j, k_ in itertools.permutations(range(3)):
    EPS[i, j, k_] = np.linalg.det(np.eye(3)[[i, j, k_]])
def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))

# =====================================================================================================================
# Section 1: F1-F3
# =====================================================================================================================
print("\n=== 1. F1-F3: little group, double cover, decomposition of the 12 ===", flush=True)
ok = all(np.allclose(wrap(g['M'].T @ k0 + np.pi * g['lam'] - k0), 0, atol=1e-12) for k0 in KPTS.values() for g in PROPER)
check("F1 all 24 proper rotations fix +k* and -k* (R^T k + pi lam = k mod 2pi): little group O, rho(g) = U_R", ok)


def find_rot(M):
    for i, g in enumerate(PROPER):
        if np.array_equal(g['M'], M): return i


ok = True; signs = set()
for g in PROPER:
    for h in PROPER:
        p = g['U'] @ h['U']; q = PROPER[find_rot(g['M'] @ h['M'])]['U']
        s_ = [s for s in (1, -1) if np.allclose(p, s * q)]; ok &= len(s_) == 1; signs |= set(s_)
check("F2a U_R U_S = +-U_RS with both signs occurring: a projective representation; {+-U_R} has 48 elements",
      ok and signs == {1, -1})


def order(X, n=12):
    Y = X.copy()
    for m in range(1, 49):
        if np.allclose(Y, np.eye(n)): return m
        Y = Y @ X
    return None


def ostat(els, n=12):
    out = {}
    for X in els:
        o = order(X, n); out[o] = out.get(o, 0) + 1
    return dict(sorted(out.items()))


st_a = ostat([s * g['U'] for g in PROPER for s in (1, -1)])
gl23 = []
for a, b, c, d in itertools.product(range(3), repeat=4):
    if (a * d - b * c) % 3:
        gl23.append(np.array([[a, b], [c, d]]))
def ord3(X):
    Y = X.copy()
    for m in range(1, 49):
        if np.array_equal(Y % 3, np.eye(2, dtype=int)): return m
        Y = (Y @ X) % 3
st_gl = {}
for X in gl23:
    o = ord3(X); st_gl[o] = st_gl.get(o, 0) + 1
st_gl = dict(sorted(st_gl.items()))
st_b = ostat([s * (1 if g['chi'] == 1 else 1j) * g['U'] for g in PROPER for s in (1, -1)])
check("F2b element orders of {+-U_R} equal those of an explicit GL(2,3) over F3 (13 involutions): the non-split double cover "
      "isoclinic to 2O; relifting odd elements by i gives 2O (1 involution)",
      st_a == st_gl and st_a.get(2) == 13 and st_b.get(2) == 1, f"{{+-U_R}}: {st_a}; GL(2,3): {st_gl}; relift: {st_b}")
ok = all(np.allclose(g['U'] @ D, D @ (D.conj().T @ g['U'] @ D), atol=1e-12) for g in PROPER for D in (DP, DM))
chiP = np.array([np.trace(DP.conj().T @ g['U'] @ DP) for g in PROPER])
chiM = np.array([np.trace(DM.conj().T @ g['U'] @ DM) for g in PROPER])
chiA = np.array([g['chi'] for g in PROPER])
nP = np.mean(np.abs(chiP) ** 2); nM = np.mean(np.abs(chiM) ** 2); ovl = abs(np.mean(np.conj(chiP) * chiM))
check("F3a D+ and D- are invariant, irreducible and inequivalent", ok and abs(nP - 1) < 1e-12 and abs(nM - 1) < 1e-12 and ovl < 1e-12,
      f"<chi,chi> = {nP:.3f}, {nM:.3f}; |<chi+,chi->| = {ovl:.1e}")
check("F3b chi_{D-}(g) = chi_A2(g) chi_{D+}(g) for all 24 lifts: D- = A2 (x) D+", np.allclose(chiM, chiA * chiP, atol=1e-12))
PG = np.eye(12) - DP @ DP.conj().T - DM @ DM.conj().T
chiG = np.array([np.trace(PG @ g['U']) for g in PROPER]); nG = np.mean(np.abs(chiG) ** 2)
oG = max(abs(np.mean(np.conj(chiG) * chiP)), abs(np.mean(np.conj(chiG) * chiM)))
sv = np.linalg.svd(np.vstack([np.kron(g['U'], g['U']) - np.eye(144) for g in PROPER]), compute_uv=False)
dcomm = int(np.sum(sv < 1e-9))
check("F3c 8-dim complement has <chi,chi> = 4 and no D+- content; commutant dimension 6 = 1 + 1 + 4: 12 = D+ + D- + 2 G3/2, "
      "D+- of multiplicity 1", abs(nG - 4) < 1e-10 and oG < 1e-12 and dcomm == 6, f"<chi_G,chi_G> = {nG:.3f}, commutant {dcomm}")

# =====================================================================================================================
# Section 2: F4-F5, step-3 sign
# =====================================================================================================================
print("\n=== 2. F4-F5: T1 frames; step-3 sign ===", flush=True)


def t1_triples(Din, Dout, chi_letter=1):
    """Null space of rho_out (sum_j R_ij Y_j) rho_in^-1 = chi(g) Y_i (all g); Y: 3 x 2 x 2."""
    rows = []
    for g in PROPER:
        ro = Dout.conj().T @ g['U'] @ Dout; ri = Din.conj().T @ g['U'] @ Din; c = g['chi'] if chi_letter == -1 else 1
        L = np.zeros((12, 12), complex)
        for i in range(3):
            for j in range(3):
                L[4 * i:4 * i + 4, 4 * j:4 * j + 4] += g['M'][i, j] * np.kron(ro, np.linalg.inv(ri).T)
            L[4 * i:4 * i + 4, 4 * i:4 * i + 4] -= c * np.eye(4)
        rows.append(L)
    _, s, Vh = np.linalg.svd(np.vstack(rows))
    return [v.reshape(3, 2, 2) for v in Vh[np.sum(s > 1e-9):].conj()]


TAU = {}
for b, D in DOUB.items():
    sols = t1_triples(D, D); Y = sols[0]
    Y = Y / np.sqrt(np.trace(Y[0] @ Y[0]) / 2)
    if not np.allclose(Y[0], Y[0].conj().T): Y = Y * 1j
    if not np.allclose(Y[0] @ Y[1], 1j * Y[2]): Y = -Y
    herm = all(np.allclose(Y[i], Y[i].conj().T) for i in range(3))
    alg = all(np.allclose(Y[i] @ Y[j], (i == j) * np.eye(2) + 1j * sum(EPS[i, j, k] * Y[k] for k in range(3)))
              for i in range(3) for j in range(3))
    algm = all(np.allclose((-Y[i]) @ (-Y[j]), (i == j) * np.eye(2) + 1j * sum(EPS[i, j, k] * (-Y[k]) for k in range(3)))
               for i in range(3) for j in range(3))
    tr = max(abs(np.trace(Y[i])) for i in range(3))
    check(f"F4 D{'+' if b > 0 else '-'}: T1 triples in End(D) form a {len(sols)}-dim space; normalised: Hermitian, traceless, "
          f"tau_i tau_j = delta_ij + i eps_ijk tau_k, and -tau violates it", len(sols) == 1 and herm and alg and not algm and tr < 1e-12)
    TAU[b] = Y
n1 = len(t1_triples(DP, DM, 1)); n2 = len(t1_triples(DP, DM, -1)); n3 = len(t1_triples(DP, DP, -1)); n4 = len(t1_triples(DM, DM, -1))
check("F5 Hom(D+,D-) contains no T1 and one T2 = T1 (x) A2; End(D+-) contains no T2",
      n1 == 0 and n2 == 1 and n3 == 0 and n4 == 0, f"dims {n1}, {n2}, {n3}, {n4}")


def label_of(B):
    wp = np.linalg.norm(DP.conj().T @ B) ** 2 / 2; wm = np.linalg.norm(DM.conj().T @ B) ** 2 / 2
    if abs(wp - 1) < 1e-8: return +1
    if abs(wm - 1) < 1e-8: return -1
    return None


# =====================================================================================================================
# C12 additions (new code; helpers below re-implemented here)
# =====================================================================================================================
from scipy.linalg import expm


class Letter:
    def __init__(self, name, chi, f, df): self.name, self.chi, self.f, self.df = name, chi, f, df


ZERO3 = [np.zeros((12, 12), complex)] * 3
def L_S(p): return Letter(f"S^{p}", 1, lambda k, p=p: Sk(k, p), lambda k, p=p: dSk(k, p))
def L_block(name, X): return Letter(name, 1, lambda k, X=X: bloch(X, k), lambda k, X=X: bloch_grad(X, k))
def L_const(name, M, chi=1): return Letter(name, chi, lambda k, M=M: M, lambda k: ZERO3)
L_RL = L_block("R_L", RL); L_RT = L_block("Rt", RTX); L_A0 = L_const("A0", A0, -1)


def eig_unitary(W):
    T, Z = schur(W, output='complex'); return np.diag(T), Z


def word_fdf(w):
    def fdf(k):
        Wk = np.eye(12, dtype=complex); d = ZERO3
        for L in w:
            U = L.f(k); dU = L.df(k); d = [d[i] @ U + Wk @ dU[i] for i in range(3)]; Wk = Wk @ U
        return Wk, d
    return fdf


def word_eval(w, k):
    X = np.eye(12, dtype=complex)
    for L in w: X = X @ L.f(k)
    return X


PERMS = [(0, 1, 2, 1), (1, 2, 0, 1), (2, 0, 1, 1), (0, 2, 1, -1), (2, 1, 0, -1), (1, 0, 2, -1)]
def W3(fdf, N, shift=0.5):
    """(1/24 pi^2) int eps_ijk tr(A_i A_j A_k), A = U^dag dU; midpoint rule on an N^3 grid (spectral for smooth maps)."""
    ks = (np.arange(N) + shift) * 2 * np.pi / N - np.pi; tot = 0.0
    for kx in ks:
        for ky in ks:
            for kz in ks:
                Wk, d = fdf(np.array([kx, ky, kz])); A = [Wk.conj().T @ d[i] for i in range(3)]
                tot += sum(s * np.trace(A[i] @ A[j] @ A[l]) for i, j, l, s in PERMS)
    return tot * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2)


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
MDIR = 2.0     # the mass of the Dirac twist; any m in (1,3) gives the same homotopy class


def nhat(q, m=MDIR):
    """n(q) = (sin q, m + sum cos q)/|.| and its q-derivatives (analytic)."""
    n = np.concatenate([np.sin(q), [m + np.cos(q).sum()]]); r = np.linalg.norm(n); nh = n / r
    dn = []
    for i in range(3):
        e = np.zeros(4); e[i] = np.cos(q[i]); e[3] = -np.sin(q[i])
        dn.append((e - nh * (nh @ e)) / r)
    return nh, dn


def pauli_map(fr, m=MDIR, center=np.zeros(3), sign=1):
    """2x2 control U = n4 + i sign n.sigma (frame fr = 3 Hermitian 2x2), q = k - center."""
    def fdf(k):
        nh, dn = nhat(np.asarray(k) - center, m)
        U = nh[3] * np.eye(2) + 1j * sign * sum(nh[i] * fr[i] for i in range(3))
        return U, [d[3] * np.eye(2) + 1j * sign * sum(d[i] * fr[i] for i in range(3)) for d in dn]
    return fdf


def L_D(b, m=MDIR, inv=False):
    """Dirac-twist letter on D_b: 1 - P_b + n4(q) P_b + i n(q).T^(b), q = k - k*; inv: its inverse."""
    Db = DOUB[b]; Pb = Db @ Db.conj().T; T = [Db @ TAU[b][i] @ Db.conj().T for i in range(3)]; s = -1 if inv else 1
    def f(k):
        nh, _ = nhat(np.asarray(k, float) - KST, m)
        return np.eye(12) - Pb + nh[3] * Pb + 1j * s * sum(nh[i] * T[i] for i in range(3))
    def df(k):
        _, dn = nhat(np.asarray(k, float) - KST, m)
        return [d[3] * Pb + 1j * s * sum(d[i] * T[i] for i in range(3)) for d in dn]
    return Letter(f"D{'+' if b > 0 else '-'}{'^-1' if inv else ''}", 1, f, df)


def covariant_err(L, nk=3, chi_of=None):
    err = 0.0
    for _ in range(nk):
        k = rng.uniform(-np.pi, np.pi, 3); Uk = L.f(k)
        for g in PROPER:
            c = g['chi'] if L.chi == -1 else 1
            err = max(err, np.abs(g['U'] @ L.f(g['M'].T @ k + np.pi * g['lam']) @ g['U'].T - c * Uk).max())
    return err


def fit_v(M, b):
    A = np.concatenate([(1j * TAU[b][i]).flatten() for i in range(3)]); y = np.concatenate([M[i].flatten() for i in range(3)])
    v = np.vdot(A, y) / np.vdot(A, A); return v, np.abs(y - v * A).max()


def sphere_chern(Wfun, k0, w0, r=0.05, nth=16, nph=32, nsel=2):
    """FHS Berry flux (outward) of each of the nsel bands nearest w0 (ordered by phase relative to w0; 0 = lowest)."""
    th = np.linspace(0, np.pi, nth + 1); ph = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; vecs = {}
    def at(i, j):
        if i == 0 or i == nth: j = 0
        if (i, j) in vecs: return vecs[(i, j)]
        n = np.array([np.sin(th[i]) * np.cos(ph[j]), np.sin(th[i]) * np.sin(ph[j]), np.cos(th[i])])
        ev, Z = eig_unitary(Wfun(k0 + r * n)); rel = np.angle(ev / w0)
        idx = np.argsort(np.abs(rel))[:nsel]; idx = idx[np.argsort(rel[idx])]
        vecs[(i, j)] = (Z[:, idx], rel[idx]); return vecs[(i, j)]
    out = []
    for sel in range(nsel):
        F = 0.0
        for i in range(nth):
            for j in range(nph):
                V = [c[0][:, [sel]] for c in (at(i, j), at(i + 1, j), at(i + 1, (j + 1) % nph), at(i, (j + 1) % nph))]
                prod = 1.0 + 0j
                for mm in range(4): prod *= np.vdot(V[mm], V[(mm + 1) % 4])
                F += np.angle(prod)
        out.append(F / (2 * np.pi))
    return out


# =====================================================================================================================
print("\n=== A. symmetry rules for W3 ===", flush=True)
# =====================================================================================================================
okdet = all(round(np.linalg.det(g['M'])) == 1 for g in PROPER)
okfix = all(np.allclose(wrap(g['M'].T @ (KST + q) + np.pi * g['lam'] - (KST + g['M'].T @ q)), 0, atol=1e-12)
            for g in PROPER for q in rng.uniform(-np.pi, np.pi, (3, 3)))
check("A1 every covariance map k -> R^T k + pi lam_R has det R = +1 and equals the rotation q -> R^T q about k* "
      "(q = k - k*): orientation-preserving, so the covariance relation reads W3(U) = W3(U) (no constraint)", okdet and okfix)

ctrl = pauli_map(SIG, center=np.zeros(3))
w_c = W3(ctrl, 16)
def tr_map(fdf, op):
    def g(k):
        U, d = fdf(k)
        if op == 'T': return U.T, [x.T for x in d]
        if op == 'C': return U.conj(), [x.conj() for x in d]
        if op == 'I': return U.conj().T, [-U.conj().T @ x @ U.conj().T for x in d]
    return g
def inv_k(fdf):
    def g(k):
        U, d = fdf(-np.asarray(k)); return U, [-x for x in d]
    return g
def rot_k(fdf, M):
    def g(k):
        U, d = fdf(M.T @ np.asarray(k)); return U, [sum(M.T[j, i] * d[j] for j in range(3)) for i in range(3)]
    return g
Mrot = PROPER[7]['M']
vals = dict(T=W3(tr_map(ctrl, 'T'), 16), C=W3(tr_map(ctrl, 'C'), 16), I=W3(tr_map(ctrl, 'I'), 16),
            P=W3(inv_k(ctrl), 16), R=W3(rot_k(ctrl, Mrot), 16))
print(f"   control 2x2 Dirac map (m=2, centre 0): W3 = {w_c.real:+.6f}; U^T {vals['T'].real:+.6f}, U* {vals['C'].real:+.6f}, "
      f"U^-1 {vals['I'].real:+.6f}, U(-k) {vals['P'].real:+.6f}, U(R^T k) {vals['R'].real:+.6f}")
check("A2 control |W3| = 1 (N = 16 midpoint, tol 1e-3; refinement in B3) and the sign rules W3(U^T) = W3(U^-1) = W3(U(-k)) = -W3(U), "
      "W3(U*) = W3(U(R^T k)) = +W3(U)", abs(abs(w_c) - 1) < 1e-3 and abs(vals['T'] + w_c) < 1e-6 and abs(vals['I'] + w_c) < 1e-6
      and abs(vals['P'] + w_c) < 1e-6 and abs(vals['C'] - w_c) < 1e-6 and abs(vals['R'] - w_c) < 1e-6)

# --- I.K: site inversion (c -> -c, k -> -k) times complex conjugation; Bloch action X(k) -> W X(k)* W^T
fam = [HON, HLINK, {Z0: LAM}]
IKsols = []
for sg in itertools.product((1, -1), repeat=12):
    Wm = np.zeros((12, 12))
    for c in range(12): Wm[ANTI[c], c] = sg[c]
    ok = True
    for X in fam:
        for a, B in X.items():
            if not np.allclose(Wm @ X.get(neg(a), np.zeros((12, 12))).conj() @ Wm.T, B, atol=1e-12): ok = False; break
        if not ok: break
    if ok: IKsols.append(Wm)
sq = sorted({int(round(np.trace(Wm @ Wm).real)) for Wm in IKsols})
WIK = [Wm for Wm in IKsols if np.allclose(Wm @ Wm, -np.eye(12))]
check("A3 I.K exists for the hopping family {H_on, H_link, Lambda}: real signed inversion W with W conj(X[-a]) W^T = X[a]; "
      "solutions with W^2 = -1 exist", len(WIK) > 0, f"{len(IKsols)} sign solutions, tr W^2 in {sq}, {len(WIK)} with W^2 = -1")
WI = WIK[0] if WIK else np.eye(12)


def ik_type(L, nk=4):
    eU = eI = 0.0
    for _ in range(nk):
        k = rng.uniform(-np.pi, np.pi, 3); U = L.f(k); X = WI @ U.conj() @ WI.T
        eU = max(eU, np.abs(X - U).max()); eI = max(eI, np.abs(X - U.conj().T).max())
    return eU, eI


def L_expRL(th): return Letter(f"exp({th:.2f} i R_L)", 1, lambda k: expm(1j * th * bloch(RL, k)), None)
def L_expHon(th): return Letter(f"exp({th:.2f} i H_on)", 1, lambda k: expm(1j * th * bloch(HON, k)), None)
types = {}
for L in [L_S(1), L_S(2), L_RL, L_RT, L_A0, L_expRL(0.7), L_expHon(0.9), L_D(1), L_D(-1)]:
    eU, eI = ik_type(L); types[L.name] = ('U' if eU < 1e-9 else '') + ('U^-1' if eI < 1e-9 else '')
    print(f"   I.K type of {L.name:16s}: |W U* W^T - U| = {eU:.1e}, |W U* W^T - U^-1| = {eI:.1e}")
check("A4 the palette has no uniform I.K type: S, S^2 and D+- satisfy W U* W^T = U only; exp(i theta H) (I.K-symmetric H) "
      "satisfies W U* W^T = U^-1 only; R_L, Rt both (involutions)",
      types['S^1'] == 'U' and types['S^2'] == 'U' and types['D+'] == 'U' and types['D-'] == 'U'
      and types['exp(0.70 i R_L)'] == 'U^-1' and types['exp(0.90 i H_on)'] == 'U^-1' and types['R_L'] == 'UU^-1', str(types))

# --- improper elements (O_h): does S lie in an O_h-covariant class?
IMP = [g for g in PSG if round(np.linalg.det(g['M'])) == -1]
def oh_ratio(L, g, nk=3, inv=False):
    cs = []
    for _ in range(nk):
        k = rng.uniform(-np.pi, np.pi, 3); A = g['U'] @ L.f(g['M'].T @ k + np.pi * g['lam']) @ g['U'].T
        B = L.f(k).conj().T if inv else L.f(k); c = np.trace(B.conj().T @ A) / 12
        cs.append((c, np.abs(A - c * B).max()))
    return cs
okS = all(all(e < 1e-9 and abs(abs(c) - 1) < 1e-9 for c, e in oh_ratio(L_S(1), g)) for g in IMP)
okD = all(all(e > 1e-3 for c, e in oh_ratio(L_D(1), g)) for g in IMP)
okDi = any(all(e < 1e-9 for c, e in oh_ratio(L_D(1), g, inv=True)) for g in IMP)
check("A5 S is covariant (up to a constant phase) under all 24 improper O_h lifts as well; D+ is not covariant under any "
      "improper lift (an O_h-covariant class, improper elements acting unitarily, would force W3 = -W3 = 0)",
      okS and okD, f"some improper lift maps D+ to a multiple of D+^-1: {okDi}")

# =====================================================================================================================
print("\n=== B. construction: the Dirac-twist letters D+ and D- ===", flush=True)
# =====================================================================================================================
LD = {b: L_D(b) for b in (1, -1)}; LDi = {b: L_D(b, inv=True) for b in (1, -1)}
eu = ec = ep = ed = ei = 0.0
for b in (1, -1):
    for _ in range(6):
        k = rng.uniform(-np.pi, np.pi, 3); U = LD[b].f(k)
        eu = max(eu, np.abs(U @ U.conj().T - np.eye(12)).max())
        ep = max(ep, max(np.abs(LD[b].f(k + 2 * np.pi * np.eye(3)[i]) - U).max() for i in range(3)))
        ei = max(ei, np.abs(LD[b].f(k) @ LDi[b].f(k) - np.eye(12)).max())
        h = 1e-6; ed = max(ed, max(np.abs((LD[b].f(k + h * np.eye(3)[i]) - LD[b].f(k - h * np.eye(3)[i])) / (2 * h)
                                          - LD[b].df(k)[i]).max() for i in range(3)))
    ec = max(ec, covariant_err(LD[b], 4), covariant_err(LDi[b], 2))
check("B1 D+- are unitary, 2pi-periodic (translation-invariant Bloch matrices), analytic, and A1-covariant: "
      "U_R D(R^T k + pi lam) U_R^T = D(k) for all 24 lifts; analytic derivative = finite difference",
      eu < 1e-12 and ep < 1e-12 and ec < 1e-12 and ei < 1e-12 and ed < 1e-7,
      f"unitarity {eu:.1e}, period {ep:.1e}, covariance {ec:.1e}, inverse {ei:.1e}, derivative {ed:.1e}")

# Fourier decay: D is not finite range (normalisation); coefficients decay exponentially
Nf = 32; ks = 2 * np.pi * np.arange(Nf) / Nf
blk = np.array([[[LD[1].f(np.array([a, b_, c]))[np.ix_([0], [0])] for c in ks] for b_ in ks] for a in ks])
coef = np.abs(np.fft.fftn(blk[..., 0, 0])) / Nf ** 3
rad = np.minimum(np.arange(Nf), Nf - np.arange(Nf)); R1 = rad[:, None, None] + rad[None, :, None] + rad[None, None, :]
dec = [coef[R1 == r].max() for r in range(0, 13, 3)]
print("   max |Fourier coefficient| of D+[0,0] at l1-range 0,3,6,9,12: " + ", ".join(f"{x:.1e}" for x in dec))
check("B2 D+ has infinite range with exponentially decaying hoppings (not finite range)", dec[2] > 1e-8 and dec[-1] < 1e-3 * dec[1])

Qb = {}
for b in (1, -1):    # unitary frame Q with Q^dag tau_i Q = sigma_i (exists by the eps relation, F4)
    w_, V = np.linalg.eigh(TAU[b][2]); V = V[:, ::-1]
    x = V.conj().T @ TAU[b][0] @ V; V = V @ np.diag([1, np.conj(x[0, 1]) / abs(x[0, 1])])
    Qb[b] = V
okQ = all(np.allclose(Qb[b].conj().T @ TAU[b][i] @ Qb[b], SIG[i], atol=1e-12) for b in (1, -1) for i in range(3))
check("B3a tau^(b) is unitarily equivalent to the Pauli triple (orientation fixed by tau_x tau_y = i tau_z)", okQ)
res = {}
for N in (8, 16, 24):
    t1 = time.time()
    res[N] = (W3(word_fdf([LD[1]]), N), W3(word_fdf([LD[-1]]), N), W3(pauli_map(SIG, center=KST), N))
    print(f"   N={N:2d}: W3(D+) = {res[N][0].real:+.8f}, W3(D-) = {res[N][1].real:+.8f}, W3(2x2 Pauli map at k*) = "
          f"{res[N][2].real:+.8f}  (imag {max(abs(r.imag) for r in res[N]):.0e}; {time.time() - t1:.0f}s)", flush=True)
wD = round(res[24][0].real)
check("B3b W3(D+) = W3(D-) = W3(Pauli Dirac map) = w with |w| = 1: midpoint grids N = 8, 16, 24 converge to the integer "
      "(12x12 letters, analytic derivatives)", abs(wD) == 1 and all(abs(res[24][i] - wD) < 1e-6 for i in range(3))
      and abs(res[24][0] - wD) < abs(res[8][0] - wD), f"w = {wD:+d}, |error| at N=24: {abs(res[24][0] - wD):.1e}")
# exact degree: preimage of the south pole (-1,0,0,0) of n-hat
pre = [q for q in itertools.product((0, np.pi), repeat=3) if MDIR + np.cos(q).sum() < 0]
check("B3c exact: n-hat(q) = -e4 only at q = (pi,pi,pi) (sin q = 0 forces q in {0,pi}^3; m + sum cos q < 0 there iff "
      "all three are pi, for 1 < m < 3), a regular preimage, so |deg| = 1 and |W3(D_b)| = 1 for every m in (1,3)",
      len(pre) == 1 and np.allclose(pre[0], np.pi))
ok_m = all(abs(abs(W3(word_fdf([L_D(1, m=mm)]), 16)) - 1) < 2e-2 for mm in (1.5, 2.5))
w_m4 = W3(word_fdf([L_D(1, m=4.0)]), 16)
check("B3d W3 is constant (= w) on 1 < m < 3 and 0 for m = 4 (outside: preimage set empty)", ok_m and abs(w_m4) < 1e-3,
      f"W3(m=4) = {w_m4.real:+.1e}")
fpm = W3(word_fdf([LD[1], LD[-1]]), 16); fpi = W3(word_fdf([LD[1], LDi[1]]), 12)
fA = W3(word_fdf([L_A0, LD[1], L_A0]), 16); fS = W3(word_fdf([LD[1], L_S(1)]), 16)
print(f"   W3(D+ D-) = {fpm.real:+.6f}, W3(D+ D+^-1) = {fpi.real:+.1e}, W3(A0 D+ A0) = {fA.real:+.6f}, W3(D+ S) = {fS.real:+.6f}")
check("B3e additivity: W3(D+ D-) = 2w; W3(D+ D+^-1) = 0; W3(A0 D+ A0) = w (A2 sandwich); W3(D+ S) = w",
      abs(fpm - 2 * wD) < 2e-3 and abs(fpi) < 1e-9 and abs(fA - wD) < 2e-3 and abs(fS - wD) < 2e-3)

# =====================================================================================================================
print("\n=== C. finite-range letters cannot approach D ===", flush=True)
# =====================================================================================================================
def mind_m1(w, N=20):
    ks = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi; best = 9.0
    for k in itertools.product(ks, repeat=3):
        k = np.array(k); X = word_eval(w, k) @ LD[1].f(k).conj().T
        best = min(best, np.min(np.abs(np.linalg.eigvals(X) + 1)))
    return best
fr_words = [[], [L_S(1)], [L_RL], [L_S(1), L_RL], [L_S(2), L_RT, L_S(-1)], [L_A0, L_S(1), L_A0, L_RL]]
dd = [mind_m1(w) for w in fr_words]
print("   min over N=20 grid of dist(-1, spec(V D+^-1)) for V = 1, S, R_L, S R_L, S^2 Rt S^-1, A0 S A0 R_L: "
      + ", ".join(f"{x:.2e}" for x in dd))
check("C1 (illustration; threshold 0.35 ~ grid half-diagonal) for each sampled finite-range V, V D+^-1 comes within grid resolution of eigenvalue -1 (consistent with "
      "sup_k ||V - D+|| = 2, which the K1 argument forces for every finite-range V)", max(dd) < 0.35)

# =====================================================================================================================
print("\n=== D. consequences: nodes of steps containing D ===", flush=True)
# =====================================================================================================================
def spec_min_outside(w, E, centres, rball=0.3, N=24):
    ks = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi; best = 9.0
    for k in itertools.product(ks, repeat=3):
        k = np.array(k)
        if min(np.linalg.norm(wrap(k - c)) for c in centres) < rball: continue
        best = min(best, np.min(np.abs(np.linalg.eigvals(word_eval(w, k)) - np.exp(1j * E))))
    return best


def cone_speeds(w, k0, E, ndir=6, delta=1e-4, npair=1):
    """half splittings of the 2 (or 4) eigenphases nearest E along random directions (Richardson)."""
    out = []
    for _ in range(ndir):
        q = rng.normal(size=3); q /= np.linalg.norm(q); r = []
        for dl in (delta, delta / 2):
            ph = np.angle(np.linalg.eigvals(word_eval(w, k0 + dl * q)) * np.exp(-1j * E))
            r.append(np.sort(ph[np.argsort(np.abs(ph))[:2 * npair]]) / dl)
        out.append((4 * r[1] - r[0]) / 3)
    return np.array(out)


mK = -KST
for b in (1, -1):
    w = [LD[b]]; nm = f"D{'+' if b > 0 else '-'}"
    dmin = spec_min_outside(w, np.pi, [mK])
    sp = cone_speeds(w, mK, np.pi)
    v_b, r_b = fit_v([DOUB[b].conj().T @ LD[b].f(mK).conj().T @ LD[b].df(mK)[i] @ DOUB[b] for i in range(3)], b)
    v_o, _ = fit_v([DOUB[-b].conj().T @ LD[b].f(mK).conj().T @ LD[b].df(mK)[i] @ DOUB[-b] for i in range(3)], -b)
    ch = sphere_chern(lambda k: word_eval(w, k), mK, -1.0)
    print(f"   step {nm}: E = pi reached outside the 0.3-ball about -k* at distance >= {dmin:.3f} (N=24); cone speeds "
          f"{np.round(sp.min(), 6)}..{np.round(sp.max(), 6)}; lemma v on D_b = {v_b.real:+.6f} (res {r_b:.0e}), on D_-b = "
          f"{abs(v_o):.0e}; FHS Berry flux (lower, upper band) = {ch[0]:+.3f}, {ch[1]:+.3f}")
    iso = np.allclose(np.abs(sp), 1 / (3 - MDIR), atol=1e-6) and np.allclose(sp[:, 0], -sp[:, 1], atol=1e-6)
    check(f"D1 step {nm} at E = pi: exactly one node, at -k* (exact: the complement of D_b is frozen at eigenvalue 1, "
          f"and e^(+-i theta) = -1 only at q = (pi,pi,pi)); it is an isolated 2-fold D_b level, an untilted isotropic one-speed "
          f"cone with speed 1/(3-m) = {1 / (3 - MDIR):.3f}, |v| = 1/(3-m) by the C11 lemma, and Berry charge +-1",
          dmin > 0.1 and iso and abs(abs(v_b) - 1 / (3 - MDIR)) < 1e-9 and abs(v_o) < 1e-12
          and abs(abs(ch[0]) - 1) < 1e-3 and abs(ch[0] + ch[1]) < 1e-3)
    if b == 1: chi_pi = round(ch[0])

# the 0-gap of the same SU(2) block (move the frozen complement away with a symmetric on-site reflection C = 1 - 2(1 - P_b))
Pc = np.eye(12) - DOUB[1] @ DOUB[1].conj().T
L_C = L_const("Cbar", np.eye(12) - 2 * Pc)
w = [LD[1], L_C]; nodes0 = [KST + np.array(q) for q in itertools.product((0, np.pi), repeat=3) if not np.allclose(q, np.pi)]
chis = []; speeds = []
for k0 in nodes0:
    ch = sphere_chern(lambda k: word_eval(w, k), k0, 1.0); chis.append(round(ch[0]))
    speeds.append(np.round(np.abs(cone_speeds(w, k0, 0.0, ndir=3)).mean(), 5))
print(f"   step D+ Cbar at E = 0: 7 nodes at k* + {{0,pi}}^3 minus (pi,pi,pi); lower-band charges {chis} (net {sum(chis):+d}); "
      f"speeds {speeds}")
dmin0 = spec_min_outside(w, 0.0, nodes0)
check("D2 same block, E = 0 gap: 7 nodes with net lower-band charge equal to that of the single E = pi node (gap "
      "orientation: the lower band at 0 is the upper band at pi), i.e. net chirality is the same in both gaps and equals "
      "+-W3 (Bessho-Sato-type relation, verified here directly); speeds 1/(m+3), 1/(m+1), 1/(m-1) are unequal, so E = 0 fails "
      "the one-speed criterion", sum(chis) == chi_pi and len(set(speeds)) == 3, f"net(0) = {sum(chis):+d}, "
      f"lower(pi) = {chi_pi:+d}; E=0 outside balls >= {dmin0:.3f}")

# --- D3: screen of short words containing D letters, B20 criterion at the D+- level quasi-energies at +-k*
SCREEN_N = 12
C_P = L_const("C+", np.eye(12) - 2 * DOUB[1] @ DOUB[1].conj().T); C_M = L_const("C-", np.eye(12) - 2 * DOUB[-1] @ DOUB[-1].conj().T)
ALPH = [LD[1], LD[-1], LDi[1], LDi[-1], L_S(1), L_S(-1), L_S(2), L_S(-2), L_RL, L_RT, L_A0, C_P, C_M]
INV = {"D+": "D+^-1", "D-": "D-^-1", "D+^-1": "D+", "D--1": "D-", "S^1": "S^-1", "S^-1": "S^1", "S^2": "S^-2", "S^-2": "S^2"}
INV["D-^-1"] = "D-"


def canon(names):
    rots = [tuple(names[i:] + names[:i]) for i in range(len(names))]; return min(rots)


words = {}
for L in range(1, 4):
    for tup in itertools.product(range(len(ALPH)), repeat=L):
        w = [ALPH[i] for i in tup]; nm = [x.name for x in w]
        if sum(x.chi == -1 for x in w) % 2: continue
        wn = sum(x.name in ("D+", "D-") for x in w) - sum(x.name in ("D+^-1", "D-^-1") for x in w)
        if wn == 0: continue
        if any(INV.get(nm[i]) == nm[(i + 1) % L] for i in range(L)) and L > 1: continue
        if any(nm[i] == nm[(i + 1) % L] and nm[i] in ("R_L", "Rt", "C+", "C-", "A0") for i in range(L)) and L > 1: continue
        words.setdefault(canon(nm), (w, wn))
print(f"   screening {len(words)} cyclic classes of words (length <= 3, prod chi = +1, W3 = w * (#D - #D^-1) != 0)")
ksg = (np.arange(SCREEN_N) + 0.5) * 2 * np.pi / SCREEN_N - np.pi
KG = [np.array(k) for k in itertools.product(ksg, repeat=3)]
npairs = nsurf = nflat = nnear = ncand = 0; cands = []; Elist = []
t0 = time.time()
for key, (w, wn) in words.items():
    EV = np.array([np.linalg.eigvals(word_eval(w, k)) for k in KG])
    c = np.linalg.det(word_eval(w, np.zeros(3))); sc = np.sqrt(c)
    Es = set()
    for k0 in (KST, -KST):  # noqa
        W0 = word_eval(w, k0)
        for b in (1, -1):
            blk = DOUB[b].conj().T @ W0 @ DOUB[b]; Es.add(round(float(np.angle(blk[0, 0])), 9))
    for E in sorted(Es):
        npairs += 1; z = np.exp(1j * E); Elist.append(E)
        d = np.prod(EV - z, axis=1) * np.exp(-6j * E) / sc
        if np.max(np.abs(d.imag)) > 1e-6 * max(1, np.max(np.abs(d))): print("   warn: d not real", key, E)
        dr = d.real; dist = np.min(np.abs(EV - z), axis=1)
        if np.max(np.abs(dr)) < 1e-9: nflat += 1; continue
        if dr.max() > 1e-12 and dr.min() < -1e-12: nsurf += 1; continue
        far = [i for i, k in enumerate(KG) if min(np.linalg.norm(wrap(k - k0)) for k0 in (KST, -KST)) > 0.6]
        if np.min(dist[far]) < 0.15: nnear += 1; continue
        ncand += 1; cands.append((key, E, w, wn, float(np.min(dist[far]))))
print(f"   {npairs} (word, E) pairs: {nsurf} with a Fermi surface (sign change of the real det function), {nflat} flat, "
      f"{nnear} reached (< 0.15) away from +-k*, {ncand} clean on the {SCREEN_N}^3 grid  ({time.time() - t0:.0f}s)")
check("D3 screen ran: every (word, E) pair is classified; E in {0, pi} only (Theta-even words: D+- scalars real). NOTE: the det-sign test is blind at E in {0, pi} for Theta-even words (Kramers pairs cross together), so 0 sign changes is NOT evidence of no Fermi surface",
      npairs == nsurf + nflat + nnear + ncand and all(abs(abs(E) - np.pi) < 1e-8 or abs(E) < 1e-8 for E in Elist))


def classify(w, E, N=20, rball=0.3):
    """B20-type classification at E: multiplicities and cone slopes at +-k*, grid distance elsewhere, lower-band charges."""
    z = np.exp(1j * E); out = dict(nodes=[])
    for kn, k0 in (('+k*', KST), ('-k*', -KST)):
        ev = np.linalg.eigvals(word_eval(w, k0)); mult = int(np.sum(np.abs(ev - z) < 1e-8))
        if mult == 0: continue
        sl = []
        for _ in range(6):
            q = rng.normal(size=3); q /= np.linalg.norm(q); r = []
            for dl in (1e-4, 5e-5):
                ph = np.angle(np.linalg.eigvals(word_eval(w, k0 + dl * q)) / z); r.append(np.sort(ph[np.argsort(np.abs(ph))[:mult]]) / dl)
            sl.append((4 * r[1] - r[0]) / 3)
        sl = np.array(sl); ch = sphere_chern(lambda k: word_eval(w, k), k0, z, nsel=mult)
        a = np.sort(np.abs(sl).ravel()); grp = [a[0]]
        for x in a[1:]:
            if x - grp[-1] > 1e-3 * max(1.0, x): grp.append(x)
        out['nodes'].append(dict(k=kn, mult=mult, speeds=np.round(grp, 5), charge=round(sum(ch[:mult // 2]), 3)))
    out['dist'] = spec_min_outside(w, E, [KST, -KST], rball=rball, N=N)
    return out


npass = 0; passes = []; nfail5 = 0
for key, E, w, wn, dm in cands:
    r = classify(w, E)
    sp = np.sort(np.concatenate([n['speeds'] for n in r['nodes']])) if r['nodes'] else np.array([0.0])
    one = (sp[-1] - sp[0]) < 1e-3 * sp[-1] and sp[0] > 1e-6 and r['dist'] > 0.1
    iso_only = all(len(n['speeds']) == 1 for n in r['nodes']) and sp[0] > 1e-6 and r['dist'] > 0.1
    npass += one
    if not (one or iso_only): nfail5 += 1; continue
    print(f"     {'.'.join(key):22s} E={E:+.4f} W3={wn * wD:+d}: " + "; ".join(
        f"{n['k']} mult {n['mult']} speeds {list(n['speeds'])} charge {n['charge']:+.2f}" for n in r['nodes'])
        + f"; elsewhere >= {r['dist']:.3f}  -> {'ONE-SPEED, CLEAN' if one else ('isotropic, several speeds' if iso_only else 'fail')}")
    if one: passes.append((key, E, wn, r))
check("D5 refined classification ran (N = 20 grid outside 0.3-balls; cone slopes at +-k*). CAUTION: grid-clean at N = 20 is "
      "not evidence of absence (see D6)", True, f"{npass} grid-clean one-speed (word, E) pairs at N=20; {nfail5} of {len(cands)} fail")


# --- D6: grid evidence for the D5 grid-clean steps D_b S^p at E = pi
print("\n=== D6. grid evidence for the steps D_b S^p at E = pi ===", flush=True)


def DSp_batch(b, p, K, m=MDIR):
    Db = DOUB[b]; Pb = Db @ Db.conj().T; T = np.array([Db @ TAU[b][i] @ Db.conj().T for i in range(3)])
    Q = K - KST; n = np.concatenate([np.sin(Q), (m + np.cos(Q).sum(1))[:, None]], 1); n /= np.linalg.norm(n, axis=1)[:, None]
    Dm = (np.eye(12) - Pb)[None] + n[:, 3, None, None] * Pb[None] + 1j * np.einsum('mi,ijk->mjk', n[:, :3], T)
    s = SDIAG[None, :] ** p * np.exp(1j * p * K @ FACE.T)
    return Dm * s[:, None, :]


def dist_batch(b, p, K, E, chunk=20000):
    out = [np.zeros(0)]
    for i in range(0, len(K), chunk):
        ev = np.linalg.eigvals(DSp_batch(b, p, K[i:i + chunk])); out.append(np.min(np.abs(ev - np.exp(1j * E)), axis=1))
    return np.concatenate(out)


kchk = rng.uniform(-np.pi, np.pi, (3, 3))
okb = all(np.allclose(DSp_batch(1, 4, kchk)[i], LD[1].f(kchk[i]) @ Sk(kchk[i], 4), atol=1e-12) for i in range(3))
check("D6a batched D+ S^4 equals the letter product", okb)


def certify_DSp(b, p, E=np.pi, N=60, sub=5, r_in=0.08):
    """||W(k') - W(k)|| <= h (Lx+Ly+Lz) on a cube of half-side h, L_i = sup||d_i D|| + sup||d_i S^p|| <= 1 + |p|
    (m = 2: |n| >= 1 exactly, |d_i n| = 1, so |d_i nhat| <= 1; ||d_i S^p|| = |p| max|f_c,i| = |p|). Bauer-Fike (W(k) normal):
    an eigenvalue e^{iE} of W(k') forces dist(e^{iE}, spec W(k)) <= h sum L. Cells meeting |k + k*| < r_in are excluded."""
    Lsum = 3 * (1.0 + abs(p)); h = np.pi / N; ks = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    K = np.array(list(itertools.product(ks, repeat=3)))
    rr = np.linalg.norm(wrap(K + KST), axis=1); keep = rr > r_in + np.sqrt(3) * h
    d = dist_batch(b, p, K[keep], E); bad = K[keep][d <= Lsum * h]
    h2 = h / sub; offs = (np.arange(sub) - (sub - 1) / 2) * 2 * h2
    O = np.array(list(itertools.product(offs, repeat=3)))
    nunres = 0; nsub = 0; dmin = np.inf; nexcl = 0
    for i in range(0, len(bad), 400):
        Kc = (bad[i:i + 400, None, :] + O[None]).reshape(-1, 3)
        rr2 = np.linalg.norm(wrap(Kc + KST), axis=1); kk = rr2 > r_in + np.sqrt(3) * h2
        nexcl += int(np.sum(~kk))
        d2 = dist_batch(b, p, Kc[kk], E); nsub += len(d2); nunres += int(np.sum(d2 <= Lsum * h2))
        if len(d2): dmin = min(dmin, d2.min())
    return dict(coarse_min=float(d.min()), refined_cells=len(bad), sub_evals=nsub, unresolved=nunres, excluded_sub=nexcl,
                bound_fine=Lsum * h2, fine_min=float(dmin), r_cert=r_in + 2 * np.sqrt(3) * h)


def local_scan(b, p, E=np.pi, r_max=0.3, nr=60, ndir=300):
    """inside the ball: min over rays of dist(e^{iE}, spec)/|q| (numerical scan, not a certificate)"""
    q = rng.normal(size=(ndir, 3)); q /= np.linalg.norm(q, axis=1)[:, None]; worst = np.inf
    for r in np.linspace(r_max / nr, r_max, nr):
        d = dist_batch(b, p, -KST[None] + r * q, E); worst = min(worst, (d / r).min())
    return worst


for b, p in [(1, 4), (-1, -4)]:
    t1 = time.time(); Ng = 40; ks = (np.arange(Ng) + 0.5) * 2 * np.pi / Ng - np.pi
    K = np.array(list(itertools.product(ks, repeat=3))); K = K[np.linalg.norm(wrap(K + KST), axis=1) > 0.3]
    dd = dist_batch(b, p, K, np.pi); j = int(np.argmin(dd))
    ev = np.linalg.eigvals(DSp_batch(b, p, K[j:j + 1]))[0]; mlt = int(np.sum(np.abs(ev + 1) < 1e-8))
    print(f"   D{'+' if b > 0 else '-'} S^{p} at E = pi: on the 40^3 grid outside the 0.3-ball, min dist {dd.min():.1e} at k/pi = "
          f"{np.round(K[j] / np.pi, 3)} (multiplicity {mlt}); fraction of grid points within 0.05: {np.mean(dd < 0.05):.3f} "
          f"({time.time() - t1:.0f}s)", flush=True)
    check(f"D6 D{'+' if b > 0 else '-'} S^{p}, grid-clean at N = 20 (D5), reaches E = pi exactly at generic grid points away from "
          f"+-k* with even multiplicity (Kramers pairs, invisible to the det-sign test): it FAILS the criterion",
          dd.min() < 1e-8 and mlt % 2 == 0)


# --- D4: openness. Perturb the step D+ by small generic O-symmetric exp(i eps H) letters (range <= 2 Hermitian H)
def sym_avg(X):
    acc = {}
    for g in PROPER:
        for a, B in conjG(g, X).items(): acc[a] = acc.get(a, 0) + B / 24
    return acc


def rand_H():
    X = {}
    for a in itertools.product((-2, -1, 0, 1, 2), repeat=3):
        if sum(abs(x) for x in a) <= 2 and rng.random() < 0.5:
            X[a] = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    H = sym_avg(X); Hd = dag(H); Hh = {a: (H.get(a, 0) + Hd.get(a, 0)) / 2 for a in set(H) | set(Hd)}
    nrm = np.linalg.norm(bloch(Hh, rng.uniform(-np.pi, np.pi, 3)), 2)
    return {a: B / nrm for a, B in Hh.items()}


def L_expH(H, eps):
    return Letter(f"exp({eps} iH)", 1, lambda k: expm(1j * eps * bloch(H, k)), None)


npert = 0; nok = 0; rep = []
for t in range(4):
    H1 = rand_H(); H2 = rand_H(); eps = 0.15
    w = [L_expH(H1, eps), LD[1], L_expH(H2, eps)]
    if max(np.abs(L_expH(H1, eps).f(kk) @ L_expH(H1, eps).f(kk).conj().T - np.eye(12)).max() for kk in rng.uniform(-3, 3, (2, 3))) > 1e-10: continue
    W0 = word_eval(w, mK); blk = DOUB[1].conj().T @ W0 @ DOUB[1]
    sc_err = np.abs(blk - blk[0, 0] * np.eye(2)).max(); Ep = float(np.angle(blk[0, 0]))
    ev0 = np.linalg.eigvals(W0); others = np.sort(np.abs(ev0 - np.exp(1j * Ep)))[2]
    dmin = spec_min_outside(w, Ep, [mK], rball=0.3, N=20)
    sp = np.abs(cone_speeds(w, mK, Ep, ndir=4))
    ch = sphere_chern(lambda k: word_eval(w, k), mK, np.exp(1j * Ep))
    npert += 1; good = sc_err < 1e-10 and others > 0.2 and dmin > 0.1 and np.ptp(sp) < 1e-5 and abs(abs(ch[0]) - 1) < 1e-3
    nok += good; rep.append((round(Ep, 4), round(others, 3), round(dmin, 3), round(float(sp.mean()), 5), round(ch[0], 3)))
print("   perturbed steps exp(i eps H1) D+ exp(i eps H2), eps = 0.15: (E', other-level gap at -k*, grid distance from e^{iE'} "
      "outside the 0.3-ball (N=20), cone speed, lower-band charge):")
for r_ in rep: print("     ", r_)
check("D4 the single-node property is open: for small generic O-symmetric perturbations the node quasi-energy moves to the "
      "D+ scalar E' at -k*, which stays an isolated 2-fold isotropic one-speed cone of charge +-1, and E' is reached nowhere "
      "else on the grid (grid evidence, not a certificate)", npert >= 3 and nok == npert, f"{nok}/{npert}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - T0:.0f}s)")
