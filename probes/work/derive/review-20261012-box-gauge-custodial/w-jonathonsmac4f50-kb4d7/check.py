#!/usr/bin/env python3
"""J:derive:review-20261012-box-gauge-custodial:a1 -- frame-rotated density + minimal/transverse coupling on box-QED.

Self-contained (numpy, scipy, sympy, mpmath-free).  One process.  Prints one PASS/FAIL line per check, then
HIT lines (only if a scoped new result is demonstrated), then 'TOTAL: PASS=n FAIL=m', and a last 'SUMMARY:' line.

Sections
  A  exact finite-lattice algebra (Fractions / Gaussian rationals): frame-rotated density, Gauss commutativity,
     charge-eigenspace rank, gauge covariance, path (flux) ambiguity of the Peierls dressing
  B  exact symbolic 4x4 Dirac-matrix algebra: rotor identity, connection term in the current, interband weight
  C  independent frequency (k0) integration with explicit 4x4 matrices vs the closed forms used in D-F
  D  physical-pole algebra (xi dependence of the pole)
  E  exact diagonalisation of a non-separable Peierls model vs the one-loop photon formulas (straight-path and
     trapezoid prescriptions)
  F  Brillouin-zone photon-side responses P_E, P_M of box QED (baseline, reproduces the source runner) and of the
     frame-rotated law with K = 0, with convergence/ambiguity bookkeeping
"""
import sys, time, itertools, random
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.integrate import quad

T0 = time.time()
NP = 0
NF = 0
NOTES = []

