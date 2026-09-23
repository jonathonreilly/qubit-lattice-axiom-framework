#!/usr/bin/env python3
"""a-delay-for-the-rate-field, independent attempt 4 (worker w-jonathonsmac4f50-j519d, claude-opus-5-5).

Exact claims are checked with sympy (symbolic, exact rationals) or fractions.
Sections E1-E2 are floating-point lattice simulations: EXECUTED evidence, not claims.
Every step label refers to ATTEMPT.md.
"""
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
NPASS = 0
NFAIL = 0


def ok(label, cond, detail=""):
    global NPASS, NFAIL
    if cond:
        NPASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NFAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def is0(expr):
    return sp.simplify(expr) == 0


# ---------------------------------------------------------------- Step 1 (a)
gam, c, wb = sp.symbols("gamma c wbar", positive=True)

# 1.1  on-site term under a change of parameter t -> f(t): w -> w/f1, v -> (v - f2/f1)/f1, dt -> f1 dt
w1, w2, v1, v2, vr, f1, f2 = sp.symbols("w1 w2 v1 v2 v_ref f1 f2", real=True)
onsite = lambda vv, ww: sum(v ** 2 / w for v, w in zip(vv, ww))
tr = lambda v: (v - f2 / f1) / f1
Ldt_old = onsite((v1, v2), (w1, w2))
Ldt_new = onsite((tr(v1), tr(v2)), (w1 / f1, w2 / f1)) * f1
diff_onsite = sp.simplify(Ldt_new - Ldt_old)
ok("1.1a on-site sum v^2/w: L dt changes under t->f(t) and the change vanishes iff f''=0",
   (not is0(diff_onsite)) and is0(diff_onsite.subs(f2, 0)), f"change = {sp.factor(diff_onsite)}")
ref = lambda vv, ww, vref: sum((v - vref) ** 2 / w for v, w in zip(vv, ww))
Ldt_new_ref = ref((tr(v1), tr(v2)), (w1 / f1, w2 / f1), tr(vr)) * f1
ok("1.1b wall-referred sum (v - v_ref)^2/w: L dt unchanged for every f", is0(Ldt_new_ref - ref((v1, v2), (w1, w2), vr)))
s_ = sp.symbols("s", positive=True)
ok("1.1c weight one: a(w)=1/w gives a(s w) s^2 = s a(w)", is0((1 / (s_ * w1)) * s_ ** 2 - s_ / w1))

# 1.2  Euler-Lagrange for K = udot^2/(2 gamma c^2 wbar e^u): d/dt dK/dudot - dK/du = (u'' - u'^2/2)/(gamma c^2 w)
t = sp.symbols("t", real=True)
u = sp.Function("u")(t)
K = sp.diff(u, t) ** 2 / (2 * gam * c ** 2 * wb * sp.exp(u))
EL = sp.diff(sp.diff(K, sp.diff(u, t)), t) - sp.diff(K, u)
target = (sp.diff(u, t, 2) - sp.diff(u, t) ** 2 / 2) / (gam * c ** 2 * wb * sp.exp(u))
ok("1.2 Euler-Lagrange of the kinetic term = (u'' - u'^2/2)/(gamma c^2 w)", is0(EL - target))

# 1.3  simplest bond energy at one site with six neighbours: dF/du_x = (12/gamma) phi_x (phi_x - avg)
px = sp.symbols("phi_x", positive=True)
pj = sp.symbols("phi_1:7", positive=True)
F_loc = (2 / gam) * sum((px - q) ** 2 for q in pj)
dFdu = (px / 2) * sp.diff(F_loc, px)  # u = 2 log phi + const, d/du = (phi/2) d/dphi
avg = sum(pj) / 6
ok("1.3 dF/du_x = (12/gamma) phi_x (phi_x - average of phi)", is0(dFdu - (12 / gam) * px * (px - avg)))

# 1.4  phi-form of the law: with u = 2 log phi - log wbar:  u'' - u'^2/2 = 2 phi''/phi - 4 phi'^2/phi^2 ;
#      law: phi'' - 2 phi'^2/phi = c^2 phi^4 Lap(phi) - (gamma c^2/2) phi^3 e,  Lap = sum_j (phi_j - phi_x)
ph = sp.Function("phi")(t)
uu = 2 * sp.log(ph) - sp.log(wb)
lhs = sp.diff(uu, t, 2) - sp.diff(uu, t) ** 2 / 2
ok("1.4a u'' - u'^2/2 = 2 phi''/phi - 4 phi'^2/phi^2",
   is0(lhs - (2 * sp.diff(ph, t, 2) / ph - 4 * sp.diff(ph, t) ** 2 / ph ** 2)))
e_ = sp.symbols("e", real=True)
Lap = sum(pj) - 6 * px
rhs_u = -gam * c ** 2 * px ** 2 * ((12 / gam) * px * (px - avg) + e_)  # = u''-u'^2/2 at the site
phi_dd_from_law = (rhs_u + 4 * sp.Symbol("pd") ** 2 / px ** 2) * px / 2  # solve 2 phi''/phi - 4 pd^2/phi^2 = rhs
claimed = 2 * sp.Symbol("pd") ** 2 / px + c ** 2 * px ** 4 * Lap - (gam * c ** 2 / 2) * px ** 3 * e_
ok("1.4b phi'' = 2 phi'^2/phi + c^2 phi^4 Lap(phi) - (gamma c^2/2) phi^3 e", is0(phi_dd_from_law - claimed))

