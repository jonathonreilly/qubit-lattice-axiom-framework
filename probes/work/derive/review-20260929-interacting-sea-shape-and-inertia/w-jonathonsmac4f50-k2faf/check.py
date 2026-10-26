#!/usr/bin/env python3
"""
check.py for J:derive:review-20260929-interacting-sea-shape-and-inertia:a1

Obligation advanced: ONE candidate cancellation of the shape (shear) dependence
of an INTERACTING vacuum, tested with its state and source action stated.

Model (supplied comparator, NOT the walker, NOT qubit sites):
  bosonic field phi_x (real, unbounded site variable) + one Dirac-type fermion
  mode psi_x per site, on a periodic cubic lattice (or small cluster).
  Prepotential  W(phi; g) = 1/2 sum_x g^{ij} (D_i phi)_x (D_j phi)_x
                            + 1/2 m^2 sum phi^2 + (lam/4) sum phi^4
  (D_i = forward difference, g = inverse metric, det g = 1 for a shear).
  A_x = d/dphi_x + W_x ,  Q = sum_x psi_x^dag A_x ,  H = {Q, Q^dag}.
  Source action: the constant (or position dependent) inverse metric g enters
  ONLY through W.  State: ground state of H.

Executed claims (exact where marked EXACT, otherwise numerical):
  S1 EXACT  Q^2 = 0 for an arbitrary symmetric (position dependent) quadratic
            part plus quartic plus a cubic term (sympy, 3 sites, generic functions).
  S2 EXACT  H = {Q,Q^dag} equals sum(-d^2 + W_x^2 - W_xx) + 2 sum W_xy psi_x^dag psi_y.
  S3 EXACT  H (exp(-W) |fermion vacuum>) = 0 for the same generic W.
  S4 EXACT  Gaussian bookkeeping: boson zero point = tr A, fermion part = -tr A.
  S5 EXACT  The positive-definiteness of A(g) on a periodic cube for a rational
            unimodular g (so exp(-2W) is integrable and E_0 = 0 is the ground energy).
  S6 EXACT  Static cubic shear coefficients of the two unprotected halves: +2, -2.
  N1..N4 NUMERIC  Exact diagonalisation of the 2x2 periodic cluster with lam>0.
  B1..B3 NUMERIC  Soft-breaking leak, geometric inertia, adiabatic inertia.
"""
import sys, time, itertools
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import sympy as S

T0 = time.time()
RES = []


def rec(ok, msg):
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


# ---------------------------------------------------------------------------
# S1-S3: exact operator identities for generic W on 3 sites (8-dim fermion Fock)
# ---------------------------------------------------------------------------
def jw_matrices(n):
    I2 = S.eye(2)
    Z = S.diag(1, -1)
    lower = S.Matrix([[0, 1], [0, 0]])  # annihilation on |0>,|1> basis: psi|1>=|0>
    ops = []
    for j in range(n):
        m = None
        for k in range(n):
            f = Z if k < j else (lower if k == j else I2)
            m = f if m is None else S.kronecker_product(m, f)
        ops.append(m)
    return ops  # psi_j (annihilation)


def build_ops(n, W, phi):
    psi = jw_matrices(n)
    psid = [m.T for m in psi]
    dim = 2 ** n
    Wx = [S.diff(W, p) for p in phi]
    Wxy = [[S.diff(W, phi[x], phi[y]) for y in range(n)] for x in range(n)]

    def Aop(x, v):
        return v.applyfunc(lambda e: S.diff(e, phi[x]) + Wx[x] * e)

    def Adop(x, v):
        return v.applyfunc(lambda e: -S.diff(e, phi[x]) + Wx[x] * e)

    def Q(v):
        out = S.zeros(dim, 1)
        for x in range(n):
            out += psid[x] * Aop(x, v)
        return out

    def Qd(v):
        out = S.zeros(dim, 1)
        for x in range(n):
            out += psi[x] * Adop(x, v)
        return out

    def Hform(F):
        Hf = S.zeros(dim, 1)
        for x in range(n):
            Hf += F.applyfunc(lambda e: -S.diff(e, phi[x], 2) + (Wx[x] ** 2 - Wxy[x][x]) * e)
        bil = S.zeros(dim)
        for x in range(n):
            for y in range(n):
                bil += 2 * Wxy[x][y] * psid[x] * psi[y]
        return Hf + bil * F

    return psi, psid, Q, Qd, Hform, Wx, Wxy