def chk(name, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {name}" + (f"  [{detail}]" if detail else ""), flush=True)
    else:
        NF += 1
        print(f"FAIL {name}" + (f"  [{detail}]" if detail else ""), flush=True)

def note(s):
    print("note " + s, flush=True)

U16 = 16 * np.pi ** 2

# ======================================================================================================
# A. exact finite-lattice algebra
# ======================================================================================================
class GQ:
    __slots__ = ("re", "im")
    def __init__(self, re=0, im=0):
        self.re = Fr(re); self.im = Fr(im)
    def __add__(s, o): return GQ(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return GQ(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return GQ(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s): return GQ(s.re, -s.im)
    def iszero(s): return s.re == 0 and s.im == 0
    def __eq__(s, o): return s.re == o.re and s.im == o.im

def zeros(n): return [[GQ(0) for _ in range(n)] for _ in range(n)]
def eye(n):
    M = zeros(n)
    for i in range(n): M[i][i] = GQ(1)
    return M
def mm(A, B):
    Bt = list(zip(*B)); out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = GQ(0)
            for t in range(len(B)):
                a = A[i][t]
                if a.re == 0 and a.im == 0: continue
                b = Bt[j][t]
                if b.re == 0 and b.im == 0: continue
                s = s + a * b
            row.append(s)
        out.append(row)
    return out
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msc(A, c): return [[A[i][j] * c for j in range(len(A[0]))] for i in range(len(A))]
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def mzero(A): return all(x.iszero() for r in A for x in r)
def rat_inverse(M):
    n = len(M)
    A = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]

PH = [GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(5, 13), Fr(12, 13)), GQ(Fr(8, 17), Fr(15, 17)), GQ(Fr(7, 25), Fr(24, 25)),
      GQ(Fr(20, 29), Fr(21, 29)), GQ(Fr(12, 37), Fr(35, 37)), GQ(Fr(-3, 5), Fr(4, 5)), GQ(Fr(15, 17), Fr(-8, 17))]
for p in PH: assert p.re * p.re + p.im * p.im == 1

def section_A():
    Lx = Ly = 3; n = 2; S = Lx * Ly; D = S * n
    sites = [(x, y) for x in range(Lx) for y in range(Ly)]
    sidx = lambda p: (p[0] % Lx) * Ly + (p[1] % Ly)
    def shift_matrix(dx, dy):
        M = zeros(D)
        for (x, y) in sites:
            for a in range(n): M[sidx((x + dx, y + dy)) * n + a][sidx((x, y)) * n + a] = GQ(1)
        return M
    def block_circ(blocks):
        M = zeros(D)
        for (dx, dy), B in blocks.items():
            for (x, y) in sites:
                s = sidx((x, y)); t = sidx((x + dx, y + dy))
                for a in range(n):
                    for b in range(n):
                        M[t * n + a][s * n + b] = M[t * n + a][s * n + b] + GQ(B[a][b])
        return M
    def proj(p):
        M = zeros(D)
        for a in range(n): M[sidx(p) * n + a][sidx(p) * n + a] = GQ(1)
        return M
    R = lambda a, b: Fr(a, b)
    tr = lambda B: [[B[j][i] for j in range(2)] for i in range(2)]
    neg_t = lambda B: [[-B[j][i] for j in range(2)] for i in range(2)]
    a10 = [[R(1, 5), R(-1, 7)], [R(1, 2), R(1, 4)]]; a01 = [[R(0, 1), R(1, 9)], [R(1, 11), R(-1, 3)]]
    a00 = [[R(0, 1), R(1, 3)], [R(-1, 3), R(0, 1)]]
    A = block_circ({(0, 0): a00, (1, 0): a10, (-1, 0): neg_t(a10), (0, 1): a01, (0, -1): neg_t(a01)})
    Ar = [[A[i][j].re for j in range(D)] for i in range(D)]
    inv = rat_inverse([[Fr(int(i == j)) - Ar[i][j] for j in range(D)] for i in range(D)])
    IpA = [[Fr(int(i == j)) + Ar[i][j] for j in range(D)] for i in range(D)]
    Ur = [[sum(inv[i][k] * IpA[k][j] for k in range(D)) for j in range(D)] for i in range(D)]   # Cayley transform
    U = [[GQ(x) for x in row] for row in Ur]; Ut = dag(U)
    I_D = eye(D)
    T10 = shift_matrix(1, 0); T01 = shift_matrix(0, 1)
    chk("A1 frame U (Cayley of rational antisymmetric translation-invariant generator) is exactly orthogonal and commutes with both translations",
        meq(mm(Ut, U), I_D) and meq(mm(U, Ut), I_D) and meq(mm(T10, U), mm(U, T10)) and meq(mm(T01, U), mm(U, T01)))
    m = {p: mm(Ut, mm(proj(p), U)) for p in sites}          # rotated density matrices m_x = U^T P_x U
    ok_orth = all(mzero(mm(m[(0, 0)], m[p])) and mzero(mm(m[p], m[(0, 0)])) for p in sites if p != (0, 0))
    ok_proj = meq(mm(m[(0, 0)], m[(0, 0)]), m[(0, 0)]) and meq(m[(0, 0)], dag(m[(0, 0)]))
    chk("A2 rotated densities m_x=U^T P_x U: orthogonal Hermitian projectors, hence mutually commuting (Gauss-law commutativity); m_0 != P_0",
        ok_orth and ok_proj and not meq(m[(0, 0)], proj((0, 0))))
    Ssum = zeros(D)
    for p in sites: Ssum = madd(Ssum, m[p])
    chk("A3 sum_x m_x = identity on all 18 dimensions: charge symbol is 1 with full-rank eigenspace at every momentum (charge-eigenspace constancy)",
        meq(Ssum, I_D))
    chk("A4 translation covariance T m_x T^-1 = m_{x+1} (exact)", meq(mm(T10, mm(m[(0, 0)], dag(T10))), m[(1, 0)]))
    # smeared density
    c = {(0, 0): Fr(1, 2), (1, 0): Fr(1, 3), (0, 1): Fr(1, 6)}
    rho = {}
    for (x, y) in sites:
        M = zeros(D)
        for (dx, dy), cv in c.items(): M = madd(M, msc(m[((x + dx) % Lx, (y + dy) % Ly)], GQ(cv)))
        rho[(x, y)] = M
    comm_ok = True
    for p in [(1, 0), (0, 1), (1, 1)]:
        comm_ok &= mzero(msub(mm(rho[(0, 0)], rho[p]), mm(rho[p], rho[(0, 0)])))
    Ssum2 = zeros(D)
    for p in sites: Ssum2 = madd(Ssum2, rho[p])
    chk("A5 smeared density rho_c(y)=sum_z c(z) m_{y+z} (scalar form factor c) commutes and sums to (sum c) * identity",
        comm_ok and meq(Ssum2, I_D))
    # control: localized non-orthogonal ('box-only') density violates commutativity
    w = [GQ(0)] * D; w[sidx((0, 0)) * n] = GQ(1); w[sidx((1, 0)) * n] = GQ(Fr(1, 2))
    def outer(v, scale): return [[v[i] * v[j].conj() * GQ(scale) for j in range(D)] for i in range(D)]
    m0 = outer(w, Fr(4, 5)); m1 = mm(T10, mm(m0, dag(T10)))
    chk("A6 control: a localized non-orthogonal density |w_x><w_x| does NOT commute with its translate (exact nonzero commutator)",
        not mzero(msub(mm(m0, m1), mm(m1, m0))))
    # Hamiltonian in original frame and tilde frame
    h10 = [[R(1, 2), R(1, 3)], [R(-1, 5), R(1, 7)]]; h01 = [[R(1, 3), R(0, 1)], [R(1, 4), R(-1, 2)]]
    h11 = [[R(1, 6), R(1, 8)], [R(-1, 9), R(1, 10)]]; h1m = [[R(1, 7), R(-1, 3)], [R(1, 11), R(1, 5)]]
    h00 = [[R(1, 2), R(1, 5)], [R(1, 5), R(-1, 3)]]
    H0 = block_circ({(0, 0): h00, (1, 0): h10, (-1, 0): tr(h10), (0, 1): h01, (0, -1): tr(h01), (1, 1): h11,
                     (-1, -1): tr(h11), (1, -1): h1m, (-1, 1): tr(h1m)})
    Ht = mm(U, mm(H0, Ut))
    rnd = random.Random(5)
    ux = {p: PH[rnd.randrange(len(PH))] for p in sites}; uy = {p: PH[rnd.randrange(len(PH))] for p in sites}
    def disp(a, Lm):
        d = a % Lm
        return d if d <= Lm // 2 else d - Lm
    def step(pos, ax, sg, u):
        x, y = pos
        if ax == 'x':
            return (u[0][(x, y)], ((x + 1) % Lx, y)) if sg > 0 else (u[0][((x - 1) % Lx, y)].conj(), ((x - 1) % Lx, y))
        return (u[1][(x, y)], (x, (y + 1) % Ly)) if sg > 0 else (u[1][(x, (y - 1) % Ly)].conj(), (x, (y - 1) % Ly))
    def transport(u, s, t, order):
        dx = disp(t[0] - s[0], Lx); dy = disp(t[1] - s[1], Ly)
        mx = [('x', 1 if dx > 0 else -1)] * abs(dx); my = [('y', 1 if dy > 0 else -1)] * abs(dy)
        W = GQ(1); pos = s
        for ax, sg in (mx + my if order == 'xy' else my + mx):
            w_, pos = step(pos, ax, sg, u); W = w_ * W
        assert pos == t
        return W
    def coupled(h, u, order):
        H = zeros(D)
        for i, s in enumerate(sites):
            for j, t in enumerate(sites):
                if j < i: continue
                W = transport(u, s, t, order) if i != j else GQ(1)
                for a in range(n):
                    for b in range(n):
                        H[j * n + a][i * n + b] = h[j * n + a][i * n + b] * W
                        if i != j: H[i * n + b][j * n + a] = h[i * n + b][j * n + a] * W.conj()
        return H
    def gmat(gs):
        M = zeros(D)
        for p, g in gs.items():
            for a in range(n): M[sidx(p) * n + a][sidx(p) * n + a] = g
        return M
    gs = {p: PH[rnd.randrange(len(PH))] for p in sites}
    def gauge_u(u, gs):
        return ({p: gs[((p[0] + 1) % Lx, p[1])] * u[0][p] * gs[p].conj() for p in sites},
                {p: gs[(p[0], (p[1] + 1) % Ly)] * u[1][p] * gs[p].conj() for p in sites})
    u = (ux, uy); u2 = gauge_u(u, gs)
    g_orig = mm(Ut, mm(gmat(gs), U))        # exp(i sum_x lambda_x rho(x)) on one-particle space
    Hs = {}
    cov = True; herm = True
    for order in ('xy', 'yx'):
        Hf = mm(Ut, mm(coupled(Ht, u, order), U)); Hf2 = mm(Ut, mm(coupled(Ht, u2, order), U))
        cov &= meq(mm(g_orig, mm(Hf, dag(g_orig))), Hf2); herm &= meq(Hf, dag(Hf)); Hs[order] = Hf
    zero_field = meq(mm(Ut, mm(coupled(Ht, ({p: GQ(1) for p in sites}, {p: GQ(1) for p in sites}), 'xy'), U)), H0)
    chk("A7 Peierls dressing of the rotated-frame hopping (both link-path orders) is exactly covariant under the gauge group generated by the rotated densities; Hermitian; reduces to H0 at zero field",
        cov and herm and zero_field)
    flat = gauge_u(({p: GQ(1) for p in sites}, {p: GQ(1) for p in sites}), gs)
    same_flat = meq(mm(Ut, mm(coupled(Ht, flat, 'xy'), U)), mm(Ut, mm(coupled(Ht, flat, 'yx'), U)))
    chk("A8 the two link-path dressings agree on pure-gauge links and differ on generic links: the path ambiguity is a gauge-invariant flux-dependent (transverse, nonminimal) term",
        same_flat and not meq(Hs['xy'], Hs['yx']))
    Ho = coupled(H0, u, 'xy'); Ho2 = coupled(H0, u2, 'xy')
    chk("A9 control: orbital Peierls on the UNROTATED hopping is covariant under on-site phases but NOT under the rotated-density gauge group (frame and coupling must be rotated together)",
        meq(mm(gmat(gs), mm(Ho, dag(gmat(gs)))), Ho2) and not meq(mm(g_orig, mm(Ho, dag(g_orig))), Ho2))

# ======================================================================================================
# B. symbolic Dirac algebra
# ======================================================================================================
def section_B():
    I = sp.I
    s0 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -I], [I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
    Z2 = sp.zeros(2)
    blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
    ax = blk(Z2, sx, sx, Z2); ay = blk(Z2, sy, sy, Z2); az = blk(Z2, sz, sz, Z2); be = blk(s0, Z2, Z2, -s0)
    G = [ax, ay, az, be]; one = sp.eye(4)
    chk("B1 explicit Dirac matrices (alpha_x,alpha_y,alpha_z,beta) satisfy the Clifford relations",
        all((G[i] * G[j] + G[j] * G[i]) == (2 * one if i == j else sp.zeros(4)) for i in range(4) for j in range(4)))
    e = (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3))
    eh = e[0] * ax + e[1] * ay + e[2] * az
    cth, sth, E = sp.Rational(7, 25), sp.Rational(24, 25), sp.Rational(5, 2)
    h = E * (cth * be + sth * eh)
    allok = True
    for tpar in (sp.Rational(1, 3), sp.Rational(1, 5), sp.Rational(2, 7), sp.Rational(0), sp.Rational(-1, 4)):
        c = (1 - tpar ** 2) / (1 + tpar ** 2); s = 2 * tpar / (1 + tpar ** 2)
        c2 = c ** 2 - s ** 2; s2 = 2 * s * c
        B = be * eh; Rr = c * one + s * B; Rd = c * one - s * B
        ct = cth * c2 + sth * s2; st = sth * c2 - cth * s2
        allok &= (sp.simplify(Rr * Rd - one) == sp.zeros(4)) and (sp.simplify(Rr * h * Rd - E * (ct * be + st * eh)) == sp.zeros(4))
    chk("B2 exact rotor identity: R=cos(phi)+sin(phi) beta e.alpha is unitary and R h R^dag = E(cos(theta-2phi) beta + sin(theta-2phi) e.alpha) (5 rational angles)", allok)
    c, s = sp.Rational(4, 5), sp.Rational(3, 5)
    Rr = c * one + s * be * eh; Rd = c * one - s * be * eh
    chk("B3 phi=theta/2 (fraction s=1 of the rotation): R h R^dag = E beta exactly, i.e. band-diagonal with a FIXED band projector (1-beta)/2",
        sp.simplify(Rr * h * Rd - E * be) == sp.zeros(4))
    k = sp.symbols('k', real=True)
    Sf = sp.Function('S')(k); Mf = sp.Function('M')(k); phi = sp.Function('phi')(k)
    hk = Sf * ax + Mf * be
    Rk = sp.cos(phi) * one + sp.sin(phi) * (be * ax); Rkd = sp.cos(phi) * one - sp.sin(phi) * (be * ax)
    ht = sp.simplify(Rk * hk * Rkd)
    conn = Rk.diff(k) * Rkd
    chk("B4 current in the rotated variables: d(R h R^dag)/dk = R h' R^dag + [R' R^dag, R h R^dag] (non-Abelian Berry-connection term), connection = phi' beta alpha_x",
        sp.simplify(ht.diff(k) - (Rk * hk.diff(k) * Rkd + conn * ht - ht * conn)) == sp.zeros(4)
        and sp.simplify(conn - sp.diff(phi, k) * (be * ax)) == sp.zeros(4))
    Ef = sp.Function('E')(k); tf = sp.Function('tt')(k)
    nsl = sp.cos(tf) * be + sp.sin(tf) * ax
    dh = (Ef * nsl).diff(k)
    Pp = (one + nsl) / 2; Pm = (one - nsl) / 2
    wgt = sp.simplify((Pp * dh * Pm * dh).trace())
    chk("B5 interband (pair-creation) weight of the zero-transfer current: Tr[P+ h' P- h'] = 2 E^2 (theta~')^2, independent of E'; zero where theta~ is constant",
        sp.simplify(wgt - 2 * Ef ** 2 * tf.diff(k) ** 2) == 0)

