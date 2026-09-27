#!/usr/bin/env python3
"""Independent check of moving jammed clusters, attempt a3.

Does not import the author's script. Breadth-first counts are rebuilt through
L = 5 at two moves and L = 4 at three moves. Larger boxes and the faceted
shapes are not.
"""
from collections import deque
from itertools import product

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def factorial(value):
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def two_move_value(length):
    return 18 * length**4 + 33 * length**2 - 24 * length


def outward_choices(length):
    counts = {1: 0, 2: 0, 3: 0}
    for site in product(range(length), repeat=3):
        exposed = sum(coordinate in (0, length - 1) for coordinate in site)
        if exposed:
            counts[exposed] += 1
    return counts


def distance_to_outside(site, length):
    return min(min(coordinate + 1, length - coordinate) for coordinate in site)


def enumerate_arrangements(length, depth):
    start = frozenset(product(range(length), repeat=3))
    box = set(start)
    seen = {start: 0}
    queue = deque([start])
    steps = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    by_depth = {0: 1}
    by_outside = {0: {0: 1}}
    vacated = {0: set()}
    while queue:
        state = queue.popleft()
        age = seen[state]
        if age == depth:
            continue
        for site in state:
            for step in steps:
                neighbor = (site[0] + step[0], site[1] + step[1], site[2] + step[2])
                if neighbor in state:
                    continue
                frozen = frozenset((state - {site}) | {neighbor})
                if frozen in seen:
                    continue
                seen[frozen] = age + 1
                by_depth[age + 1] = by_depth.get(age + 1, 0) + 1
                outside = sum(point not in box for point in frozen)
                bucket = by_outside.setdefault(age + 1, {})
                bucket[outside] = bucket.get(outside, 0) + 1
                vacated.setdefault(age + 1, set()).update(box - frozen)
                queue.append(frozen)
    return by_depth, by_outside, vacated


sample = outward_choices(5)
check(
    "surface census",
    sample == {1: 6 * 9, 2: 36, 3: 8} and sum(kind * sample[kind] for kind in sample) == 6 * 25,
    "an L=5 box has 6(L-2)^2 face records, 12(L-2) edge records and 8 corners, totalling 6L^2 outward moves",
)

side = sp.symbols("L", integer=True, positive=True)
mark = sp.symbols("x")
surface = 6 * side**2
two_records = sp.expand(surface * (surface - 1) / 2 - 12 * side)
one_record = sp.expand(36 * side**2 - 12 * side)
stated = 18 * side**4 + 33 * side**2 - 24 * side
face = 6 * (side - 2) ** 2
edge = 12 * (side - 2)
generating = (1 + mark) ** face * (1 + 2 * mark) ** edge * (1 + 3 * mark) ** 8
series_pair = sp.expand(generating.series(mark, 0, 3).coeff(mark, 2))
leading_ok = sp.expand(series_pair - two_records) == 0 and sp.expand(two_records + one_record - stated) == 0
for moves in range(1, 6):
    coefficient = sp.expand(generating.series(mark, 0, moves + 1).coeff(mark, moves))
    polynomial = sp.Poly(sp.expand(coefficient * factorial(moves)), side)
    leading_ok &= polynomial.degree() == 2 * moves
    leading_ok &= polynomial.coeff_monomial(side ** (2 * moves - 1)) == 0
    leading_ok &= polynomial.coeff_monomial(side ** (2 * moves)) == 6**moves
check(
    "leading count",
    leading_ok,
    "C(6L^2, 2) - 12L plus 36L^2 - 12L equals 18L^4 + 33L^2 - 24L; "
    "the T-move surface count is (6L^2)^T/T! with no L^{2T-1} term, for T = 1..5",
)

enumerated = {}
for length, depth in ((2, 3), (3, 3), (4, 3), (5, 2)):
    enumerated[length] = enumerate_arrangements(length, depth)
    print(f"enumerated L={length} depth={depth} counts={enumerated[length][0]}", flush=True)

census_ok = True
layer_ok = True
for length in (2, 3, 4, 5):
    by_depth, by_outside, vacated = enumerated[length]
    census_ok &= by_depth[1] == 6 * length * length
    census_ok &= by_depth[2] == two_move_value(length)
    census_ok &= by_outside[2].get(1, 0) == 36 * length * length - 12 * length
    census_ok &= by_outside[2].get(2, 0) == binomial(6 * length * length, 2) - 12 * length
    reached = set()
    for age, sites in vacated.items():
        reached |= sites
        expected = {site for site in product(range(length), repeat=3) if distance_to_outside(site, length) <= age}
        layer_ok &= reached == expected

three_table = {2: (4184, 1512), 3: (38394, 22948), 4: (189128, 138384)}
three_ok = True
for length, (total, triple) in three_table.items():
    by_depth, by_outside, _ = enumerated[length]
    three_ok &= by_depth.get(3) == total and by_outside.get(3, {}).get(3, 0) == triple

check(
    "breadth first",
    census_ok and layer_ok and three_ok,
    "for L = 2..5, N_1 = 6L^2 and N_2 = 18L^4 + 33L^2 - 24L; "
    "sites vacated within t moves are those at distance <= t from the outside; "
    "three-move counts are 4184, 38394, 189128 for L = 2, 3, 4",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL a full L^3 box of records has 6L^2 one-move arrangements. "
        "Arrangements first reached at two moves number 18L^4 + 33L^2 - 24L for L = 2..5, "
        "split into C(6L^2, 2) - 12L with two displaced records and 36L^2 - 12L with one. "
        "A record at distance d from the outside is first vacated at move d. "
        "At three moves the counts are 4184, 38394 and 189128 for L = 2, 3, 4, "
        "of which 1512, 22948 and 138384 have three displaced records. "
        "The surface generating function gives (6L^2)^T/T! with no L^{2T-1} term for T = 1..5. "
        "L = 6..10 and the faceted shapes were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - after two moves the box has 18L^4 + 33L^2 - 24L new arrangements for L = 2..5, "
        "and the three-move counts on L = 2, 3, 4 are 4184, 38394 and 189128.",
        flush=True,
    )
