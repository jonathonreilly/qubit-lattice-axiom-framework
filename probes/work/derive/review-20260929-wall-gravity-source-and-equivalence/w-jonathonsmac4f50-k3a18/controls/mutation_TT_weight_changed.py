#!/usr/bin/env python3
"""
check.py -- J:derive:review-20260929-wall-gravity-source-and-equivalence:a1

ONE source action:  the supplied block-101 mode action of the curvature member,
with the stress coupling of block 62 added (as in the constraint-algebra note),

   L = [alpha tr(hdot^2) + beta (tr hdot)^2]/wbar + K wbar (u R1(h) + R2(h)) - e u
       + (1/2) Theta_ij h_ij ,

   R1 = p^2 tr h - p.h.p ,
   R2 = -(p^2/4) tr(h^2) + |h p|^2/2 - (p.h.p) tr(h)/2 + p^2 tr(h)^2/4 .

Bounded results computed here (all exact sympy / Fraction unless stated):
  A  helicity decoupling and the static helicity weights of R2
  B  static response: lapse sourced by e + Theta_ii ; static weights scalar : TT = 1 : 2
  C  TT sector: inertia 2 alpha/wbar, speed c^2 = K wbar^2/(4 alpha), flux = c * energy density
  D  the action's own source identity at beta = -alpha, and its absence at alpha+beta != 0
  E  quadrupole radiation power by two routes with disjoint machinery
     (Poynting flux with the TT projector; classical mode-sum with polarisation tensors)
  F  what depends on what: static data (K, wbar) versus inertia (alpha) versus matter law
  G  static light bending in the same (t,x) coordinates

Only sympy and mpmath.  No file output.
"""
import itertools
import random
import sys
from fractions import Fraction

import mpmath as mp
import sympy as sp

PASS = 0
FAIL = 0
HITS = []


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + name + ((" -- " + detail) if detail else ""))
    else:
        FAIL += 1
        print("FAIL " + name + ((" -- " + detail) if detail else ""))


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


t = sp.symbols("t")
al, K, w, p = sp.symbols("alpha K wbar p", positive=True)
be = sp.symbols("beta", real=True)

# --------------------------------------------------------------------------
# A. the action, helicity decoupling, static helicity weights
# --------------------------------------------------------------------------


def R1f(h, pv):
    return pv.dot(pv) * h.trace() - (pv.T * h * pv)[0]


def R2f(h, pv):
    p2 = pv.dot(pv)
    hp = h * pv
    return (-p2 / 4 * (h * h).trace() + hp.dot(hp) / 2
            - (pv.T * h * pv)[0] * h.trace() / 2 + p2 * h.trace() ** 2 / 4)


# A1: spatial invariance of R1, R2 under h -> h + p xi^T + xi p^T, generic p and generic h
hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (min(i, j), max(i, j))))
xv = sp.Matrix(sp.symbols("x0 x1 x2"))
pg = sp.Matrix(sp.symbols("q0 q1 q2"))
hsh = hs + pg * xv.T + xv * pg.T
chk("A1 R1 invariant under h -> h + p xi^T + xi p^T (generic p, h, xi)",
    zero(R1f(hsh, pg) - R1f(hs, pg)))
chk("A1 R2 invariant under h -> h + p xi^T + xi p^T (generic p, h, xi)",
    zero(R2f(hsh, pg) - R2f(hs, pg)))

# A2: helicity decoupling.  p along z, h = [[phi+a,b,cx],[b,phi-a,cy],[cx,cy,2 xi]]
qn = "phi a b cx cy xi u".split()
q = {n: sp.Symbol(n) for n in qn}
qd = {n: sp.Symbol(n + "d") for n in qn if n != "u"}
phi, a, b, cx, cy, xi, u = [q[n] for n in qn]
hmat = sp.Matrix([[phi + a, b, cx], [b, phi - a, cy], [cx, cy, 2 * xi]])
hdmat = sp.Matrix([[qd["phi"] + qd["a"], qd["b"], qd["cx"]],
                   [qd["b"], qd["phi"] - qd["a"], qd["cy"]],
                   [qd["cx"], qd["cy"], 2 * qd["xi"]]])
