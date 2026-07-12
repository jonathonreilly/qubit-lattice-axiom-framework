#!/usr/bin/env python3
"""Exact checks for the rhalf-block-14 formation-weight classification.

The runner verifies algebra and arithmetic only.  The note-owned SOCMLC
licensing criterion is a declared classification boundary, not something a
symbolic runner can prove.
"""

from __future__ import annotations

import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool) -> None:
    """Print one numbered result and update the exact scorecard."""
    global PASS, FAIL
    number = PASS + FAIL + 1
    if bool(condition):
        PASS += 1
        print(f"[PASS] {number:02d} {label}")
    else:
        FAIL += 1
        print(f"[FAIL] {number:02d} {label}")


def normalized(weights: list[sp.Expr] | tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    total = sp.Add(*weights)
    return tuple(sp.cancel(weight / total) for weight in weights)


def k_action(matrix: sp.Matrix, swap: sp.Matrix) -> sp.Matrix:
    """K/CPT on the character basis: conjugate, then swap the doublet."""
    return sp.simplify(swap * matrix.conjugate() * swap)


def ratio_r(singlet_weight: sp.Expr) -> sp.Expr:
    return sp.cancel((1 - singlet_weight) / (2 * singlet_weight))


def rational_text(value: sp.Expr) -> str:
    value = sp.cancel(value)
    if value.is_Rational:
        numerator, denominator = value.as_numer_denom()
        return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"
    return str(value)


# Supplied carrier, two-cell quotient, and K/CPT swap.
identity = sp.eye(3)
zero = sp.zeros(3)
p_s = sp.diag(1, 0, 0)
p_d = sp.diag(0, 1, 1)
swap = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
internal_separator = sp.diag(0, 1, -1)

check(
    "the singlet/doublet projectors are orthogonal and resolve the carrier",
    p_s**2 == p_s
    and p_d**2 == p_d
    and p_s * p_d == zero
    and p_s + p_d == identity,
)

cell_dimensions = (p_s.rank(), p_d.rank())
check(
    "carrier ranks and traces give the structural dimension vector (1,2)",
    cell_dimensions == (1, 2)
    and tuple(sp.trace(projector) for projector in (p_s, p_d)) == (1, 2),
)

check(
    "K fixes both quotient cells but sends the internal doublet separator to its negative",
    k_action(p_s, swap) == p_s
    and k_action(p_d, swap) == p_d
    and k_action(internal_separator, swap) == -internal_separator,
)

x_s, x_d = sp.symbols("x_s x_d", real=True)
registrable_readout = x_s * p_s + x_d * p_d
reg_basis_matrix = sp.Matrix.hstack(
    sp.Matrix(p_s).reshape(9, 1), sp.Matrix(p_d).reshape(9, 1)
)
check(
    "orbit-constant scalar readouts are diag(x_s,x_d,x_d), a two-dimensional C+C algebra",
    registrable_readout == sp.diag(x_s, x_d, x_d)
    and k_action(registrable_readout, swap) == registrable_readout
    and reg_basis_matrix.rank() == 2,
)

a, b = sp.symbols("a b")
separator_is_registrable = sp.solve(
    list(a * p_s + b * p_d - internal_separator), (a, b), dict=True
)
check(
    "C+M2 is a strict enlargement: its supported doublet separator is not in C+C",
    p_d * internal_separator * p_d == internal_separator
    and separator_is_registrable == [],
)

# Candidates 1--4, with all masses derived from the supplied objects.
carrier_assignment = normalized([sp.Integer(rank) for rank in cell_dimensions])
w_carrier = carrier_assignment[0]
check(
    "candidate 1: normalized carrier trace gives w=1/3",
    carrier_assignment == (sp.Rational(1, 3), sp.Rational(2, 3)),
)

quotient_atoms = (p_s, p_d)
atom_assignment = normalized([sp.Integer(1) for _ in quotient_atoms])
w_atoms = atom_assignment[0]
check(
    "candidate 2: counting the two minimal central projections gives w=1/2",
    atom_assignment == (sp.Rational(1, 2), sp.Rational(1, 2)),
)

# Left multiplication by the two primitive idempotents on the basis (P_s,P_d).
left_p_s = sp.diag(1, 0)
left_p_d = sp.diag(0, 1)
licensed_regular_ranks = (left_p_s.rank(), left_p_d.rank())
regular_assignment = normalized(
    [sp.Integer(rank) for rank in licensed_regular_ranks]
)
w_regular = regular_assignment[0]
check(
    "candidate 3: the regular/HS ranks of licensed C+C are (1,1), hence w=1/2",
    licensed_regular_ranks == (1, 1) and regular_assignment == atom_assignment,
)

hypothetical_block_sizes = cell_dimensions
hypothetical_regular_ranks = tuple(size**2 for size in hypothetical_block_sizes)
hypothetical_block_assignment = normalized(
    [sp.Integer(rank) for rank in hypothetical_regular_ranks]
)
w_hypothetical_block = hypothetical_block_assignment[0]
check(
    "candidate 3-alt: the unlicensed C+M2 regular ranks (1,4) would give w=1/5",
    hypothetical_regular_ranks == (1, 4)
    and hypothetical_block_assignment == (sp.Rational(1, 5), sp.Rational(4, 5)),
)


def permutation_orbit_sizes(permutation: tuple[int, ...]) -> tuple[int, ...]:
    unseen = set(range(len(permutation)))
    sizes: list[int] = []
    while unseen:
        start = min(unseen)
        orbit: set[int] = set()
        current = start
        while current not in orbit:
            orbit.add(current)
            current = permutation[current]
        unseen -= orbit
        sizes.append(len(orbit))
    return tuple(sizes)


orbit_sizes = permutation_orbit_sizes((0, 2, 1))
orbit_assignment = normalized([sp.Integer(size) for size in orbit_sizes])
w_orbit = orbit_assignment[0]
check(
    "candidate 4: K-orbit sizes are (1,2), reproducing carrier trace w=1/3",
    orbit_sizes == cell_dimensions and orbit_assignment == carrier_assignment,
)

licensed_weights = frozenset((w_carrier, w_atoms, w_regular, w_orbit))
expected_weights = frozenset((sp.Rational(1, 3), sp.Rational(1, 2)))
check(
    "T1: deduplication gives exactly {1/3,1/2}, with 1/5 absent",
    licensed_weights == expected_weights and w_hypothetical_block not in licensed_weights,
)

check(
    "the exact fork map sends w=1/3 to r=1 and w=1/2 to r=1/2",
    ratio_r(w_carrier) == 1 and ratio_r(w_atoms) == sp.Rational(1, 2),
)

# T2: exact K-even density-operator witnesses for both assignments.
rho_dimension = identity / 3
rho_dimension_weights = (
    sp.trace(rho_dimension * p_s),
    sp.trace(rho_dimension * p_d),
)
check(
    "T2 control: rho=I/3 is positive, K-even, unit trace, and realizes (1/3,2/3)",
    sp.trace(rho_dimension) == 1
    and all(entry >= 0 for entry in rho_dimension.diagonal())
    and k_action(rho_dimension, swap) == rho_dimension
    and rho_dimension_weights == carrier_assignment,
)

rho_cell = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4))
rho_cell_weights = (sp.trace(rho_cell * p_s), sp.trace(rho_cell * p_d))
check(
    "T2 fork: diag(1/2,1/4,1/4) is positive, K-even, unit trace, and realizes (1/2,1/2)",
    sp.trace(rho_cell) == 1
    and all(entry >= 0 for entry in rho_cell.diagonal())
    and k_action(rho_cell, swap) == rho_cell
    and rho_cell_weights == atom_assignment,
)

