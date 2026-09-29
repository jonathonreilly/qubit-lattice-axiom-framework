#!/usr/bin/env python3
"""The tensor complex on finite slots at the harmonic level: whatever the residual symmetry, TT modes linear in every direction bring helicity-1 content among the gapless modes; with every transverse diffeomorphism exact the TT mode is soft.

(The runner's file name keeps the first version's words; the note's third
version states (ii) for every residual symmetry, since its proof uses none.)

Question (the gravity lane's closing question, 2026-09-29): on the landed
tensor complex with finite slots, local (finite-range) harmonic models and
the scalar (time) rule kept exact, can the TT mode be linear in every
direction with no gapless helicity +-1 mode, in either storage assignment
(momentum stored, probes 10/14; metric stored, probe 15)? Pre-registered in
the probe's scratch file (parts of (ii) computed in scratch before it).

Checks:
  A  (i), momentum stored: moves that commute with the transverse
     diffeomorphism generators (curl of G E) are the finitely supported mu
     with curl(G mu) = 0. On a 3^3 box their zeroth moments are pure trace
     and their first moments are TT-invisible in every sampled direction,
     so the TT potential has no O(q^2) term and, with the O(1) DeWitt
     kinetic term, the TT mode is soft.
  B  (i), metric stored: the leading symbols of the transverse gauge shifts
     sym(q (x) (q x zeta)) span all traceless symmetric tensors, so a local
     potential exactly invariant under them has a q -> 0 limit X(0) that
     vanishes on traceless tensors; the TT stiffness is then O(q^2) and,
     with O(q^2) Gauss-law kinetic weight (probe 15), the TT mode is soft.
  C  (ii): the TT directions TT(qhat), over all qhat, span the traceless
     tensors, so a TT mode gapless in every direction forces X(0) = 0 on
     traceless tensors (momentum stored) and a q^0 TT stiffness is nonzero
     on helicity +-1 directions on an open set (metric stored); over all 18
     first-moment dimensions (any local move, rule-compatible or not) the
     direction-averaged helicity +-1 weight is at least 1/4 of the TT weight
     (exact quadrature, Schur complement); the DeWitt form is positive on
     helicity +-1 directions. So, on an open dense set of directions, a
     linear mode carries helicity +-1 weight (momentum stored), and a mode
     in the kinetic range, linear or softer, carries it (metric stored;
     linear under premise P, probe 20 G).
  D  harmonic illustration, momentum stored, momentum rule broken: DeWitt
     kinetic, scalar law exact, potential from random local moves not in
     ker G: the TT modes are linear and so are helicity +-1 modes in some
     sampled directions.
Reference only: probes 10, 11, 15, 18, 20; Dubovsky (hep-th/0409124) for
symmetry-protected mode removal in Lorentz-violating massive gravity.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
from scipy.linalg import null_space, eigh

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260929)
E3 = np.eye(3, dtype=int); FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}; FI = {v: k for k, v in FACE.items()}
EPS = np.zeros((3, 3, 3))
for (i, j, k), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    EPS[i, j, k] = s


def offset(a):
    if a < 3:
        return np.zeros(3)
    i, j = FI[a]
    return (E3[i] + E3[j]) / 2


def G_row(x, j):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    add(x + E3[j], j, 1); add(x, j, -1)
    for i in range(3):
        if i != j:
            f = FACE[tuple(sorted((i, j)))]; add(x, f, 1); add(x - E3[i], f, -1)
    return d


def helicity_bases(n):
    n = n / np.linalg.norm(n); a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(n, a_); u /= np.linalg.norm(u); w = np.cross(n, u)
    TT = [(np.outer(u, u) - np.outer(w, w)) / np.sqrt(2), (np.outer(u, w) + np.outer(w, u)) / np.sqrt(2)]
    H1 = [(np.outer(n, u) + np.outer(u, n)) / np.sqrt(2), (np.outer(n, w) + np.outer(w, n)) / np.sqrt(2)]
    return n, TT, H1


def tensor_from_E(v):      # E-coordinates (E_xx, E_yy, E_zz, E_xy, E_yz, E_xz): the off-diagonal entries are the tensor's
    return np.array([[v[0], v[3], v[5]], [v[3], v[1], v[4]], [v[5], v[4], v[2]]])


# ---------------------------------------------------------------- A: momentum stored, transverse diffeomorphisms exact
nb = 3
box = list(itertools.product(range(nb), repeat=3)); slots = [(c, a) for c in box for a in range(6)]; sidx = {s_: i for i, s_ in enumerate(slots)}
edges = {}
def edge_vec(x, j):         # (G mu)_j(x) as a row over the box slots (slots outside the box are zero)
    row = np.zeros(len(slots))
    for k, v in G_row(x, j).items():
        if k in sidx:
            row[sidx[k]] += v
    return row
rows = []
for x in itertools.product(range(-2, nb + 2), repeat=3):
    xa = np.array(x)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        r_ = edge_vec(xa, i) + edge_vec(xa + E3[i], j) - edge_vec(xa + E3[j], i) - edge_vec(xa, j)
        if np.any(r_):
            rows.append(r_)
KA = null_space(np.array(rows))
m0s, m1s = [], []
for t in range(KA.shape[1]):
    m0 = np.zeros(6); m1 = np.zeros((6, 3))
    for (c, a), i in sidx.items():
        v = KA[i, t]
        if abs(v) > 1e-12:
            p = np.array(c, float) + offset(a); m0[a] += v; m1[a] += v * p
    m0s.append(m0); m1s.append(m1)
m0s = np.array(m0s)
zero_trace_only = np.abs(m0s[:, 3:]).max() < 1e-9 and np.abs(m0s[:, 0] - m0s[:, 1]).max() < 1e-9 and np.abs(m0s[:, 1] - m0s[:, 2]).max() < 1e-9
ttvis = 0.0
for _ in range(60):
    n, TT, H1 = helicity_bases(rng.normal(size=3))
    for m1 in m1s:
        Mt = tensor_from_E(m1 @ n)
        ttvis = max(ttvis, max(abs(np.sum(T * Mt)) for T in TT))
# symbol proof for every finite support: curl(G mu) = 0 at leading orders reads qhat x (M(q) qhat) = 0, order by order;
# order q^2 (zeroth moment M0): M0 = a I; order q^3 (first moment M1(q) = c_ijk q_k): M1(q) = l(q) I -- both TT-invisible
def kernel_dim(cols, conds):
    return null_space(np.array(conds).T if False else np.array(conds)).shape[1]
rs = np.random.default_rng(5)
# zeroth moment: 6 unknowns (symmetric M0), condition q x (M0 q) = 0 for many q
sym6 = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
    Mb = np.zeros((3, 3)); Mb[i, j] = Mb[j, i] = 1; sym6.append(Mb)
rows0 = []
for _ in range(20):
    q = rs.normal(size=3)
    rows0 += list(np.array([np.cross(q, Mb @ q) for Mb in sym6]).T)
ker0 = null_space(np.array(rows0))
M0sol = sum(ker0[b, 0] * sym6[b] for b in range(6)) if ker0.shape[1] else np.zeros((3, 3))
pure0 = ker0.shape[1] == 1 and np.allclose(M0sol / M0sol[0, 0], np.eye(3))
# first moment: 18 unknowns c_ijk (sym in ij), condition q x (M1(q) q) = 0 with M1(q)_ij = c_ijk q_k
c18 = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
    for k in range(3):
        c = np.zeros((3, 3, 3)); c[i, j, k] = 1; c[j, i, k] = 1; c18.append(c)
rows1 = []
for _ in range(30):
    q = rs.normal(size=3)
    rows1 += list(np.array([np.cross(q, np.einsum("ijk,k->ij", c, q) @ q) for c in c18]).T)
ker1 = null_space(np.array(rows1))
pure1 = ker1.shape[1] == 3
for b in range(ker1.shape[1]):
    c = sum(ker1[t, b] * c18[t] for t in range(18))
    for _ in range(5):
        q = rs.normal(size=3); M = np.einsum("ijk,k->ij", c, q)
        pure1 &= np.allclose(M - np.trace(M) / 3 * np.eye(3), 0, atol=1e-9)
# real space (Fable referee, third version): curl(G mu) = 0 iff G mu = grad phi iff mu = phi delta + ker G; on the box 42 = 27 + 15
growsG = []
for x in itertools.product(range(-2, nb + 2), repeat=3):
    for j in range(3):
        r_ = edge_vec(np.array(x), j)
        if np.any(r_):
            growsG.append(r_)
KG = null_space(np.array(growsG))
Dphi = np.zeros((len(slots), len(box)))
for b_, c in enumerate(box):
    for a in range(3):
        Dphi[sidx[(c, a)], b_] = 1
comb = np.hstack([Dphi, KG]); rk_comb = np.linalg.matrix_rank(comb, tol=1e-9)
real_space_ok = rk_comb == KA.shape[1] == len(box) + KG.shape[1] and np.linalg.norm(comb - KA @ (KA.T @ comb)) < 1e-9
okA = KA.shape[1] > 0 and zero_trace_only and ttvis < 1e-9 and pure0 and pure1 and real_space_ok
check("A: (i) momentum stored: for every finite support, curl(G mu) = 0 reads qhat x (M(q) qhat) = 0 order by order, which forces the zeroth moment to a I and the first moment to l(q) I (both pure trace, TT-invisible); so TT amplitudes start at O(q^2), a positive move potential on TT at O(q^4), and with the DeWitt kinetic term omega_TT = O(q^2); the 3^3 box exhibits such moves, and in real space ker(curl G) = {phi delta} + ker G",
      okA, f"real space on the 3^3 box: dim ker(curl G) = {KA.shape[1]} = {len(box)} (phi delta) + {KG.shape[1]} (ker G): {real_space_ok}; symbol kernels: zeroth moment {ker0.shape[1]}-dim, pure trace {pure0}; first moment {ker1.shape[1]}-dim, pure trace {pure1}; 3^3 box: {KA.shape[1]} moves, zeroth moments pure trace {zero_trace_only}, max TT visibility of first moments {ttvis:.1e}")

# ---------------------------------------------------------------- B: metric stored, transverse diffeomorphisms exact
span = []
for _ in range(40):
    q = rng.normal(size=3); z = rng.normal(size=3); e = np.cross(q, z)
    span.append(((np.outer(q, e) + np.outer(e, q)) / 2).ravel())
span = np.array(span); rkB = np.linalg.matrix_rank(span, tol=1e-9)
traceless = all(abs(np.trace(v.reshape(3, 3))) < 1e-9 for v in span)
okB = rkB == 5 and traceless
check("B: (i) metric stored: the leading symbols sym(q (x) (q x zeta)) of the transverse gauge shifts span all five traceless symmetric tensors, so a local potential exactly invariant under them has X(0) = 0 on traceless tensors; the TT stiffness is O(q^2) and with O(q^2) Gauss-law kinetic weight (probe 15) the TT mode is soft",
      okB, f"rank of 40 sampled symbols {rkB}; all traceless: {traceless}")

# ---------------------------------------------------------------- C: (ii) without exact transverse diffeomorphisms
spanTT = []
for _ in range(30):
    n, TT, H1 = helicity_bases(rng.normal(size=3)); spanTT += [T.ravel() for T in TT]
rkTT = np.linalg.matrix_rank(np.array(spanTT), tol=1e-9)
# the 18-dimensional first-moment lemma
basis = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
    for k in range(3):
        c = np.zeros((3, 3, 3)); c[i, j, k] = 1; c[j, i, k] = 1; basis.append(c / np.linalg.norm(c))
x, wx = np.polynomial.legendre.leggauss(10); phis = 2 * np.pi * np.arange(20) / 20
QT = np.zeros((18, 18)); QH = np.zeros((18, 18)); ws = 0.0
for ct, wc in zip(x, wx):
    st = np.sqrt(1 - ct ** 2)
    for ph in phis:
        n = np.array([st * np.cos(ph), st * np.sin(ph), ct]); w = wc * (2 * np.pi / 20); _, TT, H1 = helicity_bases(n)
        Jt = np.array([[np.sum(T * np.einsum("ijk,k->ij", c, n)) for c in basis] for T in TT])
        Jh = np.array([[np.sum(T * np.einsum("ijk,k->ij", c, n)) for c in basis] for T in H1])
        QT += w * Jt.T @ Jt; QH += w * Jh.T @ Jh; ws += w
QT /= ws; QH /= ws
wt, V = np.linalg.eigh(QT); R = V[:, wt > 1e-10]; Z = V[:, wt <= 1e-10]
Sc = R.T @ QH @ R - (R.T @ QH @ Z) @ np.linalg.pinv(Z.T @ QH @ Z) @ (Z.T @ QH @ R)
lam = eigh(Sc, R.T @ QT @ R, eigvals_only=True)
# the DeWitt form on helicity +-1 E-directions
Mdw = np.diag([1, 1, 1, 2, 2, 2.]) - np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]) / 2
dwmin = 1e9
for _ in range(60):
    n, TT, H1 = helicity_bases(rng.normal(size=3))
    for T in H1:
        v = np.array([T[0, 0], T[1, 1], T[2, 2], T[0, 1], T[1, 2], T[0, 2]]); dwmin = min(dwmin, v @ Mdw @ v)
okC = rkTT == 5 and abs(lam.min() - 0.25) < 1e-9 and dwmin > 0.5
check("C: (ii) TT linear in every direction, whatever the residual symmetry (the argument uses none): the TT directions over all qhat span the traceless tensors (so TT gapless everywhere forces X(0) = 0 on traceless tensors, and a q^0 TT stiffness reaches helicity +-1 on an open set); over all 18 first-moment dimensions the direction-averaged helicity +-1 weight is at least 1/4 of the TT weight (exact, Schur complement over TT-invisible parts); the DeWitt form is positive on helicity +-1 directions",
      okC, f"rank of TT directions {rkTT}; minimum +-1/TT ratio over 18 dimensions {lam.min():.6f} (spectrum {np.round(np.unique(np.round(lam, 6)), 4).tolist()}); min DeWitt value on +-1 directions {dwmin:.3f}")

# ---------------------------------------------------------------- D: harmonic illustration, momentum stored, momentum rule broken
def S_sym(q):
    K = 2 * np.sin(q / 2); KK = K @ K
    return np.array([K[0] ** 2 - KK, K[1] ** 2 - KK, K[2] ** 2 - KK, K[0] * K[1], K[1] * K[2], K[0] * K[2]], complex)


def rhat_E(pat, q):        # pat: dict (cell, slot) -> integer, an E-shift pattern; phase at slot positions
    out = np.zeros(6, complex)
    for (c, a), v in pat.items():
        out[a] += v * np.exp(-1j * q @ (np.array(c, float) + offset(a)))
    return out


def random_move():
    pat = {}
    for _ in range(4):
        c = tuple(rng.integers(0, 2, size=3)); a = int(rng.integers(0, 6)); pat[(c, a)] = pat.get((c, a), 0) + int(rng.choice([-1, 1]))
    for a in range(6):                            # remove each slot type's zeroth moment so the potential is O(q^2), keeping first moments generic
        tot = sum(v for (c, a_), v in pat.items() if a_ == a)
        if tot:
            pat[((0, 0, 0), a)] = pat.get(((0, 0, 0), a), 0) - tot
    return pat


def modes_D(moves, n):
    out = []
    for eps in (0.02, 0.01):
        q = eps * n; B = np.linalg.svd(S_sym(q)[None, :])[2][1:].conj().T          # h in ker S(q)
        Gi = np.linalg.inv(B.conj().T @ B)
        Wp = sum(np.outer(rhat_E(m, q), rhat_E(m, q).conj()) for m in moves)      # potential on h from E-shift moves
        # E-coordinates pair with q-coordinates of h; the DeWitt form acts on E
        Kred = Gi @ B.conj().T @ Mdw @ B @ Gi; Vred = B.conj().T @ Wp @ B
        w2, vec = np.linalg.eig(Vred @ Kred); o = np.argsort(w2.real)
        out.append((np.sqrt(np.maximum(w2.real[o], 0)) / np.linalg.norm(2 * np.sin(q / 2)), [B @ (Kred @ vec[:, j]) for j in o], 2 * np.sin(q / 2)))
    (o1, _, _), (o2, vecs, Kq) = out
    lin = [j for j in range(5) if o2[j] > 0.05 and abs(o1[j] - o2[j]) / o2[j] < 0.05]
    nn_, TT, H1 = helicity_bases(Kq)
    def weights(hq):
        h = np.array([[hq[0], hq[3] / 2, hq[5] / 2], [hq[3] / 2, hq[1], hq[4] / 2], [hq[5] / 2, hq[4] / 2, hq[2]]]); tot = np.sum(np.abs(h) ** 2)
        return sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in TT) / tot, sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in H1) / tot
    wts = [weights(vecs[j]) for j in lin]
    return len(lin), max((w[0] for w in wts), default=0.0), max((w[1] for w in wts), default=0.0)


okD = True; rowsD = []
for fam in range(5):
    moves = [random_move() for _ in range(8)]
    res = []
    for n in rng.normal(size=(6, 3)):
        n /= np.linalg.norm(n); res.append(modes_D(moves, n))
    tt_lin = max(r[1] for r in res); pm1_lin = max(r[2] for r in res)
    okD &= tt_lin > 0.05 and pm1_lin > 0.05
    rowsD.append(f"family {fam}: linear-mode counts {sorted(set(r[0] for r in res))}, max TT weight {tt_lin:.2f}, max +-1 weight {pm1_lin:.2f}")
check("D: harmonic illustration, momentum stored and momentum rule broken (DeWitt kinetic term, scalar law exact, potential from 8 random local moves not in ker G, zeroth moments removed): TT-carrying modes are linear and so are modes with helicity +-1 weight in some sampled directions",
      okD, "; ".join(rowsD))

print("N5 resolution 1: with exact transverse diffeomorphisms the harmonic TT mode is soft in both storage assignments (momentum stored: no TT-visible first moments; metric stored: X(0) vanishes on traceless tensors).")
print("N5 resolution 2: whatever the residual symmetry, a TT mode linear in every direction leaves helicity +-1 content among the gapless modes on an open dense set of directions: in a linear mode (momentum stored: DeWitt helicity preservation and the 18-dimensional quarter lemma); in a linear or softer mode (metric stored: probe 20's split lemma), linear under premise P. Pre-registered outcome: FAIL.")
print("per_element: each box-kernel move's zeroth and first moments; each sampled symbol.")
print("per_site: the plaquette constraints curl(G mu) = 0 at every site touching the 3^3 box.")
print("per_mode: TT and +-1 components of first moments in 60 directions; the harmonic modes in 30 family-direction pairs.")
print("per_block: the 3^3 box kernel; 5 random move families.")
print("lattice_wide: resolves the span identities and the 18-dimensional quarter bound exactly (quadrature); checked and not executed - states beyond harmonic comparators, non-local terms, composite metrics, the scalar rule softened.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