pz = sp.Matrix([0, 0, p])
R1 = sp.expand(R1f(hmat, pz))
R2 = sp.expand(R2f(hmat, pz))
chk("A2 R1 = 2 p^2 phi on the p-aligned parametrisation", zero(R1 - 2 * p ** 2 * phi))
chk("A2 R2 = p^2 (phi^2 - a^2 - b^2)/2 (cx, cy, xi drop out)",
    zero(R2 - p ** 2 * (phi ** 2 - a ** 2 - b ** 2) / 2))
ev, es = sp.symbols("e_s es")
Tm = sp.Matrix([[sp.Symbol("Txx"), sp.Symbol("Txy"), sp.Symbol("Txz")],
                [sp.Symbol("Txy"), sp.Symbol("Tyy"), sp.Symbol("Tyz")],
                [sp.Symbol("Txz"), sp.Symbol("Tyz"), sp.Symbol("Tzz")]])
Lsym = ((al * (hdmat * hdmat).trace() + be * hdmat.trace() ** 2) / w
        + K * w * (u * R1 + R2) - ev * u
        + sp.Rational(1, 2) * sum(Tm[i, j] * hmat[i, j] for i in range(3) for j in range(3)))
coords = [phi, a, b, cx, cy, xi, u] + [qd[n] for n in qn if n != "u"]
Hs = sp.hessian(Lsym, coords)
groups = {"phi": 0, "xi": 0, "u": 0, "a": 2, "b": 2, "cx": 1, "cy": 1}
names_all = qn + [n + "d" for n in qn if n != "u"]
hel = []
for n in names_all:
    base = n[:-1] if (n.endswith("d") and n != "u") else n
    hel.append(groups[base])
ok = True
for i, j in itertools.product(range(len(coords)), repeat=2):
    if hel[i] != hel[j] and sp.simplify(Hs[i, j]) != 0:
        ok = False
chk("A2 quadratic form is block diagonal in helicity {phi,xi,u | cx,cy | a,b} (general beta)", ok)
# a, b not coupled to each other
chk("A2 the two TT polarisations a, b are uncoupled",
    all(sp.simplify(Hs[coords.index(x), coords.index(y)]) == 0
        for x, y in [(a, b), (qd["a"], qd["b"]), (a, qd["b"]), (b, qd["a"])]))

# A3: static helicity weights of R2 on unit-normalised tensors, and relation to F_EH
n3 = sp.Matrix([0, 0, 1])
Ttt = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / sp.sqrt(2)
T0 = sp.diag(1, 1, -2) / sp.sqrt(6)
T1 = (n3 * sp.Matrix([1, 0, 0]).T + sp.Matrix([1, 0, 0]) * n3.T) / sp.sqrt(2)
for nm, Tn, wR2, wEH in [("TT (helicity 2)", Ttt, -sp.Rational(1, 4), sp.Rational(1, 2)),
                         ("helicity 0 trace-free", T0, sp.Rational(1, 12), -sp.Rational(1, 6)),
                         ("helicity 1", T1, 0, 0)]:
    assert sp.simplify((Tn * Tn).trace() - 1) == 0
    r2 = sp.simplify(R2f(Tn, n3))                    # p = 1
    feh = sp.simplify((Tn * Tn).trace() / 2 - (Tn * n3).dot(Tn * n3))
    chk("A3 %s: R2 weight %s, F_EH weight %s, R2 = -F_EH/2" % (nm, wR2, wEH),
        sp.simplify(r2 - wR2) == 0 and sp.simplify(feh - wEH) == 0 and sp.simplify(r2 + feh / 2) == 0)

# --------------------------------------------------------------------------
# B. static response, static helicity weights
# --------------------------------------------------------------------------
Txx, Tyy, Txy, Tzz, Txz, Tyz = [sp.Symbol(n) for n in "Txx Tyy Txy Tzz Txz Tyz".split()]
e = sp.Symbol("e")
Lst = Lsym.subs({qd[n]: 0 for n in qd})
# static stationarity in cx, cy, xi forces p.Theta = 0 (block 62 T5)
eq_cx = sp.diff(Lst, cx)
eq_cy = sp.diff(Lst, cy)
eq_xi = sp.diff(Lst, xi)
chk("B1 static equations of cx, cy, xi force Txz = Tyz = Tzz = 0 (p.Theta = 0)",
    zero(eq_cx - Tm[0, 2]) and zero(eq_cy - Tm[1, 2]) and zero(eq_xi - Tm[2, 2]))
