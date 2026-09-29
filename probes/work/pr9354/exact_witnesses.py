"""PR 9354 attack-a: WITNESS REALIZABILITY for the two finite-projection notes (finite path guide dependence; mixed energy and curvature target).

Every explicit witness the notes state is rebuilt in exact arithmetic (sympy rationals / symbolic exponentials, fractions.Fraction) with own code:
 first note : the two-state guide table at T = log(2)/2 and T = log 2 (marginals, local energies, means -1, -17/19, -35/37, differences 2/19, 2/37, propagators [[3,1],[1,3]] and [[5/4,3/4],[3/4,5/4]]);
              the noncommuting-cap example H = [[0,-1],[-1,1]], J = 0, Delta = log 2, M = 2 (C = diag(1, 1/4), endpoint -3/4 versus Rayleigh -1/2); the overcount 512 c^2 Var(Y) by enumeration;
 second note: E_mix for guides (1,1) and (1,2), the closed form -(9 exp(2t)+1)/(9 exp(2t)-1) and its value -19/17 at t = log(2)/2, the changed right boundary p0 = (1/5, 4/5) giving -17/19,
              the single-walker stationary energy -4/5, the curvature example (a = 1, c = 2, beta = 1/2, t = log(2)/2: susceptibilities 5/2 and 2 versus the ground value 4),
              the stencil algebra (A - 4 C H1^4; -7 L1/(6 H1) - 2 L3 H1/3; the exact 14 h M numerator) and the source-mapping counts (ages 7.515 .. 30, 1500 terms).
"""
import itertools, sys
from fractions import Fraction as Fr
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)
R = sp.Rational
t, h = sp.symbols("t h", positive=True)

def expmH(H, T):
    """exp(-T H) for a symmetric 2x2 with H^2 = gamma^2 I (or a diagonal) via exact spectral form"""
    return sp.simplify((-T * H).exp())

# ---------------- first note: guide table
H = sp.Matrix([[0, -1], [-1, 0]])
def endpoint(H, psi, T):
    G = sp.simplify(sp.exp(-T * H).rewrite(sp.cosh)) if False else sp.simplify((-T * H).exp())
    psi = sp.Matrix(psi)
    Z = sp.simplify((psi.T * G * psi)[0])
    marg = [sp.simplify(psi[i] * (G * psi)[i] / Z) for i in range(2)]
    EL = [sp.simplify((H * psi)[i] / psi[i]) for i in range(2)]
    mean = sp.simplify(sum(m * e for m, e in zip(marg, EL)))
    return G, Z, marg, EL, mean
