#!/usr/bin/env python3
"""Independent referee for nonlinear record motion, attempt 1.

The attempt's script is not imported. Dynamics, the support graph, and
the mean-field symbol are recomputed here. The autocorrelation runs and
the floating-point modulus scan are not rebuilt.
"""
from __future__ import annotations

import math
import random
from collections import deque
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def step(gaps, speeds, V):
    n = len(gaps)
    move = tuple(min(speeds[i] + 1, V, gaps[i]) for i in range(n))
    new_gaps = tuple(gaps[i] - move[i] + move[(i + 1) % n] for i in range(n))
    return new_gaps, move


def occupied(origin, gaps, length):
    sites = []
    cursor = origin
    for gap in gaps:
        sites.append(cursor % length)
        cursor += gap + 1
    return sites


def in_free(gaps, speeds, V):
    return all(speed >= V - 1 for speed in speeds) and all(gap >= V for gap in gaps)


def in_jam(gaps, speeds, V):
    n = len(gaps)
    return all(gaps[i] <= min(speeds[i] + 1, V) for i in range(n)) and all(
        gaps[(i + 1) % n] <= gaps[i] + 1 for i in range(n)
    )


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for left in range(total + 1):
        for rest in compositions(total - left, parts - 1):
            yield (left,) + rest


def speeds_of(n, V):
    if n == 1:
        for speed in range(V + 1):
            yield (speed,)
        return
    for head in range(V + 1):
        for tail in speeds_of(n - 1, V):
            yield (head,) + tail


def regime_of(n, V, length):
    load = n * (V + 1)
    if load < length:
        return "free"
    if load > length:
        return "jam"
    return "equal"


def shifts_by(before, after, shift, length):
    return {site % length for site in after} == {(site + shift) % length for site in before}