# ======================================================================================================
# C. independent k0 integration with explicit matrices
# ======================================================================================================
s0n = np.eye(2); sxn = np.array([[0, 1], [1, 0]], complex); syn = np.array([[0, -1j], [1j, 0]]); szn = np.diag([1., -1.]).astype(complex)
Z2n = np.zeros((2, 2))
GAM = [np.block([[Z2n, s], [s, Z2n]]) for s in (sxn, syn, szn)] + [np.block([[s0n, Z2n], [Z2n, -s0n]])]

def section_C():
    rng = np.random.default_rng(7); worst = 0.0
    for _ in range(12):
        a = rng.normal(size=4); b = rng.normal(size=4); v = rng.normal(size=4)
        h = sum(cc * G for cc, G in zip(a, GAM)); h2 = sum(cc * G for cc, G in zip(b, GAM)); V = sum(cc * G for cc, G in zip(v, GAM))
        E, E2 = np.linalg.norm(a), np.linalg.norm(b); n, n2 = a / E, b / E2
        def integrand(k0, which):
            G1 = np.linalg.inv(1j * k0 * np.eye(4) - h); G2 = np.linalg.inv(1j * k0 * np.eye(4) - h2)
            return np.trace(G1 @ G2) if which == 0 else np.trace(V @ G1 @ V @ G2)
        for which, pred in ((0, -2 * (1 - n @ n2) / (E + E2)),
                            (1, -2 * ((v @ v) * (1 + n @ n2) - 2 * (v @ n) * (v @ n2)) / (E + E2))):
            re = quad(lambda x: integrand(x, which).real, -np.inf, np.inf, epsabs=1e-12, epsrel=1e-12, limit=400)[0] / (2 * np.pi)
            im = quad(lambda x: integrand(x, which).imag, -np.inf, np.inf, epsabs=1e-12, epsrel=1e-12, limit=400)[0] / (2 * np.pi)
            worst = max(worst, abs(re - pred) / max(1, abs(pred)), abs(im))
    chk("C1 numerical k0 integration (scipy quad, explicit 4x4 matrices, 24 random cases) of Tr[G G'] and Tr[V G V G'] equals -2(1-n.n')/(E+E') and -2[v^2(1+n.n')-2(v.n)(v.n')]/(E+E')",
        worst < 1e-9, f"worst deviation {worst:.1e}")