G1, Z1, m1, E1, mean1 = endpoint(H, (1, 1), sp.log(2) / 2)
G2, Z2, m2, E2, mean2 = endpoint(H, (1, 2), sp.log(2) / 2)
prop = sp.simplify(G2 * 2 * sp.sqrt(2))
check("T = log(2)/2: propagator proportional to [[3,1],[1,3]]; guide (1,1): marginal (1/2,1/2), local energies (-1,-1), mean -1", sp.simplify(prop - sp.Matrix([[3, 1], [1, 3]])) == sp.zeros(2) and m1 == [R(1, 2), R(1, 2)] and E1 == [-1, -1] and mean1 == -1)
check("T = log(2)/2, guide (1,2): marginal (5/19, 14/19), local energies (-2, -1/2), mean -17/19, difference 2/19", m2 == [R(5, 19), R(14, 19)] and E2 == [-2, R(-1, 2)] and mean2 == R(-17, 19) and mean2 - mean1 == R(2, 19), f"{m2}, {E2}, {mean2}")
G3, Z3, m3, E3, mean3 = endpoint(H, (1, 2), sp.log(2))
check("T = log 2: propagator [[5/4,3/4],[3/4,5/4]], guide (1,2) mean -35/37, difference 2/37", sp.simplify(G3 - sp.Matrix([[R(5, 4), R(3, 4)], [R(3, 4), R(5, 4)]])) == sp.zeros(2) and mean3 == R(-35, 37) and mean3 + 1 == R(2, 37), f"{mean3}")
# ---------------- cap example
Hc = sp.Matrix([[0, -1], [-1, 1]]); Delta = sp.log(2)
K0 = sp.diag(1, sp.exp(-Delta * 1))                      # zero-jump paths: exp(-Delta D), D = diag(0, 1)
C = (K0 ** 2).applyfunc(sp.simplify)
psi = sp.Matrix([1, 2])
Ecap = sp.simplify((psi.T * Hc * C * psi)[0] / (psi.T * C * psi)[0])
sq = C.applyfunc(sp.sqrt) if False else sp.diag(1, R(1, 2))
u = sq * psi; Ray = sp.simplify((u.T * Hc * u)[0] / (u.T * u)[0])
E0c = min(sp.N(x) for x in Hc.eigenvals())
check("cap example: C = diag(1, 1/4), endpoint averaging -3/4, Rayleigh quotient of sqrt(C) psi -1/2", C == sp.diag(1, R(1, 4)) and Ecap == R(-3, 4) and Ray == R(-1, 2), f"C = {C.tolist()}, {Ecap}, {Ray}")
print(f"   (for scale) ground energy of H = [[0,-1],[-1,1]] is {float(E0c):.6f}; the capped endpoint value -0.75 lies BELOW it; the note compares only with the Rayleigh value -1/2")
# ---------------- covariance overcount by enumeration
import random
random.seed(9354)
c = Fr(3, 7)
ok = True
for _ in range(200):
    def rv(): return [(Fr(random.randint(-5, 5), random.randint(1, 4)), Fr(random.randint(1, 5))) for _ in range(random.randint(1, 3))]
    def dist(v):
        tot = sum(w for _, w in v); return [(x, w / tot) for x, w in v]
    Xa, Xb, Za, Zb, Y = (dist(rv()) for _ in range(5))
    def var_of(fn):
        pts = []
        for (xa, pa), (xb, pb), (za, pza), (zb, pzb), (y, py) in itertools.product(Xa, Xb, Za, Zb, Y):
            pts.append((fn(xa, xb, za, zb, y), pa * pb * pza * pzb * py))
        m = sum(v * p for v, p in pts); return sum(p * (v - m) ** 2 for v, p in pts)
    va = var_of(lambda xa, xb, za, zb, y: c * (15 * xa - 16 * y + za)); vb = var_of(lambda xa, xb, za, zb, y: c * (15 * xb - 16 * y + zb))
    vd = var_of(lambda xa, xb, za, zb, y: c * (15 * xa - 16 * y + za) - c * (15 * xb - 16 * y + zb))
    varY = var_of(lambda xa, xb, za, zb, y: y)
    ok &= (va + vb - vd == 512 * c * c * varY)
check("with mutually independent X_a, X_b, Z_a, Z_b, Y: Var(chi_a) + Var(chi_b) - Var(chi_a - chi_b) = 512 c^2 Var(Y) exactly (200 random rational instances)", ok)

# ---------------- second note
tt = sp.symbols("tt", positive=True)
def Emix(H, psi, p0, T):
    psi = sp.Matrix(psi); p0 = sp.Matrix(p0)
    chi = sp.diag(*[1 / x for x in psi]) * p0
    G = sp.simplify((-T * H).exp())
    Z = sp.simplify((psi.T * G * chi)[0])
    return sp.simplify((psi.T * H * G * chi)[0] / Z)
