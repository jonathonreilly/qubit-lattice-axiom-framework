#!/usr/bin/env python3
"""Block 44 refuting pass: machinery disjoint from the runner's.

W1  the bijection behind T2, built explicitly: for every configuration of three records on the 3^3 torus and every record, the unique streaming
    preimage is constructed and run forward; it must return the configuration, and distinct (configuration, record) pairs must have distinct
    (preimage, mover) pairs
W2  the momentum flux across one bond by enumeration of the bond's events in a product state (no formula): (rho/3) on the diagonal, zero off it
W3  the sphere menu's re-drawing as a symbolic identity
W4  the sphere menu's isotropic second moment <s_i s_j> = delta_ij/3 by exact integration, hence the flux rho/(3 sqrt 3) and the speed squared (1 - rho)/9
W5  T4 on a different body: an L-shaped reflecting body of three sites on the 4^3 torus, two records: stationarity and zero total force
Exact arithmetic (Fractions, sympy).
"""
import sys
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def step(x, d, L, sign=1):
    return tuple((x[i] + sign * E[d][i]) % L for i in range(3))


def forward(cfg, mover, L):
    d = cfg[mover]
    y = step(mover, d, L)
    new = dict(cfg)
    if y in cfg:
        new[mover], new[y] = cfg[y], d
    else:
        del new[mover]
        new[y] = d
    return new


def w1():
    L, n = 3, 3
    sites = list(product(range(L), repeat=3))
    ok = True
    seen = set()
    count = 0
    for occ in combinations(sites, n):
        for contents in product(range(6), repeat=n):
            cfg = dict(zip(occ, contents))
            for y, d in cfg.items():
                x = step(y, d, L, -1)
                pre = dict(cfg)
                if x in cfg:
                    pre[x], pre[y] = d, cfg[x]                  # before the exchange the content d sat behind
                else:
                    del pre[y]
                    pre[x] = d
                ok = ok and forward(pre, x, L) == cfg
                key = (tuple(sorted(pre.items())), x)
                ok = ok and key not in seen
                seen.add(key)
                count += 1
    report("W1", ok, f"all {count} (configuration, record) pairs with three records on the 3^3 torus: the constructed streaming preimage runs forward to the configuration, and the map to (preimage, mover) is one to one")


def w2():
    ok = True
    for rho in (F(3, 10), F(1, 2), F(4, 5)):
        dens = [rho / 6] * 6
        states = [None] + list(range(6))
        prob = lambda s: (1 - rho) if s is None else dens[s]
        flux = [F(0)] * 3                                       # momentum crossing the bond (x, x + e_x) in the +x sense, per unit time
        for sx in states:
            for sy in states:
                w = prob(sx) * prob(sy)
                if sx == 0:                                     # the record at x points at y
                    if sy is None:
                        gain = E[0]                             # it moves: e_x now sits at y
                    else:
                        gain = tuple(E[0][i] - E[sy][i] for i in range(3))
                    for i in range(3):
                        flux[i] += w * gain[i]
                if sy == 1:                                     # the record at y points at x
                    if sx is None:
                        gain = tuple(-v for v in E[1])          # e_{-x} leaves y for x: the +x side loses it
                    else:
                        gain = tuple(E[sx][i] - E[1][i] for i in range(3))
                    for i in range(3):
                        flux[i] += w * gain[i]
        ok = ok and flux == [rho / 3, 0, 0]
    report("W2", ok, "momentum crossing one bond per unit time, by enumeration of the bond's 49 states and its streaming events in an isotropic product state: (rho/3, 0, 0) at rho = 3/10, 1/2, 4/5")


def w3():
    a1, a2, a3, b1, b2, b3, w1_, w2_, w3_ = sp.symbols("a1 a2 a3 b1 b2 b3 w1 w2 w3", real=True)
    s, t, w = sp.Matrix([a1, a2, a3]), sp.Matrix([b1, b2, b3]), sp.Matrix([w1_, w2_, w3_])
    p = s + t
    r2 = 1 - p.dot(p) / 4
    # |P/2 + r w|^2 - 1 with r^2 substituted, modulo the constraints |s| = |t| = |w| = 1 and w.P = 0
    expr = sp.expand(p.dot(p) / 4 + r2 * w.dot(w) - 1)          # the cross term r (P.w) vanishes by orthogonality
    expr = expr.subs(w3_ ** 2, 1 - w1_ ** 2 - w2_ ** 2)
    report("W3", sp.simplify(expr) == 0, "symbolically, |P/2 +- r w|^2 = |P|^2/4 + r^2 |w|^2 = 1 when |w| = 1, w.P = 0 and r^2 = 1 - |P|^2/4; the sum of the pair is P by construction")


def w4():
    th, ph = sp.symbols("theta phi", real=True)
    s = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    ok = True
    for i in range(3):
        for j in range(3):
            val = sp.integrate(sp.integrate(s[i] * s[j] * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
            ok = ok and sp.simplify(val - (sp.Rational(1, 3) if i == j else 0)) == 0
    rho = sp.Symbol("rho", positive=True)
    flux = (rho * (1 - rho) + rho ** 2) * sp.Rational(1, 3) / sp.sqrt(3)
    speed_sq = sp.simplify(((1 - rho) / sp.sqrt(3)) * sp.diff(flux, rho))
    report("W4", ok and sp.simplify(speed_sq - (1 - rho) / 9) == 0, "the uniform sphere has <s_i s_j> = delta_ij/3 (exact integration), so the sphere menu's momentum flux is rho/(3 sqrt 3) and the linearized speed squared is (1 - rho)/9")


def w5():
    L, n = 4, 2
    solids = {(0, 0, 0), (1, 0, 0), (0, 1, 0)}
    sites = [s for s in product(range(L), repeat=3) if s not in solids]
    inflow, outflow = {}, {}
    force = [F(0)] * 3
    count = 0
    for occ in combinations(sites, n):
        for contents in product(range(6), repeat=n):
            cfg = dict(zip(occ, contents))
            key = tuple(sorted(cfg.items()))
            count += 1
            for x, d in cfg.items():
                y = step(x, d, L)
                if y in solids:
                    new = dict(cfg)
                    new[x] = d ^ 1
                    for i in range(3):
                        force[i] += 2 * E[d][i]
                else:
                    new = forward(cfg, x, L)
                k2 = tuple(sorted(new.items()))
                inflow[k2] = inflow.get(k2, 0) + 1
                outflow[key] = outflow.get(key, 0) + 1
    bad = sum(1 for k in outflow if inflow.get(k, 0) != outflow[k])
    report("W5", bad == 0 and force == [0, 0, 0], f"an L-shaped reflecting body of three sites on the 4^3 torus, two records ({count} configurations): inflow equals outflow everywhere and the total mean force on the body is exactly zero")


if __name__ == "__main__":
    for fn in (w2, w3, w4, w5, w1):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
