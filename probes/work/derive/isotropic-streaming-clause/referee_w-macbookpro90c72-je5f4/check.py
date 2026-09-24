#!/usr/bin/env python3
"""Referee for the isotropic streaming clause, a1.

Author w-jonathonsmac4f50-j8197 (claude-opus-5-5). Own shell sums.
The far-shadow density uses the strong law, which the attempt assumes.
The full 3^3 census is repeated with a fixed rational rate table.
"""
import itertools
from fractions import Fraction as Fr

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def shells():
    axis = [d for d in itertools.product((-1, 0, 1), repeat=3) if sum(v * v for v in d) == 1]
    face = [d for d in itertools.product((-1, 0, 1), repeat=3) if sum(v * v for v in d) == 2]
    body = [d for d in itertools.product((-1, 1), repeat=3)]
    return {1: axis, 2: face, 3: body}


SHELL = shells()


def sphere():
    t = sp.symbols("t", real=True)
    # t = s·n is uniform on [-1, 1]. Transverse variance is (1-t^2)/2.
    mean_abs = sp.integrate(sp.Abs(t) / 2, (t, -1, 1))
    longitudinal = sp.integrate(t ** 2 * sp.Abs(t) / 2, (t, -1, 1))
    transverse = sp.integrate((1 - t ** 2) / 2 * sp.Abs(t) / 2, (t, -1, 1))
    odd = sp.integrate(t / 2, (t, -1, 1))
    report(
        "sphere",
        mean_abs == sp.Rational(1, 2)
        and longitudinal == sp.Rational(1, 4)
        and transverse == sp.Rational(1, 8)
        and odd == 0,
        "<|s.n|>=1/2, <s_n^2 |s.n|>=1/4, <s_transverse^2 |s.n|>=1/8, and the odd part of (s.n) averages to 0",
    )


def moment():
    l1, l2, l3 = sp.symbols("lambda1 lambda2 lambda3", nonnegative=True)
    weight = {1: l1, 2: l2, 3: l3}
    # T_ijkl = sum_d lambda (d_k d_l) (delta_ij + dhat_i dhat_j) / 16
    T = {}
    S = [[0, 0, 0] for _ in range(3)]
    for radius, vecs in SHELL.items():
        lam = weight[radius]
        for vec in vecs:
            norm2 = radius
            for i in range(3):
                for j in range(3):
                    S[i][j] += lam * vec[i] * vec[j]
            for i, j, k, l in itertools.product(range(3), repeat=4):
                dhat_ij = sp.Integer(vec[i] * vec[j]) / norm2
                piece = lam * vec[k] * vec[l] * ((1 if i == j else 0) + dhat_ij) / 16
                T[(i, j, k, l)] = T.get((i, j, k, l), 0) + piece
    isotropic = l1 - l2 - sp.Rational(8, 3) * l3
    depart = sp.simplify(T[(0, 0, 0, 0)] - T[(0, 0, 1, 1)] - 2 * T[(0, 1, 0, 1)] - isotropic / 8)
    second = sp.simplify(S[0][0] - (2 * l1 + 8 * l2 + 8 * l3))
    off = sp.simplify(S[0][1])
    axis = {l1: 1 / sp.sqrt(3), l2: 0, l3: 0}
    block = (
        sp.simplify(T[(0, 0, 0, 0)].subs(axis) - 1 / (4 * sp.sqrt(3))) == 0
        and sp.simplify(T[(0, 0, 1, 1)].subs(axis) - 1 / (8 * sp.sqrt(3))) == 0
        and sp.simplify(T[(0, 1, 0, 1)].subs(axis)) == 0
    )
    line = {l1: l2 + sp.Rational(8, 3) * l3}
    alpha = sp.simplify(T[(0, 0, 1, 1)].subs(line))
    beta = sp.simplify(T[(0, 1, 0, 1)].subs(line))
    alpha_ok = sp.simplify(alpha - (sp.Rational(3, 4) * l2 + l3)) == 0
    beta_ok = sp.simplify(beta - (l2 / 8 + l3 / 6)) == 0
    # <M> = S/4, number diffusivity is half its eigenvalue.
    number = sp.simplify((S[0][0] / 4 / 2).subs(line) - (sp.Rational(5, 4) * l2 + sp.Rational(5, 3) * l3))
    report(
        "moment",
        depart == 0 and second == 0 and off == 0 and block and alpha_ok and beta_ok and number == 0,
        "T is isotropic iff lambda1 = lambda2 + (8/3) lambda3; on that line alpha=(3/4)lambda2+lambda3, beta=lambda2/8+lambda3/6, D_n=(5/4)lambda2+(5/3)lambda3",
    )


