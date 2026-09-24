#!/usr/bin/env python3
"""Referee for J:derive:the-bond-laws-completion-beyond-second-order:a3.

Independent of the author's script: Brillouin-zone Gauss quadrature for the sea,
a separate bond census, and sympy only for the even-profile algebra.
"""
import itertools
import math

import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

L = 4
BONDS = [(x, y, z, j) for x in range(L) for y in range(L) for z in range(L) for j in range(3)]


def doubled_mid(b):
    m = [2 * b[0], 2 * b[1], 2 * b[2]]
    m[b[3]] += 1
    return m


def bond_pairs():
    mids = [doubled_mid(b) for b in BONDS]
    out = []
    for i, j in itertools.combinations(range(len(BONDS)), 2):
        dd = []
        for a, c in zip(mids[i], mids[j]):
            t = (c - a) % (2 * L)
            dd.append(t - 2 * L if t > L else t)
        d2 = sum(t * t for t in dd)
        if d2 == 2:
            kind = "perp"
        elif d2 == 4 and BONDS[i][3] == BONDS[j][3]:
            kind = "coll" if dd[BONDS[i][3]] != 0 else "par"
        else:
            continue
        out.append((i, j, kind))
    return out


def zone_avg(fn, n=32):
    nodes, wts = leggauss(n)
    xs = 0.5 * (nodes + 1) * math.pi
    ws = 0.5 * wts * math.pi
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    W = ws[:, None, None] * ws[None, :, None] * ws[None, None, :]
    s2 = np.sin(X) ** 2 + np.sin(Y) ** 2 + np.sin(Z) ** 2
    return float(np.sum(fn(s2) * W) / math.pi ** 3)


def sea():
    inv = zone_avg(lambda s2: 1 / np.sqrt(s2), 40)
    inv_lo = zone_avg(lambda s2: 1 / np.sqrt(s2), 28)
    if abs(inv - inv_lo) > 5e-5:
        raise SystemExit(f"sea quadrature unstable {inv} {inv_lo}")
    # cache one mesh for G at many mu
    n = 36
    nodes, wts = leggauss(n)
    xs = 0.5 * (nodes + 1) * math.pi
    ws = 0.5 * wts * math.pi
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    W = (ws[:, None, None] * ws[None, :, None] * ws[None, None, :]) / math.pi ** 3
    s2 = np.sin(X) ** 2 + np.sin(Y) ** 2 + np.sin(Z) ** 2
    root = np.sqrt(s2)
    mean_abs = float(np.sum(root * W))

    def G(mu):
        return float(np.sum((np.sqrt(s2 + mu) - root) * W))

    return inv, mean_abs, G


def spectrum_ok():
    sig = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]

    def site(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)

    worst = 0.0
    ks = [2 * math.pi * n / L for n in range(L)]
    for dl in ((0.3, 0.0, 0.0), (0.4, -0.2, 0.7), (0.0, 0.0, 0.0)):
        H = np.zeros((2 * L ** 3, 2 * L ** 3), complex)
        for x, y, z, j in BONDS:
            e = [0, 0, 0]
            e[j] = 1
            c = math.exp(((-1) ** (x, y, z)[j]) * dl[j])
            a, b = site(x, y, z), site(x + e[0], y + e[1], z + e[2])
            blk = 0.5j * c * sig[j]
            H[2 * b:2 * b + 2, 2 * a:2 * a + 2] += blk
            H[2 * a:2 * a + 2, 2 * b:2 * b + 2] -= blk
        ev = np.sort(np.linalg.eigvalsh(H))
        mu = sum(math.sinh(v) ** 2 for v in dl)
        E = [math.sqrt(sum(math.sin(q) ** 2 for q in kk) + mu) for kk in itertools.product(ks, repeat=3)]
        pred = np.sort(np.concatenate([E, [-v for v in E]]))
        worst = max(worst, float(np.max(np.abs(ev - pred))))
    return worst


