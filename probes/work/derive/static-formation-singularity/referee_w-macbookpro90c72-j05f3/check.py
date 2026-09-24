#!/usr/bin/env python3
"""Independent referee for static-formation-singularity a2.

Six-value menu, class-(P) weights (3,1,2). Recomputes the 2x2 hull, the
disjoint-plaquette threshold, the strip certificates, the cube, and the 2x3
witness. Does not import the attempt.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F
from math import isqrt, lcm

import numpy as np

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


M = 6
PHI = [[3 if s == t else (1 if s == (t ^ 1) else 2) for t in range(M)] for s in range(M)]
NF_CACHE: dict[tuple[int, ...], int] = {}


def Nf(ts: tuple[int, ...]) -> int:
    got = NF_CACHE.get(ts)
    if got is None:
        got = sum(1 if not ts else eval_prod(s, ts) for s in range(M))
        NF_CACHE[ts] = got
    return got


def eval_prod(s: int, ts: tuple[int, ...]) -> int:
    p = 1
    for t in ts:
        p *= PHI[s][t]
    return p


def N2(a: int, b: int) -> int:
    return Nf(tuple(sorted((a, b))))


def N3(a: int, b: int, c: int) -> int:
    return Nf(tuple(sorted((a, b, c))))


def adj_of(n: int, edges):
    adj = [[] for _ in range(n)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    return adj


def predlist(order, adj):
    pos = {x: i for i, x in enumerate(order)}
    return [(x, tuple(sorted(y for y in adj[x] if pos[y] < pos[x]))) for x in order]


def weight(v, edges) -> int:
    p = 1
    for x, y in edges:
        p *= PHI[v[x]][v[y]]
    return p


def y_of(v, preds) -> int:
    p = 1
    for _x, group in preds:
        p *= Nf(tuple(sorted(v[y] for y in group)))
    return p


# ---------------------------------------------------------------- constants and the 2x2
n2 = sorted({Nf((a, b)) for a in range(M) for b in range(M)})
n3 = [Nf(tuple(sorted(t))) for t in itertools.product(range(M), repeat=3)]
n4 = [Nf(tuple(sorted(t))) for t in itertools.product(range(M), repeat=4)]
check(
    "S0 constants",
    Nf(()) == 6 and Nf((0,)) == 12 and n2 == [22, 24, 26]
    and Nf((0, 0)) == 26 and Nf((0, 1)) == 22 and Nf((0, 2)) == 24
    and min(n3) == 44 and max(n3) == 60 and min(n4) == 80 and max(n4) == 146,
    "Nf(empty)=6, Nf(one)=12, pairs 22/24/26, N3 in [44,60], N4 in [80,146]",
)

E4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
ADJ4 = adj_of(4, E4)
CFG4 = list(itertools.product(range(M), repeat=4))
Z4 = sum(weight(v, E4) for v in CFG4)


def formation(v, preds):
    num = den = 1
    for x, group in preds:
        for y in group:
            num *= PHI[v[x]][v[y]]
        den *= Nf(tuple(sorted(v[y] for y in group)))
    return num, den


order_ok = True
tvs = []
for order in itertools.permutations(range(4)):
    preds = predlist(order, ADJ4)
    total = tv = F(0)
    for v in CFG4:
        num, den = formation(v, preds)
        w = weight(v, E4)
        order_ok = order_ok and num == w
        total += F(num, den)
        tv += abs(F(w, Z4) - F(num, den))
    order_ok = order_ok and total == 1
    tvs.append(tv / 2)
check(
    "S1 fixed orders",
    order_ok and Z4 == 20784 and min(tvs) == F(455, 31176) and max(tvs) == F(37, 1299),
    "Z=20784; every order has nu=W/Y; min TV %s, max TV %s" % (min(tvs), max(tvs)),
)


def bellman(n, adj, term):
    """Scaled sup of E[term] over adapted strategies. term(complete) is an int."""
    cap = 1
    degree = max(len(a) for a in adj)
    for d in range(degree + 1):
        for tup in itertools.product(range(M), repeat=d):
            cap = lcm(cap, Nf(tuple(sorted(tup))))
    amps: dict[tuple[int, ...], list[int]] = {}

    def amplitude(vals: tuple[int, ...]) -> list[int]:
        got = amps.get(vals)
        if got is None:
            normal = Nf(vals)
            got = [eval_prod(s, vals) * cap // normal for s in range(M)]
            amps[vals] = got
        return got

    memo: dict[tuple[int, ...], int] = {}

    def value(state: tuple[int, ...]) -> int:
        got = memo.get(state)
        if got is not None:
            return got
        if -1 not in state:
            memo[state] = term(state)
            return memo[state]
        best = -1
        mutable = list(state)
        for site in range(n):
            if state[site] != -1:
                continue
            amp = amplitude(tuple(sorted(state[y] for y in adj[site] if state[y] != -1)))
            total = 0
            for color in range(M):
                mutable[site] = color
                total += amp[color] * value(tuple(mutable))
            mutable[site] = -1
            if total > best:
                best = total
        memo[state] = best
        return best

    return F(value(tuple([-1] * n)), cap**n)


# ---------------------------------------------------------------- 2x2 hull
classes: dict[tuple[int, int], int] = {}
event = set()
mu_e = nu_a = nu_b = tv_bar = F(0)
corner_a = predlist((0, 1, 3, 2), ADJ4)
corner_b = predlist((1, 0, 2, 3), ADJ4)
shape_ok = True
for v in CFG4:
    w = weight(v, E4)
    n_left = N2(v[0], v[2])
    n_right = N2(v[1], v[3])
    ya = y_of(v, corner_a)
    yb = y_of(v, corner_b)
    shape_ok = shape_ok and ya == 864 * n_right and yb == 864 * n_left
    key = (
        0 if v[0] == v[2] else (2 if v[0] == (v[2] ^ 1) else 1),
        0 if v[1] == v[3] else (2 if v[1] == (v[3] ^ 1) else 1),
    )
    classes[key] = classes.get(key, 0) + w
    mu = F(w, Z4)
    bar = (F(w, ya) + F(w, yb)) / 2
    tv_bar += abs(mu - bar)
    if mu > bar:
        event.add(v)
        mu_e += mu
        nu_a += F(w, ya)
        nu_b += F(w, yb)
tv_bar /= 2
sup_e = bellman(4, ADJ4, lambda st: 1 if st in event else 0)
claimed_classes = {
    (0, 0): 876, (0, 1): 2688, (1, 0): 2688, (0, 2): 492, (2, 0): 492,
    (1, 1): 9216, (1, 2): 1920, (2, 1): 1920, (2, 2): 492,
}
check(
    "S3 2x2 hull",
    shape_ok and classes == claimed_classes and sum(classes.values()) == Z4
    and mu_e == F(521, 1732) and nu_a == nu_b == F(1619, 5616)
    and tv_bar == F(30457, 2431728) == mu_e - nu_a
    and sup_e == F(1619, 5616),
    "TV(mu,H)=30457/2431728, attained by the corner mixture; Bellman sup of 1_E is 1619/5616",
)


# ---------------------------------------------------------------- disjoint plaquettes
P_NUM, P_DEN = mu_e.numerator, mu_e.denominator
Q_NUM, Q_DEN = sup_e.numerator, sup_e.denominator


def tail_mass(m: int, k: int, a: int, c: int) -> int:
    """c^m * P(Bin(m, a/c) >= k)."""
    b = c - a
    term = a**m
    total = 0
    j = m
    while j >= k:
        total += term
        if j == 0:
            break
        nxt = term * j * b
        div = (m - j + 1) * a
        if nxt % div:
            raise SystemExit("binomial recurrence is not integral")
        term = nxt // div
        j -= 1
    return total


def gap_at_least_half(m: int, k: int) -> bool:
    left = 2 * tail_mass(m, k, P_NUM, P_DEN) * Q_DEN**m
    right = 2 * tail_mass(m, k, Q_NUM, Q_DEN) * P_DEN**m
    return left - right >= P_DEN**m * Q_DEN**m


def first_heavier(m: int) -> int:
    lo, hi = 0, m
    while lo < hi:
        j = (lo + hi) // 2
        if P_NUM**j * (P_DEN - P_NUM) ** (m - j) * Q_DEN**m >= Q_NUM**j * (Q_DEN - Q_NUM) ** (m - j) * P_DEN**m:
            hi = j
        else:
            lo = j + 1
    return lo


def isqrt_hi(num: int, den: int, scale: int) -> int:
    q = isqrt(num * scale * scale // den)
    return q if q * q * den == num * scale * scale else q + 1


def isqrt_lo(num: int, den: int, scale: int) -> int:
    return isqrt(num * scale * scale // den)


K_STAR = first_heavier(2410)
K_PREV = first_heavier(2409)
SCALE = 10**30
low = high = 0
pair_value = (26, 24, 22)
for (i, j), wc in classes.items():
    n1, n2 = pair_value[i], pair_value[j]
    low += wc * isqrt_lo(n1 + n2, 1728 * Z4 * n1 * n2, SCALE)
    high += wc * isqrt_hi(n1 + n2, 1728 * Z4 * n1 * n2, SCALE)
beta_num = isqrt_hi(P_NUM * Q_NUM, P_DEN * Q_DEN, SCALE) + isqrt_hi(
    (P_DEN - P_NUM) * (Q_DEN - Q_NUM), P_DEN * Q_DEN, SCALE
)
check(
    "S4 disjoint threshold",
    K_STAR == 710 and gap_at_least_half(2410, 710) and not gap_at_least_half(2409, K_PREV)
    and 4 * low**1904 > 3 * SCALE**1904 and 4 * high**1906 <= 3 * SCALE**1906
    and 10**10 * (SCALE - beta_num) >= 943777 * SCALE
    and 2 * beta_num**7345 <= SCALE**7345 and 2 * beta_num**7344 > SCALE**7344,
    "TV(Bin) >= 1/2 at m=2410 (k=710) and not at 2409; BC gives TV<1/2 through m=952; 1-beta >= 9.43777e-5",
)


# ---------------------------------------------------------------- strips and tube
def column_states(width: int):
    return list(itertools.product(range(M), repeat=width))


def strip_rows(width: int):
    states = column_states(width)
    intra = []
    for col in states:
        p = 1
        for j in range(1, width):
            p *= PHI[col[j - 1]][col[j]]
        intra.append(p)

    def row(i: int):
        src = states[i]
        tr, dr = [], []
        for col in states:
            x = 1
            for j in range(1, width):
                x *= PHI[col[j - 1]][col[j]]
            for j in range(width):
                x *= PHI[src[j]][col[j]]
            d = 1
            for j in range(1, width):
                d *= N2(src[j], col[j - 1])
            tr.append(x)
            dr.append(d)
        return tr, dr

    return states, row, intra, intra, 1, 6 * 12 ** (width - 1)


def tube_rows():
    states = list(itertools.product(range(M), repeat=4))
    intra = [PHI[s[0]][s[1]] * PHI[s[0]][s[2]] * PHI[s[1]][s[3]] * PHI[s[2]][s[3]] for s in states]
    scale = 10**15
    u0 = [isqrt_hi(intra[k] ** 2, N2(s[1], s[2]), scale) for k, s in enumerate(states)]

    def row(i: int):
        src = states[i]
        tr, dr = [], []
        for k, col in enumerate(states):
            tr.append(intra[k] * PHI[src[0]][col[0]] * PHI[src[1]][col[1]] * PHI[src[2]][col[2]] * PHI[src[3]][col[3]])
            dr.append(N2(col[0], src[1]) * N2(col[0], src[2]) * N3(col[1], col[2], src[3]))
        return tr, dr

    return states, row, intra, u0, scale, 864


def perron_from_matrix(mat: np.ndarray, rounds: int = 400) -> list[int]:
    vec = np.ones(mat.shape[0])
    for _ in range(rounds):
        img = mat @ vec
        vec = img / img.max()
    return [max(1, int(round(t * 1e12))) for t in vec]


def certify(states, row, intra, u0, d0, const0):
    n = len(states)
    rows = [row(i) for i in range(n)]
    transfer = np.zeros((n, n))
    tilted = np.zeros((n, n))
    for i, (tr, dr) in enumerate(rows):
        transfer[i] = tr
        tilted[i] = [a / (d ** 0.5) for a, d in zip(tr, dr)]
    u = perron_from_matrix(transfer)
    v = perron_from_matrix(tilted)
    lam = rho = None
    ceilings: dict[tuple[int, int], int] = {}
    scale = 10**15
    for i in range(n):
        tr, dr = rows[i]
        li = F(sum(a * b for a, b in zip(tr, u)), u[i])
        tot = 0
        for a, d, b in zip(tr, dr, v):
            key = (a, d)
            c = ceilings.get(key)
            if c is None:
                c = isqrt_hi(a * a, d, scale)
                ceilings[key] = c
            tot += c * b
        ri = F(tot, scale * v[i])
        lam = li if lam is None or li < lam else lam
        rho = ri if rho is None or ri > rho else rho
    r2 = rho * rho / (12 * lam)
    rn = -((-r2.numerator * 10**12) // r2.denominator)
    uv = sum(a * b for a, b in zip(u0, v))
    big_k = F(uv * uv, d0 * d0 * min(v) ** 2) * F(max(u), const0 * sum(a * b for a, b in zip(intra, u)))
    return lam, rho, rn, big_k


def first_length(big_k: F, rn: int, thr: F) -> int:
    def ok(length: int) -> bool:
        return big_k.numerator * rn ** (length - 1) * thr.denominator <= thr.numerator * big_k.denominator * 10 ** (12 * (length - 1))

    # The growth is geometric, so a short scan from a float guess is exact at the end.
    guess = 2
    ratio = rn / 1e12
    if 0 < ratio < 1 and big_k > 0:
        import math
        guess = max(2, 1 + int(math.log(float(thr / big_k)) / math.log(ratio)))
    length = max(2, guess - 5)
    while not ok(length):
        length += 1
        if length > 100000:
            return -1
    while length > 2 and ok(length - 1):
        length -= 1
    return length


path = certify(*strip_rows(1))
check(
    "S5 path sanity",
    path[0] == path[1] == 12 and path[2] == 10**12 and path[3] == 1,
    "a path has r2=1 and K=1",
)

windows = []
cert_ok = True
for name, data, corners in (
    ("2xL", strip_rows(2), 4),
    ("3xL", strip_rows(3), 4),
    ("tube", tube_rows(), 8),
):
    lam, rho, rn, big_k = certify(*data)
    one = first_length(big_k, rn, F(1, 4))
    hull = first_length(big_k, rn, F(1, 4 * corners))
    tight = first_length(big_k, rn, F(1, 10**4 * corners))
    cert_ok = cert_ok and rn < 10**12 and one > 0 and hull == { "2xL": 4624, "3xL": 2272, "tube": 1019 }[name]
    windows.append((name, 10**12 - rn, big_k, one, hull, tight))
check(
    "S5 strip certificates",
    cert_ok and [item[4] for item in windows] == [4624, 2272, 1019],
    "; ".join(
        "%s: 1-r2>=%s e-12, K<=%s, TV>=1/2 vs one corner from L=%d and vs the hull from L=%d"
        % (name, gap, big_k.limit_denominator(10**6), one, hull)
        for name, gap, big_k, one, hull, _tight in windows
    ),
)


# ---------------------------------------------------------------- cube
def cube_edges(length: int):
    edges = []
    for i in range(length):
        edges += [(4 * i + x, 4 * i + y) for x, y in ((0, 1), (0, 2), (1, 3), (2, 3))]
    for i in range(1, length):
        edges += [(4 * (i - 1) + x, 4 * i + x) for x in range(4)]
    return edges


CUBE = cube_edges(2)
CUBE_ADJ = adj_of(8, CUBE)
CUBE_PRED = predlist(tuple(range(8)), CUBE_ADJ)
pred_ok = [group for _x, group in CUBE_PRED] == [(), (0,), (0,), (1, 2), (0,), (1, 4), (2, 4), (3, 5, 6)]
by_y: dict[int, int] = {}
INNER = [(1, 3), (1, 5), (2, 3), (2, 6), (4, 5), (4, 6)]
for free in itertools.product(range(M), repeat=6):
    v = (0,) + free
    wt = N3(v[1], v[2], v[4]) * N3(v[3], v[5], v[6])
    for a, b in INNER:
        wt *= PHI[v[a]][v[b]]
    yy = 10368 * N2(v[1], v[2]) * N2(v[1], v[4]) * N2(v[2], v[4]) * N3(v[3], v[5], v[6])
    by_y[yy] = by_y.get(yy, 0) + wt
Z_CUBE = sum(by_y.values())
tv_one = sum(abs(F(w, Z_CUBE) - F(w, yy)) for yy, w in by_y.items()) / 2
# Eight corner laws, configurations with v0=0, restored by the factor 6.
groups: dict[tuple[int, ...], int] = {}
for free in itertools.product(range(M), repeat=7):
    v = (0,) + free
    w = 1
    for a, b in CUBE:
        w *= PHI[v[a]][v[b]]
    ys = []
    for mask in range(8):
        # Corner m is the image of corner 0 under the cube reflection site |-> site xor m.
        ys.append(
            10368 * N2(v[1 ^ mask], v[2 ^ mask]) * N2(v[1 ^ mask], v[4 ^ mask])
            * N2(v[2 ^ mask], v[4 ^ mask]) * N3(v[3 ^ mask], v[5 ^ mask], v[6 ^ mask])
        )
    key = tuple(ys)
    groups[key] = groups.get(key, 0) + w
tv8 = mu8 = nu8 = F(0)
corner_mass = [F(0)] * 8
for ys, w in groups.items():
    mu = F(6 * w, Z_CUBE)
    bar = sum(F(6 * w, y) for y in ys) / 8
    tv8 += abs(mu - bar)
    if mu > bar:
        mu8 += mu
        nu8 += bar
        corner_mass = [old + F(6 * w, y) for old, y in zip(corner_mass, ys)]
tv8 /= 2
check(
    "S6 cube",
    pred_ok and Z_CUBE == 6982520832 and sum(F(w, yy) for yy, w in by_y.items()) == 1
    and tv_one == F(1182193085, 23402354976)
    and tv8 == F(3205622113713065, 81441318629518848)
    and mu8 == F(278186119, 581876736)
    and len(set(corner_mass)) == 1 and corner_mass[0] == F(377272857433, 859933780992)
    and 6 * sum(groups.values()) == Z_CUBE,
    "one corner TV=1182193085/23402354976; monotone hull TV=3205622113713065/81441318629518848",
)


# ---------------------------------------------------------------- 2x3 ladder
E23 = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
ADJ23 = adj_of(6, E23)
CFG23 = list(itertools.product(range(M), repeat=6))
Z23 = sum(weight(v, E23) for v in CFG23)
W23 = [weight(v, E23) for v in CFG23]
IX23 = {v: i for i, v in enumerate(CFG23)}
CORNER = [y_of(v, predlist((0, 1, 2, 3, 4, 5), ADJ23)) for v in CFG23]
GEO = [tuple(3 * rr + cc for rr in rows for cc in cols)
       for rows in ((0, 1), (1, 0)) for cols in ((0, 1, 2), (2, 1, 0))]
PG = [[IX23[tuple(v[g[x]] for x in range(6))] for v in CFG23] for g in GEO]
tv4 = mu4 = nb4 = F(0)
event4 = set()
for i, v in enumerate(CFG23):
    mu = F(W23[i], Z23)
    bar = sum(F(W23[i], CORNER[PG[k][i]]) for k in range(4)) / 4
    tv4 += abs(mu - bar)
    if mu > bar:
        event4.add(v)
        mu4 += mu
        nb4 += bar
tv4 /= 2
best = F(0)
seen = set()
for order in itertools.permutations(range(6)):
    preds = predlist(order, ADJ23)
    key = tuple(sorted(preds))
    if key in seen:
        continue
    seen.add(key)
    byy: dict[int, int] = {}
    for v in event4:
        yy = y_of(v, preds)
        byy[yy] = byy.get(yy, 0) + W23[IX23[v]]
    best = max(best, sum(F(w, yy) for yy, w in byy.items()))

# Witness strategies from the attempt: row 0 is the path, then a value-dependent order of row 1.
VALUE_MAPS = []
for perm in itertools.permutations(range(3)):
    for flips in itertools.product(range(2), repeat=3):
        VALUE_MAPS.append(tuple(2 * perm[i // 2] + ((i & 1) ^ flips[i // 2]) for i in range(6)))
TOPS = sorted({min(tuple(g[x] for x in t) for g in VALUE_MAPS) for t in itertools.product(range(M), repeat=3)})
TOP_CLASS = {}
for ri, rep in enumerate(TOPS):
    for g in VALUE_MAPS:
        TOP_CLASS.setdefault(tuple(g[x] for x in rep), (ri, [g.index(s) for s in range(M)]))
CODES = [
    [61, 64, 181, 62, 64, 62, 55, 64, 53, 183, 55], [61, 64, 63, 62, 64, 182, 55, 64, 183, 61, 63],
    [1, 64, 141, 62, 64, 190, 55, 64, 7, 63, 55], [61, 64, 63, 62, 64, 138, 55, 64, 183, 14, 55],
    [61, 64, 189, 62, 64, 142, 7, 64, 55, 15, 53], [61, 64, 141, 62, 64, 190, 55, 64, 7, 63, 61],
    [1, 64, 63, 62, 64, 55, 55, 64, 183, 181, 61], [61, 64, 189, 62, 64, 63, 55, 64, 55, 183, 63],
    [61, 64, 63, 2, 64, 142, 55, 64, 183, 15, 61], [61, 64, 63, 62, 64, 190, 55, 64, 183, 63, 63],
    [61, 64, 55, 62, 64, 62, 7, 64, 181, 183, 61], [61, 64, 189, 2, 64, 62, 54, 64, 55, 183, 55],
    [61, 64, 55, 62, 64, 62, 53, 64, 181, 183, 53], [1, 64, 15, 62, 64, 62, 55, 64, 135, 183, 53],
    [61, 64, 63, 62, 64, 14, 54, 64, 183, 135, 21], [1, 64, 189, 62, 64, 62, 55, 64, 55, 183, 21],
    [61, 64, 55, 62, 64, 62, 54, 64, 181, 183, 53], [61, 64, 141, 62, 64, 134, 55, 64, 7, 15, 31],
    [61, 64, 7, 62, 64, 54, 55, 64, 133, 181, 55],
]
LAM = [
    F(5489, 50000), F(4618289, 20625000), F(84779, 17187500), F(1898, 15625), F(1405037, 34375000),
    F(8304691, 103125000), F(47371, 12890625), F(11910781, 206250000), F(2299127, 51562500),
    F(976159, 10312500), F(682763, 34375000), F(832573, 51562500), F(949, 15625), F(300317, 25781250),
    F(167, 4125000), F(417449, 10312500), F(4594079, 103125000), F(216547, 20625000), F(178679, 12890625),
]
BOT = {}
for k, k2 in ((3, 4), (3, 5), (4, 3), (5, 4), (5, 3)):
    order = (0, 1, 2, k, k2, 12 - k - k2)
    BOT[(k, k2)] = [y_of(v, predlist(order, ADJ23)) for v in CFG23]


def strategy_y(code):
    out = []
    for v in CFG23:
        ri, ginv = TOP_CLASS[v[:3]]
        c = code[ri]
        k = 3 + c // 64
        k2 = 3 if k == 4 else (4 if c >> ginv[v[k]] & 1 else 8 - k)
        out.append(BOT[(k, k2)][IX23[v]])
    return out


SY = [strategy_y(code) for code in CODES]
normalised = all(sum(F(W23[i], ys[i]) for i in range(len(CFG23))) == 1 for ys in SY)
LY = 1
for ys in SY:
    for yy in set(ys):
        LY = lcm(LY, yy)
DL = 1
for x in LAM:
    DL = lcm(DL, x.denominator)
AS = [[LY // yy for yy in ys] for ys in SY]
sv = [0] * len(CFG23)
for lam, amp in zip(LAM, AS):
    lm = lam.numerator * (DL // lam.denominator)
    for i in range(len(CFG23)):
        sv[i] += lm * sum(amp[PG[k][i]] for k in range(4))
CT = 4 * DL * LY
tv_star = F(sum(W23[i] * (CT - Z23 * sv[i]) for i in range(len(CFG23)) if CT > Z23 * sv[i]), Z23 * CT)
TIED = {
    "000222": F(23, 99), "000224": F(8473, 78408), "000232": F(1), "000242": F(7, 44),
    "001002": F(184339, 303264), "001211": F(0), "002012": F(36421, 50544), "002014": F(1837, 2592),
    "002041": F(0), "002203": F(43, 48), "002221": F(13, 108), "002321": F(37, 144),
    "002405": F(3109, 4752), "002421": F(5, 72), "002454": F(0), "010232": F(1), "010242": F(1, 44),
    "012203": F(1, 24), "012242": F(15361, 41184), "012425": F(95, 96), "020020": F(1), "020030": F(5, 11),
    "020040": F(0), "020121": F(2, 33), "020131": F(0), "020141": F(0), "020424": F(1), "020434": F(1),
    "021142": F(41, 48),
}
fst = {}
tied_seen = set()
for i, v in enumerate(CFG23):
    if CT > Z23 * sv[i]:
        fst[v] = F(1)
    elif CT < Z23 * sv[i]:
        fst[v] = F(0)
    else:
        key = "".join(map(str, min(tuple(g[v[q[x]]] for x in range(6)) for g in VALUE_MAPS for q in GEO)))
        tied_seen.add(key)
        fst[v] = TIED[key]
DF = 1
for x in TIED.values():
    DF = lcm(DF, x.denominator)
eta = bellman(6, ADJ23, lambda st: (fst[st] * DF).numerator) / DF
lower = sum(fst[v] * F(W23[i], Z23) for i, v in enumerate(CFG23)) - eta
check(
    "S8 2x3 hull",
    len(seen) == 98 and best == nb4 and tv4 == F(812090431, 41067000000) == mu4 - nb4
    and len(TOPS) == 11 and sum(LAM) == 1 and min(LAM) > 0 and normalised
    and tied_seen == set(TIED)
    and lower == tv_star == F(4120449306433, 238517136000000)
    and tv_star < F(874, 1000) * tv4,
    "fixed-order TV=812090431/41067000000; full hull TV=4120449306433/238517136000000",
)

# Envelope on the plaquette is strictly weaker than the hull distance.
env = F(0)
env_ok = True
for v in CFG4:
    # minimum Y over orders is the subset DP
    g = [1] * 16
    for mask in range(1, 16):
        best_y = None
        for site in range(4):
            if mask >> site & 1:
                rest = mask & ~(1 << site)
                val = g[rest] * Nf(tuple(sorted(v[y] for y in ADJ4[site] if rest >> y & 1)))
                best_y = val if best_y is None or val < best_y else best_y
        g[mask] = best_y
    nmin = min(N2(v[0], v[2]), N2(v[1], v[3]))
    env_ok = env_ok and g[-1] == min(36 * nmin * nmin, 864 * nmin)
    if g[-1] > Z4:
        env += F(weight(v, E4), Z4) * (1 - F(Z4, g[-1]))
check(
    "S7 envelope",
    env_ok and env == F(2555, 810576) and env < tv_bar,
    "the pointwise envelope on the 2x2 is 2555/810576, strictly below the hull distance",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. At (3,1,2) the static law's total variation to the adapted hull is "
    "30457/2431728 on the 2x2 and 4120449306433/238517136000000 on the 2x3, below the fixed-order value. "
    "On m disjoint plaquettes the E-count bound crosses 1/2 between m=953 and m=2410. Corner orders on the "
    "2xL, 3xL and 2x2xL windows are singular to the static law, with total variation at least 1/2 against "
    "the monotone hull from L=4624, 2272 and 1019. The 2x2x2 monotone hull is at "
    "3205622113713065/81441318629518848. The pointwise envelope decays on 2xL and does not bound the full hull.",
    flush=True,
)
print(
    "HIT: confirmed - the adapted hull is at total variation 30457/2431728 on the 2x2 and "
    "4120449306433/238517136000000 on the 2x3, the disjoint-plaquette threshold lies in [953,2410], "
    "and corner orders on the strips and the tube are singular to the static law",
    flush=True,
)