# ======================================================================================================
# D. physical pole
# ======================================================================================================
def section_D():
    I = sp.I
    s0 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -I], [I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]]); Z2 = sp.zeros(2)
    blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
    G = [blk(Z2, s, s, Z2) for s in (sx, sy, sz)] + [blk(s0, Z2, Z2, -s0)]
    one = sp.eye(4)
    rngs = random.Random(11)
    ok_id = True
    for _ in range(4):
        a = sp.Matrix(4, 4, lambda i, j: sp.Rational(rngs.randint(-5, 5), rngs.randint(1, 4)) + I * sp.Rational(rngs.randint(-5, 5), rngs.randint(1, 4)))
        b = sp.Matrix(4, 4, lambda i, j: sp.Rational(rngs.randint(-5, 5), rngs.randint(1, 4)) + I * sp.Rational(rngs.randint(-5, 5), rngs.randint(1, 4)) + (3 if i == j else 0))
        if b.det() == 0: continue
        bi = b.inv()
        ok_id &= sp.simplify((a - b) * bi * (b - a) - (2 * a - b - a * bi * a)) == sp.zeros(4)
    chk("D1 exact identity behind the xi-dependent self-energy: (a-b) b^-1 (b-a) = 2a - b - a b^-1 a (a = G^-1(p), b = G^-1(k)), random rational complex matrices", ok_id)
    avec = (1, 2, 2, 4)                    # |a| = 5
    h = sum((c * Gm for c, Gm in zip(avec, G)), sp.zeros(4)); E = 5
    aop = E * one + h                      # a(p) at the on-shell Euclidean continuation p0 = iE
    ns = (E * one + h).nullspace()
    X = sp.Matrix(4, 4, lambda i, j: sp.Rational(rngs.randint(-4, 4), rngs.randint(1, 3)) + I * sp.Rational(rngs.randint(-4, 4), rngs.randint(1, 3)))
    c1, c2 = sp.Rational(3, 7), sp.Rational(-5, 11)
    Sig = c1 * aop + c2 * aop * X * aop    # structure of the xi-dependent part
    zero = all(sp.simplify(Sig * u) == sp.zeros(4, 1) and sp.simplify((u.H) * Sig) == sp.zeros(1, 4) for u in ns)
    chk("D2 xi-dependent part c1 a + c2 a X a annihilates the free on-shell spinors (null space dim 2) from both sides: first-order pole shift <u|Sigma_xi|u> = 0 for every X, c1, c2",
        len(ns) == 2 and zero)

# ======================================================================================================
# E/F common: box-QED and frame-rotated laws as Clifford 4-vector functions a(k): h = a . Gamma
# ======================================================================================================
def _phi(t):
    t = np.clip(t, 0.0, 1.0)
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        f0 = np.where(t > 0, np.exp(-1.0 / np.where(t > 0, t, 1.0)), 0.0)
        f1 = np.where(t < 1, np.exp(-1.0 / np.where(t < 1, 1.0 - t, 1.0)), 0.0)
    return f0 / (f0 + f1)

def plateau(k, b1, b2):
    return 1.0 - _phi((np.abs(k) - b1) / (b2 - b1))

class Model:
    def __init__(self, kind, b1, b2, r, m):
        self.kind, self.b1, self.b2, self.r, self.m = kind, b1, b2, r, m
    def S(self, k):
        rho = plateau(k, self.b1, self.b2); return rho * k + (1 - rho) * np.sin(k)
    def W(self, k):
        rho = plateau(k, self.b1, self.b2); return self.r * (1 - rho) * (1 - np.cos(k))
    def a(self, kx, ky, kz):
        kx, ky, kz = np.broadcast_arrays(kx, ky, kz)
        a1, a2, a3 = self.S(kx), self.S(ky), self.S(kz)
        a4 = self.m + self.W(kx) + self.W(ky) + self.W(kz)
        if self.kind == 'bq':
            return np.stack([a1, a2, a3, a4])
        sig = np.sqrt(a1 ** 2 + a2 ** 2 + a3 ** 2)
        E = np.sqrt(sig ** 2 + a4 ** 2)
        th = np.arctan2(sig, a4)
        rho3 = plateau(kx, self.b1, self.b2) * plateau(ky, self.b1, self.b2) * plateau(kz, self.b1, self.b2)
        tt = rho3 * th                                   # theta~ = (1-s) theta, s = 1 - rho3
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio = np.where(th > 1e-9, np.sin(tt) / np.sin(np.where(th > 1e-9, th, 1.0)), rho3)
        return np.stack([ratio * a1, ratio * a2, ratio * a3, E * np.cos(tt)])

