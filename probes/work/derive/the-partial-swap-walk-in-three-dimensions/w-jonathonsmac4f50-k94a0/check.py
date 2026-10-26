#!/usr/bin/env python3
"""
check.py -- J:derive:the-partial-swap-walk-in-three-dimensions:a1
The partial-swap (clocked) walk in three dimensions: exact symbol, exact dispersion,
ray factor, and the origin of the sideways drift.

Sections
  1  exact Gaussian-rational lattice test of the layer/symbol dictionary and of
     unitarity + range for a non-uniform clock           (exact, Fractions)
  2  exact symbol algebra (unit quaternions in sympy): parity in eps, exact
     half-trace polynomial, series, node limits          (exact, sympy)
  3  plain-order (non-palindromic) comparison: the O(eps) eigenvector term
  4  Berry-density statements                            (exact, sympy)
  5  exact Bloch-lag identity for a rotation per tick    (exact, sympy)
  6  NUMERICAL (float, not exact) packet run, labelled
Only numpy, scipy, sympy, mpmath, stdlib are used.
"""
import sys, time, itertools, random
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
RES = []


def chk(name, ok, extra=""):
    print(("PASS " if ok else "FAIL ") + name + ((" | " + str(extra)) if extra != "" else ""), flush=True)
    RES.append(bool(ok))


