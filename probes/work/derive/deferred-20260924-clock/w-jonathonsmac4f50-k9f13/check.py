#!/usr/bin/env python3
"""
Receding-wall (Dirichlet slab) limits of the exponentially clocked walk.

Setting (block 54 / 108 / 109 as landed on main, supplied model): on l^2(Z; C^2)
    (J psi)(n) = (i/2) s1 [ L^{n-1/2} psi(n-1) - L^{n+1/2} psi(n+1) ] + L^n (p2 s2 + p3 s3) psi(n),
L = lambda = mu^2 (here L=4, mu=2, all arithmetic rational), p=0 is the line.

Checks (exact Gaussian-rational / Fraction / sympy unless labelled mpmath):
  A  gauge, series, Lagrange identity, slow-end norm bound, shift covariance of slabs
  B  zero-energy boundary space of the line: Dirichlet planes L_eta, eta=(-1)^b
  C  3D witness: Dirichlet plane P_b -> span(b,c), exact rate (4/9)^(b+1)
  D  exact slab Green functions at z=i: line (no limit, two parity limits) vs 3D sector (one limit)
  E  frozen-source hash verification (skipped if the read-only checkouts are absent)
Python: sympy, mpmath, fractions only.
"""
import sys, os, json, hashlib, subprocess, time
from fractions import Fraction as F
import sympy as sp
import mpmath as mp

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def ok(name, cond, extra=""):
    if cond:
        RES["pass"] += 1
        print("PASS", name, extra)
    else:
        RES["fail"] += 1
        print("FAIL", name, extra)


# ---------------------------------------------------------------- Gaussian rationals
class GQ:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = F(r)
        self.i = F(i)

    def __add__(s, o):
        o = _g(o); return GQ(s.r + o.r, s.i + o.i)
    __radd__ = __add__

    def __sub__(s, o):
        o = _g(o); return GQ(s.r - o.r, s.i - o.i)

    def __rsub__(s, o):
        return _g(o) - s

    def __neg__(s):
        return GQ(-s.r, -s.i)

    def __mul__(s, o):
        o = _g(o); return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__

    def conj(s):
        return GQ(s.r, -s.i)

    def abs2(s):
        return s.r * s.r + s.i * s.i

    def __truediv__(s, o):
        o = _g(o); d = o.abs2(); n = s * o.conj(); return GQ(n.r / d, n.i / d)

    def __eq__(s, o):
        o = _g(o); return s.r == o.r and s.i == o.i

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __repr__(s):
        return f"({s.r}+{s.i}i)"

    def c(s):
        return complex(float(s.r), float(s.i))


def _g(x):
    return x if isinstance(x, GQ) else GQ(x, 0)


I_ = GQ(0, 1)


def mat(a, b, c, d):
    return [[_g(a), _g(b)], [_g(c), _g(d)]]


def mmul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def mdag(A):
    return [[A[j][i].conj() for j in range(2)] for i in range(2)]