HD = 1e-3
def dy1(f, kx, ky, kz):
    return (-f(kx, ky + 2 * HD, kz) + 8 * f(kx, ky + HD, kz) - 8 * f(kx, ky - HD, kz) + f(kx, ky - 2 * HD, kz)) / (12 * HD)
def dy2(f, kx, ky, kz, f0=None):
    if f0 is None: f0 = f(kx, ky, kz)
    return (-f(kx, ky + 2 * HD, kz) + 16 * f(kx, ky + HD, kz) - 30 * f0 + 16 * f(kx, ky - HD, kz) - f(kx, ky - 2 * HD, kz)) / (12 * HD * HD)
GLx, GLw = np.polynomial.legendre.leggauss(5)
GLx = 0.5 * (GLx + 1); GLw = 0.5 * GLw

def responses(model, N, q, mode, chunk=8):
    """Static one-loop photon-side responses on the N^3 midpoint grid, current along y, q along x.
       P_E(q) = [chi00(q)+chi00(-q)]/q^2,  P_M(q) = [dia - chi_p(q) - chi_p(-q) - (q=0 residual)]/q^2."""
    k1 = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    KY, KZ = np.meshgrid(k1, k1, indexing='ij')
    f = model.a
    acc = dict(chi00=0.0, chi00m=0.0, chip=0.0, chipm=0.0, dia=0.0, chip0=0.0, dia0=0.0, PEw=0.0)
    for i0 in range(0, N, chunk):
        kx = k1[i0:i0 + chunk][:, None, None]; ky = KY[None]; kz = KZ[None]
        a0 = f(kx, ky, kz); E0 = np.sqrt((a0 ** 2).sum(0)); n0 = a0 / E0
        v0 = dy1(f, kx, ky, kz)
        x2 = (v0 ** 2).sum(0); xn = (v0 * n0).sum(0)
        acc['PEw'] += np.sum((x2 - xn ** 2) / (2 * E0 ** 3))
        s0 = dy2(f, kx, ky, kz, a0)
        acc['dia0'] += np.sum(-2 * (s0 * n0).sum(0))
        acc['chip0'] += np.sum(2 * (2 * x2 - 2 * xn ** 2) / (2 * E0))
        for sgn, keys in ((+1, ('chi00', 'chip')), (-1, ('chi00m', 'chipm'))):
            qq = sgn * q
            a1 = f(kx + qq, ky, kz); E1 = np.sqrt((a1 ** 2).sum(0)); n1 = a1 / E1
            nn = (n0 * n1).sum(0)
            acc[keys[0]] += np.sum((1 - nn) / (E0 + E1))
            if mode == 'sp':
                vq = 0.0
                for xs, w in zip(GLx, GLw): vq = vq + w * dy1(f, kx + xs * qq, ky, kz)
            else:
                vq = 0.5 * (dy1(f, kx + qq, ky, kz) + v0)
            acc[keys[1]] += np.sum(((vq ** 2).sum(0) * (1 + nn) - 2 * (vq * n0).sum(0) * (vq * n1).sum(0)) / (E0 + E1))
        if mode == 'sp':
            sq = 0.0
            for xs, w in zip(GLx, GLw):
                for sg in (+1, -1): sq = sq + w * (1 - xs) * dy2(f, kx + sg * xs * q, ky, kz)
        else:
            sq = s0
        acc['dia'] += np.sum(-2 * (sq * n0).sum(0))
    V = N ** 3
    o = {k: v / V for k, v in acc.items()}
    o['PE_q'] = (o['chi00'] + o['chi00m']) / q ** 2
    o['ward0'] = o['dia0'] - o['chip0']
    o['PM_q'] = ((o['dia'] - o['chip'] - o['chipm']) - o['ward0']) / q ** 2
    return o

_cache = {}
def photon(kind, b1, b2, r, m, N, mode='sp', qs=(0.02, 0.04)):
    key = (kind, b1, b2, r, m, N, mode)
    if key in _cache: return _cache[key]
    mod = Model(kind, b1, b2, r, m)
    rs = [responses(mod, N, q, mode) for q in qs]
    q1, q2 = qs
    ex = lambda kk: (q2 ** 2 * rs[0][kk] - q1 ** 2 * rs[1][kk]) / (q2 ** 2 - q1 ** 2)
    PE, PM = ex('PE_q'), ex('PM_q')
    out = dict(PE=U16 * PE, PM=U16 * PM, dc=U16 * (PM - PE) / 2, PEw=U16 * rs[0]['PEw'], ward0=rs[0]['ward0'])
    _cache[key] = out
    return out

