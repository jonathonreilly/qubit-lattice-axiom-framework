#!/usr/bin/env python3
"""C3 of CRITERIA.md: exact algebra for NT2 gate. No Monte Carlo."""
import itertools
import json
import sympy as sp


def r_moment(n):
    """E R^n for R = |X|^2, X ~ N(0, I_3)."""
    out = sp.Integer(1)
    for k in range(n):
        out *= 2 * k + 3
    return out


def c3a():
    k = sp.symbols("k")
    ey2 = sum(c * r_moment(p) for c, p in [(1, 1), (2 * k, 2), (k**2, 3)])
    ey4 = sum(c * r_moment(p) for c, p in
              [(1, 2), (4 * k, 3), (6 * k**2, 4), (4 * k**3, 5), (k**4, 6)])
    exc = sp.expand(ey4 - sp.Rational(5, 3) * ey2**2)
    return {
        "EY2": str(sp.expand(ey2)),
        "EY4": str(sp.expand(ey4)),
        "excess": str(exc),
        "pass": exc == sp.expand(120 * k + 3120 * k**2 + 31080 * k**3 + 116760 * k**4),
    }


def pairings(items):
    items = list(items)
    if not items:
        yield []
        return
    a = items[0]
    for i in range(1, len(items)):
        b = items[i]
        rest = items[1:i] + items[i + 1:]
        for p in pairings(rest):
            yield [(a, b)] + p


def c3b():
    a = sp.symbols("a")
    out = {}
    for name, s in [("plus", {(0, 1): a, (1, 2): a, (0, 2): a}),
                    ("minus", {(0, 1): a, (1, 2): -a, (0, 2): a})]:
        total = sp.Integer(0)
        n = 3
        # fields: (vector index, slot); colour contraction by connected loops
        fields = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        count = 0
        for p in pairings(fields):
            count += 1
            # colour graph: slots of one vector share colour; pairing identifies colours
            parent = {f: f for f in fields}

            def find(x):
                while parent[x] != x:
                    x = parent[x]
                return x

            def union(x, y):
                parent[find(x)] = find(y)

            for i in range(3):
                union((i, 0), (i, 1))
            w = sp.Integer(1)
            for u, v in p:
                union(u, v)
                i, j = sorted((u[0], v[0]))
                if i != j:
                    w *= s[(i, j)]
            comps = len({find(f) for f in fields})
            total += w * n**comps
        out[name] = sp.expand(total)
        out["count"] = count
    diff = sp.expand(out["plus"] - out["minus"])
    return {
        "pairings": out["count"],
        "plus": str(out["plus"]),
        "minus": str(out["minus"]),
        "difference": str(diff),
        "pass": out["count"] == 15 and diff == 48 * a**3
        and out["plus"] == 27 + 54 * a**2 + 24 * a**3,
    }


def gauss_moment_poly(expr, vars_, cov):
    """Exact E[expr] for a polynomial in centred Gaussians with covariance cov, by Wick."""
    poly = sp.Poly(sp.expand(expr), *vars_)
    total = sp.Integer(0)
    for mon, coef in poly.terms():
        idx = []
        for i, e in enumerate(mon):
            idx += [i] * e
        if len(idx) % 2:
            continue
        term = sp.Integer(0)
        cache = {}

        def rec(lst):
            key = tuple(lst)
            if key in cache:
                return cache[key]
            if not lst:
                return sp.Integer(1)
            a = lst[0]
            res = sp.Integer(0)
            for i in range(1, len(lst)):
                res += cov[a][lst[i]] * rec(lst[1:i] + lst[i + 1:])
            cache[key] = res
            return res

        term = rec(idx)
        total += coef * term
    return sp.expand(total)


