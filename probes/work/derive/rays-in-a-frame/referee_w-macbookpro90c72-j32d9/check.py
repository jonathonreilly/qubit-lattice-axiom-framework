#!/usr/bin/env python3
"""Referee for rays-in-a-frame a2.

Author w-macbookpro90c72-j2bd3 (claude-opus-5-5). Own Hamilton derivatives and a 4^3 anticommutator.
"""
import itertools
import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def rays():
    x = sp.symbols("x1 x2 x3")
    k = sp.symbols("k1 k2 k3")
    m = sp.symbols("m", positive=True)
    a = sp.Function("a")(*x)
    w = sp.Function("w")(*x)
    g = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            g[i][j] = g[j][i] = sp.Function(f"g{i}{j}")(*x)
    s = [sp.sin(ki) for ki in k]
    quad = sum(g[i][j] * s[i] * s[j] for i in range(3) for j in range(3))
    E = sp.sqrt(a**2 * m**2 + w**2 * quad)
    ok = True
    for i in range(3):
        v = w**2 * sum(g[i][j] * s[j] for j in range(3)) * sp.cos(k[i]) / E
        ok &= sp.simplify(sp.diff(E, k[i]) - v) == 0
        force = -(
            m**2 * a * sp.diff(a, x[i])
            + w * sp.diff(w, x[i]) * quad
            + (w**2 / 2) * sum(sp.diff(g[j][l], x[i]) * s[j] * s[l] for j in range(3) for l in range(3))
        ) / E
        ok &= sp.simplify(-sp.diff(E, x[i]) - force) == 0
    zero = {k[0]: 0, k[1]: 0, k[2]: 0}
    acc = []
    for i in range(3):
        bit = 0
        for l in range(3):
            bit += sp.diff(sp.diff(E, k[i]), k[l]).subs(zero) * (-sp.diff(E, x[l])).subs(zero)
        acc.append(sp.simplify(bit))
    fall = [-w**2 * sum(g[i][l] * sp.diff(sp.log(a), x[l]) for l in range(3)) for i in range(3)]
    ok &= all(sp.simplify(acc[i] - fall[i]) == 0 for i in range(3))
    report(
        "ray equations",
        bool(ok),
        "v and k-dot match the closed forms, and a slow body falls as -w^2 g^{il} d_l log a",
    )


def bending():
    z = sp.symbols("z")
    wb = sp.symbols("wbar", positive=True)
    ww = sp.Function("w")(z)
    ell = wb / ww
    c = ww / ell
    weak = sp.simplify(sp.diff(sp.log(c), z) / sp.diff(sp.log(ww), z) - 2)
    P, Q, g = sp.symbols("P Q g")
    chi, N = 1 + Q * g, 1 - P * g
    log_c = sp.log(N / chi**3)
    log_a = sp.log(N / chi)
    ratio = sp.diff(log_c, g).subs(g, 0) / sp.diff(log_a, g).subs(g, 0)
    strong = sp.simplify(ratio - (P + 3 * Q) / (P + Q))
    report(
        "twice the fall",
        weak == 0 and strong == 0,
        "weak field bends twice the fall; the strong-field ratio is (P+3Q)/(P+Q)",
    )


def wave():
    eps, q, z, t = sp.symbols("eps q z t", real=True)
    Om, T = sp.symbols("Omega T", positive=True)
    Ap, Ax = sp.symbols("Ap Ax", real=True)
    kap = sp.pi / 3
    phase = q * z - Om * t
    h11 = Ap * sp.cos(phase)
    h12 = Ax * sp.cos(phase)
    # E = sqrt(sin^2 k1 (1 - eps h11) + 2 eps h12 sin k1 sin k2 + ...) at k=(kap,0,0)
    k1, k2, k3 = sp.symbols("k1 k2 k3")
    g11 = 1 - eps * h11
    g22 = 1 + eps * h11
    g12 = -eps * h12
    Q = g11 * sp.sin(k1) ** 2 + g22 * sp.sin(k2) ** 2 + sp.sin(k3) ** 2 + 2 * g12 * sp.sin(k1) * sp.sin(k2)
    E = sp.sqrt(Q)
    ray = {k1: kap, k2: 0, k3: 0}

    def lin(expr):
        return sp.series(expr, eps, 0, 2).removeO().coeff(eps)

    v1 = lin(sp.diff(E, k1)).subs(ray)
    v2 = lin(sp.diff(E, k2)).subs(ray)
    v3 = lin(sp.diff(E, k3)).subs(ray)
    k3dot = lin(-sp.diff(E, z)).subs(ray)
    ok = sp.simplify(v1 + sp.cos(kap) * h11 / 2) == 0
    ok &= sp.simplify(v2 + h12) == 0
    ok &= sp.simplify(v3) == 0
    ok &= sp.simplify(k3dot - sp.sin(kap) * sp.diff(h11, z) / 2) == 0
    drift = sp.integrate(v2, (t, 0, T))
    turn = sp.integrate(k3dot, (t, 0, T))
    ok &= sp.simplify(drift + Ax * (sp.sin(q * z) - sp.sin(q * z - Om * T)) / Om) == 0
    ok &= sp.simplify(turn + sp.sin(kap) * Ap * q * (sp.cos(q * z - Om * T) - sp.cos(q * z)) / (2 * Om)) == 0
    # along q, k=(0,0,kap): first order of v and k-dot vanishes because h_3j = 0
    along = {k1: 0, k2: 0, k3: kap}
    ok &= all(sp.simplify(lin(sp.diff(E, kk)).subs(along)) == 0 for kk in (k1, k2, k3))
    report(
        "transverse wave",
        bool(ok),
        "a ray along axis 1 feels h_11 as delay and turn and h_12 as drift; a ray along q feels nothing at first order",
    )