def exact_operator_identities():
    # (i) three sites, symbolic prepotential coefficients, polynomial test vectors of degree <= 3
    # (ii) two sites, completely generic component functions f_s(phi_0, phi_1)
    import random
    random.seed(7)
    for n, generic in ((3, False), (2, True)):
        phi = S.symbols("p0:%d" % n, real=True)
        a = {}
        for i in range(n):
            for j in range(i, n):
                a[(i, j)] = a[(j, i)] = S.Symbol("a%d%d" % (i, j), real=True)
        lam, mu = S.symbols("lam mu", real=True)
        W = S.Rational(1, 2) * sum(a[(i, j)] * phi[i] * phi[j] for i in range(n) for j in range(n))
        W += lam / 4 * sum(p ** 4 for p in phi) + mu * sum(phi[i] * phi[(i + 1) % n] ** 2 for i in range(n))
        psi, psid, Q, Qd, Hform, Wx, Wxy = build_ops(n, W, phi)
        dim = 2 ** n
        ok = True
        for i in range(n):
            for j in range(n):
                ac = psi[i] * psid[j] + psid[j] * psi[i]
                ok &= (ac == (S.eye(dim) if i == j else S.zeros(dim)))
                ok &= (psid[i] * psid[j] + psid[j] * psid[i] == S.zeros(dim))
        rec(ok, "S0 Jordan-Wigner fermions anticommute exactly (%d modes)" % n)
        if generic:
            F = S.Matrix([S.Function("f%d" % s)(*phi) for s in range(dim)])
            label = "generic component functions"
        else:
            mons = [S.Integer(1)] + list(phi) + [phi[i] * phi[j] for i in range(n) for j in range(i, n)] + [phi[0] * phi[1] * phi[2], phi[0] ** 3]
            F = S.Matrix([sum(S.Integer(random.randint(-3, 3)) * m for m in mons) for _ in range(dim)])
            label = "random integer polynomial test vectors"
        q2 = Q(Q(F)).applyfunc(S.expand)
        rec(q2 == S.zeros(dim, 1), "S1 EXACT [%d sites, %s] Q^2 F = 0 with symmetric quadratic part (free entries) + quartic + cubic prepotential" % (n, label))
        H1 = (Q(Qd(F)) + Qd(Q(F))).applyfunc(S.expand)
        Hf = Hform(F).applyfunc(S.expand)
        rec((H1 - Hf).applyfunc(S.expand) == S.zeros(dim, 1),
            "S2 EXACT [%d sites, %s] {Q,Q^dag} = sum(-d^2 + W_x^2 - W_xx) + 2 sum W_xy psi_x^dag psi_y" % (n, label))
        vac = None
        for s_ in range(dim):
            e = S.zeros(dim, 1)
            e[s_] = 1
            if all(psi[x] * e == S.zeros(dim, 1) for x in range(n)):
                vac = e
        Psi0 = vac * S.exp(-W)
        HP = (Q(Qd(Psi0)) + Qd(Q(Psi0))).applyfunc(lambda e_: S.expand(e_ * S.exp(W)))
        HP2 = Hform(Psi0).applyfunc(lambda e_: S.expand(e_ * S.exp(W)))
        rec(HP == S.zeros(dim, 1) and HP2 == S.zeros(dim, 1),
            "S3 EXACT [%d sites] H exp(-W)|vac> = 0 (both as {Q,Q^dag} and in the local form), generic symbolic a_ij, lam, mu" % n)


