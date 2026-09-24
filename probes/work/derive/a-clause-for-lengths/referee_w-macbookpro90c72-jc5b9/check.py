#!/usr/bin/env python3
"""Referee for a-clause-for-lengths a1.

Author w-jonathonsmac4f50-jbfce (claude-opus-5-5). Independent Hamilton check.
The 40x64 slab was not re-executed.
"""
import itertools

import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def lattice_identity():
    x = sp.symbols("x1 x2 x3", real=True)
    k = sp.symbols("k1 k2 k3", real=True)
    m = sp.symbols("m", real=True)
    a = sp.Function("a")(*x)
    c = sp.Function("c")(*x)
    S = sum(sp.sin(kj) ** 2 for kj in k)
    E = sp.sqrt(a ** 2 * m ** 2 + c ** 2 * S)
    v = [sp.diff(E, kj) for kj in k]
    kdot = [-sp.diff(E, xj) for xj in x]
    acc = [
        sum(sp.diff(v[j], x[l]) * v[l] for l in range(3))
        + sum(sp.diff(v[j], k[l]) * kdot[l] for l in range(3))
        for j in range(3)
    ]
    bracket = [
        a ** 2 * m ** 2 * sp.diff(sp.log(a), x[j]) + c ** 2 * S * sp.diff(sp.log(c), x[j])
        for j in range(3)
    ]
    law = [
        -c ** 2 * sp.cos(2 * k[j]) * bracket[j] / E ** 2
        + 2 * v[j] * sum(v[l] * sp.diff(sp.log(c), x[l]) for l in range(3))
        for j in range(3)
    ]
    mid = [
        -(c ** 2 * sp.cos(2 * k[j]) / E) * sp.diff(E, x[j])
        + (sp.sin(2 * k[j]) / (2 * E)) * sum(v[l] * sp.diff(c ** 2, x[l]) for l in range(3))
        for j in range(3)
    ]
    zero = all(sp.simplify(acc[j] - law[j]) == 0 and sp.simplify(mid[j] - law[j]) == 0 for j in range(3))
    report(
        "step1 lattice law",
        zero,
        "Hamilton acc equals the mixture law and the step-1 intermediate form, for arbitrary a(x), c(x)",
    )


def limits_and_block54():
    x = sp.symbols("x1 x2 x3", real=True)
    k = sp.symbols("k1 k2 k3", real=True)
    m, kk = sp.symbols("m kk", real=True)
    a = sp.Function("a")(*x)
    c = sp.Function("c")(*x)
    S = sum(sp.sin(kj) ** 2 for kj in k)
    E2 = a ** 2 * m ** 2 + c ** 2 * S
    v = [c ** 2 * sp.sin(2 * k[j]) / (2 * sp.sqrt(E2)) for j in range(3)]
    law = [
        -c ** 2 * sp.cos(2 * k[j])
        * (a ** 2 * m ** 2 * sp.diff(sp.log(a), x[j]) + c ** 2 * S * sp.diff(sp.log(c), x[j]))
        / E2
        + 2 * v[j] * sum(v[l] * sp.diff(sp.log(c), x[l]) for l in range(3))
        for j in range(3)
    ]
    fall = sp.limit(law[0].subs({k[1]: 0, k[2]: 0, k[0]: kk}), kk, 0)
    bend = sp.simplify(law[0].subs({m: 0, k[0]: 0, k[2]: 0, k[1]: sp.pi / 3}))
    lim_ok = sp.simplify(fall + c ** 2 * sp.diff(sp.log(a), x[0])) == 0 and sp.simplify(
        bend + c ** 2 * sp.diff(sp.log(c), x[0])
    ) == 0
    w = sp.Function("w")(*x)
    du = sp.diff(sp.log(w), x[0])
    # a = w, c = w^2 (wbar = 1): coefficients -w^4 and -2 w^4. At the value w=1 those are -du and -2 du.
    slow = sp.simplify((-c ** 2 * sp.diff(sp.log(a), x[0])).subs({a: w, c: w ** 2}))
    light = sp.simplify((-c ** 2 * sp.diff(sp.log(c), x[0])).subs({a: w, c: w ** 2}))
    coef_s = sp.simplify(slow / du)
    coef_l = sp.simplify(light / du)
    scale_ok = coef_s == -(w ** 4) and coef_l == -2 * (w ** 4)
    scale_ok = scale_ok and coef_s.subs(w, 1) == -1 and coef_l.subs(w, 1) == -2
    scale_ok = scale_ok and coef_s.subs(w, 3) == -81 and coef_l.subs(w, 3) == -162
    # a = c = w collapses the mixture to block 54
    ww = sp.Function("w")(*x)
    uu = sp.log(ww)
    red = sp.simplify(
        law[0].subs({a: ww, c: ww})
        + ww ** 2 * sp.cos(2 * k[0]) * sp.diff(uu, x[0])
        - 2 * v[0].subs({a: ww, c: ww}) * sum(v[l].subs({a: ww, c: ww}) * sp.diff(uu, x[l]) for l in range(3))
    )
    report(
        "step3 limits",
        lim_ok and scale_ok and red == 0,
        "slow fall -c^2 dlog a, transverse massless bend -c^2 dlog c; "
        "a=w, c=w^2 is -w^4 and -2 w^4 (hence -du and -2 du at w=1); a=c=w is block 54",
    )