def deterministic():
    """Every orbit on the executed rings ends in the claimed rigid motion."""
    bounds = {1: 9, 2: 8, 3: 7}
    states = lemmas = orbits = 0
    wrong_set = lemma_bad = orbit_bad = motion_bad = 0
    worst = 0
    samples = []
    for V, length_max in bounds.items():
        for length in range(V + 1, length_max + 1):
            for n in range(1, length):
                kind = regime_of(n, V, length)
                slack = length - n
                for gaps0 in compositions(slack, n):
                    for speeds0 in speeds_of(n, V):
                        states += 1
                        if kind == "free" and in_jam(gaps0, speeds0, V):
                            wrong_set += 1
                        if kind == "jam" and in_free(gaps0, speeds0, V):
                            wrong_set += 1
                        if kind == "equal":
                            free = in_free(gaps0, speeds0, V)
                            jam = in_jam(gaps0, speeds0, V)
                            if free != jam or (free and gaps0 != (V,) * n):
                                wrong_set += 1
                        gaps1, speeds1 = step(gaps0, speeds0, V)
                        lemmas += 1
                        if any(gap < 0 for gap in gaps1) or sum(gaps1) != slack:
                            lemma_bad += 1
                        elif any(gaps1[i] < speeds1[(i + 1) % n] for i in range(n)):
                            lemma_bad += 1
                        else:
                            for i in range(n):
                                move_now = min(speeds1[i] + 1, V, gaps1[i])
                                if move_now != gaps1[i]:
                                    continue
                                gaps2, speeds2 = step(gaps1, speeds1, V)
                                leader = (i + 1) % n
                                leader_move = min(speeds1[leader] + 1, V, gaps1[leader])
                                # Saturated at t=1: the next gap is the leader's move, and the next move copies it.
                                if speeds2[i] != move_now or gaps2[i] != leader_move or speeds2[i] != gaps1[i]:
                                    lemma_bad += 1
                                    continue
                                _gaps3, speeds3 = step(gaps2, speeds2, V)
                                if speeds3[i] != leader_move or gaps2[i] != speeds3[i]:
                                    lemma_bad += 1
                        seen = {}
                        cursor = (gaps0, speeds0)
                        entered = None
                        while cursor not in seen and entered is None:
                            if arrived(cursor[0], cursor[1], V, kind):
                                entered = cursor
                                break
                            seen[cursor] = len(seen)
                            nxt_gaps, nxt_speeds = step(cursor[0], cursor[1], V)
                            cursor = (nxt_gaps, nxt_speeds)
                        if entered is None:
                            orbit_bad += 1
                            continue
                        orbits += 1
                        worst = max(worst, len(seen))
                        if not motion_ok(entered, V, length, kind):
                            motion_bad += 1
    # The transient length above is only used as a recorded observation.
    check(
        "deterministic sets",
        wrong_set == 0,
        f"{states} states on V=1..3, L<=9/8/7: free excludes the jam set, jam excludes the free set, "
        "and on the equal line the two sets are the uniform gap V",
    )
    check(
        "deterministic lemmas",
        lemma_bad == 0,
        f"after one step on {lemmas} states the gap is at least the leader's speed, saturation persists, "
        "and the saturated record copies its leader",
    )
    check(
        "deterministic orbits",
        orbit_bad == 0 and motion_bad == 0 and orbits == states,
        f"all {orbits} orbits enter the rigid set for their density and then translate "
        f"(+V, -1, or both when the gaps are V); longest observed entry {worst}",
    )

    gaps = (0, 2)
    speeds = (0, 2)
    both = all(gaps[i] == min(speeds[i] + 1, 2, gaps[i]) for i in range(2))
    nxt, _ = step(gaps, speeds, 2)
    again, move = step(nxt, (0, 2), 2)
    # speeds after the first step are the first moves (0, 2)
    check(
        "deterministic t=0",
        both and nxt == (2, 0) and move[0] != nxt[0],
        "gaps (0, 2), speeds (0, 2), V=2: both saturated at step 0, and record 0 is not saturated at step 1",
    )

    rng = random.Random(20260926)
    bad_large = 0
    large_n = 0
    for length, V, n in (
        (40, 2, 8),
        (40, 2, 18),
        (40, 2, 13),
        (60, 4, 8),
        (60, 4, 20),
        (60, 4, 12),
        (80, 3, 10),
        (80, 3, 30),
        (80, 3, 20),
    ):
        for _ in range(6):
            large_n += 1
            gaps0 = random_gaps(rng, length - n, n)
            speeds0 = tuple(rng.randrange(V + 1) for _ in range(n))
            if not reaches(gaps0, speeds0, V, regime_of(n, V, length), length):
                bad_large += 1
    check(
        "deterministic larger rings",
        bad_large == 0,
        f"{large_n} random states on L=40, 60, 80 enter the same rigid motion; seed 20260926",
    )
    del samples


def arrived(gaps, speeds, V, kind):
    if kind == "free":
        return in_free(gaps, speeds, V)
    if kind == "jam":
        return in_jam(gaps, speeds, V)
    return gaps == (V,) * len(gaps) and in_free(gaps, speeds, V)


def motion_ok(state, V, length, kind):
    gaps, speeds = state
    origin = 0
    before = occupied(origin, gaps, length)
    new_gaps, move = step(gaps, speeds, V)
    after = occupied(origin + move[0], new_gaps, length)
    if kind == "free":
        return move == (V,) * len(gaps) and new_gaps == gaps and shifts_by(before, after, V, length)
    if kind == "jam":
        return move == gaps and in_jam(new_gaps, move, V) and shifts_by(before, after, -1, length)
    return (
        move == (V,) * len(gaps)
        and new_gaps == gaps
        and shifts_by(before, after, V, length)
        and shifts_by(before, after, -1, length)
    )


def reaches(gaps0, speeds0, V, kind, length, limit=20000):
    cursor = (gaps0, speeds0)
    seen = set()
    while cursor not in seen and len(seen) <= limit:
        if arrived(cursor[0], cursor[1], V, kind):
            return motion_ok(cursor, V, length, kind)
        seen.add(cursor)
        gaps, speeds = step(cursor[0], cursor[1], V)
        if any(gap < 0 for gap in gaps):
            return False
        cursor = (gaps, speeds)
    return False


