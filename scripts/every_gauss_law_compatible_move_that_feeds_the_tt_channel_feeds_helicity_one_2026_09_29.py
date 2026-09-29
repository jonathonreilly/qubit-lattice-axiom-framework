#!/usr/bin/env python3
"""Every Gauss-law-compatible move that feeds the TT channel feeds the helicity-1 channel, at least a quarter as much on direction average.

Question (probe 18's open route: another move set): in probe 15's swapped
assignment (metric stored, exact scalar Gauss law), kinetic terms are built
from moves r with S r = 0. Their O(q^2) kinetic form is fixed by first
moments. Can some move family feed the TT channel at O(q^2) while its
helicity +-1 weight vanishes in every direction? Then an on-site stiffness
could make TT linear with the helicity +-1 partners frozen. Registered in the
probe's scratch file after the scratch computation (so the registration fixes
the reading, not the evidence): PASS if yes, FAIL otherwise.

First-moment space (probe 15 B): 8-dimensional, M(q) = sym(q (x) xi) +
sym(q x A) with xi in R^3 (the gauge patterns) and A symmetric traceless (the
symmetric curls). For a move, r_hat(q) = -i M(q) + O(q^2).

Checks:
  A  the lattice box-kernel first moments (integer kernel of S on a 2^3 box)
     span exactly this 8-dimensional space: each move's q -> M(q) is a
     combination of the 3 + 5 continuum forms (least-squares residual 0).
  B  exact sphere quadrature (product Gauss-Legendre x uniform, exact for
     the polynomial degrees involved): the direction averages obey
     <|M_+-1|^2> = (1/4) <|M_TT|^2> + (1/3)|xi|^2, with no xi-A cross term.
     So for any move family (a sum of such forms) the direction-averaged
     helicity +-1 kinetic weight is at least 1/4 of the TT weight, and every
     nonzero first moment is helicity +-1 visible (the +-1 form is positive
     definite on all 8 dimensions).
  C  lattice families: the box kernel, 200 random integer combinations and
     random sub-families: direction-averaged +-1/TT weight >= 1/4 (exact
     quadrature, lattice first moments).
  D  on-site stiffnesses: the helicity +-1 directions sym(qhat (x) e),
     e _|_ qhat, over all qhat span the traceless symmetric tensors, so any
     on-site positive form that stiffens a TT direction stiffens helicity
     +-1 directions on an open set.
  E  harmonic illustration with random non-covariant move families and an
     |h|^2 stiffness: every family whose linear modes carry TT weight has, in
     some sampled direction, a linear mode with helicity +-1 weight.
  F  over all 18 first-moment dimensions the bound is still 1/4 (spin 2;
     spin 3 gives 8/5).
  G  from the kinetic range to the modes (second-round correction): modes
     in Range K split into linear modes and soft modes (Range K meets
     ker V); the referee's pointwise counterexample (pure-TT linear modes,
     +-1 content in a soft mode) is reproduced; premise P (ker V meets
     ker s(qhat) only in 0) holds off a cone for kernels of dimension <= 1
     and then a linear mode carries +-1 weight; a two-dimensional kernel
     meets ker s(qhat) in every direction.
  H  (added after confirmation) a two-dimensional kernel still cannot hide
     all non-TT content in soft modes: some linear mode is not pure TT on a
     dense set of directions, with no premise P (proof in the note; random
     admissible kernels; control with a singular traceless element).
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import eigh, null_space

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


def mat(i, j):
    M = np.zeros((3, 3)); M[i, j] = 1; return M


S0 = [np.diag([1, -1, 0.]) / np.sqrt(2), np.diag([1, 1, -2.]) / np.sqrt(6)] + [(mat(i, j) + mat(j, i)) / np.sqrt(2) for (i, j) in [(0, 1), (1, 2), (0, 2)]]


def M_cont(v, n):          # continuum first-moment form for v = (xi, a)
    xi, a = v[:3], v[3:]
    A = sum(a[k] * S0[k] for k in range(5))
    g = (np.outer(n, xi) + np.outer(xi, n)) / 2
    C = np.einsum("ikl,k,lj->ij", EPS, n, A)
    return g + (C + C.T) / 2


def parts(M, n):
    a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(n, a_); u /= np.linalg.norm(u); w = np.cross(n, u)
    TT = [(np.outer(u, u) - np.outer(w, w)) / np.sqrt(2), (np.outer(u, w) + np.outer(w, u)) / np.sqrt(2)]
    H1 = [(np.outer(n, u) + np.outer(u, n)) / np.sqrt(2), (np.outer(n, w) + np.outer(w, n)) / np.sqrt(2)]
    return np.array([np.sum(T * M) for T in TT]), np.array([np.sum(T * M) for T in H1])


def offset(a):
    if a < 3:
        return np.zeros(3)
    i, j = FI[a]
    return (E3[i] + E3[j]) / 2


def S_row(x):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    for j in range(3):
        for i in range(3):
            if i != j:
                add(x + E3[i], j, 1); add(x - E3[i], j, 1); add(x, j, -2)
    for (i, j), f in FACE.items():
        add(x, f, -1); add(x - E3[i], f, 1); add(x - E3[j], f, 1); add(x - E3[i] - E3[j], f, -1)
    return d


# ---------------------------------------------------------------- A: lattice first moments = the 3 + 5 continuum forms
nb = 2
box = list(itertools.product(range(nb), repeat=3)); slots = [(c, a) for c in box for a in range(6)]; sidx = {s_: i for i, s_ in enumerate(slots)}
rows = []
for y in itertools.product(range(-2, nb + 2), repeat=3):
    d = S_row(y); row = [0] * len(slots); t = False
    for k, v in d.items():
        if k in sidx:
            row[sidx[k]] += v; t = True
    if t and any(row):
        rows.append(row)
KS = []
for v in sp.Matrix(rows).nullspace():
    den = sp.ilcm(*[sp.fraction(z)[1] for z in v]); w = np.array([int(z * den) for z in v]); KS.append(w // np.gcd.reduce(np.abs(w[w != 0])))
KS = np.array(KS).T.astype(float)


def first_moment_tensor(r):      # the symmetric tensor-valued linear map q -> M(q), as a 3x3x3 array M[i, j, k] (q-coordinate slot -> tensor)
    Mk = np.zeros((3, 3, 3))
    for (c, a), i in sidx.items():
        v = r[i]
        if v:
            p = np.array(c, float) + offset(a)
            if a < 3:
                Mk[a, a] += v * p
            else:
                ii, jj = FI[a]; Mk[ii, jj] += v * p / 2; Mk[jj, ii] += v * p / 2    # q-coordinate 2h_ij -> tensor entry h_ij = value / 2
    return Mk


def M_lat(r, n):
    return np.einsum("ijk,k->ij", first_moment_tensor(r), n)


# least squares: M_lat(r, .) against the 8 continuum forms, over sampled directions
nsamp = rng.normal(size=(12, 3)); nsamp /= np.linalg.norm(nsamp, axis=1)[:, None]
basis = np.array([np.concatenate([M_cont(np.eye(8)[b], n).ravel() for n in nsamp]) for b in range(8)]).T
resid = 0.0; coefs = []
for t in range(KS.shape[1]):
    target = np.concatenate([M_lat(KS[:, t], n).ravel() for n in nsamp])
    c, *_ = np.linalg.lstsq(basis, target, rcond=None); coefs.append(c)
    resid = max(resid, np.abs(basis @ c - target).max())
coefs = np.array(coefs); rank_c = np.linalg.matrix_rank(coefs, tol=1e-9)
# general statement: first moments c[i,j,k] (symmetric in i, j) of any finitely supported r with S r = 0 satisfy
# (q^2 delta_ij - q_i q_j) c_ijk q_k = 0 identically in q: a linear map from 18 unknowns to the 10 cubic monomials; its kernel is 8-dim
mons = [m for m in itertools.product(range(4), repeat=3) if sum(m) == 3]
def cubic_coeffs(c):
    out = np.zeros(len(mons))
    # expand (q^2 delta_ij - q_i q_j) c_ijk q_k
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if c[i, j, k] == 0:
                    continue
                for l in range(3):
                    e = [0, 0, 0]; e[l] += 2; e[k] += 1
                    if i == j:
                        out[mons.index(tuple(e))] += c[i, j, k]
                e = [0, 0, 0]; e[i] += 1; e[j] += 1; e[k] += 1
                out[mons.index(tuple(e))] -= c[i, j, k]
    return out
cb = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
    for k in range(3):
        c = np.zeros((3, 3, 3)); c[i, j, k] = 1; c[j, i, k] = 1; cb.append(c)
Lmap = np.array([cubic_coeffs(c) for c in cb]).T
rank_map = np.linalg.matrix_rank(Lmap, tol=1e-9)
kern = null_space(Lmap)
# the 8 continuum forms, as c-tensors, lie in the kernel
def c_of(v):
    return np.array([[[M_cont(v, np.eye(3)[k])[i, j] for k in range(3)] for j in range(3)] for i in range(3)])
cont_in_kernel = max(np.abs(cubic_coeffs(c_of(np.eye(8)[b]))).max() for b in range(8)) < 1e-12
check("A: for any finitely supported r with S r = 0 the leading symbol forces (q^2 delta_ij - q_i q_j) M_ij(q) = 0, a map of rank 10 on the 18 first-moment unknowns whose 8-dimensional kernel is exactly sym(q (x) xi) + sym(q x A); the 2^3 box kernel realises all 8",
      resid < 1e-9 and rank_c == 8 and rank_map == 10 and kern.shape[1] == 8 and cont_in_kernel, f"rank of the cubic map {rank_map}, kernel {kern.shape[1]}; the 8 continuum forms in the kernel: {cont_in_kernel}; {KS.shape[1]} box moves fit them with residual {resid:.1e}, coefficient rank {rank_c}")

# ---------------------------------------------------------------- B: exact sphere quadrature
x, wx = np.polynomial.legendre.leggauss(10); phis = 2 * np.pi * np.arange(20) / 20
QT = np.zeros((8, 8)); QH = np.zeros((8, 8)); wsum = 0.0
for ct, wc in zip(x, wx):
    st = np.sqrt(1 - ct ** 2)
    for ph in phis:
        n = np.array([st * np.cos(ph), st * np.sin(ph), ct]); wgt = wc * (2 * np.pi / 20)
        Jt = np.zeros((2, 8)); Jh = np.zeros((2, 8))
        for b in range(8):
            t_, h_ = parts(M_cont(np.eye(8)[b], n), n); Jt[:, b] = t_; Jh[:, b] = h_
        QT += wgt * Jt.T @ Jt; QH += wgt * Jh.T @ Jh; wsum += wgt
QT /= wsum; QH /= wsum
cross = np.abs(QH[:3, 3:]).max()
ratio = eigh(QH[3:, 3:], QT[3:, 3:], eigvals_only=True)
okB = cross < 1e-12 and np.allclose(ratio, 0.25, atol=1e-10) and np.allclose(QH[:3, :3], np.eye(3) / 3, atol=1e-10) and np.abs(QT[:3, :]).max() < 1e-12 and np.linalg.eigvalsh(QH).min() > 0.09
check("B: exact sphere quadrature (the analytic proof is in the note): <|M_+-1|^2> = (1/4) <|M_TT|^2> + (1/3)|xi|^2 with no xi-A cross term on average, so every move family's direction-averaged helicity +-1 kinetic weight is at least a quarter of its TT weight, and the +-1 form is positive definite on all 8 first-moment dimensions",
      okB, f"xi-A cross block max {cross:.1e}; +-1/TT ratio on the curl part {np.round(ratio, 12).tolist()}; gauge block of <|M_+-1|^2> = I/3: {np.allclose(QH[:3, :3], np.eye(3) / 3, atol=1e-10)}; smallest eigenvalue of the +-1 form {np.linalg.eigvalsh(QH).min():.4f}")

# ---------------------------------------------------------------- C: lattice families
quad = []
for ct, wc in zip(x, wx):
    st = np.sqrt(1 - ct ** 2)
    for ph in phis:
        quad.append((np.array([st * np.cos(ph), st * np.sin(ph), ct]), wc * (2 * np.pi / 20)))
Mcache = {}


def family_ratio(R_):
    T_ = 0.0; H_ = 0.0
    for n, wgt in quad:
        for t in range(R_.shape[1]):
            t_, h_ = parts(M_lat(R_[:, t], n), n); T_ += wgt * (t_ @ t_); H_ += wgt * (h_ @ h_)
    return H_ / T_ if T_ > 1e-12 else np.inf
rs = [family_ratio(KS)]
for _ in range(200):
    rs.append(family_ratio((KS @ rng.integers(-3, 4, size=KS.shape[1]))[:, None]))
for _ in range(30):
    sub = rng.choice(KS.shape[1], size=3, replace=False); rs.append(family_ratio(KS[:, sub]))
finite = [v for v in rs if np.isfinite(v)]
okC = min(finite) >= 0.25 - 1e-9
check("C: lattice families (the box kernel, 200 random integer combinations, 30 random 3-move sub-families), with the exact quadrature: direction-averaged helicity +-1 / TT kinetic weight >= 1/4",
      okC, f"box kernel {rs[0]:.4f}; min over the random families {min(finite):.4f} (exact quadrature; families with no TT weight skipped: {len(rs) - len(finite)})")

# ---------------------------------------------------------------- D: the helicity +-1 directions span the traceless symmetric tensors
span = []
for n in rng.normal(size=(30, 3)):
    n /= np.linalg.norm(n); a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(n, a_); u /= np.linalg.norm(u); w = np.cross(n, u)
    span += [(np.outer(n, u) + np.outer(u, n)).ravel(), (np.outer(n, w) + np.outer(w, n)).ravel()]
rk = np.linalg.matrix_rank(np.array(span), tol=1e-9)
traceless = all(abs(np.trace(v.reshape(3, 3))) < 1e-12 for v in span)
# every helicity +-1 tensor sym(qhat (x) e) at qhat is a TT tensor at n = qhat x e
def tt_proj(n):
    n = n / np.linalg.norm(n); a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(n, a_); u /= np.linalg.norm(u); w = np.cross(n, u)
    B = np.array([((np.outer(u, u) - np.outer(w, w)) / np.sqrt(2)).ravel(), ((np.outer(u, w) + np.outer(w, u)) / np.sqrt(2)).ravel()]).T
    return B @ B.T
lemma_err = 0.0
for _ in range(500):
    qv = rng.normal(size=3); qv /= np.linalg.norm(qv); e = np.cross(qv, rng.normal(size=3)); e /= np.linalg.norm(e)
    T = ((np.outer(qv, e) + np.outer(e, qv)) / np.sqrt(2)).ravel(); P = tt_proj(np.cross(qv, e))
    lemma_err = max(lemma_err, np.linalg.norm(T - P @ T))
# every 2-plane of traceless symmetric tensors contains a rank-2 element (det restricted to the plane is a real binary cubic, so it has a real root),
# and a rank-2 traceless symmetric tensor is a TT tensor at its null direction; so a PSD stiffness positive on every TT plane has at most a
# one-dimensional kernel among traceless tensors
def traceless_rand():
    M = rng.normal(size=(3, 3)); M = M + M.T; return M - np.trace(M) / 3 * np.eye(3)
plane_ok = True
for _ in range(300):
    A1, A2 = traceless_rand(), traceless_rand()
    ts = np.linspace(0, np.pi, 721); dets = [np.linalg.det(np.cos(t) * A1 + np.sin(t) * A2) for t in ts]
    sign_change = any(dets[k] * dets[k + 1] <= 0 for k in range(len(dets) - 1))
    plane_ok &= sign_change
check("D: the helicity +-1 directions sym(qhat (x) e), e _|_ qhat, span all five traceless tensors, and each of them is a TT tensor at the direction qhat x e; so an on-site stiffness that is positive semidefinite and positive on every TT plane (as a TT mode linear in every direction needs, metric stored) is positive on every helicity +-1 plane and has at most a one-dimensional traceless kernel (every traceless 2-plane contains a TT-type element), hence is positive definite on TT(qhat) + helicity +-1(qhat) off a cone of directions",
      rk == 5 and traceless and lemma_err < 1e-12 and plane_ok, f"rank of 60 sampled +-1 directions: {rk}; all traceless: {traceless}; max distance of sym(qhat (x) e) from TT(qhat x e) over 500 samples: {lemma_err:.1e}; every one of 300 random traceless 2-planes contains a rank-2 (TT-type) element: {plane_ok}")

# ---------------------------------------------------------------- E: harmonic check, random non-covariant families, |h|^2 stiffness
Nmet = np.diag([1, 1, 1, .5, .5, .5])


def Xr(q):
    K = 2 * np.sin(q / 2); X = np.zeros((6, 6)); fc = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
    for a in range(3):
        for b in range(3):
            if a != b:
                X[a, b] = -K[3 - a - b] ** 2
    for a in range(3):
        for f, (i, jj) in fc.items():
            if a not in (i, jj):
                X[a, f] = X[f, a] = K[i] * K[jj]
    for f, (i, jj) in fc.items():
        X[f, f] = K[3 - i - jj] ** 2 / 2
        for g, (kk, l) in fc.items():
            if g != f:
                sh = set((i, jj)) & set((kk, l)); X[f, g] = -K[(set((i, jj)) - sh).pop()] * K[(set((kk, l)) - sh).pop()] / 2
    return X


def S_sym(q):
    K = 2 * np.sin(q / 2); KK = K @ K
    return np.array([K[0] ** 2 - KK, K[1] ** 2 - KK, K[2] ** 2 - KK, K[0] * K[1], K[1] * K[2], K[0] * K[2]], complex)


def rhat(r, q):
    out = np.zeros(6, complex)
    for (c, a), i in sidx.items():
        if r[i]:
            out[a] += r[i] * np.exp(-1j * q @ (np.array(c, float) + offset(a)))
    return out


def linear_modes_pm1(R_, n, m2=1.0):
    """numbers of gapless linear modes at direction n, and the largest helicity +-1 weight among them"""
    om = []; vecs = None
    for eps in (0.02, 0.01):
        q = eps * n; s_ = S_sym(q); B = np.linalg.svd(s_[None, :])[2][1:].conj().T
        kap = sum(np.outer(rhat(R_[:, t], q), rhat(R_[:, t], q).conj()) for t in range(R_.shape[1]))
        Gi = np.linalg.inv(B.conj().T @ B); kred = Gi @ B.conj().T @ kap @ B @ Gi; Vred = B.conj().T @ (Xr(q) + m2 * Nmet) @ B
        w2, V_ = np.linalg.eig(Vred @ kred); o = np.argsort(w2.real)
        om.append(np.sqrt(np.maximum(w2.real[o], 0)) / np.linalg.norm(2 * np.sin(q / 2)))
        if eps == 0.01:
            vecs = [B @ (kred @ V_[:, j]) for j in o]; Kq = 2 * np.sin(q / 2)
    lin = [j for j in range(5) if om[1][j] > 0.05 and abs(om[0][j] - om[1][j]) / om[1][j] < 0.05]
    kh = Kq / np.linalg.norm(Kq); best = 0.0; best_tt = 0.0
    for j in lin:
        hq = vecs[j]; h = np.array([[hq[0], hq[3] / 2, hq[5] / 2], [hq[3] / 2, hq[1], hq[4] / 2], [hq[5] / 2, hq[4] / 2, hq[2]]])
        a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(kh, a_); u /= np.linalg.norm(u); w = np.cross(kh, u)
        H1 = [(np.outer(kh, u) + np.outer(u, kh)) / np.sqrt(2), (np.outer(kh, w) + np.outer(w, kh)) / np.sqrt(2)]
        TTb = [(np.outer(u, u) - np.outer(w, w)) / np.sqrt(2), (np.outer(u, w) + np.outer(w, u)) / np.sqrt(2)]
        tot = np.sum(np.abs(h) ** 2)
        best = max(best, sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in H1) / tot if tot > 0 else 0.0)
        best_tt = max(best_tt, sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in TTb) / tot if tot > 0 else 0.0)
    return len(lin), best, best_tt


okE = True; rowsE = []
for trial in range(8):
    R_ = KS[:, rng.choice(KS.shape[1], size=3, replace=False)]
    res = []
    for n in rng.normal(size=(8, 3)):
        n /= np.linalg.norm(n); res.append(linear_modes_pm1(R_, n))
    tt_w = max(r[2] for r in res); pm1 = max(r[1] for r in res)
    okE &= (tt_w <= 0.05) or pm1 > 0.05
    rowsE.append(f"family {trial}: linear-mode counts {sorted(set(r[0] for r in res))}, largest TT weight {tt_w:.2f} and largest helicity +-1 weight {pm1:.2f} among linear modes")
check("E: harmonic illustration with random non-covariant move families (3 box-kernel moves each) and an |h|^2 stiffness: every family whose linear modes carry TT weight also has, in some sampled direction, a linear mode with helicity +-1 weight (the linear modes are not pure TT)",
      okE, "; ".join(rowsE))

# ---------------------------------------------------------------- F: all 18 first-moment dimensions (moves not constrained by the momentum rule)
basis18 = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]:
    for k in range(3):
        c = np.zeros((3, 3, 3)); c[i, j, k] = 1; c[j, i, k] = 1; basis18.append(c / np.linalg.norm(c))
QT18 = np.zeros((18, 18)); QH18 = np.zeros((18, 18))
for n, wgt in quad:
    Jt = np.zeros((2, 18)); Jh = np.zeros((2, 18))
    for b, c in enumerate(basis18):
        t_, h_ = parts(np.einsum("ijk,k->ij", c, n), n); Jt[:, b] = t_; Jh[:, b] = h_
    QT18 += wgt * Jt.T @ Jt; QH18 += wgt * Jh.T @ Jh
QT18 /= sum(w_ for _, w_ in quad); QH18 /= sum(w_ for _, w_ in quad)
wt, V = np.linalg.eigh(QT18); Rr = V[:, wt > 1e-10]; Zz = V[:, wt <= 1e-10]
Sc = Rr.T @ QH18 @ Rr - (Rr.T @ QH18 @ Zz) @ np.linalg.pinv(Zz.T @ QH18 @ Zz) @ (Zz.T @ QH18 @ Rr)
lam18 = eigh(Sc, Rr.T @ QT18 @ Rr, eigvals_only=True)
check("F: over all 18 first-moment dimensions (moves not restricted by any rule, as in the momentum-stored assignment with the momentum rule broken) the direction-averaged helicity +-1 weight is still at least 1/4 of the TT weight: the minimum 1/4 comes from spin 2, spin 3 gives 8/5 (Schur complement over the TT-invisible parts)",
      abs(lam18.min() - 0.25) < 1e-9 and abs(lam18.max() - 1.6) < 1e-9, f"TT-visible dimension {Rr.shape[1]}; +-1/TT ratios {np.round(np.unique(np.round(lam18, 9)), 6).tolist()}")

# ---------------------------------------------------------------- G: from the kinetic range to the modes (the referee's counterexample; premise P)
B6 = S0 + [np.eye(3) / np.sqrt(3)]


def vec6(M):
    return np.array([np.sum(b * M) for b in B6])


def ten6(v):
    return sum(v[k] * B6[k] for k in range(6))


def s_of(n):                 # leading symbol of the scalar stencil at qhat = n, as a functional on 6-vectors
    return np.array([n @ b @ n - np.trace(b) for b in B6])


def range_modes(K, V):
    """modes of x'' = -K V x inside Range K: returns (positive eigenvalues, positive modes, zero modes)"""
    ev, U = np.linalg.eigh(K); keep = ev > 1e-10; Bm = U[:, keep] * np.sqrt(ev[keep])
    lam, Y = np.linalg.eigh(Bm.T @ V @ Bm)
    pos = [Bm @ Y[:, i] for i in range(len(lam)) if lam[i] > 1e-9]; zer = [Bm @ Y[:, i] for i in range(len(lam)) if lam[i] <= 1e-9]
    return lam[lam > 1e-9], pos, zer


def weights(x, n):
    t_, h_ = parts(ten6(x), n); tot = x @ x
    return (t_ @ t_) / tot, (h_ @ h_) / tot


def min_on_tt_planes(V, samples=400):
    mins = []
    for n in rng.normal(size=(samples, 3)):
        n /= np.linalg.norm(n); a_ = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(n, a_); u /= np.linalg.norm(u); w = np.cross(n, u)
        Tb = np.array([vec6((np.outer(u, u) - np.outer(w, w)) / np.sqrt(2)), vec6((np.outer(u, w) + np.outer(w, u)) / np.sqrt(2))]).T
        mins.append(np.linalg.eigvalsh(Tb.T @ V @ Tb).min())
    return min(mins)


# G1: the referee's pointwise counterexample at qhat = z: u = (TT1 + H1x + nn)/sqrt(3), V = 1 - u u^T, K = P_TT + u u^T
z = np.array([0, 0, 1.]); ex, ey = np.array([1., 0, 0]), np.array([0, 1., 0])
TT1 = vec6((np.outer(ex, ex) - np.outer(ey, ey)) / np.sqrt(2)); TT2 = vec6((np.outer(ex, ey) + np.outer(ey, ex)) / np.sqrt(2))
H1x = vec6((np.outer(z, ex) + np.outer(ex, z)) / np.sqrt(2)); NN = vec6(np.outer(z, z))
uv = (TT1 + H1x + NN) / np.sqrt(3); V1 = np.eye(6) - np.outer(uv, uv); K1 = np.outer(TT1, TT1) + np.outer(TT2, TT2) + np.outer(uv, uv)
lam1, pos1, zer1 = range_modes(K1, V1)
g1_tt_min = min_on_tt_planes(V1)          # >= 1 - |traceless part of u|^2 = 1/9
g1_pos_pure = all(weights(x, z)[0] > 1 - 1e-12 for x in pos1)
g1_zero_pm1 = [weights(x, z)[1] for x in zer1]
g1_ok = (abs(s_of(z) @ uv) < 1e-12 and np.allclose(sorted(lam1), [2 / 3, 1]) and g1_pos_pure and len(zer1) == 1
         and abs(g1_zero_pm1[0] - 1 / 3) < 1e-12 and g1_tt_min > 1 / 9 - 1e-9)

# G2: premise P (stiffness kernel meets ker s(qhat) only in 0): with a kernel of dimension <= 1 it holds off a quadric cone; then some linear mode carries +-1 weight
fam_ok = True; n_dirs = 0; n_P_fail = 0; min_best = 1.0
wk = rng.normal(size=6); wk /= np.linalg.norm(wk)
stiff = {"kernel = trace (probe 18)": np.eye(6) - np.outer(vec6(np.eye(3) / np.sqrt(3)), vec6(np.eye(3) / np.sqrt(3))), "kernel = random w": np.eye(6) - np.outer(wk, wk)}
for name, V in stiff.items():
    fam_ok &= min_on_tt_planes(V) > 1e-6
    for trial in range(6):
        vs = rng.normal(size=(3, 8))
        for n in rng.normal(size=(40, 3)):
            n /= np.linalg.norm(n); n_dirs += 1
            Ms = [vec6(M_cont(v, n)) for v in vs]; K = sum(np.outer(m, m) for m in Ms)
            kin_pm1 = sum(np.sum(parts(ten6(m), n)[1] ** 2) for m in Ms)
            ker = null_space(np.vstack([V, s_of(n)[None, :]]), rcond=1e-9)
            if ker.shape[1] > 0:
                n_P_fail += 1; continue
            lam, pos, zer = range_modes(K, V)
            best = max(weights(x, n)[1] for x in pos)
            fam_ok &= (len(zer) == 0) and (kin_pm1 < 1e-12 or best > 1e-8)
            if kin_pm1 > 1e-6:
                min_best = min(min_best, best)

# G3: a two-dimensional kernel (trace and one nonsingular traceless k) meets ker s(qhat) at every direction, so the soft alternative is not excluded pointwise
kv = vec6(np.diag([1, 1, -2.]) / np.sqrt(6)); tv = vec6(np.eye(3) / np.sqrt(3)); V3 = np.eye(6) - np.outer(kv, kv) - np.outer(tv, tv)
g3_meet = all(null_space(np.vstack([V3, s_of(n / np.linalg.norm(n))[None, :]]), rcond=1e-9).shape[1] == 1 for n in rng.normal(size=(200, 3)))
g3_ok = g3_meet and min_on_tt_planes(V3) > 1e-6
check("G: from the kinetic range to the modes. The modes inside Range K split as positive modes plus Range K intersect ker V, so if the positive modes are pure TT the non-TT kinetic content sits in soft modes. The referee's pointwise counterexample (qhat = z, V = 1 - u u^T, K = P_TT + u u^T, u = (TT1 + H1x + nn)/sqrt 3) has pure-TT linear modes and one soft mode with helicity +-1 weight 1/3. Premise P (ker V meets ker s(qhat) only in 0) excludes the soft alternative; it holds off a quadric cone when the stiffness kernel has dimension <= 1 (probe 18's kernel, the trace, never meets ker s), and then some linear mode carries +-1 weight. A two-dimensional kernel meets ker s(qhat) in every direction (open case)",
      g1_ok and fam_ok and g3_ok,
      f"G1: positive eigenvalues {np.round(sorted(lam1), 6).tolist()}, positive modes pure TT: {g1_pos_pure}, soft-mode +-1 weight {np.round(g1_zero_pm1, 6).tolist()}, smallest eigenvalue of V on 400 sampled TT planes {g1_tt_min:.3f} (bound 1/9); "
      f"G2: {n_dirs} family-direction pairs with two kernel-<=1 stiffnesses, premise P failed at {n_P_fail}, elsewhere no soft mode in Range K and some linear mode with +-1 weight (smallest largest +-1 weight {min_best:.3f}): {fam_ok}; "
      f"G3: two-dimensional kernel meets ker s at all 200 sampled directions: {g3_meet}")

# ---------------------------------------------------------------- H: a two-dimensional stiffness kernel (added after confirmation)
# ker V = span{t, k}, tr t = 1, k traceless and nonsingular (a singular traceless tensor is TT at its null direction). In direction n,
# ker V meets ker s(n) along w(n) = (n.k.n) t - (n.t.n - |n|^2) k. Pure-TT linear modes on an open set of directions would force every
# move's g(n) = M(n) n to be parallel to f(n) = w(n) n (for T in ker s(n), T n fixes T's non-TT part); f is a primitive cubic (the note's
# proof: finitely many common complex zeros), so g = 0 and the move vanishes. Checked on random admissible kernels; the weaker scalar
# condition det(n, g, f) = 0 (non-TT content of the linear modes only of helicity 0) is also checked on random kernels (open in general).
def f_two(n, t, k):
    return ((n @ k @ n) * t - (n @ t @ n - n @ n) * k) @ n


rgH = np.random.default_rng(314)
NSH = rgH.normal(size=(80, 3)); NSH /= np.linalg.norm(NSH, axis=1)[:, None]
ratios_par = []; ratios_det = []; dets_k = []
for trial in range(30):
    while True:
        a_k = rgH.normal(size=5); kH = sum(a_k[j] * S0[j] for j in range(5)); kH /= np.linalg.norm(kH)
        if abs(np.linalg.det(kH)) > 0.05:
            break
    tH = np.eye(3) / 3 + sum(rgH.normal() * S0[j] for j in range(5)); dets_k.append(abs(np.linalg.det(kH)))
    rows_par = []; rows_det = []
    for n in NSH:
        fv = f_two(n, tH, kH); gcols = [M_cont(np.eye(8)[b], n) @ n for b in range(8)]
        rows_par.append(np.array([np.cross(gc, fv) for gc in gcols]).T)
        rows_det.append([np.linalg.det(np.array([n, gc, fv])) for gc in gcols])
    sv = np.linalg.svd(np.vstack(rows_par), compute_uv=False); ratios_par.append(sv[-1] / sv[0])
    sv = np.linalg.svd(np.array(rows_det), compute_uv=False); ratios_det.append(sv[-1] / sv[0])
# control: a singular traceless k (a TT-type tensor, excluded by positivity on TT planes) does admit a nonzero solution
kS = np.diag([-1, 0, 1.]) / np.sqrt(2); tS = np.array([[0, 0, 1.], [0, 1, 0], [1, 0, 0]])     # k singular (TT at the y direction), tr t = 1
rows_c = []
for n in NSH:
    fv = f_two(n, tS, kS); rows_c.append(np.array([np.cross(M_cont(np.eye(8)[b], n) @ n, fv) for b in range(8)]).T)
svc = np.linalg.svd(np.vstack(rows_c), compute_uv=False); ctrl = svc[-1] / svc[0]
okH = min(ratios_par) > 1e-3 and min(ratios_det) > 1e-3 and ctrl < 1e-10
check("H: a stiffness kernel of dimension two (a trace-one tensor t plus a nonsingular traceless k) cannot hide all non-TT content in soft modes: pure-TT linear modes on an open set of directions would force M(n) n parallel to the primitive cubic f(n) = w(n) n, hence every move to vanish (proof in the note); so with no premise P some linear mode is not pure TT on a dense set of directions. Checked on 30 random admissible kernels (only the zero move); the weaker helicity-0-only condition det(n, g, f) = 0 also has only the zero move on these kernels (not proved in general); control: a singular traceless k, which positivity on TT planes excludes, admits a nonzero move",
      okH, f"parallel condition, smallest singular ratio over 30 kernels {min(ratios_par):.3f}; helicity-0-only condition {min(ratios_det):.3f}; control with singular k {ctrl:.1e}; smallest |det k| {min(dets_k):.3f}")

print("N5 resolution 1: every Gauss-law-compatible move with a TT-visible first moment is helicity +-1 visible; averaged over directions the +-1 weight is at least a quarter of the TT weight, for any move family (exact quadrature).")
print("N5 resolution 2: so breaking the momentum rule by an on-site stiffness to make the TT modes linear in every direction leaves, in an open dense set of directions, non-TT kinetic content that sits either in a linear mode or in a softer mode inside the kinetic range; with premise P (stiffness kernel meeting ker s(qhat) only in 0, true off a cone when that kernel has dimension <= 1) some linear mode carries helicity +-1 weight; with no premise, some linear mode is not pure TT on a dense set of directions (H). Pre-registered outcome: FAIL.")
print("per_element: each box-kernel move's first moments fitted to the 3 + 5 continuum forms; each random family's weights.")
print("per_site: the scalar rule at every site touching the 2^3 box.")
print("per_mode: TT and helicity +-1 components on the exact quadrature grid; the five harmonic modes in 64 family-direction pairs; the modes inside the kinetic range in 480 family-direction pairs (G); the parallel condition of H at 80 directions for 30 admissible kernels and a singular-kernel control.")
print("per_block: the 2^3 box kernel, 200 random integer combinations, 38 random sub-families; 12 random 3-move families (G); 30 random two-dimensional stiffness kernels (H).")
print("lattice_wide: resolves the direction-averaged identity exactly by quadrature for the full 8-dimensional first-moment space, and (by the note's proofs) the split lemma and Lemma H for every PSD on-site stiffness positive on every TT plane; checked and not executed - whether a two-dimensional kernel's linear modes must carry helicity +-1 rather than helicity 0 only, higher-moment (O(q^3)) kinetic terms, non-harmonic states, non-on-site symmetry breaking.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