def points():
    x = sp.symbols("x1 x2 x3", real=True)
    k = sp.symbols("k1 k2 k3", real=True)
    m = sp.symbols("m", real=True)
    jets = [
        (
            sp.Rational(5, 4) * (1 + sp.Rational(3, 10) * x[0]),
            sp.Rational(2, 3) * (1 - sp.Rational(7, 20) * x[0]),
            {x[0]: sp.Rational(1, 7), x[1]: 0, x[2]: 0},
        ),
        (
            2 + sp.Rational(-1, 3) * x[0] + sp.Rational(1, 5) * x[1] + sp.Rational(1, 4) * x[2],
            sp.Rational(3, 2) + sp.Rational(1, 8) * x[0] + sp.Rational(-1, 6) * x[1] + sp.Rational(1, 9) * x[2],
            {x[0]: sp.Rational(-1, 4), x[1]: sp.Rational(1, 3), x[2]: sp.Rational(1, 5)},
        ),
        (
            1 + sp.Rational(1, 2) * x[0] + sp.Rational(-1, 3) * x[1] + sp.Rational(1, 7) * x[2],
            sp.Rational(4, 5) + sp.Rational(-1, 5) * x[0] + sp.Rational(1, 4) * x[1],
            {x[0]: sp.Rational(1, 2), x[1]: sp.Rational(-1, 5), x[2]: sp.Rational(1, 6)},
        ),
    ]
    pyth = [
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), sp.Rational(12, 13)),
        (sp.Rational(-8, 17), sp.Rational(15, 17)),
        (0, 1),
    ]
    npts = 0
    ok = True
    for (aa, cc, xx), masses in itertools.product(jets, (0, sp.Rational(1, 2))):
        S = sum(sp.sin(kj) ** 2 for kj in k)
        E = sp.sqrt(aa ** 2 * m ** 2 + cc ** 2 * S)
        v = [sp.diff(E, kj) for kj in k]
        kdot = [-sp.diff(E, xj) for xj in x]
        acc = [
            sum(sp.diff(v[j], x[t]) * v[t] for t in range(3))
            + sum(sp.diff(v[j], k[t]) * kdot[t] for t in range(3))
            for j in range(3)
        ]
        law = [
            -cc ** 2 * sp.cos(2 * k[j])
            * (aa ** 2 * m ** 2 * sp.diff(sp.log(aa), x[j]) + cc ** 2 * S * sp.diff(sp.log(cc), x[j]))
            / E ** 2
            + 2 * v[j] * sum(v[t] * sp.diff(sp.log(cc), x[t]) for t in range(3))
            for j in range(3)
        ]
        diff = [acc[j] - law[j] for j in range(3)]
        for (s1, c1), (s2, c2), mm in itertools.product(pyth, pyth[:3], (masses,)):
            rep = {
                sp.sin(k[0]): s1,
                sp.cos(k[0]): c1,
                sp.sin(k[1]): s2,
                sp.cos(k[1]): c2,
                sp.sin(k[2]): 0,
                sp.cos(k[2]): 1,
                sp.sin(2 * k[0]): 2 * s1 * c1,
                sp.cos(2 * k[0]): c1 ** 2 - s1 ** 2,
                sp.sin(2 * k[1]): 2 * s2 * c2,
                sp.cos(2 * k[1]): c2 ** 2 - s2 ** 2,
                sp.sin(2 * k[2]): 0,
                sp.cos(2 * k[2]): 1,
            }
            base = {m: mm, **xx}
            # skip the singular rest point
            Sval = s1 ** 2 + s2 ** 2
            aval = sp.simplify(aa.subs(base))
            cval = sp.simplify(cc.subs(base))
            if aval <= 0 or cval <= 0 or (mm == 0 and Sval == 0):
                continue
            for j in range(3):
                got = sp.simplify(diff[j].subs(base).subs(rep))
                ok = ok and got == 0
            npts += 1
    report(
        "step2 rational points",
        ok and npts >= 36,
        f"{npts} jets off the origin, including a three-direction gradient and m=0",
    )


