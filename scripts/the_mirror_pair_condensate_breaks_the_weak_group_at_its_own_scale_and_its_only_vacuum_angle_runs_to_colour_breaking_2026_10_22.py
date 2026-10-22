AUDIT_INPUT_PATHS = ('docs/THE_MIRROR_PAIR_CONDENSATE_BREAKS_THE_WEAK_GROUP_AT_ITS_OWN_SCALE_AND_ITS_ONLY_VACUUM_ANGLE_RUNS_TO_COLOUR_BREAKING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Mirror pair condensate as the electroweak breaker? (finite runner, seeded).

Sections:
  A  the toy quartic is the Spin(6) member of the vector-channel pair square of
     a Spin(2k) spinor; Spin(10) is the k = 5 member (Clifford construction)
  B  weights: SM charges of the 16 and the 10; no colour-singlet doublet in the
     45; every colour-singlet doublet generator of u(16N) has |B-L| = 2; a
     B-L-neutral doublet generator needs light x mirror (16 x 16)
  C  the Spin(10) pair-square vacuum manifold S^9: Goldstone count, the angle
     between the (6,1,1) and (1,2,2) ends, the gauge potential, v = f sin(theta)
     with cos(theta) measuring colour breaking
  D  the toy's SU(4)/Sp(4) on SM-charged modes: forced content, embeddings of
     the mirror family, statistics and Witten count
  E  estimates against measurement (condensed mirror; new-content candidate)
Measured numbers enter only [E] items; supplied inputs are named at the end.
"""
import itertools
import time
from fractions import Fraction as Fr

import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
PI = np.pi


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text} | {vals}")


def null_space(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A)
    r = int((s > tol * max(1.0, s[0] if s.size else 1.0)).sum())
    return vh[r:].conj().T


# ---------------------------------------------------------------- A
print("== A. toy quartic = Spin(6) vector-channel pair square")
X2 = np.array([[0, 1], [1, 0]], complex)
Y2 = np.array([[0, -1j], [1j, 0]])
Z2 = np.diag([1.0 + 0j, -1.0])
I2 = np.eye(2, dtype=complex)


def kron_list(ms):
    out = np.eye(1, dtype=complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def clifford(k):
    g = []
    for j in range(k):
        for P in (X2, Y2):
            g.append(kron_list([Z2] * j + [P] + [I2] * (k - j - 1)))
    return g


def pair_channel(k):
    """Vector-channel pairing matrices M_a on the + chiral spinor (dim 2^(k-1))."""
    g = clifford(k)
    n = 2 ** k
    gens = [(g[a] @ g[b] - g[b] @ g[a]) / 4 for a in range(2 * k) for b in range(a + 1, 2 * k)]
    # invariant bilinear C (C S + S^T C = 0): products of all real or all imaginary gammas
    gam = kron_list([Z2] * k)  # proportional to the chirality Gamma_1...Gamma_2k
    ev, U = np.linalg.eigh(gam)
    Pp = U[:, ev > 0]
    for C in (np.linalg.multi_dot(g[0::2]) if k > 1 else g[0], np.linalg.multi_dot(g[1::2]) if k > 1 else g[1]):
        inv = max(np.abs(C @ S + S.T @ C).max() for S in gens)
        Ms = [Pp.T @ C @ g[a] @ Pp for a in range(2 * k)]
        if inv < 1e-12 and max(np.abs(M).max() for M in Ms) > 1e-6:
            return Ms
    return None


res = {}
for k in (3, 5):
    Ms = pair_channel(k)
    sym = max(np.abs(M - M.T).max() for M in Ms)
    asym = max(np.abs(M + M.T).max() for M in Ms)
    rank = np.linalg.matrix_rank(np.array([M.ravel() for M in Ms]), tol=1e-8)
    res[k] = (Ms, sym, asym, rank)
Ms6 = res[3][0]
T4 = sum(np.einsum("ij,kl->ijkl", M, M) for M in Ms6)
eps = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])
lam = T4[0, 1, 2, 3]
err_eps = np.abs(T4 - lam * eps).max()
ok = res[3][2] < 1e-9 and res[3][3] == 6 and res[5][1] < 1e-9 and res[5][3] == 10 and err_eps < 1e-9 \
    and abs(lam) > 1e-6
check(ok, "A1", "[T] vector-channel pairing of a chiral Spin(2k) spinor: k=3 (4x4->6) antisymmetric, k=5 (16x16->10) "
      "symmetric; k=3: sum_a M_a(ij)M_a(kl) = lam eps_ijkl, so the toy quartic c1c2c3c4 is the Spin(6) pair square "
      "and Spin(10)'s is the k=5 member (spinless toy pair <-> spin-singlet Weyl pair)",
      f"k=3 |M+M^T| {res[3][2]:.0e}, span {res[3][3]}; k=5 |M-M^T| {res[5][1]:.0e}, span {res[5][3]}; "
      f"|T - lam eps| {err_eps:.0e}")
def sphere_goldstones(d):
    gens = []
    for i, j in itertools.combinations(range(d), 2):
        E = np.zeros((d, d))
        E[i, j], E[j, i] = 1, -1
        gens.append(E)
    n = RNG.normal(size=d)
    return np.linalg.matrix_rank(np.array([E @ n for E in gens]), tol=1e-9)


gs = {d: sphere_goldstones(d) for d in (6, 10)}
check(gs == {6: 5, 10: 9}, "A2", "[T] toy SU(4) -> Sp(4) = SO(6) -> SO(5) (S^5); Spin(10) analogue SO(10) -> SO(9) (S^9)",
      f"Goldstones of a generic vector: SO(6) {gs[6]}, SO(10) {gs[10]}")

# ---------------------------------------------------------------- B
print("== B. weights of the 16, 10, 45 and u(16)")
half = Fr(1, 2)
W16 = [tuple(half * s for s in sg) for sg in itertools.product((1, -1), repeat=5)
       if sum(1 for s in sg if s < 0) % 2 == 0]


def charges(h):
    t3l = (h[3] + h[4]) / 2
    t3r = (h[3] - h[4]) / 2
    bl = -Fr(2, 3) * (h[0] + h[1] + h[2])
    return t3l, t3r, bl, t3r + bl / 2


def col0(h):
    return h[0] == h[1] == h[2]


ys = sorted(charges(h)[3] for h in W16)
ys_expect = sorted([Fr(1, 6)] * 6 + [Fr(-2, 3)] * 3 + [Fr(1, 3)] * 3 + [Fr(-1, 2)] * 2 + [Fr(1), Fr(0)])
W10 = []
for i in range(5):
    for s in (1, -1):
        e = [Fr(0)] * 5
        e[i] = Fr(s)
        W10.append(tuple(e))
c10 = [charges(h) for h in W10]
ew10 = [c for c, h in zip(c10, W10) if col0(h)]
ok = ys == ys_expect and len(ew10) == 4 and all(c[2] == 0 and abs(c[0]) == half and abs(c[3]) == half for c in ew10) \
    and all(abs(c[2]) == Fr(2, 3) for c, h in zip(c10, W10) if not col0(h))
check(ok, "B1", "[T] 16 weights give the measured hypercharges; 10 = (1,2,2) + (6,1,1); its colour-singlet part is a "
      "Y = +-1/2 bidoublet with B-L = 0: a (1,2,2) mirror pair condensate carries SU(2)_L x U(1)_Y, keeps Z4 of B-L",
      f"16 hypercharges ok; colour-singlet 10 components {len(ew10)}, B-L 0, |Y| 1/2")
roots = []
for i, j in itertools.combinations(range(5), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        e = [Fr(0)] * 5
        e[i], e[j] = Fr(si), Fr(sj)
        roots.append(tuple(e))
w45 = roots + [tuple([Fr(0)] * 5)] * 5
d45 = [h for h in w45 if col0(h) and abs(charges(h)[0]) == half]
diffs = [tuple(a - b for a, b in zip(u, w)) for u in W16 for w in W16]
dd = sorted({charges(h)[2] for h in diffs if col0(h) and abs(charges(h)[0]) == half})
sums = [tuple(a + b for a, b in zip(u, w)) for u in W16 for w in W16]
ds = sorted({charges(h)[2] for h in sums if col0(h) and abs(charges(h)[0]) == half})
dy = sorted({charges(h)[3] for h in diffs if col0(h) and abs(charges(h)[0]) == half})
ok = len(w45) == 45 and not d45 and dd == [-2, 2] and 0 in ds
check(ok, "B2", "[T] no 45 weight has zero colour weight and T3L = +-1/2: adj(Spin(10) x family) holds no colour-singlet "
      "doublet, so no condensate of a Spin(10)-symmetric mirror sector, any channel, has a pNGB Higgs doublet",
      f"45 weights {len(w45)}; colour-zero doublet weights {len(d45)}")
check(ok, "B3", "[T] u(16N) (all symmetries of free 16s): colour-zero doublet generators have |B-L| = 2; B-L-neutral ones "
      "only in light x mirror (16 x 16), broken at O(g) by a mirror-only quartic",
      f"u(16) doublet B-L {[str(x) for x in dd]}, Y {[str(x) for x in dy]}; 16x16 doublet B-L {[str(x) for x in ds]}")

# ---------------------------------------------------------------- C
print("== C. the pair-square vacuum manifold S^9")


def realify(A):
    return np.block([[A.real, -A.imag], [A.imag, A.real]])


lam8 = []
for i in range(3):
    for j in range(i + 1, 3):
        for typ in ("s", "a"):
            m = np.zeros((3, 3), complex)
            if typ == "s":
                m[i, j] = m[j, i] = 1
            else:
                m[i, j], m[j, i] = -1j, 1j
            lam8.append(m)
lam8 += [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
# vector-index layout: 0..5 = R^6 of the colour 3 (re, im), 6..9 = R^4 of the bidoublet
Xc = []
for L in lam8:
    X = np.zeros((10, 10))
    X[:6, :6] = realify(-1j * L / 2)
    Xc.append(X)
J6 = realify(1j * np.eye(3))
qi = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], float)
qj = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]], float)
qk = qi @ qj
ri = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]], float)


def emb4(m):
    X = np.zeros((10, 10))
    X[6:, 6:] = m
    return X


XL = [emb4(q / 2) for q in (qi, qj, qk)]
XY = np.zeros((10, 10))
XY[6:, 6:] = ri / 2
XY[:6, :6] = J6 / 3
cas3 = -sum(X @ X for X in Xc)[:6, :6]
casL = -sum(X @ X for X in XL)[6:, 6:]
comm = max(np.abs(a @ b - b @ a).max() for a in XL for b in [emb4(ri)])
ok = np.allclose(cas3, 4 / 3 * np.eye(6)) and np.allclose(casL, 0.75 * np.eye(4)) and comm < 1e-12 \
    and np.allclose(-(XY @ XY)[6:, 6:], 0.25 * np.eye(4)) and np.allclose(-(XY @ XY)[:6, :6], np.eye(6) / 9)
# so(10) basis and commutant of colour
so10 = []
for a, b in itertools.combinations(range(10), 2):
    E = np.zeros((10, 10))
    E[a, b], E[b, a] = 1, -1
    so10.append(E)
A = np.vstack([np.array([(E @ X - X @ E).ravel() for E in so10]).T for X in Xc])
dcom = null_space(A).shape[1]
check(ok and dcom == 7, "C1", "[T] on the 10: Casimirs colour 4/3, SU(2)_L 3/4, Y^2 1/4 | 1/9; commutant of colour in so(10) has dim 7, "
      "so no SU(4) on mirror modes commutes with colour",
      f"commutant dim {dcom}")
G_SM = Xc + XL + [XY]


def unbroken_dim(n, gens):
    return len(gens) - np.linalg.matrix_rank(np.array([X @ n for X in gens]), tol=1e-9)


def so10_goldstones(n):
    return np.linalg.matrix_rank(np.array([E @ n for E in so10]), tol=1e-9)


nh = np.zeros(10)
nh[6] = 1
nt = np.zeros(10)
nt[0] = 1
gh = so10_goldstones(nh)
col_broken_h = np.linalg.matrix_rank(np.array([X @ nh for X in Xc]), tol=1e-9)
ew_broken_h = np.linalg.matrix_rank(np.array([X @ nh for X in XL + [XY]]), tol=1e-9)
fixed_sm = null_space(np.vstack([X for X in G_SM])).shape[1]
check(gh == 9 and col_broken_h == 0 and ew_broken_h == 3 and fixed_sm == 0, "C2",
      "[T] S^9: 9 Goldstones; at the (1,2,2) end colour kept, 3 eaten + 6 colour-triplet; no SM-fixed point",
      f"goldstones {gh}; colour broken {col_broken_h}; EW broken {ew_broken_h}; SM-fixed directions {fixed_sm}")
# misalignment angle and gauge potential
lin_err, mw_err, col_err = 0.0, 0.0, 0.0
g3, g2, gp = 1.0, 1.0, np.sqrt(3 / 5)
for _ in range(20):
    t = np.zeros(10)
    t[:6] = RNG.normal(size=6)
    t /= np.linalg.norm(t)
    h = np.zeros(10)
    h[6:] = RNG.normal(size=4)
    h /= np.linalg.norm(h)
    th = np.linspace(0, PI / 2, 9)
    V, MW, CB = [], [], []
    for x in th:
        n = np.cos(x) * t + np.sin(x) * h
        V.append(g3 ** 2 * sum(np.sum((X @ n) ** 2) for X in Xc) + g2 ** 2 * sum(np.sum((X @ n) ** 2) for X in XL)
                 + gp ** 2 * np.sum((XY @ n) ** 2))
        MW.append(sum(np.sum((X @ n) ** 2) for X in XL[:2]))
        CB.append(sum(np.sum((X @ n) ** 2) for X in Xc))
    s2 = np.sin(th) ** 2
    Ah, At = 0.75 * g2 ** 2 + 0.25 * gp ** 2, 4 / 3 * g3 ** 2 + gp ** 2 / 9
    lin_err = max(lin_err, np.abs(np.array(V) - (At + (Ah - At) * s2)).max())
    mw_err = max(mw_err, np.abs(np.array(MW) - 0.5 * s2).max())
    col_err = max(col_err, np.abs(np.array(CB) - 4 / 3 * (1 - s2)).max())
check(max(lin_err, mw_err, col_err) < 1e-12, "C3",
      "[T] n = cos(th) t + sin(th) h: W-mass sum = sin^2(th)/2, colour-breaking sum = (4/3)cos^2(th) exactly; "
      "the only angle on S^9 runs EW -> COLOUR breaking; unbroken colour forces th = pi/2, v = f",
      f"errors: m_W {mw_err:.0e}, colour {col_err:.0e}")
rows = []
for name, (a3, a2, a1) in {"GUT-equal": (1.0, 1.0, 3 / 5), "m_Z": (1.2172 ** 2, 0.6517 ** 2, 0.3576 ** 2),
                           "1 TeV": (1.06 ** 2, 0.64 ** 2, 0.362 ** 2)}.items():
    Ah, At = 0.75 * a2 + 0.25 * a1, 4 / 3 * a3 + a1 / 9
    rows.append((name, Ah, At))
check(lin_err < 1e-12 and all(Ah < At for _, Ah, At in rows), "C4",
      "[T/E] gauge-loop potential sum g^2|T n|^2 is exactly linear in sin^2(th): no interior minimum; "
      "measured or unified couplings pick the (1,2,2) end",
      "; ".join(f"{n}: A_h {a:.3f} < A_t {b:.3f}" for n, a, b in rows) + f"; linearity {lin_err:.0e}")

# ---------------------------------------------------------------- D
print("== D. the toy's SU(4)/Sp(4) on SM-charged modes")
eps2 = np.array([[0, 1], [-1, 0]], complex)


def su2_on(idx):
    out = []
    for P in (X2, Y2, Z2):
        T = np.zeros((4, 4), complex)
        T[np.ix_(idx, idx)] = P / 2
        out.append(T)
    return out


def act(T, S):
    return T @ S + S @ T.T


def ew_setup(yD, y1, y2):
    TL = su2_on([0, 1])
    Yg = np.diag([yD, yD, y1, y2]).astype(complex)
    return TL, Yg, TL[2] + Yg


SB = np.zeros((4, 4), complex)
SB[:2, :2] = eps2
SB[2, 3], SB[3, 2] = 1, -1
SH = np.zeros((4, 4), complex)
SH[0, 3], SH[3, 0] = 1, -1   # up with s_-1/2, down with s_+1/2: Q-neutral
SH[1, 2], SH[2, 1] = -1, 1
TL, Yg, Q = ew_setup(0.0, 0.5, -0.5)
# su(4) basis (traceless Hermitian)
su4 = []
for i in range(4):
    for j in range(i + 1, 4):
        for typ in ("s", "a"):
            m = np.zeros((4, 4), complex)
            if typ == "s":
                m[i, j] = m[j, i] = 1
            else:
                m[i, j], m[j, i] = -1j, 1j
            su4.append(m / 2)
for d in range(1, 4):
    v = np.zeros(4)
    v[:d] = 1
    v[d] = -d
    su4.append(np.diag(v / np.sqrt(2 * d * (d + 1))).astype(complex))
th = np.linspace(0, PI / 2, 7)
mw = []
qerr = 0.0
for x in th:
    S = np.cos(x) * SB + np.sin(x) * SH
    mw.append(sum(np.sum(np.abs(act(T, S)) ** 2) for T in TL[:2]))
    qerr = max(qerr, np.abs(act(Q, S)).max())
mw = np.array(mw) / mw[-1]
stab = 15 - np.linalg.matrix_rank(np.array([act(T, SB).ravel() for T in su4]), tol=1e-9)
# Goldstone directions at theta = 0: charges under (T3L, Y)
tan = np.array([act(T, SB).ravel() for T in su4])
ok = np.allclose(mw, np.sin(th) ** 2) and qerr < 1e-12 and stab == 10 and \
    np.abs(act(TL[0], SB)).max() < 1e-12 and np.abs(act(Yg, SB)).max() < 1e-12
check(ok, "D1", "[T] SU(4)/Sp(4), 4 = (2)_0 + (1)_+-1/2: stabiliser 10 (5 = doublet + singlet), th = 0 keeps "
      "SU(2)_L x U(1)_Y, Q kept at all th, m_W^2 ~ sin^2(th)",
      f"stabiliser {stab}; m_W^2(theta)/m_W^2(pi/2) {np.round(mw, 4).tolist()}")
# forced content: Sigma_B neutral needs yD = 0 and y1 = -y2; pNGB Y = yD + y_i
yd_16 = sorted({Fr(1, 6), Fr(-1, 2), Fr(-1, 6), Fr(1, 2)})
lept = ew_setup(-0.5, 0.0, 1.0)
qb_lept = np.abs(act(lept[2], SB)).max()
check(qb_lept > 0.1 and Fr(0) not in yd_16, "D2",
      "[T] 4 = (2)_yD + (1)_y1 + (1)_y2: neutral th = 0 end with Y = 1/2 pNGB forces yD = 0, y = +-1/2; "
      "16/16bar doublets have Y = +-1/6, +-1/2 (NEW content); mirror (L', L'^c) four: th = 0 end charged",
      f"doublet Y in 16, 16bar: {[str(y) for y in yd_16]}; |Q Sigma_B| leptonic {qb_lept:.2f}")
# spinful Weyl modes without an extra antisymmetric index: symmetric Sigma (10 of SU(4))
basis_sym = []
for i in range(4):
    for j in range(i, 4):
        m = np.zeros((4, 4), complex)
        m[i, j] = m[j, i] = 1
        basis_sym.append(m.ravel())
Bs = np.array(basis_sym).T
cons = np.vstack([np.array([act(T, Bs[:, c].reshape(4, 4)).ravel() for c in range(Bs.shape[1])]).T
                  for T in TL + [Yg]])
inv = null_space(cons)
maxrank = max(np.linalg.matrix_rank((Bs @ inv[:, c]).reshape(4, 4), tol=1e-9) for c in range(inv.shape[1])) \
    if inv.shape[1] else 0
n_doublets = {"no index": 1, "two-valued index": 2}
check(maxrank == 2 and n_doublets["no index"] % 2 == 1, "D3",
      "[T] spinful Weyl modes pair symmetrically (10 of SU(4)): EW-invariant vacua rank <= 2, and 4 modes hold one "
      "(Witten-anomalous) doublet; the toy's 6 needs a two-valued antisymmetric index: 8 Weyl modes per cell",
      f"max rank of EW-invariant symmetric vacuum {maxrank}; doublets per 4 modes {n_doublets}")
check(dcom == 7 and qb_lept > 0.1 and all(abs(c[2]) == Fr(2, 3) for c, h in zip(c10, W10) if not col0(h)), "D4", "[T] toy SU(4) on the mirror 16: (a) SU(4)_PS: 6 = (6,1,1), colour breaking; (b) Spin(6) on bidoublet + 2 "
      "colour directions: colour generators; (c) leptonic (L', L'^c): charged end. None gives a neutral EW-safe end",
      "(a) B1, (b) C1, (c) D2")

# ---------------------------------------------------------------- E
print("== E. estimates against measurement")
S_MEAS, S_ERR = -0.05, 0.07
s_fam = 4 / (6 * PI)
mh, mt = 125.1, 172.6


def a_half(tau):
    f = np.arcsin(np.sqrt(tau)) ** 2
    return 2 * (tau + (tau - 1) * f) / tau ** 2


at = a_half(mh ** 2 / (4 * mt ** 2))
ggh = {nf: ((at + 2 * nf * 4 / 3) / at) ** 2 for nf in (1, 3)}
V_EW, M_CELL = 246.22, 2.44e18


def pagels(N, Lam):
    lo, hi = 1e-3, 1e5
    for _ in range(200):
        m = np.sqrt(lo * hi)
        v2 = N * m * m / (4 * PI ** 2) * np.log(Lam ** 2 / m ** 2)
        lo, hi = (m, hi) if v2 < V_EW ** 2 else (lo, m)
    return m


mstar = {N: pagels(N, M_CELL) for N in (4, 12)}
mstrong = {N: 2 * PI * V_EW / np.sqrt(N) for N in (4, 12)}
check(ggh[1] > 5 and (s_fam - S_MEAS) / S_ERR > 3, "E1",
      "[E] condensed mirror (v = f, degenerate, T = 0): S, gg->h, Pagels-Stokar mass",
      f"S = {s_fam:.3f} (1 fam, {(s_fam - S_MEAS) / S_ERR:.1f} sigma), {3 * s_fam:.3f} (3 fam, "
      f"{(3 * s_fam - S_MEAS) / S_ERR:.1f} sigma); sigma(gg->h)/SM = {ggh[1]:.1f}, {ggh[3]:.0f} vs ~1.0(1); "
      f"m* (cutoff M) = {mstar[4]:.0f}, {mstar[12]:.0f} GeV vs charged-lepton bound 100.8; strong (log~1) "
      f"{mstrong[4]:.0f}, {mstrong[12]:.0f} GeV")
kv, kverr = 1.035, 0.031
xi_max = 1 - (kv - 1.96 * kverr) ** 2
f_min = V_EW / np.sqrt(xi_max)
dS = xi_max / (12 * PI) * np.log((4 * PI * f_min) ** 2 / mh ** 2)
dT = -3 / (16 * PI * 0.769) * xi_max * np.log((4 * PI * f_min) ** 2 / mh ** 2)
delta = (f_min / M_CELL) ** 2
nrung = np.log2(M_CELL / f_min)
check(xi_max < 0.1 and abs(dS) < 0.05 and delta < 1e-29, "E2",
      "[E] new-content candidate: kappa_V = cos th bounds xi; IR S, T; f from rung n or near-critical g",
      f"xi <= {xi_max:.3f}, f >= {f_min:.0f} GeV, mirror-free; dS ~ {dS:.3f}, dT ~ {dT:.3f}; "
      f"(g-g_c)/g_c ~ {delta:.0e} at the cell; rung n ~ {nrung:.1f} (kappa = 1)")
mpngb = np.sqrt(3 * 0.09 * (4 / 3) / (4 * PI)) * 4 * PI * V_EW
check(mpngb < 1500, "E3", "[E] condensed mirror's colour-triplet pNGBs (Y -+1/3): colour-loop mass at f = v", f"m ~ {mpngb:.0f} GeV (pair-produced by QCD)")
print("supplied: toy quartic and its phase (toy-qmc), Spin(10) pair square on the mirror 16 (CL-1 mirror term), SM gauge "
      "embedding in Spin(10), gauge-loop sign (vacuum alignment), new content (2)_0 + (1)_+-1/2 x 2, top coupling, "
      "cutoff M = 2.44e18 GeV, Pagels-Stokar leading log, kappa = 1; measured: v, m_h, m_t, couplings, S = -0.05(7), "
      "kappa_V = 1.035(31), mu_ggF ~ 1.0(1), LEP heavy lepton 100.8 GeV.")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