def random_gaps(rng, total, parts):
    if parts == 1:
        return (total,)
    cuts = sorted(rng.sample(range(total + parts - 1), parts - 1))
    points = [-1] + cuts + [total + parts - 1]
    return tuple(points[i + 1] - points[i] - 1 for i in range(parts))


def encode(speeds, base):
    code = 0
    scale = 1
    for speed in speeds:
        code += (speed + 1) * scale
        scale *= base
    return code


def decode(code, length, base):
    speeds = []
    for _ in range(length):
        speeds.append(code % base - 1)
        code //= base
    return speeds


def occupied_count(code, length, base):
    count = 0
    for _ in range(length):
        if code % base:
            count += 1
        code //= base
    return count


def successors(code, length, base, V):
    speeds = decode(code, length, base)
    places = [i for i, speed in enumerate(speeds) if speed >= 0]
    n = len(places)
    if n == 0 or n == length:
        return []
    pre = []
    for k, site in enumerate(places):
        nxt = places[(k + 1) % n]
        gap = (nxt - site - 1) % length
        pre.append(min(speeds[site] + 1, V, gap))
    movable = [k for k, move in enumerate(pre) if move >= 1]
    found = []
    clash = False
    for mask in range(1 << len(movable)):
        move = pre[:]
        for bit, index in enumerate(movable):
            if mask & (1 << bit):
                move[index] -= 1
        board = [-1] * length
        clash = False
        for index, site in enumerate(places):
            dest = (site + move[index]) % length
            if board[dest] != -1:
                clash = True
                break
            board[dest] = move[index]
        if clash:
            break
        found.append(encode(board, base))
    return found, clash, pre, places, speeds


def support():
    """Unique aperiodic closed class on every executed finite ring."""
    specs = [(1, 8), (2, 7), (3, 6)]
    cases = states = 0
    reach_bad = period_bad = rise_bad = clash_bad = cruise_bad = 0
    for V, length_max in specs:
        for length in range(2, length_max + 1):
            base = V + 2
            total = base ** length
            forward = [[] for _ in range(total)]
            counts = [0] * (length + 1)
            for code in range(total):
                count = occupied_count(code, length, base)
                if count == 0 or count == length:
                    continue
                counts[count] += 1
                succ, clash, pre, places, speeds = successors(code, length, base, V)
                if clash:
                    clash_bad += 1
                forward[code] = succ
                slowed = pre[:]
                for index, move in enumerate(slowed):
                    if move >= 1:
                        slowed[index] -= 1
                for index, site in enumerate(places):
                    if slowed[index] > speeds[site]:
                        rise_bad += 1
            reverse = [[] for _ in range(total)]
            for code in range(total):
                for nxt in forward[code]:
                    reverse[nxt].append(code)
            for n in range(1, length):
                cases += 1
                states += counts[n]
                cruise = n == 1 and min(V, length - 1) >= 2
                if cruise:
                    ref = min(V, length - 1) + 1
                else:
                    ref = sum(base ** i for i in range(n))
                seen = {ref}
                queue = deque([ref])
                while queue:
                    node = queue.popleft()
                    for prev in reverse[node]:
                        if prev not in seen:
                            seen.add(prev)
                            queue.append(prev)
                if len(seen) != counts[n]:
                    reach_bad += 1
                gcd, closure = period_of(ref, forward)
                if gcd != 1:
                    period_bad += 1
                if cruise:
                    allowed = {min(V, length - 1) - 1, min(V, length - 1)}
                    if not cruise_ok(ref, forward, length, base, allowed):
                        cruise_bad += 1
                    if not returns_at(ref, forward, length) or not returns_at(ref, forward, length + 1):
                        cruise_bad += 1
                elif not has_self_loop(ref, forward):
                    period_bad += 1
                del closure
    check(
        "support graph",
        reach_bad == 0 and period_bad == 0 and rise_bad == 0 and clash_bad == 0 and cruise_bad == 0,
        f"{cases} rings, {states} states, V=1 L<=8, V=2 L<=7, V=3 L<=6: one closed class, period 1; "
        "all-slowdown never raises a speed; a lone record with room cruises in {m-1, m} and returns in L and L+1 steps. "
        "The author's 1184754-state graph was not rebuilt",
    )
    check("lowering maneuver", lowering_trace(), "from a common speed 2, withholding one slowdown drops the next common speed")