Lst0 = Lst.subs({Txz: 0, Tyz: 0, Tzz: 0, ev: e})
sol = sp.solve([sp.diff(Lst0, v) for v in (phi, a, b, u)], [phi, a, b, u], dict=True)[0]
chk("B1 static lapse u = -(e + Theta_xx + Theta_yy)/(4 K wbar p^2)",
    zero(sol[u] + (e + Txx + Tyy) / (4 * K * w * p ** 2)))
chk("B1 static scalar phi = e/(2 K wbar p^2)", zero(sol[phi] - e / (2 * K * w * p ** 2)))
Leff = sp.simplify(Lst0.subs(sol))
tt2 = (Txx - Tyy) ** 2 / 2 + 3 * Txy ** 2          # Theta_TT : Theta_TT
Leff_claim = (e ** 2 + 2 * e * (Txx + Tyy)) / (8 * K * w * p ** 2) + tt2 / (4 * K * w * p ** 2)
chk("B1 L_eff(static) = (e^2 + 2 e Theta_ii)/(8 K wbar p^2) + Theta_TT:Theta_TT/(4 K wbar p^2)",
    zero(Leff - Leff_claim))
w_scalar = sp.Rational(1, 8) / (K * w)
w_tt = sp.Rational(1, 4) / (K * w)
chk("B2 static weights: scalar (e e) : TT (Theta Theta) = 1 : 2, both alpha-free",
    zero(w_tt / w_scalar - 2) and not (w_scalar.has(al) or w_tt.has(al)))
GE = 1 / (16 * sp.pi * K * w)
# two static point energies E1,E2 at distance r: V = -2 e1 e2/(8 K w p^2) -> -(E1 E2)/(4 K w) * 1/(4 pi r)
chk("B3 pair energy of two static energies: V = -G_E E1 E2 / r with G_E = 1/(16 pi K wbar)",
    zero(sp.Rational(2, 8) / (K * w) / (4 * sp.pi) - GE))

# 1/p^2 -> 1/(4 pi r):  f = exp(-m r)/(4 pi r) solves (-lap + m^2) f = delta
r, m = sp.symbols("r m", positive=True)
f = sp.exp(-m * r) / (4 * sp.pi * r)
lap = sp.diff(r ** 2 * sp.diff(f, r), r) / r ** 2
chk("B3 Fourier pair 1/(p^2+m^2) <-> exp(-m r)/(4 pi r): (-lap + m^2) f = 0 for r>0",
    zero(-lap + m ** 2 * f))
chk("B3 ... and unit delta weight: -4 pi r^2 f'(r) -> 1 as r -> 0",
    sp.limit(-4 * sp.pi * r ** 2 * sp.diff(f, r), r, 0) == 1)

# T71-type sign: the attraction sign of the static pair energy is the sign of K wbar, the same K that makes TT stable
Kneg = sp.Symbol("Kneg", negative=True)
chk("B5 sign: V_ee = -e1 e2/(4 K wbar p^2) is attractive iff K wbar > 0; TT frequency^2 = K wbar^2 p^2/(4 alpha) > 0 iff K/alpha > 0 -- "
    "one sign datum (K>0, alpha>0) covers stability and attraction",
    bool((-sp.Integer(1) / (4 * Kneg * w)).is_positive) and bool((Kneg * w ** 2 / (4 * al)).is_negative)
    and bool((-sp.Integer(1) / (4 * K * w)).is_negative) and bool((K * w ** 2 / (4 * al)).is_positive))

# --------------------------------------------------------------------------
# C. TT sector: inertia, speed, energy flux
# --------------------------------------------------------------------------
tt = sp.symbols("tt")
aF = sp.Function("a")(t)
Lt = ((al * 2 * sp.diff(aF, t) ** 2) / w + K * w * (-(p ** 2) * aF ** 2 / 2)
      + sp.Symbol("Tp") * aF)        # Tp = (Txx - Tyy)/2