# 1.5  weak field at uniform wbar: u'' = c^2 wbar^2 Lap u - gamma c^2 wbar e ; const = 6 in the (avg - u) form
ux = sp.symbols("u_x", real=True)
uj = sp.symbols("u_1:7", real=True)
eps = sp.symbols("epsilon", positive=True)
phis = [sp.sqrt(wb) * sp.exp(eps * q / 2) for q in (ux,) + uj]
rhs_eps = -gam * c ** 2 * phis[0] ** 2 * ((12 / gam) * phis[0] * (phis[0] - sum(phis[1:]) / 6) + eps * e_)
lin = sp.simplify(sp.diff(rhs_eps, eps).subs(eps, 0))
ok("1.5a linear part = c^2 wbar^2 (sum_j u_j - 6 u_x) - gamma c^2 wbar e",
   is0(lin - (c ** 2 * wb ** 2 * (sum(uj) - 6 * ux) - gam * c ** 2 * wb * e_)), f"{sp.expand(lin)}")
ok("1.5b in the form c^2 wbar^2 * const * (average of u - u): const = 6",
   is0(lin.subs(e_, 0) - c ** 2 * wb ** 2 * 6 * (sum(uj) / 6 - ux)))

# 1.6  principal part about ANY static background phi0: coefficient of a neighbour's eta_j is c^2 phi0_x^4 = c^2 w_x^2
etax = sp.symbols("eta_x", real=True)
etaj = sp.symbols("eta_1:7", real=True)
p0x = sp.symbols("p0x", positive=True)
p0j = sp.symbols("p0_1:7", positive=True)
eloc = sp.symbols("epsilon_loc", real=True)  # e = phi^2 * epsilon_loc (local energy density)
R = lambda P, Pj: c ** 2 * P ** 4 * (sum(Pj) - 6 * P) - (gam * c ** 2 / 2) * P ** 3 * (P ** 2 * eloc)
R_eps = R(p0x + eps * etax, [a + eps * b for a, b in zip(p0j, etaj)])
lin6 = sp.diff(R_eps, eps).subs(eps, 0)
ok("1.6 linearization about any background: coefficient of each neighbour = c^2 w_x^2 (w_x = phi0_x^2)",
   all(is0(sp.diff(lin6, q) - c ** 2 * p0x ** 4) for q in etaj))

# 1.7  dispersion omega^2 = c^2 wbar^2 E(k), group speed <= c wbar, = c wbar at k -> 0
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
Ek = sum(2 - 2 * sp.cos(k) for k in (k1, k2, k3))
g2 = sum(sp.diff(Ek, k) ** 2 for k in (k1, k2, k3)) / (4 * Ek)  # |grad sqrt(E)|^2
g2_half = sum((2 * sp.sin(k / 2) * sp.cos(k / 2)) ** 2 for k in (k1, k2, k3)) / sum(4 * sp.sin(k / 2) ** 2 for k in (k1, k2, k3))
ok("1.7a |grad_k sqrt(E)|^2 = sum sin^2(k/2)cos^2(k/2) / sum sin^2(k/2)  (<= 1 since cos^2 <= 1)",
   is0(sp.expand_trig(g2 - g2_half).rewrite(sp.exp)))
kk = sp.symbols("kk", positive=True)
ok("1.7b along an axis omega = 2 c wbar sin(k/2): group speed -> c wbar as k -> 0",
   sp.limit(sp.diff(c * wb * sp.sqrt(Ek.subs({k1: kk, k2: 0, k3: 0})), kk), kk, 0) == c * wb)

# ---------------------------------------------------------------- Step 2 (b)
x_, y_, z_, rho, beta = sp.symbols("x y z rho beta", positive=True)
useady = -1 / sp.sqrt(z_ ** 2 + (1 - beta ** 2) * (x_ ** 2 + y_ ** 2))
op = (1 - beta ** 2) * sp.diff(useady, z_, 2) + sp.diff(useady, x_, 2) + sp.diff(useady, y_, 2)
ok("2.1 V < c: steady co-moving field -1/sqrt(z'^2 + (1-V^2/c^2) rho^2) solves the steady law off the body", is0(op))

# 2.2 V = c: retarded time of a point source on the axis at speed c from t = 0; LW denominator = c t - z
tt, tr_ = sp.symbols("t t_r", positive=True)
zz = sp.symbols("zeta", real=True)
sol = sp.solve(sp.Eq((zz - c * tr_) ** 2 + rho ** 2, c ** 2 * (tt - tr_) ** 2), tr_)
den = [sp.simplify(c * (tt - s0) - (zz - c * s0)) for s0 in sol]
ok("2.2a V = c: Lienard-Wiechert denominator c(t - t_r) - (z - c t_r) = c t - z, independent of rho",
   all(is0(d - (c * tt - zz)) for d in den), f"t_r = {sol}")
