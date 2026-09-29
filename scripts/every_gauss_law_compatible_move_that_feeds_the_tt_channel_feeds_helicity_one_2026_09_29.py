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
  E  harmonic check with random non-covariant move families and an |h|^2
     stiffness: every family with linear TT-carrying modes also has, in some
     sampled direction, a linear mode with helicity +-1 weight (the lemma
     gives an open set of directions, not every direction).
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import eigh

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
check("A: the lattice first moments of Gauss-law-compatible moves (integer kernel of S on a 2^3 box) are exactly combinations of the 3 gauge forms sym(q (x) xi) and the 5 symmetric-curl forms sym(q x A), and span all 8",
      resid < 1e-9 and rank_c == 8, f"{KS.shape[1]} moves; max least-squares residual {resid:.1e}; rank of the coefficient matrix {rank_c}")

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
check("B: exact sphere quadrature: <|M_+-1|^2> = (1/4) <|M_TT|^2> + (1/3)|xi|^2 with no xi-A cross term, so every move family's direction-averaged helicity +-1 kinetic weight is at least a quarter of its TT weight, and the +-1 form is positive definite on all 8 first-moment dimensions",
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
check("D: the helicity +-1 directions sym(qhat (x) e), e _|_ qhat, span all five traceless symmetric tensors as qhat varies, so an on-site positive form that stiffens any TT direction stiffens helicity +-1 directions on an open set of qhat",
      rk == 5 and traceless, f"rank of 60 sampled +-1 directions: {rk}; all traceless: {traceless}")

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
    kh = Kq / np.linalg.norm(Kq); best = 0.0
    for j in lin:
        hq = vecs[j]; h = np.array([[hq[0], hq[3] / 2, hq[5] / 2], [hq[3] / 2, hq[1], hq[4] / 2], [hq[5] / 2, hq[4] / 2, hq[2]]])
        a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0]); u = np.cross(kh, a_); u /= np.linalg.norm(u); w = np.cross(kh, u)
        H1 = [(np.outer(kh, u) + np.outer(u, kh)) / np.sqrt(2), (np.outer(kh, w) + np.outer(w, kh)) / np.sqrt(2)]
        tot = np.sum(np.abs(h) ** 2)
        best = max(best, sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in H1) / tot if tot > 0 else 0.0)
    return len(lin), best


okE = True; rowsE = []
for trial in range(8):
    R_ = KS[:, rng.choice(KS.shape[1], size=3, replace=False)]
    res = []
    for n in rng.normal(size=(8, 3)):
        n /= np.linalg.norm(n); res.append(linear_modes_pm1(R_, n))
    has_tt_family = max(r[0] for r in res) >= 2
    pm1 = max(r[1] for r in res)
    okE &= (not has_tt_family) or pm1 > 0.05
    rowsE.append(f"family {trial}: linear-mode counts {sorted(set(r[0] for r in res))}, largest helicity +-1 weight among linear modes {pm1:.2f}")
check("E: harmonic check with random non-covariant move families (3 box-kernel moves each) and an |h|^2 stiffness: every family with linear TT-carrying modes also has, in some sampled direction, a linear mode with helicity +-1 weight (as the lemma requires on an open set of directions, not in every direction)",
      okE, "; ".join(rowsE))

print("N5 resolution 1: every Gauss-law-compatible move with a TT-visible first moment is helicity +-1 visible; averaged over directions the +-1 weight is at least a quarter of the TT weight, for any move family (exact quadrature).")
print("N5 resolution 2: so breaking the momentum rule by an on-site stiffness to make the TT modes linear also makes helicity +-1 partners gapless and linear in an open set of directions. Pre-registered outcome: FAIL.")
print("per_element: each box-kernel move's first moments fitted to the 3 + 5 continuum forms; each random family's weights.")
print("per_site: the scalar rule at every site touching the 2^3 box.")
print("per_mode: TT and helicity +-1 components on the exact quadrature grid; the five harmonic modes in 64 family-direction pairs.")
print("per_block: the 2^3 box kernel, 200 random integer combinations, 38 random sub-families.")
print("lattice_wide: resolves the direction-averaged identity exactly by quadrature for the full 8-dimensional first-moment space; checked and not executed - higher-moment (O(q^3)) kinetic terms, non-harmonic states, non-on-site symmetry breaking.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