def rest():
    m0, m1, m2, m3 = sp.symbols("m0 m1 m2 m3")
    ms = [m1, m2, m3]
    sig = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    M = m0 * sp.eye(2) + m1 * sig[0] + m2 * sig[1] + m3 * sig[2]
    anti = []
    for b in range(3):
        comm = sp.expand(M * sig[b] + sig[b] * M)
        anti.append(sp.simplify(comm - (2 * m0 * sig[b] + 2 * ms[b] * sp.eye(2))))
    only_zero = all(a == sp.zeros(2) for a in anti)
    # staggered sign on 4^3 anticommutes with a varying frame's nearest-neighbour hop
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    n = len(sites)
    ix = {p: i for i, p in enumerate(sites)}
    dim = 2 * n
    H = np.zeros((dim, dim), complex)
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    pauli = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    for x in sites:
        i = ix[x]
        for j, step in enumerate(axes):
            y = tuple((x[a] + step[a]) % L for a in range(3))
            ym = tuple((x[a] - step[a]) % L for a in range(3))
            # integer frame, different at each site
            frame = np.array([x[0] + 1 + j, x[1] + 2, x[2] + 3], float)
            coin = sum(frame[a] * pauli[a] for a in range(3))
            for c in range(2):
                for d in range(2):
                    # S contributes +1/(2i) toward +e and -1/(2i) toward -e, times coin/2 from each end of the anticommutator
                    H[2 * i + c, 2 * ix[y] + d] += coin[c, d] / (4j)
                    H[2 * i + c, 2 * ix[ym] + d] += -coin[c, d] / (4j)
                    ycoin = np.array([y[0] + 1 + j, y[1] + 2, y[2] + 3], float)
                    yc = sum(ycoin[a] * pauli[a] for a in range(3))
                    H[2 * i + c, 2 * ix[y] + d] += yc[c, d] / (4j)
                    mcoin = np.array([ym[0] + 1 + j, ym[1] + 2, ym[2] + 3], float)
                    mc = sum(mcoin[a] * pauli[a] for a in range(3))
                    H[2 * i + c, 2 * ix[ym] + d] += -mc[c, d] / (4j)
    eps = np.zeros((dim, dim), complex)
    for x in sites:
        s = 1 if sum(x) % 2 == 0 else -1
        i = ix[x]
        eps[2 * i, 2 * i] = s
        eps[2 * i + 1, 2 * i + 1] = s
    antiH = np.max(np.abs(eps @ H + H @ eps))
    m = 3
    sq = (H + m * eps) @ (H + m * eps) - H @ H - (m ** 2) * np.eye(dim)
    report(
        "rest energy",
        bool(only_zero) and antiH < 1e-9 and np.max(np.abs(sq)) < 1e-8,
        "no nonzero 2x2 matrix anticommutes with all three Paulis; the staggered sign anticommutes with a varying frame on 4^3 and squares to H^2+m^2",
    )


def main():
    rays()
    bending()
    wave()
    rest()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the ray equations are the Hamilton equations of E^2 = a^2 m^2 + w^2 g^{ij} sin k_i sin k_j, "
        "and a slow body falls as -w^2 g^{il} d_l log a. Block 60's weak field bends twice the fall, and the strong field "
        "by (P+3Q)/(P+Q). A transverse traceless wave acts only through the row h_j. No on-site matrix anticommutes with "
        "a full frame; the staggered rest energy does, and falls with the inverse metric."
    )
    print(
        "SUMMARY: confirmed the ray equations, the factor 2, the row structure at k=pi/3, and the staggered square on 4^3. "
        "The eikonal limit itself was assumed, as the attempt says."
    )


if __name__ == "__main__":
    main()