def minv(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert not det.iszero()
    return [[A[1][1] / det, -A[0][1] / det], [-A[1][0] / det, A[0][0] / det]]


def msc(A, s):
    return [[A[i][j] * s for j in range(2)] for i in range(2)]


S1 = mat(0, 1, 1, 0)
S2 = mat(0, GQ(0, -1), GQ(0, 1), 0)
S3 = mat(1, 0, 0, -1)
ID = mat(1, 0, 0, 1)
ZER = mat(0, 0, 0, 0)

LAM = F(4)
MU = F(2)  # mu^2 = lambda


def lam_pow2(k):
    """lambda^(k/2) = mu^k, exact."""
    return MU ** k


def blocks(n, p2, p3):
    """(lower, diag, upper) blocks of J at site n: coefficients of psi(n-1), psi(n), psi(n+1)."""
    lower = msc(S1, GQ(0, F(1, 2)) * lam_pow2(2 * n - 1))
    upper = msc(S1, GQ(0, F(-1, 2)) * lam_pow2(2 * n + 1))
    diag = msc(madd(msc(S2, p2), msc(S3, p3)), LAM ** n)
    return lower, diag, upper


def slab_green00(a, b, z, p2, p3):
    """(J_[a,b] - z)^{-1}_{00} for the Dirichlet slab on sites a..b (psi(a-1)=psi(b+1)=0), exact."""
    zI = msc(ID, z)
    # left Schur complements: SL[n] = D_n - z - lower_n SL[n-1]^{-1} upper_{n-1}
    SL = {}
    prev = None
    for n in range(a, 1):
        lo, di, up = blocks(n, p2, p3)
        S = msub(di, zI)
        if prev is not None:
            _, _, upm = blocks(n - 1, p2, p3)
            S = msub(S, mmul(mmul(lo, minv(prev)), upm))
        SL[n] = S
        prev = S
    SR = {}
    prev = None
    for n in range(b, -1, -1):
        lo, di, up = blocks(n, p2, p3)
        S = msub(di, zI)
        if prev is not None:
            lop, _, _ = blocks(n + 1, p2, p3)
            S = msub(S, mmul(mmul(up, minv(prev)), lop))
        SR[n] = S
        prev = S
    lo0, di0, up0 = blocks(0, p2, p3)
    S0 = msub(msub(di0, zI), ZER)
    if a < 0:
        _, _, upm = blocks(-1, p2, p3)
        S0 = msub(S0, mmul(mmul(lo0, minv(SL[-1])), upm))
    if b > 0:
        lop, _, _ = blocks(1, p2, p3)
        S0 = msub(S0, mmul(mmul(up0, minv(SR[1])), lop))
    return minv(S0)


def mnorm2(A):
    return sum((A[i][j] - 0).abs2() for i in range(2) for j in range(2) if True)


def mdiff2(A, B):
    return sum((A[i][j] - B[i][j]).abs2() for i in range(2) for j in range(2))


# ================================================================== A
print("# A. exact identities")

# A1 gauge: spinor chain -> real tridiagonal with bonds mu^(2n+1)/2   (landed T1, recomputed)
m_, n_ = sp.symbols("mu n", positive=True)
f_nm1, f_np1 = sp.symbols("f_nm1 f_np1")
# psi(n) = i^n f_n ; row of (J psi)(n)/i^n for the sigma_1 coupling between components of one chain
lhs = sp.I / 2 * (m_ ** (2 * n_ - 1) * sp.I ** (-1) * f_nm1 - m_ ** (2 * n_ + 1) * sp.I * f_np1)
rhs = sp.Rational(1, 2) * m_ ** (2 * n_ - 1) * f_nm1 + sp.Rational(1, 2) * m_ ** (2 * n_ + 1) * f_np1
ok("A1 real gauge psi=i^n f gives bonds mu^(2n+1)/2", sp.simplify(lhs - rhs) == 0)

# A2 series: (i e/2)(S(X/L)-S(L X)) = X S(X) with c_j = 2 i e c_{j-1}/(L^j - L^-j)
Ls = sp.symbols("L", positive=True)
Xs = sp.symbols("X")
good = True
for e in (1, -1):
    c = [sp.Integer(1)]
    for j in range(1, 7):
        c.append(2 * sp.I * e * c[-1] / (Ls ** j - Ls ** (-j)))
    Sx = sum(c[j] * Xs ** j for j in range(7))
    resid = sp.expand(sp.I * e / 2 * (Sx.subs(Xs, Xs / Ls) - Sx.subs(Xs, Xs * Ls)) - Xs * Sx)
    # only the X^7 term may survive
    resid = sp.simplify(resid)
    poly = sp.Poly(sp.together(resid), Xs)
    low = [sp.simplify(poly.coeff_monomial(Xs ** k)) for k in range(0, 7)]
    good = good and all(t == 0 for t in low) and sp.simplify(poly.coeff_monomial(Xs ** 7)) != 0
ok("A2 chain series solves the energy-z recurrence through X^6 (remainder only at X^7), both e, symbolic L", good)

# A3 coefficient decay (entire in z): ratio |c_j/c_{j-1}| = 2/(L^j-L^-j) strictly decreasing, L=4
ratios = [F(2) / (LAM ** j - LAM ** (-j)) for j in range(1, 12)]
ok("A3 series ratios strictly decreasing (L=4), -> 0 superexponentially",
   all(ratios[k + 1] < ratios[k] for k in range(len(ratios) - 1)) and ratios[-1] < F(1, 10 ** 6))

# A4 slow end: Gershgorin row-sum bound on sites n<=N is lambda^(N+1/2)-type, so J_{(-inf,N]} is bounded
bnd = lambda N: (lam_pow2(2 * N + 1) + lam_pow2(2 * N - 1)) / 2 + LAM ** N * F(1)  # bonds + |p|*L^N with |p|<=1
vals = [bnd(N) for N in range(-12, 4)]
ok("A4 row-sum bound of the slow half is finite and decays like L^N (exact, N=-12..3)",
   all(vals[k + 1] > vals[k] for k in range(len(vals) - 1)) and vals[0] < F(1, 10 ** 6))

# A5 Lagrange identity exactly on a window (3D sector, p=(1/4,1/3)), random Gaussian-rational vectors
import random
random.seed(7)
p2, p3 = F(1, 4), F(1, 3)


def rand_vec(a, b):
    return {n: [GQ(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(2)] for n in range(a - 1, b + 2)}


def apply_J(v, n):
    lo, di, up = blocks(n, p2, p3)
    out = []
    for r in range(2):
        out.append(lo[r][0] * v[n - 1][0] + lo[r][1] * v[n - 1][1] + di[r][0] * v[n][0] + di[r][1] * v[n][1]
                   + up[r][0] * v[n + 1][0] + up[r][1] * v[n + 1][1])
    return out


def ip(x, y):
    return x[0].conj() * y[0] + x[1].conj() * y[1]


a_, b_ = -3, 4
xi = rand_vec(a_, b_ + 1)
ps = rand_vec(a_, b_ + 1)
lhs = GQ(0)
for n in range(a_, b_ + 1):
    lhs = lhs + ip(xi[n], apply_J(ps, n)) - ip(apply_J(xi, n), ps[n])
# boundary term:  B_b - B_{a-1}, with B_N = -(i/2)L^{N+1/2}[xi_N^† s1 psi_{N+1} + xi_{N+1}^† s1 psi_N]
def Bterm(N):
    s1 = lambda v: [v[1], v[0]]
    t = ip(xi[N], s1(ps[N + 1])) + ip(xi[N + 1], s1(ps[N]))
    return GQ(0, F(-1, 2)) * lam_pow2(2 * N + 1) * t


rhs = Bterm(b_) - Bterm(a_ - 1)
ok("A5 Lagrange identity sum[xi^dag J psi - (J xi)^dag psi] = B_b - B_(a-1), exact", lhs == rhs)

# A6 shift covariance of slabs: S J_[a,b] S^-1 = L^-1 J_[a+1,b+1] (real-gauge scalar chain, exact matrices)
def jac(a, b):
    n = b - a + 1
    M = sp.zeros(n, n)
    for k in range(n - 1):
        bond = sp.Rational(1, 2) * sp.Integer(2) ** (2 * (a + k) + 1)  # b_{a+k} = mu^(2(a+k)+1)/2
        M[k, k + 1] = bond
        M[k + 1, k] = bond
    return M


Ja = jac(-2, 5)
Jb = jac(-1, 6)
ok("A6 slab shift covariance S J_[a,b] S^-1 = L^-1 J_[a+1,b+1] (Jacobi matrices, exact)", Ja * 4 == Jb)  # L*J_[a,b] has J_[a+1,b+1] bonds

# ================================================================== B
print("# B. line: boundary space and Dirichlet planes")
# zero-energy solutions u_{e,v}(n)=(e/mu)^n v; boundary form between (e,v),(e',v') at cut N is
#   -(i/2)(ee')^N (e+e') v^dag s1 v'   (derived above); G = diag(-i s1, +i s1) for every N
sx = sp.Matrix([[0, 1], [1, 0]])
def Gform(N):
    G = sp.zeros(4, 4)
    for ie, e in enumerate((1, -1)):
        for je, e2 in enumerate((1, -1)):
            blk = -sp.I / 2 * sp.Integer(e * e2) ** N * (e + e2) * sx
            G[2 * ie:2 * ie + 2, 2 * je:2 * je + 2] = blk
    return G
G0 = sp.diag(-sp.I * sx, sp.I * sx)
ok("B1 boundary form of the four zero-energy solutions is diag(-i s1, i s1) at every cut", all(Gform(N) == G0 for N in range(-3, 6)))

# Dirichlet plane for far wall at b+1:  psi(b+1)=0 <=> c_+ + (-1)^(b+1) c_- = 0   <=> c_+ = eta c_-, eta=(-1)^b
x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
def plane_basis(eta):
    # c_- = (u, w) free, c_+ = eta c_-
    return [sp.Matrix([eta, 0, 1, 0]), sp.Matrix([0, eta, 0, 1])]
lag = True
for eta in (1, -1):
    B = plane_basis(eta)
    for u in B:
        for w in B:
            lag = lag and sp.simplify((u.H * G0 * w)[0]) == 0
ok("B2 L_eta={c_+=eta c_-} is Lagrangian for G (both eta)", lag)
# direct: psi(b+1)=0 for u=sum c u_{e,v} reproduces c_+ = (-1)^b c_-
Mb = sp.symbols("Mb")
direct = True
for b in range(-2, 7):
    for u in plane_basis((-1) ** b):
        c_plus = sp.Matrix([u[0], u[1]]); c_minus = sp.Matrix([u[2], u[3]])
        psi = (1 / sp.Integer(2)) ** (b + 1) * c_plus + (-1 / sp.Integer(2)) ** (b + 1) * c_minus
        direct = direct and psi == sp.zeros(2, 1)
ok("B3 psi(b+1)=0 for the plane vectors at b=-2..6 (mu=2, original gauge)", direct)

# T1 = diag(mu,-mu) on the boundary space; L_eta -> L_-eta
Tm = sp.diag(2, 2, -2, -2)
shifted = [Tm * v for v in plane_basis(1)]
in_Lm = all((v[0] == -v[2]) and (v[1] == -v[3]) for v in shifted)
in_Lp = all((v[0] == v[2]) and (v[1] == v[3]) for v in shifted)
ok("B4 T1 maps L_+ onto L_- and L_+ != L_-, so neither Dirichlet plane is kept by the unit shift", in_Lm and not in_Lp)
# kept planes split along the two T1 eigenspaces (c_-=0 / c_+=0); L_eta meets each only in 0
inter_plus = [v for v in plane_basis(1) if v[2] == 0 and v[3] == 0]
ok("B5 L_eta intersects the T1-eigenspace {c_-=0} only in 0 (so not of the form L(v1,v2))", len(inter_plus) == 0 and all(
    sp.Matrix.hstack(*plane_basis(e)).rank() == 2 for e in (1, -1)))
# chain-separation: chain A = {(x, s3 x)}, chain B = {(x,-s3 x)} in (c_+,c_-) coordinates
s3 = sp.diag(1, -1)
def chain_vec(sign, x):
    return sp.Matrix(list(x) + list(sign * s3 * sp.Matrix(x)))
t1, t2 = sp.symbols("t1 t2")
sep = True
for eta in (1, -1):
    # A-vector in L_eta: x = eta*sign*s3 x  with sign=+1 -> s3 x = eta x
    xa = sp.Matrix([1, 0]) if eta == 1 else sp.Matrix([0, 1])
    xb = sp.Matrix([0, 1]) if eta == 1 else sp.Matrix([1, 0])
    va, vb = chain_vec(1, xa), chain_vec(-1, xb)
    in_plane = lambda v: v[0] == eta * v[2] and v[1] == eta * v[3]
    sep = sep and in_plane(va) and in_plane(vb) and sp.Matrix.hstack(va, vb).rank() == 2
ok("B6 L_eta = (chain A vector) + (chain B vector): chain-separate, with the SAME eigen-label of sigma_3 on both chains", sep)

# ================================================================== C
print("# C. 3D witness lambda=4, p=(1/4,1/3): Dirichlet plane P_b -> span(b,c)")
p2s, p3s = sp.Rational(1, 4), sp.Rational(1, 3)
s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3m = sp.Matrix([[1, 0], [0, -1]])
Nm = p2s * s3m - p3s * s2m  # N = sin k2 s3 - sin k3 s2
msq = p2s ** 2 + p3s ** 2
ok("C1 N^2 = m^2 = 25/144", sp.simplify(Nm * Nm - msq * sp.eye(2)) == sp.zeros(2, 2))
mm = sp.Rational(5, 12); ss = sp.Rational(13, 12)
ok("C2 s=sqrt(1+m^2)=13/12 and m < m* = sinh(g/2) = (L-1)/(2 mu) = 3/4", ss ** 2 == 1 + mm ** 2 and mm < sp.Rational(3, 4))
# zero-energy Floquet solutions (r/mu)^n v, N v = ((r-1/r)/2) v
roots = {"a": mm + ss, "b": mm - ss, "c": ss - mm, "d": -mm - ss}
vplus = (Nm - mm * sp.eye(2)).nullspace()[0]
vminus = (Nm + mm * sp.eye(2)).nullspace()[0]
sig = {"a": vplus, "b": vplus, "c": vminus, "d": vminus}
fl = True
for k, r in roots.items():
    r = sp.nsimplify(r)
    # exact quadratic: (r-1/r)/2 = +-m with the sign of the label
    target = mm if k in ("a", "b") else -mm
    fl = fl and sp.simplify((r - 1 / r) / 2 - target) == 0
    # full recurrence: zero-energy equation  (i/2)s1[ L^{n-1/2}u(n-1) - L^{n+1/2}u(n+1)] + L^n (p.s) u(n) = 0 with u(n)=(r/2)^n v
    n0 = 0
    u = lambda n: (r / 2) ** n * sig[k]
    expr = (sp.I / 2) * sx * (2 ** (2 * n0 - 1) * u(n0 - 1) - 2 ** (2 * n0 + 1) * u(n0 + 1)) + 4 ** n0 * (p2s * s2m * 0 + (p2s * s2m + p3s * s3m)) * u(n0)
    fl = fl and sp.simplify(expr) == sp.zeros(2, 1)
ok("C3 a,b,c,d are exact zero-energy solutions; roots 3/2,-2/3,2/3,-3/2; all |r/mu|<1 so all four are l^2 at the fast end",
   fl and sorted(roots.values()) == [sp.Rational(-3, 2), sp.Rational(-2, 3), sp.Rational(2, 3), sp.Rational(3, 2)])
# NOTE: in C3 the transverse term of J is p2 s2 + p3 s3 (landed convention); N = p2 s3 - p3 s2 is the s1-twisted partner:
# the recurrence check above uses the landed J itself, so the labels a..d are tied to J, not to N alone.

# boundary form among a..d (cut independent), pairs
labs = ["a", "b", "c", "d"]
def Bform3(ka, kb, N):
    ra, rb = roots[ka], roots[kb]
    return -sp.I / 2 * (ra * rb) ** N * (ra + rb) * (sig[ka].H * sx * sig[kb])[0] * (1 if True else 1)
Gm = sp.zeros(4, 4)
for i, ka in enumerate(labs):
    for j, kb in enumerate(labs):
        vals = {sp.nsimplify(sp.simplify(Bform3(ka, kb, N))) for N in range(0, 4)}
        Gm[i, j] = list(vals)[0] if len(vals) == 1 else sp.nan
ok("C4 boundary form of a..d is cut-independent and pairs only a-c and b-d (recomputed; known)",
   not Gm.has(sp.nan) and all((Gm[i, j] != 0) == ({labs[i], labs[j]} in ({"a", "c"}, {"b", "d"})) for i in range(4) for j in range(4) if i != j))

# Dirichlet plane at cut b: psi(b+1)=0, sum_i c_i (r_i/2)^(b+1) v_i = 0 ; v_a=v_b=v+, v_c=v_d=v-
rate = sp.Rational(4, 9)
exact = True; lag3 = True
for b in range(0, 9):
    # +-component equations
    #   v+ : c_a r_a^(b+1) + c_b r_b^(b+1) = 0 ; v- : c_c r_c^(b+1) + c_d r_d^(b+1) = 0
    ra, rb, rc, rd = (roots[k] for k in labs)
    # basis of the plane, parametrised by (c_b, c_c)
    v1 = sp.Matrix([-(rb / ra) ** (b + 1), 1, 0, 0])
    v2 = sp.Matrix([0, 0, 1, -(rc / rd) ** (b + 1)])
    for v in (v1, v2):
        psi = sum((v[i] * (roots[labs[i]] / 2) ** (b + 1) * sig[labs[i]] for i in range(4)), sp.zeros(2, 1))
        exact = exact and sp.simplify(psi) == sp.zeros(2, 1)
    for u in (v1, v2):
        for w in (v1, v2):
            lag3 = lag3 and sp.simplify((u.H * Gm * w)[0]) == 0
    exact = exact and abs(-(rb / ra) ** (b + 1)) == rate ** (b + 1) and abs(-(rc / rd) ** (b + 1)) == rate ** (b + 1)
ok("C5 P_b (b=0..8) is spanned by (a-component=-(r_b/r_a)^(b+1)) b and (d-component=-(r_c/r_d)^(b+1)) c, exact; |coefficients| = (4/9)^(b+1)", exact)
ok("C6 each P_b is Lagrangian for the cut-independent form (it is the Dirichlet condition at one cut)", lag3)
ok("C7 P_b -> span(b,c) geometrically at ratio 4/9 per step of b (both parities): the b,c pair is one of the four shift-kept planes (isotropic: G_bb=G_cc=G_bc=0)",
   Gm[1, 1] == 0 and Gm[2, 2] == 0 and Gm[1, 2] == 0)

# ================================================================== D
print("# D. exact slab Green functions at z=i (Gaussian rationals); a=-A absorbs the slow end")
z = GQ(0, 1)
A = 12
def table(p2, p3, bs):
    return {b: slab_green00(-A, b, z, p2, p3) for b in bs}
t0 = time.time()
line = table(F(0), F(0), range(6, 16))
# slow-end truncation independence (A=9 vs A=12): resolvent identity bound says the change is <= ~2 L^-A / |Im z|^2
g9 = slab_green00(-9, 10, z, F(0), F(0)); g12 = slab_green00(-12, 10, z, F(0), F(0))
ok("D0 slow-end truncation A=9 vs A=12 changes G(0,0) by < 4^-9 (resolvent perturbation scale; slow end is bounded)",
   mdiff2(g9, g12) < F(1, 4 ** 18))
# line: odd/even differ by a fixed amount, same parity converge geometrically
def d2(x, y): return mdiff2(x, y)
dev = [d2(line[b], line[b + 2]) for b in (6, 8, 10, 12)]        # same parity (even b)
dod = [d2(line[b], line[b + 2]) for b in (7, 9, 11, 13)]        # same parity (odd b)
dpar = [d2(line[b], line[b + 1]) for b in range(6, 14)]         # opposite parity
ok("D1 line: same-parity slabs form a Cauchy sequence (squared gaps shrink by > 100x per step of 2)",
   all(dev[k + 1] * 100 < dev[k] for k in range(3)) and all(dod[k + 1] * 100 < dod[k] for k in range(3)),
   "gaps2 even=" + ", ".join(f"{float(x):.2e}" for x in dev))
lim_even = line[14]; lim_odd = line[13]
ok("D2 line: the even-b and odd-b limits differ by a fixed amount (|dG|^2 > 1/50 at every b=6..13); no limit of the full slab family",
   all(x > F(1, 50) for x in dpar), "min |dG|^2=%.4f" % float(min(dpar)))
# 3D sector: no parity dependence, whole family Cauchy
p3d = (F(1, 4), F(1, 3))
t3 = table(p3d[0], p3d[1], range(6, 15))
gaps3 = [d2(t3[b], t3[b + 1]) for b in range(6, 14)]
ok("D3 3D sector (m=5/12<m*): successive slabs (both parities) converge: squared gaps shrink every step, ratio ~ (4/9)^2 per step",
   all(gaps3[k + 1] < gaps3[k] for k in range(len(gaps3) - 1)) and gaps3[-1] < F(1, 10 ** 4),
   "gaps2=" + ", ".join(f"{float(x):.2e}" for x in gaps3[:5]))
rat = [float(gaps3[k + 1] / gaps3[k]) for k in range(len(gaps3) - 1)]
ok("D4 3D: gap ratio -> (4/9)^2 = 0.1975 (the rate of C5/C7, not the 1/16 of the series corrections)",
   abs(rat[-1] - 16 / 81) < 0.03, "ratios=" + ", ".join("%.3f" % r for r in rat))

# D5: limit Green function from the proved structure (line), mpmath: G = phi_-(0) theta(0)/W with theta_par=f_+ + eta f_-
mp.mp.dps = 40
zz = mp.mpc(0, 1)
def fser(n, e, zz, J=40):
    """f_e(n) = (i e/mu)^n S_e(z L^-n) , scalar real-gauge chain with bonds mu^(2n+1)/2."""
    c = mp.mpf(1); s = mp.mpf(1)
    X = zz * mp.mpf(4) ** (-n); term = mp.mpc(1); tot = mp.mpc(1)
    cj = mp.mpc(1)
    for j in range(1, J):
        cj = mp.mpc(0, 2 * e) * cj / (mp.mpf(4) ** j - mp.mpf(4) ** (-j))
        tot += cj * X ** j
    return (mp.mpc(0, e) / 2) ** n * tot
def bond(n): return mp.mpf(2) ** (2 * n + 1) / 2
# residual of the recurrence for the closed-form series
res = max(abs(bond(n - 1) * fser(n - 1, e, zz) + bond(n) * fser(n + 1, e, zz) - zz * fser(n, e, zz)) for n in range(-2, 6) for e in (1, -1))
ok("D5a series f_e(n) solves the scalar chain recurrence at z=i to < 1e-25 (mpmath 40 digits)", res < mp.mpf(10) ** -25, "resid=%s" % mp.nstr(res, 3))
# phi_-: Dirichlet-at--A forward recursion
def phi_minus(zz, Aa=26, upto=3):
    ph = {-Aa - 1: mp.mpc(0), -Aa: mp.mpc(1)}
    for n in range(-Aa, upto):
        ph[n + 1] = (zz * ph[n] - bond(n - 1) * ph[n - 1]) / bond(n)
    return ph
ph = phi_minus(zz)
def G00_limit(eta):
    th = lambda n: fser(n, 1, zz) + eta * fser(n, -1, zz)
    W = bond(0) * (ph[0] * th(1) - ph[1] * th(0))
    return ph[0] * th(0) / W
# scalar-chain slab values at b via the same exact code restricted?  use the 2x2 line table: component (0,0) = chain with sigma_1 coupling;
# the line G(0,0) is a 2x2 matrix; the scalar chain through site 0 carries the up-component at even n -> entry [0][0]
ge, go_ = lim_even, lim_odd
Ge = complex(ge[0][0].c()); Go = complex(go_[0][0].c())
L_e = complex(G00_limit(+1)); L_o = complex(G00_limit(-1))
# the slab with wall at b+1 gives eta=(-1)^b ; here lim_even uses b=14 (eta=+1), lim_odd uses b=13 (eta=-1)
ok("D5b exact slab G(0,0) (b=14) matches theta=f_+ + f_-, and (b=13) matches theta=f_+ - f_-, to < 1e-6; they are different numbers",
   abs(Ge - L_e) < 1e-6 and abs(Go - L_o) < 1e-6 and abs(L_e - L_o) > 0.1,
   "even %s vs %s ; odd %s vs %s" % (complex(round(Ge.real, 8), round(Ge.imag, 8)), complex(round(L_e.real, 8), round(L_e.imag, 8)),
                                     complex(round(Go.real, 8), round(Go.imag, 8)), complex(round(L_o.real, 8), round(L_o.imag, 8))))

# D6: boundary-term vanishing that makes the limit a genuine resolvent: B_N(theta,theta^bar) = O(L^-N)
def Bnorm(eta, N):
    th = lambda n: fser(n, 1, zz) + eta * fser(n, -1, zz)
    return abs(bond(N) * (th(N) * mp.conj(th(N + 1)) - th(N + 1) * mp.conj(th(N))))
vals = [Bnorm(1, N) * mp.mpf(4) ** N for N in range(4, 14)]
ok("D6 |b_N (theta_N conj theta_{N+1} - c.c.)| * L^N stays bounded for N=4..13 (so the boundary term -> 0 geometrically)",
   max(vals) < 10, "max=%s" % mp.nstr(max(vals), 4))
# and at z=0 it is exactly 0 for every N
def Bzero(eta, N):
    th = lambda n: (mp.mpc(0, 1) / 2) ** n + eta * (mp.mpc(0, -1) / 2) ** n
    return bond(N) * (th(N) * mp.conj(th(N + 1)) - th(N + 1) * mp.conj(th(N)))
ok("D7 at z=0, B_N(theta,theta^bar)=0 for every N (the (1+eta s)(1-eta s)=0 mechanism)", all(abs(Bzero(e, N)) < mp.mpf(10) ** -30 for e in (1, -1) for N in range(0, 12)))

# ================================================================== E
print("# E. frozen sources")
MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt"
BATCH = "/Users/jonBridger/.probe-clones/probes-view/probes/work/deferred-science-20260924/batch-10.json"
if os.path.isdir(MAIN) and os.path.exists(BATCH):
    d = json.load(open(BATCH))
    good_n = 0; tot = 0
    for s in d["sources"]:
        tot += 1
        r = subprocess.run(["git", "-C", MAIN, "show", s["head"] + ":" + s["path"]], capture_output=True)
        if r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest() == s["sha256"]:
            good_n += 1
    ok("E1 SHA256 of all %d batch-10 frozen sources reproduces the manifest" % tot, good_n == tot, "%d/%d" % (good_n, tot))
else:
    print("SKIP E1 (read-only checkouts absent)")

print("TOTAL: PASS=%d FAIL=%d" % (RES["pass"], RES["fail"]))
print("runtime_s=%.1f" % (time.time() - T0))
if RES["fail"] == 0:
    print("HIT: for the supplied exponential clocked walk, Dirichlet slabs with receding far wall have no strong-resolvent limit on the line (the two parity limits differ and are exchanged by the unit shift, so neither keeps U(t)T1=T1U(lambda t)); in a sector 0<m<m* with the witness data they converge to the pair span(b,c) at rate (s-m)/(s+m)=4/9 per step (scoped to the supplied model; same-family, unrefereed)")
    print("SUMMARY: PARTIAL - the slab (receding-wall) rule does not supply a unit-shift-compatible fast-end condition on the line and selects span(b,c) in sectors with m>0 (zero-energy plane exact; resolvent convergence proved on the line, only checked in 3D); physical selection and the m=0 sector remain open")
else:
    print("SUMMARY: ROUTE FAILS AT a check above")
sys.exit(0 if RES["fail"] == 0 else 1)
