#!/usr/bin/env python3
"""Independent referee for relabelling-blindness in the cube kinetic family, a2.

The Euler conditions and the mode pencil are recomputed. The attempt's
script is not imported.
"""
from __future__ import annotations

import itertools
import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


time = sp.symbols("t")
momentum = sp.Matrix(sp.symbols("p1 p2 p3", real=True))
coupling, diagonal, mixed, shear, rotation = sp.symbols("K M1 M2 M3 N", real=True)
shifts = sp.symbols("c0:4", real=True)
transverse = sp.Matrix(sp.symbols("b1 b2 b3", real=True))
pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
off_diagonal = ((0, 1), (0, 2), (1, 2))
strain_functions = {pair: sp.Function(f"h{pair[0]}{pair[1]}")(time) for pair in pairs}
rotation_functions = {pair: sp.Function(f"w{pair[0]}{pair[1]}")(time) for pair in off_diagonal}
multiplier = sp.Function("u")(time)
clock = sp.Function("zeta")(time)


def symmetric(values):
    matrix = sp.zeros(3)
    for (row, column), value in values.items():
        matrix[row, column] = value
        matrix[column, row] = value
    return matrix


def antisymmetric(values):
    matrix = sp.zeros(3)
    for (row, column), value in values.items():
        matrix[row, column] = value
        matrix[column, row] = -value
    return matrix


strain = symmetric(strain_functions)
spin = antisymmetric(rotation_functions)


def scalar_one(matrix):
    return momentum.dot(momentum) * matrix.trace() - (momentum.T * matrix * momentum)[0]


def scalar_two(matrix):
    square = momentum.dot(momentum)
    image = matrix * momentum
    return (
        -square / 4 * (matrix * matrix).trace()
        + image.dot(image) / 2
        - (momentum.T * matrix * momentum)[0] * matrix.trace() / 2
        + square / 4 * matrix.trace() ** 2
    )


def kinetic(rate):
    return (
        diagonal * sum(rate[index, index] ** 2 for index in range(3))
        + mixed * sum(rate[left, left] * rate[right, right] for left, right in off_diagonal)
        + shear * sum(rate[left, right] ** 2 for left, right in off_diagonal)
    )


def lagrangian(matrix, factor, rotation_field):
    spin_rate = rotation_field.diff(time)
    return kinetic(matrix.diff(time)) + rotation * sum(spin_rate[left, right] ** 2 for left, right in off_diagonal) + coupling * (factor * scalar_one(matrix) + scalar_two(matrix))


fields = list(strain_functions.values()) + list(rotation_functions.values()) + [multiplier, clock]


def euler(expression, field):
    derivative = sp.diff(expression, field)
    for order in range(1, 5):
        derivative += (-1) ** order * sp.diff(sp.diff(expression, sp.diff(field, time, order)), time, order)
    return sp.expand(derivative)


def coefficients(change, extras=()):
    derivatives = [sp.diff(field, time, order) for field in fields for order in range(8, -1, -1)]
    names = {derivative: sp.Symbol(f"D{index}") for index, derivative in enumerate(derivatives)}
    equations = set()
    for field in fields:
        substituted = euler(change, field).subs(names)
        if substituted == 0:
            continue
        for coefficient in sp.Poly(substituted, *names.values()).coeffs():
            for term in sp.Poly(sp.expand(coefficient), *momentum, *extras).coeffs():
                equations.add(term)
    return list(equations)


base = lagrangian(strain, multiplier, spin)
shift = sum(shifts[order] * sp.diff(clock, time, order) for order in range(4))
gradient = momentum * clock / 2
gradient_change = sp.expand(lagrangian(strain + momentum * gradient.T + gradient * momentum.T, multiplier + shift, spin) - base)
gradient_equations = coefficients(gradient_change)
gradient_solution = sp.solve(gradient_equations, [diagonal, mixed, shear, rotation, *shifts], dict=True)
witness = sp.expand(gradient_change.subs({diagonal: 0, mixed: coupling * shifts[2], shear: -coupling * shifts[2], shifts[0]: 0, shifts[1]: 0, shifts[3]: 0}))
boundary = coupling * shifts[2] * clock.diff(time) * scalar_one(strain)
check(
    "gradient",
    gradient_solution == [{diagonal: 0, mixed: coupling * shifts[2], shear: -coupling * shifts[2], shifts[0]: 0, shifts[1]: 0, shifts[3]: 0}]
    and sp.simplify(witness - boundary.diff(time)) == 0,
    "the gradient relabelling is a symmetry exactly for (0, c, -c) with u shifted by (c/K) zeta''",
)