Em11 = Emix(H, (1, 1), (R(1, 2), R(1, 2)), tt); Em12 = Emix(H, (1, 2), (R(1, 2), R(1, 2)), tt)
closed = -(9 * sp.exp(2 * tt) + 1) / (9 * sp.exp(2 * tt) - 1)
check("guide (1,1): E_mix = -1 for all t; guide (1,2): E_mix = -(9 exp(2t)+1)/(9 exp(2t)-1) (symbolic in t)", sp.simplify(Em11 + 1) == 0 and sp.simplify(Em12.rewrite(sp.exp) - closed) == 0, str(sp.simplify(Em12)))
val = sp.simplify(closed.subs(tt, sp.log(2) / 2))
check("at t = log(2)/2 the (1,2) value is -19/17, strictly below the ground energy -1", val == R(-19, 17) and val < -1, str(val))
alt = Emix(H, (1, 2), (R(1, 5), R(4, 5)), sp.log(2) / 2)
check("replacing p0 by (1/5, 4/5) changes the same-guide answer to -17/19", alt == R(-17, 19), str(alt))
# single walker stationary energy
psi2 = sp.Matrix([1, 2]); var_e = sp.simplify((psi2.T * H * psi2)[0] / (psi2.T * psi2)[0])
check("single-walker stationary energy psi^T H psi / psi^T psi = -4/5 for guide (1,2) (ground energy -1)", var_e == R(-4, 5), str(var_e))
# proposal chain check: Q, detailed balance and the limit
Q = sp.zeros(2)
for x in range(2):
    for y in range(2):
        if x != y: Q[x, y] = -H[y, x] * psi2[y] / psi2[x]
    Q[x, x] = -sum(Q[x, y] for y in range(2) if y != x)
pi = sp.Matrix([R(1, 5), R(4, 5)])
check("proposal generator Q has detailed balance with pi = psi^2/sum psi^2 = (1/5, 4/5) and pi^T Q = 0", sp.simplify(pi.T * Q) == sp.zeros(1, 2) and sp.simplify(pi[0] * Q[0, 1] - pi[1] * Q[1, 0]) == 0, f"Q = {Q.tolist()}")
EL = [(H * psi2)[i] / psi2[i] for i in range(2)]
check("its limiting energy sum_x pi(x) E_L(x) equals -4/5", sp.simplify(sum(pi[i] * EL[i] for i in range(2))) == R(-4, 5))
# curvature example
a, cc, beta, hh, tt2 = sp.symbols("a c beta h t2", positive=True)
gam = sp.sqrt(a ** 2 + cc ** 2 * hh ** 2); Cc = sp.cosh(2 * beta * hh)
E4 = -gam * (a * Cc + gam * sp.tanh(gam * tt2)) / (gam + a * Cc * sp.tanh(gam * tt2))
chi_mix = sp.simplify(-sp.diff(E4, hh, 2).subs(hh, 0))
formula = (cc ** 2 / a) * (1 - sp.exp(-2 * a * tt2)) + 4 * a * beta ** 2 * sp.exp(-2 * a * tt2)
check("the second derivative of eq. (4) at h = 0 reproduces eq. (5): chi_mix(t) = (c^2/a)(1 - e^{-2at}) + 4 a beta^2 e^{-2at} (symbolic)", sp.simplify((chi_mix - formula).rewrite(sp.exp)) == 0)
# eq (4) against the matrix definition (3) at a numeric point
Hh = sp.Matrix([[cc * hh, -a], [-a, -cc * hh]]); psih = sp.Matrix([sp.exp(beta * hh), sp.exp(-beta * hh)])
vals = {a: 1, cc: 2, beta: R(1, 2), hh: R(3, 10), tt2: sp.log(2) / 2}
chi_v = sp.diag(1 / psih[0], 1 / psih[1]) * sp.Matrix([R(1, 2), R(1, 2)])
Gh = sp.simplify((-tt2 * Hh).exp()) if False else None
import mpmath as mp
mp.mp.dps = 40
def emix_num(av, cv, bv, hv, tv):
    Hm = mp.matrix([[cv * hv, -av], [-av, -cv * hv]]); ps = mp.matrix([mp.e ** (bv * hv), mp.e ** (-bv * hv)]); ch = mp.matrix([mp.mpf(1) / 2 / ps[0], mp.mpf(1) / 2 / ps[1]])
    G = mp.expm(-tv * Hm); Z = (ps.T * G * ch)[0]; return (ps.T * Hm * G * ch)[0] / Z