# ----------------------------------------------------------------------------------
# Section 1.  Gaussian rationals, exact lattice walk
# ----------------------------------------------------------------------------------
class Z:
    __slots__ = ("r", "i")

    def __init__(s, r=0, i=0):
        s.r = Fr(r)
        s.i = Fr(i)

    def __add__(a, b):
        return Z(a.r + b.r, a.i + b.i)

    def __sub__(a, b):
        return Z(a.r - b.r, a.i - b.i)

    def __mul__(a, b):
        return Z(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    def conj(a):
        return Z(a.r, -a.i)

    def zero(a):
        return a.r == 0 and a.i == 0

    def __eq__(a, b):
        return a.r == b.r and a.i == b.i


ZI = Z(0, 1)
ZMI = Z(0, -1)


def sp2z(x):
    x = sp.nsimplify(x)
    return Z(Fr(int(sp.numer(sp.re(x))), int(sp.denom(sp.re(x)))), Fr(int(sp.numer(sp.im(x))), int(sp.denom(sp.im(x)))))


# Pauli matrices and the per-axis basis {a_j,b_j}:  sigma_j = |a><b|+|b><a|, sigma_{j+1} = -i|a><b| + i|b><a|
PAULI = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def basis_V(j):
    X = PAULI[j]
    Y = PAULI[(j + 1) % 3]
    Zm = -sp.I * X * Y
    M = sp.eye(2) + X * PAULI[0] + Y * PAULI[1] + Zm * PAULI[2]
    nrm = sp.sqrt(sp.simplify((M.H * M).trace() / 2))
    V = (M / nrm).applyfunc(sp.simplify)
    assert sp.simplify(V.H * V - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(V * PAULI[0] * V.H - X) == sp.zeros(2)
    assert sp.simplify(V * PAULI[1] * V.H - Y) == sp.zeros(2)
    return V


VS = [basis_V(j) for j in range(3)]
VZ = [[[sp2z(V[a, b]) for b in range(2)] for a in range(2)] for V in VS]
VZH = [[[VZ[j][b][a].conj() for b in range(2)] for a in range(2)] for j in range(3)]  # V^dagger
chk("1.0 basis matrices V_j (columns a_j,b_j) are unitary and send (sigma_x,sigma_y) to (sigma_j,sigma_{j+1}), exact", True)


def trans(psi, M, wrap):
    """apply the 2x2 matrix M (list of lists of Z) site by site to state dict {(x,y,z,c):Z}"""
    sites = {}
    for (x, y, z, c), v in psi.items():
        sites.setdefault((x, y, z), [Z(), Z()])[c] = v
    out = {}
    for s, (v0, v1) in sites.items():
        for a in range(2):
            w = M[a][0] * v0 + M[a][1] * v1
            if not w.zero():
                out[s + (a,)] = w
    return out


def addv(s, j, d, wrap):
    t = list(s)
    t[j] += d
    if wrap:
        t = [t[i] % wrap[i] for i in range(3)]
    return tuple(t)


def apply_layer(psi, j, kind, bond, wrap=None):
    """one layer: exp(-i eps_b sigma_x) on the pairs (a,x),(b,x+e_j) [kind A] or (b,x),(a,x+e_j) [kind B].
    bond(x,y,z,j) -> (cos,sin) Fractions of the angle of the bond (x, x+e_j)."""
    phi = trans(psi, VZH[j], wrap)           # components (a,b)
    # collect pair base points x
    bases = set()
    for (x, y, z, c), v in phi.items():
        s = (x, y, z)
        if kind == "A":
            bases.add(s if c == 0 else addv(s, j, -1, wrap))
        else:
            bases.add(s if c == 1 else addv(s, j, -1, wrap))
    out = {}
    for s in bases:
        sp_ = addv(s, j, 1, wrap)
        co, si = bond(s[0], s[1], s[2], j)
        co = Z(co)
        mis = Z(0, -si)       # -i sin
        if kind == "A":
            p, q = phi.get(s + (0,), Z()), phi.get(sp_ + (1,), Z())     # a(x), b(x+e)
            pn, qn = co * p + mis * q, co * q + mis * p
            out[s + (0,)] = pn
            out[sp_ + (1,)] = qn
        else:
            p, q = phi.get(s + (1,), Z()), phi.get(sp_ + (0,), Z())     # b(x), a(x+e)
            pn, qn = co * p + mis * q, co * q + mis * p
            out[s + (1,)] = pn
            out[sp_ + (0,)] = qn
    out = {k: v for k, v in out.items() if not v.zero()}
    return trans(out, VZ[j], wrap)


SEQ = [(0, "A"), (0, "B"), (1, "A"), (1, "B"), (2, "A"), (2, "B")]


def pal_tick(psi, half_bond, wrap=None):
    """palindromic product L1(e/2)..L5(e/2) L6(e) L5(e/2)..L1(e/2); half_bond gives (cos(a/2), sin(a/2))"""
    def full_bond(x, y, z, j):
        c, s = half_bond(x, y, z, j)
        return (c * c - s * s, 2 * c * s)
    for (j, kd) in SEQ[:5]:
        psi = apply_layer(psi, j, kd, half_bond, wrap)
    psi = apply_layer(psi, SEQ[5][0], SEQ[5][1], full_bond, wrap)
    for (j, kd) in reversed(SEQ[:5]):
        psi = apply_layer(psi, j, kd, half_bond, wrap)
    return psi


# ----------------------------------------------------------------------------------
# Section 2.  symbol algebra with unit quaternions: S = q0 - i q.sigma
# ----------------------------------------------------------------------------------
c1, c2, c3, s1, s2, s3, C, Sn = sp.symbols("c1 c2 c3 s1 s2 s3 C Sn")
cs = [c1, c2, c3]
ss = [s1, s2, s3]
eps = sp.symbols("e")


def red(x):
    x = sp.expand(x)
    p = sp.Poly(x, s1, s2, s3, Sn)
    out = 0
    for mon, co in p.terms():
        a, b, cc, d = mon
        out += (co * (1 - c1 ** 2) ** (a // 2) * s1 ** (a % 2) * (1 - c2 ** 2) ** (b // 2) * s2 ** (b % 2)
                * (1 - c3 ** 2) ** (cc // 2) * s3 ** (cc % 2) * (1 - C ** 2) ** (d // 2) * Sn ** (d % 2))
    return sp.expand(out)


def qmul(a, b):
    a0, av = a
    b0, bv = b
    dot = sum(x * y for x, y in zip(av, bv))
    cr = [av[1] * bv[2] - av[2] * bv[1], av[2] * bv[0] - av[0] * bv[2], av[0] * bv[1] - av[1] * bv[0]]
    return (a0 * b0 - dot, [a0 * bv[i] + b0 * av[i] + cr[i] for i in range(3)])


def qred(a):
    return (red(a[0]), [red(x) for x in a[1]])


def layer_q(j, sign, cosa, sina):
    n = [0, 0, 0]
    n[j] = cs[j]
    n[(j + 1) % 3] = sign * ss[j]
    return (cosa, [sina * x for x in n])      # g_A = c_j X - s_j Y (sign=-1), g_B = c_j X + s_j Y (sign=+1)


SG = [(0, -1), (0, 1), (1, -1), (1, 1), (2, -1), (2, 1)]
half = lambda j, sg: layer_q(j, sg, C, Sn)
full = lambda j, sg: layer_q(j, sg, C ** 2 - Sn ** 2, 2 * C * Sn)

Spal = (sp.Integer(1), [0, 0, 0])
for (j, sg) in SG[:5]:
    Spal = qred(qmul(Spal, half(j, sg)))
Spal = qred(qmul(Spal, full(*SG[5])))
for (j, sg) in reversed(SG[:5]):
    Spal = qred(qmul(Spal, half(j, sg)))
Q0, QV = Spal


def evalS(q, vals):
    q0, qv = q
    return (q0.subs(vals), [x.subs(vals) for x in qv])


def pauli_sum(q0, qv):
    return q0 * sp.eye(2) - sp.I * sum((qv[i] * PAULI[i] for i in range(3)), sp.zeros(2))


# --- 1.1  layer/symbol dictionary and palindromic product on a 4x4x4 torus, exact
def zmat_apply(Mz, u):
    return [Mz[a][0] * u[0] + Mz[a][1] * u[1] for a in range(2)]


half_pair = (Fr(3, 5), Fr(4, 5))                      # cos(e/2), sin(e/2): e is a non-rational angle with these values
cos_e, sin_e = half_pair[0] ** 2 - half_pair[1] ** 2, 2 * half_pair[0] * half_pair[1]
rnd = random.Random(12345)
allk = list(itertools.product(range(4), repeat=3))
nodes = [(1, 1, 1), (1, 1, 3), (1, 3, 1), (3, 1, 1), (1, 3, 3), (3, 1, 3), (3, 3, 1), (3, 3, 3)]
ksel = nodes + rnd.sample([k for k in allk if k not in nodes], 12)
CK = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}   # (cos,sin) of pi n/2
IP = {0: Z(1, 0), 1: Z(0, 1), 2: Z(-1, 0), 3: Z(0, -1)}  # i^n
ok_dict = True
wrap = (4, 4, 4)
for kn in ksel:
    for ucomp in range(2):
        psi = {}
        for x in itertools.product(range(4), repeat=3):
            ph = IP[(kn[0] * x[0] + kn[1] * x[1] + kn[2] * x[2]) % 4]
            psi[x + (ucomp,)] = ph
        out = pal_tick(psi, lambda x, y, z, j: half_pair, wrap)
        vals = {C: sp.Rational(3, 5), Sn: sp.Rational(4, 5)}
        for j in range(3):
            vals[cs[j]] = CK[kn[j]][0]
            vals[ss[j]] = CK[kn[j]][1]
        q0v, qvv = evalS(Spal, vals)
        Sm = pauli_sum(q0v, qvv)
        col = [sp2z(Sm[a, ucomp]) for a in range(2)]
        for x in itertools.product(range(4), repeat=3):
            ph = IP[(kn[0] * x[0] + kn[1] * x[1] + kn[2] * x[2]) % 4]
            for a in range(2):
                got = out.get(x + (a,), Z())
                want = ph * col[a]
                if not (got == want):
                    ok_dict = False
chk("1.1 exact: the lattice palindromic 6-layer walk on a 4x4x4 torus acts on every tested Bloch wave (8 Weyl nodes + 12 others, both spinors) as S(k)=q0-i q.sigma with S built from g_A=c_j sigma_j - s_j sigma_{j+1}, g_B=c_j sigma_j + s_j sigma_{j+1}",
    ok_dict, "tested %d k-points x 2 spinors, cos(e/2)=3/5, sin(e/2)=4/5" % len(ksel))

# --- 1.2  unitarity and range for a non-uniform clock on the infinite lattice (finite support), exact
TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]


def wild_half(x, y, z, j):
    a, b, c = TRI[(3 * x + 5 * y + 7 * z + 2 * j) % 5]
    sgn = -1 if (x + y * 2 + z * 3 + j) % 3 == 0 else 1
    return (Fr(a, c), sgn * Fr(b, c))


def inner(p, q):
    t = Z()
    for k, v in p.items():
        if k in q:
            t = t + v.conj() * q[k]
    return t


rnd2 = random.Random(7)
vecs = []
for _ in range(3):
    v = {}
    for _ in range(7):
        key = (rnd2.randint(-2, 2), rnd2.randint(-2, 2), rnd2.randint(-2, 2), rnd2.randint(0, 1))
        v[key] = Z(Fr(rnd2.randint(-5, 5), rnd2.randint(1, 4)), Fr(rnd2.randint(-5, 5), rnd2.randint(1, 4)))
    vecs.append(v)
imgs = [pal_tick(v, wild_half) for v in vecs]
ok_unit = True
for a in range(3):
    for b in range(3):
        d = inner(imgs[a], imgs[b]) - inner(vecs[a], vecs[b])
        if not d.zero():
            ok_unit = False
chk("1.2 exact: with a non-uniform clock (bond angles from a table of Pythagorean angles, random signs) the palindromic walk preserves all inner products of 3 random finite-support vectors (unitary on finite support)", ok_unit)

rng_ok = True
for c in range(2):
    out = pal_tick({(0, 0, 0, c): Z(1)}, wild_half)
    xs = [abs(k[0]) for k in out]
    ys = [abs(k[1]) for k in out]
    zs = [abs(k[2]) for k in out]
    if not (max(xs) <= 4 and max(ys) <= 4 and max(zs) <= 3):
        rng_ok = False
chk("1.3 exact: a site is spread to at most 4,4,3 sites along axes 1,2,3 (layer count per axis in the palindromic order), for the non-uniform clock", rng_ok)

def wild_half_neg(x, y, z, j):
    c, s = wild_half(x, y, z, j)
    return (c, -s)


ok_inv = True
for v in vecs:
    back = pal_tick(pal_tick(v, wild_half), wild_half_neg)
    if set(k for k, a in back.items() if not a.zero()) != set(k for k, a in v.items() if not a.zero()):
        ok_inv = False
    for k, a in v.items():
        if not (back.get(k, Z()) == a):
            ok_inv = False
chk("1.4 exact: for the non-uniform clock, U(-angles) U(angles) = identity on the same random vectors (palindromic order makes the walk's inverse the walk with all angles negated: quasi-energy odd in the angle field, no even-order term in the effective generator)", ok_inv)

# ----------------------------------------------------------------------------------
# Section 2 (cont.)  checks on the symbolic symbol
# ----------------------------------------------------------------------------------
norm2 = red(Q0 ** 2 + sum(x ** 2 for x in QV) - 1)
chk("2.1 exact: q0^2+|q|^2=1 identically in (c_j,s_j,C,Sn) modulo c^2+s^2=1 (S is in SU(2))", norm2 == 0)

q0_free = Q0.free_symbols
chk("2.2 exact: q0 contains no Sn (even in eps); every q_i is Sn times a polynomial in (C,c,s) (odd in eps)",
    (Sn not in q0_free) and all(sp.Poly(x, Sn).degree() == 1 and sp.Poly(x, Sn).coeff_monomial(1) == 0 for x in QV))


def flip(expr):
    return expr.subs(Sn, -Sn)


Sminus = (flip(Q0), [flip(x) for x in QV])
prod = qred(qmul(Spal, Sminus))
chk("2.3 exact: S(eps)*S(-eps)=identity as polynomials (palindromic order: S(-eps)=S(eps)^{-1}); hence cos(omega) is even and sin(omega)n is odd in eps",
    prod[0] == 1 and all(x == 0 for x in prod[1]))

# independent cross-check of the polynomial against explicit 2x2 matrix products at exact points
pts_k = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)),
         (sp.Rational(-8, 17), sp.Rational(15, 17)), (sp.Rational(20, 29), sp.Rational(-21, 29)),
         (sp.Rational(7, 25), sp.Rational(24, 25)), (sp.Rational(-15, 17), sp.Rational(-8, 17))]
