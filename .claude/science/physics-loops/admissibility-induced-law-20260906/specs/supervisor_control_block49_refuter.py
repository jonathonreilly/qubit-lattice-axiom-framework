"""Block 49 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic integration, a transport solve, path enumeration, quadrature).
W1  the mean content 2/3 of cosine-law emission, <|s|_1> = 3/2 and the angular mean 1 + 4/pi - 9/4 of the residue, by symbolic integration.
W2  the stationary transport equation with a capturing and emitting site, solved site by site in exact arithmetic (no closed formula used):
    with cosine-law emission at the capture rate the density is uniform; with no emission it is the capture deficit.
W3  emitted records by enumerating every step sequence: first step through a face with the cosine law, then the directed walk.
W4  the residue of uniform emission at finite distance by quadrature over the simplex; approach to |r|_1 (|r|_1 - 3/2) as 1/n.
W5  the ratio q_1/G and the comparator arithmetic, symbolically.
Floating point is used in W4 only (a control, not the runner)."""
import itertools
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.special import gammaln

ROOT = Path(__file__).resolve().parents[5]
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
mu = sp.symbols("mu", positive=True)
mean_cos = sp.integrate(mu * mu, (mu, 0, 1)) / sp.integrate(mu, (mu, 0, 1))
th, ph = sp.symbols("theta phi", positive=True)
sx, sy, sz = sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)
one = sx + sy + sz


def octant_mean(expr):
    return sp.simplify(8 * sp.integrate(sp.integrate(expr * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, sp.pi / 2)) / (4 * sp.pi))


m1 = octant_mean(one)
resid = sp.simplify(octant_mean(one * one) - sp.Rational(3, 2) * m1)
report("W1", mean_cos == sp.Rational(2, 3) and m1 == sp.Rational(3, 2) and sp.simplify(resid - (1 + 4 / sp.pi - sp.Rational(9, 4))) == 0,
       f"symbolic: mean content of cosine-law emission along the normal {mean_cos}; <|s|_1> = {m1}; angular mean of |s|_1 (|s|_1 - 3/2) = {resid} = {float(resid):.4f}")

# ------------------------------------------------------------------------------------------------ W2
ok = True
side = 5
for d, length in (((1, 2, 2), 3), ((2, 3, 6), 7), ((3, 4, 0), 5)):
    a = [F(c, length) for c in d]                                      # step rates in units of 1/sqrt 3
    a1 = sum(a)
    rho_f = F(2, 9)                                                    # upstream density of this content
    for emitting in (True, False):
        dens = {}
        capture_rate = a1 * rho_f                                      # inflow into the capturing site from its upstream neighbours
        for x in sorted(itertools.product(range(side), repeat=3), key=sum):
            if x == (0, 0, 0):
                dens[x] = F(0)
                continue
            inflow = F(0)
            for k in range(3):
                y = tuple(x[i] - (1 if i == k else 0) for i in range(3))
                inflow += a[k] * (dens[y] if min(y) >= 0 else rho_f)   # sites behind the block carry the upstream density
            if emitting and sum(x) == 1:
                k = x.index(1)
                inflow += capture_rate * a[k] / a1                      # cosine law: placed on e_k with frequency a_k/|a|_1
            dens[x] = inflow / a1
        if emitting:
            ok = ok and all(v == rho_f for x, v in dens.items() if x != (0, 0, 0))
        else:
            w = [c / a1 for c in a]
            for x, v in dens.items():
                if x == (0, 0, 0):
                    continue
                n = sum(x)
                h = F(sp.factorial(n)) / (sp.factorial(x[0]) * sp.factorial(x[1]) * sp.factorial(x[2])) * w[0] ** x[0] * w[1] ** x[1] * w[2] ** x[2]
                ok = ok and v == rho_f * (1 - h)
report("W2", ok, "transport solve on a 5x5x5 block, three contents: with cosine-law emission at the capture rate the stationary density is the upstream density at every site; without emission it is the upstream density times one minus the multinomial expression")