def has_self_loop(ref, forward):
    return ref in forward[ref]


def period_of(ref, forward):
    level = {ref: 0}
    queue = deque([ref])
    gcd = 0
    while queue:
        node = queue.popleft()
        for nxt in forward[node]:
            if nxt not in level:
                level[nxt] = level[node] + 1
                queue.append(nxt)
            else:
                gcd = math.gcd(gcd, level[node] + 1 - level[nxt])
    return gcd, len(level)


def cruise_ok(ref, forward, length, base, allowed):
    level = {ref}
    queue = deque([ref])
    while queue:
        node = queue.popleft()
        for speed in decode(node, length, base):
            if speed >= 0 and speed not in allowed:
                return False
        for nxt in forward[node]:
            if nxt not in level:
                level.add(nxt)
                queue.append(nxt)
    return True


def returns_at(ref, forward, steps):
    layer = {ref}
    for _ in range(steps):
        layer = {nxt for node in layer for nxt in forward[node]}
    return ref in layer


def lowering_trace():
    """N=3, L=12, V=3, gaps (3,3,3), speeds (2,2,2). Record 0 does not slow until its gap is 2."""
    gaps = [3, 3, 3]
    speeds = [2, 2, 2]
    V = 3
    for _ in range(6):
        if gaps[0] <= 2:
            break
        gaps, speeds = policy_step(gaps, speeds, V, noslow={0})
    if gaps[0] != 2 or speeds[0] < 3:
        return False
    gaps, speeds = policy_step(gaps, speeds, V, noslow=set())
    if speeds[0] != 1:
        return False
    for _ in range(8):
        if len(set(speeds)) == 1:
            break
        gaps, speeds = policy_step(gaps, speeds, V, noslow=set())
    return len(set(speeds)) == 1 and speeds[0] <= 1 and all(gap >= 0 for gap in gaps)


def policy_step(gaps, speeds, V, noslow):
    n = len(gaps)
    pre = [min(speeds[i] + 1, V, gaps[i]) for i in range(n)]
    move = []
    for i, raw in enumerate(pre):
        if i not in noslow and raw >= 1:
            raw -= 1
        move.append(raw)
    new_gaps = [gaps[i] - move[i] + move[(i + 1) % n] for i in range(n)]
    return new_gaps, move