aa = sp.symbols("a", positive=True)
Zeta = sp.symbols("Z", positive=True)  # Z = c t - z
growth = sp.integrate(sp.pi * (2 * c * tt - Zeta) * Zeta / Zeta ** 4, (Zeta, aa, 2 * c * tt))
ok("2.2b V = c: wake energy lower bound pi int (c^2t^2 - z^2)/(ct - z)^4 dz grows linearly in t",
   sp.limit(growth / tt, tt, sp.oo) == sp.pi * c / aa ** 2, f"integral = {sp.simplify(growth)}")

# 2.3 V > c: resonance c|k| = k.V has solutions (cone cos theta = c/V); V <= c: none except k = 0
V, th = sp.symbols("V theta", positive=True)
cth = sp.symbols("cos_theta", real=True)
res = lambda VV: sp.solveset(sp.Eq(c, VV * cth), cth, sp.Interval(-1, 1))
ok("2.3 resonance c|k| = |k| V cos(theta): no direction for V = c/2 or 9c/10; the cone cos(theta) = c/V for V = 2c; for V = c, theta = 0",
   res(c / 2) == sp.EmptySet and res(sp.Rational(9, 10) * c) == sp.EmptySet and res(2 * c) == sp.FiniteSet(sp.Rational(1, 2))
   and res(c) == sp.FiniteSet(1))
# 2.4 bodies of block 54's ray energy with a rest term: V(p) = p/sqrt(m^2+p^2) takes every value in [0,1)
m_, p_, V0 = sp.symbols("m p V0", positive=True)
Vp = p_ / sp.sqrt(m_ ** 2 + p_ ** 2)
ok("2.4 V(p) = p/sqrt(m^2+p^2): V^2 = V0^2 at p^2 = m^2 V0^2/(1-V0^2); 1 - V^2 = m^2/(m^2+p^2) > 0; V -> 1 as p -> oo",
   is0((Vp ** 2).subs(p_, m_ * V0 / sp.sqrt(1 - V0 ** 2)) - V0 ** 2) and is0(1 - Vp ** 2 - m_ ** 2 / (m_ ** 2 + p_ ** 2))
   and sp.limit(Vp, p_, sp.oo) == 1)

# ---------------------------------------------------------------- Step 3 (c) retarded kernel on the lattice
tt2, ss, nn = sp.symbols("t s n", positive=True)
# Laplace's method for e^{-2t} I_n(2t) = (1/pi) int_0^pi e^{-2t(1-cos th)} cos(n th) dth, th = s/sqrt(t)
ser_exp = sp.series(2 * tt2 * (1 - sp.cos(ss / sp.sqrt(tt2))), tt2, sp.oo, 2).removeO()
ok("3.1a 2t(1 - cos(s/sqrt t)) = s^2 - s^4/(12 t) + O(t^-2)", is0(sp.expand(ser_exp) - (ss ** 2 - ss ** 4 / (12 * tt2))))
ser_cos = sp.series(sp.cos(nn * ss / sp.sqrt(tt2)), tt2, sp.oo, 2).removeO()
ok("3.1b cos(n s/sqrt t) = 1 - n^2 s^2/(2t) + O(t^-2)", is0(sp.expand(ser_cos) - (1 - nn ** 2 * ss ** 2 / (2 * tt2))))
lap_int = sp.integrate(sp.exp(-ss ** 2) * (1 + ss ** 4 / (12 * tt2) - nn ** 2 * ss ** 2 / (2 * tt2)), (ss, 0, sp.oo)) / (sp.pi * sp.sqrt(tt2))
ok("3.1c e^{-2t}I_n(2t) = (4 pi t)^{-1/2} (1 - (4n^2-1)/(16 t) + O(t^-2))",
   is0(lap_int - (1 - (4 * nn ** 2 - 1) / (16 * tt2)) / sp.sqrt(4 * sp.pi * tt2)))
X1, X2, X3 = sp.symbols("x1 x2 x3", real=True)
c1 = sum(-(4 * q ** 2 - 1) / 16 for q in (X1, X2, X3))
ok("3.1d c1(x) = -|x|^2/4 + 3/16", is0(c1 - (-(X1 ** 2 + X2 ** 2 + X3 ** 2) / 4 + sp.Rational(3, 16))))
lam = sp.symbols("lambda", positive=True)
coef1 = (4 * sp.pi) ** sp.Rational(-3, 2) * sp.gamma(sp.Rational(-1, 2))
coef3 = (4 * sp.pi) ** sp.Rational(-3, 2) * sp.gamma(sp.Rational(-3, 2))
ok("3.2a lambda^1 coefficient (4pi)^{-3/2} Gamma(-1/2) = -1/(4 pi), the same at every site", is0(coef1 + 1 / (4 * sp.pi)))
r2 = sp.symbols("r2", nonnegative=True)
ok("3.2b lambda^3 coefficient c1(x) (4pi)^{-3/2} Gamma(-3/2) = -(|x|^2 - 3/4)/(24 pi)",
   is0(coef3 * (-r2 / 4 + sp.Rational(3, 16)) + (r2 - sp.Rational(3, 4)) / (24 * sp.pi)))