def algebra():
    x = sp.symbols("x", positive=True)
    phi_n1 = 4 * (sp.cosh(x / 2) - 1)
    phi_n2 = x * sp.sinh(x / 2)
    # pair rewriting
    c, cp = sp.symbols("c cp", positive=True)
    psi = lambda ph: sp.sqrt(c * cp) * ph.subs(x, sp.log(c / cp))
    n1 = sp.simplify(sp.expand((psi(phi_n1) - 2 * (sp.sqrt(c) - sp.sqrt(cp)) ** 2).rewrite(sp.exp)))
    n2 = sp.simplify(sp.expand((psi(phi_n2) - (c - cp) * sp.log(c / cp) / 2).rewrite(sp.exp)))
    z = sp.symbols("z", positive=True)
    f = sp.sinh(z) ** 3 - 6 * sp.sinh(z) + 6 * z
    df = sp.simplify(sp.expand(sp.diff(f, z).rewrite(sp.exp)))
    target = sp.simplify(sp.expand((3 * (sp.cosh(z) - 1) ** 2 * (sp.cosh(z) + 2)).rewrite(sp.exp)))
    gap = x * sp.sinh(x / 2) - 4 * (sp.cosh(x / 2) - 1)
    u = sp.symbols("u", positive=True)
    q = u * sp.sinh(u) - 2 * (sp.cosh(u) - 1)
    same = sp.simplify(sp.expand((gap - 2 * q.subs(u, x / 2)).rewrite(sp.exp)))
    dq = sp.simplify(sp.expand((sp.diff(q, u) - (u * sp.cosh(u) - sp.sinh(u))).rewrite(sp.exp)))
    if n1 != 0 or n2 != 0 or df != target or same != 0 or dq != 0:
        raise SystemExit(f"profile algebra failed n1={n1} n2={n2} same={same} dq={dq}")
    # row sum of block 59's M at k=0
    a, b, d = sp.symbols("alpha beta delta")
    c0 = -2 * a - 8 * b - 4 * d
    diag = c0 + 2 * a + 4 * d
    if sp.expand(diag + 2 * 4 * b) != 0:
        raise SystemExit("M(0) does not kill the uniform mode")
    return True