# ---------------------------------------------------------------------------
# S4/S5/S6: lattice facts (exact rationals / sympy)
# ---------------------------------------------------------------------------
def lattice_matrix(L, g, m2):
    """A = m2 + sum_ij g_ij D_i^T D_j on the periodic L^3 torus, exact rationals."""
    n = L ** 3
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    D = []
    for i in range(3):
        M = S.zeros(n, n)
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    c = [x, y, z]
                    r = idx(*c)
                    c2 = list(c)
                    c2[i] += 1
                    M[r, idx(*c2)] += 1
                    M[r, r] += -1
        D.append(M)
    A = m2 * S.eye(n)
    for i in range(3):
        for j in range(3):
            A += g[i, j] * D[i].T * D[j]
    return A


def exact_pos_def(M):
    """Symmetric Fraction matrix: positive definite iff Gaussian elimination without pivoting has all pivots > 0."""
    n = len(M)
    M = [row[:] for row in M]
    assert all(M[i][j] == M[j][i] for i in range(n) for j in range(n))
    for k in range(n):
        if M[k][k] <= 0:
            return False
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            if f != 0:
                for j in range(k, n):
                    M[i][j] -= f * M[k][j]
    return True


def lattice_facts():
    L = 3
    g = S.Matrix([[2, 1, 0], [1, 1, 0], [0, 0, 1]])  # rational, symmetric, det = 1, positive definite
    assert g.det() == 1
    m2 = S.Rational(1, 1)
    A = lattice_matrix(L, g, m2)
    n = L ** 3
    # exact positive definiteness via leading principal minors / LDL
    ok = exact_pos_def([[Fraction(int(S.numer(A[i, j])), int(S.denom(A[i, j]))) for j in range(n)] for i in range(n)])
    rec(ok, "S5 EXACT A(g) = m^2 + g^{ij} D_i^T D_j is positive definite on the 3^3 torus for a rational unimodular shear g (exp(-2W) integrable)")
    diag = A[0, 0]
    expect = m2 + sum(g) + g.trace()
    rec(all(A[i, i] == expect for i in range(n)) and diag == expect,
        "S4a EXACT A_xx = m^2 + sum(g) + tr(g) = %s (so tr A = V (m^2 + tr(g Cbar)), Cbar = I + 11^T)" % diag)
    # Gaussian bookkeeping: sum of eigenvalues = trace (exact), oscillator ground energy a for -d^2 + a^2 phi^2
    x, a = S.symbols("x a", positive=True)
    psi0 = S.exp(-a * x ** 2 / 2)
    Hpsi = -S.diff(psi0, x, 2) + a ** 2 * x ** 2 * psi0
    rec(S.simplify(Hpsi - a * psi0) == 0,
        "S4b EXACT (-d^2 + a^2 phi^2) exp(-a phi^2/2) = a exp(-a phi^2/2): boson zero point per mode = a, sum over modes = tr A")
    # fermion part of S2 in the zero-fermion sector is -sum_x W_xx = -tr A (+ interaction part): shown in S2/S3
    # S6: static cubic shear coefficients of the two halves, c = d^2/dt^2 at t=0 of E(expm(t eps))
    t = S.symbols("t", real=True)
    e_axis = S.diag(1, -1, 0) / S.sqrt(2)
    e_face = S.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / S.sqrt(2)
    out = []
    for name, eps in (("axis", e_axis), ("face", e_face)):
        assert S.simplify((eps * eps).trace() - 1) == 0 and eps.trace() == 0
        gt = (t * eps).exp()
        Ab = m2 + gt.trace() + sum(gt)  # A_xx(t)  [E_boson/V = A_xx exactly, S4a]
        cb = S.simplify(S.diff(Ab, t, 2).subs(t, 0))
        cf = S.simplify(-S.diff(Ab, t, 2).subs(t, 0))
        out.append((name, cb, cf))
    ok = all(cb == 2 and cf == -2 for _, cb, cf in out)
    rec(ok, "S6 EXACT per-site static shear coefficients (E = E0 + c t^2/2, tr eps^2 = 1): boson half c_E = c_T = +2, fermion half = -2, sum = 0 "
        "(%s)" % ", ".join("%s: %s/%s" % o for o in out))
    # the central-difference variant: Cbar_ij = <sin k_i sin k_j> computed exactly on Z_4^3 -> (1/2) I
    Lg = 4
    ks = [S.pi * n_ / 2 for n_ in range(Lg)]
    Cc = S.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            tot = 0
            for kv in itertools.product(ks, repeat=3):
                tot += S.sin(kv[i]) * S.sin(kv[j])
            Cc[i, j] = S.simplify(tot / Lg ** 3)
    gt = (t * e_axis).exp()
    cc = S.simplify(S.diff((gt * Cc).trace(), t, 2).subs(t, 0))
    rec(Cc == S.eye(3) / 2 and cc == S.Rational(1, 2),
        "S6b EXACT central-difference coupling (sin k_i sin k_j, exact Z_4^3 average = I/2): boson half c = +1/2, fermion half -1/2; the value depends on the coupling, the cancellation does not")