pts_h = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(12, 13), sp.Rational(5, 13)), (sp.Rational(15, 17), sp.Rational(8, 17))]


def mat_layer(j, sg, k, a_c, a_s):
    X = PAULI[j]
    Y = PAULI[(j + 1) % 3]
    g = k[0] * X + sg * k[1] * Y
    return a_c * sp.eye(2) - sp.I * a_s * g


ok_cross = True
for trial in range(6):
    kk = [pts_k[(trial + 2 * j) % 6] for j in range(3)]
    Cv, Sv = pts_h[trial % 3]
    vals = {C: Cv, Sn: Sv}
    for j in range(3):
        vals[cs[j]] = kk[j][0]
        vals[ss[j]] = kk[j][1]
    Mx = sp.eye(2)
    for (j, sg) in SG[:5]:
        Mx = Mx * mat_layer(j, sg, kk[j], Cv, Sv)
    Mx = Mx * mat_layer(SG[5][0], SG[5][1], kk[SG[5][0]], Cv ** 2 - Sv ** 2, 2 * Cv * Sv)
    for (j, sg) in reversed(SG[:5]):
        Mx = Mx * mat_layer(j, sg, kk[j], Cv, Sv)
    q0v, qvv = evalS(Spal, vals)
    if (Mx - pauli_sum(q0v, qvv)).applyfunc(sp.expand) != sp.zeros(2):
        ok_cross = False