# Sweep guards: arbitrary exponents and the symmetry-allowed continuum.
alpha = sp.symbols("alpha", real=True)
w_alpha = sp.cancel(1 / (1 + sp.Integer(2) ** alpha))
check(
    "the external exponent family is nonconstant and yields 1/2, 1/3, 1/5 at alpha=0,1,2",
    w_alpha.subs(alpha, 0) == sp.Rational(1, 2)
    and w_alpha.subs(alpha, 1) == sp.Rational(1, 3)
    and w_alpha.subs(alpha, 2) == sp.Rational(1, 5)
    and sp.diff(w_alpha, alpha) != 0,
)

t = sp.symbols("t", real=True)
rho_family = sp.diag(t, (1 - t) / 2, (1 - t) / 2)
family_weights = (sp.trace(rho_family * p_s), sp.trace(rho_family * p_d))
check(
    "symmetry alone leaves the full K-even family diag(t,(1-t)/2,(1-t)/2)",
    sp.trace(rho_family) == 1
    and k_action(rho_family, swap) == rho_family
    and family_weights == (t, 1 - t),
)

# T4: exact dependence on changed supplied invariants.
hypothetical_13_dimensions = (sp.Integer(1), sp.Integer(3))
hypothetical_13_trace = normalized(hypothetical_13_dimensions)
hypothetical_13_atoms = normalized((sp.Integer(1), sp.Integer(1)))
hypothetical_13_set = frozenset(
    (hypothetical_13_trace[0], hypothetical_13_atoms[0])
)
check(
    "T4 two-cell check: dimensions/orbits (1,3) change the set to {1/4,1/2}",
    hypothetical_13_trace == (sp.Rational(1, 4), sp.Rational(3, 4))
    and hypothetical_13_set
    == frozenset((sp.Rational(1, 4), sp.Rational(1, 2))),
)

three_singletons = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
three_assignments = (
    normalized(three_singletons),  # carrier trace
    normalized(three_singletons),  # orbit count
    normalized(three_singletons),  # quotient-atom count
    normalized(tuple(size**2 for size in three_singletons)),  # regular/HS
)
check(
    "T4 three-cell check: three identical singletons collapse all constructions to uniform thirds",
    frozenset(three_assignments)
    == frozenset(((sp.Rational(1, 3),) * 3,)),
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")

ordered_verdict = sorted(licensed_weights, key=sp.default_sort_key)
verdict_text = "{" + ", ".join(rational_text(value) for value in ordered_verdict) + "}"
print(f"VERDICT: W_expr = {verdict_text}.")
print(
    "CANDIDATE-3 ALGEBRA: A_reg=C+C because scalar readouts are constant on "
    "the K-doublet; C+M2 contains forbidden internal-doublet data, so 1/5 is excluded."
)
print("T1: SOCMLC gives a finite exact two-weight set.")
print("T2: both exact fork endpoints are lawful and neither is selected.")
print("T3: conditionally, the continuum dial becomes a finite selection problem; this runner selects nothing.")
print("T4: changing the supplied menu invariants changes or collapses the set.")
print(f"CHECKS: PASS={PASS} FAIL={FAIL}.")
print(
    "PROPOSED CLAIM_SCOPE: conditional canonical-measure classification on "
    "the supplied C3 carrier and its two-cell orbit-constant quotient only."
)
print(
    "UNCERTAINTIES: SOCMLC completeness is contestable; the orbit clause is "
    "bridge-carried; a separately supplied block algebra or formation operator would enlarge the set."
)

sys.exit(0 if FAIL == 0 else 1)
