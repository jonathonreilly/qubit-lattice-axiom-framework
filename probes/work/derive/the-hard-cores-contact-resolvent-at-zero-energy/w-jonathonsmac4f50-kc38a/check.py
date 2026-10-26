#!/usr/bin/env python3
"""Contact resolvent of the hard core at zero energy (walk h(k)=sum_a sigma_a sin k_a, one record per site,
antisymmetric pairs).  Sections:
  A  exact symbolic / rational facts   (sympy, Fractions)           -> labelled EXACT
  B  float64 numerical facts            (numpy / mpmath)              -> labelled NUM
Every line starts with PASS or FAIL.  No HIT is printed unless the exact section supports it (see end)."""
import sys, time, itertools, random
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp
from sympy.physics.quantum import TensorProduct as TP

T0 = time.time()
PASS = FAIL = 0
EXACT_OK = True


def chk(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS", label, detail)
    else:
        FAIL += 1
        print("FAIL", label, detail)
    return ok


# ------------------------------------------------------------------ A. exact
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
I2 = sp.eye(2)
s_sing = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)          # coincident singlet (constant in q-space)
z = sp.symbols('z')
a = sp.symbols('a1 a2 a3', real=True)                    # u1 = (sin q_a)       record 1
b = sp.symbols('b1 b2 b3', real=True)                    # u2 = (sin(K_a-q_a))  record 2
h1 = sum((a[i] * sig[i] for i in range(3)), sp.zeros(2))
h2 = sum((b[i] * sig[i] for i in range(3)), sp.zeros(2))
h0 = TP(h1, I2) + TP(I2, h2)                              # fibre generator h0(q;K) at one q
A2 = sum(x * x for x in a)
B2 = sum(x * x for x in b)
dd = sum(x * y for x, y in zip(a, b))
S = A2 + B2 - z ** 2
fnum = z * (S + 2 * dd)
fden = S ** 2 - 4 * A2 * B2                                # closed form g = fnum/fden

# A1: closed form of the singlet matrix element of the free pair resolvent, polynomial identity
M = (h0 - z * sp.eye(4)).applyfunc(sp.expand)
det = sp.expand(M.det(method='berkowitz'))
num = sp.expand((s_sing.T * M.adjugate(method='berkowitz') * s_sing)[0])
chk("A1 EXACT  det(h0-z)=S^2-4A^2B^2 and s^T adj(h0-z) s = z(S+2u1.u2) as polynomials in (u1,u2,z)",
    sp.expand(det - fden) == 0 and sp.expand(num - fnum) == 0)
# hence s^T (h0-z)^-1 s = z (A^2+B^2-z^2+2 u1.u2)/((A^2+B^2-z^2)^2-4A^2B^2)  wherever det != 0

# A2: pointwise oddness in z (follows from A1) and the antiunitary explanation
chk("A2 EXACT  g(-z) = -g(z) pointwise in q (substitute z->-z in the closed form)",
    sp.simplify((fnum / fden).subs(z, -z) + fnum / fden) == 0)
iSy = sp.Matrix([[0, 1], [-1, 0]])                          # i*sigma_y
Th = TP(iSy, iSy)                                           # Theta = Th * complex-conjugation
lhs = Th * h0.conjugate() * Th.inv()
chk("A2b EXACT chiral antiunitary Theta=(i sy x i sy)K: Theta h0 Theta^-1 = -h0 for real u1,u2",
    sp.simplify(lhs + h0) == sp.zeros(4))
chk("A2c EXACT Theta fixes the coincident singlet: (i sy x i sy) conj(s) = s",
    sp.simplify(Th * s_sing.conjugate() - s_sing) == sp.zeros(4, 1))

# A3: the supervisor's staggered-sign route:  q -> q+Pi sends h0(q;K) -> -h0(q;K), K fixed
qs = sp.symbols('q1 q2 q3', real=True)
Ks = sp.symbols('K1 K2 K3', real=True)
u1q = [sp.sin(x) for x in qs]
u2q = [sp.sin(Kx - x) for Kx, x in zip(Ks, qs)]
u1s = [sp.sin(x + sp.pi) for x in qs]
u2s = [sp.sin(Kx - (x + sp.pi)) for Kx, x in zip(Ks, qs)]
chk("A3 EXACT  staggered sign: u1(q+Pi)=-u1(q), u2(q+Pi;K)=-u2(q;K) => h0(q+Pi)=-h0(q); c fixed; fibre K unchanged",
    all(sp.simplify(x + y) == 0 for x, y in zip(u1s, u1q)) and all(sp.simplify(x + y) == 0 for x, y in zip(u2s, u2q)))