chk("2.4 exact: the unit-quaternion polynomial equals the explicit product of eleven 2x2 layer matrices at 6 exact rational (k,eps) points", ok_cross)

# --- series in eps
def eser(x, n):
    return sp.expand(sp.series(x.subs({C: sp.cos(eps / 2), Sn: sp.sin(eps / 2)}), eps, 0, n).removeO())


def redk(x):
    x = sp.expand(x)
    p = sp.Poly(x, s1, s2, s3)
    out = 0
    for mon, co in p.terms():
        a, b, cc = mon
        out += co * (1 - c1 ** 2) ** (a // 2) * s1 ** (a % 2) * (1 - c2 ** 2) ** (b // 2) * s2 ** (b % 2) * (1 - c3 ** 2) ** (cc // 2) * s3 ** (cc % 2)
    return sp.expand(out)


Qser = [eser(x, 6) for x in QV]
Q0ser = eser(Q0, 7)
q1v = [redk(x.coeff(eps, 1)) for x in Qser]
q2v = [redk(x.coeff(eps, 2)) for x in Qser]
q3v = [redk(x.coeff(eps, 3)) for x in Qser]
P = c1 ** 2 + c2 ** 2 + c3 ** 2
chk("2.5 exact: first order q = 2 eps (cos k_1, cos k_2, cos k_3) (the generator 2 sum_j cos k_j sigma_j of block 105 T1, now in 3D); second order vanishes",
    q1v == [2 * c1, 2 * c2, 2 * c3] and q2v == [0, 0, 0])
chk("2.6 exact: q0 = 1 - 2 P eps^2 + O(eps^4), P=sum cos^2 k_j", redk(Q0ser.coeff(eps, 2)) == -2 * P and Q0ser.coeff(eps, 1) == 0 and Q0ser.coeff(eps, 3) == 0)

cq3 = sp.expand(sum(a * b for a, b in zip([c1, c2, c3], q3v)))
rho = sp.simplify(cq3 / (2 * P) + 2 * P / 3)     # omega = 2 eps |c| (1 + eps^2 rho + O(eps^4)),  rho = omega3/omega1
print("   exact c.q3 =", sp.factor(cq3))
print("   exact rho(k) = omega3/omega1 =", rho)
# verify rho against an independent exact route: omega = acos(q0) expanded
t, n1, n2, n3 = sp.symbols("t n1 n2 n3", positive=True)
subs_node = {c1: -sp.sin(t * n1), c2: -sp.sin(t * n2), c3: -sp.sin(t * n3), s1: sp.cos(t * n1), s2: sp.cos(t * n2), s3: sp.cos(t * n3)}
# independent check of rho: sin(omega)^2 = |q|^2 expansion, at an exact rational point with perfect-square P
pt = {c1: sp.Rational(3, 5), c2: sp.Rational(4, 5), c3: 0, s1: sp.Rational(4, 5), s2: sp.Rational(-3, 5), s3: 1}
qe = [x.subs(pt) for x in Qser]
q0e = Q0ser.subs(pt)
# cos(omega) = q0 -> omega^2 series
w1 = 2 * sp.sqrt(P.subs(pt))
w3 = rho.subs(pt) * w1
# 1 - cos(omega) with omega = w1 eps + w3 eps^3:  eps^2: w1^2/2 ; eps^4: w1 w3 - w1^4/24 ; compare with 1 - q0 from the half-trace polynomial
chk("2.7 exact: independent route at the rational point (cos k_j)=(3/5,4/5,0): -[eps^4]q0 = w1 w3 - w1^4/24 and [eps^2]q0 = -w1^2/2, with w1=2|c|, w3=rho w1 from the c.q3 formula",
    sp.simplify(Q0ser.coeff(eps, 2).subs(pt) + w1 ** 2 / 2) == 0 and sp.simplify(-Q0ser.coeff(eps, 4).subs(pt) - (w1 * w3 - w1 ** 4 / 24)) == 0)

rho_node = sp.series(sp.simplify(rho.subs(subs_node).subs({n1: n1, n2: n2, n3: n3})), t, 0, 2).removeO()
rho_expected = (-(n1 ** 2 + n2 ** 2 + n3 ** 2) + 3 * t * (n1 ** 2 * n2 - n1 * n3 ** 2 + n2 ** 2 * n3)) / (6 * (n1 ** 2 + n2 ** 2 + n3 ** 2))
chk("2.8 exact: at a Weyl node k=(pi/2)(1,1,1)+q, q=t n: rho = -1/6 + (t/2)(n1^2 n2 + n2^2 n3 - n1 n3^2)/|n|^2 + O(t^2); the isotropic limit -1/6 equals block 105 T2's line value -sin^2 k/6 at its node",
    sp.simplify(rho_node - rho_expected) == 0)
chk("2.9 exact: ray-force factor eps d_eps(omega)/omega = 1+2 eps^2 rho+O(eps^4) -> 1 - eps^2/3 at the node, equal to the line value 1 - eps^2 sin^2 k/3 (block 105 T2) at its node",
    sp.simplify(rho_node.subs(t, 0) + sp.Rational(1, 6)) == 0)

# ----------------------------------------------------------------------------------
# Section 3.  plain (non-palindromic) order: the O(eps) eigenvector term
# ----------------------------------------------------------------------------------
def lq(j, sign, a):
    n = [0, 0, 0]
    n[j] = cs[j]
    n[(j + 1) % 3] = sign * ss[j]
    return (sp.cos(a), [sp.sin(a) * x for x in n])


Spl = (sp.Integer(1), [0, 0, 0])
for (j, sg) in SG:
    Spl = qmul(lq(j, sg, eps), Spl)       # layer 1 applied first
plQ = [sp.expand(sp.series(x, eps, 0, 4).removeO()) for x in Spl[1]]
pl1 = [sp.expand(x.coeff(eps, 1)) for x in plQ]
pl2 = [sp.factor(redk(sp.expand(x.coeff(eps, 2)))) for x in plQ]
chk("3.1 exact: plain order U=L6...L1 has the same first-order generator 2 sum cos k_j sigma_j but a nonzero second-order term q2 (odd + even powers of eps appear)",
    [redk(x) for x in pl1] == [2 * c1, 2 * c2, 2 * c3] and any(x != 0 for x in pl2))
print("   plain order q2 =", pl2)
Rn = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
nvec = sp.Matrix([n1, n2, n3])
q2node = sp.Matrix([sp.series(x.subs(subs_node), t, 0, 2).removeO() for x in pl2])
chk("3.2 exact: at the node, plain-order N=q/eps = -2t[(1 - eps R) n] + O(eps t^2, eps^2 t), R the cyclic shift (R n)=(n2,n3,n1): a linear map M=1-eps R of the monopole field c",
    sp.simplify(q2node - 2 * t * Rn * nvec) == sp.zeros(3, 1))
Msym = sp.Matrix(3, 3, sp.symbols("m0:9"))
u, v, w_ = [sp.Matrix(sp.symbols(nm + "0:3")) for nm in ("u", "v", "w")]
lhs = (Msym * u).dot((Msym * v).cross(Msym * w_))
rhs = Msym.det() * u.dot(v.cross(w_))
chk("3.3a exact: (Mu).(Mv x Mw) = det(M) u.(v x w) for symbolic 3x3 M", sp.expand(lhs - rhs) == 0)
A = -Rn
# sphere average of c^.A c^ is tr(A)/3 -> relative change average of (trA - 3 c^Ac^) is 0
th, ph_ = sp.symbols("th ph", real=True)
cv = sp.Matrix([sp.sin(th) * sp.cos(ph_), sp.sin(th) * sp.sin(ph_), sp.cos(th)])
avg = sp.integrate(sp.integrate((A.trace() - 3 * (cv.T * A * cv)[0]) * sp.sin(th), (ph_, 0, 2 * sp.pi)), (th, 0, sp.pi))
chk("3.4 exact: the sphere average of the O(eps) relative change eps(trA-3 c^.A c^) of the monopole density vanishes for A=-R", sp.simplify(avg) == 0)

# ----------------------------------------------------------------------------------
# Section 4.  Berry (solid-angle) density
# ----------------------------------------------------------------------------------
ks = sp.symbols("k1 k2 k3", real=True)
rep = {c1: sp.cos(ks[0]), c2: sp.cos(ks[1]), c3: sp.cos(ks[2]), s1: sp.sin(ks[0]), s2: sp.sin(ks[1]), s3: sp.sin(ks[2])}


def solid_density(N, a, b):
    Nk = [x.subs(rep) for x in N]
    da = [sp.diff(x, ks[a]) for x in Nk]
    db = [sp.diff(x, ks[b]) for x in Nk]
    cr = [da[1] * db[2] - da[2] * db[1], da[2] * db[0] - da[0] * db[2], da[0] * db[1] - da[1] * db[0]]
    trip = sum(Nk[i] * cr[i] for i in range(3))
    return trip / sum(x ** 2 for x in Nk) ** sp.Rational(3, 2)


nv = (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3))
sub_k = {ks[i]: sp.pi / 2 + t * nv[i] for i in range(3)}
N0 = [2 * c1, 2 * c2, 2 * c3]
Npal = [x + eps ** 2 * y for x, y in zip(N0, q3v)]
Npl = [N0[i] + eps * pl2[i] + eps ** 2 * sp.expand(redk(sp.expand(plQ[i].coeff(eps, 3)))) for i in range(3)]
d0 = solid_density(N0, 0, 1)
dpal = sp.series(solid_density(Npal, 0, 1).subs(sub_k), eps, 0, 3).removeO()
dpl = sp.series(solid_density(Npl, 0, 1).subs(sub_k), eps, 0, 2).removeO()
d0n = sp.simplify(d0.subs(sub_k))
chk("4.1 exact: eps^0 solid-angle density Phi_12 at the node along n=(2/3,1/3,2/3) is -2/(3 t^2)+O(1), i.e. the monopole -q^/q^2 component (sign: node k=(pi/2)(1,1,1) is left-handed, opposite to block 54's sigma.sin k node)",
    sp.simplify(sp.series(d0n, t, 0, 0).removeO() + sp.Rational(2, 3) / t ** 2) == 0)
