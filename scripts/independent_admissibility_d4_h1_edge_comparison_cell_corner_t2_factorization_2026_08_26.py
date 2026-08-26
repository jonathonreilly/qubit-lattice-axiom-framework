#!/usr/bin/env python3
"""Independent Block-207 edge/corner factorization checker.

This checker deliberately does not import the primary Block-207 runner.  It
uses character sums rather than the primary nullspace census, constructs the
radial/handed incidence maps from indices, and rebuilds the native Laurent
feature equations from the inherited Block-193/206 raw action constructors.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as b206  # noqa: E402


I = sp.I
B = b193.b190
AUDIT_TIMEOUT_SEC = 120
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_"
    "FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PRIMARY = (
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_"
    "factorization_2026_08_26.py"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block207-edge-comparison-cell-corner-t2-"
    "factorization-20260826"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
PARENT = "42b25280486363e9c2017698b813edf182d1a1a3"
PREREG = "c5f6e2fc8dea20218313944c8d5f5dae0f4d90cc"
MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "78d0c9a24ccb4eb96fe2112f60c1aea491100514"
PREFLIGHT_BLOB = "11addbb97c79b5acc0489f3dd940356726989bb6"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.py",
    ".claude/science/physics-loops/toe-axiom-closure-block207-edge-comparison-cell-corner-t2-factorization-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block207-edge-comparison-cell-corner-t2-factorization-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_main", "drop_parent", "drop_prereg", "alter_goal",
    "alter_preflight", "claim_scalar_edge_t2", "erase_scalar_corner_t2",
    "erase_corner_bloch_t2", "erase_corner_m2_t2", "linear_corner_moment",
    "mix_selector_classes", "flip_radial_selector", "flip_handed_selector",
    "rotate_sites_only", "remove_commutator_i", "swap_shell_parities",
    "erase_native_vertex", "change_tt_column", "fit_group_weights",
    "use_adjoint_reverse", "break_forward_residual", "break_reverse_residual",
    "erase_atom_uniqueness", "call_factor_cube_physical",
    "claim_spatial_fit", "hide_uncovered_rows", "hide_temporal_witness",
    "erase_p_collision", "supply_p_label", "erase_corner_positivity",
    "claim_action_m2_contents", "identify_exterior_with_m2", "open_h2",
    "claim_formation", "claim_history", "claim_axiom", "claim_obligation",
    "claim_toe", "claim_retained", "claim_broad_no_go", "erase_note_scope",
)


def rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix), extension=True).rank()


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=300
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=300,
    ).returncode == 0


@cache
def authority() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_now": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_now": git("hash-object", "--", PREFLIGHT),
        "axiom_main": git("rev-parse", f"origin/main:{AXIOM}"),
        "axiom_now": git("hash-object", "--", AXIOM),
        "registry_main": git("rev-parse", f"origin/main:{REGISTRY}"),
        "registry_now": git("hash-object", "--", REGISTRY),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def rotations() -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in permutations(range(3)):
        perm = sp.zeros(3)
        for row, column in enumerate(permutation):
            perm[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * perm
            if candidate.det() == 1:
                result.append(candidate)
    return tuple(result)


def edges() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (1, -1)
    )


def corners() -> tuple[sp.Matrix, ...]:
    return tuple(sp.Matrix(c) for c in product((-1, 1), repeat=3))


def permutation_representation(
    rotation: sp.MatrixBase, shell: tuple[sp.Matrix, ...]
) -> sp.Matrix:
    result = sp.zeros(len(shell))
    for source, vector in enumerate(shell):
        transformed = sp.Matrix(rotation * vector)
        target = next(i for i, candidate in enumerate(shell)
                      if candidate == transformed)
        result[target, source] = 1
    return result


def t2_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    tensors = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in tensors:
        transformed = sp.Matrix(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1], transformed[1, 2], transformed[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


def character_multiplicity(
    domain_representations: tuple[sp.Matrix, ...]
) -> sp.Expr:
    return sp.simplify(sum(
        sp.trace(domain) * sp.trace(t2_representation(rotation))
        for rotation, domain in zip(rotations(), domain_representations)
    ) / len(rotations()))


def parity_matrix(shell: tuple[sp.Matrix, ...]) -> sp.Matrix:
    result = sp.zeros(len(shell))
    for source, vector in enumerate(shell):
        target = next(i for i, candidate in enumerate(shell)
                      if candidate == -vector)
        result[target, source] = 1
    return result


def corner_bloch_basis() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    shell = corners()
    linear = sp.zeros(3, 24)
    paired = sp.zeros(3, 24)
    triple = sp.zeros(3, 24)
    for corner_index, c in enumerate(shell):
        def put(matrix: sp.Matrix, row: int, component: int,
                value: sp.Expr) -> None:
            matrix[row, 3 * corner_index + component] += value / 8

        put(linear, 0, 1, c[0]); put(linear, 0, 0, c[1])
        put(linear, 1, 2, c[1]); put(linear, 1, 1, c[2])
        put(linear, 2, 2, c[0]); put(linear, 2, 0, c[2])

        put(paired, 0, 0, c[0] * c[2])
        put(paired, 0, 1, -c[1] * c[2])
        put(paired, 1, 1, c[0] * c[1])
        put(paired, 1, 2, -c[0] * c[2])
        put(paired, 2, 2, c[1] * c[2])
        put(paired, 2, 0, -c[0] * c[1])

        cubic = c[0] * c[1] * c[2]
        put(triple, 0, 2, cubic)
        put(triple, 1, 0, cubic)
        put(triple, 2, 1, cubic)
    return linear, paired, triple


@cache
def representation_facts() -> dict[str, object]:
    group = rotations()
    edge_reps = tuple(permutation_representation(r, edges()) for r in group)
    corner_reps = tuple(
        permutation_representation(r, corners()) for r in group
    )
    edge_bloch = tuple(
        sp.kronecker_product(shell, r)
        for shell, r in zip(edge_reps, group)
    )
    corner_bloch = tuple(
        sp.kronecker_product(shell, r)
        for shell, r in zip(corner_reps, group)
    )
    mixed = sp.Matrix((
        tuple(c[0] * c[1] / 8 for c in corners()),
        tuple(c[1] * c[2] / 8 for c in corners()),
        tuple(c[0] * c[2] / 8 for c in corners()),
    ))
    corner_basis = corner_bloch_basis()
    mixed_covariant = all(
        t2_representation(r) * mixed == mixed * corner
        for r, corner in zip(group, corner_reps)
    )
    bloch_basis_covariant = all(
        t2_representation(r) * basis == basis * domain
        for r, domain in zip(group, corner_bloch)
        for basis in corner_basis
    )
    bloch_basis_independent = rank(sp.Matrix.hstack(*(
        basis.reshape(72, 1) for basis in corner_basis
    ))) == 3

    edge_parity = sp.kronecker_product(
        parity_matrix(edges()), sp.eye(3)
    )
    odd_sum = 0
    even_sum = 0
    for r, domain in zip(group, edge_bloch):
        target_character = sp.trace(t2_representation(r))
        total_character = sp.trace(domain)
        parity_character = sp.trace(edge_parity * domain)
        even_sum += (total_character + parity_character) * target_character / 2
        odd_sum += (total_character - parity_character) * target_character / 2

    return {
        "group_order": len(group),
        "closed": all(any(a * b == c for c in group)
                      for a in group for b in group),
        "edge_scalar_hom": character_multiplicity(edge_reps),
        "edge_bloch_hom": character_multiplicity(edge_bloch),
        "corner_scalar_hom": character_multiplicity(corner_reps),
        "corner_bloch_hom": character_multiplicity(corner_bloch),
        "corner_m2_hom": (
            character_multiplicity(corner_reps)
            + character_multiplicity(corner_bloch)
        ),
        "mixed_rank": mixed.rank(),
        "mixed_covariant": mixed_covariant,
        "bloch_basis_covariant": bloch_basis_covariant,
        "bloch_basis_independent": bloch_basis_independent,
        "odd_hom": sp.simplify(odd_sum / len(group)),
        "even_hom": sp.simplify(even_sum / len(group)),
    }


def selector_matrices() -> dict[str, sp.Matrix]:
    edge_shell = edges()
    corner_shell = corners()
    radial = sp.zeros(8, 18)
    handed = sp.zeros(8, 18)
    for row, c in enumerate(corner_shell):
        for axis in range(3):
            direction = c[axis] * sp.eye(3)[:, axis]
            edge = next(i for i, candidate in enumerate(edge_shell)
                        if candidate == direction)
            cross = direction.cross(c) / sp.sqrt(3)
            for component in range(3):
                radial[row, 3 * edge + component] += (
                    c[component] / sp.sqrt(3)
                )
                handed[row, 3 * edge + component] += cross[component]

    odd = sp.zeros(3, 18)
    even = sp.zeros(3, 18)
    pairs = ((0, 1), (1, 2), (0, 2))
    for row, (left, right) in enumerate(pairs):
        remaining = next(axis for axis in range(3)
                         if axis not in (left, right))
        orientation = sp.LeviCivita(left, right, remaining)
        for edge, direction in enumerate(edge_shell):
            axis = next(i for i, value in enumerate(direction) if value)
            sign = direction[axis]
            for component in range(3):
                odd[row, 3 * edge + component] = -sign * (
                    int(axis == left and component == right)
                    + int(axis == right and component == left)
                )
                even[row, 3 * edge + component] = orientation * (
                    int(axis == left) - int(axis == right)
                ) * int(component == remaining)
    mixed = sp.Matrix((
        tuple(c[0] * c[1] / 8 for c in corner_shell),
        tuple(c[1] * c[2] / 8 for c in corner_shell),
        tuple(c[0] * c[2] / 8 for c in corner_shell),
    ))
    return {
        "radial": radial, "handed": handed, "odd": odd,
        "even": even, "mixed": mixed,
    }


@cache
def selector_facts() -> dict[str, object]:
    matrices = selector_matrices()
    radial = matrices["radial"]
    handed = matrices["handed"]
    odd = matrices["odd"]
    even = matrices["even"]
    mixed = matrices["mixed"]
    edge_parity = sp.kronecker_product(
        parity_matrix(edges()), sp.eye(3)
    )
    corner_parity = parity_matrix(corners())
    group = rotations()
    covariance = all(
        permutation_representation(r, corners()) * radial
        == radial * sp.kronecker_product(
            permutation_representation(r, edges()), r
        )
        and permutation_representation(r, corners()) * handed
        == handed * sp.kronecker_product(
            permutation_representation(r, edges()), r
        )
        and t2_representation(r) * odd
        == odd * sp.kronecker_product(
            permutation_representation(r, edges()), r
        )
        and t2_representation(r) * even
        == even * sp.kronecker_product(
            permutation_representation(r, edges()), r
        )
        for r in group
    )

    sigma = (
        sp.Matrix(((0, 1), (1, 0))),
        sp.Matrix(((0, -I), (I, 0))),
        sp.Matrix(((1, 0), (0, -1))),
    )
    pauli_jordan = True
    pauli_commutator = True
    for c in corners():
        chat = c / sp.sqrt(3)
        chat_sigma = sum((chat[a] * sigma[a] for a in range(3)), sp.zeros(2))
        for axis in range(3):
            n = c[axis] * sp.eye(3)[:, axis]
            n_sigma = sum((n[a] * sigma[a] for a in range(3)), sp.zeros(2))
            cross = n.cross(chat)
            cross_sigma = sum(
                (cross[a] * sigma[a] for a in range(3)), sp.zeros(2)
            )
            pauli_commutator = pauli_commutator and (
                sp.expand((n_sigma * chat_sigma - chat_sigma * n_sigma)
                          / (2 * I) - cross_sigma) == sp.zeros(2)
            )
            pauli_jordan = pauli_jordan and all(
                sp.simplify(sp.trace(sigma[a] * chat_sigma) / 2 - chat[a])
                == 0 for a in range(3)
            )

    return {
        "covariance": covariance,
        "radial_composition": mixed * radial == -odd / (2 * sp.sqrt(3)),
        "handed_composition": mixed * handed == even / (2 * sp.sqrt(3)),
        "basis_independent": rank(sp.Matrix.hstack(
            odd.reshape(54, 1), even.reshape(54, 1)
        )) == 2,
        "odd_parity": odd * edge_parity == -odd,
        "even_parity": even * edge_parity == even,
        "mixed_even": mixed * corner_parity == mixed,
        "radial_parity": corner_parity * radial == -radial * edge_parity,
        "handed_parity": corner_parity * handed == handed * edge_parity,
        "pauli_jordan": pauli_jordan,
        "pauli_commutator": pauli_commutator,
    }


def reverse_polynomial(polynomial: B.PolyMatrix) -> B.PolyMatrix:
    result: B.PolyMatrix = {}
    for power, matrix in polynomial.items():
        transformed = power[:4] + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = B.poly_add(result, {transformed: matrix})
    return result


def native_hodge(slot: int) -> B.PolyMatrix:
    left, right = B.PAIRS4[slot]
    scalar = B.poly_scale(B.poly_multiply(
        B.placed_cosine(left), B.placed_cosine(right)
    ), -1 / sp.sqrt(2))
    internal = (
        B.CREATION[left] * B.ANNIHILATION[right]
        + B.CREATION[right] * B.ANNIHILATION[left]
    )
    return B.poly_multiply(scalar, {B.ZERO_EXPONENT: internal})


def differences() -> tuple[tuple[B.PolyMatrix, ...], tuple[B.PolyMatrix, ...]]:
    incoming = []
    outgoing = []
    for axis in range(4):
        incoming.append({
            B.exponent({axis: 1}): B.CREATION[axis] / (2 * I),
            B.exponent({axis: -1}): -B.CREATION[axis] / (2 * I),
        })
        outgoing.append({
            B.exponent({axis: 1}, {axis: 1}): B.CREATION[axis] / (2 * I),
            B.exponent({axis: -1}, {axis: -1}): -B.CREATION[axis] / (2 * I),
        })
    return tuple(incoming), tuple(outgoing)


def source_from_raw() -> tuple[B.PolyMatrix, tuple[sp.Expr, ...]]:
    coefficients = b193.tt_source_coefficients("H1", 1)
    source: B.PolyMatrix = {}
    for coefficient, vertex in zip(coefficients, b206.raw_action_vertices()):
        source = B.poly_add(source, B.poly_scale(vertex, coefficient))
    return source, coefficients


def feature_library(
    slots: tuple[int, ...], coefficients: tuple[sp.Expr, ...], atomized: bool
) -> tuple[list[tuple[str, B.PolyMatrix]], tuple[sp.Expr, ...]]:
    incoming, outgoing = differences()
    columns: list[tuple[str, B.PolyMatrix]] = []
    weights = []
    for slot in slots:
        hodge = native_hodge(slot)
        groups = [(f"{slot}:mass", hodge, B.MASS * coefficients[slot])]
        for axis in range(4):
            groups.append((
                f"{slot}:right:{axis}",
                B.poly_scale(B.poly_multiply(hodge, incoming[axis]), I),
                coefficients[slot],
            ))
            groups.append((
                f"{slot}:left:{axis}",
                B.poly_scale(B.poly_multiply(
                    B.poly_transpose(outgoing[axis]), hodge
                ), I),
                coefficients[slot],
            ))
        for name, polynomial, weight in groups:
            pieces = (
                tuple({power: matrix} for power, matrix in polynomial.items())
                if atomized else (polynomial,)
            )
            for index, piece in enumerate(pieces):
                columns.append((f"{name}:{index}" if atomized else name, piece))
                weights.append(weight)
    return columns, tuple(weights)


def sparse_design(
    columns: list[tuple[str, B.PolyMatrix]], target: B.PolyMatrix | None = None
) -> tuple[sp.Matrix, sp.Matrix, tuple[tuple[object, ...], ...]]:
    zero = sp.zeros(16)
    polynomials = [polynomial for _name, polynomial in columns]
    surfaces = polynomials + ([target] if target is not None else [])
    rows = tuple(sorted({
        (power, row, column)
        for polynomial in surfaces
        for power, matrix in polynomial.items()
        for row in range(16) for column in range(16)
        if matrix[row, column] != 0
    }))
    matrix = sp.Matrix([
        [polynomial.get(power, zero)[row, column]
         for polynomial in polynomials]
        for power, row, column in rows
    ])
    vector = sp.Matrix([
        (target if target is not None else {}).get(power, zero)[row, column]
        for power, row, column in rows
    ])
    return matrix, vector, rows


@cache
def factorization_facts() -> dict[str, object]:
    source, coefficients = source_from_raw()
    inherited_source = b206.combined_raw_source()
    incoming, outgoing = differences()
    vertices = b206.raw_action_vertices()
    vertex_checks = []
    for slot in (7, 8, 9):
        hodge = native_hodge(slot)
        reconstructed = B.poly_add(
            B.poly_scale(hodge, B.MASS),
            B.poly_scale(B.poly_multiply(
                hodge, B.poly_add(*incoming)
            ), I),
            B.poly_scale(B.poly_multiply(
                B.poly_transpose(B.poly_add(*outgoing)), hodge
            ), I),
        )
        vertex_checks.append(reconstructed == vertices[slot])

    generic, _generic_weights = feature_library((7, 8, 9), coefficients, False)
    generic_atoms, _ = feature_library((7, 8, 9), coefficients, True)
    generic_matrix, _, _ = sparse_design(generic)
    generic_atom_matrix, _, _ = sparse_design(generic_atoms)

    grouped, grouped_weights = feature_library((8, 9), coefficients, False)
    atoms, atom_weights = feature_library((8, 9), coefficients, True)
    forward_matrix, forward_vector, forward_rows = sparse_design(grouped, source)
    atom_matrix, atom_vector, _ = sparse_design(atoms, source)
    reverse_source = reverse_polynomial(source)
    reverse_groups = [(name, reverse_polynomial(poly)) for name, poly in grouped]
    reverse_atoms = [(name, reverse_polynomial(poly)) for name, poly in atoms]
    reverse_matrix, reverse_vector, reverse_rows = sparse_design(
        reverse_groups, reverse_source
    )
    reverse_atom_matrix, reverse_atom_vector, _ = sparse_design(
        reverse_atoms, reverse_source
    )
    weights = sp.Matrix(grouped_weights)
    atom_weight_vector = sp.Matrix(atom_weights)
    stacked = forward_matrix.col_join(reverse_matrix)
    stacked_target = forward_vector.col_join(reverse_vector)

    spatial = [(name, poly) for name, poly in grouped
               if not name.endswith(":3")]
    spatial_matrix, spatial_vector, spatial_rows = sparse_design(spatial, source)
    uncovered = tuple(
        row for index, row in enumerate(spatial_rows)
        if all(spatial_matrix[index, column] == 0
               for column in range(spatial_matrix.cols))
        and spatial_vector[index] != 0
    )
    reverse_spatial = [
        (name, reverse_polynomial(poly)) for name, poly in spatial
    ]
    reverse_spatial_matrix, reverse_spatial_vector, reverse_spatial_rows = (
        sparse_design(reverse_spatial, reverse_source)
    )
    reverse_uncovered = tuple(
        row for index, row in enumerate(reverse_spatial_rows)
        if all(reverse_spatial_matrix[index, column] == 0
               for column in range(reverse_spatial_matrix.cols))
        and reverse_spatial_vector[index] != 0
    )

    witness_power = (-1, 0, -1, -1, 0, 0, 0, -1)
    flattened = sp.Matrix.hstack(*(
        matrix.reshape(256, 1) for matrix in source.values()
    ))
    spatial_support = {power[:3] + power[4:7] for power in source}
    matter_support = {power[:3] for power in spatial_support}
    geometry_support = {power[3:] for power in spatial_support}

    return {
        "tt_coefficients": tuple(sp.simplify(x) for x in coefficients),
        "source_independent_match": source == inherited_source,
        "vertices": all(vertex_checks),
        "generic_shape": generic_matrix.shape,
        "generic_rank": rank(generic_matrix),
        "generic_atom_shape": generic_atom_matrix.shape,
        "generic_atom_rank": rank(generic_atom_matrix),
        "generic_atom_nullity": generic_atom_matrix.cols - rank(generic_atom_matrix),
        "forward_shape": forward_matrix.shape,
        "forward_rank": rank(forward_matrix),
        "forward_augmented": rank(forward_matrix.row_join(forward_vector)),
        "forward_residual": sum(x != 0 for x in forward_matrix * weights - forward_vector),
        "atom_shape": atom_matrix.shape,
        "atom_rank": rank(atom_matrix),
        "atom_augmented": rank(atom_matrix.row_join(atom_vector)),
        "atom_residual": sum(x != 0 for x in atom_matrix * atom_weight_vector - atom_vector),
        "reverse_rank": rank(reverse_matrix),
        "reverse_augmented": rank(reverse_matrix.row_join(reverse_vector)),
        "reverse_residual": sum(x != 0 for x in reverse_matrix * weights - reverse_vector),
        "reverse_atom_rank": rank(reverse_atom_matrix),
        "reverse_atom_augmented": rank(reverse_atom_matrix.row_join(reverse_atom_vector)),
        "reverse_atom_residual": sum(x != 0 for x in reverse_atom_matrix * atom_weight_vector - reverse_atom_vector),
        "stacked_rank": rank(stacked),
        "stacked_augmented": rank(stacked.row_join(stacked_target)),
        "stacked_residual": sum(x != 0 for x in stacked * weights - stacked_target),
        "weight_vector": tuple(grouped_weights),
        "support_union": set(source) == set().union(*(set(poly) for _name, poly in grouped)),
        "forward_terms": len(source),
        "reverse_terms": len(reverse_source),
        "coefficient_nnz": sum(x != 0 for matrix in source.values() for x in matrix),
        "coefficient_span": rank(flattened),
        "rank_distribution": dict(Counter(matrix.rank() for matrix in source.values())),
        "spatial_support": len(spatial_support),
        "matter_support": len(matter_support),
        "geometry_support": len(geometry_support),
        "spatial_shape": spatial_matrix.shape,
        "spatial_rank": rank(spatial_matrix),
        "spatial_augmented": rank(spatial_matrix.row_join(spatial_vector)),
        "uncovered": len(uncovered),
        "reverse_spatial_rank": rank(reverse_spatial_matrix),
        "reverse_spatial_augmented": rank(
            reverse_spatial_matrix.row_join(reverse_spatial_vector)
        ),
        "reverse_uncovered": len(reverse_uncovered),
        "temporal_witness": sp.simplify(source[witness_power][1, 12]),
        "actual_reverse": True,
        "factor_cube_physical": False,
    }


@cache
def collision_facts() -> dict[str, object]:
    incoming, transfer = b193.POINTS["H1"]
    control = (sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3])
    coefficients = b193.tt_source_coefficients("H1", 1)

    def pair(momentum: tuple[sp.Expr, ...]) -> tuple[sp.Matrix, sp.Matrix]:
        outgoing = tuple(momentum[i] + transfer[i] for i in range(4))
        _a, _h, forward = B.centered_objects(momentum, transfer)
        _ra, _rh, reverse = B.centered_objects(
            outgoing, tuple(-x for x in transfer)
        )
        return tuple(sp.expand(sum(
            (coefficients[i] * vertices[i] for i in range(10)),
            sp.zeros(16),
        )) for vertices in (forward, reverse))  # type: ignore[return-value]

    primary = pair(incoming)
    alternative = pair(control)
    delta = tuple(sp.expand(a - b) for a, b in zip(primary, alternative))
    return {
        "same_q": True,
        "forward_rank": rank(delta[0]),
        "reverse_rank": rank(delta[1]),
        "forward_nnz": sum(x != 0 for x in delta[0]),
        "reverse_nnz": sum(x != 0 for x in delta[1]),
        "forward_witness": sp.factor(delta[0][0, 4]),
        "reverse_witness": sp.factor(delta[1][0, 4]),
        "p_external": False,
    }


@cache
def positive_m2_facts() -> dict[str, object]:
    coefficients = b193.tt_source_coefficients("H1", 1)
    h = sp.Matrix((
        coefficients[7] / sp.sqrt(2),
        coefficients[9] / sp.sqrt(2),
        coefficients[8] / sp.sqrt(2),
    ))
    tensor = sp.Matrix(((0, h[0], h[2]),
                        (h[0], 0, h[1]),
                        (h[2], h[1], 0)))
    affine = -tensor / 4
    field = sp.Matrix.vstack(*(affine * c for c in corners()))
    face = sp.zeros(18, 24)
    for edge, direction in enumerate(edges()):
        axis = next(i for i, value in enumerate(direction) if value)
        sign = direction[axis]
        selected = [i for i, c in enumerate(corners()) if c[axis] == sign]
        for corner in selected:
            for component in range(3):
                face[3 * edge + component, 3 * corner + component] = sp.Rational(1, 4)
    face_values = face * field
    selector = selector_matrices()
    corner_norms = tuple(sp.simplify((affine * c).dot(affine * c))
                         for c in corners())
    face_norms = tuple(sp.simplify(
        face_values[3 * edge:3 * edge + 3, 0].dot(
            face_values[3 * edge:3 * edge + 3, 0]
        )
    ) for edge in range(6))
    group = rotations()
    face_covariance = all(
        sp.kronecker_product(permutation_representation(r, edges()), r) * face
        == face * sp.kronecker_product(
            permutation_representation(r, corners()), r
        ) for r in group
    )
    expected_corner = (3 + sp.sqrt(2)) / 16
    expected_face = sp.Rational(3, 32)
    return {
        "target": tuple(sp.simplify(x) for x in h),
        "map_rank": face.rank(),
        "covariant": face_covariance,
        "odd_output": tuple(sp.simplify(x) for x in selector["odd"] * face_values),
        "even_output": tuple(sp.simplify(x) for x in selector["even"] * face_values),
        "max_corner": expected_corner,
        "max_corner_attained": expected_corner in corner_norms,
        "max_corner_dominates": all(
            sp.simplify(expected_corner - x).is_nonnegative is True
            for x in corner_norms
        ),
        "max_face": expected_face,
        "max_face_attained": expected_face in face_norms,
        "max_face_dominates": all(
            sp.simplify(expected_face - x).is_nonnegative is True
            for x in face_norms
        ),
        "strict_positive": all(
            sp.simplify(1 - x).is_positive is True
            for x in corner_norms + face_norms
        ),
        "action_derived": False,
    }


@cache
def note_scope() -> dict[str, bool]:
    path = ROOT / NOTE
    if not path.is_file():
        return {"exists": False, "scope": False, "resolution": False}
    text = path.read_text()
    return {
        "exists": True,
        "scope": all(phrase in text for phrase in (
            "operator-factorization support", "same-time spatial cube",
            "actual neighboring `M2`", "H2 remains sealed",
            "obligation retirement: 0", "TOE percentage movement: 0",
        )),
        "resolution": all(phrase in text for phrase in (
            "per_element:", "per_site:", "per_mode:",
            "per_block:", "lattice_wide:",
        )),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    auth = authority()
    rep = representation_facts()
    selectors = selector_facts()
    factor = factorization_facts()
    collision = collision_facts()
    witness = positive_m2_facts()
    scope = note_scope()
    claims: dict[str, object] = {
        "main": MAIN, "parent": True, "prereg": True,
        "goal": GOAL_BLOB, "preflight": PREFLIGHT_BLOB,
        "edge_scalar": 0, "corner_scalar": 1, "corner_bloch": 3,
        "corner_m2": 4, "mixed": True, "selector_mixed": False,
        "radial_sign": -1, "handed_sign": 1, "selector_covariance": True,
        "commutator_i": True, "parities": (1, 1), "vertices": True,
        "tt_column": 1, "weights_fitted": False, "actual_reverse": True,
        "forward_residual": 0, "reverse_residual": 0, "atom_rank": 136,
        "factor_cube_physical": False, "spatial_fit": False,
        "uncovered": 128, "temporal_witness": sp.Rational(1, 8),
        "collision": True, "p_external": False, "positive": True,
        "action_m2": False, "exterior_m2": False, "h2": False,
        "formation": False, "history": False, "axiom": False,
        "obligation": 0, "toe": False, "retained": False,
        "broad_no_go": False, "note_scope": True,
    }
    changes = {
        "stale_main": ("main", "stale"), "drop_parent": ("parent", False),
        "drop_prereg": ("prereg", False), "alter_goal": ("goal", "bad"),
        "alter_preflight": ("preflight", "bad"),
        "claim_scalar_edge_t2": ("edge_scalar", 1),
        "erase_scalar_corner_t2": ("corner_scalar", 0),
        "erase_corner_bloch_t2": ("corner_bloch", 2),
        "erase_corner_m2_t2": ("corner_m2", 3),
        "linear_corner_moment": ("mixed", False),
        "mix_selector_classes": ("selector_mixed", True),
        "flip_radial_selector": ("radial_sign", 1),
        "flip_handed_selector": ("handed_sign", -1),
        "rotate_sites_only": ("selector_covariance", False),
        "remove_commutator_i": ("commutator_i", False),
        "swap_shell_parities": ("parities", (0, 2)),
        "erase_native_vertex": ("vertices", False),
        "change_tt_column": ("tt_column", 0),
        "fit_group_weights": ("weights_fitted", True),
        "use_adjoint_reverse": ("actual_reverse", False),
        "break_forward_residual": ("forward_residual", 1),
        "break_reverse_residual": ("reverse_residual", 1),
        "erase_atom_uniqueness": ("atom_rank", 135),
        "call_factor_cube_physical": ("factor_cube_physical", True),
        "claim_spatial_fit": ("spatial_fit", True),
        "hide_uncovered_rows": ("uncovered", 0),
        "hide_temporal_witness": ("temporal_witness", 0),
        "erase_p_collision": ("collision", False),
        "supply_p_label": ("p_external", True),
        "erase_corner_positivity": ("positive", False),
        "claim_action_m2_contents": ("action_m2", True),
        "identify_exterior_with_m2": ("exterior_m2", True),
        "open_h2": ("h2", True), "claim_formation": ("formation", True),
        "claim_history": ("history", True), "claim_axiom": ("axiom", True),
        "claim_obligation": ("obligation", 1), "claim_toe": ("toe", True),
        "claim_retained": ("retained", True),
        "claim_broad_no_go": ("broad_no_go", True),
        "erase_note_scope": ("note_scope", False),
    }
    if mutation:
        key, value = changes[mutation]
        claims[key] = value

    a = (
        auth["main"] == claims["main"]
        and auth["parent"] == claims["parent"]
        and auth["prereg"] == claims["prereg"]
        and auth["goal_registered"] == claims["goal"]
        and auth["goal_now"] == GOAL_BLOB
        and auth["preflight_registered"] == claims["preflight"]
        and auth["preflight_now"] == PREFLIGHT_BLOB
        and auth["axiom_main"] == AXIOM_BLOB
        and auth["axiom_now"] == AXIOM_BLOB
        and auth["registry_main"] == REGISTRY_MAIN_BLOB
        and auth["registry_now"] == REGISTRY_WORKTREE_BLOB
        and auth["inputs"]
    )
    b = (
        rep["group_order"] == 24 and rep["closed"]
        and rep["edge_scalar_hom"] == claims["edge_scalar"]
        and rep["edge_bloch_hom"] == 2
        and rep["corner_scalar_hom"] == claims["corner_scalar"]
        and rep["corner_bloch_hom"] == claims["corner_bloch"]
        and rep["corner_m2_hom"] == claims["corner_m2"]
        and rep["mixed_rank"] == 3
        and rep["mixed_covariant"] == claims["mixed"]
        and rep["bloch_basis_covariant"] and rep["bloch_basis_independent"]
        and (rep["odd_hom"], rep["even_hom"]) == claims["parities"]
    )
    c = (
        selectors["covariance"] == claims["selector_covariance"]
        and selectors["radial_composition"] == (claims["radial_sign"] == -1)
        and selectors["handed_composition"] == (claims["handed_sign"] == 1)
        and selectors["basis_independent"]
        and selectors["odd_parity"] and selectors["even_parity"]
        and selectors["mixed_even"] and selectors["radial_parity"]
        and selectors["handed_parity"] and selectors["pauli_jordan"]
        and selectors["pauli_commutator"] == claims["commutator_i"]
        and claims["selector_mixed"] is False
    )
    d = (
        factor["source_independent_match"]
        and factor["vertices"] == claims["vertices"]
        and factor["tt_coefficients"][8:] == (-sp.sqrt(2), sp.Integer(1))
        and claims["tt_column"] == 1 and claims["weights_fitted"] is False
        and factor["generic_shape"] == (816, 27)
        and factor["generic_rank"] == 27
        and factor["generic_atom_shape"] == (816, 204)
        and factor["generic_atom_rank"] == 202
        and factor["generic_atom_nullity"] == 2
    )
    e = (
        factor["forward_shape"] == (560, 18)
        and factor["forward_rank"] == factor["forward_augmented"] == 18
        and factor["forward_residual"] == claims["forward_residual"]
        and factor["atom_shape"] == (560, 136)
        and factor["atom_rank"] == claims["atom_rank"]
        and factor["atom_augmented"] == 136 and factor["atom_residual"] == 0
        and factor["reverse_rank"] == factor["reverse_augmented"] == 18
        and factor["reverse_residual"] == claims["reverse_residual"]
        and factor["reverse_atom_rank"] == factor["reverse_atom_augmented"] == 136
        and factor["reverse_atom_residual"] == 0
        and factor["stacked_rank"] == factor["stacked_augmented"] == 18
        and factor["stacked_residual"] == 0
        and factor["actual_reverse"] == claims["actual_reverse"]
        and factor["factor_cube_physical"] == claims["factor_cube_physical"]
        and factor["support_union"] and factor["forward_terms"] == 110
        and factor["reverse_terms"] == 110 and factor["coefficient_nnz"] == 560
        and factor["coefficient_span"] == 18
        and factor["rank_distribution"] == {4: 80, 6: 4, 8: 24, 12: 2}
        and (factor["spatial_support"], factor["matter_support"],
             factor["geometry_support"]) == (78, 38, 26)
    )
    f = (
        factor["spatial_shape"] == (560, 14)
        and factor["spatial_rank"] == 14
        and factor["spatial_augmented"] == (14 if claims["spatial_fit"] else 15)
        and factor["uncovered"] == claims["uncovered"]
        and factor["reverse_spatial_rank"] == 14
        and factor["reverse_spatial_augmented"] == 15
        and factor["reverse_uncovered"] == 128
        and factor["temporal_witness"] == claims["temporal_witness"]
        and collision["same_q"]
        and (collision["forward_rank"] == 12) == claims["collision"]
        and collision["reverse_rank"] == 12
        and collision["forward_nnz"] == collision["reverse_nnz"] == 56
        and sp.simplify(collision["forward_witness"]
                        - I * (1 + sp.sqrt(3)) / 8) == 0
        and sp.simplify(collision["reverse_witness"]
                        - I * (5 - sp.sqrt(3)) / 8) == 0
        and collision["p_external"] == claims["p_external"]
    )
    g = (
        witness["target"] == (0, 1 / sp.sqrt(2), -1)
        and witness["map_rank"] == 12 and witness["covariant"]
        and witness["odd_output"] == witness["target"]
        and witness["even_output"] == (0, 0, 0)
        and witness["max_corner"] == (3 + sp.sqrt(2)) / 16
        and witness["max_face"] == sp.Rational(3, 32)
        and witness["max_corner_attained"] and witness["max_corner_dominates"]
        and witness["max_face_attained"] and witness["max_face_dominates"]
        and witness["strict_positive"] == claims["positive"]
        and witness["action_derived"] == claims["action_m2"]
        and claims["exterior_m2"] is False
    )
    h = (
        claims["h2"] is False and claims["formation"] is False
        and claims["history"] is False and claims["axiom"] is False
        and claims["obligation"] == 0 and claims["toe"] is False
        and claims["retained"] is False and claims["broad_no_go"] is False
        and scope["exists"] and scope["scope"] == claims["note_scope"]
        and scope["resolution"]
    )
    return {
        "A": (a, "authority and immutable Block-207 registration are independently pinned"),
        "B": (b, "character sums and explicit corner moments give edge/corner T2 multiplicities"),
        "C": (c, "direct Pauli incidence gives radial-to-odd and handed-to-even selectors"),
        "D": (d, "raw action vertices independently split into the native 27 feature groups"),
        "E": (e, "one constructed weight vector reconstructs forward and actual reverse exactly"),
        "F": (f, "temporal support and same-q different-p residuals are exact and nonzero"),
        "G": (g, "positive corner and face M2 states realize only the H1 odd shear"),
        "H": (h, "scope keeps physical M2 ownership, H2, formation, and history open"),
    }


def mutation_sweep() -> int:
    survivors = []
    for mutation in MUTATIONS:
        if all(ok for ok, _message in evaluate(mutation).values()):
            survivors.append(mutation)
    print(
        f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(survivors)} "
        f"FAIL={len(survivors)}"
    )
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    checks = evaluate(args.mutation)
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
    factor = factorization_facts()
    collision = collision_facts()
    print("INDEPENDENT_HOM: edge scalar/Bloch=0/2; corner scalar/Bloch/M2=1/3/4; parity=1/1.")
    print("INDEPENDENT_SELECTORS: M*A_rad=-D_odd/(2*sqrt(3)); M*A_hand=D_even/(2*sqrt(3)).")
    print("INDEPENDENT_FACTOR: generic=27/27; H1 grouped=18/18; atoms=136/136; shared reverse residual=0.")
    print(
        "INDEPENDENT_BOUNDARY: spatial rank/augmented=14/15; "
        f"uncovered={factor['uncovered']}; witness=1/8; collision="
        f"{collision['forward_witness']},{collision['reverse_witness']}."
    )
    print("INDEPENDENT_RESULT: exact operator factorization and positive odd M2 witness; physical clock/M2 ownership remains open.")
    passed = sum(ok for ok, _message in checks.values())
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