# A4: K = 0
g_K0 = sp.simplify((fnum / fden).subs({b[0]: -a[0], b[1]: -a[1], b[2]: -a[2]}))
chk("A4 EXACT  K=0 (u2=-u1): g(z;q) = z/(4 eps^2 - z^2)  with eps^2=sum a_i^2",
    sp.simplify(g_K0 - z / (4 * A2 - z ** 2)) == 0)
# (+,-) weights (1+c)/4 = (A B + u1.u2)/(4AB) vanish at K=0:
chk("A4b EXACT K=0: A*B + u1.u2 = 0 identically, so the (+,-) overlaps (1+c)/4 vanish",
    sp.simplify((sp.sqrt(A2) * sp.sqrt(B2) + dd).subs({b[0]: -a[0], b[1]: -a[1], b[2]: -a[2]})) == 0)

# A5: exact rational tori L=4, L=6 (all sines are 0,+-1 resp. 0,+-sqrt3/2; every needed product is rational)
def torus_G(L, m, zval):
    sint = {4: [0, 1, 0, -1], 6: [0, 1, 1, 0, -1, -1]}[L]
    f2 = {4: Fr(1), 6: Fr(3, 4)}[L]                         # (unit)^2
    tot = Fr(0)
    for q in itertools.product(range(L), repeat=3):
        u1 = [sint[x] for x in q]
        u2 = [sint[(m[i] - q[i]) % L] for i in range(3)]
        A2_ = f2 * sum(x * x for x in u1)
        B2_ = f2 * sum(x * x for x in u2)
        d_ = f2 * sum(x * y for x, y in zip(u1, u2))
        Sv = A2_ + B2_ - zval * zval
        tot += zval * (Sv + 2 * d_) / (Sv * Sv - 4 * A2_ * B2_)
    return tot / L ** 3

okodd = True
cnt = 0
for L in (4, 6):
    for m in itertools.product(range(L), repeat=3):
        for zv in (Fr(1, 3), Fr(7, 5)):
            try:
                g1 = torus_G(L, m, zv)
                g2 = torus_G(L, m, -zv)
            except ZeroDivisionError:
                continue
            cnt += 1
            okodd &= (g1 + g2 == 0)
chk("A5 EXACT  G_cc(-z)=-G_cc(z) exactly (Fractions) on the L=4 and L=6 tori, every fibre K, two z each", okodd, f"({cnt} cases)")

# A5b: matrix resolvent vs closed form on actual L=4 lattice points (exact 4x4 rational solve)
okm = True
for q, m in [((0, 1, 2), (1, 0, 3)), ((1, 1, 3), (2, 2, 0)), ((3, 1, 0), (0, 0, 0)), ((1, 2, 1), (1, 1, 1))]:
    sint = [0, 1, 0, -1]
    u1 = [sint[x] for x in q]
    u2 = [sint[(m[i] - q[i]) % 4] for i in range(3)]
    sub = {a[i]: u1[i] for i in range(3)}
    sub.update({b[i]: u2[i] for i in range(3)})
    zv = sp.Rational(3, 7)
    Mn = (h0 - zv * sp.eye(4)).subs(sub)
    val = sp.simplify((s_sing.T * Mn.LUsolve(s_sing))[0])
    form = (fnum / fden).subs(sub).subs(z, zv)
    okm &= (sp.simplify(val - form) == 0)
chk("A5b EXACT  exact 4x4 rational resolvent equals closed form at L=4 lattice points", okm)

# A5c: accidental zero-energy pair states on small tori: z*G(z) -> residue at z=0 (K=0): the 8 corner q have A=B=0
def torus_residue_K0(L):
    sint = {4: [0, 1, 0, -1], 6: [0, 1, 1, 0, -1, -1]}[L]
    n_corner = sum(1 for q in itertools.product(range(L), repeat=3) if all(sint[x] == 0 for x in q))
    return Fr(-n_corner, L ** 3)
