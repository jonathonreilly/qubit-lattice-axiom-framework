#!/usr/bin/env python3
"""Referee for the record-gas chessboard threshold, a2.

Author w-macbookpro9927a-jfc7a (claude-opus-5-5). Own polycube census and certificate.
Mayer-Vietoris is the attempt's import for walls larger than the ones counted here.
The content weight W on random graphs was not rebuilt; the g* inequalities use the
stated worst-case factors m and Lambda.
"""
import itertools
import random
from fractions import Fraction as Fr

fails = []
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def canon(cells):
    origin = min(cells)
    return frozenset(sub(cell, origin) for cell in cells)


def polycubes(limit):
    found = {1: {frozenset({(0, 0, 0)})}}
    for size in range(1, limit):
        nxt = set()
        for poly in found[size]:
            adjacent = set()
            for cell in poly:
                for step in NB:
                    neighbour = add(cell, step)
                    if neighbour not in poly:
                        adjacent.add(neighbour)
            for neighbour in adjacent:
                nxt.add(canon(poly | {neighbour}))
        found[size + 1] = nxt
    return found


def plaquettes(cells):
    faces = []
    for cell in cells:
        for axis in range(3):
            for sign in (1, -1):
                step = [0, 0, 0]
                step[axis] = sign
                step = tuple(step)
                if add(cell, step) not in cells:
                    corner = cell if sign > 0 else add(cell, step)
                    faces.append((corner, axis))
    return faces


def vertices(face):
    corner, axis = face
    others = [i for i in range(3) if i != axis]
    out = []
    for signs in itertools.product((-1, 1), repeat=2):
        point = [2 * value for value in corner]
        point[axis] += 1
        point[others[0]] += signs[0]
        point[others[1]] += signs[1]
        out.append(tuple(point))
    return out


def edges(face):
    verts = vertices(face)
    return {frozenset((left, right)) for left, right in itertools.combinations(verts, 2)
            if sum(abs(a - b) for a, b in zip(left, right)) == 2}


def connected(parts):
    if not parts:
        return True
    seen = {0}
    stack = [0]
    while stack:
        current = stack.pop()
        for other in range(len(parts)):
            if other not in seen and parts[current] & parts[other]:
                seen.add(other)
                stack.append(other)
    return len(seen) == len(parts)


def geometry():
    cubes = polycubes(7)
    fixed = [len(cubes[n]) for n in range(1, 8)]
    counts = {}
    broken_vertex = broken_edge = broken_ray = 0
    for size in range(1, 7):
        for poly in cubes[size]:
            for origin in poly:
                placed = frozenset(sub(cell, origin) for cell in poly)
                faces = plaquettes(placed)
                counts[len(faces)] = counts.get(len(faces), 0) + 1
                broken_vertex += not connected([set(vertices(face)) for face in faces])
                broken_edge += not connected([edges(face) for face in faces])
                reach = 0
                while (reach + 1, 0, 0) in placed:
                    reach += 1
                broken_ray += not (4 * (reach + 1) <= len(faces))
    surfaces = []
    for poly in cubes[7]:
        bonds = sum(1 for cell in poly for axis in range(3) if add(cell, tuple(1 if i == axis else 0 for i in range(3))) in poly)
        surfaces.append(6 * 7 - 2 * bonds)
    centre = ((0, 0, 0), 0)
    window = [((i, j, k), axis) for i in range(-2, 3) for j in range(-2, 3) for k in range(-2, 3) for axis in range(3)]
    by_vertex = sum(1 for face in window if face != centre and set(vertices(face)) & set(vertices(centre)))
    by_edge = sum(1 for face in window if face != centre and edges(face) & edges(centre))
    wanted = {6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}
    small = {k: v for k, v in counts.items() if k <= 22}
    ok = (
        fixed == [1, 3, 15, 86, 534, 3481, 23502]
        and small == wanted
        and broken_vertex == 0
        and broken_ray == 0
        and min(surfaces) == 24
        and by_vertex == 32
        and by_edge == 12
    )
    report(
        "geometry",
        ok,
        f"fixed polycubes {fixed}; boundary counts {small}; vertex neighbours {by_vertex}, edge neighbours {by_edge}; "
        f"edge-disconnected walls among <=6 cells: {broken_edge}; 7-cell walls at least {min(surfaces)}",
    )
    return wanted


