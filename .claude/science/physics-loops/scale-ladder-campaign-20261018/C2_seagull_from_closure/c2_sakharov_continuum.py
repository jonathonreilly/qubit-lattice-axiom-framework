#!/usr/bin/env python3
"""C2 part 2 (continuum, exact sympy): which contact term restores the Ward identity, and what induced 1/G results.

Euclidean d = 4, real scalar, background g = delta + h, h(x) = eps (A e^{ik.x} + B e^{-ik.x}) (A, B symmetric, symbolic).
One-loop W[h] = 1/2 Tr log O,  regularised by proper time:  W = -1/2 int_{1/L2}^inf ds/s Tr e^{-s O}  (L2 = Lambda^2),
Tr e^{-sO} to second order by Duhamel:  -s Tr(O2 e^{-s O0}) + s^2 int_0^1 du Tr(O1^B e^{-us O0} O1^A e^{-(1-u)s O0}).
Gaussian loop integrals done exactly (shift p = q - u k, moments by exp(lap_q/(4s))).  Everything below is computed, the
expected constants are the textbook heat-kernel values (DeWitt; Gilkey a1 = (1/6 - zeta) R), quoted, not fitted.

O = Delta_g + zeta R  (covariant Laplace-type operator on scalars; the proper-time cutoff on it is a covariant regulator)
O = D := sqrt(g) (Delta_g + zeta R)  (the flat-measure Hessian of S = 1/2 int sqrt g (g^{mn} dphi dphi + zeta R phi^2):
          its vertices are exactly the closure-forced couplings of c2_closure.py, its seagull D2 is the closure seagull;
          proper time on D is NOT a covariant regulator)

Checks
  P1  D2 (the closure-forced minimal seagull, zeta = 0) is k-independent: its tadpole is a pure Pi(0) contact term.
      Delta_2 (covariant operator) is k-dependent: the k^2 contact terms come from the measure factor g^{-1/2}.
  P2  O = Delta_g + zeta R: W^(2) at order k^0 = -L2^2/(64 pi^2) [sqrt g]^(2)  and at order k^2
      = -(1/6 - zeta) L2/(32 pi^2) [sqrt g R]^(2): Ward identity exact, induced 1/(16 pi G) = (1/6 - zeta) L2/(32 pi^2)
  P3  zeta enters 1/G linearly with slope -L2/(32 pi^2) = -<phi^2>/2 (zeta is the closure-free direction of S4)
  P4  O = D (closure seagull + non-covariant proper-time regulator): the k^2 symbol is NOT transverse (Ward ratio printed)
"""
from __future__ import annotations
import time, itertools
import numpy as np
import sympy as sp

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


I = sp.I
d = 4
R4 = range(d)
k = sp.symbols("k0:4", real=True)
p = sp.symbols("p0:4", real=True)
q = sp.symbols("q0:4", real=True)
Z, eps, s, u, tau, L2, zeta = sp.symbols("Z eps s u tau L2 zeta")
IDX = [(a, b) for a in R4 for b in R4 if a <= b]
Asym = {ab: sp.Symbol(f"A{ab[0]}{ab[1]}") for ab in IDX}
Bsym = {ab: sp.Symbol(f"B{ab[0]}{ab[1]}") for ab in IDX}
A = sp.Matrix(d, d, lambda i, j: Asym[(min(i, j), max(i, j))])
B = sp.Matrix(d, d, lambda i, j: Bsym[(min(i, j), max(i, j))])
H = eps * (A * Z + B / Z)


def trunc(e, n=2):
    e = sp.expand(e)
    return sum(e.coeff(eps, j) * eps ** j for j in range(n + 1))


def Dx(e, mu):
    """d/dx_mu on a Laurent polynomial in Z (Z = e^{ik.x})."""
    e = sp.expand(e)
    out = 0
    for t in sp.Add.make_args(e):
        n = t.as_powers_dict().get(Z, 0)
        out += t * I * n * k[mu]
    return sp.expand(out)


g = sp.eye(d) + H
gi = (sp.eye(d) - H + H * H).applyfunc(trunc)
trH = H.trace()
sqrtg = trunc(1 + trH / 2 + trH ** 2 / 8 - (H * H).trace() / 4)
isqrtg = trunc(1 - trH / 2 + trH ** 2 / 8 + (H * H).trace() / 4)
# check the two square-root series against each other
assert trunc(sp.expand(sqrtg * isqrtg)) == 1