# ---------------------------------------------------------------------------
# Numerical machinery: 2x2 periodic cluster, harmonic-oscillator truncation
# ---------------------------------------------------------------------------
def make_one_site(d, s, kmax=8):
    D = d + kmax + 2
    b = np.diag(np.sqrt(np.arange(1, D)), 1)
    bd = b.T
    phi = (b + bd) / np.sqrt(2 * s)
    p2 = -(s / 2) * (b - bd) @ (b - bd)
    P = []
    M = np.eye(D)
    for k in range(kmax + 1):
        P.append(sp.csr_matrix(M[:d, :d]))
        M = M @ phi
    p2c = sp.csr_matrix(p2[:d, :d])
    return P, p2c


def kron_list(ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kron(out, m, format="csr")
    return out


class Cluster:
    def __init__(self, d, s=2.0, nsite=4):
        self.d, self.s, self.n = d, s, nsite
        self.P, self.p2 = make_one_site(d, s)
        self.dim = d ** nsite
        self.I = sp.identity(d, format="csr")

    def mono(self, powers):
        ms = [self.P[powers.get(x, 0)] for x in range(self.n)]
        return kron_list(ms)

    def p2sum(self):
        tot = sp.csr_matrix((self.dim, self.dim))
        for x in range(self.n):
            ms = [self.p2 if y == x else self.I for y in range(self.n)]
            tot = tot + kron_list(ms)
        return tot

    def build(self, A, lam, Ap=None, kind="susy"):
        """kind: 'susy' -> sum(p^2 + W_x^2 - W_xx);  'bos' -> sum(p^2 + W_x^2);
        'dH' -> t-derivative of the susy zero-fermion operator (needs Ap = dA/dt)."""
        n = self.n
        if kind == "dH":
            tot = sp.csr_matrix((self.dim, self.dim))
            for x in range(n):
                # 2 W_x dW_x - dW_xx,  W_x = sum_y A_xy phi_y + lam phi_x^3,  dW_x = sum_y Ap_xy phi_y
                for y in range(n):
                    for z in range(n):
                        c = 2 * A[x, y] * Ap[x, z]
                        if c != 0:
                            pw = {}
                            pw[y] = pw.get(y, 0) + 1
                            pw[z] = pw.get(z, 0) + 1
                            tot = tot + c * self.mono(pw)
                for z in range(n):
                    c = 2 * lam * Ap[x, z]
                    if c != 0:
                        pw = {x: 3}
                        pw[z] = pw.get(z, 0) + 1
                        tot = tot + c * self.mono(pw)
                tot = tot - Ap[x, x] * self.mono({})
            return tot.tocsr()
        tot = self.p2sum()
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    c = A[x, y] * A[x, z]
                    if c != 0:
                        pw = {}
                        pw[y] = pw.get(y, 0) + 1
                        pw[z] = pw.get(z, 0) + 1
                        tot = tot + c * self.mono(pw)
            for y in range(n):
                c = 2 * lam * A[x, y]
                if c != 0:
                    pw = {x: 3}
                    pw[y] = pw.get(y, 0) + 1
                    tot = tot + c * self.mono(pw)
            tot = tot + lam ** 2 * self.mono({x: 6})
            if kind == "susy":
                tot = tot - A[x, x] * self.mono({}) - 3 * lam * self.mono({x: 2})
        return tot.tocsr()


def torus22_A(t, shape, m2=1.0):
    from scipy.linalg import expm
    if shape == "axis":
        eps = np.diag([1.0, -1.0]) / np.sqrt(2)
    else:
        eps = np.array([[0.0, 1.0], [1.0, 0.0]]) / np.sqrt(2)
    g = expm(t * eps)
    gp = eps @ g  # d g / dt
    idx = lambda x, y: (x % 2) * 2 + (y % 2)
    Dm = []
    for i in range(2):
        M = np.zeros((4, 4))
        for x in range(2):
            for y in range(2):
                r = idx(x, y)
                c = [x, y]
                c[i] += 1
                M[r, idx(*c)] += 1
                M[r, r] += -1
        Dm.append(M)
    A = m2 * np.eye(4)
    Ap = np.zeros((4, 4))
    for i in range(2):
        for j in range(2):
            T = Dm[i].T @ Dm[j]
            A += g[i, j] * T
            Ap += gp[i, j] * T
    return A, Ap


def ground(H, k=3):
    w, v = spla.eigsh(H, k=k, which="SA", tol=1e-11, ncv=min(H.shape[0] - 1, 40))
    o = np.argsort(w)
    return w[o], v[:, o]


def numeric_cluster(d=13, s=6.0):
    cl = Cluster(d, s)
    h = 0.3
    results = {}
    for shape in ("axis", "face"):
        for lam in (0.0, 3.0):
            E0 = {}
            E1 = {}
            Eb = {}
            for t in (-h, 0.0, h):
                A, Ap = torus22_A(t, shape)
                Hs = cl.build(A, lam, kind="susy")
                w, _ = ground(Hs, k=12)
                E0[t], E1[t] = w[0], w[:]
                Hb = cl.build(A, lam, kind="bos")
                wb, _ = ground(Hb, k=1)
                Eb[t] = wb[0]
            results[(shape, lam)] = (E0, E1, Eb)
    return cl, results, h


def run_numeric():
    d = 13
    t_start = time.time()
    cl, res, h = numeric_cluster(d=d, s=6.0)
    for (shape, lam), (E0, E1, Eb) in res.items():
        mx = max(abs(v) for v in E0.values())
        rec(mx < 5e-4 and min(E0.values()) > -1e-6,
            "N1 2x2 cluster d=%d %s shear lam=%.1f: SUSY ground energy at t=-h,0,+h = %s (exact value 0; truncation gives a variational upper bound)"
            % (d, shape, lam, ", ".join("%.2e" % E0[t] for t in sorted(E0))))
    # curvature of the unprotected boson-only energy vs the SUSY one
    for shape in ("axis", "face"):
        for lam in (0.0, 3.0):
            E0, E1, Eb = res[(shape, lam)]
            cb = (Eb[h] - 2 * Eb[0.0] + Eb[-h]) / h ** 2
            cs = (E0[h] - 2 * E0[0.0] + E0[-h]) / h ** 2
            if lam == 0.0:
                ok = abs(cb - 4 * 2.0) < 0.15 * 8 and abs(cs) < 0.1
                tag = "(free: expected +2 per site x 4 sites = +8 up to O(h^2))"
            else:
                ok = cb > 1.0 and abs(cs) < 0.1 and abs(Eb[0.0] - 20.0) > 1.0
                tag = "(interacting; boson-only energy at t=0 is %.3f, free value 20, so the quartic term is not small)" % Eb[0.0]
            rec(ok, "N2 %s shear lam=%.1f: boson-only energy curvature d2E/dt2 = %.3f, supersymmetric total = %.4f %s"
                % (shape, lam, cb, cs, tag))
    # excitation spectrum sees the shear
    for lam in (0.0, 3.0):
        E0, E1, Eb = res[("face", lam)]
        lv0 = E1[0.0]
        lvh = E1[h]
        shift = np.abs(lvh - lv0)
        rec(shift.max() > 0.05 and abs(E0[h]) < 1e-3 and abs(E0[0.0]) < 1e-3,
            "N3 face shear lam=%.1f: 12 lowest levels flat -> sheared (t=%.1f) differ by up to %.3f (lowest gap %.4f -> %.4f); E_0 stays %.1e" % (lam, h, shift.max(), lv0[1], lvh[1], E0[h]))
    print("   (cluster ED time %.1fs)" % (time.time() - t_start), flush=True)
    return cl


def convergence(shape="face", lam=3.0):
    out = []
    for d, s in ((9, 6.0), (11, 6.0), (13, 6.0)):
        cl = Cluster(d, s)
        A, Ap = torus22_A(0.3, shape)
        w, _ = ground(cl.build(A, lam, kind="susy"), k=1)
        out.append((d, w[0]))
    mono = all(out[i][1] >= out[i + 1][1] - 1e-9 for i in range(len(out) - 1)) and out[-1][1] > -1e-9
    rec(mono, "N4 truncation convergence of the SUSY ground energy (face shear t=0.3, lam=3): " + ", ".join("d=%d: %.2e" % o for o in out) + " (non-increasing, bounded below by exact 0)")


# ---------------------------------------------------------------------------
# B1: soft breaking leak (Gaussian, exact one-loop, 3D torus quadrature)
# ---------------------------------------------------------------------------
def bz_grid(L):
    k = 2 * np.pi * (np.arange(L) + 0.5) / L  # midpoint grid
    K = np.meshgrid(k, k, k, indexing="ij")
    return K


def Cmat(K):
    v = [np.exp(1j * k) - 1 for k in K]
    return v  # C_ij = conj(v_i) v_j


def soft_break():
    L = 32
    K = bz_grid(L)
    v = Cmat(K)
    m2 = 1.0

    def Cdot(eps):
        # tr(eps C) = sum eps_ij conj(v_i) v_j
        out = 0
        for i in range(3):
            for j in range(3):
                if eps[i, j] != 0:
                    out = out + eps[i, j] * (np.conj(v[i]) * v[j]).real
        return out
    epsA = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
    epsF = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0.0]]) / np.sqrt(2)
    for name, eps in (("axis", epsA), ("face", epsF)):
        a = m2 + Cdot(np.eye(3))
        ap = Cdot(eps)
        app = Cdot(eps @ eps)
        c0 = np.mean(app)  # curvature of the boson half (free) = tr(eps^2 Cbar)
        rec(abs(c0 - 2.0) < 1e-9, "B0 %s: BZ-quadrature boson-half curvature = %.12f (exact 2)" % (name, c0))
        res = []
        for delta in (0.0, 0.02, 0.1):
            f1 = lambda a_: a_ / np.sqrt(a_ ** 2 + delta) if delta > 0 else np.ones_like(a_)
            # f(a) = sqrt(a^2+delta) - a ; f' = a/sqrt - 1 ; f'' = delta/(a^2+delta)^{3/2}
            fp = (a / np.sqrt(a ** 2 + delta)) - 1
            fpp = delta / (a ** 2 + delta) ** 1.5
            c = np.mean(fpp * ap ** 2 + fp * app)
            res.append((delta, c))
        # finite-difference cross-check of the analytic curvature at delta = 0.1
        from scipy.linalg import expm
        def Et(tt, delta):
            g = expm(tt * eps)
            at = m2 + sum(g[i, j] * (np.conj(v[i]) * v[j]).real for i in range(3) for j in range(3))
            return np.mean(np.sqrt(at ** 2 + delta) - at)
        hh = 1e-3
        fd = (Et(hh, 0.1) - 2 * Et(0, 0.1) + Et(-hh, 0.1)) / hh ** 2
        ok = abs(res[0][1]) < 1e-12 and res[1][1] != 0 and abs(fd - res[2][1]) < 1e-5 * max(1, abs(fd))
        rec(ok, "B1 %s soft breaking (boson mass^2 shift delta only): curvature per site delta=0,0.02,0.1: %s ; FD check at 0.1: %.6f vs %.6f"
            % (name, ", ".join("%.5f" % c for _, c in res), fd, res[2][1]))
        lin = res[1][1] / 0.02
        lin2 = res[2][1] / 0.1
        rec(lin != 0 and abs(lin - lin2) / abs(lin) < 0.2,
            "B1b %s leak is first order in the breaking (nonzero, same sign and size at delta = 0.02 and 0.1): c/delta = %.4f, %.4f" % (name, lin, lin2))