# ------------------------------------------------------------------------------------------------ W3
ok = True
for d, length in (((1, 2, 2), 3), ((2, 3, 6), 7)):
    s = [F(c, length) for c in d]
    l1 = sum(s)
    w = [c / l1 for c in s]
    for n in (1, 2, 4, 6):
        hit = {}
        for first in range(3):
            p_first = s[first] / l1                                    # face k is chosen with the cosine weight s.e_k over the total |s|_1
            for seq in itertools.product(range(3), repeat=n - 1):
                pr = p_first
                x = [0, 0, 0]
                x[first] += 1
                for k in seq:
                    pr *= w[k]
                    x[k] += 1
                hit[tuple(x)] = hit.get(tuple(x), F(0)) + pr
        for x, val in hit.items():
            closed = F(sp.factorial(n)) / (sp.factorial(x[0]) * sp.factorial(x[1]) * sp.factorial(x[2])) * w[0] ** x[0] * w[1] ** x[1] * w[2] ** x[2]
            ok = ok and val == closed
report("W3", ok, "path enumeration: a record emitted through a face chosen with the cosine law and streaming from there passes a site with the multinomial probability of the directed walk from the body (n = 1, 2, 4, 6; two contents)")


# ------------------------------------------------------------------------------------------------ W4
def quad_residue(tx, grid=2400):
    nn = sum(tx)
    g = (np.arange(grid) + 0.5) / grid
    w1, w2 = np.meshgrid(g, g, indexing="ij")
    w3 = 1 - w1 - w2
    keep = w3 > 0
    w1, w2, w3 = w1[keep], w2[keep], w3[keep]
    logh = gammaln(nn + 1) - sum(gammaln(c + 1) for c in tx) + tx[0] * np.log(w1) + tx[1] * np.log(w2) + tx[2] * np.log(w3)
    t_ = w1 * w1 + w2 * w2 + w3 * w3
    rhat = np.array(tx) / np.linalg.norm(tx)
    l1 = 1 / np.sqrt(t_)                                               # |s|_1 = 1/|w|_2
    s_r = (w1 * rhat[0] + w2 * rhat[1] + w3 * rhat[2]) / np.sqrt(t_)    # s . r
    integrand = (l1 - 1.5) * s_r * l1 ** 3                              # weight (|s|_1 - 3/2) s.r with d Omega = |s|_1^3 dw
    return float(sum(c * c for c in tx)) * np.sum(np.exp(logh) * integrand) / grid ** 2


ok = True
lines = []
for tx, name in (((12, 24, 24), "(1,2,2)"), ((20, 20, 20), "(1,1,1)"), ((56, 2, 2), "(28,1,1)"), ((11, 16, 33), "(11,16,33)")):
    r2 = float(sum(c * c for c in tx))
    l1 = sum(tx) / np.sqrt(r2)
    want = l1 * (l1 - 1.5)
    q = [quad_residue(tuple(m * c for c in tx)) for m in (1, 4, 16)]
    dev = [q[i] - want for i in range(3)]
    lines.append(f"{name}: limit {want:+.4f}; quadrature at n = 60, 240, 960: {q[0]:+.4f}, {q[1]:+.4f}, {q[2]:+.4f} (deviation times n: {60 * dev[0]:+.2f}, {240 * dev[1]:+.2f}, {960 * dev[2]:+.2f})")
    ok = ok and abs(dev[2]) < abs(dev[1]) < abs(dev[0]) and abs(960 * dev[2] - 240 * dev[1]) < 0.25 * abs(240 * dev[1]) + 0.05
report("W4", ok, "the residue of uniform emission in units of rho/(4 pi sqrt 3 r^2), by quadrature over the simplex: approach to |r|_1 (|r|_1 - 3/2) with a deviation proportional to 1/n: " + "; ".join(lines))

# ------------------------------------------------------------------------------------------------ W5
rho = sp.symbols("rho", positive=True)
q1 = sp.sqrt(3) * rho / 2
g_ = 3 * sp.sqrt(3) * rho / (16 * sp.pi * (1 - rho))
ratio = sp.simplify(q1 / g_)
ticks = sp.Rational(435, 1000) * 10 ** 18 / (sp.Rational(539, 100) * sp.Integer(10) ** -44)          # 4.35e17 s over 5.39e-44 s
bound = 3 / (8 * sp.pi * ticks)
report("W5", sp.simplify(ratio - 8 * sp.pi * (1 - rho) / 3) == 0 and 7.9e60 < float(ticks) < 8.2e60 and 1.4e-62 < float(bound) < 1.6e-62,
       f"symbolic: q_1/G = {ratio}; comparator: {float(ticks):.2e} ticks, 3/(8 pi T) = {float(bound):.2e}")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