pal_e1 = sp.simplify(dpal.coeff(eps, 1))
chk("4.2 exact: palindromic order has NO eps^1 term in the Berry density (n is even in eps)", pal_e1 == 0)
rat_pal = sp.series(sp.simplify(dpal.coeff(eps, 2) / d0n), t, 0, 2)
chk("4.3 exact: palindromic eps^2 correction to the monopole density is relatively O(t): ratio = (43/36) t + O(t^2) along n=(2/3,1/3,2/3)",
    sp.simplify(rat_pal.removeO() - sp.Rational(43, 36) * t) == 0, "ratio series = %s" % rat_pal)
rat_pl = sp.series(sp.simplify(dpl.coeff(eps, 1) / d0n), t, 0, 1).removeO()
exp_pl = 3 * (nv[0] * nv[1] + nv[1] * nv[2] + nv[2] * nv[0])
chk("4.4 exact: plain order has an eps^1 correction of relative size 3(n1n2+n2n3+n3n1)=8/3 (order one, direction dependent) to the same monopole density at the node: ratio -> 8/3",
    sp.simplify(rat_pl - exp_pl) == 0, "ratio = %s, formula 3 n.Rn = %s" % (rat_pl, exp_pl))

# ----------------------------------------------------------------------------------
# Section 5.  exact Bloch lag identity for a rotation per tick
# ----------------------------------------------------------------------------------
sc, cc_ = sp.symbols("s_t c_t")      # sin(theta), cos(theta); relation s^2 + c^2 = 1
nn_ = sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3)])
vv_ = sp.Matrix([sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(2, 3)])
assert nn_.dot(vv_) == 0 and nn_.dot(nn_) == 1 and vv_.dot(vv_) == 1
Rv = lambda x: (cc_ ** 2 - sc ** 2) * x + 2 * sc * cc_ * nn_.cross(x)      # rotation by 2 theta about n, on vectors perpendicular to n
cand = -vv_ / 2 - (cc_ / sc) / 2 * nn_.cross(vv_)
resid = (Rv(cand) - cand - vv_).applyfunc(lambda e: sp.expand(sp.together(e) * sc))
ok51 = True
for e_ in resid:
    num = sp.numer(sp.together(e_))
    rem = sp.rem(sp.expand(num), cc_ ** 2 + sc ** 2 - 1, cc_)
    ok51 = ok51 and sp.expand(rem) == 0