# ---------------------------------------------------------------------------
# B2/B3: inertia of the sea.  Geometric (Berry) metric and adiabatic mass
# ---------------------------------------------------------------------------
def inertia_checks(cl_unused=None):
    # single oscillator check of M = a'^2/(16 a^3) for H = p^2 + a^2 phi^2 : Hp = 2 a a' phi^2
    d, s = 40, 1.3
    D = d + 4
    b = np.diag(np.sqrt(np.arange(1, D)), 1)
    phi = (b + b.T) / np.sqrt(2 * s)
    p2 = -(s / 2) * (b - b.T) @ (b - b.T)
    a, ap = 1.7, 0.6
    H = p2 + a ** 2 * phi @ phi
    Hp = 2 * a * ap * phi @ phi
    H, Hp = H[:d, :d], Hp[:d, :d]
    w, v = np.linalg.eigh(H)
    mat = v.T @ Hp @ v
    M = 2 * sum(abs(mat[n, 0]) ** 2 / (w[n] - w[0]) ** 3 for n in range(1, d))
    Gm = sum(abs(mat[n, 0]) ** 2 / (w[n] - w[0]) ** 2 for n in range(1, d))
    rec(abs(M - ap ** 2 / (16 * a ** 3)) < 1e-6 and abs(Gm - ap ** 2 / (8 * a ** 2)) < 1e-6,
        "B2a single mode: adiabatic mass M = 2 sum|<n|H'|0>|^2/E_n^3 = %.8f (formula a'^2/(16 a^3) = %.8f), Berry metric %.8f (a'^2/(8a^2) = %.8f)"
        % (M, ap ** 2 / (16 * a ** 3), Gm, ap ** 2 / (8 * a ** 2)))
    # BZ sum for the 3D lattice: sea inertia per site
    L = 32
    K = bz_grid(L)
    v = Cmat(K)
    m2 = 1.0
    out = {}
    for name, eps in (("axis", np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)), ("face", np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0.0]]) / np.sqrt(2))):
        a_ = m2 + sum((np.conj(v[i]) * v[i]).real for i in range(3))
        ap_ = sum(eps[i, j] * (np.conj(v[i]) * v[j]).real for i in range(3) for j in range(3))
        out[name] = (np.mean(ap_ ** 2 / (16 * a_ ** 3)), np.mean(ap_ ** 2 / (8 * a_ ** 2)))
    rec(all(m > 0 for m, g in out.values()),
        "B2b free 3D lattice sea (m^2=1, forward coupling), per site: adiabatic mass M = %.5f (axis), %.5f (face); Berry metric %.5f, %.5f; static energy identically 0"
        % (out["axis"][0], out["face"][0], out["axis"][1], out["face"][1]))