zz = sp.symbols('zz')
resid_ok = True
for L in (4, 6):
    sint = {4: [0, 1, 0, -1], 6: [0, 1, 1, 0, -1, -1]}[L]
    f2 = {4: sp.Integer(1), 6: sp.Rational(3, 4)}[L]
    G = 0
    # group identical (A2) values: at K=0, g = z/(4A2 - z^2) except corner points A2=0 where g = -1/z
    from collections import Counter
    cc = Counter()
    for q in itertools.product(range(L), repeat=3):
        cc[f2 * sum(sint[x] ** 2 for x in q)] += 1
    for A2v, mult in cc.items():
        G += mult * (zz / (4 * A2v - zz ** 2) if A2v != 0 else -1 / zz)
    G = G / L ** 3
    res = sp.limit(zz * G, zz, 0)
    resid_ok &= (sp.Rational(res) == sp.Rational(torus_residue_K0(L).numerator, torus_residue_K0(L).denominator))
chk("A5c EXACT  torus K=0 has a pole z*G -> -(8/L^3) at z=0 (L=4: -1/8, L=6: -1/27) from corner pairs: finite-volume artefact", resid_ok)

# A6: prolate spheroidal geometry of the corner shell (leading order in small offsets)
Kk, xi, eta, phi = sp.symbols('K xi eta phi', positive=True)
xpar = Kk * xi * eta / 2
xperp = (Kk / 2) * sp.sqrt((xi ** 2 - 1) * (1 - eta ** 2))
# offsets of the two records:  d1 = x + K/2,  d2 = K/2 - x   (x = relative offset about the midpoint)
r1sq = (xpar + Kk / 2) ** 2 + xperp ** 2
r2sq = (xpar - Kk / 2) ** 2 + xperp ** 2
chk("A6a EXACT  r1=|d1|=K(xi+eta)/2 and r2=|d2|=K(xi-eta)/2 in these coordinates",
    sp.simplify(r1sq - (Kk * (xi + eta) / 2) ** 2) == 0 and sp.simplify(r2sq - (Kk * (xi - eta) / 2) ** 2) == 0)
rho_ = sp.symbols('rho', positive=True)
J = sp.Matrix([[sp.diff(xpar, xi), sp.diff(xpar, eta)], [sp.diff(xperp, xi), sp.diff(xperp, eta)]]).det()
chk("A6b EXACT  d^3x = x_perp dx_par dx_perp dphi = (K^3/8)(xi^2-eta^2) dxi deta dphi",
    sp.simplify(xperp * J + (Kk ** 3 / 8) * (xi ** 2 - eta ** 2)) == 0 or sp.simplify(xperp * J - (Kk ** 3 / 8) * (xi ** 2 - eta ** 2)) == 0)
# singlet weight (1-c)/4 with c = n1.n2 = d1.(K-d1)/(r1 r2)  (u1~d1, u2~K-d1=d2 up to the common corner sign)
d1dotd2 = (xpar + Kk / 2) * (Kk / 2 - xpar) - xperp ** 2
r1 = Kk * (xi + eta) / 2
r2 = Kk * (xi - eta) / 2
cexpr = d1dotd2 / (r1 * r2)
chk("A6c EXACT  (1-c) = 2(xi^2-1)/(xi^2-eta^2)  so weight (1-c)/4 * Jacobian = (K^3/16)(xi^2-1): uniform in (eta,phi)",
    sp.simplify(1 - cexpr - 2 * (xi ** 2 - 1) / (xi ** 2 - eta ** 2)) == 0)
E_ = sp.symbols('E', positive=True)
xi0 = E_ / Kk
# direct: integral over shell delta(E-K xi): int dxi delta(E-K xi) -> 1/K at xi0
shell_int = (Kk ** 3 / 16) * (xi0 ** 2 - 1) * 2 * 2 * sp.pi / Kk
rho_c = sp.simplify(8 / (2 * sp.pi) ** 3 * shell_int)
chk("A6d EXACT  rho_c(E;K) = (E^2-K^2)/(4 pi^2) for E>K (8 corners, leading order);  K->0 gives E^2/(4 pi^2)",
    sp.simplify(rho_c - (E_ ** 2 - Kk ** 2) / (4 * sp.pi ** 2)) == 0)