axis = momentum.cross(transverse) * clock
transverse_change = sp.expand(
    lagrangian(strain + momentum * axis.T + axis * momentum.T, multiplier + shift, spin + (momentum * axis.T - axis * momentum.T) / 2) - base
)
transverse_solution = sp.solve(coefficients(transverse_change, tuple(transverse)), [mixed, shear, rotation, *shifts], dict=True)
unchanged = sp.expand(
    lagrangian(strain + momentum * axis.T + axis * momentum.T, multiplier, spin + (momentum * axis.T - axis * momentum.T) / 2).subs({mixed: 2 * diagonal, shear: 0, rotation: 0})
    - base.subs({mixed: 2 * diagonal, shear: 0, rotation: 0})
)
check(
    "transverse",
    transverse_solution == [{mixed: 2 * diagonal, shear: 0, rotation: 0, shifts[0]: 0, shifts[1]: 0, shifts[2]: 0, shifts[3]: 0}] and unchanged == 0,
    "a transverse relabelling is a symmetry exactly for (M, 2M, 0) with N = 0 and no multiplier shift",
)
both = sp.solve(gradient_equations + coefficients(transverse_change, tuple(transverse)), [diagonal, mixed, shear, rotation, *shifts], dict=True)
check(
    "both",
    both == [{diagonal: 0, mixed: 0, shear: 0, rotation: 0, shifts[0]: 0, shifts[1]: 0, shifts[2]: 0, shifts[3]: 0}],
    "the two demands together leave only the zero kinetic term",
)

rate = sp.Matrix(3, 3, sp.symbols("v0:9"))
components = list(rate)
quadratic = sp.Matrix(9, 9, lambda row, column: sp.Symbol(f"q{min(row, column)}{max(row, column)}"))
symbols = sorted(quadratic.free_symbols, key=str)
quarter = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
third = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
inversion = -sp.eye(3)
invariance = []
for group in (quarter, third, inversion):
    image = list(group * rate * group.T)
    action = sp.Matrix(9, 9, lambda row, column: sp.diff(image[row], components[column]))
    invariance.extend(action.T * quadratic * action - quadratic)
reduced = quadratic.subs(sp.solve(invariance, symbols, dict=True)[0])
free = sorted(reduced.free_symbols, key=str)
symmetric_part = (rate + rate.T) / 2
antisymmetric_part = (rate - rate.T) / 2
basis = [
    sum(rate[index, index] ** 2 for index in range(3)),
    sum(rate[left, left] * rate[right, right] for left, right in off_diagonal),
    sum(symmetric_part[left, right] ** 2 for left, right in off_diagonal),
    sum(antisymmetric_part[left, right] ** 2 for left, right in off_diagonal),
]
form = sp.expand((sp.Matrix([components]) * reduced * sp.Matrix(components))[0])
weights = sp.symbols("k0:4")
matched = sp.solve(sp.Poly(sp.expand(form - sum(weight * term for weight, term in zip(weights, basis))), *components).coeffs(), list(weights) + free, dict=True)
check(
    "cube forms",
    len(free) == 4 and len(matched) == 1 and len({matched[0][weight] for weight in weights}) == 4,
    "the cube leaves exactly four quadratic numbers in the full rate",
)
generator = antisymmetric({pair: sp.Symbol(f"o{pair[0]}{pair[1]}") for pair in off_diagonal})
numbers = sp.symbols("n1:5")
invariant = sum(number * term for number, term in zip(numbers, basis))
difference = sp.expand(invariant.subs({components[index]: (rate + generator)[index] for index in range(9)}) - invariant)
blind = sp.solve(sp.Poly(difference, *components, *generator.free_symbols).coeffs(), list(numbers), dict=True)
check("rotation blindness", blind == [{numbers[3]: 0}], "a coin rotation changes the quadratic form unless the antisymmetric coefficient vanishes")
check(
    "which demand rotates",
    rotation not in gradient_solution[0] and transverse_solution[0][rotation] == 0,
    "the gradient demand leaves the rotation coefficient free and the transverse demand sets it to zero",
)