rr = sp.symbols("r", positive=True)
cont = sp.series(sp.exp(-lam * rr) / (4 * sp.pi * rr), lam, 0, 4).removeO()
ok("3.2c continuum comparator e^{-lam r}/(4 pi r) = 1/(4pi r) - lam/(4pi) + lam^2 r/(8pi) - lam^3 r^2/(24 pi) + ...",
   is0(cont - (1 / (4 * sp.pi * rr) - lam / (4 * sp.pi) + lam ** 2 * rr / (8 * sp.pi) - lam ** 3 * rr ** 2 / (24 * sp.pi))))
# 3.3 cross-check at x = 0 through the density of states: N(E) = E^{3/2}/(6 pi^2) (1 + (3/2)<h> E), <h> = <sum n^4>/12
thh, phh = sp.symbols("theta phi_a", real=True)
nvec = (sp.sin(thh) * sp.cos(phh), sp.sin(thh) * sp.sin(phh), sp.cos(thh))
avg_n4 = sp.integrate(sp.integrate(sum(q ** 4 for q in nvec) * sp.sin(thh), (phh, 0, 2 * sp.pi)), (thh, 0, sp.pi)) / (4 * sp.pi)
ok("3.3a <sum_j n_j^4> over the sphere = 3/5", is0(avg_n4 - sp.Rational(3, 5)))
Es = sp.symbols("E", positive=True)
hbar_ = avg_n4 / 12
NE = Es ** sp.Rational(3, 2) / (6 * sp.pi ** 2) * (1 + sp.Rational(3, 2) * hbar_ * Es)
DOS = sp.diff(NE, Es)
ok("3.3b density of states near E = 0: sqrt(E)/(4 pi^2) (1 + E/8)", is0(DOS - sp.sqrt(Es) / (4 * sp.pi ** 2) * (1 + Es / 8)))
om = sp.symbols("omega", positive=True)
img0 = sp.pi * DOS.subs(Es, om ** 2 / c ** 2)
odd0 = sp.im(sp.expand((-lam / (4 * sp.pi) + lam ** 3 * sp.Rational(3, 4) / (24 * sp.pi)).subs(lam, -sp.I * om / c)))
ok("3.3c Im g(0,omega) = pi DOS(omega^2/c^2) agrees with the lambda^1 and lambda^3 terms at x = 0", is0(img0 - odd0))
# 3.4 gradient of the lambda^3 term: grad_x sum_y (|x-y|^2 - 3/4) e_y = 2 (x Q - D); the lattice 3/4 exerts no pull
yv = sp.symbols("y1:4", real=True)
xv = (X1, X2, X3)
term = sum((a - b) ** 2 for a, b in zip(xv, yv)) - sp.Rational(3, 4)
ok("3.4 grad of (|x-y|^2 - 3/4) is 2(x - y): the lattice constant carries no pull",
   all(is0(sp.diff(term, a) - 2 * (a - b)) for a, b in zip(xv, yv)))

# numerical evidence for 3.1c on the 3D kernel (floating point; evidence)
from scipy.special import ive  # noqa: E402

worst = 0.0
for xx in ((0, 0, 0), (1, 0, 0), (2, 1, 0), (3, 2, 1)):
    cc1 = -sum(q * q for q in xx) / 4 + 3 / 16
    for T_ in (100.0, 400.0, 1600.0):
        pt = np.prod([ive(q, 2 * T_) for q in xx])
        rem = ((4 * np.pi * T_) ** 1.5 * pt - 1 - cc1 / T_) * T_ ** 2
        worst = max(worst, abs(rem))
ok("3.5 [executed] (4 pi t)^{3/2} p_t(x) - 1 - c1(x)/t is O(t^-2) at t = 100..1600", worst < 5.0, f"max |t^2 * remainder| = {worst:.3f}")

# ---------------------------------------------------------------- Step 4 (c) monopole: far charge = ledger
# 4.1 exact lattice check (block 56 T2(b), re-proved in ATTEMPT): box 5^3, interior 3^3, walls phi = 1
n = 3
idx = {(i, j, k): a for a, (i, j, k) in enumerate((i, j, k) for i in range(n) for j in range(n) for k in range(n))}
gq = sp.Rational(3, 2)
mv = {(0, 1, 1): sp.Rational(2, 3), (2, 1, 2): sp.Rational(5, 4), (1, 1, 1): sp.Rational(1, 7)}
A = sp.zeros(n ** 3, n ** 3)
bvec = sp.zeros(n ** 3, 1)
for s0, a in idx.items():
    A[a, a] = 6 + (gq / 2) * mv.get(s0, 0)  # -Lap phi + (gamma/2) m phi = 0  <=>  (12/gamma) phi (phi - avg) = -m phi^2
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        nb = tuple(q + dq for q, dq in zip(s0, d))
        if nb in idx:
            A[a, idx[nb]] -= 1
        else:
            bvec[a] += 1  # wall at phi = 1
phi_sol = A.LUsolve(bvec)
P = {s0: phi_sol[a] for s0, a in idx.items()}
get = lambda s0: P.get(s0, sp.Integer(1))
bonds = set()
for s0 in idx:
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        nb = tuple(q + dq for q, dq in zip(s0, d))
        bonds.add(tuple(sorted((s0, nb))))