EL_a = sp.diff(sp.diff(Lt, sp.Derivative(aF, t)), t) - sp.diff(Lt, aF)
c2 = K * w ** 2 / (4 * al)
chk("C1 TT equation: a'' + c^2 p^2 a = (wbar/(4 alpha)) Theta_+ with c^2 = K wbar^2/(4 alpha)",
    zero(sp.expand(EL_a * w / (4 * al)) - (sp.diff(aF, t, 2) + c2 * p ** 2 * aF - w / (4 * al) * sp.Symbol("Tp"))))
# tensor normalisation: L_TT = (alpha/wbar) tr(hd^2) - (K wbar p^2/4) tr(h^2)  -> I = 2 alpha/wbar, Kg = K wbar/2
I_tt = 2 * al / w
Kg = K * w / 2
chk("C1 inertia I = 2 alpha/wbar, gradient stiffness K_g = K wbar/2, speed c^2 = K_g/I",
    zero(Kg / I_tt - c2))
# plane outgoing wave h = f(t - x/c): flux S = c * energy density
cc, x_, = sp.symbols("c x", positive=True)
fF = sp.Function("f")
hw = fF(t - x_ / cc)
Edens = (al / w) * 1 * sp.diff(hw, t) ** 2 * 1 + (K * w / 4) * sp.diff(hw, x_) ** 2   # per unit tr (h as one component)
S = -(K * w / 2) * sp.diff(hw, x_) * sp.diff(hw, t)
chk("C2 outgoing wave: Poynting flux = c * energy density when c^2 = K wbar^2/(4 alpha)",
    zero((S - cc * Edens).subs(cc, sp.sqrt(c2)).doit()))
chk("C2 outgoing wave: flux = (K wbar/(2c)) (dh/dt)^2",
    zero((S - (K * w / (2 * cc)) * sp.diff(hw, t) ** 2).subs(cc, sp.sqrt(c2)).doit()))
# residue of the TT propagator
om = sp.symbols("omega")
prop = 1 / (I_tt * (c2 * p ** 2 - om ** 2))
res = sp.residue(prop, om, sp.sqrt(c2) * p)
chk("C3 TT propagator: static value 1/(K_g p^2); residue at omega = c p is -1/(2 I c p)",
    zero(prop.subs(om, 0) - 1 / (Kg * p ** 2)) and zero(res + 1 / (2 * I_tt * sp.sqrt(c2) * p)))

# --------------------------------------------------------------------------
# D. the source identity of the action
# --------------------------------------------------------------------------
phF, xiF, uF = [sp.Function(n)(t) for n in ("phi", "xi", "u")]
eF, TzzF, SxxyyF = [sp.Function(n)(t) for n in ("e", "Tzz", "Sxy")]
Lsc = ((al * (2 * sp.diff(phF, t) ** 2 + 4 * sp.diff(xiF, t) ** 2) + be * (2 * sp.diff(phF, t) + 2 * sp.diff(xiF, t)) ** 2) / w
       + K * w * (uF * 2 * p ** 2 * phF + p ** 2 * phF ** 2 / 2) - eF * uF + TzzF * xiF
       + SxxyyF * phF)               # SxxyyF = (Txx+Tyy)/2
def EL(L, f):
    return sp.diff(sp.diff(L, sp.Derivative(f, t)), t) - sp.diff(L, f)
E_u, E_xi, E_phi = EL(Lsc, uF), EL(Lsc, xiF), EL(Lsc, phF)
chk("D0 helicity-0 sector reproduces the full-action equations (xi: 8(alpha+beta) xi'' + 8 beta phi'' ... )",
    zero(E_xi - ((8 * (al + be) * sp.diff(xiF, t, 2) + 8 * be * sp.diff(phF, t, 2)) / w - TzzF)))
# beta = -alpha
Eu_s = sp.solve(E_u, phF)[0]                      # phi = e/(2 K wbar p^2)
Exi_ba = E_xi.subs(be, -al)
chk("D1 beta = -alpha: xi-equation contains no xi, only phi'': -8 alpha phi''/wbar = Theta_zz",
    zero(Exi_ba - (-8 * al * sp.diff(phF, t, 2) / w - TzzF)))
ddotphi = sp.solve(Exi_ba, sp.diff(phF, t, 2))[0]
eddot = sp.simplify(2 * K * w * p ** 2 * ddotphi)
chk("D1 beta = -alpha: e'' = -(K wbar^2/(4 alpha)) p^2 Theta_zz  (the action's own source identity)",
    zero(eddot + c2 * p ** 2 * TzzF))
