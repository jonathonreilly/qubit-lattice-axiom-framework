#!/usr/bin/env python3
"""Block 45 refuting pass: machinery disjoint from the runner's.

W1  the continuity identities from configuration DIFFERENCES: for 4000 random three-record configurations of the 3^3 torus every event is
    applied, the change of occupancy and momentum at every site is read off the new configuration, and the rate-weighted sum is compared
    with minus the divergence of the declared observables, written here independently as functions of an ordered bond
W2  the tilted sphere state's moments in closed form (coth l - 1/l and 1 - 2 <s_z>/l), their series, and A = (3/5 - rho)/rho, B = -1/(5 rho)
W3  the force of a uniform wind on an inflow by symbolic integration of the second-order flux over a sphere, with and without the pressure term
W4  the six-axis menu's second moments from the closed form 2 cosh l_1/(2 sum cosh l_k)
Exact arithmetic (Fractions, sympy).
"""
import random
import sys
from fractions import Fraction as F
from itertools import product

import sympy as sp

E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
L = 3
fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def nb(x, k):
    return tuple((x[i] + E[k][i]) % L for i in range(3))


def events(cfg, gamma):
    out = []
    for x, d in cfg.items():
        y = nb(x, d)
        new = dict(cfg)
        if y in cfg:
            new[x], new[y] = cfg[y], d
        else:
            del new[x]
            new[y] = d
        out.append((F(1), new))
    for x in cfg:
        for k in (0, 2, 4):
            y = nb(x, k)
            if y in cfg:
                a, b = cfg[x], cfg[y]
                if b == a ^ 1:
                    for e in range(6):
                        new = dict(cfg)
                        new[x], new[y] = e, e ^ 1
                        out.append((gamma / 6, new))
                else:
                    new = dict(cfg)
                    new[x], new[y] = b, a
                    out.append((gamma / 2, new))
                    out.append((gamma / 2, dict(cfg)))
    return out


def bond_current(cfg, x, k):
    y = nb(x, k)
    return int(x in cfg and cfg[x] == k and y not in cfg) - int(y in cfg and cfg[y] == k ^ 1 and x not in cfg)


def bond_flux(cfg, x, k, gamma):
    y = nb(x, k)
    f = [F(0)] * 3
    if x in cfg and cfg[x] == k:
        for i in range(3):
            f[i] += E[k][i] - (E[cfg[y]][i] if y in cfg else 0)
    if y in cfg and cfg[y] == k ^ 1:
        for i in range(3):
            f[i] -= E[k ^ 1][i] - (E[cfg[x]][i] if x in cfg else 0)
    if x in cfg and y in cfg:
        a, b = cfg[x], cfg[y]
        for i in range(3):
            f[i] += gamma * (F(E[a][i]) if b == a ^ 1 else F(E[a][i] - E[b][i], 2))
    return f


def w1():
    rng = random.Random(9)
    sites = list(product(range(L), repeat=3))
    gamma = F(3, 2)
    ok = True
    for _ in range(4000):
        occ = rng.sample(sites, 3)
        cfg = {s: rng.randrange(6) for s in occ}
        dn = {s: F(0) for s in sites}
        dp = {s: [F(0)] * 3 for s in sites}
        for rate, new in events(cfg, gamma):
            for s in sites:
                dn[s] += rate * (int(s in new) - int(s in cfg))
                for i in range(3):
                    dp[s][i] += rate * ((E[new[s]][i] if s in new else 0) - (E[cfg[s]][i] if s in cfg else 0))
        for s in sites:
            ok = ok and dn[s] == -sum(bond_current(cfg, s, k) for k in range(6))
            div = [sum(bond_flux(cfg, s, k, gamma)[i] for k in range(6)) for i in range(3)]
            ok = ok and dp[s] == [-v for v in div]
    report("W1", ok, "4000 random three-record configurations of the 3^3 torus, scattering rate 3/2: the changes of occupancy and momentum read off the new configurations equal minus the divergence of the current and of the momentum flux at every site")


def w2():
    lam, rho, g = sp.symbols("lambda rho g", positive=True)
    mz = sp.coth(lam) - 1 / lam
    mzz = 1 - 2 * mz / lam
    s1 = sp.series(mz, lam, 0, 4).removeO()
    s2 = sp.series(mzz, lam, 0, 3).removeO()
    ok = sp.simplify(s1 - (lam / 3 - lam ** 3 / 45)) == 0 and sp.simplify(s2 - (sp.Rational(1, 3) + 2 * lam ** 2 / 45)) == 0
    sub = {lam: 3 * g / rho}
    pzz = sp.expand((rho * s2 - rho ** 2 * (lam / 3) ** 2).subs(sub))
    pxx = sp.expand((rho * (1 - s2) / 2).subs(sub))
    a = sp.simplify((pzz - pxx).coeff(g, 2))
    b = sp.simplify(pxx.coeff(g, 2))
    ok = ok and sp.simplify(a - (sp.Rational(3, 5) - rho) / rho) == 0 and sp.simplify(b + 1 / (5 * rho)) == 0
    report("W2", ok, "closed forms <s_z> = coth l - 1/l and <s_z^2> = 1 - 2 <s_z>/l: series l/3 - l^3/45 and 1/3 + 2 l^2/45; the second-order flux has A = (3/5 - rho)/rho and B = -1/(5 rho)")


def w3():
    th, ph, a, q, g1, r = sp.symbols("theta phi A q g1 R", positive=True)
    n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    wind = sp.Matrix([0, 0, g1])
    inflow = -q / (4 * sp.pi * r ** 2) * n
    results = {}
    for name, b_eff in (("with the pressure term", -a / 2), ("without it", sp.Symbol("B"))):
        cross = a * (wind * (inflow.T * n)[0] + inflow * (wind.T * n)[0]) + 2 * b_eff * (wind.T * inflow)[0] * n
        force = -sp.integrate(sp.integrate(cross[2] * r ** 2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
        results[name] = sp.simplify(force)
    ok = sp.simplify(results["with the pressure term"] - a * q * g1) == 0 and sp.simplify(results["without it"] - (sp.Rational(4, 3) * a + sp.Rational(2, 3) * sp.Symbol("B")) * q * g1) == 0
    report("W3", ok, "symbolic integration of the cross term of the second-order flux over a sphere around the inflow: the force is A q g1 when the pressure adjusts (B_eff = -A/2) and (4A/3 + 2B/3) q g1 for a general isotropic coefficient")


def w4():
    l1, l2, l3, t = sp.symbols("l1 l2 l3 t", real=True)
    m11 = 2 * sp.cosh(t * l1) / (2 * (sp.cosh(t * l1) + sp.cosh(t * l2) + sp.cosh(t * l3)))
    ser = sp.series(m11, t, 0, 3).removeO()
    ok = sp.simplify(ser - (sp.Rational(1, 3) + t ** 2 * (l1 ** 2 / 9 - (l2 ** 2 + l3 ** 2) / 18))) == 0
    report("W4", ok, "six axes: 2 cosh l_1/(2 sum cosh l_k) = 1/3 + l_1^2/9 - (l_2^2 + l_3^2)/18 + ...; the mixed second moments vanish because no content has two non-zero components")


if __name__ == "__main__":
    for fn in (w2, w3, w4, w1):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