def ricci_scalar():
    dg = [[[Dx(g[a, b], c) for c in R4] for b in R4] for a in R4]
    Gam = [[[trunc(sum(gi[l, m] * (dg[m][a][b] + dg[m][b][a] - dg[a][b][m]) for m in R4) / 2)
             for b in R4] for a in R4] for l in R4]
    R = 0
    for a in R4:
        for b in R4:
            Rab = sum(Dx(Gam[l][a][b], l) - Dx(Gam[l][a][l], b) for l in R4)
            Rab += sum(Gam[l][l][m] * Gam[m][a][b] - Gam[l][b][m] * Gam[m][a][l] for l in R4 for m in R4)
            R += gi[a, b] * trunc(Rab)
    return trunc(R)


print("   building R ...", flush=True)
Rs = ricci_scalar()
sgR = trunc(sqrtg * Rs)


def part(e, epow, zpow):
    e = sp.expand(e).coeff(eps, epow)
    e = sp.expand(e * Z ** 2)     # shift so that powers are non-negative
    return sp.expand(e.coeff(Z, zpow + 2))


# operator symbols acting on e^{ip.x}: O e^{ipx} = [sum_n c_n(p) Z^n] e^{ipx}
ip = [I * p[m] for m in R4]


def sym_Delta(with_measure=True, density=False):
    """symbol of Delta_g + zeta R (with_measure) or of D = sqrt g (Delta_g + zeta R) (density=True)."""
    if density:
        # D phi = -d_m (sqrt g g^{mn} d_n phi) + zeta sqrt g R phi
        W = (sqrtg * gi).applyfunc(trunc)
        out = 0
        for m in R4:
            for n in R4:
                out += -(Dx(W[m, n], m) * ip[n] + W[m, n] * ip[m] * ip[n])
        out += zeta * sgR
        return trunc(out)
    W = (sqrtg * gi).applyfunc(trunc)
    out = 0
    for m in R4:
        for n in R4:
            out += -gi[m, n] * ip[m] * ip[n] - trunc(isqrtg * Dx(W[m, n], m)) * ip[n]
    out += zeta * Rs
    return trunc(out)


def gauss(f):
    """int d^4q/(2pi)^4 f(q) e^{-s q^2} for polynomial f."""
    f = sp.expand(f)
    out = 0
    term = f
    n = 0
    while term != 0:
        out += term.subs({qq: 0 for qq in q}) / (4 * s) ** n / sp.factorial(n)
        term = sp.expand(sum(sp.diff(term, qq, 2) for qq in q))
        n += 1
    return sp.expand(out / (16 * sp.pi ** 2 * s ** 2))


def W2(sym):
    """AB-coefficient of W = -1/2 int ds/s Tr e^{-s O}, to order k^2 (k -> tau k)."""
    O1A = part(sym, 1, 1)                 # <p+k|O1|p>
    O1B = part(sym, 1, -1)                # <p-k|O1|p>
    O2 = part(sym, 2, 0)                  # <p|O2|p>
    O1B_pk = O1B.subs({p[m]: p[m] + k[m] for m in R4}, simultaneous=True)   # <p|O1|p+k>
    sh = {p[m]: q[m] - u * k[m] for m in R4}
    bub = sp.expand((O1B_pk * O1A).subs(sh, simultaneous=True))
    k2 = sum(kk ** 2 for kk in k)
    expo = sp.expand(1 - s * u * (1 - u) * k2 * tau ** 2)
    sc = {kk: tau * kk for kk in k}
    bubt = sp.expand(sp.expand(bub.subs(sc, simultaneous=True)) * expo)
    bubt = sum(bubt.coeff(tau, j) for j in range(3))  # orders tau^0..2 (tau set to 1)
    Tb = sp.integrate(gauss(bubt), (u, 0, 1))
    sea = sp.expand(O2.subs({p[m]: q[m] for m in R4}).subs(sc, simultaneous=True))
    sea = sum(sea.coeff(tau, j) for j in range(3))
    Ts = gauss(sea)
    T = sp.expand(s ** 2 * Tb - s * Ts)
    # -1/2 int_{1/L2} ds/s s^a = -1/2 * L2^(-a) * (-1/a)   (a < 0); a = 0 would be log divergent
    out = 0
    for t in sp.Add.make_args(T):
        a = t.as_powers_dict().get(s, 0)
        assert a < 0, f"log-divergent term s^{a}"
        out += -sp.Rational(1, 2) * (t / s ** a) * L2 ** (-a) * (-sp.Rational(1, 1) / a)
    return sp.expand(out), O2


def korder(e, n):
    sc = {kk: tau * kk for kk in k}
    return sp.expand(sp.expand(e.subs(sc, simultaneous=True)).coeff(tau, n))


print("   symbols ...", flush=True)
symO = sym_Delta()
symD = sym_Delta(density=True)