def section_E():
    Lx = Ly = 14
    kk = 2 * np.pi * np.arange(Lx) / Lx
    KX, KY = np.meshgrid(kk, kk, indexing='ij')
    def avec(kx, ky):
        m = 1.0
        return np.stack([np.sin(kx) + 0.3 * np.sin(ky) * np.cos(kx), np.sin(ky) + 0.2 * np.sin(kx) * np.cos(ky),
                         0.5 * np.sin(kx) * np.sin(ky),
                         m + (1 - np.cos(kx)) + (1 - np.cos(ky)) + 0.3 * np.sin(kx) * np.sin(ky)])
    hk = np.zeros((Lx, Ly, 4, 4), complex)
    for i in range(Lx):
        for j in range(Ly): hk[i, j] = sum(c * G for c, G in zip(avec(kk[i], kk[j]), GAM))
    t = {}
    for Rx in range(-3, 4):
        for Ry in range(-3, 4):
            tt = sum(hk[i, j] * np.exp(1j * (kk[i] * Rx + kk[j] * Ry)) for i in range(Lx) for j in range(Ly)) / (Lx * Ly)
            if np.abs(tt).max() > 1e-12: t[(Rx, Ry)] = tt
    nonsep = [R for R in t if R[0] != 0 and R[1] != 0]
    q = 2 * np.pi / Lx
    def energy(a, phi, mode):
        E = 0.0
        for ky in kk:
            H = np.zeros((4 * Lx, 4 * Lx), complex)
            for (Rx, Ry), tt in t.items():
                for x0 in range(Lx):
                    x1 = (x0 + Rx) % Lx
                    if mode == 'sp':
                        Phi = a * (np.sin(q * (x0 + Rx)) - np.sin(q * x0)) / (q * Rx) if Rx != 0 else a * np.cos(q * x0)
                        ph = np.exp(1j * Ry * Phi)
                    else:
                        ph = 0.5 * (np.exp(1j * Ry * a * np.cos(q * (x0 + Rx))) + np.exp(1j * Ry * a * np.cos(q * x0)))
                    H[4 * x1:4 * x1 + 4, 4 * x0:4 * x0 + 4] += tt * np.exp(-1j * ky * Ry) * ph
            for x0 in range(Lx): H[4 * x0:4 * x0 + 4, 4 * x0:4 * x0 + 4] += phi * np.cos(q * x0) * np.eye(4)
            assert np.abs(H - H.conj().T).max() < 1e-10
            w = np.linalg.eigvalsh(H); E += w[w < 0].sum()
        return E
    def f(kx, ky, kz): return avec(kx, ky)
    def formula(mode):
        a0 = avec(KX, KY); E = np.sqrt((a0 ** 2).sum(0)); n = a0 / E
        chip = 0.0; chi00 = 0.0
        for sg in (+1, -1):
            qq = sg * q
            a1 = avec(KX + qq, KY); E1 = np.sqrt((a1 ** 2).sum(0)); n1 = a1 / E1; nn = (n * n1).sum(0)
            chi00 += np.sum((1 - nn) / (E + E1))
            if mode == 'sp':
                vq = 0.0
                for xs, w in zip(GLx, GLw): vq = vq + w * dy1(f, KX + xs * qq, KY, 0.0)
            else:
                vq = 0.5 * (dy1(f, KX + qq, KY, 0.0) + dy1(f, KX, KY, 0.0))
            chip += np.sum(((vq ** 2).sum(0) * (1 + nn) - 2 * (vq * n).sum(0) * (vq * n1).sum(0)) / (E + E1))
        if mode == 'sp':
            sq = 0.0
            for xs, w in zip(GLx, GLw):
                for sg in (+1, -1): sq = sq + w * (1 - xs) * dy2(f, KX + sg * xs * q, KY, 0.0)
        else:
            sq = dy2(f, KX, KY, 0.0)
        dia = np.sum(-2 * (sq * n).sum(0))
        return 0.25 * (dia - chip), -0.25 * chi00
    da = 2e-2
    res = {}
    E0 = {m_: energy(0, 0, m_) for m_ in ('sp', 'trap')}
    for mode in ('sp', 'trap'):
        e2 = (energy(da, 0, mode) + energy(-da, 0, mode) - 2 * E0[mode]) / (2 * da ** 2)
        fp = (energy(0, da, mode) + energy(0, -da, mode) - 2 * E0[mode]) / (2 * da ** 2)
        fa, fe = formula(mode)
        res[mode] = (e2, fa, fp, fe)
    chk("E1 exact diagonalisation (14x14 torus, 9 hops incl. diagonals, matrix-valued, non-separable) reproduces the one-loop straight-path magnetic coefficient and the electric coefficient",
        len(nonsep) >= 4 and abs(res['sp'][0] - res['sp'][1]) / abs(res['sp'][1]) < 1e-4 and abs(res['sp'][2] - res['sp'][3]) / abs(res['sp'][3]) < 1e-4,
        f"a^2 coeff ED {res['sp'][0]:.6f} vs formula {res['sp'][1]:.6f}; phi^2 coeff ED {res['sp'][2]:.6f} vs {res['sp'][3]:.6f}")
    chk("E2 same for the trapezoid prescription H=(H_xy+H_yx)/2 (Hermitian lattice dressing); the electric coefficient is identical for both prescriptions",
        abs(res['trap'][0] - res['trap'][1]) / abs(res['trap'][1]) < 1e-4 and abs(res['trap'][2] - res['sp'][2]) < 1e-9,
        f"a^2 coeff ED {res['trap'][0]:.6f} vs formula {res['trap'][1]:.6f}")
    chk("E3 the two gauge-covariant minimal dressings give DIFFERENT vacuum magnetic responses for the same non-separable matrix hopping (exact-diagonalisation values)",
        abs(res['sp'][0] - res['trap'][0]) > 0.1 * abs(res['sp'][0]), f"{res['sp'][0]:.4f} vs {res['trap'][0]:.4f}")
    return res

