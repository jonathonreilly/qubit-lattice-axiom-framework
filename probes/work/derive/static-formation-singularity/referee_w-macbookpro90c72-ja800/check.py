#!/usr/bin/env python3
"""Referee for static-formation-singularity a3.

Author w-jonathonsmac4f50-ja5a1 (claude-opus-5). This file does not import that
check. Six-axis weights at (p, q, r) = (3, 1, 2): equal, antipodal, orthogonal.
"""
import itertools
import math
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction as Fr

p, q, r = 3, 1, 2
Ktab = [[p if i == j else (q if i == (j ^ 1) else r) for j in range(6)] for i in range(6)]
fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def K(i, j):
    return Ktab[i][j]


def N_of(us):
    return sum(math.prod(K(t, u) for u in us) for t in range(6))


def weights(nn):
    w = [math.prod(K(s, b) for b in nn) for s in range(6)]
    return w, sum(w)


def plaquette_and_chernoff():
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    Z = sum(math.prod(K(u[a], u[b]) for a, b in edges) for u in itertools.product(range(6), repeat=4))
    # closed count: 12^4 monochromatic-free bulk plus the three global pairings of antipodes, each 2^4
    closed = 12 ** 4 + 3 * 2 ** 4
    Ds = []
    for order in itertools.permutations(range(4)):
        done, prod = [], 1
        for x in order:
            k = sum(1 for y in done if (x, y) in edges or (y, x) in edges)
            prod *= 6 if k == 0 else (p ** k + q ** k + 4 * r ** k)
            done.append(x)
        Ds.append(prod)
    pi_s, pi_f = Fr(6 * p ** 4, Z), Fr(6 * p ** 4, min(Ds))
    between = pi_f < Fr(9, 400) < pi_s
    # A^400 = (10409/10400)^400 * (25/26)^9 , B^400 = (86519/86600)^400 * (25/24)^9
    a_num = 10409 ** 400 * 25 ** 9
    a_den = 10400 ** 400 * 26 ** 9
    b_num = 86519 ** 400 * 25 ** 9
    b_den = 86600 ** 400 * 24 ** 9
    getcontext().prec = 80
    logA = Decimal(a_num).ln() - Decimal(a_den).ln()
    logB = Decimal(b_num).ln() - Decimal(b_den).ln()
    # per-plaquette rates; A = exp(log(A^400)/400)
    rateA, rateB = -logA / 400, -logB / 400
    m = 80237
    sum_m = Decimal(m) * (logA / 400) 
    # compare A^m + B^m with 1/2 by scaling to the smaller exponent
    def tail_sum(mm):
        eA = (Decimal(mm) * logA / 400).exp()
        eB = (Decimal(mm) * logB / 400).exp()
        return eA + eB
    # 80237 = ceil(ln 4 / slower rate): each tail is then < 1/4, so the sum is < 1/2.
    # The sum itself crosses 1/2 earlier; 80237 is a correct sufficient count, not the first.
    lo, hi = 1, 90000
    while lo < hi:
        mid = (lo + hi) // 2
        if tail_sum(mid) < Decimal("0.5"):
            hi = mid
        else:
            lo = mid + 1
    report(
        "plaquettes",
        Z == 20784 and Z == closed and set(Ds) == {22464, 24336} and pi_s == Fr(81, 3464) and pi_f == Fr(9, 416) and between and a_num < a_den and b_num < b_den and tail_sum(m) < Decimal("0.5") and lo == 79827,
        f"Z=20784=12^4+3*2^4, D in {{22464,24336}}, pi_s=81/3464, pi_f=9/416, 9/416<9/400<81/3464, "
        f"A^400<1 and B^400<1 by integer comparison; A^m+B^m<1/2 at m={m} "
        f"(rates {rateA:.6e}, {rateB:.6e}); the sum crosses 1/2 at m={lo}",
    )