chk("5.1 exact: for a Bloch rotation by 2 theta about n, (R-1)(-v/2 - (cot theta/2) n x v) = v on v perp n (tested for n=(2,1,2)/3, v=(1,2,-2)/3, modulo sin^2+cos^2=1); the 1/theta ~ 1/eps part is the sideways n x v lag, the remainder -v/2 is smaller by a factor of order eps",
    ok51)

# ----------------------------------------------------------------------------------
# Section 6.  NUMERICAL (floating point) packet run -- labelled, not exact
# ----------------------------------------------------------------------------------
print("-- section 6: NUMERICAL (floating point) packet run, not exact --", flush=True)
try:
    import numpy as np
    from scipy.integrate import solve_ivp  # noqa: F401  (kept for parity with the standalone script)

    sgn_ = [np.array(m, complex) for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
    I2 = np.eye(2, dtype=complex)
    NODE = np.array([np.pi / 2] * 3)

    def np_V(j):
        X = sgn_[j]; Y = sgn_[(j + 1) % 3]
        Zm = -1j * X @ Y
        M = np.eye(2) + X @ sgn_[0] + Y @ sgn_[1] + Zm @ sgn_[2]
        return M / np.sqrt(np.trace(M.conj().T @ M).real / 2)

    NV = [np_V(j) for j in range(3)]

    def np_layer(psi, j, kind, co, si):
        V = NV[j]
        phi = np.einsum("ab,xyzb->xyza", V.conj().T, psi)
        a = phi[..., 0]; b = phi[..., 1]
        if kind == "A":
            bs = np.roll(b, -1, axis=j)
            an = co * a - 1j * si * bs
            bn = np.roll(co * bs - 1j * si * a, 1, axis=j)
        else:
            as_ = np.roll(a, -1, axis=j)
            bn = co * b - 1j * si * as_
            an = np.roll(co * as_ - 1j * si * b, 1, axis=j)
        return np.einsum("ab,xyzb->xyza", V, np.stack([an, bn], -1))

    def np_tick(w, e0):
        ang = [e0 * np.sqrt(w * np.roll(w, -1, axis=j)) for j in range(3)]
        cf = [(np.cos(a), np.sin(a)) for a in ang]
        ch = [(np.cos(a / 2), np.sin(a / 2)) for a in ang]

        def tick(psi):
            for (j, kd) in SEQ[:5]:
                psi = np_layer(psi, j, kd, *ch[j])
            psi = np_layer(psi, SEQ[5][0], SEQ[5][1], *cf[SEQ[5][0]])
            for (j, kd) in reversed(SEQ[:5]):
                psi = np_layer(psi, j, kd, *ch[j])
            return psi
        return tick

    def np_symbol(k, e):
        k = np.atleast_2d(k); N = k.shape[0]; e = np.broadcast_to(e, (N,))

        def lay(j, kind, a):
            X = sgn_[j]; Y = sgn_[(j + 1) % 3]
            cj = np.cos(k[:, j])[:, None, None]; sj = np.sin(k[:, j])[:, None, None]
            g = cj * X - sj * Y if kind == "A" else cj * X + sj * Y
            aa = a[:, None, None]
            return np.cos(aa) * I2 - 1j * np.sin(aa) * g
        S = np.broadcast_to(I2, (N, 2, 2)).copy()
        for (j, kd) in SEQ[:5]:
            S = S @ lay(j, kd, e / 2)
        S = S @ lay(SEQ[5][0], SEQ[5][1], e)
        for (j, kd) in reversed(SEQ[:5]):
            S = S @ lay(j, kd, e / 2)
        return S

    def beig(k, e):
        ev, Vv = np.linalg.eig(np_symbol(k, e))
        ph = np.angle(ev)
        i = np.argmin(ph, axis=1); idx = np.arange(len(i))
        u = Vv[idx, :, i]
        u = u / np.linalg.norm(u, axis=1)[:, None]
        u = u * np.exp(-1j * np.angle(u[:, 0]))[:, None]
        return -ph[idx, i], u

    def bgrad(k, e, h=1e-5):
        g = np.zeros_like(k)
        for a in range(3):
            d = np.zeros(3); d[a] = h
            g[:, a] = (beig(k + d, e)[0] - beig(k - d, e)[0]) / (2 * h)
        return g

    def bberry(k, e, h=2e-4):
        Om = np.zeros((len(k), 3))
        dot = lambda p, q: (p.conj() * q).sum(1)
        for c in range(3):
            a, b = (c + 1) % 3, (c + 2) % 3
            ea = np.zeros(3); ea[a] = h; eb = np.zeros(3); eb[b] = h
            u0 = beig(k, e)[1]; u1 = beig(k + ea, e)[1]; u2 = beig(k + ea + eb, e)[1]; u3 = beig(k + eb, e)[1]
            Om[:, c] = -np.angle(dot(u0, u1) * dot(u1, u2) * dot(u2, u3) * dot(u3, u0)) / h ** 2
        return Om

    def cloud(m, gd, k0, e0, g, T, sigma, anom, Nr=600, seed=0):
        rng = np.random.default_rng(seed)
        x = rng.normal(size=(Nr, 3)) * sigma
        q = k0 * m + rng.normal(size=(Nr, 3)) / (2 * sigma)
        x = np.concatenate([x, -x]); q = np.concatenate([q, 2 * k0 * m - q])
        nt = int(round(T / (2 * e0)))

        def rhs(x, q):
            w = 1 + g * (x @ gd)
            k = NODE + q; ee = e0 * w
            v = bgrad(k, ee)
            dw = 1e-5
            dEde = (beig(k, ee * (1 + dw))[0] - beig(k, ee * (1 - dw))[0]) / (2 * dw * ee)
            kd = -(dEde * e0 * g)[:, None] * gd[None, :]
            if anom:
                v = v - np.cross(kd, bberry(k, ee))
            return v, kd
        X = x.copy(); Q = q.copy()
        for _ in range(nt):
            k1x, k1q = rhs(X, Q)
            k2x, k2q = rhs(X + 0.5 * k1x, Q + 0.5 * k1q)
            k3x, k3q = rhs(X + 0.5 * k2x, Q + 0.5 * k2q)
            k4x, k4q = rhs(X + k3x, Q + k3q)
            X = X + (k1x + 2 * k2x + 2 * k3x + k4x) / 6; Q = Q + (k1q + 2 * k2q + 2 * k3q + k4q) / 6
        return (X - x).mean(0)

    def run_sim(m, gd, k0, e0, g, T, L, sigma):
        ctr = np.array([L / 2] * 3); x0 = ctr - m * T / 2
        n = np.fft.fftfreq(L, 1.0 / L); kg = 2 * np.pi * n / L
        KX, KY, KZ = np.meshgrid(kg, kg, kg, indexing="ij")
        q0 = k0 * m
        wrap_ = lambda a, c: (a - c + np.pi) % (2 * np.pi) - np.pi
        D = np.stack([wrap_(KX, q0[0]), wrap_(KY, q0[1]), wrap_(KZ, q0[2])], -1)
        f = np.exp(-(D ** 2).sum(-1) * sigma ** 2)
        mask = f > 1e-7
        kk = np.stack([KX, KY, KZ], -1)[mask]
        th, u = beig(NODE + kk, np.full(len(kk), e0))
        psik = np.zeros((L, L, L, 2), complex)
        psik[mask] = (f[mask] * np.exp(-1j * (kk @ x0)))[:, None] * u
        psi = np.fft.ifftn(psik, axes=(0, 1, 2)) * L ** 3
        X = np.stack(np.meshgrid(*[np.arange(L)] * 3, indexing="ij"), -1)
        psi = psi * np.exp(1j * np.pi / 2 * X.sum(-1))[..., None]
        psi /= np.sqrt((np.abs(psi) ** 2).sum())
        d0_ = (np.abs(psi) ** 2).sum(-1)
        c0 = np.array([(d0_ * X[..., a]).sum() for a in range(3)])
        tick = np_tick(1 + g * ((X - ctr) @ gd), e0)
        for _ in range(int(round(T / (2 * e0)))):
            psi = tick(psi)
        dd = (np.abs(psi) ** 2).sum(-1)
        edge = sum(dd.take(range(0, 3), axis=a).sum() + dd.take(range(L - 3, L), axis=a).sum() for a in range(3))
        return np.array([(dd * X[..., a]).sum() for a in range(3)]) - c0, edge

    # sanity: float symbol agrees with the exact polynomial at a generic point
    kt = np.array([0.7, 1.9, 2.6]); et = 0.31
    Sn_ = np_symbol(kt, np.array([et]))[0]
    vals = {C: np.cos(et / 2), Sn: np.sin(et / 2)}
    for j in range(3):
        vals[cs[j]] = np.cos(kt[j]); vals[ss[j]] = np.sin(kt[j])
    q0f = float(Q0.subs(vals)); qvf = [float(x.subs(vals)) for x in QV]
    Sref = q0f * I2 - 1j * sum(qvf[i] * sgn_[i] for i in range(3))
    chk("6.0 NUMERICAL: float symbol equals the exact quaternion polynomial at a generic (k,eps) to 1e-12", np.abs(Sn_ - Sref).max() < 1e-12)

    m = np.array([1.0, 0, 0]); gd = np.array([0.0, 0, 1])
    e0, k0, T, L, sg_ = 0.2, 0.5, 30.0, 64, 5.0
    gg = 0.004
    res = {}
    for s_ in (1, -1):
        res[s_] = run_sim(m, gd, k0, e0, s_ * gg, T, L, sg_)
        print("   packet run g=%+.3f displacement %s edge weight %.1e  [%.0f s]" % (s_ * gg, np.round(res[s_][0], 4), res[s_][1], time.time() - T0), flush=True)
    sim_odd = (res[1][0] - res[-1][0]) / 2
    cl0 = (cloud(m, gd, k0, e0, gg, T, sg_, False) - cloud(m, gd, k0, e0, -gg, T, sg_, False)) / 2
    cl1 = (cloud(m, gd, k0, e0, gg, T, sg_, True) - cloud(m, gd, k0, e0, -gg, T, sg_, True)) / 2
    print("   odd-in-g displacement: packet %s ; cloud of scalar rays (exact omega) %s ; cloud with anomalous velocity %s" % (np.round(sim_odd, 4), np.round(cl0, 4), np.round(cl1, 4)), flush=True)
    drift_sim = sim_odd[1] - cl0[1]
    drift_pred = cl1[1] - cl0[1]
    chk("6.1 NUMERICAL: fall (odd-in-g z displacement) of the packet agrees with the cloud of rays of the exact omega to 0.02 (eps0=0.2, k=0.5 along x, gradient z, T=30)",
        abs(sim_odd[2] - cl0[2]) < 0.02, "packet %.4f cloud %.4f" % (sim_odd[2], cl0[2]))
    chk("6.2 NUMERICAL: the scalar rays give essentially no sideways (y) displacement (|y|<0.03) while the packet is displaced sideways by > 0.1 (gradient x motion direction)",
        abs(cl0[1]) < 0.03 and drift_sim > 0.1, "cloud y %.4f ; packet y %.4f" % (cl0[1], sim_odd[1]))
    chk("6.3 NUMERICAL: packet-minus-cloud sideways displacement equals the Berry-curvature (anomalous velocity) prediction within 15%",
        abs(drift_sim - drift_pred) < 0.15 * abs(drift_pred), "packet-cloud %.4f prediction %.4f (ratio %.3f)" % (drift_sim, drift_pred, drift_sim / drift_pred))
    # lowest-order lattice monopole value, same configuration: g T/(2 k) with lattice factors (block 54 form)
    print("   (long-wavelength  g T/(2k) = %.4f; sign is + here because the node (pi/2,pi/2,pi/2) has opposite handedness to block 54's node at 0)" % (gg * T / (2 * k0)))
except Exception as exc:  # pragma: no cover
    chk("6.x NUMERICAL block ran without exception", False, repr(exc))

# ----------------------------------------------------------------------------------
npass = sum(RES)
nfail = len(RES) - npass
print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
print("runtime %.0f s" % (time.time() - T0))
if nfail == 0:
    print("HIT: [scoped to the supplied choices: partner sigma_{j+1} for axis j, layer order A1 B1 A2 B2 A3 B3 palindromic with half angles] (i) exact 3D symbol S(k)=q0-i q.sigma of the palindromic partial-swap walk (eleven dimer factors, verified against the lattice walk on a torus) with explicit half-trace polynomial and omega=2 eps |cos k| (1+eps^2 rho(k)+O(eps^4)), rho(node)=-1/6+(1/2)(q1^2 q2+q2^2 q3-q1 q3^2)/|q|^2+O(q^2); (ii) S(-eps)=S(eps)^(-1) (and U(-angles)=U(angles)^(-1) for every clock field), so omega is odd and the band vector is even in eps: NO O(eps) eigenvector term in the palindromic order; (iii) in the plain order the O(eps) eigenvector term is the constant linear map 1-eps R on the node's field c (R the cyclic shift), whose effect on the Berry density has zero sphere average; the order-eps^0 monopole is untouched at this order. NOT claimed: an exact lattice drift law; the identification of the packet's sideways displacement with -kdot x Omega is semiclassical (ASSUMED) and only floating-point supported")
print("SUMMARY: PARTIAL exact 3D palindromic partial-swap symbol, dispersion polynomial and eps^2 coefficient, eps-parity (no O(eps) eigenvector term) and the plain-order O(eps) term as a linear map on the node field, so the sideways drift is not an O(eps) eigenvector effect; the exact lattice drift law is only semiclassical (ASSUMED) and floating-point supported")
sys.exit(0 if nfail == 0 else 1)