def drift():
    l1, l2, l3 = sp.symbols("lambda1 lambda2 lambda3", nonnegative=True)
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    content = (s1, s2, s3)
    weight = {1: l1, 2: l2, 3: l3}
    kappa = l1 + 2 * sp.sqrt(2) * l2 + 4 * l3 / sp.sqrt(3)
    # Pair identity: (u)_+ d + (-u)_+ (-d) = u d, so each undirected pair contributes lambda (s·dhat) d.
    mean = [0, 0, 0]
    seen = set()
    for radius, vecs in SHELL.items():
        for vec in vecs:
            key = tuple(sorted((vec, tuple(-v for v in vec))))
            if key in seen:
                continue
            seen.add(key)
            dot = sum(content[i] * vec[i] for i in range(3)) / sp.sqrt(radius)
            for i in range(3):
                mean[i] += weight[radius] * dot * vec[i]
    samples = [
        (1, 0, 0),
        (0, 1, 0),
        (sp.Rational(3, 5), sp.Rational(4, 5), 0),
        (1 / sp.sqrt(2), 1 / sp.sqrt(2), 0),
        (1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)),
        (1 / sp.sqrt(3), 1 / sp.sqrt(3), -1 / sp.sqrt(3)),
        (2 / sp.sqrt(5), 1 / sp.sqrt(5), 0),
        (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)),
        (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)),
    ]
    ok = len(seen) == 13 and all(
        sp.simplify(mean[i].subs({s1: a, s2: b, s3: c}) - kappa * (a, b, c)[i]) == 0
        for a, b, c in samples
        for i in range(3)
    )
    # The algebraic pair reduction itself.
    u, d0 = sp.symbols("u d0", real=True)
    plus = (u + sp.Abs(u)) / 2
    minus = (-u + sp.Abs(u)) / 2
    pair = sp.simplify(plus * d0 + minus * (-d0) - u * d0)
    report(
        "drift",
        ok and pair == 0,
        "each opposite pair contributes (s·dhat) d, and the mean displacement is kappa s with kappa = lambda1 + 2*sqrt(2)*lambda2 + 4*lambda3/sqrt(3)",
    )


def potential():
    x, y, z = sp.symbols("x y z", real=True, nonzero=True)
    radius = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    chi = 1 / radius
    lap = sum(sp.diff(chi, v, 2) for v in (x, y, z))
    grad = [sp.diff(chi, v) for v in (x, y, z)]
    lap_grad = [sum(sp.diff(component, v, 2) for v in (x, y, z)) for component in grad]
    cleared = sp.simplify(sp.together(lap * radius ** 3))
    cleared_g = [sp.simplify(sp.together(component * radius ** 5)) for component in lap_grad]
    report(
        "potential",
        cleared == 0 and all(piece == 0 for piece in cleared_g),
        "away from the origin, grad(1/r) is divergence-free and each component is harmonic, so both streaming terms vanish",
    )


def capture():
    l1, l2, l3 = sp.symbols("lambda1 lambda2 lambda3", nonnegative=True)
    weight = {1: l1, 2: l2, 3: l3}

    def direct(content):
        total = 0
        for radius, vecs in SHELL.items():
            for vec in vecs:
                dot = sum(content[i] * vec[i] for i in range(3))
                total += weight[radius] * sp.Max(dot, 0) / sp.sqrt(radius)
        return total

    def closed(content):
        axes = sum(sp.Abs(c) for c in content)
        pairs = sum(
            sp.Max(sp.Abs(content[i]), sp.Abs(content[j]))
            for i, j in ((0, 1), (0, 2), (1, 2))
        )
        signs = 0
        for pattern in itertools.product((1, -1), repeat=2):
            signed = content[0] + pattern[0] * content[1] + pattern[1] * content[2]
            signs += sp.Abs(signed)
        return l1 * axes + l2 * sp.sqrt(2) * pairs + l3 * signs / sp.sqrt(3)

    directions = [
        (1, 0, 0),
        (0, 1, 0),
        (1 / sp.sqrt(2), 1 / sp.sqrt(2), 0),
        (1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)),
        (sp.Rational(3, 5), sp.Rational(4, 5), 0),
        (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)),
        (2 / sp.sqrt(5), -1 / sp.sqrt(5), 0),
        (1 / sp.sqrt(3), -1 / sp.sqrt(3), 1 / sp.sqrt(3)),
        (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)),
    ]
    agree = all(sp.simplify(direct(vec) - closed(vec)) == 0 for vec in directions)
    axis = direct((1, 0, 0))
    body = direct((1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)))
    line = {l1: l2 + sp.Rational(8, 3) * l3}
    gap = sp.expand(sp.simplify((body - axis).subs(line)))
    c2 = sp.simplify(gap.coeff(l2))
    c3 = sp.simplify(gap.coeff(l3))
    wanted2 = sp.sqrt(3) + sp.sqrt(6) - 1 - 2 * sp.sqrt(2)
    wanted3 = sp.Rational(4, 3) * sp.sqrt(3) - sp.Rational(2, 3)
    positive = float(c2) > 0 and float(c3) > 0
    # Three members. Compare the three direction classes.
    members = {
        "axis": {l1: 1 / sp.sqrt(3), l2: 0, l3: 0},
        "face": {l1: 1, l2: 1, l3: 0},
        "body": {l1: 8, l2: 0, l3: 3},
    }
    classes = {
        "axis": (1, 0, 0),
        "face": (1 / sp.sqrt(2), 1 / sp.sqrt(2), 0),
        "body": (1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)),
    }
    spreads = {}
    for name, subs in members.items():
        vals = [sp.simplify(direct(vec).subs(subs)) for vec in classes.values()]
        spreads[name] = sp.simplify(max(vals, key=lambda v: float(v)) / min(vals, key=lambda v: float(v)))
    report(
        "capture",
        agree
        and sp.simplify(c2 - wanted2) == 0
        and sp.simplify(c3 - wanted3) == 0
        and positive
        and abs(float(spreads["axis"]) - sp.sqrt(3)) < 1e-12
        and abs(float(spreads["face"]) - 1.1530) < 5e-5
        and abs(float(spreads["body"]) - 1.3301) < 5e-5,
        "closed capture matches the 26-neighbour sum; on the isotropy line body exceeds axis by "
        f"{c2}*lambda2+{c3}*lambda3; spreads are sqrt(3), {float(spreads['face']):.4f}, {float(spreads['body']):.4f}",
    )


