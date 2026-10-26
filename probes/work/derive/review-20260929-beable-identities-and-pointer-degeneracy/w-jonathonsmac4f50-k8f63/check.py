#!/usr/bin/env python3
"""Slater-column ("Laplace") carrier assignments under changes of representative.

Scope: ONE sub-obligation of J:derive:review-20260929-beable-identities-and-pointer-degeneracy:a1
(the 'Slater-column carrier assignments under basis changes with exact determinants' part).
Not attempted here: Born-equivariance/dt-error bound, pointer impurity at L=10.

Setting (supplied, not axiom content): N0 sea orbitals S (columns) and one added orbital phi.
For a configuration of N = N0+1 occupied sites, A is the N x N matrix of orbital values
(rows = occupied sites, column 0 = phi, columns 1..N0 = sea).  Amplitude = det A.
Laplace term for row i:  t_i = A[i,0] * (A^{-1})[0,i]   (so det A * t_i is the i-th term of the
expansion of det A along column 0).  'Laplace carrier weight' p_i = |t_i|^2 / sum_j |t_j|^2.

Machinery: Fractions (own Bareiss determinant, own Gauss-Jordan), sympy for Gaussian-rational
entries, numpy/mpmath only for the ring ensemble part.  Disjoint from the source scripts.
"""
import sys, random, itertools, time
from fractions import Fraction as F
import numpy as np
import sympy as sp
import mpmath as mp

RESULTS = []
T0 = time.time()


def rec(ok, msg):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg)
    sys.stdout.flush()


