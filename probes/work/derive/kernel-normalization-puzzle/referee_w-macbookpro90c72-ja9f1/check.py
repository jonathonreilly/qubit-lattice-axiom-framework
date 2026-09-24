#!/usr/bin/env python3
"""Independent checks for kernel-normalization-puzzle a3.

The pair-sum identity, the gain cancellation, and the light-cone exchange weights.
"""
import itertools

import sympy as sp

FAILS = []
STENCILS = {
    "n3": [(0, 0), (-1, 0), (0, -1)],
    "n4": [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)],
    "n7": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
}


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def main():
    ident = True
    for st in STENCILS.values():
        d = len(st[0])
        ks = sp.symbols(f"k0:{d}", real=True)
        n = len(st)
        phi = sum(sp.exp(sp.I * sum(ks[i] * y[i] for i in range(d))) for y in st) / n
        mod2 = sp.expand(sp.expand_complex(phi * sp.conjugate(phi)))
        lhs = sum(
            1 - sp.cos(sum(ks[i] * (y[i] - yp[i]) for i in range(d)))
            for y, yp in itertools.combinations(st, 2)
        )
        ident &= sp.simplify(sp.expand(lhs - sp.Rational(n * n, 2) * (1 - mod2))) == 0
    ok("E1", ident, "pair sum (n^2/2)(1-|phi|^2) on the n=3,4,7 stencils, so E[delta]=n sigma^2")

    x = sp.symbols("x", positive=True)
    gain = sp.expand((1 - x) * (1 + x * (1 - x)))
    leading = sp.expand((1 - x) * (1 + x))
    ok("E2", gain == 1 - 2 * x ** 2 + x ** 3 and gain.coeff(x, 1) == 0 and leading == 1 - x ** 2,
       "Hartree gain is 1 - 2x^2 + x^3; the order 1/beta cancels")

    # simplex differences eps_a - eps_b are one orbit
    orbit = True
    for n in (3, 4):
        diffs = set()
        for a, b in itertools.permutations(range(n), 2):
            v = [0] * n
            v[a] += 1
            v[b] -= 1
            diffs.add(tuple(sorted(v)))
        orbit &= len(diffs) == 1
    ok("simplex", orbit, "ordered pair differences of a simplex are one orbit, so the exchange term vanishes")

    # light-cone Gamma
    ce, c2, cd, c0 = sp.symbols("ce c2 cd c0")
    def cov(v):
        r2 = sum(t * t for t in v)
        nz = sum(t != 0 for t in v)
        if r2 == 0:
            return c0
        if r2 == 1:
            return ce
        if r2 == 4:
            return c2
        if r2 == 2 and nz == 2:
            return cd
        raise AssertionError(v)
    st = STENCILS["n7"]
    gam = {tuple(y): sum(cov(tuple(a - b for a, b in zip(y, z))) for z in st) for y in st}
    gbar = sum(gam.values()) / 7
    delta = c2 + 4 * cd - 5 * ce
    centre = sp.simplify(gam[(0, 0, 0)] - gbar + sp.Rational(6, 7) * delta) == 0
    arms = all(sp.simplify(gam[y] - gbar - delta / 7) == 0 for y in st if y != (0, 0, 0))
    ok("E3", centre and arms, "Gamma(0)-mean = -(6/7) Delta and Gamma(e)-mean = Delta/7")

    s2, W, Dc = sp.symbols("sigma2 W Delta_c", positive=True)
    noise = sp.expand(1 + s2 - s2 * (W - 1) - (1 + s2 * (2 - W)))
    # small-k ratio: (1/7) / (1/7 + sigma2 Delta_c/343) = 1/(1 + sigma2 Delta_c/49)
    ratio = (sp.Rational(1, 7)) / (sp.Rational(1, 7) + s2 * Dc / 343)
    gap = sp.simplify(sp.together(ratio - 1 / (1 + s2 * Dc / 49)))
    ok("E4", noise == 0 and gap == 0,
       "noise factor 1+sigma^2(2-W); light-cone R(0+) divides by 1+sigma^2 Delta_c/49")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent algebra did not match")
        return
    print(
        "HIT: confirmed - E[delta]=n sigma^2, the 1/beta gain cancels, simplex exchange vanishes, "
        "and the one-loop factor is 1+sigma^2(2-W)"
    )
    print(
        "SUMMARY: confirmed E1-E4; the executed plateaus were not re-parsed, and the one-loop closure stays assumed"
    )


if __name__ == "__main__":
    main()