def mean_field():
    outside = (
        (2, sp.Integer(0), sp.Rational(3, 20), sp.Rational(-5, 13) + sp.I * sp.Rational(12, 13)),
        (2, sp.Rational(1, 50), sp.Rational(3, 20), sp.Rational(-5, 13) + sp.I * sp.Rational(12, 13)),
        (5, sp.Integer(0), sp.Rational(1, 50), sp.Rational(-8, 17) + sp.I * sp.Rational(15, 17)),
    )
    points = (
        (1, sp.Rational(1, 4), sp.Rational(1, 3), 5),
        (2, sp.Rational(1, 4), sp.Rational(1, 4), 7),
        (2, sp.Integer(0), sp.Rational(3, 20), 7),
        (3, sp.Rational(1, 2), sp.Rational(1, 10), 9),
    )
    jacobian_ok = True
    for V, rate, rho, length in points:
        jacobian_ok &= jacobian_matches(V, rate, rho, length)
    check(
        "mean-field jacobian",
        jacobian_ok,
        "uniform fixed point and symbol weights match unit differences of the ring map at 4 points",
    )

    identity_ok = density_identity()
    scalar_ok = True
    for rate, rho in ((sp.Rational(1, 4), sp.Rational(1, 3)), (sp.Integer(0), sp.Rational(1, 5)), (sp.Rational(1, 2), sp.Rational(7, 10))):
        scalar_ok &= v1_weights(rate, rho)
    check(
        "mean-field V=1",
        identity_ok and scalar_ok,
        "density weights are r, (1-r)(1-rho), (1-r)rho; "
        "1-|lambda|^2 = 2p(1-p)(1-cos k) + 4p^2 rho(1-rho) sin^2 k with p=1-r",
    )

    signed = []
    signed_ok = True
    for V in (2, 3, 5):
        count, least = negative_weights(V, sp.Rational(1, 4), sp.Rational(1, 4))
        signed.append((V, count, least))
        signed_ok &= count > 0
    signed_ok &= signed[0][1] == 3 and signed[0][2] == sp.Rational(-111, 880)
    check(
        "mean-field signs",
        signed_ok,
        "at r=rho=1/4 the speed weights are negative: "
        + ", ".join(f"V={V} count {count} least {least}" for V, count, least in signed),
    )

    schur_ok = (
        schur_inside([sp.Rational(-1, 2), 1])
        and schur_inside([-1, 2])
        and not schur_inside([-2, 1])
        and not schur_inside([-1, 1])
    )
    angles = (
        sp.Rational(4, 5) + sp.I * sp.Rational(3, 5),
        sp.Rational(3, 5) + sp.I * sp.Rational(4, 5),
        sp.I,
        sp.Rational(-5, 13) + sp.I * sp.Rational(12, 13),
        sp.Rational(-3, 5) + sp.I * sp.Rational(4, 5),
        sp.Integer(-1),
    )
    stable = total = 0
    for V in (2, 3, 5):
        for rate in (sp.Rational(1, 4), sp.Rational(1, 2)):
            for rho in (sp.Rational(1, 10), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(4, 5)):
                table, dist, gain = weights(V, rate, rho)
                for angle in angles:
                    total += 1
                    if schur_inside(char_coeffs(symbol(V, table, gain, angle))):
                        stable += 1
    check(
        "mean-field damping",
        schur_ok and stable == total == 144,
        f"all roots strictly inside at {stable}/{total} points "
        "V in {2,3,5}, r in {1/4,1/2}, rho in {1/10,1/4,1/2,4/5}, six roots of unity angles",
    )

    moduli = []
    outside_ok = True
    for V, rate, rho, angle in outside:
        outside_ok &= sp.simplify(angle * sp.conjugate(angle)) == 1
        table, dist, gain = weights(V, rate, rho)
        coeffs = char_coeffs(symbol(V, table, gain, angle))
        outside_ok &= (not schur_inside(coeffs)) and resultant_nonzero(coeffs)
        moduli.append(max_root_modulus(coeffs))
    check(
        "mean-field outside roots",
        outside_ok and all(mod > 1 for mod in moduli),
        "Schur-Cohn fails and the resultant with the reciprocal is nonzero at the three stated points; "
        f"float max moduli {moduli}. The modulus scan over the (V, r, rho) grid was not rebuilt",
    )


def trans(V, rate, ahead):
    size = V + 1
    table = [[sp.Integer(0) for _ in range(size)] for _ in range(size)]
    for speed in range(size):
        room = min(speed + 1, V)
        empty = sp.Integer(1)
        mass = []
        for site in range(room):
            mass.append(empty * ahead[site])
            empty *= 1 - ahead[site]
        mass.append(empty)
        for raw in range(room + 1):
            if raw >= 1:
                table[speed][raw] += (1 - rate) * mass[raw]
                table[speed][raw - 1] += rate * mass[raw]
            else:
                table[speed][0] += mass[0]
    return table