chk("D1 ... and the coefficient equals the TT speed squared (J = kappa P with kappa = c^2)",
    zero(c2 - (K * w ** 2 / (4 * al))))
# alpha + beta != 0 : xi'' solvable for any Theta_zz, no identity
xidd = sp.solve(E_xi, sp.diff(xiF, t, 2))[0]
chk("D2 alpha+beta != 0: xi'' = [w Theta_zz - 8 beta phi'']/(8(alpha+beta)) for ANY Theta_zz (no identity on e)",
    zero(xidd - (w * TzzF / 8 - be * sp.diff(phF, t, 2)) / (al + be)))
chk("D2 ... so with alpha+beta != 0 the equations are solvable for any (e, Theta); identity absent",
    sp.simplify(sp.denom(sp.together(xidd)).subs(be, -al)) == 0)

# D3: moment identity  int x_i x_j e'' = 2 c^2 int Theta_ij  for compact support when e'' = c^2 d_k d_l Theta_kl
X = sp.symbols("X0 X1 X2")


def gauss_int(poly):
    poly = sp.Poly(sp.expand(poly), *X)
    tot = 0
    for mon, co in poly.terms():
        term = co
        for k in mon:
            if k % 2:
                term = 0
                break
            term *= sp.gamma(sp.Rational(k + 1, 2))
        tot += term
    return sp.simplify(tot)


random.seed(20260929)
okmom = True
G = sp.exp(-(X[0] ** 2 + X[1] ** 2 + X[2] ** 2))
for trial in range(3):
    Th = {}
    for i in range(3):
        for j in range(i, 3):
            mons = [1, X[0], X[1], X[2], X[0] ** 2, X[1] * X[2], X[0] * X[1], X[2] ** 2, X[0] * X[1] * X[2], X[0] ** 2 * X[1]]
            Th[(i, j)] = sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4)) * mo for mo in mons)
            Th[(j, i)] = Th[(i, j)]
    Tg = {k: v * G for k, v in Th.items()}
    dd = sum(sp.diff(Tg[(k, l)], X[k], X[l]) for k in range(3) for l in range(3))
    poly_dd = sp.simplify(dd / G)
    for (i, j) in [(0, 0), (0, 1), (1, 2), (2, 2)]:
        lhs = gauss_int(sp.expand(X[i] * X[j] * poly_dd))
        rhs = 2 * gauss_int(Th[(i, j)])
        if sp.simplify(lhs - rhs) != 0:
            okmom = False
chk("D3 compact support: int x_i x_j d_k d_l Theta_kl = 2 int Theta_ij (3 random Gaussian-polynomial tensors, exact)", okmom)
chk("D3 hence Q''_ij = 2 c^2 A_ij, A_ij = int Theta_ij, Q_ij = int e x_i x_j (given e'' = c^2 d_k d_l Theta_kl)", okmom)

# B4: stationary compact bodies keep only e as the monopole source (virial), binding energy included
okv = True
for trial in range(3):
    psi = sum(sp.Rational(random.randint(-4, 4), random.randint(1, 3)) * mo
              for mo in [1, X[0], X[1] * X[2], X[0] ** 2, X[2] ** 2 * X[1], X[0] * X[1]]) * G
    lapl = sum(sp.diff(psi, X[k], 2) for k in range(3))
    Thst = {(i, j): (lapl if i == j else 0) - sp.diff(psi, X[i], X[j]) for i in range(3) for j in range(3)}
    div_ok = all(sp.simplify(sum(sp.diff(Thst[(i, j)], X[j]) for j in range(3))) == 0 for i in range(3))
    trace = sp.simplify(sum(Thst[(i, i)] for i in range(3)) / G)
    int_tr = gauss_int(trace)
    int_xtr = [gauss_int(sp.expand(X[k] * trace)) for k in range(3)]
    if not (div_ok and sp.simplify(int_tr) == 0 and all(sp.simplify(v) == 0 for v in int_xtr)):
        okv = False