mpar2 = sp.integrate((xpar ** 2).subs(xi, xi0) / 2, (eta, -1, 1))
mperp2 = sp.integrate((xperp ** 2).subs(xi, xi0) / 2, (eta, -1, 1))
chk("A6e EXACT  uniform-in-eta shell means: <x_par^2>=E^2/12, <x_perp^2>=(E^2-K^2)/6",
    sp.simplify(mpar2 - E_ ** 2 / 12) == 0 and sp.simplify(mperp2 - (E_ ** 2 - Kk ** 2) / 6) == 0)
xx, Kc = sp.symbols('x Kc', real=True)
chk("A6f EXACT  (K/2+x)^3+(K/2-x)^3 = K^3/4 + 3 K x^2  (so Delta g_a = -2 K_a (<x_a^2> - x_a^2); block 152 T3(b) family)",
    sp.expand((Kc / 2 + xx) ** 3 + (Kc / 2 - xx) ** 3 - (Kc ** 3 / 4 + 3 * Kc * xx ** 2)) == 0)
# the sum of cubes equals K^3-3K^2 p+3 K p^2 (no p^3) for p=K/2+x:
pp = sp.symbols('p', real=True)
chk("A6g EXACT  p^3+(K-p)^3 = K^3 - 3K^2 p + 3K p^2 (the odd p^3 cancels)",
    sp.expand(pp ** 3 + (Kc - pp) ** 3 - (Kc ** 3 - 3 * Kc ** 2 * pp + 3 * Kc * pp ** 2)) == 0)

# A7: exact inequality used for the lower bound  (zeta^2-a)/(zeta^2-b) >= 1-a for zeta>=1, 0<=b<=a<=1
za, aa, ba = sp.symbols('zeta a b', real=True)
chk("A7 EXACT  (zeta^2-a)-(1-a)(zeta^2-b) = a(zeta^2-1)+b(1-a) >= 0 for zeta>=1, 0<=b<=a<=1",
    sp.expand((za ** 2 - aa) - (1 - aa) * (za ** 2 - ba) - (aa * (za ** 2 - 1) + ba * (1 - aa))) == 0)
# A7b: <sin^2 q_a/(4 eps^2)> = 1/12: sum over a of sin^2/eps^2 = 1 and the three axes are permuted by the cubic symmetry
chk("A7b EXACT  sum_a sin^2 q_a / eps^2 = 1 (three equal means by axis permutation => each 1/3)",
    sp.simplify(sum(sp.sin(x) ** 2 for x in qs) / sum(sp.sin(x) ** 2 for x in qs)) == 1)

# A8: K != 0 forbids the exact vanishing of all (+,-) overlaps; flat (+,-) band at K in {0,pi}^3 \ {0}
# overlap (1+c) A B = AB + u1.u2 ; vanishes for every q iff u2 = -u1 iff sin(K_a-q_a) = -sin q_a for all q_a iff K_a = 0 (mod 2pi)
qa, Ka = sp.symbols('qa Ka', real=True)
expr = sp.sin(Ka - qa) + sp.sin(qa)
chk("A8 EXACT  sin(K-q)+sin q = 2 sin(K/2) cos(K/2-q): identically 0 in q iff sin(K/2)=0, i.e. K=0 mod 2pi: the (+,-) overlaps vanish identically only at K=0",
    sp.simplify(expr - 2 * sp.sin(Ka / 2) * sp.cos(Ka / 2 - qa)) == 0)
chk("A8b EXACT  eps^2(q)-eps^2(K-q) = sum_a sin K_a sin(2q_a-K_a):  (+,-) energy zero locus; all K_a in {0,pi} => identically flat zero band",
    sp.simplify(sum(sp.sin(x) ** 2 - sp.sin(Kx - x) ** 2 - sp.sin(Kx) * sp.sin(2 * x - Kx) for Kx, x in zip(Ks, qs))) == 0)

print("-- exact section done at %.1fs" % (time.time() - T0))