Fb = (2 / gq) * sum((get(a) - get(b)) ** 2 for a, b in bonds)
He = sum(m0 * get(s0) ** 2 for s0, m0 in mv.items())  # e = m w = m phi^2 for bodies at rest
ledger = sp.nsimplify(He + Fb)
charge = sum(m0 * get(s0) for s0, m0 in mv.items())  # sum e/phi = sum m phi
flux = sum((1 - get(a if a in idx else b)) for a, b in bonds if (a in idx) != (b in idx))
ok("4.1a exact static lattice solution: ledger <H_w> + F = sum_x e_x/phi_x (far charge)", sp.simplify(ledger - charge) == 0,
   f"ledger = {sp.nsimplify(ledger)}")
ok("4.1b wall flux sum (1 - phi) = (gamma/2) x ledger (Gauss form of 'the far field reads the ledger')",
   sp.simplify(flux - gq / 2 * ledger) == 0)
ok("4.1c the naive linear-in-u charge sum e = sum m phi^2 differs from the ledger here", sp.simplify(He - ledger) != 0)

# 4.2 two point bodies (local units, wbar = 1): eps_A = m_A + T_A, phi(x_A) = 1 + u_B(x_A)/2, u_B(x_A) = -G m_B/r
G, mA, mB, TA, TB, r_ = sp.symbols("G m_A m_B T_A T_B r", positive=True)
uBA = -G * mB / r_
uAB = -G * mA / r_
U = -G * mA * mB / r_
Qeff = (mA + TA) * (1 + uBA / 2) + (mB + TB) * (1 + uAB / 2)
Qnaive = (mA + TA) * (1 + uBA) + (mB + TB) * (1 + uAB)
second = lambda ex: sp.Add(*[q for q in sp.expand(ex).as_ordered_terms() if not ((q.has(TA) or q.has(TB)) and q.has(G))])  # drop O(T G) = 1PN
ok("4.2a far charge sum eps phi = M + T + U (to the order of U)", is0(second(Qeff) - (mA + mB + TA + TB + U)))
ok("4.2b the linear-in-u source sum e/wbar = M + T + 2U", is0(second(Qnaive) - (mA + mB + TA + TB + 2 * U)))

# 4.3 local units: phi = sqrt(wbar) theta, tau = wbar t, e = w eps = wbar theta^2 eps turns Step 1.4 into
#     theta'' - 2 theta'^2/theta = c^2 theta^4 [Lap theta - (gamma/2) eps theta]   (wbar drops out)
epsl, Lth = sp.symbols("eps_loc Lap_theta", real=True)
th0, th1, th2 = sp.symbols("th0 th1 th2", real=True)  # theta, dtheta/dtau, d2theta/dtau2; d/dt = wbar d/dtau
# direct route: write theta(wbar t) derivatives by the chain rule
lhs_chain = sp.sqrt(wb) * wb ** 2 * th2 - 2 * (sp.sqrt(wb) * wb * th1) ** 2 / (sp.sqrt(wb) * th0)
rhs_chain = c ** 2 * (sp.sqrt(wb) * th0) ** 4 * sp.sqrt(wb) * Lth - (gam * c ** 2 / 2) * (sp.sqrt(wb) * th0) ** 3 * wb * th0 ** 2 * epsl
ok("4.3a local units: both sides of Step 1.4 scale as wbar^{5/2}, leaving theta'' - 2theta'^2/theta = c^2 theta^4 [Lap theta - (gamma/2) eps theta]",
   is0(lhs_chain / (sp.sqrt(wb) * wb ** 2) - (th2 - 2 * th1 ** 2 / th0))
   and is0(rhs_chain / (sp.sqrt(wb) * wb ** 2) - c ** 2 * th0 ** 4 * (Lth - gam / 2 * epsl * th0)))
# 4.3b rewriting as a wave equation with source sigma
sig = gam / 2 * epsl * th0 + (th2 * (th0 ** -4 - 1) - 2 * th1 ** 2 * th0 ** -5) / c ** 2
Lth_solved = sp.solve(sp.Eq(th2 - 2 * th1 ** 2 / th0, c ** 2 * th0 ** 4 * (Lth - gam / 2 * epsl * th0)), Lth)[0]
ok("4.3b (Lap - d^2/dtau^2 / c^2) theta = sigma, sigma = (gamma/2) eps theta + [theta''(theta^-4 - 1) - 2 theta'^2 theta^-5]/c^2",
   is0(Lth_solved - th2 / c ** 2 - sig))
# 4.4 the orbit-dependent part of sum delta^2 for two point fields: Phi(r) = C - 2 pi r solves Lap_r Phi = -4 pi / r
ok("4.4 Lap(-2 pi r) = -4 pi/r in three dimensions (the cross integral int dx/(|x-a||x-b|) = C - 2 pi |a-b|)",
   is0(sp.diff(rr ** 2 * sp.diff(-2 * sp.pi * rr, rr), rr) / rr ** 2 + 4 * sp.pi / rr))

