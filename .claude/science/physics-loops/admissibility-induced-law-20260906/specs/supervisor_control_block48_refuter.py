"""Block 48 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic integration, path enumeration, Monte Carlo, quadrature).
W1  the sphere moments of T2 by symbolic integration in spherical coordinates.
W2  the deficit of T3 by enumerating every step sequence of the directed walk (no closed formula used).
W3  the change of variables d Omega = |s|_1^3 dw by numerical quadrature of a test function.
W4  the collisionless force coefficient at finite distance by Monte Carlo over contents and paths and by quadrature over the simplex; approach to |r|_1^2 as 1/n.
W5  the window algebra of T5 by symbolic algebra, and the angular average 1 + 4/pi of |s|_1^2.
Floating point is used in W3 and W4 (controls, not the runner)."""
import itertools
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

ROOT = Path(__file__).resolve().parents[5]
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
th, ph = sp.symbols("theta phi", positive=True)
sx, sy, sz = sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)


def octant_mean(expr):
    """Average over the sphere of an expression even in each coordinate: eight times the first-octant integral over 4 pi."""
    val = sp.integrate(sp.integrate(expr * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, sp.pi / 2))
    return sp.simplify(8 * val / (4 * sp.pi))


one = sx + sy + sz                                                     # |s|_1 in the first octant
m1 = octant_mean(one)
mxx = octant_mean(one * sx * sx)
mzz = octant_mean(one * sz * sz)
half_zz = sp.simplify(sp.integrate(sp.integrate(sz * sz * sz * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi))
half_xx = sp.simplify(sp.integrate(sp.integrate(sz * sx * sx * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi))
sq = octant_mean(one * one)
report("W1", m1 == sp.Rational(3, 2) and mxx == sp.Rational(1, 2) and mzz == sp.Rational(1, 2) and half_zz == sp.Rational(1, 8) and half_xx == sp.Rational(1, 16),
       f"symbolic: <|s|_1> = {m1}, <|s|_1 s_x^2> = {mxx}, <|s|_1 s_z^2> = {mzz}, <max(0,s_z) s_z^2> = {half_zz}, <max(0,s_z) s_x^2> = {half_xx}")

# ------------------------------------------------------------------------------------------------ W2
ok = True
for d in ((1, 2, 2), (2, 3, 6), (3, 4, 0)):
    w = [F(c, sum(d)) for c in d]
    for n in (1, 2, 3, 5, 7):
        hit = {}
        for seq in itertools.product(range(3), repeat=n):
            pr = F(1)
            x = [0, 0, 0]
            for k in seq:
                pr *= w[k]
                x[k] += 1
            hit[tuple(x)] = hit.get(tuple(x), F(0)) + pr
        for x, val in hit.items():
            closed = F(sp.factorial(n)) / (sp.factorial(x[0]) * sp.factorial(x[1]) * sp.factorial(x[2])) * w[0] ** x[0] * w[1] ** x[1] * w[2] ** x[2]
            ok = ok and val == closed
        ok = ok and sum(hit.values()) == 1
report("W2", ok, "path enumeration: the probability that the directed walk passes a site equals the multinomial expression, and the probabilities over a shell sum to one (n = 1, 2, 3, 5, 7; three contents)")

# ------------------------------------------------------------------------------------------------ W3
g_sphere = lambda t, p: (np.sin(t) * np.cos(p) + 2 * np.cos(t) ** 2) * np.sin(t)          # test function g(s) = s_x + 2 s_z^2, first octant
lhs, _ = integrate.dblquad(g_sphere, 0, np.pi / 2, 0, np.pi / 2)


def g_simplex(w2, w1):
    w3 = 1 - w1 - w2
    nrm = np.sqrt(w1 * w1 + w2 * w2 + w3 * w3)
    return (w1 / nrm + 2 * (w3 / nrm) ** 2) / nrm ** 3


rhs, _ = integrate.dblquad(g_simplex, 0, 1, 0, lambda w1: 1 - w1)
report("W3", abs(lhs - rhs) < 1e-7, f"quadrature: the integral of a test function over the octant of the sphere, {lhs:.8f}, equals its integral over the simplex with the weight |w|_2^-3 = |s|_1^3, {rhs:.8f}")

# ------------------------------------------------------------------------------------------------ W4
rng = np.random.default_rng(48)
n = 60
targets = {(12, 24, 24): "(1,2,2)", (20, 20, 20): "(1,1,1)", (56, 2, 2): "(28,1,1)", (11, 16, 33): "(2,3,6) nearly"}
acc = {x: 0.0 for x in targets}
acc2 = {x: 0.0 for x in targets}
total = 0
for chunk in range(24):
    m = 2_000_000
    v = np.abs(rng.normal(size=(m, 3)))
    v /= np.linalg.norm(v, axis=1, keepdims=True)                     # uniform on the first octant
    l1 = v.sum(axis=1)
    x = rng.multinomial(n, v / l1[:, None])
    total += m
    for tx in targets:
        sel = (x[:, 0] == tx[0]) & (x[:, 1] == tx[1]) & (x[:, 2] == tx[2])
        rhat = np.array(tx) / np.linalg.norm(tx)
        val = l1[sel] * (v[sel] @ rhat)
        acc[tx] += val.sum()
        acc2[tx] += (val ** 2).sum()
from scipy.special import gammaln


def quad_coeff(tx, grid=2400):
    """The same finite-n coefficient by a midpoint rule over the simplex (deterministic; no sampling)."""
    nn = sum(tx)
    g = (np.arange(grid) + 0.5) / grid
    w1, w2 = np.meshgrid(g, g, indexing="ij")
    w3 = 1 - w1 - w2
    keep = w3 > 0
    w1, w2, w3 = w1[keep], w2[keep], w3[keep]
    logh = gammaln(nn + 1) - sum(gammaln(c + 1) for c in tx) + tx[0] * np.log(w1) + tx[1] * np.log(w2) + tx[2] * np.log(w3)
    t_ = w1 * w1 + w2 * w2 + w3 * w3
    rhat = np.array(tx) / np.linalg.norm(tx)
    phi_r = (w1 * rhat[0] + w2 * rhat[1] + w3 * rhat[2]) * t_ ** -2.5
    return float(sum(c * c for c in tx)) * np.sum(np.exp(logh) * phi_r) / grid ** 2


ok = True
lines = []
for tx, name in targets.items():
    r2 = float(sum(c * c for c in tx))
    coeff = (np.pi / 2) * r2 * acc[tx] / total                        # the octant has solid angle pi/2
    err = (np.pi / 2) * r2 * np.sqrt(acc2[tx]) / total
    want = sum(tx) ** 2 / r2
    q60 = quad_coeff(tx)
    q240 = quad_coeff(tuple(4 * c for c in tx))
    q960 = quad_coeff(tuple(16 * c for c in tx))
    d60, d240, d960 = q60 - want, q240 - want, q960 - want
    lines.append(f"{name}: limit |r|_1^2 = {want:.4f}; Monte Carlo at n = 60: {coeff:.3f} +- {err:.3f}; quadrature at n = 60, 240, 960: {q60:.4f}, {q240:.4f}, {q960:.4f} (deviation times n: {60 * d60:+.2f}, {240 * d240:+.2f}, {960 * d960:+.2f})")
    ok = ok and abs(coeff - q60) < 4 * err and abs(d960) < abs(d240) < abs(d60) and abs(960 * d960 - 240 * d240) < 0.25 * abs(240 * d240) + 0.05
report("W4", ok, "the collisionless force coefficient in units of rho/(4 pi sqrt 3 r^2), by Monte Carlo over contents and paths (48 million contents) and by quadrature over the simplex: the two agree at n = 60 and the quadrature approaches |r|_1^2 with a deviation proportional to 1/n: " + "; ".join(lines))

# ------------------------------------------------------------------------------------------------ W5
rho, n1, r = sp.symbols("rho N_1 r", positive=True)
q1 = sp.sqrt(3) * rho / 2
k0 = sp.sqrt(3) / (4 * sp.pi * rho * (1 - rho))
wind = k0 * q1 * n1 / r ** 2
acc_ = q1 * wind / sp.sqrt(3)
big_a = acc_ * r ** 2
tff = sp.pi / (2 * sp.sqrt(2)) * r ** sp.Rational(3, 2) / sp.sqrt(big_a)
ratio = sp.simplify((q1 * tff) ** 2)
gas_inside = sp.Rational(4, 3) * sp.pi * rho * r ** 3
bound = 8 * n1 / (3 * sp.pi ** 2 * (1 - rho))
ok = sp.simplify(wind - 3 * n1 / (8 * sp.pi * (1 - rho) * r ** 2)) == 0 and sp.simplify(ratio - sp.pi ** 3 * rho * (1 - rho) * r ** 3 / (2 * n1)) == 0 and sp.simplify(ratio - gas_inside / bound) == 0
ok = ok and sp.simplify(sq - (1 + 4 / sp.pi)) == 0
report("W5", ok, f"symbolic: wind 3 N_1/(8 pi (1 - rho) r^2); (q_1 t)^2 = {ratio}; equal to the gas inside the radius over 8 N_1/(3 pi^2 (1 - rho)); the angular average of |s|_1^2 is {sq}, that is {float(sq) / 2.25:.4f} of 9/4")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
