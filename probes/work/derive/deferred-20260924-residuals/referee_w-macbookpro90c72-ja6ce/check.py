#!/usr/bin/env python3
"""Independent referee for deferred-20260924-residuals a1.

The bright-from-dark block is rebuilt from the rotor-cube words. The
attempt's script is not imported. The off-lattice branch and the
300-start search were not rerun.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from itertools import combinations, product

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


OUTSIDE = (0, 3, 5, 6)
INSIDE = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in OUTSIDE for b in INSIDE if a ^ b in (1, 2, 4))
TREE = (1, 2, 3, 4, 6, 9, 11)
CHORDS = (0, 5, 7, 8, 10)

words = []
for occupied in combinations(range(8), 6):
    for minus in occupied:
        words.append(tuple((-1 if i == minus else 1) if i in occupied else 0 for i in range(8)))


def grade(word):
    return sum(word[site] == 0 for site in OUTSIDE)


low = [word for word in words if grade(word) == 0]
middle = [word for word in words if grade(word) == 1]
upper = [word for word in words if grade(word) == 2]
dark = [word for word in middle if not any(word[a] == word[b] == 0 for a, b in EDGES)]
bright = [word for word in middle if word not in dark]
dark_index = {word: n for n, word in enumerate(dark)}
bright_index = {word: n for n, word in enumerate(bright)}


def hop(word, inward):
    found = []
    for edge_index, (a, b) in enumerate(EDGES):
        legal = word[a] == 0 and word[b] != 0 if inward else word[a] != 0 and word[b] == 0
        if not legal:
            continue
        charge = word[b] if inward else word[a]
        moved = list(word)
        moved[a], moved[b] = (charge, 0) if inward else (0, charge)
        winding = [0] * 5
        if edge_index in CHORDS:
            winding[CHORDS.index(edge_index)] = charge if inward else -charge
        found.append((tuple(moved), tuple(winding)))
    return found


def commutator(word):
    total = defaultdict(int)
    for first_inward, sign in ((True, 1), (False, -1)):
        for middle_word, first_winding in hop(word, first_inward):
            for final_word, second_winding in hop(middle_word, not first_inward):
                winding = tuple(left + right for left, right in zip(first_winding, second_winding))
                total[(final_word, winding)] += sign
    return {key: value for key, value in total.items() if value}


columns = [commutator(word) for word in dark]
entries = []
lands_in_bright = True
for column, image in enumerate(columns):
    for (word, winding), value in image.items():
        if word not in bright_index:
            lands_in_bright = False
            continue
        entries.append((bright_index[word], column, winding, value))

incidence = sp.zeros(8, 12)
for index, (a, b) in enumerate(EDGES):
    incidence[a, index] = 1
    incidence[b, index] = -1
tree_block = incidence.extract(range(7), TREE)
flat = sp.zeros(72, 24)
for row, column, _winding, value in entries:
    flat[row, column] += value
uniform = sp.ones(24, 1)
check(
    "S invariants",
    [len(low), len(middle), len(upper), len(dark), len(bright)] == [36, 96, 36, 24, 72]
    and lands_in_bright
    and abs(tree_block.det()) == 1
    and flat.rank() == 23
    and flat * uniform == sp.zeros(72, 1),
    "grades 36/96/36, 24 dark and 72 bright words, flat rank 23, uniform kernel",
)

background = sp.Matrix([int(site in OUTSIDE) for site in range(8)])
references = {}
for word in words:
    solved = tree_block.inv() * (sp.Matrix(word) - background)[:7, :]
    cycle = sp.zeros(12, 1)
    for slot, edge in enumerate(TREE):
        cycle[edge] = solved[slot]
    references[word] = cycle


def flow(state, center=None):
    out = defaultdict(int)
    for (word, cycle), amplitude in state.items():
        for edge_index, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            if not word[a] or word[b]:
                continue
            moved, updated = list(word), list(cycle)
            moved[a], moved[b] = 0, word[a]
            updated[edge_index] -= word[a]
            out[(tuple(moved), tuple(updated))] += amplitude
    return dict(out)


def birth(state, sign):
    out = defaultdict(int)
    for (word, cycle), amplitude in state.items():
        if word[0] or word[1]:
            continue
        for sigma in ([sign] if sign else (-1, 1)):
            moved, updated = list(word), list(cycle)
            moved[0], moved[1] = sigma, -sigma
            updated[0] += sigma
            out[(tuple(moved), tuple(updated))] += amplitude
    return dict(out)


vacuum = {(tuple(int(site in OUTSIDE) for site in range(8)), (0,) * 12): 1}
inputs = []
for sign in (1, -1, 0):
    born = birth(flow(vacuum), sign)
    returned = {key: -value for key, value in flow(born, 0).items()}
    norm = sum(value * value for value in born.values())
    items = []
    for (word, cycle), amplitude in returned.items():
        winding = tuple(int((sp.Matrix(cycle) - references[word])[chord]) for chord in CHORDS)
        items.append((dark_index[word], winding, amplitude))
    inputs.append((norm, items))


def character(signs, winding):
    value = 1
    for sign, exponent in zip(signs, winding):
        if sign == -1 and exponent % 2:
            value = -value
    return value


def block_at(signs):
    matrix = sp.zeros(72, 24)
    for row, column, winding, value in entries:
        matrix[row, column] += value * character(signs, winding)
    return matrix


def slope_at(signs, axis):
    matrix = sp.zeros(72, 24)
    for row, column, winding, value in entries:
        matrix[row, column] += winding[axis] * value * character(signs, winding)
    return matrix


expected = {
    (1, 1, 1, 1, 1): 1,
    (1, 1, 1, -1, -1): 1,
    (1, -1, -1, 1, -1): 2,
    (1, -1, -1, -1, 1): 1,
    (-1, 1, -1, 1, 1): 1,
    (-1, 1, -1, -1, -1): 2,
    (-1, -1, 1, 1, -1): 4,
    (-1, -1, 1, -1, 1): 2,
}
found = {}
nondegenerate = True
overlaps_ok = True
for signs in product((1, -1), repeat=5):
    matrix = block_at(signs)
    rank = matrix.rank()
    if rank == 24:
        continue
    kernel = sp.Matrix.hstack(*matrix.nullspace())
    dimension = kernel.shape[1]
    found[signs] = dimension
    pencil = matrix.row_join(sp.Matrix.hstack(*[slope_at(signs, axis) * kernel for axis in range(5)]))
    nondegenerate = nondegenerate and pencil.rank() == rank + 5 * dimension
    projector = kernel * (kernel.T * kernel).inv() * kernel.T
    weights = []
    for norm, items in inputs:
        vector = sp.zeros(24, 1)
        for column, winding, amplitude in items:
            vector[column] += amplitude * character(signs, winding)
        weights.append(sp.together((vector.T * projector * vector)[0] / norm))
    overlaps_ok = overlaps_ok and weights == [sp.Rational(dimension, 12), sp.Rational(dimension, 12), sp.Rational(dimension, 6)]
check(
    "H phases",
    found == expected and sum(found.values()) == 14 and nondegenerate and overlaps_ok,
    "exactly the eight listed phases are dark, dims 1,1,2,1,1,2,4,2; pencils are full rank; overlaps are 1/12, 1/12, 1/6 per dimension",
)

variables = sp.symbols("z1:6")
rows = defaultdict(dict)
for row, column, winding, value in entries:
    monomial = value
    for variable, exponent in zip(variables, winding):
        monomial *= variable ** exponent
    rows[row][column] = sp.expand(rows[row].get(column, 0) + monomial)


def unit_monomial(expression):
    terms = sp.Add.make_args(sp.expand(expression))
    if len(terms) != 1 or terms[0] == 0:
        return False
    shifted = sp.expand(terms[0] * sp.Mul(*[variable ** 8 for variable in variables]))
    return abs(sp.Poly(shifted, *variables).coeffs()[0]) == 1


remaining = {row: dict(entries_by_column) for row, entries_by_column in rows.items()}
active = set(range(24))
pivots = 0
while True:
    choice = None
    for row, entries_by_column in remaining.items():
        for column, expression in entries_by_column.items():
            if column in active and unit_monomial(expression):
                weight = sum(column in other for other in remaining.values())
                candidate = (weight, row, column)
                if choice is None or candidate < choice:
                    choice = candidate
    if choice is None:
        break
    _, pivot_row, pivot_column = choice
    pivot = remaining.pop(pivot_row)
    pivot_value = pivot[pivot_column]
    for row, entries_by_column in list(remaining.items()):
        if pivot_column not in entries_by_column:
            continue
        factor = sp.expand(entries_by_column[pivot_column] / pivot_value)
        for column, expression in pivot.items():
            updated = sp.expand(entries_by_column.get(column, 0) - factor * expression)
            if updated == 0:
                entries_by_column.pop(column, None)
            else:
                entries_by_column[column] = updated
        entries_by_column.pop(pivot_column, None)
        if not entries_by_column:
            remaining.pop(row)
    active.discard(pivot_column)
    pivots += 1

columns_left = sorted(active)
residual = {row: {column: expression for column, expression in entries_by_column.items() if column in active} for row, entries_by_column in remaining.items()}
residual = {row: entries_by_column for row, entries_by_column in residual.items() if entries_by_column}
avoiding = [row for row, entries_by_column in residual.items() if columns_left[-1] not in entries_by_column]
block = sp.Matrix([[residual[row].get(column, 0) for column in columns_left[:3]] for row in avoiding])
minor_target = -(variables[1] ** 3 - variables[3] ** 3 * variables[4]) * (variables[1] ** 3 * variables[4] - variables[3] ** 3) * (variables[0] * variables[2] + 1)
minor_match = False
for chosen in combinations(range(4), 3):
    numerator = sp.fraction(sp.together(block.extract(list(chosen), [0, 1, 2]).det(method="berkowitz")))[0]
    minor_match = minor_match or sp.expand(numerator - minor_target) == 0 or sp.expand(numerator + minor_target) == 0
check(
    "G reduction",
    pivots == 20 and len(columns_left) == 4 and len(residual) == 52 and len(avoiding) == 4 and minor_match,
    "20 unit pivots leave a 52 by 4 residual, and one 3 by 3 minor is the stated product",
)

last = columns_left[-1]
last_entries = [residual[row][last] for row in residual if last in residual[row]]
factored = [sp.factor(sp.fraction(sp.together(expression))[0]) for expression in last_entries]


def contains(expression):
    return any(sp.expand(item - expression) == 0 or sp.expand(item + expression) == 0 for item in factored)


specialised = {variables[1]: -1, variables[2]: 1, variables[3]: 1, variables[4]: -1}
gcd_value = None
for expression in last_entries:
    reduced = sp.expand(sp.fraction(sp.together(expression))[0].subs(specialised))
    if reduced != 0:
        gcd_value = reduced if gcd_value is None else sp.gcd(gcd_value, reduced)
check(
    "G last column",
    contains(variables[4] + 1)
    and contains(variables[1] + variables[3])
    and contains(variables[2] + variables[3] * variables[4])
    and contains(variables[2] + variables[4])
    and sp.expand(gcd_value - (variables[0] + 1)) == 0,
    "the last-column branch forces z = (-1,-1,1,1,-1)",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. On the rotor cube the bright-from-dark block has flat rank 23. Exactly eight of the "
    "32 half-period phases are dark, with kernel dimensions 1, 1, 2, 1, 1, 2, 4, 2. Each pencil has full column rank, "
    "and the three inputs overlap every kernel by 1/12, 1/12, 1/6 per dimension. Twenty unit pivots leave a 52 by 4 "
    "residual whose last-column branch is only (-1,-1,1,1,-1). The exponent 5/2 is exact only if no dark phase lies "
    "off that lattice; that exclusion, and the 300-start search, were not proved.",
    flush=True,
)
print(
    "HIT: confirmed - exactly eight half-period phases are dark, with dimensions 1, 1, 2, 1, 1, 2, 4, 2, "
    "all nondegenerate and overlapped by 1/12, 1/12, 1/6 per dimension; the last-column branch of the 52 by 4 "
    "residual is only (-1,-1,1,1,-1), while the exponent 5/2 stays conditional on no off-lattice dark phase",
    flush=True,
)
