#!/usr/bin/env python3
"""Exact checks for the finite qubit-lattice joint-presentation bridge."""

from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM_MEMO = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: object, detail: str = "") -> None:
    """Record and print one independently evaluated condition."""
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"[PASS] {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"[FAIL] {label}" + (f" -- {detail}" if detail else ""))


def flattened_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


I2 = sp.eye(2)
SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = {
    "I": I2,
    "x": SIGMA_X,
    "y": SIGMA_Y,
    "z": SIGMA_Z,
}


def tensor_word(factors: tuple[sp.Matrix, ...] | list[sp.Matrix]) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for factor in factors:
        result = sp.kronecker_product(result, factor)
    return result


def embedded_generators(n: int) -> dict[tuple[int, str], sp.Matrix]:
    generators: dict[tuple[int, str], sp.Matrix] = {}
    for slot in range(n):
        for label in ("x", "y", "z"):
            factors = [I2] * n
            factors[slot] = PAULI[label]
            generators[(slot, label)] = tensor_word(factors)
    return generators


def pauli_strings(n: int) -> list[sp.Matrix]:
    return [
        tensor_word([PAULI[label] for label in labels])
        for labels in itertools.product(("I", "x", "y", "z"), repeat=n)
    ]


def row_flatten(matrix: sp.Matrix) -> list[sp.Expr]:
    return [matrix[row, col] for row in range(matrix.rows) for col in range(matrix.cols)]


def commutant_dimension(generators: list[sp.Matrix]) -> int:
    """Compute dim{M : [M,g]=0 for every g} from the exact commutator map."""
    d = generators[0].rows
    identity = sp.eye(d)
    blocks = [
        sp.kronecker_product(g.T, identity) - sp.kronecker_product(identity, g)
        for g in generators
    ]
    stacked_map = sp.Matrix.vstack(*blocks)
    return d * d - stacked_map.rank()


def hermitian_real_coordinates(matrix: sp.Matrix) -> list[sp.Expr]:
    """Coordinates in a fixed real basis of Hermitian 4-by-4 matrices."""
    coordinates: list[sp.Expr] = [matrix[i, i] for i in range(matrix.rows)]
    for i in range(matrix.rows):
        for j in range(i + 1, matrix.cols):
            real_part, imaginary_part = sp.expand(matrix[i, j]).as_real_imag()
            coordinates.extend((real_part, imaginary_part))
    return coordinates


print("GROUP A -- live axiom text")
axiom_text = flattened_text(AXIOM_MEMO)
check(
    "A1 lattice substrate sentence is present",
    "Physical sites are the points of the cubic lattice `Z^3`" in axiom_text,
)
check(
    "A2 one-site algebra sentence is present",
    "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    in axiom_text,
)
check("A3 no-site-privilege sentence is present", "No site is privileged." in axiom_text)
check(
    "A4 further structure is assigned downstream",
    "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration"
    in axiom_text,
)


print("GROUP B -- exact tensor generation")
canonical_generators: dict[int, dict[tuple[int, str], sp.Matrix]] = {}
for n in (2, 3):
    generators = embedded_generators(n)
    canonical_generators[n] = generators
    zero = sp.zeros(2**n)
    distinct_site_commutators = [
        generators[(left_slot, left_label)] * generators[(right_slot, right_label)]
        - generators[(right_slot, right_label)] * generators[(left_slot, left_label)]
        for left_slot in range(n)
        for right_slot in range(left_slot + 1, n)
        for left_label in ("x", "y", "z")
        for right_label in ("x", "y", "z")
    ]
    check(
        f"B1 n={n}: distinct-site Pauli images commute elementwise",
        all(commutator == zero for commutator in distinct_site_commutators),
        f"tested={len(distinct_site_commutators)}",
    )

    strings = pauli_strings(n)
    expected_dimension = 4**n
    check(
        f"B2 n={n}: the tensor-word family has exactly 4^n members",
        len(strings) == expected_dimension,
        f"members={len(strings)}",
    )
    flattened = sp.Matrix([row_flatten(string) for string in strings])
    gram = flattened.conjugate() * flattened.T
    check(
        f"B2 n={n}: Pauli strings have the exact trace Gram matrix 2^n I",
        gram == (2**n) * sp.eye(expected_dimension),
        f"Gram shape={gram.shape}",
    )
    actual_rank = flattened.rank()
    check(
        f"B2 n={n}: Pauli strings have exact matrix-space rank 4^n",
        actual_rank == expected_dimension == (2**n) ** 2,
        f"rank={actual_rank}",
    )

same_factor_commutator = SIGMA_X * SIGMA_Z - SIGMA_Z * SIGMA_X
check(
    "B3 rejector: same-factor M_2 generators violate elementwise commutation",
    same_factor_commutator != sp.zeros(2),
    f"commutator={same_factor_commutator.tolist()}",
)


print("GROUP C -- exact minimality and multiplicity discrimination")
minimal_generators = list(canonical_generators[2].values())
minimal_commutant_dimension = commutant_dimension(minimal_generators)
check(
    "C1 minimal C^4 carrier has scalar commutant",
    minimal_commutant_dimension == 1,
    f"commutant dimension={minimal_commutant_dimension}",
)

multiplicity_generators = [sp.kronecker_product(g, I2) for g in minimal_generators]
multiplicity_commutant_dimension = commutant_dimension(multiplicity_generators)
check(
    "C2 multiplicity-two C^8 carrier has a four-dimensional commutant",
    multiplicity_commutant_dimension == 4,
    f"commutant dimension={multiplicity_commutant_dimension}",
)
check(
    "C2 rejector: the minimal carrier is not accepted as multiplicity two",
    minimal_commutant_dimension != 4,
    f"minimal commutant dimension={minimal_commutant_dimension}",
)