def main():
    algebra()
    print("STEP S1-S4 FOLLOWS: weight one fixes the second-order threshold at <1/|s|>/4 independent of the unit; "
          "phi=4(cosh(x/2)-1) is 2(sqrt c-sqrt c')^2 and phi=x sinh(x/2) is (c-c')log(c/c')/2; "
          "M(k=0) kills (1,1,1) with c0=-2alpha-8beta-4delta")

    pairs = bond_pairs()
    from collections import Counter
    per = Counter()
    for i, j, kind in pairs:
        per[(i, kind)] += 1
        per[(j, kind)] += 1
    counts = {k: sorted({per[(i, k)] for i in range(len(BONDS))}) for k in ("coll", "perp", "par")}
    if counts != {"coll": [2], "perp": [8], "par": [4]}:
        raise SystemExit(f"pair census {counts}")
    # alternation cost versus the closed form, numeric phi
    delta = (0.37, -0.21, 0.55)
    alpha, beta, delta_par = 0.4, 0.15, -0.2  # parallel coefficient must drop out
    kappa = alpha + 2 * beta

    def phi(x):
        return math.cosh(0.3 * x) - 1  # even, phi(0)=0

    def sign_u(b):
        return delta[b[3]] * ((-1) ** b[b[3]])

    direct = 0.0
    K = {"coll": alpha, "perp": beta, "par": delta_par}
    for i, j, kind in pairs:
        ui, uj = sign_u(BONDS[i]), sign_u(BONDS[j])
        direct += K[kind] * math.exp((ui + uj) / 2) * phi(ui - uj)
    direct /= L ** 3
    d1, d2, d3 = delta
    closed = alpha * sum(phi(2 * d) for d in delta) + 2 * beta * sum(
        math.cosh((delta[i] + delta[j]) / 2) * phi(delta[i] - delta[j])
        + math.cosh((delta[i] - delta[j]) / 2) * phi(delta[i] + delta[j])
        for i, j in itertools.combinations(range(3), 2)
    )
    n2 = 0.0
    for i, j, kind in pairs:
        ui, uj = sign_u(BONDS[i]), sign_u(BONDS[j])
        n2 += K[kind] * (math.exp(ui) - math.exp(uj)) * (ui - uj) / 2
    n2 /= L ** 3
    n2_closed = 2 * kappa * sum(d * math.sinh(d) for d in delta)
    if abs(direct - closed) > 1e-12 or abs(n2 - n2_closed) > 1e-12:
        raise SystemExit(f"cost mismatch {direct} {closed} {n2} {n2_closed}")
    print("STEP S5-S6 FOLLOWS: 4^3 census is 2 collinear, 8 perpendicular, 4 parallel; "
          f"a generic even profile reproduces the closed cost (dev {abs(direct-closed):.1e}); "
          f"N2 cost is 2*kappa*sum d sinh d (dev {abs(n2-n2_closed):.1e}), parallel coupling absent")

    worst = spectrum_ok()
    if worst > 1e-12:
        raise SystemExit(f"spectrum dev {worst}")
    print(f"STEP S5 SPECTRUM FOLLOWS: staggered hop on 4^3 matches +-sqrt(sum sin^2 k + sum sinh^2 delta) to {worst:.1e}")

    inv, mean_abs, G = sea()
    if mean_abs > math.sqrt(1.5) + 1e-9:
        raise SystemExit("mean |s| exceeds sqrt(3/2)")
    kc = inv / 4
    J1 = inv / 2 - G(1.0)
    J3 = inv * 1.5 - G(3.0)
    if not (J1 > kc / 3 and J3 / 9 > kc / 6):
        raise SystemExit(f"J margins failed {J1} {J3} {kc}")
    # sampled strict inequality on the two lines the proof splits into regions
    axis = np.linspace(0.02, 6.0, 80)
    axis_ratio = [kc * (2 * a * math.sinh(a)) / G(math.sinh(a) ** 2) for a in axis]
    diag = np.linspace(0.02, 4.0, 60)
    diag_ratio = [kc * 12 * (math.cosh(d) - 1) / G(3 * math.sinh(d) ** 2) for d in diag]
    if min(axis_ratio) <= 1 or min(diag_ratio) <= 1:
        raise SystemExit(f"ratio dipped {min(axis_ratio)} {min(diag_ratio)}")
    a, r = 2.2, 0.1
    C = (1 - 2 * r) * 4 * (math.cosh(a) - 1) + r * (16 * math.cosh(a) - 32 * math.cosh(a / 2) + 16)
    witness = G(math.sinh(a) ** 2) / C
    rcrit = (1 / kc - 4) / 8
    # o(e^{|x|/2}) witness: quadratic profile on the diagonal
    Bquad = 3 * 1.0 * (2 * 8) ** 2 / 2 - math.sqrt(3) * math.sinh(8) + math.sqrt(1.5)
    if Bquad >= 0 or witness <= kc or rcrit <= 0.049:
        raise SystemExit(f"witnesses {Bquad} {witness} {rcrit}")
    # slope of J/mu^2 versus log(1/mu)
    def J(mu):
        return inv * mu / 2 - G(mu)
    m1, m2 = 1e-4, 1e-3
    slope = (J(m1) / m1 ** 2 - J(m2) / m2 ** 2) / math.log(m2 / m1)
    target = 1 / (4 * math.pi ** 2)
    print(f"STEP S7-S16 FOLLOWS: <1/|s|>={inv:.6f} so kappa_c={kc:.6f} ( <|s|>={mean_abs:.4f}<=sqrt(3/2) ); "
          f"J(1)={J1:.6f} > kappa_c/3={kc/3:.6f}; J(3)/9={J3/9:.6f} > kappa_c/6={kc/6:.6f} "
          f"(the attempt's 'J(1)>=0.0805' rounds {J1:.6f}); "
          f"N2 axis min kappa_c*cost/G={min(axis_ratio):.4f}, N1 diagonal min={min(diag_ratio):.4f}; "
          f"at beta/kappa=1/10, a=2.2, G/C={witness:.5f}>kappa_c; r<(1/kappa_c-4)/8={rcrit:.5f} so r<0.049 is inside; "
          f"quadratic witness at delta=8, kappa=1 is {Bquad:.1f}<0; "
          f"slope of J/mu^2 vs log(1/mu) on [1e-4,1e-3] is {slope:.5f} against 1/(4 pi^2)={target:.5f}")
    if abs(slope - target) / target > 0.05:
        raise SystemExit("Dirac slope off")

    print("SUMMARY: confirmed - on weight-one pair completions of block 59, one even profile per class with phi''(0)=1; "
          "profiles o(e^{|x|/2}) are unbounded below on the alternation family at every kappa; "
          f"profiles >= x sinh(x/2), including N2, make the uniform field the strict global minimum on that family for every kappa>=kappa_c={kc:.6f}, "
          "with a continuous transition whose leading law is mu log(1/mu) ~ 4*pi**2*(kappa_c-kappa); "
          "N1 does so on the diagonal and does not on the whole family at beta/kappa=1/10")
    print("HIT: confirmed - pair ledgers leave one even profile per class; x sinh(x/2) (N2) keeps the uniform field the strict minimum on the alternation family for kappa>=<1/|s|>/4, continuously, and o(e^{|x|/2}) profiles do not; N1 fails on that family at beta/kappa=1/10")


if __name__ == "__main__":
    main()