# ------------------------------------------------------------------ B. numerical
# B1 real-space check on the L=3 torus that the fibre momentum-space formula is the contact resolvent of
#    the free two-record generator H (x) 1 + 1 (x) H  (float64)
L = 3
sg = [np.array(m.tolist(), dtype=complex) for m in sig]
sites = list(itertools.product(range(L), repeat=3))
idx = {s_: i for i, s_ in enumerate(sites)}
V = len(sites)


def shift(ax, sgn):
    Mx = np.zeros((V, V))
    for s_ in sites:
        t = list(s_)
        t[ax] = (t[ax] + sgn) % L
        Mx[idx[tuple(t)], idx[s_]] = 1
    return Mx


Hs = sum(np.kron((shift(ax, 1) - shift(ax, -1)) / (2j), sg[ax]) for ax in range(3))
nn = 2 * V
H2 = np.kron(Hs, np.eye(nn)) + np.kron(np.eye(nn), Hs)
s_num = np.array([0, 1, -1, 0], complex) / np.sqrt(2)


def cK(Kv):
    v = np.zeros(nn * nn, complex)
    for x in sites:
        ph = np.exp(1j * sum(Kv[i] * x[i] for i in range(3))) / np.sqrt(V)
        i = idx[x]
        for c1 in range(2):
            for c2 in range(2):
                v[(2 * i + c1) * nn + (2 * i + c2)] += ph * s_num[2 * c1 + c2]
    return v


def Gcc_real(Kv, zv):
    c = cK(Kv)
    return np.vdot(c, np.linalg.solve(H2 - zv * np.eye(nn * nn), c))


def Gcc_mom(Kv, zv):
    tot = 0
    for q in itertools.product(2 * np.pi * np.arange(L) / L, repeat=3):
        u1 = np.sin(q)
        u2 = np.sin(np.array(Kv) - np.array(q))
        h = np.kron(sum(u1[i] * sg[i] for i in range(3)), np.eye(2)) + np.kron(np.eye(2), sum(u2[i] * sg[i] for i in range(3)))
        tot += np.vdot(s_num, np.linalg.solve(h - zv * np.eye(4), s_num))
    return tot / V


worst = 0
for m in [(0, 0, 0), (1, 0, 0), (1, 2, 0), (1, 1, 1)]:
    Kv = [2 * np.pi * mm / L for mm in m]
    for zv in (0.37 + 0.2j, -0.37 + 0.2j):
        worst = max(worst, abs(Gcc_real(Kv, zv) - Gcc_mom(Kv, zv)))
chk("B1 NUM    real-space L=3 torus: <c_K|(H(x)1+1(x)H - z)^-1|c_K> equals the fibre formula (max residual %.1e)" % worst, worst < 1e-10)

# B2 band weights: singlet overlap with band pair (s1,s2) is (1 - s1 s2 n1.n2)/4
rng = np.random.default_rng(7)
okw = True
for _ in range(20):
    u1 = rng.normal(size=3)
    u2 = rng.normal(size=3)
    h = np.kron(sum(u1[i] * sg[i] for i in range(3)), np.eye(2)) + np.kron(np.eye(2), sum(u2[i] * sg[i] for i in range(3)))
    w, v = np.linalg.eigh(h)
    A_, B_ = np.linalg.norm(u1), np.linalg.norm(u2)
    c_ = u1 @ u2 / (A_ * B_)
    pred = sorted([(s1 * A_ + s2 * B_, (1 - s1 * s2 * c_) / 4) for s1 in (1, -1) for s2 in (1, -1)])
    for k in range(4):
        okw &= abs(w[k] - pred[k][0]) < 1e-12 and abs(abs(v[:, k].conj() @ s_num) ** 2 - pred[k][1]) < 1e-12
chk("B2 NUM    singlet overlap with band pair (s1,s2) is (1-s1 s2 n1.n2)/4 (random vectors)", okw)

# B3 K=0: C0 = <1/(4 eps^2)> = W3/6 with W3 the simple-cubic Watson integral; G(E)/E -> C0
Wclosed = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)


def mean_inv_eps2(N):
    q = 2 * np.pi * (np.arange(N) + 0.5) / N
    s2 = np.sin(q) ** 2
    tot = 0.0
    for i in range(N):
        tot += (1.0 / (s2[i] + s2[:, None] + s2[None, :])).sum()
    return tot / N ** 3