def c3c():
    """Excess slope for general weights, one colour triple is costly, so use the
    two-link case with symbolic correlation and general weights, three colours."""
    v1, v2, c, w1, w2, k = sp.symbols("v1 v2 c w1 w2 k")
    xs = sp.symbols("x1:4")
    ys = sp.symbols("y1:4")
    vars_ = list(xs) + list(ys)
    cov = [[0] * 6 for _ in range(6)]
    for a in range(3):
        cov[a][a] = v1
        cov[a + 3][a + 3] = v2
        cov[a][a + 3] = c
        cov[a + 3][a] = c
    rx = sum(x**2 for x in xs)
    ry = sum(y**2 for y in ys)
    # first order in k only
    phi = [w1 * x * (1 + k * rx) + w2 * y * (1 + k * ry) for x, y in zip(xs, ys)]
    mod2 = sum(p**2 for p in phi)
    mod2_0 = mod2.subs(k, 0)
    dmod2 = sp.diff(mod2, k).subs(k, 0)
    m2 = gauss_moment_poly(mod2_0, vars_, cov)
    dm2 = gauss_moment_poly(dmod2, vars_, cov)
    dm4 = gauss_moment_poly(2 * mod2_0 * dmod2, vars_, cov)
    slope = sp.expand(dm4 - sp.Rational(10, 3) * m2 * dm2)
    r1 = w1 * v1 + w2 * c
    r2 = w1 * c + w2 * v2
    target = sp.expand(120 * (w1 * r1**3 + w2 * r2**3))
    return {"slope_minus_target": str(sp.expand(slope - target)),
            "pass": sp.expand(slope - target) == 0}


def c3d():
    import math
    # Proca mixtures: masses s_j, weights n_j
    mix = [(0.0, 0.2), (0.5, 1.0), (4.0, 0.7), (50.0, 0.3)]
    rho = lambda z: sum(n * (z / (z + s) if z + s > 0 else 1.0) for s, n in mix)
    zs = [10 ** (e / 4) for e in range(-16, 25)]
    mono = all(rho(a) <= rho(b) + 1e-14 for a, b in zip(zs, zs[1:]))
    # Flux variance at side r: integrate |f(q)|^2 rho(q^2 / r^2) over a positive radial weight
    def pvar(r, rho_):
        h = 0.02
        tot = 0.0
        for i in range(1, 2000):
            q = i * h
            w = q**3 * (math.sin(q / 2) / (q / 2)) ** 4 * math.exp(-0.05 * q)
            tot += h * w * rho_(q * q / r**2)
        return tot
    rs = [2.0**(-e) for e in range(0, 9)]
    pv = [pvar(r, rho) for r in rs]
    nonincreasing_in_r = all(a <= b + 1e-9 for a, b in zip(pv, pv[1:]))
    # Running profile: rho decreasing in z, so not a Proca mixture
    c, b = 1.0, 0.3715
    rrun = lambda z: 1.0 / (c + b * math.log1p(z))
    run_decreasing = all(rrun(a) > rrun(b_) for a, b_ in zip(zs, zs[1:]))
    # Spectral density of D(z) = rrun(z) / z on the cut z = -s, s > 1:
    # Im of 1/(c + b log(1 - s + i0)) = -b pi / ((c + b log(s - 1))^2 + (b pi)^2)
    # sigma(s) = (1/pi) Im D(-s - i0) sign convention: D(z) = int sigma / (z + s)
    # D(-s - i0) = int sigma(t) / (t - s - i0), Im = pi sigma(s).
    def sigma(s):
        den = (c + b * math.log(s - 1)) ** 2 + (b * math.pi) ** 2
        # rrun(-s - i0) = 1/(c + b(log(s-1) - i pi)) has Im = + b pi / den
        im_rrun = b * math.pi / den
        # D = rrun / z with z = -s, so Im D = - im_rrun / s
        return (-im_rrun / s) / math.pi
    sig = [sigma(1.0 + 10 ** (e / 3)) for e in range(-6, 19)]
    return {
        "proca_rho_monotone": mono,
        "flux_variance_grows_as_r_decreases": nonincreasing_in_r,
        "flux_var_samples": [round(x, 4) for x in pv],
        "running_rho_decreasing": run_decreasing,
        "running_spectral_density_max": max(sig),
        "pass": mono and nonincreasing_in_r and run_decreasing and max(sig) < 0,
    }


if __name__ == "__main__":
    res = {"C3a": c3a(), "C3b": c3b(), "C3c": c3c(), "C3d": c3d()}
    print(json.dumps(res, indent=1, default=str))
    with open(__file__.replace("nt2_algebra.py", "nt2_algebra.json"), "w") as f:
        json.dump(res, f, indent=1, default=str)