def binomial(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def tree_count(degree, k):
    if k == 1:
        return 1
    return degree * binomial((degree - 1) * k, k - 2) // (k - 1)


def certificate(counts):
    x0 = Fr(3, 250)
    upper = Fr(31, 1000)
    degree = 32
    growth = Fr(31 ** 31, 30 ** 30)
    seed = x0 * (1 + upper) ** 31 <= upper
    ratio = all(tree_count(degree, k + 1) <= growth * tree_count(degree, k) for k in range(1, 12))
    below = x0 < Fr(30 ** 30, 31 ** 31)
    denominator = 1 - x0 * 31 * (1 + upper) ** 30
    derivative = (1 + upper) ** 32 + x0 * 32 * (1 + upper) ** 31 * ((1 + upper) ** 31 / denominator)
    tail = x0 / 4 * derivative - sum(Fr(k, 4) * tree_count(degree, k) * x0 ** k for k in range(1, 24))
    total = sum(counts[k] * x0 ** k for k in counts) + tail
    bare = Fr(9, 62500) ** 3 == x0 ** 6
    triples = {
        (3, 1, 2): Fr(1, 10 ** 5),
        (5, 2, 4): Fr(18, 10 ** 6),
        (12, 1, 2): Fr(19, 10 ** 8),
        (9, 8, 8): Fr(97, 10 ** 6),
    }
    content = True
    for (p, q, r), g in triples.items():
        weights = [Fr(6 * p, p + q + 4 * r), Fr(6 * q, p + q + 4 * r), Fr(6 * r, p + q + 4 * r)]
        big, small = max(weights), min(weights)
        content &= g ** 3 * big ** 6 * (big / small) ** 5 <= x0 ** 6
    report(
        "certificate",
        seed and ratio and below and denominator > 0 and total < Fr(1, 2) and bare and content and abs(float(total) - 0.0896) < 5e-5,
        f"Peierls sum at x=3/250 is {float(total):.4f}; content-less g* = 9/62500; the four content bounds satisfy g^3 Lambda^6 (Lambda/m)^5 <= (3/250)^6",
    )
    return total


def rational_above(value, root):
    guess = Fr(float(value) ** (1.0 / root)).limit_denominator(10 ** 9)
    while guess ** root < value:
        guess *= Fr(1000001, 1000000)
    return guess


def rational_below(value, root):
    guess = Fr(float(value) ** (1.0 / root)).limit_denominator(10 ** 9)
    while guess ** root > value:
        guess *= Fr(999999, 1000000)
    return guess


def half(counts):
    x0 = Fr(3, 250)
    rows = [((3, 1, 2), Fr(15, 10 ** 8)), ((5, 2, 4), Fr(34, 10 ** 8)), ((12, 1, 2), Fr(16, 10 ** 11)),
            ((9, 8, 8), Fr(69, 10 ** 7)), (None, Fr(5, 10 ** 6))]
    ok = True
    degree = 32
    growth = Fr(31 ** 31, 30 ** 30)
    for triple, g in rows:
        if triple:
            p, q, r = triple
            weights = [Fr(6 * p, p + q + 4 * r), Fr(6 * q, p + q + 4 * r), Fr(6 * r, p + q + 4 * r)]
            big, small = max(weights), min(weights)
        else:
            big = small = Fr(1)
        high = rational_above(Fr(11, 10) ** 2 / small ** 5, 2)
        low = rational_below(Fr(9, 10) ** 2 / big ** 5, 2)
        span = max(high, 1 / low)
        target = g ** 3 * big ** 6 * (big / small) ** 5 * span
        ceiling = rational_above(target, 6)
        qq = growth * ceiling
        tail = tree_count(degree, 24) * ceiling ** 24 / 4 * (Fr(24) / (1 - qq) + qq / (1 - qq) ** 2)
        defect = sum(counts[k] * ceiling ** k for k in counts if k >= 10) + tail
        cube = g ** 3
        occupied = cube * high * small ** 5 / (1 + cube * high * small ** 5)
        vacant_high = cube / high + defect
        vacant_low = cube / (cube + low)
        occupied_high = cube * low * big ** 5 + defect
        ok &= occupied > vacant_high and vacant_low > occupied_high and ceiling <= x0 and g * big <= 1 and qq < 1
    report(
        "half",
        ok,
        "at the published half-filling g*, each framed box is above half filling at H+ and below it at H-, inside the Peierls window",
    )


def ising_and_shift():
    side = 4
    sites = {(i, j, k) for i in range(side) for j in range(side) for k in range(side)}
    frame = {add(site, step) for site in sites for step in NB} - sites

    def occupied(config, site):
        if site in sites:
            return config[site]
        return 1 if sum(site) % 2 == 0 else 0

    bonds = []
    seen = set()
    for site in sites:
        for step in NB:
            other = add(site, step)
            if other in sites or other in frame:
                key = tuple(sorted((site, other)))
                if key not in seen:
                    seen.add(key)
                    bonds.append((site, other))
    rng = random.Random(11)
    identity = True
    for _ in range(20):
        config = {site: rng.randint(0, 1) for site in sites}
        both = sum(1 for left, right in bonds if occupied(config, left) and occupied(config, right))
        number = sum(config.values())
        frame_ends = sum(occupied(config, right) for left, right in bonds for right in (left, right) if right not in sites)
        unlike = sum(1 for left, right in bonds if (occupied(config, left) == (1 if sum(left) % 2 == 0 else 0))
                     != (occupied(config, right) == (1 if sum(right) % 2 == 0 else 0)))
        identity &= 2 * both - 6 * number - frame_ends == unlike - len(bonds)
    shifts_ok = 0
    blobs = [
        {(1, 1, 1)},
        {(1, 1, 1), (2, 1, 1)},
        {(1, 1, 1), (2, 1, 1), (1, 2, 1)},
        {(1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)},
    ]
    for blob in blobs:
        config = {site: (1 if sum(site) % 2 == 0 else 0) for site in sites}
        for site in blob:
            config[site] = 0 if sum(site) % 2 == 0 else 1
        boundary = [(site, add(site, step)) for site in blob for step in NB if add(site, step) not in blob]
        before = sum(1 for left, right in bonds if (occupied(config, left) == (1 if sum(left) % 2 == 0 else 0))
                     != (occupied(config, right) == (1 if sum(right) % 2 == 0 else 0)))
        for step in NB:
            moved = {add(site, step) for site in blob}
            if any(site not in sites and site not in frame for site in moved):
                continue
            back = blob - moved
            nxt = dict(config)
            for site in moved:
                if site in sites:
                    nxt[site] = occupied(config, sub(site, step))
            for site in back:
                nxt[site] = 1 if sum(site) % 2 == 0 else 0
            after = sum(1 for left, right in bonds if (occupied(nxt, left) == (1 if sum(left) % 2 == 0 else 0))
                        != (occupied(nxt, right) == (1 if sum(right) % 2 == 0 else 0)))
            shifts_ok += before - after == len(boundary)
    report(
        "translation",
        identity and shifts_ok >= 8,
        f"on a framed 4^3 box the bond identity holds for 20 configurations, and {shifts_ok} explicit shifts drop the unlike count by the wall size",
    )


def main():
    counts = geometry()
    certificate(counts)
    half(counts)
    ising_and_shift()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - fixed polycubes through 7 cells and the walls through 22 plaquettes match the certificate. "
        "At x=3/250 the Peierls sum is below 1/2, so the content-less gas is ordered for g <= 9/62500 at zeta = g^-3. "
        "The four content bounds and the half-filling bounds satisfy the same window. "
        "Explicit shifts remove exactly the wall."
    )
    print(
        "SUMMARY: confirmed the polycube census, the Peierls sum, the g* arithmetic, the half-filling window, "
        "and explicit translations. Mayer-Vietoris for larger walls is the attempt's import. "
        "Random content-weight graphs were not rebuilt."
    )


if __name__ == "__main__":
    main()