# P1
O2_D = part(symD.subs(zeta, 0), 2, 0)
O2_O = part(symO.subs(zeta, 0), 2, 0)
kfreeD = not any(O2_D.has(kk) for kk in k)
kdepO = any(O2_O.has(kk) for kk in k)
check("P1", kfreeD and kdepO, "the closure-forced minimal seagull D2 (second order of sqrt g g^{mn} p p) is k-independent, so "
      "its tadpole is a pure Pi(0) contact term and cannot change the k^2 symbol; the covariant operator's O2 is "
      "k-dependent only through the measure factor g^{-1/2}")

# P2 / P3
print("   W2 for the covariant operator ...", flush=True)
WO, _ = W2(symO)
EH = part(sgR, 2, 0)
CC = part(sqrtg, 2, 0)
W0 = korder(WO, 0)
Wk2 = korder(WO, 2)
r0 = sp.simplify(W0 + L2 ** 2 / (64 * sp.pi ** 2) * CC)
r2 = sp.simplify(sp.expand(Wk2 + (sp.Rational(1, 6) - zeta) * L2 / (32 * sp.pi ** 2) * EH))
odd = sp.expand(korder(WO, 1))
check("P2", r0 == 0 and r2 == 0 and odd == 0,
      "covariant regulator: W^(2) = -L2^2/(64 pi^2)[sqrt g]^(2) - (1/6 - zeta) L2/(32 pi^2) [sqrt g R]^(2) + O(k^4), "
      "exactly (all 20x20 A.B coefficients); Ward identity exact; induced 1/(16 pi G) = (1/6 - zeta) Lambda^2/(32 pi^2) "
      "per real scalar")
# Ward identity explicitly: A pure gauge
xi = sp.symbols("xi0:4")
gaugeA = {Asym[(a, b)]: k[a] * xi[b] + k[b] * xi[a] for (a, b) in IDX}
wardO = sp.expand(Wk2.subs(gaugeA, simultaneous=True))
dz = sp.diff(Wk2, zeta)
check("P3", wardO == 0 and sp.simplify(dz - L2 / (32 * sp.pi ** 2) * EH) == 0,
      "explicit: k^2 part vanishes for A = k xi + xi k; d(1/(16 pi G))/d zeta = -L2/(32 pi^2) = -<phi^2>/2 "
      "(<phi^2> = L2/(16 pi^2) in this regulator): the closure-free zeta moves 1/G at O(Lambda^2)")

# P4
print("   W2 for the flat-measure Hessian D (closure vertices, proper time on D) ...", flush=True)
WD, _ = W2(symD.subs(zeta, 0))
WDk2 = korder(WD, 2)
wardD = sp.expand(WDk2.subs(gaugeA, simultaneous=True))
# numeric Ward ratio: 10x10 symbol at random unit k, max |M2 . gauge| / (max|M2|)
rng = np.random.default_rng(3)
kv = rng.normal(size=4); kv /= np.linalg.norm(kv)
subk = {k[m]: sp.Float(kv[m]) for m in R4}


def mat(Wexpr):
    Mx = np.zeros((10, 10))
    e = sp.expand(Wexpr.subs({L2: 1, zeta: 0}).subs(subk))
    for i, ab in enumerate(IDX):
        for j, cd in enumerate(IDX):
            Mx[i, j] = float(sp.re(e.coeff(Asym[ab]).coeff(Bsym[cd])))
    return Mx


MD = mat(WDk2)
MO = mat(Wk2)


def ward_ratio(Mx):
    best = 0
    for nu in R4:
        v = np.zeros(10)
        for i, (a, b) in enumerate(IDX):
            v[i] = kv[a] * (1.0 if b == nu else 0) + kv[b] * (1.0 if a == nu else 0)
        best = max(best, np.abs(v @ Mx).max())
    return best / np.abs(Mx).max()


rD, rO = ward_ratio(MD), ward_ratio(MO)
proj = float(np.vdot(MD.ravel(), MO.ravel()) / np.vdot(MO.ravel(), MO.ravel()))
print(f"   Ward ratio (max|gauge . M2| / max|M2|):  covariant O: {rO:.2e};  flat-measure D: {rD:.3f};  "
      f"EH-projection of D's k^2 symbol on O's: {proj:.4f} x (1/6) L2/(32 pi^2)")
check("P4", wardD != 0 and rD > 1e-2 and rO < 1e-12,
      "same closure-forced vertices and seagull, proper time on D instead of the covariant operator: the k^2 symbol is "
      "not transverse; the Ward identity at k^2 is a property of the regulator/measure, not of the classical seagull")

print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