def scale():
    wx, wy, t, u, d, g, x = sp.symbols("wx wy t u d g x", positive=True)
    step = sp.simplify(wx / sp.sqrt(wx * wy) - sp.sqrt(wx / wy)) == 0
    step = step and sp.simplify(wy / sp.sqrt(wx * wy) - sp.sqrt(wy / wx)) == 0
    depth_ok = True
    uniform_ok = True
    for p in (0, 1, sp.Rational(1, 2), sp.Rational(3, 2), -1):
        f = wx ** p * wy ** (1 - p)
        cov = sp.simplify(f.subs({wx: t * wx, wy: t * wy}) - t * f) == 0
        length = sp.simplify(sp.sqrt(wx * wy) / f)
        depth = sp.simplify(sp.diff(length.subs({wx: sp.exp(u), wy: sp.exp(u + d)}), u))
        depth_ok = depth_ok and cov and depth == 0
        ww = sp.exp(g * x)
        bond = sp.sqrt(ww * ww * sp.exp(g)) * sp.exp(-g) ** p
        ratio = sp.simplify(sp.diff(sp.log(bond), x) / sp.diff(sp.log(ww), x))
        uniform_ok = uniform_ok and ratio == 1
    wbar = sp.symbols("wbar", positive=True)
    cref = sp.exp(g * x) ** 2 / wbar
    ratio_ref = sp.simplify(sp.diff(sp.log(cref), x) / g)
    length2 = sp.simplify(sp.sqrt(wx * wy) / wx ** 2)
    sees_depth = sp.simplify(sp.diff(length2.subs({wx: sp.exp(u), wy: sp.exp(u + d)}), u)) != 0
    report(
        "step4 scale covariance",
        step and depth_ok and uniform_ok and ratio_ref == 2 and sees_depth,
        "degree-1 monomials of the two endpoints stay at ratio 1 on a uniform gradient; "
        "c=w^2/wbar has ratio 2 and is not depth-free",
    )


def finite_difference():
    def pack(z):
        return np.asarray(z, dtype=float)

    def fields(z):
        z = pack(z)
        a = np.exp(0.13 * z[0] - 0.07 * z[1] + 0.05 * z[2])
        c = np.exp(-0.04 * z[0] + 0.11 * z[1] - 0.02 * z[2])
        da = a * np.array([0.13, -0.07, 0.05])
        dc = c * np.array([-0.04, 0.11, -0.02])
        return a, c, da, dc

    def energy(z, k, mass):
        a, c, _, _ = fields(z)
        return np.sqrt(a ** 2 * mass ** 2 + c ** 2 * np.sum(np.sin(k) ** 2))

    def velocity(z, k, mass):
        _, c, _, _ = fields(z)
        return c ** 2 * np.sin(2 * k) / (2 * energy(z, k, mass))

    def kdot(z, k, mass):
        eps = 1e-6
        out = np.zeros(3)
        for j in range(3):
            dx = np.zeros(3)
            dx[j] = eps
            out[j] = -(energy(pack(z) + dx, k, mass) - energy(pack(z) - dx, k, mass)) / (2 * eps)
        return out

    def claimed(z, k, mass):
        a, c, da, dc = fields(z)
        S = np.sum(np.sin(k) ** 2)
        E2 = a ** 2 * mass ** 2 + c ** 2 * S
        v = velocity(z, k, mass)
        dloga = da / a
        dlogc = dc / c
        acc = np.zeros(3)
        for j in range(3):
            bracket = a ** 2 * mass ** 2 * dloga[j] + c ** 2 * S * dlogc[j]
            acc[j] = -c ** 2 * np.cos(2 * k[j]) * bracket / E2 + 2 * v[j] * np.dot(v, dlogc)
        return acc

    worst = 0.0
    samples = [
        (np.array([0.2, -0.4, 0.1]), np.array([0.7, -1.1, 0.4]), 0.5),
        (np.array([-0.3, 0.2, 0.5]), np.array([0.0, 1.2, -0.3]), 0.0),
        (np.array([0.0, 0.0, 0.0]), np.array([0.3, 0.0, 0.0]), 2.0),
    ]
    for z, k, mass in samples:
        v = velocity(z, k, mass)
        kd = kdot(z, k, mass)
        eps = 1e-5
        vp = velocity(z + eps * v, k + eps * kd, mass)
        vm = velocity(z - eps * v, k - eps * kd, mass)
        err = float(np.max(np.abs((vp - vm) / (2 * eps) - claimed(z, k, mass))))
        worst = max(worst, err)
    report(
        "finite difference",
        worst < 1e-6,
        f"central difference of v along the Hamilton field, worst abs error {worst:.3e}",
    )


def main():
    lattice_identity()
    limits_and_block54()
    points()
    scale()
    finite_difference()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the lattice family E^2 = a^2 m^2 + c^2 sum sin^2 k has the ray law "
        "dv_j/dt = -c^2 cos(2k_j)[a^2 m^2 d_j log a + c^2 S d_j log c]/E^2 + 2 v_j(v . grad log c); "
        "slow bodies fall at -c^2 grad log a and a transverse massless ray bends at -c^2 grad log c; "
        "a degree-1 bond rate of the two endpoint rates keeps that ratio at 1"
    )
    print(
        "SUMMARY: confirmed the Hamilton identity, the rational jets, the two limits "
        "(unit-scale coefficients -1 and -2, and -81 and -162 at w=3), the block-54 reduction, "
        "and the scale-covariance exclusion. The 40x64 slab was not re-executed."
    )


if __name__ == "__main__":
    main()