v1, v2 = mean_inv_eps2(128), mean_inv_eps2(256)
ext = 2 * v2 - v1                                           # midpoint rule, 1/N error from the 1/q^2 corner singularities
C0_num = ext / 4
C0 = float(Wclosed) / 6
chk("B3 NUM    C0=<1/(4 eps^2)> = W3/6 = %.6f (W3=int 1/(1-(1/3)sum cos) Watson closed form %.10f); lattice midpoint extrapolation %.5f" % (C0, float(Wclosed), C0_num),
    abs(C0_num - C0) < 2e-3 and abs(float(Wclosed) - 1.5163860592) < 1e-9)

# B4 density of states at K=0: rho_c(E)=E^2/(4 pi^2): count of {sum sin^2 p <= E^2/4} near one corner
def corner_volume(Ecut, h=0.004):
    pmax = Ecut / 2 * 1.3
    g_ = np.arange(-pmax, pmax + h / 2, h)
    X, Y, Zg = np.meshgrid(g_, g_, g_, indexing='ij')
    inside = (np.sin(X) ** 2 + np.sin(Y) ** 2 + np.sin(Zg) ** 2) <= Ecut ** 2 / 4
    return inside.sum() * h ** 3 / (2 * np.pi) ** 3 * 8


E1, E2 = 0.30, 0.34
rho_est = 0.5 * (corner_volume(E2) - corner_volume(E1)) / (E2 - E1)       # weight (1-c)/4=1/2, derivative of the volume
rho_pred = ((E1 + E2) / 2) ** 2 / (4 * np.pi ** 2)
chk("B4 NUM    K=0 contact density rho_c(E)=E^2/(4 pi^2) on the exact lattice dispersion: estimate %.5f vs %.5f" % (rho_est, rho_pred),
    abs(rho_est / rho_pred - 1) < 0.04)

# B5 exact lattice G vs leading-order form  G_lead(z;K) = z < (z^2-|w|^2)/(4 eps^2 (z^2-(K.v)^2)) >,  w_a=K_a cos q_a, v=grad eps
def G_exact(zv, Kv, N):
    q = 2 * np.pi * (np.arange(N) + 0.5) / N
    Y, Zg = np.meshgrid(q, q, indexing='ij')
    tot = 0j
    for qx in q:
        u1 = [np.sin(qx) * np.ones_like(Y), np.sin(Y), np.sin(Zg)]
        u2 = [np.sin(Kv[0] - qx) * np.ones_like(Y), np.sin(Kv[1] - Y), np.sin(Kv[2] - Zg)]
        A2_ = sum(x * x for x in u1)
        B2_ = sum(x * x for x in u2)
        d_ = sum(x * y for x, y in zip(u1, u2))
        Sv = A2_ + B2_ - zv * zv
        tot += (zv * (Sv + 2 * d_) / (Sv * Sv - 4 * A2_ * B2_)).sum()
    return tot / N ** 3


def G_lead(zv, Kv, N):
    q = 2 * np.pi * (np.arange(N) + 0.5) / N
    Y, Zg = np.meshgrid(q, q, indexing='ij')
    tot = 0j
    for qx in q:
        u = [np.sin(qx) * np.ones_like(Y), np.sin(Y), np.sin(Zg)]
        co = [np.cos(qx) * np.ones_like(Y), np.cos(Y), np.cos(Zg)]
        e2 = sum(x * x for x in u)
        w2 = sum((Kv[i] * co[i]) ** 2 for i in range(3))
        Kv_ = sum(Kv[i] * u[i] * co[i] for i in range(3)) / np.sqrt(e2)
        tot += (zv * (zv * zv - w2) / (4 * e2 * (zv * zv - Kv_ ** 2))).sum()
    return tot / N ** 3


errs = {}
for kap in (0.4, 0.2, 0.1):
    for zeta in (1.5, 3.0):
        zv = kap * (zeta + 0.5j)
        ge = G_exact(zv, (kap, 0, 0), 160)
        gl = G_lead(zv, (kap, 0, 0), 160)
        errs[(kap, zeta)] = abs(ge - gl) / kap
