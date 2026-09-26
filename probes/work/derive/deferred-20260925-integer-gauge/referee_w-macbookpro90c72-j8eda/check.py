#!/usr/bin/env python3
"""Independent referee for deferred-20260925-integer-gauge a1.

The tensor stencil, the planar moves, and a connected-support search are
rebuilt here. The attempt's script is not imported.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from math import gcd

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


AXIS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(left, right, sign=1):
    return tuple(left[i] + sign * right[i] for i in range(3))


def pair(i, j):
    return (min(i, j), max(i, j))


def apply_stencil(slots):
    rows = {}
    for ((i, j), site), value in slots.items():
        if value == 0:
            continue
        if i == j:
            bumps = (((j, add(site, AXIS[j], -1)), 1), ((j, site), -1))
        else:
            bumps = ((j, site), 1), ((j, add(site, AXIS[i])), -1), ((i, site), 1), ((i, add(site, AXIS[j])), -1)
        for key, sign in bumps:
            rows[key] = rows.get(key, 0) + sign * value
    return {key: value for key, value in rows.items() if value}


def doubled(component, site):
    i, j = component
    even = tuple(2 * coordinate for coordinate in site)
    if i == j:
        return (even, i)
    return (add(add(even, AXIS[i]), AXIS[j]), -1)


def odd_axes(point):
    return [axis for axis in range(3) if point[axis] % 2]


def rows_touching(slot):
    point, label = slot
    axes = odd_axes(point)
    if not axes:
        return [add(point, AXIS[label]), add(point, AXIS[label], -1)]
    return [add(point, AXIS[axis], sign) for axis in axes for sign in (1, -1)]


def slots_on_row(row):
    axis = odd_axes(row)[0]
    found = []
    for direction in range(3):
        for sign in (1, -1):
            slot = (add(row, AXIS[direction], sign), axis if direction == axis else -1)
            found.append((slot, sign))
    return found


def order_key(slot):
    return (slot[0], slot[1])


def laurent_add(*polynomials):
    total = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            total[exponent] = total.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in total.items() if coefficient}


def shift(polynomial, displacement):
    return {add(exponent, displacement): coefficient for exponent, coefficient in polynomial.items()}


def factor_u(polynomial, axis):
    return laurent_add(polynomial, {exponent: -coefficient for exponent, coefficient in shift(polynomial, AXIS[axis]).items()})


def to_charges(slots):
    charges = {}
    for ((i, j), site), value in slots.items():
        if value == 0:
            continue
        exponent = site if i != j else add(site, AXIS[i], -1)
        component = charges.setdefault((i, j), {})
        component[exponent] = component.get(exponent, 0) + value
    return charges


def from_charges(charges):
    slots = {}
    for (i, j), polynomial in charges.items():
        for exponent, coefficient in polynomial.items():
            if coefficient == 0:
                continue
            site = exponent if i != j else add(exponent, AXIS[i])
            slots[((i, j), site)] = slots.get(((i, j), site), 0) + coefficient
    return {key: value for key, value in slots.items() if value}


def charge_rows(charges):
    rows = {}
    for row in range(3):
        terms = [factor_u(charges.get(pair(column, row), {}), column) for column in range(3)]
        rows[row] = laurent_add(*terms)
    return rows


samples_ok = True
for trial in range(12):
    slots = {}
    for index in range(8):
        component = pair((trial + index) % 3, (trial + 2 * index) % 3)
        site = ((index - 2) % 3 - 1, (trial - index) % 3, (index + trial) % 2)
        slots[(component, site)] = slots.get((component, site), 0) + ((index % 5) - 2)
    direct = apply_stencil(slots)
    generated = charge_rows(to_charges(slots))
    via = {(row, exponent): coefficient for row, polynomial in generated.items() for exponent, coefficient in polynomial.items() if coefficient}
    samples_ok = samples_ok and direct == via
check("stencil", samples_ok, "the lattice stencil agrees with div Q after Q_jj = t_j^{-1} P_jj")


def airy(first, second, seed):
    return {
        (first, first): factor_u(factor_u(seed, second), second),
        (second, second): factor_u(factor_u(seed, first), first),
        pair(first, second): {exponent: -coefficient for exponent, coefficient in factor_u(factor_u(seed, first), second).items()},
    }


def planar(first, second, center=(0, 0, 0)):
    slots = {
        ((first, first), center): -2,
        ((second, second), center): -2,
        ((first, first), add(center, AXIS[second])): 1,
        ((first, first), add(center, AXIS[second], -1)): 1,
        ((second, second), add(center, AXIS[first])): 1,
        ((second, second), add(center, AXIS[first], -1)): 1,
    }
    face = pair(first, second)
    corners = (
        (center, -1),
        (add(center, AXIS[first], -1), 1),
        (add(center, AXIS[second], -1), 1),
        (add(add(center, AXIS[first], -1), AXIS[second], -1), -1),
    )
    for site, value in corners:
        slots[(face, site)] = value
    return slots


planar_ok = True
for first, second in ((0, 1), (0, 2), (1, 2)):
    move = planar(first, second)
    seed = {(add(add((0, 0, 0), AXIS[first], -1), AXIS[second], -1)): 1}
    planar_ok = planar_ok and from_charges(airy(first, second, seed)) == move
    planar_ok = planar_ok and apply_stencil(move) == {}
    planar_ok = planar_ok and len(move) == 10 and sum(abs(value) for value in move.values()) == 12
check("planar", planar_ok, "each named displacement is an Airy monomial, has support 10 and L1 12, and is a move")

u1, u2, u3, phi, amplitude, partner, diagonal = sp.symbols("u1 u2 u3 phi a b Q11")
symbols = [u1, u2, u3]


def symbolic_rows(charges):
    return [sp.expand(sum(symbols[column] * charges.get(pair(column, row), 0) for column in range(3))) for row in range(3)]


airy_rows = symbolic_rows({(0, 0): u2 ** 2 * phi, (1, 1): u1 ** 2 * phi, (0, 1): -u1 * u2 * phi})
face_only = symbolic_rows({(0, 1): u3 * amplitude, (0, 2): -u2 * amplitude, (1, 2): -u1 * amplitude})
one_diagonal = symbolic_rows({(0, 0): -2 * u2 * u3 * partner, (0, 1): u1 * u3 * partner, (0, 2): u1 * u2 * partner, (1, 2): -u1 ** 2 * partner})
forced = symbolic_rows({(0, 0): diagonal, (0, 1): u3 * partner, (0, 2): u2 * partner, (1, 2): -u1 * partner})
exponent_m, exponent_n, coefficient_a, coefficient_b = sp.symbols("m n A B")
difference = sp.Matrix([[1, 1], [exponent_m, exponent_n]]).det()
check(
    "divisibility",
    airy_rows == [0, 0, 0]
    and face_only[0] == 0
    and face_only[1] == 0
    and sp.expand(face_only[2] + 2 * u1 * u2 * amplitude) == 0
    and one_diagonal == [0, 0, 0]
    and forced[1] == 0
    and forced[2] == 0
    and sp.expand(forced[0] - u1 * diagonal - 2 * u2 * u3 * partner) == 0
    and sp.expand(difference - (exponent_n - exponent_m)) == 0
    and min(abs(left) + abs(right) + abs(left + right) for left in range(-4, 5) for right in range(-4, 5) if left and right and left + right) == 4,
    "Airy and the one-diagonal family are kernel elements; a double root forces equal exponents; three nonzero integers summing to 0 have L1 at least 4",
)


def search(anchor, budget):
    anchor_key = order_key(anchor)
    leaves = []
    nodes = 0

    def classify(support, excluded):
        best = None
        for slot in support:
            for row in rows_touching(slot):
                present = 0
                open_slots = []
                for candidate, _sign in slots_on_row(row):
                    if candidate in support:
                        present += 1
                    elif candidate in excluded or order_key(candidate) < anchor_key:
                        continue
                    else:
                        open_slots.append(candidate)
                if not open_slots:
                    if present == 1:
                        return True, None
                    continue
                priority = (0 if present == 1 else 1, len(open_slots))
                if best is None or priority < best[0]:
                    best = (priority, row, open_slots, present)
        return False, best

    def walk(support, excluded):
        nonlocal nodes
        nodes += 1
        dead, choice = classify(support, excluded)
        if dead:
            return
        if choice is None:
            leaves.append(frozenset(support))
            return
        _priority, _row, open_slots, present = choice
        room = budget - len(support)
        for mask in range(1 << len(open_slots)):
            chosen = [open_slots[index] for index in range(len(open_slots)) if mask >> index & 1]
            if len(chosen) > room or present + len(chosen) == 1:
                continue
            chosen_set = set(chosen)
            walk(support | frozenset(chosen), excluded | frozenset(slot for slot in open_slots if slot not in chosen_set))

    walk(frozenset([anchor]), frozenset())
    return leaves, nodes


anchors = (
    ((0, 0, 0), 0),
    ((0, 0, 0), 1),
    ((0, 0, 0), 2),
    ((1, 1, 0), -1),
    ((1, 0, 1), -1),
    ((0, 1, 1), -1),
)
print("searching connected supports up to size 12", flush=True)
all_leaves = []
node_count = 0
for anchor in anchors:
    found, used = search(anchor, 12)
    all_leaves.extend(found)
    node_count += used
    print(f"  anchor {anchor}: {used} nodes, {len(found)} leaves", flush=True)
print(f"  total {node_count} nodes, {len(all_leaves)} leaves", flush=True)


def incidence(support):
    columns = sorted(support, key=order_key)
    index = {slot: position for position, slot in enumerate(columns)}
    rows = sorted({row for slot in support for row in rows_touching(slot)})
    matrix = []
    for row in rows:
        entries = [0] * len(columns)
        for slot, sign in slots_on_row(row):
            if slot in index:
                entries[index[slot]] = sign
        matrix.append(entries)
    return columns, matrix


def rational_kernel(matrix, width):
    reduced = [[Fraction(entry) for entry in row] for row in matrix]
    pivots = []
    rank = 0
    for column in range(width):
        pivot = next((row for row in range(rank, len(reduced)) if reduced[row][column] != 0), None)
        if pivot is None:
            continue
        reduced[rank], reduced[pivot] = reduced[pivot], reduced[rank]
        scale = reduced[rank][column]
        reduced[rank] = [entry / scale for entry in reduced[rank]]
        for row in range(len(reduced)):
            if row != rank and reduced[row][column] != 0:
                factor = reduced[row][column]
                reduced[row] = [entry - factor * pivot_entry for entry, pivot_entry in zip(reduced[row], reduced[rank])]
        pivots.append(column)
        rank += 1
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [Fraction(0)] * width
        vector[free_column] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def canonical(assignment):
    origin = min(assignment, key=order_key)
    point = origin[0]
    shift = tuple(-2 * ((point[axis] - (point[axis] % 2)) // 2) for axis in range(3))
    return frozenset(((add(slot[0], shift), slot[1]), coefficient) for slot, coefficient in assignment.items())


planar_shapes = set()
for first, second in ((0, 1), (0, 2), (1, 2)):
    for sign in (1, -1):
        move = planar(first, second)
        planar_shapes.add(canonical({doubled(component, site): sign * value for (component, site), value in move.items()}))

deficient = []
for support in all_leaves:
    columns, matrix = incidence(support)
    basis = rational_kernel(matrix, len(columns))
    if basis:
        deficient.append((support, columns, basis))
def primitive(assignment):
    denominator = 1
    for value in assignment.values():
        denominator = denominator * value.denominator // gcd(denominator, value.denominator)
    integers = {slot: int(value * denominator) for slot, value in assignment.items()}
    common = 0
    for value in integers.values():
        common = gcd(common, abs(value))
    return {slot: value // common for slot, value in integers.items()}


identified = True
for support, columns, basis in deficient:
    for vector in basis:
        assignment = primitive({columns[index]: value for index, value in enumerate(vector) if value})
        if canonical(assignment) not in planar_shapes:
            identified = False
check(
    "search",
    node_count == 1954858
    and len(all_leaves) == 103
    and len(deficient) == 3
    and all(len(support) == 10 for support, _columns, _basis in deficient)
    and identified,
    f"{node_count} nodes, {len(all_leaves)} leaves, {len(deficient)} rational kernels, all planar of size 10",
)


def monotone_amplitude():
    move = planar(0, 1)
    ordered = sorted(move)
    target = [move[slot] for slot in ordered]

    def energy(heights):
        slots = {ordered[index]: height * (1 if target[index] > 0 else -1) for index, height in enumerate(heights) if height}
        rows = apply_stencil(slots)
        return sum(value * value for value in rows.values())

    box = list(itertools.product(*[range(abs(value) + 1) for value in target]))
    values = {}
    for state in sorted(box, key=sum):
        if sum(state) == 0:
            values[state] = Fraction(1)
            continue
        total = Fraction(0)
        for index, height in enumerate(state):
            if height:
                previous = state[:index] + (height - 1,) + state[index + 1 :]
                total += values[previous]
        if sum(state) == 12:
            values[state] = total
        else:
            values[state] = total / energy(state)
    endpoint = tuple(abs(value) for value in target)
    zeros = [state for state in box if energy(state) == 0]
    return len(box), zeros, endpoint, values[endpoint]


count, zeros, endpoint, amplitude = monotone_amplitude()
check(
    "amplitude",
    count == 2304
    and sorted(zeros) == [tuple(0 for _ in range(10)), endpoint]
    and amplitude == Fraction(111150053, 31850496),
    f"the monotone order-12 weight is {amplitude}",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. Every connected support of size at most 12 that can be a move is one of three planar "
    "kernels, each of support 10. The named displacements have L1 12 and lie in the kernel. The generating-function "
    "stencil, the Airy identities, and the order-12 weight 111150053/31850496 were recomputed. The Z_N table and the "
    "unit-entry gap from 14 to 20 were not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - every nonzero finite-support integer move found by the box-free search through support 12 is a "
    "planar move, with minimum support 10 and minimum L1 12",
    flush=True,
)