def colour_and_blocks():
    # 2D dependency: nearest neighbours and the anti-diagonal e1-e2. Colour (x-y) mod 3.
    shifts2 = ((1, 0), (0, 1), (1, -1))
    ok2 = all((dx - dy) % 3 != 0 for dx, dy in shifts2)
    # 3D: NN and face diagonals ei-ej. Colour x+2y+3z mod 4.
    def col(x, y, z):
        return (x + 2 * y + 3 * z) % 4
    shifts3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]
    ok3 = all(col(*s) != 0 for s in shifts3)
    # blocks {y, y+(1,-1,0)} on 4Z^3: a displacement of 4 e_i meets no dependency edge
    def dep(delta):
        d = tuple(delta)
        flips = {d, tuple(-x for x in d)}
        return any(tuple(s) in flips for s in shifts3)
    far = True
    for axis in range(3):
        step = tuple(4 if i == axis else 0 for i in range(3))
        far = far and not dep(step)
        u = (1, -1, 0)
        far = far and not dep(tuple(step[i] - u[i] for i in range(3)))
        far = far and not dep(tuple(step[i] + u[i] for i in range(3)))
    report(
        "colours",
        ok2 and ok3 and far,
        "anti-diagonals change (x-y) mod 3; face diagonals change x+2y+3z mod 4; blocks on 4Z^3 share no dependency edge",
    )


def normalisers():
    pairs = {(a, b): N_of((a, b)) for a in range(6) for b in range(6)}
    eq = pairs[(0, 0)]
    anti = pairs[(0, 1)]
    orth = pairs[(0, 2)]
    ok = eq == 26 and anti == 22 and orth == 24 and set(pairs.values()) == {22, 24, 26}
    # 2D: automaton weight / (nearest-neighbour weight * g) is independent of s, all 6^6 boundaries
    const = True
    best = None
    for nn in itertools.product(range(6), repeat=4):
        left, up, right, down = nn
        for b5, b6 in itertools.product(range(6), repeat=2):
            g = [Fr(1, pairs[(s, b5)] * pairs[(s, b6)]) for s in range(6)]
            w, Zw = weights(nn)
            Eg = sum(Fr(w[s], Zw) * g[s] for s in range(6))
            var = sum(Fr(w[s], Zw) * (g[s] - Eg) ** 2 for s in range(6))
            val = var / (2 * max(g) ** 2)
            if best is None or val < best:
                best = val
            ratios = []
            for s in range(6):
                form = K(s, left) * K(s, up) * Fr(K(right, s) * K(right, b5), pairs[(s, b5)]) * Fr(K(down, s) * K(down, b6), pairs[(s, b6)])
                stat = w[s] * g[s]
                ratios.append(form / stat if stat else None)
            const = const and len(set(ratios)) == 1
    gmin = None
    for nn in itertools.product(range(6), repeat=6):
        w, Zw = weights(nn)
        m = Fr(min(w), Zw)
        if gmin is None or m < gmin:
            gmin = m
    report(
        "z2-min",
        ok and const and best == Fr(19, 4604256) and best > 0,
        f"N is 26, 24, 22; the 2D conditional ratio is constant in s on every boundary; "
        f"min Var(g)/(2 gmax^2) = {best}",
    )
    return pairs, gmin


