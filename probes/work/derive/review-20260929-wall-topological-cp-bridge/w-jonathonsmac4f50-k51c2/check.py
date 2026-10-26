#!/usr/bin/env python3
"""review-20260929-wall-topological-cp-bridge : check.py

Model (SUPPLIED by the lane, not by the axioms): 2D even-L periodic staggered
fermion with unitary links, eps = (-1)^(x1+x2), taste-singlet Hermitian
grading Gamma_f = i eta_2 (C1 C2 + C2 C1)/2 (the 2026-07-02 supplier operator),
mass operator  M(m, m5) = D + m + i m5 Gamma  (m > 0, m5 real).

Part E  : EXACT arithmetic over Q(i) (own Gaussian-rational class, Fractions),
          Z_4 link configurations on the 4x4 torus.  Total flux is an exact
          integer there (sum of principal plaquette angles = 2 pi Q).
Part F  : double precision numpy on the uniform-flux U(1) family (CHECKED, not
          exact); every claim is also stated as a proof in ATTEMPT.md.
Only numpy/scipy/sympy/mpmath/fractions are used.  Own machinery throughout.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
RESULTS = []
NCASES = [0]


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (" :: " + detail if detail else ""))


# ----------------------------------------------------------------------------
# Part E machinery: exact Gaussian rationals and dense matrices over Q(i)
# ----------------------------------------------------------------------------
class GQ:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(s, o):
        return GQ(s.re + o.re, s.im + o.im)

    def __sub__(s, o):
        return GQ(s.re - o.re, s.im - o.im)

    def __neg__(s):
        return GQ(-s.re, -s.im)

    def __mul__(s, o):
        return GQ(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    def conj(s):
        return GQ(s.re, -s.im)

    def inv(s):
        n = s.re * s.re + s.im * s.im
        return GQ(s.re / n, -s.im / n)

    def iszero(s):
        return s.re == 0 and s.im == 0

    def __eq__(s, o):
        return s.re == o.re and s.im == o.im

    def __repr__(s):
        return "(%s%+si)" % (s.re, s.im)


ZERO = GQ(0, 0)
ONE = GQ(1, 0)
I_ = GQ(0, 1)


def mzeros(n, m=None):
    m = n if m is None else m
    return [[GQ() for _ in range(m)] for _ in range(n)]


def meye(n):
    A = mzeros(n)
    for i in range(n):
        A[i][i] = GQ(1, 0)
    return A


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = mzeros(n, m)
    for i in range(n):
        Ai = A[i]
        for l in range(k):
            a = Ai[l]
            if a.iszero():
                continue
            Bl = B[l]
            for j in range(m):
                b = Bl[j]
                if not b.iszero():
                    C[i][j] = C[i][j] + a * b
    return C


def mdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mconj(A):
    return [[a.conj() for a in row] for row in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def miszero(A):
    return all(a.iszero() for row in A for a in row)


def mtrace(A):
    t = GQ()
    for i in range(len(A)):
        t = t + A[i][i]
    return t


def mdet(A):
    n = len(A)
    M = [row[:] for row in A]
    det = GQ(1, 0)
    for c in range(n):
        p = None
        for r in range(c, n):
            if not M[r][c].iszero():
                p = r
                break
        if p is None:
            return GQ()
        if p != c:
            M[c], M[p] = M[p], M[c]
            det = -det
        piv = M[c][c]
        det = det * piv
        pinv = piv.inv()
        for r in range(c + 1, n):
            if M[r][c].iszero():
                continue
            f = M[r][c] * pinv
            for j in range(c, n):
                M[r][j] = M[r][j] - f * M[c][j]
    return det


def minv(A):
    n = len(A)
    M = [A[i][:] + meye(n)[i] for i in range(n)]
    for c in range(n):
        p = None
        for r in range(c, n):
            if not M[r][c].iszero():
                p = r
                break
        if p is None:
            raise ZeroDivisionError("singular")
        M[c], M[p] = M[p], M[c]
        pinv = M[c][c].inv()
        M[c] = [x * pinv for x in M[c]]
        for r in range(n):
            if r != c and not M[r][c].iszero():
                f = M[r][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def mnullspace(A):
    """columns spanning ker A (A square, exact rref)."""
    n = len(A)
    M = [row[:] for row in A]
    piv_cols = []
    r = 0
    for c in range(n):
        p = None
        for rr in range(r, n):
            if not M[rr][c].iszero():
                p = rr
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pinv = M[r][c].inv()
        M[r] = [x * pinv for x in M[r]]
        for rr in range(n):
            if rr != r and not M[rr][c].iszero():
                f = M[rr][c]
                M[rr] = [M[rr][j] - f * M[r][j] for j in range(n)]
        piv_cols.append(c)
        r += 1
        if r == n:
            break
    free = [c for c in range(n) if c not in piv_cols]
    basis = []
    for f in free:
        v = [GQ() for _ in range(n)]
        v[f] = GQ(1, 0)
        for i, pc in enumerate(piv_cols):
            v[pc] = -M[i][f]
        basis.append(v)
    return basis


def kernel_projector(D):
    n = len(D)
    basis = mnullspace(D)
    if not basis:
        return mzeros(n), 0
    K = [[basis[j][i] for j in range(len(basis))] for i in range(n)]
    Kd = mdag(K)
    gram = mmul(Kd, K)
    P = mmul(mmul(K, minv(gram)), Kd)
    return P, len(basis)


I4 = [GQ(1, 0), GQ(0, 1), GQ(-1, 0), GQ(0, -1)]  # i^k


def z4_operators(L, k1, k2):
    """exact D, Gamma, eps for Z_4 links U_mu(x) = i^{k_mu(x)}  (L x L torus)."""
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    T1 = mzeros(N)
    T2 = mzeros(N)
    for x in range(L):
        for y in range(L):
            T1[idx(x, y)][idx(x + 1, y)] = I4[k1[x][y] % 4]
            T2[idx(x, y)][idx(x, y + 1)] = I4[k2[x][y] % 4]
    eta2 = mzeros(N)
    eps = mzeros(N)
    for x in range(L):
        for y in range(L):
            eta2[idx(x, y)][idx(x, y)] = GQ((-1) ** x, 0)
            eps[idx(x, y)][idx(x, y)] = GQ((-1) ** (x + y), 0)
    half = GQ(Fr(1, 2), 0)
    D = mscal(half, madd(msub(T1, mdag(T1)), mmul(eta2, msub(T2, mdag(T2)))))
    C1 = mscal(half, madd(T1, mdag(T1)))
    C2 = mscal(half, madd(T2, mdag(T2)))
    S = mscal(half, madd(mmul(C1, C2), mmul(C2, C1)))
    G = mscal(I_, mmul(eta2, S))
    return D, G, eps, T1, T2


def z4_flux(L, k1, k2):
    """exact integer Q: principal plaquette angles (in (-pi, pi]) sum to 2 pi Q."""
    tot = 0
    lift = {0: 0, 1: 1, 2: 2, 3: -1}  # k*pi/2 with k=2 -> +pi (principal value)
    for x in range(L):
        for y in range(L):
            k = (k1[x][y] + k2[(x + 1) % L][y] - k1[x][(y + 1) % L] - k2[x][y]) % 4
            tot += lift[k]
    assert tot % 4 == 0
    return tot // 4


def det_M(D, G, m, m5):
    n = len(D)
    M = madd(madd(D, mscal(GQ(m, 0), meye(n))), mscal(GQ(0, m5), G))
    return mdet(M)


def lagrange_deriv_at0(vals, ts):
    """exact derivative at 0 of the polynomial through (ts, vals)."""
    total = GQ()
    for j, tj in enumerate(ts):
        # l_j'(0) = sum_{k != j} prod_{i != j,k} (0 - t_i) / prod_{i != j} (t_j - t_i)
        den = Fr(1)
        for i, ti in enumerate(ts):
            if i != j:
                den *= (tj - ti)
        num = Fr(0)
        for k, tk in enumerate(ts):
            if k == j:
                continue
            term = Fr(1)
            for i, ti in enumerate(ts):
                if i != j and i != k:
                    term *= (0 - ti)
            num += term
        total = total + GQ(num / den, 0) * vals[j]
    return total


def plaq_ks(L, k1, k2):
    return [(k1[x][y] + k2[(x + 1) % L][y] - k1[x][(y + 1) % L] - k2[x][y]) % 4
            for x in range(L) for y in range(L)]


def make_configs():
    rng = np.random.default_rng(20260929)
    L = 4
    out = {}
    out["free"] = ([[0] * L for _ in range(L)], [[0] * L for _ in range(L)])
    r1 = rng.integers(0, 2, (L, L)) * 2
    r2 = rng.integers(0, 2, (L, L)) * 2
    out["Z2real"] = (r1.tolist(), r2.tolist())  # real links: contains pi plaquettes
    # admissible Z_4 configs (no plaquette angle equal to pi), Q != 0:
    # two with exact kernel, two without (selected by exact kernel computation)
    want = {"adm_ker": 2, "adm_noker": 2}
    got = {"adm_ker": [], "adm_noker": []}
    for t in range(400000):
        k1 = rng.integers(0, 4, (L, L)).tolist()
        k2 = rng.integers(0, 4, (L, L)).tolist()
        if 2 in plaq_ks(L, k1, k2):
            continue
        q = z4_flux(L, k1, k2)
        if q == 0:
            continue
        D = z4_operators(L, k1, k2)[0]
        n0 = len(mnullspace(D))
        key = "adm_ker" if n0 > 0 else "adm_noker"
        if len(got[key]) < want[key]:
            got[key].append((k1, k2))
        if all(len(got[k]) >= want[k] for k in want):
            break
    for key in want:
        for i, c in enumerate(got[key]):
            out["%s%d" % (key, i)] = c
    # non-admissible (contain pi plaquettes) configs with exact kernel
    found = 0
    for t in range(4000):
        k1 = rng.integers(0, 4, (L, L)).tolist()
        k2 = rng.integers(0, 4, (L, L)).tolist()
        if 2 not in plaq_ks(L, k1, k2):
            continue
        if z4_flux(L, k1, k2) == 0:
            continue
        D = z4_operators(L, k1, k2)[0]
        if len(mnullspace(D)) > 0:
            out["rough%d" % found] = (k1, k2)
            found += 1
        if found >= 2:
            break
    return out


# ----------------------------------------------------------------------------
# Part E : exact checks
# ----------------------------------------------------------------------------
def part_E():
    L = 4
    N = 16
    configs = make_configs()
    mval = Fr(1, 3)
    m5val = Fr(2, 5)
    info = {}
    for name, (k1, k2) in configs.items():
        D, G, eps, T1, T2 = z4_operators(L, k1, k2)
        Q = z4_flux(L, k1, k2)
        info[name] = (D, G, eps, Q)
        ok = (meq(mdag(D), mscal(GQ(-1, 0), D))
              and miszero(madd(mmul(eps, D), mmul(D, eps)))
              and meq(mdag(G), G)
              and miszero(msub(mmul(eps, G), mmul(G, eps))))
        report("E1 structure D^dag=-D, {eps,D}=0, Gamma^dag=Gamma, [eps,Gamma]=0 exact [%s, Q=%d]" % (name, Q), ok)
        tr0 = mtrace(G)
        report("E1b tr(Gamma_f)=0 exactly [%s]" % name, tr0.iszero())

    # E2 conjugation law det M(m5)^* = det M(-m5), exact
    for name, (D, G, eps, Q) in info.items():
        dp = det_M(D, G, mval, m5val)
        dm = det_M(D, G, mval, -m5val)
        report("E2 det M(m5)^* = det M(-m5) exactly [%s]" % name, dp.conj() == dm,
               "Im det = %s" % (float(dp.im),))

    # E3 charge conjugation in 2D: U -> U^*  (k -> -k): det M(U*) = conj det M(U) always;
    # Q(U*) = -Q(U) exactly when no plaquette angle equals pi (branch cut), fails on the cut.
    for name, (k1, k2) in configs.items():
        D, G, eps, Q = info[name]
        k1c = [[(-v) % 4 for v in row] for row in k1]
        k2c = [[(-v) % 4 for v in row] for row in k2]
        Dc, Gc, _, _, _ = z4_operators(L, k1c, k2c)
        Qc = z4_flux(L, k1c, k2c)
        d = det_M(D, G, mval, m5val)
        dc = det_M(Dc, Gc, mval, m5val)
        has_pi = 2 in plaq_ks(L, k1, k2)
        real_links = all(v % 2 == 0 for r in k1 for v in r) and all(v % 2 == 0 for r in k2 for v in r)
        ok = (dc == d.conj())
        if real_links:
            ok = ok and d.im == 0
        if not has_pi:
            ok = ok and (Qc == -Q)
        report("E3 2D C-law det M(U*)=conj det M(U) exactly; Q(U*)=-Q(U) iff no pi-plaquette (this config has pi: %s); "
               "real links give real det [%s]" % (has_pi, name), ok, "Q(U)=%d Q(U*)=%d" % (Q, Qc))
    k1, k2 = configs["Z2real"]
    Qz = info["Z2real"][3]
    Dz, Gz = info["Z2real"][0], info["Z2real"][1]
    report("E3b branch-cut counterexample: real-link config is C-invariant (det M real) yet principal-angle Q=%d != 0 "
           "= -Q: Q is C-odd only on the admissible (no-pi) set" % Qz,
           Qz != 0 and det_M(Dz, Gz, mval, m5val).im == 0)

    # E4 odd class: Hermitian eps-odd mass gives det > 0 exactly
    # H1 = i (T1 - T1^dag) is Hermitian and flips eps (one hop)
    for name, (k1, k2) in configs.items():
        D, G, eps, Q = info[name]
        _, _, _, T1, T2 = z4_operators(L, k1, k2)
        H1 = mscal(I_, msub(T1, mdag(T1)))
        assert meq(mdag(H1), H1)
        assert miszero(madd(mmul(eps, H1), mmul(H1, eps)))
        n = len(D)
        M = madd(madd(D, mscal(GQ(mval, 0), meye(n))), mscal(GQ(0, m5val), H1))
        d = mdet(M)
        report("E4 eps-odd Hermitian mass: det(D+m+i m5 H1) real and > 0 exactly [%s]" % name,
               d.im == 0 and d.re > 0, "det=%s" % (float(d.re),))

    # E5 first-order formulas, exact
    kernel_nonzero_seen = False
    for name, (D, G, eps, Q) in info.items():
        n = len(D)
        m = mval
        mI = mscal(GQ(m, 0), meye(n))
        Mi = minv(madd(D, mI))  # (D+m)^{-1}
        trMG = mtrace(mmul(Mi, G))
        # polynomial p(t) = det(D+m+i t Gamma), degree <= 16 : exact derivative from 17 points
        ts = [Fr(j) for j in range(n + 1)]
        vals = [det_M(D, G, m, t) for t in ts]
        p0 = vals[0]
        dp0 = lagrange_deriv_at0(vals, ts)
        lhs = dp0
        rhs = I_ * p0 * trMG
        report("E5a p'(0) = i det(D+m) Tr[(D+m)^-1 Gamma] exact [%s]" % name, lhs == rhs)
        # R = (m^2 - D^2)^{-1}
        R = minv(msub(mscal(GQ(m * m, 0), meye(n)), mmul(D, D)))
        slope = mscal(GQ(m, 0), mmul(G, R))
        s = mtrace(slope)
        report("E5b Re Tr[(D+m)^-1 Gamma] = m Tr[Gamma R], Tr[Gamma R] real, R=(m^2-D^2)^-1 [%s]" % name,
               s.im == 0 and trMG.re == s.re,
               "d(arg det)/d m5|0 = %s" % (float(s.re),))
        # E5c decomposition: m Tr[G R] = Tr[G P]/m + (m/2) Tr[{G,D} R D^+]
        P, n0 = kernel_projector(D)
        if n0:
            kernel_nonzero_seen = True
        negD2 = msub(mzeros(n), mmul(D, D))
        E = msub(minv(madd(negD2, P)), P)
        Dplus = mscal(GQ(-1, 0), mmul(D, E))
        ok_pinv = meq(mmul(D, Dplus), msub(meye(n), P))
        A = madd(mmul(G, D), mmul(D, G))
        deftr = mtrace(mmul(mmul(A, R), Dplus))
        idx_term = mtrace(mmul(G, P))
        lhs2 = s
        rhs2 = GQ(1 / m, 0) * idx_term + GQ(m / 2, 0) * deftr
        report("E5c exact split: slope = Tr(Gamma P_ker)/m + (m/2) Tr[{Gamma,D} R D+] [%s]" % name,
               ok_pinv and lhs2 == rhs2,
               "n0=%d Tr(G P)=%s defect=%s" % (n0, idx_term.re, float((GQ(m / 2, 0) * deftr).re)))
        if name == "free":
            report("E5d free field: {Gamma_f,D}=0 exactly, Tr(Gamma P)=0, slope=0 exactly",
                   miszero(A) and idx_term.iszero() and s.re == 0)
    report("E5e kernel nonzero in at least one exact config", kernel_nonzero_seen)

    # E6 exact counterexamples: dim ker D vs 2|Q|, Tr(Gamma P), real weight
    for name, (D, G, eps, Q) in info.items():
        if not (name.startswith("rough") or name.startswith("adm")):
            continue
        n = len(D)
        P, n0 = kernel_projector(D)
        trGP = mtrace(mmul(G, P)).re
        d = det_M(D, G, mval, m5val)
        A = madd(mmul(G, D), mmul(D, G))
        wrongdim = (n0 != 2 * abs(Q))
        report("E6 [%s]: Q=%d, dim ker D=%d (2|Q|=%d), Tr(Gamma P_ker)=%s, Im det M(m=1/3,m5=2/5)=%.5f, "
               "{Gamma,D}!=0:%s, tr Gamma=0"
               % (name, Q, n0, 2 * abs(Q), trGP, float(d.im), not miszero(A)),
               d.im != 0 and (not miszero(A)) and mtrace(G).iszero())
        if name.startswith("adm_noker"):
            report("E6c [%s] admissible Z_4 config with Q=%d but NO exact zero mode: Tr(Gamma P_ker)=0, so the small-m "
                   "index pole is absent while the phase is nonzero (Im det=%.5f): dim ker D = 2|Q| is not forced"
                   % (name, Q, float(d.im)), wrongdim and trGP == 0 and d.im != 0)
    # sign pattern of Im det for admissible configs: Q>0 -> Im<0, Q<0 -> Im>0 (convention of this runner)
    signs = []
    for name, (D, G, eps, Q) in info.items():
        if name.startswith("adm"):
            d = det_M(D, G, mval, m5val)
            signs.append((Q, d.im < 0))
    report("E6b admissible configs: sign(Im det M) = -sign(Q) in all %d cases (source convention: U_1,U_2 hops as in the "
           "07-02 note, plaquette U1(x)U2(x+1)U1^*(x+2)U2^*(x), mass +i m5 Gamma_f): %s" % (len(signs), signs),
           all((q > 0) == neg for q, neg in signs) and len(signs) >= 3)
    return info


# ----------------------------------------------------------------------------
# Part F : double precision numerics on uniform-flux U(1) torus (CHECKED)
# ----------------------------------------------------------------------------
def build_flux(L, Q):
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    phi = 2 * np.pi * Q / L ** 2
    T1 = np.zeros((N, N), complex)
    T2 = np.zeros((N, N), complex)
    U1 = np.ones((L, L), complex)
    U2 = np.zeros((L, L), complex)
    for x in range(L):
        for y in range(L):
            U1[x, y] = np.exp(-1j * phi * L * y) if x == L - 1 else 1.0
            U2[x, y] = np.exp(1j * phi * x)
            T1[idx(x, y), idx(x + 1, y)] = U1[x, y]
            T2[idx(x, y), idx(x, y + 1)] = U2[x, y]
    eta2 = np.diag([(-1.0) ** x for x in range(L) for y in range(L)]).astype(complex)
    eps = np.diag([(-1.0) ** (x + y) for x in range(L) for y in range(L)]).astype(complex)
    D = 0.5 * ((T1 - T1.conj().T) + eta2 @ (T2 - T2.conj().T))
    C1 = (T1 + T1.conj().T) / 2
    C2 = (T2 + T2.conj().T) / 2
    G = 1j * eta2 @ ((C1 @ C2 + C2 @ C1) / 2)
    # total principal plaquette angle
    tot = 0.0
    for x in range(L):
        for y in range(L):
            p = U1[x, y] * U2[(x + 1) % L, y] * np.conj(U1[x, (y + 1) % L]) * np.conj(U2[x, y])
            tot += np.angle(p)
    return D, G, eps, tot / (2 * np.pi)


def kernel_data(D, tol=1e-9):
    w, v = np.linalg.eigh(1j * D)
    z = np.abs(w) < tol
    nz = np.abs(w[~z])
    return w, v, z, (nz.min() if nz.size else np.inf)


def flow(D, G, eps, m):
    out = []
    for s in (+1, -1):
        H = eps @ D - s * m * G
        H = (H + H.conj().T) / 2
        out.append(int((np.linalg.eigvalsh(H) < 0).sum()))
    return out[0] - out[1]


def theorem_data(D, G):
    w, v, z, Delta = kernel_data(D)
    n0 = int(z.sum())
    if n0 == 0:
        return None
    V = v[:, z]
    GVV = V.conj().T @ G @ V
    GVV = (GVV + GVV.conj().T) / 2
    ev = np.linalg.eigvalsh(GVV)
    gam0 = np.abs(ev).min()
    sig = int((ev > 0).sum() - (ev < 0).sum())
    return n0, Delta, gam0, sig, ev.sum()


def part_F():
    # F0: reproduce the 07-02 measured anticommutator norms and flux integrality
    for (L, Q, ref) in [(8, 1, 0.480), (8, 2, 0.956), (12, 1, 0.321), (12, 2, 0.640)]:
        D, G, eps, qq = build_flux(L, Q)
        nrm = np.linalg.norm(G @ D + D @ G)
        report("F0 uniform flux L=%d Q=%d: plaquette-angle sum/2pi=%.12f, ||{Gamma,D}||_F=%.4f (07-02 note: %.3f)"
               % (L, Q, qq, nrm, ref), abs(qq - Q) < 1e-9 and abs(nrm - ref) < 1e-3)

    # F-lemma: Haynsworth inertia additivity on random Hermitian matrices
    rng = np.random.default_rng(5)
    ok = True
    for t in range(200):
        n, k = 9, 4
        X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        H = (X + X.conj().T) / 2
        A = H[k:, k:]
        B = H[:k, k:]
        Sc = H[:k, :k] - B @ np.linalg.inv(A) @ B.conj().T
        def inertia(M):
            e = np.linalg.eigvalsh((M + M.conj().T) / 2)
            return (int((e > 0).sum()), int((e < 0).sum()))
        a, s_, h = inertia(A), inertia(Sc), inertia(H)
        ok &= (h == (a[0] + s_[0], a[1] + s_[1]))
    report("F1 lemma: In(H)=In(A)+In(H/A) (Haynsworth) on 200 random Hermitian matrices", ok)

    # F2: the flow theorem  flow(m) = sig(P Gamma P|ker)  for 0 < m < gamma0*Delta/(1+gamma0)
    ncases = 0
    nfail = 0
    nvals = 0
    bad = []
    for L in (6, 8, 10, 12):
        for Q in range(-3, 4):
            D, G, eps, qq = build_flux(L, Q)
            th = theorem_data(D, G)
            if th is None:
                continue
            n0, Delta, gam0, sig, trv = th
            if gam0 < 1e-6:
                continue  # Gamma_VV singular: theorem hypothesis not met
            mmax = gam0 * Delta / (1 + gam0)
            if mmax < 2e-6:
                continue
            ncases += 1
            for frac in (0.1, 0.5, 0.95):
                m = frac * mmax
                assert m / (Delta - m) < gam0 + 1e-15
                f = flow(D, G, eps, m)
                nvals += 1
                if f != sig:
                    nfail += 1
                    bad.append((L, Q, frac, f, sig))
    NCASES[0] = ncases
    report("F2 flow theorem: flow(m)=sig(Gamma_VV) for m<gamma0*Delta/(1+gamma0) on %d (L,Q) cases, %d m-values"
           % (ncases, nvals), nfail == 0 and ncases >= 20, "failures=%s" % (bad[:3],))

    # F3: sig(Gamma_VV) = -2Q on cases with dim ker = 2|Q| (the note's tested family and more)
    rows = []
    allok = True
    for L in (8, 12):
        for Q in (-2, -1, 1, 2):
            D, G, eps, qq = build_flux(L, Q)
            n0, Delta, gam0, sig, trv = theorem_data(D, G)
            rows.append((L, Q, n0, sig, round(trv, 4)))
            allok &= (n0 == 2 * abs(Q) and sig == -2 * Q)
    report("F3 note's tested family (L=8,12; Q=+-1,+-2): dim ker D=2|Q|, sig(Gamma_VV)=-2Q, so the 07-02 flow plateau "
           "is the theorem's value", allok, str(rows))

    # F4: scope boundary: (L=8,Q=3): exact kernel is 2-dim, flow m-window
    D, G, eps, qq = build_flux(8, 3)
    n0, Delta, gam0, sig, trv = theorem_data(D, G)
    mmax = gam0 * Delta / (1 + gam0)
    f_small = flow(D, G, eps, 0.3 * mmax)
    f_mid = flow(D, G, eps, 0.05)
    f_big = flow(D, G, eps, 1.0)
    report("F4 (L=8,Q=3): dim ker=%d (not 2Q=6), smallest nonzero |lambda|=%.2e; flow=%d inside hypothesis "
           "(m=%.1e), flow=%d at m=0.05 and %d at m=1: the flux-only law holds only above a splitting scale"
           % (n0, Delta, f_small, 0.3 * mmax, f_mid, f_big),
           n0 == 2 and f_small == sig == -2 and f_mid == -6 and f_big == -6)

    # F5: first-order phase slope formula vs finite difference of arg det (double precision)
    maxerr = 0.0
    for (L, Q, m) in [(8, 1, 0.3), (8, 2, 0.05), (6, 3, 0.2), (8, 3, 0.05)]:
        D, G, eps, qq = build_flux(L, Q)
        n = D.shape[0]
        R = np.linalg.inv(m * m * np.eye(n) - D @ D)
        slope = m * np.trace(G @ R).real
        h = 1e-6
        def phase(t):
            # np.errstate: the macOS BLAS raises spurious FP flags inside slogdet even when the
            # returned (sign, logdet) is finite and correct (checked against finite cond numbers)
            with np.errstate(all="ignore"):
                sgn, _ld = np.linalg.slogdet(D + m * np.eye(n) + 1j * t * G)
            return np.angle(sgn)
        fd = (phase(h) - phase(-h)) / (2 * h)
        maxerr = max(maxerr, abs(fd - slope))
    report("F5 d(arg det M)/d m5 = m Tr[Gamma (m^2 - D^2)^-1] vs central difference, 4 cases", maxerr < 1e-6,
           "max err %.1e" % maxerr)

    # F6: finite-lattice normalisation: Tr(Gamma_VV) is not the integer sig; it is Q-nonlinear
    rows = []
    for L in (8, 12, 16, 20):
        for Q in (1, 2):
            D, G, eps, qq = build_flux(L, Q)
            n0, Delta, gam0, sig, trv = theorem_data(D, G)
            rows.append((L, Q, round(trv, 5), round((1 - abs(trv) / (2 * Q)) * L * L / (np.pi * Q), 4)))
    # test: ratio (1-|Tr|/2Q) L^2/(pi Q) within 3% of 1 for L>=12 (fit, not proof)
    fitok = all(abs(r[3] - 1) < 0.03 for r in rows if r[0] >= 12)
    nonint = all(abs(abs(r[2]) - 2 * r[1]) > 1e-3 for r in rows)
    report("F6 Tr(Gamma_VV) = -2Q(1 - pi Q/L^2 + ...) numerically, never the integer -2Q (finite L); "
           "table (L,Q,Tr,ratio): %s" % (rows,), fitok and nonint)

    # F7: combined phase at first order, small m: Phi_Q = theta Q + alpha Tr(Gamma_VV)
    D1, G1, e1, _ = build_flux(12, 1)
    D2, G2, e2, _ = build_flux(12, 2)
    t1 = theorem_data(D1, G1)[4]
    t2 = theorem_data(D2, G2)[4]
    # theta_g that cancels sector Q=1 (alpha=1): theta = -t1/1 ; residual in sector Q=2
    theta = -t1
    resid2 = theta * 2 + t2
    report("F7 one theta_g cannot cancel the phase in Q=1 and Q=2 at once on L=12: Tr1=%.5f Tr2=%.5f, "
           "residual in Q=2 after cancelling Q=1: %.2e (nonzero, = 4 pi/L^2 = %.2e within 5e-3)" % (t1, t2, resid2, 4 * np.pi / 144),
           abs(resid2 - 4 * np.pi / 144) < 5e-3 and t1 < 0 and t2 < t1)

    # F8: convention dependence of the combined phase sign
    D, G, eps, _ = build_flux(8, 1)
    Dm, Gm, em, _ = build_flux(8, -1)
    t_p = theorem_data(D, G)[4]
    t_m = theorem_data(Dm, Gm)[4]
    report("F8 sign convention: Tr(Gamma_VV)=%.5f at Q=+1, %.5f at Q=-1 (exact C-oddness in 2D); flipping the "
           "orientation of Q or the sign of m5 turns cancellation into addition" % (t_p, t_m),
           abs(t_p + t_m) < 1e-12 and t_p < 0)

    # F9: near-kernel version of the theorem (8,3): 6-dim approximate kernel
    D, G, eps, _ = build_flux(8, 3)
    w, v = np.linalg.eigh(1j * D)
    order = np.argsort(np.abs(w))
    Vidx = order[:6]
    delta = np.abs(w[Vidx]).max()
    Delta_ = np.abs(w[order[6]])
    V = v[:, Vidx]
    GVV = V.conj().T @ G @ V
    ev = np.linalg.eigvalsh((GVV + GVV.conj().T) / 2)
    gam0 = np.abs(ev).min()
    sig = int((ev > 0).sum() - (ev < 0).sum())
    ms = []
    okk = True
    for m in np.linspace(0.005, 0.2, 40):
        if delta / m + m / (Delta_ - m) < gam0 and m < Delta_:
            ms.append(m)
            okk &= (flow(D, G, eps, m) == sig)
    report("F9 near-kernel theorem (L=8,Q=3, V = 6 lowest |lambda| modes, delta=%.1e, Delta=%.3f, gamma0=%.3f, "
           "sig=%d): flow = sig on %d admissible m-values" % (delta, Delta_, gam0, sig, len(ms)),
           okk and len(ms) >= 5 and sig == -6)

    # F11: the 2|Q| lowest modes of the note's tested family are zero to roundoff (not split pairs)
    mx = 0.0
    for (L, Q) in [(8, 1), (8, 2), (12, 1), (12, 2)]:
        D_, G_, e_, _ = build_flux(L, Q)
        w_ = np.sort(np.abs(np.linalg.eigvalsh(1j * D_)))
        mx = max(mx, w_[:2 * abs(Q)].max())
    report("F11 (8,1),(8,2),(12,1),(12,2): the 2|Q| lowest |lambda| are <= %.1e (exact zeros to roundoff), "
           "not taste-split +-lambda pairs as described in 07-02 note:237" % mx, mx < 1e-12)

    # F12: exact-kernel dimension is not 2|Q| outside the tested family
    rows = []
    for (L, Q) in [(8, 3), (8, 5), (10, 3), (12, 5), (4, 3)]:
        D_, G_, e_, _ = build_flux(L, Q)
        w_, v_, z_, Dl_ = kernel_data(D_)
        rows.append((L, Q, int(z_.sum()), 2 * abs(Q)))
    report("F12 dim ker D != 2|Q| for uniform flux at (L,Q,dim ker,2|Q|) = %s" % (rows,),
           all(r[2] != r[3] for r in rows))


    # F10: order of limits m -> 0 versus fixed m for the physical slope (8,3)
    w10, v10 = np.linalg.eigh(1j * D)
    g10 = np.real(np.einsum("ik,ij,jk->k", v10.conj(), G, v10))  # g_k = <k|Gamma|k>

    def mcoef(m):  # alpha-normalised coefficient m * d arg det / d m5 = sum_k m^2 g_k / (m^2 + lambda_k^2)
        return float(np.sum(m * m * g10 / (m * m + w10 ** 2)))
    zk = np.abs(w10) < 1e-9
    tr_ker = float(g10[zk].sum())
    c_small = mcoef(1e-6)
    c_mid = mcoef(0.05)
    report("F10 (L=8,Q=3) alpha-normalised phase coefficient m*dPhi/dm5: %.5f at m=1e-6 (= Tr Gamma_ker = %.5f, 2 exact "
           "zero modes) vs %.4f at m=0.05 (6 near-kernel modes): order of limits m->0 vs L->inf matters"
           % (c_small, tr_ker, c_mid),
           abs(c_small - tr_ker) < 1e-4 and abs(tr_ker + 1.7026) < 5e-3 and c_mid < -5.0)


def main():
    part_E()
    part_F()
    n_pass = sum(RESULTS)
    n_fail = len(RESULTS) - n_pass
    print("HIT: scoped, same-family, unrefereed: (i) proved conditional inertia theorem flow(m)=sig(P Gamma_f P|ker D) for "
          "m<gamma0*Delta/(1+gamma0) (the 07-02 note's -2Q plateau was machine-verified only), with checked hypotheses on "
          "%d (L,Q) cases; (ii) exact defect identity slope = Tr(Gamma P_ker)/m + (m/2)Tr[{Gamma,D}R D+]; (iii) exact Z_4 "
          "counterexamples to dim ker D = 2|Q| and to a real weight" % NCASES[0]) if n_fail == 0 else None
    print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
    print("SUMMARY: On the actual 2D staggered/taste-singlet-mass surface, the combined phase slope equals the kernel "
          "trace of Gamma_f (non-integer, Q-nonlinear at finite L) plus an exact anticommutator defect, while the "
          "integer -2Q of the 07-02 spectral flow is the signature of the kernel compression under a proved explicit "
          "m-window; elapsed %.1fs" % (time.time() - T0))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