# ======================================================================================================
# F. Brillouin-zone numerics and structure of the frame-rotated law
# ======================================================================================================
def section_F():
    # --- structural facts of the rotated law, pointwise
    rng = np.random.default_rng(3)
    b1, b2, r, m = 1.0, 2.0, 1.0, 0.5
    bq, rot = Model('bq', b1, b2, r, m), Model('rot', b1, b2, r, m)
    kin = rng.uniform(-b1, b1, size=(3, 400))
    chk("F1 inside the cube |k_j|<=b1 the rotated law equals box QED exactly (box Feynman rules and in-box current unchanged)",
        np.abs(rot.a(*kin) - bq.a(*kin)).max() < 1e-14)
    sgn = rng.choice([-1.0, 1.0], size=(3, 400))
    kout = sgn * rng.uniform(b2, np.pi, size=(3, 400))
    ao = rot.a(*kout)
    chk("F2 outside the shell (all |k_j|>=b2) the rotated law is exactly band-diagonal: a = (0,0,0,E), band projector (1-beta)/2 fixed; E unchanged by the rotation",
        np.abs(ao[:3]).max() < 1e-14 and np.abs(ao[3] - np.sqrt((bq.a(*kout) ** 2).sum(0))).max() < 1e-12)
    # unit-vector derivative (pair-creation weight) outside vs shell
    def nhat(kx, ky, kz):
        a = rot.a(kx, ky, kz); return a / np.sqrt((a ** 2).sum(0))
    w_out = (((nhat(kout[0], kout[1] + 1e-4, kout[2]) - nhat(kout[0], kout[1] - 1e-4, kout[2])) / 2e-4) ** 2).sum(0)
    kshell = np.stack([rng.uniform(b1 + 0.2, b2 - 0.2, 400), rng.uniform(-b1, b1, 400), rng.uniform(-b1, b1, 400)])
    w_sh = (((nhat(kshell[0], kshell[1] + 1e-4, kshell[2]) - nhat(kshell[0], kshell[1] - 1e-4, kshell[2])) / 2e-4) ** 2).sum(0)
    chk("F3 minimal pair-creation weight |d_y n~|^2 vanishes outside (<1e-12) and is positive on the shell: the frame rotation relocates the interband current into the shell",
        w_out.max() < 1e-12 and w_sh.min() >= 0 and w_sh.max() > 1e-2, f"max outside {w_out.max():.1e}, max on shell {w_sh.max():.3f}")
    # charge symbol and band projectors
    def Pminus(a):
        E = np.linalg.norm(a); return 0.5 * (np.eye(4) - sum(c * G for c, G in zip(a / E, GAM)))
    pts = [kout[:, i] for i in range(6)]
    dev_rot = max(np.abs(Pminus(rot.a(*p)) - 0.5 * (np.eye(4) - GAM[3])).max() for p in pts)
    dev_bq = max(np.abs(Pminus(bq.a(*pts[i])) - Pminus(bq.a(*pts[j]))).max() for i in range(6) for j in range(i))
    chk("F4 charge-eigenspace constancy is not band constancy: the charge symbol is the 4x4 identity (rank 4) at every k in both frames, while the band subspace is fixed outside only after the rotation (deviation 0) and varies in the original frame",
        dev_rot < 1e-12 and dev_bq > 0.05, f"rotated {dev_rot:.1e}, original {dev_bq:.3f}")
    # --- Cauchy-Schwarz floor on the electric channel
    def floor_bound(b1_, b2_, r_, m_):
        mod = Model('bq', b1_, b2_, r_, m_)
        ky = np.linspace(-b1_, b1_, 161); KY, KZ = np.meshgrid(ky, ky, indexing='ij')
        xs = np.linspace(b1_, b2_, 401)
        a_e = mod.a(b1_, KY, KZ); Ee = np.sqrt((a_e ** 2).sum(0)); th = np.arccos(a_e[3] / Ee)
        A = mod.a(xs[:, None, None], KY[None], KZ[None]); EE = np.sqrt((A ** 2).sum(0))
        line = np.trapezoid(2 * EE, xs, axis=0)
        return U16 * 2 * np.trapezoid(np.trapezoid(th ** 2 / line, ky, axis=1), ky) / (2 * np.pi) ** 3
    # line-wise inequality check on the rotated law
    modr = Model('rot', b1, b2, r, m)
    xs = np.linspace(b1, b2, 4001); okline = True; minratio = 1e9
    for (ky_, kz_) in [(0.0, 0.0), (0.5, -0.3), (-0.9, 0.8), (0.95, 0.95), (0.2, 0.7), (-0.6, -0.1)]:
        A = modr.a(xs, ky_, kz_); Eq = np.sqrt((A ** 2).sum(0)); nn_ = A / Eq
        dn2 = (np.gradient(nn_, xs, axis=1) ** 2).sum(0)
        lhs = np.trapezoid(dn2 / (2 * Eq), xs)
        Ab = Model('bq', b1, b2, r, m).a(b1, ky_, kz_); th_e = np.arccos(Ab[3] / np.linalg.norm(Ab))
        rhs = th_e ** 2 / np.trapezoid(2 * Eq, xs)
        okline &= lhs >= rhs * (1 - 1e-6); minratio = min(minratio, lhs / rhs)
    chk("F5 Cauchy-Schwarz line bound: on every x-line through the cube, int |d_x n~|^2/(2E) dkx >= theta_e^2 / int 2E dkx (theta_e = Dirac polar angle at the cube face)",
        okline, f"min lhs/rhs over 6 lines = {minratio:.3f}")
    # --- BZ numerics
    ref23 = dict(PEw=15.594538872403044, PM=39.43120021912496)           # source runner photon(Law(2,3,1,2,3,0.5),64) x 16pi^2
    ref12 = dict(PEw=0.044436258851928576 * U16, PM=0.07132560702151347 * U16)   # source runner photon(Law(1,2,1,1,2,0.5),64)
    p23 = photon('bq', 2.0, 3.0, 1.0, 0.5, 64)
    p12 = photon('bq', 1.0, 2.0, 1.0, 0.5, 64)
    chk("F6 baseline: this independent implementation of box QED (straight-path vertex, explicit grid sums) reproduces the source runner r85_box_qed.photon to <=1e-6 relative (shapes (2,3) and (1,2), N=64, m=0.5)",
        abs(p23['PEw'] / ref23['PEw'] - 1) < 1e-6 and abs(p23['PM'] / ref23['PM'] - 1) < 1e-6
        and abs(p12['PEw'] / ref12['PEw'] - 1) < 1e-6 and abs(p12['PM'] / ref12['PM'] - 1) < 1e-6,
        f"(2,3): P_M {p23['PM']:.5f} vs {ref23['PM']:.5f}; (1,2): P_M {p12['PM']:.5f} vs {ref12['PM']:.5f}")
    out = {}
    for label, args in [('bq12', ('bq', 1.0, 2.0, 1.0, 0.5, 'sp')), ('rot12sp', ('rot', 1.0, 2.0, 1.0, 0.5, 'sp')),
                        ('rot12trap', ('rot', 1.0, 2.0, 1.0, 0.5, 'trap')), ('rot12r0', ('rot', 1.0, 2.0, 0.0, 0.5, 'sp')),
                        ('rot23sp', ('rot', 2.0, 3.0, 1.0, 0.5, 'sp'))]:
        kind, B1, B2, rr, mm_, mode = args
        a96 = photon(kind, B1, B2, rr, mm_, 96, mode)
        if label == 'rot23sp':
            out[label] = (a96, a96)       # shape (2,3) converges slowly in P_M (N=64: -0.3, 96: +0.28, 128: +0.19, 160: +0.21); only P_E is used below
            note(f"{label}: N=96 P_E={a96['PE']:.4f} P_M={a96['PM']:.4f} dc={a96['dc']:+.4f} (units e^2/16pi^2, m=0.5; slow P_M convergence, see ATTEMPT)")
            continue
        a64 = photon(kind, B1, B2, rr, mm_, 64, mode)
        out[label] = (a64, a96)
        note(f"{label}: N=64 P_E={a64['PE']:.4f} P_M={a64['PM']:.4f} dc={a64['dc']:+.4f} | N=96 P_E={a96['PE']:.4f} P_M={a96['PM']:.4f} dc={a96['dc']:+.4f} (units e^2/16pi^2, m=0.5)")
    conv = {k: abs(v[1]['dc'] - v[0]['dc']) for k, v in out.items() if k != 'rot23sp'}
    chk("F7 grid-convergence bookkeeping: |dc(N=96)-dc(N=64)| < 0.35 (units e^2/16pi^2) for the four runs at shapes (1,2), and Ward residuals |dia-chi_p| (q=0) < 5e-3 at N=96",
        max(conv.values()) < 0.35 and max(abs(v[1]['ward0']) for v in out.values()) < 5e-3,
        "max conv diff %.3f; N=160 values (not rerun here) 3.490 and 0.206 for rot12sp, rot23sp" % max(conv.values()))
    chk("F8 electric channel: P_E is independent of the minimal-coupling prescription (SP vs trapezoid) and of N to 1e-3; and P_E(rotated) exceeds P_E(box QED) at shape (1,2)",
        abs(out['rot12sp'][1]['PE'] - out['rot12trap'][1]['PE']) < 1e-3 and out['rot12sp'][1]['PE'] > out['bq12'][1]['PE'] + 1.0,
        f"rot {out['rot12sp'][1]['PE']:.3f} vs box QED {out['bq12'][1]['PE']:.3f}")
    fl12 = floor_bound(1.0, 2.0, 1.0, 0.5); fl23 = floor_bound(2.0, 3.0, 1.0, 0.5)
    chk("F9 electric-channel floor (Cauchy-Schwarz): P_E(rotated) >= floor from the x-slabs; (1,2) floor and (2,3) floor both below the computed values",
        out['rot12sp'][1]['PE'] > fl12 > 1.5 and out['rot23sp'][1]['PE'] > fl23 > 5.0,
        f"(1,2): P_E {out['rot12sp'][1]['PE']:.3f} >= {fl12:.3f}; (2,3): P_E {out['rot23sp'][1]['PE']:.3f} >= {fl23:.3f}")
    d_sp = out['rot12sp'][1]['dc']; d_tr = out['rot12trap'][1]['dc']
    chk("F10 photon-side split dc=(P_M-P_E)/2 of the K=0 rotated law (straight-path dressing) and of box QED at shape (1,2), r=1, m=0.5 are both nonzero beyond 3x the grid-convergence error",
        d_sp > 3 * max(conv['rot12sp'], 0.01) and out['bq12'][1]['dc'] > 3 * max(conv['bq12'], 0.01),
        f"rotated SP {d_sp:+.3f} (conv err {conv['rot12sp']:.3f}); box QED {out['bq12'][1]['dc']:+.3f}")
    chk("F11 the photon-side split changes sign when the edge mass is switched off (r=0) for the rotated law: no sign-definiteness (tuned zeros exist in (r, shape) space)",
        out['rot12r0'][1]['dc'] < -1.0 and out['rot12sp'][1]['dc'] > 1.0,
        f"r=1: {out['rot12sp'][1]['dc']:+.3f}, r=0: {out['rot12r0'][1]['dc']:+.3f}")
    chk("F12 prescription dependence: trapezoid and straight-path dressings of the SAME rotated density/hopping differ in dc by more than 10 (units e^2/16pi^2) at shape (1,2), against a convergence error < 0.35",
        abs(d_tr - d_sp) > 10.0 and conv['rot12trap'] < 0.35, f"trapezoid {d_tr:+.3f} vs straight-path {d_sp:+.3f}")
    chk("F13 control: box QED (axis-only hops) has NO prescription dependence in the same code path (trapezoid = straight-path for the separable law to 1e-3 in e^2/16pi^2, finite-difference noise ~1e-5)",
        abs(photon('bq', 1.0, 2.0, 1.0, 0.5, 64, 'trap')['dc'] - p12['dc']) < 1e-3)
    return out