def stationary(table):
    size = len(table)
    matrix = sp.zeros(size)
    target = sp.zeros(size, 1)
    for dest in range(size - 1):
        for speed in range(size):
            matrix[dest, speed] = table[speed][dest] - (1 if dest == speed else 0)
    for speed in range(size):
        matrix[size - 1, speed] = 1
    target[size - 1] = 1
    solved = matrix.LUsolve(target)
    return [sp.together(solved[speed]) for speed in range(size)]


def weights(V, rate, rho):
    table = trans(V, rate, [rho] * V)
    dist = stationary(table)
    gain = [[sp.Integer(0) for _ in range(V)] for _ in range(V + 1)]
    for site in range(V):
        high = [rho] * V
        low = [rho] * V
        high[site] = 1
        low[site] = 0
        above = trans(V, rate, high)
        below = trans(V, rate, low)
        for dest in range(V + 1):
            gain[dest][site] = sp.together(
                sum(rho * dist[speed] * (above[speed][dest] - below[speed][dest]) for speed in range(V + 1))
            )
    column = [sum(table[speed][dest] for dest in range(V + 1)) for speed in range(V + 1)]
    if any(entry != 1 for entry in column):
        raise RuntimeError("transition columns do not sum to 1")
    if any(sp.together(sum(gain[dest][site] for dest in range(V + 1))) != 0 for site in range(V)):
        raise RuntimeError("density derivatives do not sum to 0")
    return table, dist, gain


def canonical(expr):
    number = sp.expand(expr)
    return sp.together(sp.re(number)) + sp.I * sp.together(sp.im(number))


def symbol(V, table, gain, angle):
    inverse = sp.expand(1 / angle)
    rows = []
    for dest in range(V + 1):
        extra = sum(gain[dest][site] * inverse ** (dest - (site + 1)) for site in range(V))
        rows.append(
            [canonical(inverse ** dest * table[speed][dest] + extra) for speed in range(V + 1)]
        )
    return sp.Matrix(rows)


def char_coeffs(matrix):
    lam = sp.symbols("lam")
    high = matrix.charpoly(lam).all_coeffs()
    return [sp.together(coef) for coef in reversed(high)]