frequency = sp.symbols("X")
member = {diagonal: 0, mixed: -2, shear: 2}
coordinate = list(strain_functions.values()) + [multiplier] + list(rotation_functions.values())
rates = [value.diff(time) for value in coordinate]
kinetic_form = sp.expand(kinetic(strain.diff(time)).subs(member) + rotation * sum(spin.diff(time)[left, right] ** 2 for left, right in off_diagonal))
potential = sp.expand(coupling * (multiplier * scalar_one(strain) + scalar_two(strain)))
mass = sp.Matrix(10, 10, lambda row, column: sp.diff(kinetic_form, rates[row], rates[column]))
stiffness = sp.Matrix(10, 10, lambda row, column: sp.diff(potential, coordinate[row], coordinate[column]))
mode_ok = True
for sample in ((1, 2, 2), (sp.Rational(2, 5), sp.Rational(1, 3), -sp.Rational(3, 7))):
    replacement = {momentum[index]: sample[index] for index in range(3)}
    replacement.update({coupling: 1})
    pencil = (frequency * mass + stiffness).subs(replacement)
    block = pencil[:7, :7]
    rank = block.rank()
    divisor = 0
    for row_set in itertools.combinations(range(7), rank):
        for column_set in itertools.combinations(range(7), rank):
            divisor = sp.gcd(divisor, block.extract(list(row_set), list(column_set)).det())
    roots = sp.roots(sp.Poly(sp.factor(divisor), frequency))
    momentum_square = sum(value ** 2 for value in sample)
    mode_ok = mode_ok and rank == 6 and pencil[7:, :7].is_zero_matrix and pencil[:7, 7:].is_zero_matrix
    mode_ok = mode_ok and roots.get(sp.Rational(momentum_square, 4)) == 2 and set(roots) <= {0, sp.Rational(momentum_square, 4)}
    mode_ok = mode_ok and sp.simplify(sp.factor(pencil[7:, 7:].det()) - 8 * rotation ** 3 * frequency ** 3) == 0
probe = (frequency * mass + stiffness).subs({momentum[0]: 1, momentum[1]: 2, momentum[2]: 2, coupling: 1, rotation: 1})
gauge = sp.Matrix([1, 4, 4, 2, 2, 4, 2 * frequency, 0, 0, 0])
kernel = probe.subs(frequency, sp.Rational(9, 4)).nullspace()
span = sp.Matrix.hstack(*kernel)
parameters = sp.Matrix(sp.symbols(f"y0:{len(kernel)}"))
combination = span * parameters
reconstructed = sp.Matrix(3, 3, lambda row, column: combination[pairs.index((min(row, column), max(row, column)))])
constraints = list(reconstructed * sp.Matrix([1, 2, 2])) + [reconstructed.trace(), combination[6], combination[7], combination[8], combination[9]]
constraint_rank = sp.Matrix([[sp.diff(constraint, parameter) for parameter in parameters] for constraint in constraints]).rank()
check(
    "modes",
    mode_ok and len(kernel) == 3 and len(kernel) - constraint_rank == 2 and sp.Matrix.hstack(span, gauge.subs(frequency, sp.Rational(9, 4))).rank() == len(kernel) and sp.simplify(probe * gauge) == sp.zeros(10, 1),
    "the travelling root is p^2/4 with multiplicity two, and at that root the kernel is the transverse-traceless pair plus the gradient gauge",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. In the cube kinetic family a gradient relabelling in time is a symmetry exactly for "
    "(M1, M2, M3) = (0, c, -c), with the multiplier shifted by (c/K) zeta''. A transverse relabelling is a symmetry "
    "exactly for (M, 2M, 0) with the antisymmetric rate coefficient zero and no shift. Both demands leave only zero. "
    "The cube allows exactly four quadratic numbers in the full rate, and rotation blindness removes the antisymmetric one. "
    "The gradient survivor has one travelling transverse-traceless pair at X = p^2/4. Orders beyond the second strain were not classified.",
    flush=True,
)
print(
    "HIT: confirmed - gradient relabelling fixes (0, c, -c) with shift (c/K) zeta'', transverse relabelling fixes "
    "(M, 2M, 0) with no shift, and only the zero term satisfies both",
    flush=True,
)