# ======================================================================================================
def main():
    section_B(); section_C(); section_D()
    ed = section_E()
    out = section_F()
    section_A()
    hit = False
    d_sp = out['rot12sp'][1]['dc']; d_tr = out['rot12trap'][1]['dc']
    if NF == 0 and abs(d_tr - d_sp) > 10.0 and abs(ed['sp'][0] - ed['trap'][0]) > 0.1 * abs(ed['sp'][0]):
        hit = True
        print(f"HIT: for the specified construction (rotated density, K=0) the photon-side light-cone split is NOT fixed by the density frame and the "
              f"hopping: two gauge-covariant minimal dressings (ED-validated) give dc = {d_sp:+.2f} vs {d_tr:+.2f} (e^2/16pi^2, shape (1,2), m=0.5) while the "
              f"electric channel P_E = {out['rot12sp'][1]['PE']:.2f} (above a proved floor) is prescription-independent; so for this construction the flux-dependent "
              f"(transverse nonminimal) part of the coupling is load-bearing for the photon cone (scope: photon side only, one loop, m=0.5, K=0, shapes (1,2) and (2,3))", flush=True)
    print(f"TOTAL: PASS={NP} FAIL={NF}", flush=True)
    print(f"SUMMARY: a frame-rotated Peierls density removes the minimal pair-creation current outside the box only by moving it into the shell "
          f"(proved floor; P_E {out['bq12'][1]['PE']:.2f} -> {out['rot12sp'][1]['PE']:.2f} at shape (1,2)), and its photon-side cone split depends on the O(F) dressing "
          f"({d_sp:+.1f} vs {d_tr:+.1f} in e^2/16pi^2), so the transverse kernel decides it, while the electron-side loop and an explicit kernel K remain uncomputed.", flush=True)
    sys.exit(0 if NF == 0 else 1)

if __name__ == "__main__":
    main()