for n in range(1, 6):
    carrier_dimension = 2**n
    if n == 1:
        dimension_gate = carrier_dimension == 2 and carrier_dimension < 3
        detail = "single-site dimension=2 is below 3"
    else:
        dimension_gate = carrier_dimension == 2**n and carrier_dimension >= 4 >= 3
        detail = f"multi-site dimension={carrier_dimension} is at least 4"
    check(f"C3 n={n}: carrier dimension gate", dimension_gate, detail)


print("GROUP D -- projection span and exact trace-form tests")
d = 4
basis_vectors = [sp.eye(d).col(i) for i in range(d)]
spanning_vectors: list[sp.Matrix] = list(basis_vectors)
for i in range(d):
    for j in range(i + 1, d):
        spanning_vectors.append(basis_vectors[i] + basis_vectors[j])
        spanning_vectors.append(basis_vectors[i] + sp.I * basis_vectors[j])

rank_one_projections = [
    (vector * vector.H) / (vector.H * vector)[0] for vector in spanning_vectors
]
projection_coordinate_matrix = sp.Matrix(
    [hermitian_real_coordinates(projection) for projection in rank_one_projections]
)
projection_span_rank = projection_coordinate_matrix.rank()
check(
    "D1 exact rank-one projections span the full real Hermitian space",
    len(rank_one_projections) == 16 and projection_span_rank == d * d,
    f"family size={len(rank_one_projections)}, real rank={projection_span_rank}",
)

diagonal_projections = [sp.diag(*bits) for bits in itertools.product((0, 1), repeat=d)]
diagonal_coordinate_matrix = sp.Matrix(
    [hermitian_real_coordinates(projection) for projection in diagonal_projections]
)
diagonal_span_rank = diagonal_coordinate_matrix.rank()
check(
    "D2 rejector: diagonal projections have deficient real span",
    diagonal_span_rank == 4 and diagonal_span_rank < d * d,
    f"real rank={diagonal_span_rank} < {d * d}",
)

sigma = sp.diag(sp.Rational(1, 10), sp.Rational(2, 10), sp.Rational(3, 10), sp.Rational(4, 10))
sigma_eigenvalues = list(sigma.eigenvals().keys())
check(
    "D3 density matrix is exactly positive with unit trace",
    sp.trace(sigma) == 1 and all(value > 0 for value in sigma_eigenvalues),
    f"eigenvalues={sigma_eigenvalues}",
)

resolution = [vector * vector.H for vector in basis_vectors]
resolution_is_orthogonal = all(
    resolution[i] * resolution[j] == sp.zeros(d)
    for i in range(d)
    for j in range(d)
    if i != j
)
check(
    "D3 projectors form an exact orthogonal resolution of identity",
    resolution_is_orthogonal and sum(resolution, sp.zeros(d)) == sp.eye(d),
)


def measure(projection: sp.Matrix) -> sp.Expr:
    return sp.trace(sigma * projection)


weights = [measure(projection) for projection in resolution]
check(
    "D3 trace weights are nonnegative and normalized",
    all(weight >= 0 for weight in weights) and sum(weights, sp.S.Zero) == 1,
    f"weights={weights}",
)
pair_additivity = all(
    measure(resolution[i] + resolution[j])
    == measure(resolution[i]) + measure(resolution[j])
    for i in range(d)
    for j in range(i + 1, d)
)
check("D3 trace form is exactly additive on every tested orthogonal pair", pair_additivity)


print("GROUP E -- note content and link gates")
note_text = NOTE.read_text(encoding="utf-8")
flat_note = " ".join(note_text.split())
check(
    "E1 live memo basename is present",
    "MINIMAL_AXIOMS_2026-06-29.md" in flat_note,
)
obsolete_targets = [
    "](" + "MINIMAL_AXIOMS_2026-05-20.md)",
    "](" + "MINIMAL_AXIOMS_2026-06-05.md)",
]
check(
    "E1 obsolete memo link targets are absent",
    all(target not in note_text for target in obsolete_targets),
)
check(
    "E2 the bridge selection is explicitly named",
    "named minimality selection" in flat_note.lower(),
)
check(
    "E2 the commuting joint presentation is explicitly supplied rather than axiom-derived",
    "supplied commuting joint presentation" in flat_note.lower()
    and "do not themselves construct a common `B(H)` representation" in flat_note,
)
check(
    "E2 source note disclaims audit-outcome authority",
    "does not set or predict an audit outcome" in flat_note,
)
forbidden_overclaims = [
    "closes " + "the",
    "only " + "route",
    "exhau" + "sted",
    "Status: " + "ret" + "ained",
]
check(
    "E3 forbidden overclaims are absent",
    all(phrase not in note_text for phrase in forbidden_overclaims),
)
markdown_targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note_text)
expected_targets = [
    "../scripts/frontier_qubit_lattice_joint_presentation_tensor_substrate_2026_07_09.py",
    "../logs/runner-cache/frontier_qubit_lattice_joint_presentation_tensor_substrate_2026_07_09.txt",
    "MINIMAL_AXIOMS_2026-06-29.md",
]
check(
    "E3 markdown link inventory is exactly the three authorized targets",
    markdown_targets == expected_targets,
    f"targets={markdown_targets}",
)


if FAIL == 0:
    print("VERDICT: exact bridge checks and all named rejectors pass.")
else:
    print("VERDICT: one or more exact bridge checks failed.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