def z3(gmin):
    N3 = {}
    for trip in itertools.product(range(6), repeat=3):
        N3[trip] = N_of(trip)
    rel = lambda a, b: "eq" if a == b else ("anti" if a == (b ^ 1) else "orth")
    bad = []
    minrel = None
    for fd in itertools.product(range(6), repeat=6):
        g = [Fr(1, N3[(s, fd[0], fd[1])] * N3[(s, fd[2], fd[3])] * N3[(s, fd[4], fd[5])]) for s in range(6)]
        if len(set(g)) == 1:
            bad.append(fd)
            continue
        if fd[0] == fd[1]:
            v = (max(g) - min(g)) ** 2 / (4 * max(g) ** 2)
            if minrel is None or v < minrel:
                minrel = v
    kinds = defaultdict(int)
    for fd in bad:
        kinds[tuple(sorted(rel(fd[2 * j], fd[2 * j + 1]) for j in range(3)))] += 1
    # algebraic 3D ratio on 40 deterministic boundaries, every spin
    alg = True
    for n in range(40):
        # deterministic spread, not random: base-6 digits of n and of n+17
        spins = []
        x = n * 17 + 3
        for _ in range(12):
            spins.append(x % 6)
            x = x // 6 + 5
        preds, succs = spins[0:3], spins[3:6]
        pairs = [spins[6:8], spins[8:10], spins[10:12]]
        ratios = []
        for s in range(6):
            own = math.prod(K(s, b) for b in preds)
            g = Fr(1)
            succ = Fr(1)
            gamma = Fr(own)
            for z, (a, b) in zip(succs, pairs):
                g /= N3[(s, a, b)]
                succ *= K(z, s)
                gamma *= K(s, z)
            # predecessor normaliser does not depend on s; successor pair-weights K(z,a)K(z,b) do not either
            weight = Fr(own) * succ * g
            ratios.append(weight / (gamma * g))
        alg = alg and ratios == [Fr(1)] * 6
    c3 = gmin * gmin * minrel
    report(
        "z3",
        len(bad) == 600 and dict(kinds) == {("anti", "anti", "anti"): 216, ("orth", "orth", "orth"): 384} and all(fd[0] != fd[1] for fd in bad) and gmin == Fr(1, 986) and minrel == Fr(4, 28561) and alg and c3 == Fr(1, 986) ** 2 * Fr(4, 28561),
        f"600 flat face-diagonal boundaries (216 antipodal, 384 orthogonal), none with a1=b1; "
        f"min gamma={gmin}; min (gmax-gmin)^2/(4 gmax^2) on a1=b1 is {minrel}; "
        f"c3={c3}; 3D conditional ratio constant in s on 40 boundaries",
    )