# ---------------------------------------------------------------- Step 5 (c) dipole at leading order
rv = sp.Matrix(sp.symbols("r1:4", real=True))
rn = sp.sqrt(rv.dot(rv))
EA, EB, SA, SB = sp.symbols("E_A E_B S_A S_B", positive=True)
gradG = -rv / (4 * sp.pi * rn ** 3)  # grad of 1/(4 pi r)
pull_A = EA * SB * gam * gradG  # block 55 T3 with G0 -> 1/(4 pi r)
pull_B = EB * SA * gam * (-gradG)
tot = (pull_A + pull_B).subs({SA: EA, SB: EB})
ok("5.1 matched pulls: with S proportional to E the two pulls cancel (D'' = sum F = 0 at leading order)",
   all(is0(q) for q in tot) and not all(is0(q) for q in (pull_A + pull_B).subs({SA: 1, SB: 1})))

# ---------------------------------------------------------------- Step 6 (c) power at leading order
# 6.1 angular averages
nv = sp.Matrix(nvec)
avg_ang = lambda ex: sp.simplify(sp.integrate(sp.integrate(ex * sp.sin(thh), (phh, 0, 2 * sp.pi)), (thh, 0, sp.pi)) / (4 * sp.pi))
ok("6.1a <n_i n_j> = delta_ij/3", avg_ang(nv[0] ** 2) == sp.Rational(1, 3) and avg_ang(nv[0] * nv[1]) == 0)
ok("6.1b <n_i n_j n_k n_l> = (dd+dd+dd)/15", avg_ang(nv[0] ** 4) == sp.Rational(1, 5) and avg_ang(nv[0] ** 2 * nv[1] ** 2) == sp.Rational(1, 15))
J = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"J{min(i, j)}{max(i, j)}"))
lhs6 = avg_ang(sp.expand((nv.T * J * nv)[0] ** 2))
rhs6 = (2 * sum(J[i, j] ** 2 for i in range(3) for j in range(3)) + J.trace() ** 2) / 15
ok("6.1c <(n.J.n)^2> = (2 J:J + (tr J)^2)/15 for symmetric J", is0(lhs6 - rhs6))
# 6.2 flux prefactor: energy density (1/(2 gamma))(u'^2/c^2 + |grad u|^2) (local units), u = -(gamma/(4 pi R)) f
ok("6.2 power prefactor (1/gamma)(1/c)(gamma/(4 pi))^2 (4 pi) = G/c with G = gamma/(4 pi)",
   is0((1 / gam) * (1 / c) * (gam / (4 * sp.pi)) ** 2 * 4 * sp.pi - (gam / (4 * sp.pi)) / c))
# 6.3 Kepler averages (exact)
ee, ff, Mm, mu, a_ = sp.symbols("e f M mu a", positive=True)
pp = a_ * (1 - ee ** 2)
hh = sp.sqrt(G * Mm * pp)
rK = pp / (1 + ee * sp.cos(ff))
Dt = lambda X: sp.simplify(hh / rK ** 2 * sp.diff(X, ff))
xs, ys = rK * sp.cos(ff), rK * sp.sin(ff)
I = sp.Matrix([[mu * xs * xs, mu * xs * ys], [mu * xs * ys, mu * ys * ys]])
I3 = I.applyfunc(lambda X: Dt(Dt(Dt(X))))
II = sum(I3[i, j] ** 2 for i in range(2) for j in range(2))
trI3 = I3[0, 0] + I3[1, 1]
TK = 2 * sp.pi * a_ ** sp.Rational(3, 2) / sp.sqrt(G * Mm)


def orbit_avg(X):
    integrand = sp.expand(sp.expand_trig(sp.simplify(sp.expand(X * rK ** 2 / hh))))
    return sp.simplify(sp.integrate(integrand, (ff, 0, 2 * sp.pi)) / TK)


aII = orbit_avg(II)
atr = orbit_avg(trI3 ** 2)
Uk = -G * mu * Mm / rK
Ud = Dt(Uk)
ok("6.3a Lagrange-Jacobi on Kepler orbits: tr I''' = -2 dU/dt", is0(trI3 + 2 * Ud))
base = G ** 4 * mu ** 2 * Mm ** 3 / (a_ ** 5 * (1 - ee ** 2) ** sp.Rational(7, 2))
Pscalar = sp.simplify(G / 60 * (2 * aII + atr))  # times 1/c^5
ok("6.3b <P> c^5 = (16/15) G^4 mu^2 M^3/a^5 (1 + 99e^2/32 + 51e^4/128)/(1-e^2)^{7/2}",
   is0(Pscalar - sp.Rational(16, 15) * base * (1 + sp.Rational(99, 32) * ee ** 2 + sp.Rational(51, 128) * ee ** 4)))
Pcomp = sp.simplify(G / 5 * (aII - atr / 3))  # comparator's traceless quadrupole formula, times 1/c^5
ok("6.3c comparator check: (G/5)<Q''':Q'''> reproduces 32/5 (1 + 73e^2/24 + 37e^4/96)/(1-e^2)^{7/2}",
   is0(Pcomp - sp.Rational(32, 5) * base * (1 + sp.Rational(73, 24) * ee ** 2 + sp.Rational(37, 96) * ee ** 4)))