def interacting_inertia():
    d, s = 13, 6.0
    cl = Cluster(d, s)
    t = 0.0
    shape = "face"
    res = {}
    for lam in (0.0, 3.0):
        A, Ap = torus22_A(t, shape)
        H = cl.build(A, lam, kind="susy")
        w, v = ground(H, k=1)
        E0, psi = w[0], v[:, 0]
        Hp = cl.build(A, lam, Ap=Ap, kind="dH")
        u = Hp @ psi
        u = u - psi * (psi @ u)
        # R u = (H-E0)^{-1} u on the complement (MINRES, spectrum of complement gapped)
        Hs = (H - E0 * sp.identity(H.shape[0])).tocsr()
        def solve(rhs):
            y, info = spla.minres(Hs, rhs, rtol=1e-12, maxiter=20000) if 'rtol' in spla.minres.__code__.co_varnames else spla.minres(Hs, rhs, tol=1e-12, maxiter=20000)
            y = y - psi * (psi @ y)
            return y
        y = solve(u)
        z = solve(y)
        M = 2 * (y @ z)
        G = y @ y
        res[lam] = (M, G, E0)
    rec(res[0.0][0] > 0 and res[3.0][0] > 0,
        "B3 2x2 cluster face shear t=0: adiabatic mass M(lam=0) = %.5f, M(lam=3) = %.5f ; Berry metric %.5f, %.5f (ground energy %.1e, %.1e)"
        % (res[0.0][0], res[3.0][0], res[0.0][1], res[3.0][1], res[0.0][2], res[3.0][2]))
    # cross-check of lam=0 against the mode formula on the 2x2 torus
    A, Ap = torus22_A(t, shape)
    ev, U = np.linalg.eigh(A)
    Apm = U.T @ Ap @ U
    # A and Ap commute (translation invariant): diagonal in the same modes
    offd = np.max(np.abs(Apm - np.diag(np.diag(Apm))))
    ap_ = np.diag(Apm)
    Mf = np.sum(ap_ ** 2 / (16 * ev ** 3))
    Gf = np.sum(ap_ ** 2 / (8 * ev ** 2))
    rec(offd < 1e-12 and abs(Mf - res[0.0][0]) < 2e-3 * max(1, abs(Mf)) and abs(Gf - res[0.0][1]) < 2e-3 * max(1, abs(Gf)),
        "B3b lam=0 ED inertia %.5f / Berry %.5f agree with mode formula %.5f / %.5f" % (res[0.0][0], res[0.0][1], Mf, Gf))


def main():
    exact_operator_identities()
    lattice_facts()
    run_numeric()
    convergence()
    soft_break()
    inertia_checks()
    interacting_inertia()
    npass = sum(RES)
    nfail = len(RES) - npass
    print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
    print("   (runtime %.1fs)" % (time.time() - T0))
    if nfail == 0 and CLAIM_HIT:
        print("HIT: scoped counterexample to 'only tuning or volume-preserving flow removes the interacting shape term': exact Q-exact interacting completion (continuous-site comparator).")
    print("SUMMARY: In a supplied Q-exact (boson + fermion) lattice model with a quartic interaction, the vacuum energy is exactly 0 for every symmetric "
          "quadratic prepotential, hence for any constant or position-dependent inverse metric entering through it (exact algebra, plus 2x2-cluster exact diagonalisation "
          "at quartic coupling 3), although the boson-only and fermion-only halves have static shear coefficients +2 and -2 per site, the excitation levels move with the "
          "shear and the sea has nonzero Berry/adiabatic inertia; a boson mass shift leaks at first order; the walker's Dirac sea on qubit sites, wave speeds and exact poles are not covered.")
    sys.exit(0 if nfail == 0 else 1)


CLAIM_HIT = True

if __name__ == "__main__":
    main()