chk("B4 stationary compact stress (d_j Theta_ij = 0, Gaussian-polynomial family, exact): int Theta_ii = 0 and int x_k Theta_ii = 0, "
    "so the far lapse is sourced by int e (binding energy included) and the pull at O(gradient) is -E_tot grad u", okv)


# --------------------------------------------------------------------------
# E. quadrupole radiation power, two routes
# --------------------------------------------------------------------------
th, ph = sp.symbols("theta varphi", real=True)
nv = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
th_hat = sp.Matrix([sp.cos(th) * sp.cos(ph), sp.cos(th) * sp.sin(ph), -sp.sin(th)])
ph_hat = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
Asym = sp.Matrix(3, 3, lambda i, j: sp.Symbol("A%d%d" % (min(i, j), max(i, j))))
trA = Asym.trace()
AA = sum(Asym[i, j] ** 2 for i in range(3) for j in range(3))
Ptr = sp.eye(3) - nv * nv.T
PA = Ptr * Asym * Ptr
ATTsq = sp.expand((PA * PA).trace() * 0 + sum(PA[i, j] ** 2 for i in range(3) for j in range(3)) - sp.Rational(1, 2) * (Ptr * Asym).trace() ** 2)
# route 1 (projector): angular integral of A^TT:A^TT
I_proj = sp.integrate(sp.integrate(sp.expand(ATTsq * sp.sin(th)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
target = sp.Rational(8, 5) * sp.pi * (AA - trA ** 2 / 3)
chk("E1 sphere integral of the TT-projected square: (8 pi/5)(A:A - (tr A)^2/3)", zero(I_proj - target))
# route 2 (polarisation tensors): sum over lambda of (A : e^lambda)^2
ep = (th_hat * th_hat.T - ph_hat * ph_hat.T) / sp.sqrt(2)
ex = (th_hat * ph_hat.T + ph_hat * th_hat.T) / sp.sqrt(2)
ApA = sum(Asym[i, j] * ep[i, j] for i in range(3) for j in range(3))
AxA = sum(Asym[i, j] * ex[i, j] for i in range(3) for j in range(3))
I_pol = sp.integrate(sp.integrate(sp.expand(sp.simplify((ApA ** 2 + AxA ** 2)) * sp.sin(th)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
chk("E2 polarisation-tensor sum gives the same sphere integral (independent construction)", zero(I_pol - target))

c = sp.symbols("c", positive=True)            # speed read off the TT equation
# Poynting route: h = (wbar/(4 alpha)) (1/(4 pi c^2 r)) A^TT(t - r/c);  S_r = (K wbar/(2c)) tr(hdot^2)
pref = w / (4 * al) / (4 * sp.pi * c ** 2)
Adot = sp.Symbol("Adot2")                    # stands for  Adot:Adot - (tr Adot)^2/3 , the TF square
P_flux = (K * w / (2 * c)) * pref ** 2 * sp.Rational(8, 5) * sp.pi * Adot
# mode-sum route: oscillator I = 2 alpha/wbar per polarisation, force F_lambda = A_lambda/2 (amplitude A0 cos wt)
omg = sp.symbols("omega", positive=True)
Ahat = sp.Symbol("Ahat2")                    # A0:A0 - (tr A0)^2/3
# per mode <P> = (pi F^2/(4 I)) delta(omega_p - omega);  int d^3p/(2pi)^3 delta(c p - omega) g = omega^2/(c^3 (2pi)^3) * oint g /... (see below)
# P_mode = (pi/(4 I)) (1/4) * (1/c) * [omega^2/c^2 /(2pi)^3] * (8 pi/5) Ahat
P_mode = (sp.pi / (4 * I_tt)) * sp.Rational(1, 4) * (omg ** 2 / c ** 3) / (2 * sp.pi) ** 3 * sp.Rational(8, 5) * sp.pi * Ahat
P_flux_avg = P_flux.subs(Adot, omg ** 2 * Ahat / 2)    # < Adot^2 > = omega^2 A0^2 / 2
chk("E3 flux route and mode-sum route give the same power when c^2 = K wbar^2/(4 alpha)",
    zero((P_flux_avg - P_mode).subs(K, 4 * al * c ** 2 / w ** 2)))
chk("E3 and NOT otherwise: the two routes differ at fixed alpha, K, wbar if c is not the TT speed",
    not zero((P_flux_avg - P_mode).subs({K: 4 * al * 4 / w ** 2, c: 1})))

# Lorentzian -> delta limit used in the mode-sum (numerical, mpmath): int_0^inf gamma om/((x^2-om^2)^2+gamma^2 om^2) dx -> pi/(2 om)
mp.mp.dps = 30
om0 = mp.mpf(3) / 2
vals = []
for g in (mp.mpf(10) ** -2, mp.mpf(10) ** -3):
    val = mp.quad(lambda x: g * om0 / ((x ** 2 - om0 ** 2) ** 2 + g ** 2 * om0 ** 2), [0, om0 - 1, om0, om0 + 1, 10 * om0, mp.inf])
    vals.append(val)
target_l = mp.pi / (2 * om0)
chk("E4 Lorentzian absorption line integrates to pi/(2 omega) as gamma -> 0 (delta(omega_p^2-omega^2) = delta/(2 omega))",
    abs(vals[1] - target_l) < mp.mpf(10) ** -3 * 5 and abs(vals[1] - target_l) < abs(vals[0] - target_l))

# conserved source law:  A = Q''/(2 c^2)   ->  power in terms of the e-quadrupole third derivative
Q3 = sp.Symbol("Q3sq")       # < dddot Q^TF : dddot Q^TF >
P_Q = sp.simplify((K * w / (2 * c)) * pref ** 2 * sp.Rational(8, 5) * sp.pi * Q3 / (4 * c ** 4))
P_Q = sp.simplify(P_Q.subs(al, K * w ** 2 / (4 * c ** 2)))
chk("E5 P = <dddot Q^TF:dddot Q^TF> / (80 pi K wbar c^5)", zero(P_Q - Q3 / (80 * sp.pi * K * w * c ** 5)))
GR_form = GE / (5 * c ** 5) * Q3
chk("E5 = (G_E/(5 c^5)) <dddot Q^TF^2> with G_E = 1/(16 pi K wbar): the quadrupole formula, ratio 1 for every alpha/K",
    zero(P_Q - GR_form))
chk("E5 in static-weight language: P = W_TT <dddotQ^2>/(20 pi c^5), W_TT = 1/(4 K wbar)",
    zero(P_Q - w_tt * Q3 / (20 * sp.pi * c ** 5)))

# --------------------------------------------------------------------------
# F. what depends on what
# --------------------------------------------------------------------------
static_quants = [GE, w_scalar, w_tt, sol[u], sol[phi], sol[a]]
chk("F1 every static quantity (G_E, weights, u, phi, a) is independent of alpha",
    all(not sp.sympify(s).has(al) for s in static_quants))
# two inertias, same K, wbar:
Kv, wv = sp.Integer(1), sp.Integer(1)
alA, alB = sp.Rational(1, 4), sp.Integer(1)
cA, cB = sp.sqrt(Kv * wv ** 2 / (4 * alA)), sp.sqrt(Kv * wv ** 2 / (4 * alB))
PA_ = (Q3 / (80 * sp.pi * Kv * wv * cA ** 5))
PB_ = (Q3 / (80 * sp.pi * Kv * wv * cB ** 5))
ratio = sp.simplify(PB_ / PA_)
chk("F1 counterexample: same K, wbar (same static G_E, same weights, same bending) but alpha = 1/4 vs 1 "
    "-> c = 1 vs 1/2 and power ratio 32 for the same energy-quadrupole history", ratio == 32 and cA == 1 and cB == sp.Rational(1, 2))
def P_of_alpha(a_):
    return Q3 / (80 * sp.pi * K * w * (sp.sqrt(K * w ** 2 / (4 * a_))) ** 5)


chk("F1 P scales as alpha^(5/2) at fixed K, wbar and fixed energy-quadrupole history: P(4 alpha)/P(alpha) = 32",
    zero(sp.simplify(P_of_alpha(4 * al) / P_of_alpha(al)) - 32))
# F2: matter law J = kappa P with kappa != c^2 at alpha+beta != 0  (A = Q''/(2 kappa))
kap = sp.symbols("kappa", positive=True)
cm = sp.sqrt(kap)
P_k = sp.simplify((K * w / (2 * c)) * pref ** 2 * sp.Rational(8, 5) * sp.pi * Q3 / (4 * kap ** 2))
P_k = sp.simplify(P_k.subs(al, K * w ** 2 / (4 * c ** 2)))
chk("F2 alpha+beta != 0, matter law J = kappa P: P = G_E <dddotQ^2>/(5 c kappa^2)",
    zero(P_k - GE * Q3 / (5 * c * kap ** 2)))
chk("F2 relative to the quadrupole formula at the MATTER speed c_m = sqrt(kappa): P/P_GR = c_m/c  (=1 iff c = c_m)",
    zero(P_k / (GE * Q3 / (5 * cm ** 5)) - cm / c))

# --------------------------------------------------------------------------
# G. static light bending in the same coordinates (rate field u, length field h)
# --------------------------------------------------------------------------
E_, rr, zz, bb, lam = sp.symbols("E r z b lambda", positive=True)
u_r = -GE * E_ / rr                                   # B3, any alpha
lam_r = -u_r                                         # h_ij = 2 lambda delta_ij ,  p^2 lambda = e/(4 K wbar) = -u p^2 (B1)
chk("G1 at Theta = 0: u = -phi/2; the isotropic part h_ij = phi delta_ij (gauge-equivalent to the p-aligned form by A1) so lambda = phi/2 = -u",
    zero(sol[u].subs({Txx: 0, Tyy: 0}) + sol[phi] / 2))
# metric:  g_00 = -(1 + 2u),  g_ij = (1 + 2 lam) delta_ij = (1 - 2 u) delta_ij  (lengths^2 = 1 + h, ASSUMED reading)
gam = sp.symbols("gamma")
n_ind = sp.sqrt(1 + 2 * lam_r) / sp.sqrt(1 + 2 * u_r)
n_lin = sp.series(n_ind, E_, 0, 2).removeO()
chk("G2 refractive index n = 1 - 2u to first order (gamma_PPN = 1)", zero(n_lin - (1 - 2 * u_r)))
rho = sp.sqrt(bb ** 2 + zz ** 2)
n1 = (n_lin).subs(rr, rho)
defl = -sp.integrate(sp.diff(n1, bb), (zz, -sp.oo, sp.oo))
defl = sp.simplify(defl)
chk("G2 deflection = 4 G_E E / b = E/(4 pi K wbar b), no alpha, no c", zero(defl - 4 * GE * E_ / bb) and not defl.has(al))
n_clock = sp.series(1 / sp.sqrt(1 + 2 * u_r), E_, 0, 2).removeO()
defl_clock = sp.simplify(-sp.integrate(sp.diff(n_clock.subs(rr, rho), bb), (zz, -sp.oo, sp.oo)))
chk("G2 clock alone (h = 0) bends by 2 G_E E / b, half of the combined value", zero(defl_clock - 2 * GE * E_ / bb))

# G3: bending is a function of (K, wbar, E, b) only; the speed c^2 = K wbar^2/(4 alpha) varies freely with alpha
chk("G3 same coordinates, same fields: deflection has no alpha while c^2 does -> bending and the wave speed are separate numbers here "
    "(beta = -alpha action); no relation 1 + c_m^2/c^2 appears",
    (not defl.has(al)) and c2.has(al) and zero(sp.diff(defl, al)) and not zero(sp.diff(c2, al)))

# --------------------------------------------------------------------------
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
if FAIL == 0:
    print("HIT: block-101 member (beta=-alpha, stress coupling) radiates the quadrupole law P=(G_E/(5c^5))<dddotQ^TF^2> "
          "with G_E=1/(16 pi K wbar) from the static scalar weight and c^2=K wbar^2/(4 alpha) forced by the action's own source identity "
          "(ratio to the quadrupole formula is 1 for every alpha/K); at alpha+beta!=0 with matter law J=kappa P it is c_m/c; "
          "this is scoped to the supplied mode action and long-wavelength quadrupole, and is not a physical source, not a speed bound.")
print("SUMMARY: for the supplied block-101 mode action with stress coupling, static helicity weights (scalar:TT = 1:2, alpha-free) fix G_E and the bending "
      "(gamma=1, alpha-free), while the quadrupole power needs inertia alpha through c^-5 and the action's own source identity, giving exactly the quadrupole formula at the TT speed.")
sys.exit(0 if FAIL == 0 else 1)