r15 = errs[(0.1, 1.5)] / errs[(0.2, 1.5)]
r30 = errs[(0.1, 3.0)] / errs[(0.2, 3.0)]
chk("B5 NUM    |G_exact-G_lead|/K halves when K halves (error O(K^2) absolute): ratios %.2f (zeta=1.5), %.2f (zeta=3)" % (r15, r30),
    0.35 < r15 < 0.65 and 0.35 < r30 < 0.65)
chk("B5b NUM   at K=0.1, zeta=1.5 the leading form already agrees to %.3f of |G|/K" % errs[(0.1, 1.5)], errs[(0.1, 1.5)] < 0.03)

# B6 leading-order real part for E>|K| along K=(1,0,0): Re G_lead/E between 1/12 and C0, increasing with E/K
zetas = (1.0001, 1.2, 2.0, 4.0, 10.0)
vals = []
for zt in zetas:
    a1 = G_lead(zt + 0j, (1.0, 0, 0), 128).real
    a2 = G_lead(zt + 0j, (1.0, 0, 0), 256).real
    vals.append((2 * a2 - a1) / zt)
chk("B6 NUM    Re G_lead(E)/E for zeta=E/K=" + ",".join("%g" % x for x in zetas) + ": " + ", ".join("%.4f" % x for x in vals)
    + "  (all >= 1/12=0.0833 and <= C0=%.4f, increasing)" % C0,
    all(v >= 1 / 12 - 1e-3 for v in vals) and all(v <= C0 + 2e-3 for v in vals) and all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)))

# B7 at fixed K, E -> 0 the leading-order amplitude saturates:  Im G_lead(i gamma K)/K -> pi J > 0 (K || x)
im = [(G_lead(1j * gm, (1.0, 0, 0), 256)).imag for gm in (0.2, 0.1, 0.05)]
chk("B7 NUM    Im G_lead(i*gamma*K)/K = %s for gamma=0.2,0.1,0.05: tends to a positive constant (about 0.31), so |G(0+i0;K)| ~ 0.31 |K| and the E=0 pole of T exists only at K=0" % ", ".join("%.3f" % x for x in im),
    all(0.28 < x < 0.34 for x in im))

# B8 shell weights/moments on the exact lattice dispersion, one corner (x8), K=(kap,0,0)
def shell_stats(E, kap, h=0.0035, dE_frac=0.04):
    pmax = E * 0.8
    g_ = np.arange(-pmax, pmax + h / 2, h)
    X, Y, Zg = np.meshgrid(g_ + 0 * 0, g_, g_, indexing='ij')
    # offsets of the two records near the same corner: d1 = p, d2 = K - p;  exact dispersions
    u1 = (np.sin(X), np.sin(Y), np.sin(Zg))
    u2 = (np.sin(kap - X), np.sin(-Y), np.sin(-Zg))
    A_ = np.sqrt(sum(x * x for x in u1))
    B_ = np.sqrt(sum(x * x for x in u2))
    c_ = sum(x * y for x, y in zip(u1, u2)) / (A_ * B_ + 1e-300)
    wgt = (1 - c_) / 4
    En = A_ + B_
    sel = np.abs(En - E) < dE_frac * E
    # delta(E - En) ~ 1/(2 dE) box
    dE = dE_frac * E
    rho = 8 * (wgt * sel).sum() * h ** 3 / (2 * np.pi) ** 3 / (2 * dE)
    W_ = (wgt * sel).sum()
    xcen = X - kap / 2                                      # x = p - K/2
    mean_par = (wgt * sel * xcen ** 2).sum() / W_
    mean_perp = (wgt * sel * (Y ** 2 + Zg ** 2)).sum() / W_
    return rho, mean_par, mean_perp


kap, Ev = 0.10, 0.30
rho_n, mpar_n, mperp_n = shell_stats(Ev, kap)
rho_p = (Ev ** 2 - kap ** 2) / (4 * np.pi ** 2)
chk("B8 NUM    exact-dispersion corner shell (K=0.1,E=0.3): rho_c=%.5f vs (E^2-K^2)/(4pi^2)=%.5f; <x_par^2>=%.5f vs E^2/12=%.5f; <x_perp^2>=%.5f vs (E^2-K^2)/6=%.5f"
    % (rho_n, rho_p, mpar_n, Ev ** 2 / 12, mperp_n, (Ev ** 2 - kap ** 2) / 6),
    abs(rho_n / rho_p - 1) < 0.06 and abs(mpar_n / (Ev ** 2 / 12) - 1) < 0.05 and abs(mperp_n / ((Ev ** 2 - kap ** 2) / 6) - 1) < 0.05)