class Gauss:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = a if isinstance(a, F) else F(a)
        self.b = b if isinstance(b, F) else F(b)

    def __add__(self, other):
        other = other if isinstance(other, Gauss) else Gauss(other)
        return Gauss(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        other = other if isinstance(other, Gauss) else Gauss(other)
        return Gauss(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        other = other if isinstance(other, Gauss) else Gauss(other)
        return Gauss(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def conj(self):
        return Gauss(self.a, -self.b)

    def n2(self):
        return self.a * self.a + self.b * self.b

    def iszero(self):
        return self.a == 0 and self.b == 0


def as_frac(expr):
    rat = sp.Rational(sp.together(expr))
    return F(rat.p, rat.q)


def as_gauss(expr):
    number = sp.expand(expr)
    return Gauss(as_frac(sp.re(number)), as_frac(sp.im(number)))


def schur_inside(coeffs):
    values = [as_gauss(coef) for coef in coeffs]
    while len(values) > 1 and values[-1].iszero():
        values.pop()
    while len(values) > 1:
        low, high = values[0], values[-1]
        if low.n2() >= high.n2():
            return False
        degree = len(values) - 1
        folded = [high.conj() * values[index] - low * values[degree - index].conj() for index in range(degree + 1)]
        if not folded[0].iszero():
            return False
        values = folded[1:]
    return bool(values)


def resultant_nonzero(coeffs):
    lam = sp.symbols("lam")
    degree = len(coeffs) - 1
    poly = sum(coeffs[index] * lam ** index for index in range(degree + 1))
    star = sum(sp.conjugate(coeffs[degree - index]) * lam ** index for index in range(degree + 1))
    return sp.resultant(sp.expand(poly), sp.expand(star), lam) != 0


def max_root_modulus(coeffs):
    import numpy as np

    roots = np.roots([complex(coef) for coef in reversed(coeffs)])
    return round(float(max(abs(root) for root in roots)), 5)


def ring_map(fields, V, rate):
    length = len(fields[0])
    density = [sum(fields[speed][site] for speed in range(V + 1)) for site in range(length)]
    out = [[sp.Integer(0) for _ in range(length)] for _ in range(V + 1)]
    for site in range(length):
        table = trans(V, rate, [density[(site + ahead) % length] for ahead in range(1, V + 1)])
        for speed in range(V + 1):
            mass = fields[speed][site]
            if mass == 0:
                continue
            for dest in range(V + 1):
                out[dest][(site + dest) % length] += mass * table[speed][dest]
    return out


def jacobian_matches(V, rate, rho, length):
    table, dist, gain = weights(V, rate, rho)
    base = [[rho * dist[speed] for _ in range(length)] for speed in range(V + 1)]
    image = ring_map(base, V, rate)
    if any(sp.together(image[speed][site] - base[speed][site]) != 0 for speed in range(V + 1) for site in range(length)):
        return False
    for speed in range(V + 1):
        for site in range(length):
            bumped = [row[:] for row in base]
            bumped[speed][site] += 1
            delta = ring_map(bumped, V, rate)
            for dest in range(V + 1):
                for place in range(length):
                    shift = (place - site) % length
                    want = table[speed][dest] if shift == dest else 0
                    for ahead in range(V):
                        disp = dest - (ahead + 1)
                        if disp % length == shift:
                            want += gain[dest][ahead]
                    if sp.together(delta[dest][place] - image[dest][place] - want) != 0:
                        return False
    return True


def density_identity():
    rate, rho, cosine, sine = sp.symbols("r rho c s", real=True)
    keep = 1 - rate
    real = rate + keep * cosine
    imag = keep * (2 * rho - 1) * sine
    modulus = sp.expand(real ** 2 + imag ** 2)
    target = 2 * keep * rate * (1 - cosine) + 4 * keep ** 2 * rho * (1 - rho) * sine ** 2
    difference = sp.expand((1 - modulus - target).subs(sine ** 2, 1 - cosine ** 2))
    return difference == 0


def v1_weights(rate, rho):
    length = 7
    table, dist, _gain = weights(1, rate, rho)
    if any(table[0][dest] != table[1][dest] for dest in range(2)):
        return False
    base = [[rho * dist[speed] for _ in range(length)] for speed in range(2)]
    image = ring_map(base, 1, rate)
    bumped = [row[:] for row in base]
    bumped[0][0] += 1
    delta = ring_map(bumped, 1, rate)
    change = [sp.together(sum(delta[speed][site] - image[speed][site] for speed in range(2))) for site in range(length)]
    keep = 1 - rate
    expect = [sp.Integer(0)] * length
    expect[0] = rate
    expect[1] = keep * (1 - rho)
    expect[length - 1] = keep * rho
    return change == [sp.together(item) for item in expect]


def negative_weights(V, rate, rho):
    _table, _dist, gain = weights(V, rate, rho)
    values = [gain[dest][site] for dest in range(V + 1) for site in range(V)]
    negative = [value for value in values if value < 0]
    return len(negative), min(negative)


def main():
    deterministic()
    support()
    mean_field()
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. At r=0 every orbit on the executed rings, and 54 random states on "
        "L=40, 60 and 80, ends in rigid translation of the occupied set: +V below density 1/(V+1), a jam "
        "wave at -1 above, and both when every gap equals V. For 0<r<1 the executed finite rings have one "
        "aperiodic closed class. The V=1 mean field damps every nonzero mode, and the V>=2 linearization "
        "has a root outside the unit circle at the three stated points and is damped at the 144 rational "
        "points. The autocorrelation runs and the modulus scan were not rebuilt. Geometric convergence of "
        "a finite chain is imported, not re-proved.",
        flush=True,
    )
    print(
        "HIT: confirmed - at r=0 the occupied set eventually translates by +V or by the jam wave -1, "
        "for 0<r<1 every executed finite ring has one aperiodic closed class, and the mean-field "
        "linearization is not always damped",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