def census():
    sites = list(itertools.product(range(3), repeat=3))
    solid = {(0, 0, 0)}
    hops = [vec for vecs in SHELL.values() for vec in vecs]
    contents = (0, 1, 2, 3, 4, 5)
    # Fixed positive rationals. Opposite content reverses the hop, as the shell rule does.
    rates = {}
    for label, scale in ((0, 1), (2, 2), (4, 3)):
        rates[label] = {hop: Fr(1 + (abs(sum(hop)) + scale) % 5, 1 + (scale + hop[0]) % 4) for hop in hops}
        rates[label ^ 1] = {hop: rates[label][tuple(-v for v in hop)] for hop in hops}
    vectors = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}

    def wrap(point):
        return tuple(v % 3 for v in point)

    def run(count, labels, blocked, exchange):
        free = [site for site in sites if site not in blocked]
        inflow, outflow = {}, {}

        def add(book, key, value):
            book[key] = book.get(key, 0) + value

        configs = []
        for occupied in itertools.combinations(free, count):
            for choice in itertools.product(labels, repeat=count):
                configs.append(tuple(sorted(zip(occupied, choice))))
        for conf in configs:
            where = dict(conf)
            for place, label in conf:
                for hop, rate in rates[label].items():
                    target_site = wrap((place[0] + hop[0], place[1] + hop[1], place[2] + hop[2]))
                    moved = dict(where)
                    if target_site in blocked:
                        moved[place] = label ^ 1
                    elif target_site in where:
                        if not exchange:
                            continue
                        moved[place], moved[target_site] = where[target_site], label
                    else:
                        del moved[place]
                        moved[target_site] = label
                    arrived = tuple(sorted(moved.items()))
                    add(outflow, conf, rate)
                    add(inflow, arrived, rate)
        bad = sum(1 for conf in configs if inflow.get(conf, 0) != outflow.get(conf, 0))
        return len(configs), bad

    with_solid = run(2, contents, solid, True)
    plain = run(2, contents, set(), True)
    three = run(3, (0, 1), set(), True)
    no_exchange = run(2, contents, set(), False)
    # Reflection identity of the shell rule: a(-s, d) = a(s, -d).
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    content = (s1, s2, s3)
    reflection = True
    for radius, vecs in SHELL.items():
        lam = sp.symbols("lam", positive=True)
        for vec in vecs[:1]:
            forward = lam * sp.Max(sum((-content[i]) * vec[i] for i in range(3)), 0) / sp.sqrt(radius)
            backward = lam * sp.Max(sum(content[i] * (-vec[i]) for i in range(3)), 0) / sp.sqrt(radius)
            reflection &= sp.simplify(forward - backward) == 0
    report(
        "census",
        with_solid == (11700, 0)
        and plain == (12636, 0)
        and three[0] == 23400
        and three[1] == 0
        and no_exchange[0] == 12636
        and no_exchange[1] > 0
        and reflection,
        f"with exchange, unbalanced counts are 0 on {with_solid[0]}, {plain[0]} and {three[0]} configurations; "
        f"without exchange, {no_exchange[1]} of {no_exchange[0]} fail. The shell rule reverses under reflection",
    )


def main():
    sphere()
    moment()
    drift()
    potential()
    capture()
    census()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the forward-only shell rule has mean displacement kappa s with one constant, "
        "and its fourth-rank moment is isotropic exactly when lambda1 = lambda2 + (8/3) lambda3. "
        "On that line the streaming term is (3/2)[alpha Lap g + 2 beta grad div g] and it vanishes for g=grad(1/r). "
        "The uniform product measure balances for every rate table tested, with exchange. "
        "The capture rate is never constant on this family: on the isotropy line a body diagonal is captured faster than an axis."
    )
    print(
        "SUMMARY: confirmed the sphere moments, the isotropy line, the drift, the potential cancellation, "
        "the capture spreads sqrt(3), 1.153 and 1.330, and the 3^3 balance. "
        "The strong-law step from flux to a pointwise shadow density is the attempt's assumption."
    )


if __name__ == "__main__":
    main()