ok("6.3d circular orbits: scalar/comparator = 1/6", is0((Pscalar / Pcomp).subs(ee, 0) - sp.Rational(1, 6)))
extra = sp.simplify((G / c) * (orbit_avg(Ud ** 2) + orbit_avg(Ud * trI3) / (3 * c ** 2)))
ok("6.4 the linear-in-u reading adds (G/c)<(tr I''')^2>(1/4 - 1/(6c^2)) = spurious monopole power",
   is0(extra - (G / c) * atr * (sp.Rational(1, 4) - 1 / (6 * c ** 2))),
   f"= {sp.factor(sp.simplify(extra))}")
atr_closed = G ** 3 * Mm ** 3 * mu ** 2 * ee ** 2 * (4 + ee ** 2) / (2 * a_ ** 5 * (1 - ee ** 2) ** sp.Rational(7, 2))
ok("6.5 <(tr I''')^2> = G^3 M^3 mu^2 e^2 (4+e^2) / (2 a^5 (1-e^2)^{7/2}): zero on circles", is0(atr - atr_closed))

print(f"exact part done in {time.time() - T0:.1f} s")

# ---------------------------------------------------------------- E  executed lattice simulations (floating point)


def lap3(f):
    g = -6 * f
    g[1:] += f[:-1]
    g[:-1] += f[1:]
    g[:, 1:] += f[:, :-1]
    g[:, :-1] += f[:, 1:]
    g[:, :, 1:] += f[:, :, :-1]
    g[:, :, :-1] += f[:, :, 1:]
    return g


def evolve(n, gm, mfun, wbar, cc, dt, T, phi0, probes):
    """Full law of Step 1.4 in psi = 1/phi (no first-derivative term):
    psi'' = -c^2 phi^2 Lap(phi) + (gamma c^2/2) m phi^3   (bodies at rest, e = m phi^2); walls phi = sqrt(wbar)."""
    edge = np.sqrt(wbar)
    phi = phi0.copy()
    psi = 1 / phi
    psio = psi.copy()
    ts, out = [], []
    for s0 in range(int(round(T / dt)) + 1):
        tnow = s0 * dt
        ts.append(tnow)
        out.append([phi[p] for p in probes])
        lp = lap3(np.pad(phi, 1, constant_values=edge))[1:-1, 1:-1, 1:-1]
        psin = 2 * psi - psio + dt ** 2 * (-cc ** 2 * phi ** 2 * lp + (gm * cc ** 2 / 2) * mfun(tnow) * phi ** 3)
        psio, psi = psi, psin
        phi = 1 / psi
    return np.array(ts), np.array(out)


def halfrise(ts, y, y0, yinf):
    fr = (y - y0) / (yinf - y0)
    i = int(np.argmax(fr >= 0.5))
    if fr[i] < 0.5 or i == 0:
        return np.nan
    return ts[i - 1] + (0.5 - fr[i - 1]) / (fr[i] - fr[i - 1]) * (ts[i] - ts[i - 1])


from scipy.integrate import quad  # noqa: E402


def Glat(xx):
    f = lambda tq: np.prod([ive(abs(q), 2 * tq) for q in xx])
    Tt = 2000.0
    cc1 = -sum(q * q for q in xx) / 4 + 3 / 16
    head = sum(quad(f, lo, hi, limit=400, epsabs=1e-13, epsrel=1e-12)[0] for lo, hi in ((0, 5), (5, 50), (50, 400), (400, Tt)))
    return head + (4 * np.pi) ** -1.5 * (2 / np.sqrt(Tt) + cc1 * (2 / 3) * Tt ** -1.5)


# E1: a source switched on at t = 0; front speed at two ambient rates, same step in lattice time
n = 49
C = n // 2
rs = [6, 8, 10, 12, 14, 16, 18]
G0 = Glat((0, 0, 0))
Gr = [Glat((q, 0, 0)) for q in rs]
ok("E1.0 [executed] lattice G(0) = 0.2527310...", abs(G0 - 0.252731009858) < 1e-9, f"G(0) = {G0:.12f}")
speeds = {}
for m0 in (0.02, 6.0):
    for wbar in (1.0, 2.0):
        msite = np.zeros((n, n, n))
        msite[C, C, C] = m0
        # free-space static value behind the front (one body: phi/sqrt(wbar) = 1 - (gamma/2) m G(x)/(1 + (gamma/2) m G(0)))
        th_inf = [1 - 0.5 * m0 * g / (1 + 0.5 * m0 * G0) for g in Gr]
        probes = [(C + q, C, C) for q in rs]
        ts, out = evolve(n, 1.0, lambda tq: msite, wbar, 1.0, 0.1, 26 / wbar, np.full((n, n, n), np.sqrt(wbar)), probes)
        th = [halfrise(ts, out[:, i], np.sqrt(wbar), np.sqrt(wbar) * th_inf[i]) for i in range(len(rs))]
        sl = np.polyfit(rs, th, 1)
        speeds[(m0, wbar)] = 1 / sl[0]
        print(f"EXEC E1 m={m0} wbar={wbar}: half-rise times at r={rs}: {np.round(th, 3).tolist()}  fitted speed {1 / sl[0]:.4f} sites per unit t")
for m0 in (0.02, 6.0):
    s1, s2 = speeds[(m0, 1.0)], speeds[(m0, 2.0)]
    ok(f"E1.{'a' if m0 < 1 else 'b'} [executed] front speed = c x ambient rate within 3% at wbar = 1 and 2 (source m = {m0})",
       abs(s1 - 1) < 0.03 and abs(s2 - 2) < 0.06 and abs(s2 / s1 - 2) < 0.01, f"speeds {s1:.4f}, {s2:.4f}, ratio {s2 / s1:.4f}")