# ---------------------------------------------------------------- exact helpers (Fractions)
def det_frac(M):
    """Fraction determinant by fraction-free-style elimination with row swaps (exact)."""
    n = len(M)
    A = [row[:] for row in M]
    d = F(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if A[r][c] != 0:
                p = r
                break
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return d


def minor_frac(M, i, j):
    return det_frac([[M[r][c] for c in range(len(M)) if c != j] for r in range(len(M)) if r != i])


def t_by_cofactor(M):
    """t_i = A[i,0]*(-1)^i*minor(i,0)/det  -- Laplace definition, no matrix inverse used."""
    d = det_frac(M)
    return [M[i][0] * (-1) ** i * minor_frac(M, i, 0) / d for i in range(len(M))], d


def inv_frac(M):
    n = len(M)
    A = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [row[n:] for row in A]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def rank_frac(M):
    A = [row[:] for row in M]
    r = 0
    rows, cols = len(A), len(A[0])
    for c in range(cols):
        p = next((k for k in range(r, rows) if A[k][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for k in range(rows):
            if k != r and A[k][c] != 0:
                f = A[k][c] / A[r][c]
                A[k] = [a - f * b for a, b in zip(A[k], A[r])]
        r += 1
    return r


def rand_mat(n, rng, lo=-6, hi=6):
    while True:
        M = [[F(rng.randint(lo, hi)) for _ in range(n)] for _ in range(n)]
        if det_frac(M) != 0 and all(minor_frac(M, i, 0) != 0 for i in range(n)):
            return M


def with_col0(M, col):
    return [[col[i]] + M[i][1:] for i in range(len(M))]


# ---------------------------------------------------------------- C1: identities, Levi / unipotent action
rng = random.Random(20260929)
N0 = 4
N = N0 + 1
ok_sum = ok_inv = ok_det = ok_dual = ok_levi = True
nneg = 0
for trial in range(40):
    A = rand_mat(N, rng)
    t, d = t_by_cofactor(A)
    Ai = inv_frac(A)
    t_inv = [A[i][0] * Ai[0][i] for i in range(N)]
    ok_inv &= (t == t_inv)
    ok_sum &= (sum(t) == 1)
    nneg += any(x < 0 for x in t)
    # unipotent change: column 0 -> column 0 + sum_k y_k column k  (same Slater state, same amplitudes)
    y = [F(rng.randint(-9, 9)) for _ in range(N0)]
    col = [A[i][0] + sum(y[k] * A[i][k + 1] for k in range(N0)) for i in range(N)]
    A2 = with_col0(A, col)
    ok_det &= (det_frac(A2) == d)
    A2i = inv_frac(A2)
    ok_dual &= (A2i[0] == Ai[0])  # row 0 of the inverse (the dual vector b) is unchanged
    t2, _ = t_by_cofactor(A2)
    ok_sum &= (sum(t2) == 1)
    # Levi change: scale column 0 and mix sea columns by GL(N0): t unchanged
    lam = F(rng.randint(1, 7), rng.randint(1, 7)) * rng.choice([-1, 1])
    while True:
        G = [[F(rng.randint(-4, 4)) for _ in range(N0)] for _ in range(N0)]
        if det_frac(G) != 0:
            break
    sea = [[A[i][k + 1] for k in range(N0)] for i in range(N)]
    sea2 = matmul(sea, G)
    A3 = [[lam * A[i][0]] + sea2[i] for i in range(N)]
    t3, d3 = t_by_cofactor(A3)
    ok_levi &= (t3 == t) and (d3 == lam * det_frac(G) * d)
rec(ok_inv, "C1a Laplace definition via cofactors equals A[i,0]*(A^-1)[0,i] exactly (40 random 5x5 rational matrices)")
rec(ok_sum, "C1b sum_i t_i = 1 exactly for every matrix and every representative")
rec(ok_det and ok_dual, "C1c column0 -> column0 + sea-span element: det A unchanged and row 0 of A^-1 unchanged exactly")
rec(ok_levi, "C1d t invariant exactly under column-0 scaling and any GL(N0) mixing of sea columns (Levi subgroup)")
rec(nneg > 0, "C1e t_i can be negative for rational matrices (%d/40 had a negative entry): t is not a probability vector" % nneg)

# ---------------------------------------------------------------- C2: realizability theorem
# Claim: fix S (sea columns) and a.  For every vector tau in Q^N with sum tau = 1 and tau_i = 0 whenever
# b_i = 0, there is y with  a' = a + S y  and  t(a') = tau.  Here b = row 0 of A^{-1}.
def realize(A, tau):
    N = len(A)
    Ai = inv_frac(A)
    b = Ai[0]
    ap = [tau[i] / b[i] for i in range(N)]               # requires b_i != 0
    v = [ap[i] - A[i][0] for i in range(N)]
    # solve S y = v (S = columns 1..N-1, N x (N-1), full column rank): use A^{-1}: A y' = v with y'_0 = 0 needed
    coef = [sum(Ai[k][i] * v[i] for i in range(N)) for k in range(N)]   # coefficients of v in basis of columns
    return ap, coef


ok_real = True
ok_state = True
det_checks = 0
for trial in range(25):
    A = rand_mat(N, rng)
    t0, d0 = t_by_cofactor(A)
    for target in range(N + 3):
        if target < N:
            tau = [F(int(i == target)) for i in range(N)]     # deterministic: site `target` carries it
        else:
            w = [F(rng.randint(-5, 5)) for _ in range(N)]
            s = sum(w) if sum(w) != 0 else F(1)
            tau = [x / s for x in w] if sum(w) != 0 else [F(int(i == 0)) for i in range(N)]
        ap, coef = realize(A, tau)
        ok_state &= (coef[0] == 0)                       # a' - a lies in the sea span (no column-0 component)
        A2 = with_col0(A, ap)
        t2, d2 = t_by_cofactor(A2)                       # independent: cofactor route, fresh determinants
        ok_real &= (t2 == tau)
        ok_real &= (d2 == d0)
        det_checks += 1
rec(ok_state, "C2a every target tau (sum 1) is reached by a' with a'-a in the sea span: component on the added column is exactly 0")
rec(ok_real, "C2b %d exact constructions: t(a') = tau and det unchanged, incl. deterministic tau = e_j for every occupied site j" % det_checks)

# the map y -> (S y) o b has image exactly {x : sum x = 0}: rank N0 = N-1
rk_ok = True
for trial in range(20):
    A = rand_mat(N, rng)
    Ai = inv_frac(A)
    b = Ai[0]
    cols = [[A[i][k + 1] * b[i] for k in range(N0)] for i in range(N)]       # N x N0
    rk_ok &= (rank_frac(cols) == N0)
    rk_ok &= all(sum(cols[i][k] for i in range(N)) == 0 for k in range(N0))
rec(rk_ok, "C2c y -> (S y)*b is injective with image inside {sum=0} and of dimension N0=N-1, hence equal to it")

# forced zeros: if b_i = 0 then t_i = 0 for every representative
# explicit example: sea rows 0 and 2 equal, so deleting any other row leaves a singular sea block
Srows = [[1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
c0 = [3, 2, 1, 4, 5]
A = [[F(c0[i])] + [F(v) for v in Srows[i]] for i in range(N)]
bsup = [(-1) ** i * minor_frac(A, i, 0) for i in range(N)]
zero_idx = [i for i in range(N) if bsup[i] == 0]
ok_zero = len(zero_idx) >= 1 and det_frac(A) != 0
for _ in range(30):
    y = [F(rng.randint(-9, 9)) for _ in range(N0)]
    col = [A[i][0] + sum(y[k] * A[i][k + 1] for k in range(N0)) for i in range(N)]
    t2, _ = t_by_cofactor(with_col0(A, col))
    ok_zero &= all(t2[i] == 0 for i in zero_idx) and sum(t2) == 1
rec(ok_zero, "C2d where b_i=0 (site i carries zero sea-minor) t_i = 0 for every representative, rest still sum to 1 (support = {b_i != 0})")

# ---------------------------------------------------------------- C3: Gaussian-rational (complex) version with sympy
def grat(rng):
    return sp.Rational(rng.randint(-5, 5), rng.randint(1, 3)) + sp.I * sp.Rational(rng.randint(-5, 5), rng.randint(1, 3))


rngc = random.Random(77)
ok_c = True
for trial in range(5):
    while True:
        Ac = sp.Matrix(4, 4, lambda i, j: grat(rngc))
        if Ac.det() != 0:
            break
    d = sp.expand(Ac.det())
    Aci = Ac.inv()
    tc = [sp.expand(Ac[i, 0] * Aci[0, i]) for i in range(4)]
    ok_c &= sp.simplify(sum(tc) - 1) == 0
    y = [grat(rngc) for _ in range(3)]
    col = Ac[:, 0] + Ac[:, 1:] * sp.Matrix(y)
    A2 = Ac.copy()
    A2[:, 0] = col
    ok_c &= sp.simplify(A2.det() - d) == 0
    A2i = A2.inv()
    ok_c &= all(sp.simplify(A2i[0, i] - Aci[0, i]) == 0 for i in range(4))
    t2 = [sp.expand(A2[i, 0] * A2i[0, i]) for i in range(4)]
    # complex weights |t|^2 changed
    w1 = [sp.simplify(sp.Abs(x) ** 2) for x in tc]
    w2 = [sp.simplify(sp.Abs(x) ** 2) for x in t2]
    ok_c &= sp.simplify(sum(t2) - 1) == 0
    ok_c &= any(sp.simplify(a - b) != 0 for a, b in zip(w1, w2))
rec(ok_c, "C3 complex Gaussian-rational 4x4 (sympy exact): det and dual row unchanged, sum t = 1, |t_i|^2 weights change")

# ---------------------------------------------------------------- C4: Born-ensemble identity (exact)
# sum over configurations containing site x of |Psi(conf)|^2 |t_x(conf)|^2 = |phi(x)|^2 * sum_{conf' not containing x} |Psi_sea(conf')|^2
Lsites, n0 = 6, 2
rng4 = random.Random(5)
S4 = [[F(rng4.randint(-4, 4)) for _ in range(n0)] for _ in range(Lsites)]
phi = [F(rng4.randint(-4, 4)) for _ in range(Lsites)]
while rank_frac(S4) < n0:
    S4 = [[F(rng4.randint(-4, 4)) for _ in range(n0)] for _ in range(Lsites)]


def ensemble_density(phi):
    out = [F(0)] * Lsites
    for conf in itertools.combinations(range(Lsites), n0 + 1):
        A = [[phi[x]] + S4[x] for x in conf]
        d = det_frac(A)
        if d == 0:
            continue
        for i, x in enumerate(conf):
            Mi = minor_frac(A, i, 0)                    # = sea amplitude on conf minus x (up to sign)
            out[x] += (A[i][0] * Mi) ** 2               # |Psi|^2 |t_i|^2 = |A_i0 M_i0|^2
    return out


def rhs(phi):
    out = []
    for x in range(Lsites):
        z = F(0)
        for c in itertools.combinations([s for s in range(Lsites) if s != x], n0):
            z += det_frac([S4[s] for s in c]) ** 2
        out.append(phi[x] ** 2 * z)
    return out


lhs0 = ensemble_density(phi)
ok4 = (lhs0 == rhs(phi))
y4 = [F(3), F(-2)]
phi2 = [phi[x] + sum(y4[k] * S4[x][k] for k in range(n0)) for x in range(Lsites)]
lhs2 = ensemble_density(phi2)
ok4 &= (lhs2 == rhs(phi2))
# same many-body state: all amplitudes equal
same = all(det_frac([[phi[x]] + S4[x] for x in c]) == det_frac([[phi2[x]] + S4[x] for x in c])
           for c in itertools.combinations(range(Lsites), n0 + 1))
rec(ok4, "C4a Born-ensemble identity  sum_conf |Psi|^2 |t_x|^2 = |phi(x)|^2 * (sea weight of configs avoiding x), exact (L=6, N0=2), both representatives")
rec(same and lhs0 != lhs2, "C4b the two representatives have identical amplitudes on all 20 configurations but different ensemble carrier densities")

# ---------------------------------------------------------------- C5: 'canonical' (orthogonal) representative depends on a metric
Wd = [F(1), F(2), F(1), F(3), F(1), F(5)]


def proj_rep(phi, W):
    # phi_perp w.r.t. <u,v>_W = sum W_x u_x v_x : subtract sea-span component (exact normal equations)
    G = [[sum(W[x] * S4[x][a] * S4[x][b] for x in range(Lsites)) for b in range(n0)] for a in range(n0)]
    r = [sum(W[x] * S4[x][a] * phi[x] for x in range(Lsites)) for a in range(n0)]
    Gi = inv_frac(G)
    c = [sum(Gi[a][b] * r[b] for b in range(n0)) for a in range(n0)]
    return [phi[x] - sum(c[a] * S4[x][a] for a in range(n0)) for x in range(Lsites)], c


rep_I, _ = proj_rep(phi, [F(1)] * Lsites)
rep_W, _ = proj_rep(phi, Wd)
ok5 = True
ortho = all(sum(rep_I[x] * S4[x][a] for x in range(Lsites)) == 0 for a in range(n0))
orthoW = all(sum(Wd[x] * rep_W[x] * S4[x][a] for x in range(Lsites)) == 0 for a in range(n0))
ok5 &= ortho and orthoW
amp_same = all(det_frac([[rep_I[x]] + S4[x] for x in c]) == det_frac([[rep_W[x]] + S4[x] for x in c]) for c in
               itertools.combinations(range(Lsites), n0 + 1))
differs = False
for conf in itertools.combinations(range(Lsites), n0 + 1):
    if det_frac([[rep_I[x]] + S4[x] for x in conf]) == 0:
        continue
    t1, _ = t_by_cofactor([[rep_I[x]] + S4[x] for x in conf])
    t2, _ = t_by_cofactor([[rep_W[x]] + S4[x] for x in conf])
    if t1 != t2:
        differs = True
rec(ok5 and amp_same and differs,
    "C5 two 'canonical' (orthogonal-to-sea) representatives for two inner products give identical amplitudes but different Laplace weights (exact)")

# ---------------------------------------------------------------- C6: the split (added orbital, sea) is not intrinsic either
A = rand_mat(N, rng)
tA, dA = t_by_cofactor(A)
# same state: swap column 0 with column 1 (sign flip only); then 'column 0' is a different orbital
Asw = [[A[i][1], A[i][0]] + A[i][2:] for i in range(N)]
tS, dS = t_by_cofactor(Asw)
rec(dS == -dA and tS != tA and sum(tS) == 1,
    "C6 relabelling which orbital is 'the added one' (same N-particle state up to sign) changes t exactly")

# ---------------------------------------------------------------- C7: physical ring, full Born ensemble, no Monte Carlo
mp.mp.dps = 50


def ring_ensemble(L, n0, tt, extra_coeffs, tag):
    """Exact enumeration over all C(L, n0+1) configurations (float64), antiperiodic ring, h = -hop.
    Returns Born-averaged second moment of carrier displacement, excess density second moment, etc."""
    ks = np.array([(2 * m + 1) * np.pi / L for m in range(L)])
    ks = np.where(ks > np.pi, ks - 2 * np.pi, ks)
    E = -2 * np.cos(ks)
    x = np.arange(L)
    modes = np.exp(1j * np.outer(x, ks)) / np.sqrt(L)       # modes[x, m]
    order = np.argsort(E)
    sea_idx = order[:n0]
    emp_idx = order[n0:]
    assert abs(E[order[n0 - 1]] - E[order[n0]]) > 1e-9, "degenerate Fermi level"
    sea_t = modes[:, sea_idx] * np.exp(-1j * E[sea_idx] * tt)
    # added orbital e_0 evolved
    phi0_modes = np.conj(modes[0, :])                       # <mode_m | e_0>
    e0_t = (modes * (phi0_modes * np.exp(-1j * E * tt))).sum(axis=1)
    perp_t = (modes[:, emp_idx] * (phi0_modes[emp_idx] * np.exp(-1j * E[emp_idx] * tt))).sum(axis=1)
    reps = {}
    reps["canonical (orthogonal to sea)"] = perp_t
    reps["plain e_0"] = e0_t
    for name, c in extra_coeffs.items():
        # add c * (sea orbital k) -- coefficient fixed in time-0 picture, evolved with the sea orbital
        v = perp_t.copy()
        for k, ck in c.items():
            v = v + ck * sea_t[:, k]
        reps[name] = v
    d = np.minimum(x, L - x).astype(float)                   # minimal-image distance from origin
    out = {}
    born_tot = 0.0
    dens = np.zeros(L)
    # state check: amplitudes for different representatives
    amps = {k: [] for k in reps}
    confs = list(itertools.combinations(range(L), n0 + 1))
    M2 = {k: 0.0 for k in reps}
    minM2 = 0.0
    maxM2 = 0.0
    min_b = 1e9
    for conf in confs:
        idx = list(conf)
        S = sea_t[idx, :]
        wts = {}
        base_amp = None
        for name, v in reps.items():
            A = np.concatenate([v[idx][:, None], S], axis=1)
            dt_ = np.linalg.det(A)
            amps[name].append(dt_)
            Ai = np.linalg.inv(A) if abs(dt_) > 1e-13 else None
            if Ai is None:
                wts[name] = None
                continue
            t = A[:, 0] * Ai[0, :]
            w = np.abs(t) ** 2
            wts[name] = w / w.sum()
            if name.startswith("canonical"):
                min_b = min(min_b, np.min(np.abs(Ai[0, :])))
        a = amps["canonical (orthogonal to sea)"][-1]
        B = abs(a) ** 2
        born_tot += B
        for i, xx in enumerate(idx):
            dens[xx] += B
        dd = d[idx] ** 2
        if B > 0 and wts["canonical (orthogonal to sea)"] is not None:
            for name in reps:
                M2[name] += B * float(np.dot(wts[name], dd))
            minM2 += B * float(dd.min())
            maxM2 += B * float(dd.max())
    for name in reps:
        out[name] = M2[name] / born_tot
    dens /= born_tot
    nsea = np.sum(np.abs(sea_t) ** 2, axis=1)
    exc = dens - nsea.sum() / L
    exc_m2 = float(np.sum(d ** 2 * exc))
    amp_dev = max(abs(np.array(amps[k]) - np.array(amps["canonical (orthogonal to sea)"])).max() for k in reps)
    return dict(per_rep=out, born_tot=born_tot, exc_m2=exc_m2, minM2=minM2 / born_tot, maxM2=maxM2 / born_tot,
                amp_dev=amp_dev, min_b=min_b, dens=dens, nsea=nsea, reps=reps, sea_t=sea_t)


L, n0, tt = 12, 6, 3.0
extra = {"canonical + 10*(sea orbital 0)": {0: 10.0}, "canonical + 10*(sea orbital 5)": {5: 10.0},
         "canonical - 3*(sea orbital 2)": {2: -3.0},
         "canonical + 100*(sea orbital 3)": {3: 100.0}, "canonical + 100*(sea orbital 1) - 100*(sea orbital 4)": {1: 100.0, 4: -100.0}}
R = ring_ensemble(L, n0, tt, extra, "ring12")
rec(abs(R["born_tot"] - (1 - n0 / L)) < 1e-12,
    "C7a ring L=12 antiperiodic closed shell (no zero modes): total Born weight = 1 - N0/L = %.12f" % R["born_tot"])
rec(R["amp_dev"] < 1e-11, "C7b all representatives give the same amplitudes on all 792 configurations (max dev %.1e)" % R["amp_dev"])
print("INFO per-representative Born-averaged second moment of the Laplace carrier's displacement about the origin (exact enumeration):")
for k, v in R["per_rep"].items():
    print("INFO   %-36s <d^2>_carrier = %.4f" % (k, v))
print("INFO   excess-density second moment <d^2>_excess = %.4f   (extreme assignments: min %.4f, max %.4f)" %
      (R["exc_m2"], R["minM2"], R["maxM2"]))
vals = list(R["per_rep"].values())
span = max(vals) - min(vals)
rec(span > 1.0 and R["minM2"] < min(vals) and R["maxM2"] > max(vals),
    "C7c same state, same Bell-sampled ensemble: carrier <d^2> over the tested representatives spans [%.3f, %.3f]; the "
    "per-configuration extremes are %.3f and %.3f" % (min(vals), max(vals), R["minM2"], R["maxM2"]))
# unnormalised Born-ensemble identity on the ring: sum_conf |Psi|^2 sum_i |t_i|^2 [x_i = x] = |phi(x)|^2 (1 - n_sea(x))
phi = R["reps"]["plain e_0"]
Ldat = L
conf_all = list(itertools.combinations(range(L), n0 + 1))
S = R["sea_t"]
acc = np.zeros(L)
for conf in conf_all:
    idx = list(conf)
    A = np.concatenate([phi[idx][:, None], S[idx, :]], axis=1)
    for i, xx in enumerate(idx):
        sub = np.delete(np.delete(A, i, axis=0), 0, axis=1)
        acc[xx] += abs(A[i, 0] * np.linalg.det(sub)) ** 2
pred = np.abs(phi) ** 2 * (1 - R["nsea"])
rec(np.max(np.abs(acc - pred)) < 1e-12,
    "C7d ring: sum_conf |A_i0 M_i0|^2 = |phi(x)|^2 (1 - n_sea(x)) for the plain-e_0 representative (max dev %.1e)" %
    np.max(np.abs(acc - pred)))

# high-precision spot check of the invariances on the physical ring (mpmath 50 digits)
Lm, n0m = 12, 6
ksm = [(2 * m + 1) * mp.pi / Lm for m in range(Lm)]
Em = [-2 * mp.cos(k) for k in ksm]
order = sorted(range(Lm), key=lambda m: Em[m])
sea_m = order[:n0m]
conf = [0, 1, 3, 4, 7, 9, 10]
tm = mp.mpf(3)


def orb(m, x):
    return mp.e ** (1j * ksm[m] * x) / mp.sqrt(Lm)


def sea_col(m, x):
    return orb(m, x) * mp.e ** (-1j * Em[m] * tm)


def phi_col(x):
    return sum(orb(m, x) * mp.conj(orb(m, 0)) * mp.e ** (-1j * Em[m] * tm) for m in range(Lm))


Am = mp.matrix(7, 7)
for r, x in enumerate(conf):
    Am[r, 0] = phi_col(x)
    for c, m in enumerate(sea_m):
        Am[r, c + 1] = sea_col(m, x)
Ami = Am ** -1
tm_ = [Am[i, 0] * Ami[0, i] for i in range(7)]
Am2 = Am.copy()
for r, x in enumerate(conf):
    Am2[r, 0] = Am[r, 0] + 10 * Am[r, 1] - 3 * Am[r, 4]
tm2 = [Am2[i, 0] * (Am2 ** -1)[0, i] for i in range(7)]
cond = abs(sum(tm_) - 1) < mp.mpf(10) ** -40 and abs(sum(tm2) - 1) < mp.mpf(10) ** -40 and \
    abs(mp.det(Am) - mp.det(Am2)) < mp.mpf(10) ** -40 and max(abs(tm_[i] - tm2[i]) for i in range(7)) > mp.mpf(10) ** -3
rec(cond, "C7e mpmath(50 digits) physical ring L=12, one configuration: det and sum t invariant to 1e-40, t itself moves by >1e-3 under col0 += 10 col1 - 3 col4")

# ---------------------------------------------------------------- C8: antiperiodic L=10 note (context only; not the pointer obligation)
k10 = [(2 * m + 1) * mp.pi / 10 for m in range(10)]
zero10 = [m for m in range(10) if abs(mp.cos(k10[m])) < mp.mpf(10) ** -40]
rec(len(zero10) == 2, "C8 (context) antiperiodic ring L=10 has exactly 2 one-body zero modes (m=%s); L=12 has none -- the ring "
                       "sizes used in C7 are non-degenerate at half filling" % zero10)

tot_pass = sum(RESULTS)
tot_fail = len(RESULTS) - tot_pass
print("TOTAL: PASS=%d FAIL=%d" % (tot_pass, tot_fail))
print("INFO runtime %.1f s" % (time.time() - T0))
if tot_fail == 0:
    print("HIT: for a fixed Slater state and sea, the Laplace carrier assignment over equivalent representatives of the added orbital "
          "realizes EVERY weight vector on the occupied sites that sums to 1 (support = nonzero dual entries), so it carries no "
          "information beyond the state; the 'canonical' choice depends on an inner product.")
print("SUMMARY: exact-arithmetic proof-checks that the Laplace/Slater-column carrier weights t_i (sum t_i = 1) are invariant only "
      "under the Levi group (column scaling, sea-GL), and under adding sea orbitals to the added column (same state, same amplitudes) "
      "they sweep the whole hyperplane sum t = 1, so any carrier distribution on the occupied sites (including 'site j carries it') is "
      "realized by some representative; the orthogonal 'canonical' choice depends on the inner product.")
sys.exit(0 if tot_fail == 0 else 1)