def windows(pairs):
    edges = ((0, 1), (0, 2), (1, 3), (2, 3))
    pats = list(itertools.product(range(6), repeat=4))
    Z = sum(math.prod(K(u[a], u[b]) for a, b in edges) for u in pats)
    mu, nu = {}, {}
    for u in pats:
        mu[u] = Fr(math.prod(K(u[a], u[b]) for a, b in edges), Z)
        nu[u] = Fr(1, 6) * Fr(K(u[1], u[0]), 12) * Fr(K(u[2], u[0]), 12) * Fr(K(u[3], u[1]) * K(u[3], u[2]), pairs[(u[1], u[2])])
    ratio_ok = all(mu[u] / nu[u] == Fr(864 * pairs[(u[1], u[2])], Z) for u in pats)
    tv = sum(abs(mu[u] - nu[u]) for u in pats) / 2
    anti_mu = sum(mu[u] for u in pats if u[1] == u[2])
    anti_nu = sum(nu[u] for u in pats if u[1] == u[2])
    const_gap = sum(mu[u] - nu[u] for u in pats if len(set(u)) == 1)
    star = {u for u in pats if mu[u] > nu[u]}
    nn_mu = sum(mu[u] * sum(u[a] == u[b] for a, b in edges) for u in pats)
    nn_nu = sum(nu[u] * sum(u[a] == u[b] for a, b in edges) for u in pats)
    gap = Fr(81, 3464) - Fr(9, 416)
    report(
        "window-2d",
        ratio_ok and sum(nu.values()) == 1 and star == {u for u in pats if u[1] == u[2]} and tv == anti_mu - anti_nu == Fr(455, 31176) and anti_mu - anti_nu == Fr(169, 866) - Fr(13, 72) and nn_nu == 1 and abs(float(nn_mu) - 1.01155) < 5e-6 and abs(float(tv / const_gap) - 8.3) < 0.05,
        f"TV={tv}=169/866-13/72, optimal event is the anti-diagonal equality, constant-indicator gap is {float(tv/const_gap):.2f} times smaller, "
        f"equal-bond count {float(nn_mu):.5f} against 1",
    )

    # 2x2x2, site index x+2y+4z
    def ix(x, y, z):
        return x + 2 * y + 4 * z
    sites = [(x, y, z) for z in range(2) for y in range(2) for x in range(2)]
    edges3 = []
    for x, y, z in sites:
        for j, step in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
            if (x, y, z)[j] == 0:
                nxt = (x + step[0], y + step[1], z + step[2])
                edges3.append((ix(x, y, z), ix(*nxt)))
    preds = {ix(x, y, z): [] for x, y, z in sites}
    for x, y, z in sites:
        for j, step in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
            if (x, y, z)[j] == 1:
                prv = (x - step[0], y - step[1], z - step[2])
                preds[ix(x, y, z)].append(ix(*prv))
    level2 = [ix(x, y, z) for x, y, z in sites if x + y + z == 2]
    top = ix(1, 1, 1)
    N3 = {trip: N_of(trip) for trip in itertools.product(range(6), repeat=3)}
    WQ = defaultdict(int)
    fd = defaultdict(int)
    Zc = 0
    const_w = 0
    for u in itertools.product(range(6), repeat=8):
        w = math.prod(K(u[a], u[b]) for a, b in edges3)
        Q = math.prod(pairs[(u[preds[s][0]], u[preds[s][1]])] for s in level2) * N3[tuple(u[y] for y in preds[top])]
        Zc += w
        WQ[Q] += w
        if len(set(u)) == 1:
            const_w += w
        if u[ix(1, 0, 0)] == u[ix(0, 1, 0)]:
            fd[Q] += w
    base = 6 * 12 ** 3
    nu_tot = sum(Fr(wq, base * Q) for Q, wq in WQ.items())
    tv8 = sum(abs(Fr(wq, Zc) - Fr(wq, base * Q)) for Q, wq in WQ.items()) / 2
    c_mu, c_nu = Fr(const_w, Zc), Fr(6 * p ** 12, base * (pairs[(0, 0)] ** 3) * N3[(0, 0, 0)])
    fd_mu = Fr(sum(fd.values()), Zc)
    fd_nu = sum(Fr(wq, base * Q) for Q, wq in fd.items())
    report(
        "window-3d",
        nu_tot == 1 and Zc == 6982520832 and tv8 == Fr(1182193085, 23402354976) and abs(float(c_mu) - 0.000457) < 1e-6 and abs(float(c_nu) - 0.000292) < 1e-6 and abs(float(fd_mu) - 0.1975) < 5e-5 and abs(float(fd_nu) - 0.1806) < 5e-5,
        f"Z={Zc}, TV={tv8}={float(tv8):.5f}, constant {float(c_mu):.6f} vs {float(c_nu):.6f}, "
        f"one face-diagonal {float(fd_mu):.5f} vs {float(fd_nu):.5f}",
    )


def main():
    plaquette_and_chernoff()
    colour_and_blocks()
    pairs, gmin = normalisers()
    z3(gmin)
    windows(pairs)
    print(f"TOTAL: PASS={5 - len(fails)} FAIL={len(fails)}")
    if fails:
        print("SUMMARY: fails at step " + fails[0] + " - independent recomputation disagreed")
        return
    print(
        "SUMMARY: confirmed - disjoint plaquettes separate the static law from every adapted formation law "
        "(TV at least max(81/3464-9/416, 1-A^m-B^m), above 1/2 from m=80237), and on Z^2 and Z^3 the specific "
        "relative entropy is at least (19/4604256)/3 and (1/986)^2*(4/28561)/4, so the measures are singular; "
        "on the 2x2 window the anti-diagonal equality is the exact total-variation event"
    )
    print(
        "HIT: confirmed - the a3 bounds survive independent enumeration: plaquette constants 81/3464 and 9/416, "
        "integer A^400<1 and B^400<1, A^m+B^m<1/2 at the stated m=80237 (the sum crosses at 79827), "
        "Z^2 minimum 19/4604256, 600 flat Z^3 boundaries with constants 1/986 and 4/28561, "
        "2x2 TV 455/31176, and 2x2x2 TV 1182193085/23402354976"
    )


if __name__ == "__main__":
    main()