# E2: the LOCAL rate: a weak probe pulse passing a held well of slow clocks is delayed by int (1/w - 1) dl / c
import scipy.sparse.linalg as spl  # noqa: E402


def static_theta(nn_, gm, mfield):
    shp = (nn_,) * 3

    def mvv(v):
        f = v.reshape(shp)
        return (-(lap3(np.pad(f, 1))[1:-1, 1:-1, 1:-1]) + (gm / 2) * mfield * f).ravel()

    Aop = spl.LinearOperator((nn_ ** 3, nn_ ** 3), matvec=mvv, dtype=float)
    b = np.zeros(shp)
    for ax in range(3):
        sl0 = [slice(None)] * 3
        sl0[ax] = 0
        b[tuple(sl0)] += 1
        sl0[ax] = -1
        b[tuple(sl0)] += 1
    xsol, info = spl.cg(Aop, b.ravel(), rtol=1e-12, maxiter=5000)
    assert info == 0
    return xsol.reshape(shp)


n = 61
C = n // 2
Xg, Yg, Zg = np.meshgrid(*(np.arange(n) - C,) * 3, indexing="ij")
bimp, Lh = 5, 16
peaks = {}
preds = {}
wimp = {}
for mB in (0.0, 0.01, 0.02, 0.05, 0.1):
    mfB = np.where(Xg ** 2 + Yg ** 2 + Zg ** 2 <= 9, mB, 0.0)
    thB = static_theta(n, 1.0, mfB) if mB > 0 else np.ones((n, n, n))
    mfP = np.zeros((n, n, n))
    mfP[C - Lh, C + bimp, C] = 0.05
    ts, out = evolve(n, 1.0, lambda tq: mfB + (mfP if tq < 2.0 else 0.0), 1.0, 1.0, 0.2, 2 * Lh + 30, thB,
                     [(C + Lh, C + bimp, C)])
    d = thB[C + Lh, C + bimp, C] - out[:, 0]
    i = int(np.argmax(d))
    peaks[mB] = ts[i] + 0.5 * 0.2 * (d[i - 1] - d[i + 1]) / (d[i - 1] - 2 * d[i] + d[i + 1])
    wimp[mB] = float(thB[C, C + bimp, C] ** 2)
    line = thB[C - Lh:C + Lh + 1, C + bimp, C] ** 2
    preds[mB] = float(np.sum((1 / line[1:] - 1) + (1 / line[:-1] - 1)) / 2)
worst_rel = 0.0
for mB in (0.01, 0.02, 0.05, 0.1):
    dly = peaks[mB] - peaks[0.0]
    worst_rel = max(worst_rel, abs(dly / preds[mB] - 1))
    print(f"EXEC E2 held well m_B={mB} per site on a ball of radius 3: w at the ray's closest point = {wimp[mB]:.4f}  "
          f"measured delay {dly:.3f}  straight-ray int(1/w - 1) dl = {preds[mB]:.3f}")
ok("E2 [executed] a probe pulse through slow clocks is delayed by the straight-ray integral of (1/w - 1)/c within 12%",
   worst_rel < 0.12, f"worst relative deviation {worst_rel:.3f}")

print(f"total {time.time() - T0:.1f} s; PASS={NPASS} FAIL={NFAIL}")
if NFAIL:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NFAIL} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (a) weak-field law u'' = c^2 wbar^2 Lap u - gamma c^2 wbar e, const 6 in the (average - u) form, "
      "principal part c^2 w_x^2 Lap about every static background (c sites per local tick); (b) c is fixed by neither "
      "covariance nor scale covariance; 'no ever-growing wake for every body' is c >= 1, an inequality; (c) the lattice "
      "retarded kernel's odd part is -lam/(4pi) (the same at every site) and -lam^3(|x|^2 - 3/4)/(24pi); the far field's "
      "monopole charge is the ledger, so the monopole is silent at leading order (the linear-in-u reading radiates "
      "spuriously); the dipole is silent at leading order by matched pulls; leading power (G/(60c^5))<2 I''':I''' + (tr I''')^2> "
      "= (16/15)(G^4 mu^2 M^3/(c^5 a^5))(1 + 99e^2/32 + 51e^4/128)/(1-e^2)^{7/2}, 1/6 of the comparator at e = 0")
print("HIT: within blocks 53-57's supplied clauses, the rate field's motion referred to the wall clocks has local speed "
      "c w_x (principal part, every background); no-growing-wake for all bodies is exactly c >= 1 (continuum level); "
      "the far monopole charge equals the ledger, so two circling point bodies radiate at leading order only through the "
      "scalar quadrupole with trace: <P> = (16/15) G^4 mu^2 M^3 (1 + 99e^2/32 + 51e^4/128)/(c^5 a^5 (1-e^2)^{7/2}), "
      "G = gamma/(4 pi), local units; the lattice retarded kernel's odd terms are -lam/(4 pi) and -lam^3 (|x|^2 - 3/4)/(24 pi)")