# B9 scaling table of the leading-order rate pieces (K || x), from B6's G_lead and A6: Gamma_q and R_x
print("-- B9 leading-order table, K||x, K->0 with E=zeta*K  (Gamma=2 pi w rho_c/|G|^2, R_x=Gamma*(g_bar-g)_x)")
C0v = C0
Gam_inf = 1 / (4 * np.pi * C0v ** 2)
print("   E>>K limit of Gamma_q: 1/(4 pi C0^2) = %.4f = 9/(pi W3^2)" % Gam_inf)
for zt, gv in zip(zetas, vals):
    gK = gv * zt                       # Re G / K
    eta_vals = (0.0, 0.5)
    for et in eta_vals:
        w_ = (zt ** 2 - 1) / (2 * (zt ** 2 - et ** 2))
        Gam = 2 * np.pi * w_ * (zt ** 2 - 1) / (4 * np.pi ** 2) / gK ** 2   # K-independent at leading order
        Rx = Gam * (zt ** 2 / 6) * (3 * et ** 2 - 1)    # in units K^3 (E=zeta K): kappa E^2/6 (3 eta^2-1)
        print("   zeta=%6.4g eta=%.1f  Gamma=%.4f   R_x/K^3=%+.4f" % (zt, et, Gam, Rx))
okG = all(2 * np.pi * 0.5 * (zt ** 2 - 1) / (4 * np.pi ** 2) / ((gv * zt) ** 2) <= 36 / np.pi + 1e-9 for zt, gv in zip(zetas, vals))
chk("B9 NUM    Gamma_q <= pi rho_c/(Re G)^2 <= 36/pi (from Re G >= E/12) at every tabulated zeta; Gamma -> 1/(4 pi C0^2)=9/(pi W3^2)=1.2459 as zeta->infinity",
    okG and abs(Gam_inf - 1.2459) < 2e-3)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("runtime %.1fs" % (time.time() - T0))
if FAIL == 0:
    print("HIT: (i) EXACT: for every total wave vector K and every z off the spectrum the free-pair singlet resolvent is odd pointwise in the relative momentum, "
          "g(z)=z(A^2+B^2-z^2+2u1.u2)/((A^2+B^2-z^2)^2-4A^2B^2), hence G_cc(-z)=-G_cc(z) (Re G_cc(E+i0) odd, Im even), on tori of any even size as well as in infinite volume; "
          "(ii) EXACT at K=0: the (+,-) overlaps vanish identically (and only at K=0 mod 2pi) and G_cc(z)=z<1/(4 eps^2-z^2)>, so G_cc(E+i0;0)=C0 E + i E^2/(4 pi) + o(E^2) with C0=W3/6=0.2527 and the contact amplitude 1/G_cc has a simple pole at E=0 "
          "(the o(E^2) and the pole statement use the standard Hoelder-1/2 threshold argument written in ATTEMPT.md, not a runner); "
          "(iii) SCOPED ASYMPTOTIC (leading form NUM-checked, error O(K^2) numerically): for small K and E>=|K|, G_cc = z<(z^2-|w|^2)/(4 eps^2 (z^2-(K.v)^2))> + O(K^2), Re G >= E/12 for that leading form by an exact inequality, Im G=(E^2-K^2)/(4 pi); "
          "so for upper-band pairs the golden-rule collision rate Gamma stays O(1) (limit 9/(pi W3^2)=1.246 for E>>K), and the rate of change of g is Gamma*(g_bar-g) ~ K E^2 (E^3 at E~|K|), not ~K E^4 (E^5)")
print("SUMMARY: oddness of G_cc exact in all fibres; K=0 contact amplitude has a simple threshold pole; at E>=|K| small, |G_cc| ~ E (not constant), so the hard-core collision rate of slow upper-band pairs is O(E^0) and the g-change rate is ~K E^2 (E^3 at E~|K|) rather than E^5")
sys.exit(0 if FAIL == 0 else 1)