tv = mp.log(2) / 2
e_num = emix_num(1, 2, mp.mpf(1) / 2, mp.mpf(3) / 10, tv)
e_form = E4.subs({a: 1, cc: 2, beta: R(1, 2), hh: R(3, 10), tt2: sp.log(2) / 2})
check("eq. (4) equals the matrix definition (3) at (a, c, beta, h, t) = (1, 2, 1/2, 3/10, log(2)/2) to 30 digits", abs(e_num - mp.mpf(sp.N(e_form, 50))) < mp.mpf(10) ** -30, f"{mp.nstr(e_num, 20)}")
v52 = sp.simplify(chi_mix.subs({a: 1, cc: 2, beta: R(1, 2), tt2: sp.log(2) / 2})); v2 = sp.simplify(chi_mix.subs({a: 1, cc: 2, beta: 0, tt2: sp.log(2) / 2}))
vg = sp.simplify((cc ** 2 / a).subs({a: 1, cc: 2}))
check("a = 1, c = 2, beta = 1/2, t = log(2)/2: susceptibilities 5/2 (guide beta = 1/2) and 2 (uniform guide), ground susceptibility 4", v52 == R(5, 2) and v2 == 2 and vg == 4, f"{v52}, {v2}, {vg}")
# zero-field energy exact at every age for both guides
E40 = sp.simplify(E4.subs(hh, 0))
check("both guides have E_mix(t, h = 0) = -a for every t", sp.simplify(E40 + a) == 0)
# ---------------- stencil algebra
E0_, A, B, Cq, L1, L3, H1 = sp.symbols("E0 A B C L1 L3 H1")
Eb = lambda x: E0_ - A * x ** 2 - B * x ** 4 - Cq * x ** 6 + L1 * x + L3 * x ** 3
num = sp.expand(15 * Eb(0) - 16 * Eb(H1) + Eb(2 * H1))
even = sp.expand((num.subs({L1: 0, L3: 0}) / (12 * H1 ** 2)))
odd = sp.expand((num - num.subs({L1: 0, L3: 0})) / (12 * H1 ** 2))
check("stencil algebra: even part A - 4 C H1^4 (no B term); odd part -7 L1/(6 H1) - 2 L3 H1/3", sp.simplify(even - (A - 4 * Cq * H1 ** 4)) == 0 and sp.simplify(odd - (-7 * L1 / (6 * H1) - 2 * L3 * H1 / 3)) == 0, f"even {even}, odd {odd}")
Aa, M = sp.symbols("Aa M")
lin = lambda x: Aa - x * M
check("one-walker linear energy A - h M: the three-field numerator is exactly 14 h M", sp.expand(15 * lin(0) - 16 * lin(H1) + lin(2 * H1)) == 14 * H1 * M)
# source-mapping counts
ages = [Fr(15, 1000) * j for j in range(501, 2001)]
check("PR9356 mapping: (1/1500) sum over j = 501..2000 of E_mix(.015 j): 1500 terms, ages 7.515 through 30", len(ages) == 1500 and ages[0] == Fr(7515, 1000) and ages[-1] == 30 and 2000 - 2000 // 4 == 1500)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9354 (both notes): the two-state tables (-17/19, -35/37, 2/19, 2/37), the cap example (-3/4 versus -1/2; note: -3/4 is below the ground energy {float(E0c):.4f}), overcount 512 c^2 Var(Y), E_mix -19/17 and -17/19, single-walker -4/5, curvature 5/2 / 2 / 4, stencil algebra and 1500 ages all exist and reproduce exactly; PASS={PASS} FAIL={FAIL}; no defect in the notes' witnesses")
sys.exit(1 if FAIL else 0)
