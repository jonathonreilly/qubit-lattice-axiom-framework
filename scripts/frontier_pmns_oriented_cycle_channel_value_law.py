#!/usr/bin/env python3
"""Bounded oriented-cycle coordinate extraction for a supplied 3x3 block.

This runner proves only finite matrix algebra:

  * an explicit supplied triplet embedding compresses an explicit finite
    cycle representation to C = E12 + E23 + E31;
  * the supplied coordinate projectors produce the ordered orthonormal basis
    E12, E23, E31;
  * for every supplied A in M_3(C), diag(A C^dagger) gives the exact
    Hilbert--Schmidt coordinates of its forward-cycle projection.

No physical carrier, Record readout, active-block selection, or coefficient
value-selection bridge is claimed.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "pmns_oriented_cycle_channel_value_law_note"
RUNNER_PATH = "scripts/frontier_pmns_oriented_cycle_channel_value_law.py"
NOTE_PATH = ROOT / "docs/PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1.0e-12


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def result_exit_code(fail_count: int) -> int:
    """Return a truthful process status for the accumulated failures."""
    return 1 if fail_count else 0


def e(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i, j] = 1.0
    return out


E11 = e(0, 0)
E22 = e(1, 1)
E33 = e(2, 2)
E12 = e(0, 1)
E23 = e(1, 2)
E31 = e(2, 0)
CYCLE = E12 + E23 + E31
I3 = np.eye(3, dtype=complex)


def taste_vector(state: tuple[int, int, int]) -> np.ndarray:
    factors = [
        np.array([1.0, 0.0], dtype=complex) if bit == 0 else np.array([0.0, 1.0], dtype=complex)
        for bit in state
    ]
    return np.kron(factors[0], np.kron(factors[1], factors[2]))


def supplied_triplet_embedding() -> np.ndarray:
    """Explicit isometric embedding used only as finite matrix data."""
    states = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return np.column_stack([taste_vector(state) for state in states])


def supplied_cycle_representation() -> np.ndarray:
    """Explicit 8x8 order-three cycle representation."""
    states = [(a1, a2, a3) for a1 in range(2) for a2 in range(2) for a3 in range(2)]
    state_index = {state: i for i, state in enumerate(states)}
    cycle = np.zeros((8, 8), dtype=complex)
    for state in states:
        a1, a2, a3 = state
        image = (a3, a1, a2)
        sign = (-1) ** ((a1 + a2) * a3)
        cycle[state_index[image], state_index[state]] = sign
    return cycle


def supplied_site_projector(state: tuple[int, int, int]) -> np.ndarray:
    vector = taste_vector(state)
    return np.outer(vector, vector.conj())


def projected_scalar_projectors() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    embedding = supplied_triplet_embedding()
    states = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return tuple(
        embedding.conj().T @ supplied_site_projector(state) @ embedding
        for state in states
    )


def projected_forward_cycle() -> np.ndarray:
    """Compression identity for the explicitly supplied finite matrices."""
    embedding = supplied_triplet_embedding()
    cycle = supplied_cycle_representation()
    return embedding.conj().T @ np.linalg.matrix_power(cycle, 2) @ embedding


def oriented_cycle_basis() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    projectors = projected_scalar_projectors()
    cycle = projected_forward_cycle()
    return tuple(projector @ cycle for projector in projectors)


def _as_complex_3x3(a: np.ndarray) -> np.ndarray:
    matrix = np.asarray(a, dtype=complex)
    if matrix.shape != (3, 3):
        raise ValueError(f"expected a supplied 3x3 matrix, got shape {matrix.shape}")
    return matrix


def oriented_cycle_coeffs_from_block(a: np.ndarray) -> np.ndarray:
    """Hilbert--Schmidt coordinates on the supplied forward-cycle basis."""
    matrix = _as_complex_3x3(a)
    return np.diag(matrix @ projected_forward_cycle().conj().T)


def forward_cycle_projection(a: np.ndarray) -> np.ndarray:
    """Orthogonal projection onto span(E12,E23,E31)."""
    matrix = _as_complex_3x3(a)
    coeffs = oriented_cycle_coeffs_from_block(matrix)
    basis = oriented_cycle_basis()
    return sum((coefficient * vector for coefficient, vector in zip(coeffs, basis)), np.zeros((3, 3), dtype=complex))


def explicit_forward_cycle_slots(a: np.ndarray) -> np.ndarray:
    matrix = _as_complex_3x3(a)
    return matrix[0, 1] * E12 + matrix[1, 2] * E23 + matrix[2, 0] * E31


def generic_test_matrices() -> tuple[np.ndarray, ...]:
    fixed = np.array(
        [
            [1.2 + 0.3j, -0.7 + 1.1j, 2.4 - 0.2j],
            [0.6 - 0.9j, -1.5 + 0.4j, 0.8 + 0.5j],
            [-1.1 + 0.2j, 1.7 - 0.6j, 0.3 - 1.4j],
        ],
        dtype=complex,
    )
    second = np.array(
        [
            [-0.25 + 0.75j, 2.0 - 1.0j, -1.2 + 0.4j],
            [1.3 + 0.8j, 0.5 - 0.2j, -0.9 - 1.7j],
            [0.45 + 1.25j, -2.2 + 0.1j, 1.1 + 0.6j],
        ],
        dtype=complex,
    )
    rng = np.random.default_rng(731_903)
    seeded = tuple(
        rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        for _ in range(3)
    )
    return (fixed, second, *seeded)


def part0_source_scope_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE SCOPE FIREWALL")
    print("=" * 88)

    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "**Claim type:** bounded_theorem",
        "supplied complex `3 x 3` matrix `A`",
        "The title, theorem, and runner do not interpret `c` as a physical observable",
        "consistency-only",
        "remaining `missing_bridge_theorem` is explicit",
        "Record-compatible physical observable/readout map",
        "framework construction identifying which matrix-valued block is `A`",
        "separate state, parameter, or selector law fixing the numerical cycle",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note states scope phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "exact " + "native observable/value law",
        "remaining positive carrier on the retained PMNS active class",
        "equips the oriented cycle channel with a " + "native observable law",
        "same values are read from the lower-level active response profile",
    ]
    for phrase in forbidden_note_phrases:
        check(f"source note excludes stale overclaim: {phrase}", phrase not in note)

    forbidden_runner_imports = [
        "active_" + "operator",
        "sector_operator_" + "fixture_from_effective_block",
        "active_response_columns_" + "from_sector_operator",
        "derive_active_block_" + "from_response_columns",
    ]
    for symbol in forbidden_runner_imports:
        check(f"runner excludes target-derived fixture helper: {symbol}", symbol not in source)

    check("runner failure status is nonzero when failures exist", result_exit_code(1) != 0)
    check("runner success status is zero when no failures exist", result_exit_code(0) == 0)
    check("stable claim id is preserved", CLAIM_ID == "pmns_oriented_cycle_channel_value_law_note")


def part1_supplied_projected_cycle_and_basis_identities() -> None:
    print("\n" + "=" * 88)
    print("PART 1: SUPPLIED PROJECTED-CYCLE AND BASIS IDENTITIES")
    print("=" * 88)

    embedding = supplied_triplet_embedding()
    cycle8 = supplied_cycle_representation()
    q1, q2, q3 = projected_scalar_projectors()
    c = projected_forward_cycle()
    b1, b2, b3 = oriented_cycle_basis()

    check("The supplied triplet embedding is isometric", np.linalg.norm(embedding.conj().T @ embedding - I3) < TOL)
    check("The supplied 8x8 cycle representation is unitary", np.linalg.norm(cycle8.conj().T @ cycle8 - np.eye(8)) < TOL)
    check("The supplied 8x8 cycle representation has order three", np.linalg.norm(np.linalg.matrix_power(cycle8, 3) - np.eye(8)) < TOL)
    check("The supplied compression identity gives C", np.linalg.norm(c - CYCLE) < TOL, f"error={np.linalg.norm(c - CYCLE):.2e}")
    check("The projected coordinate projectors are E11,E22,E33",
          np.linalg.norm(q1 - E11) < TOL and np.linalg.norm(q2 - E22) < TOL and np.linalg.norm(q3 - E33) < TOL)
    check("The projected coordinate projectors are mutually orthogonal",
          all(np.linalg.norm(left @ right) < TOL for i, left in enumerate((q1, q2, q3)) for j, right in enumerate((q1, q2, q3)) if i != j))
    check("The projected coordinate projectors resolve I3", np.linalg.norm(q1 + q2 + q3 - I3) < TOL)
    check("P1 C = E12", np.linalg.norm(b1 - E12) < TOL)
    check("P2 C = E23", np.linalg.norm(b2 - E23) < TOL)
    check("P3 C = E31", np.linalg.norm(b3 - E31) < TOL)

    gram = np.array([[np.trace(left.conj().T @ right) for right in (b1, b2, b3)] for left in (b1, b2, b3)])
    check("The ordered edge basis is Hilbert--Schmidt orthonormal", np.linalg.norm(gram - I3) < TOL)


def part2_generic_complex_matrix_coordinate_extraction() -> None:
    print("\n" + "=" * 88)
    print("PART 2: GENERIC COMPLEX-MATRIX COORDINATE EXTRACTION")
    print("=" * 88)

    basis = oriented_cycle_basis()
    matrix_units = tuple(e(i, j) for i in range(3) for j in range(3))
    expected_unit_coeffs = tuple(
        np.array([unit[0, 1], unit[1, 2], unit[2, 0]], dtype=complex)
        for unit in matrix_units
    )
    check(
        "all nine standard matrix units obey the coordinate and projection identities",
        all(
            np.linalg.norm(oriented_cycle_coeffs_from_block(unit) - expected) < TOL
            and np.linalg.norm(forward_cycle_projection(unit) - explicit_forward_cycle_slots(unit)) < TOL
            for unit, expected in zip(matrix_units, expected_unit_coeffs)
        ),
    )

    for index, matrix in enumerate(generic_test_matrices(), start=1):
        coeffs = oriented_cycle_coeffs_from_block(matrix)
        slots = np.array([matrix[0, 1], matrix[1, 2], matrix[2, 0]], dtype=complex)
        traces = np.array([np.trace(vector.conj().T @ matrix) for vector in basis], dtype=complex)
        rebuilt = forward_cycle_projection(matrix)
        expected = explicit_forward_cycle_slots(matrix)
        residual = matrix - rebuilt
        residual_coordinates = np.array([np.trace(vector.conj().T @ residual) for vector in basis], dtype=complex)

        check(f"matrix {index}: diag(A C^dagger) extracts A12,A23,A31",
              np.linalg.norm(coeffs - slots) < TOL,
              f"error={np.linalg.norm(coeffs - slots):.2e}")
        check(f"matrix {index}: trace coordinates equal diag(A C^dagger)",
              np.linalg.norm(traces - coeffs) < TOL,
              f"error={np.linalg.norm(traces - coeffs):.2e}")
        check(f"matrix {index}: basis reconstruction equals the explicit forward-cycle slots",
              np.linalg.norm(rebuilt - expected) < TOL,
              f"error={np.linalg.norm(rebuilt - expected):.2e}")
        check(f"matrix {index}: reconstruction residual is orthogonal to the cycle basis",
              np.linalg.norm(residual_coordinates) < TOL,
              f"error={np.linalg.norm(residual_coordinates):.2e}")


def part3_projection_identities() -> None:
    print("\n" + "=" * 88)
    print("PART 3: FORWARD-CYCLE PROJECTION IDENTITIES")
    print("=" * 88)

    a, b = generic_test_matrices()[:2]
    alpha = 0.7 - 0.4j
    beta = -1.2 + 0.3j
    projected_a = forward_cycle_projection(a)
    projected_b = forward_cycle_projection(b)
    projected_combo = forward_cycle_projection(alpha * a + beta * b)

    check("The forward-cycle projection is complex-linear",
          np.linalg.norm(projected_combo - alpha * projected_a - beta * projected_b) < TOL)
    check("The forward-cycle projection is idempotent",
          np.linalg.norm(forward_cycle_projection(projected_a) - projected_a) < TOL)
    check("The extracted coordinates reconstruct every basis vector",
          all(np.linalg.norm(forward_cycle_projection(vector) - vector) < TOL for vector in oriented_cycle_basis()))
    check("A matrix with no E12,E23,E31 entries projects to zero",
          np.linalg.norm(forward_cycle_projection(np.diag([1 + 2j, -3 + 0.5j, 4 - 1j]))) < TOL)


def part4_hostile_wrong_cycle_and_wrong_basis_controls() -> None:
    print("\n" + "=" * 88)
    print("PART 4: HOSTILE WRONG-CYCLE AND WRONG-BASIS CONTROLS")
    print("=" * 88)

    matrix = generic_test_matrices()[0]
    correct_coeffs = oriented_cycle_coeffs_from_block(matrix)
    correct_projection = explicit_forward_cycle_slots(matrix)

    wrong_cycle = CYCLE.conj().T
    wrong_cycle_coeffs = np.diag(matrix @ wrong_cycle.conj().T)
    check("Using the reverse cycle fails to extract the forward-cycle coordinates",
          np.linalg.norm(wrong_cycle_coeffs - correct_coeffs) > 1.0e-6,
          f"|delta|={np.linalg.norm(wrong_cycle_coeffs - correct_coeffs):.6f}")

    reversed_basis = (e(0, 2), e(1, 0), e(2, 1))
    wrong_basis_coeffs = np.array([np.trace(vector.conj().T @ matrix) for vector in reversed_basis], dtype=complex)
    check("Using the reverse-edge basis fails to extract A12,A23,A31",
          np.linalg.norm(wrong_basis_coeffs - correct_coeffs) > 1.0e-6,
          f"|delta|={np.linalg.norm(wrong_basis_coeffs - correct_coeffs):.6f}")

    permuted_basis = (E23, E31, E12)
    wrong_reconstruction = sum(
        (coefficient * vector for coefficient, vector in zip(correct_coeffs, permuted_basis)),
        np.zeros((3, 3), dtype=complex),
    )
    check("Keeping the coordinates but permuting the ordered basis breaks reconstruction",
          np.linalg.norm(wrong_reconstruction - correct_projection) > 1.0e-6,
          f"|delta|={np.linalg.norm(wrong_reconstruction - correct_projection):.6f}")

    malformed_ok = False
    try:
        oriented_cycle_coeffs_from_block(np.eye(4, dtype=complex))
    except ValueError:
        malformed_ok = True
    check("The extractor rejects a matrix outside the stated 3x3 scope", malformed_ok)


def part5_result() -> None:
    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Bounded algebraic oriented-cycle coordinate-extraction lemma:")
    print("    - the supplied finite projection gives C and E12,E23,E31")
    print("    - diag(A C^dagger) gives the exact coordinates for any supplied")
    print("      complex 3x3 matrix A")
    print("    - those coordinates reconstruct exactly the orthogonal forward-cycle")
    print("      projection of A")
    print()
    print("  No physical carrier, Record readout, A-selection, or value-selection")
    print("  bridge is supplied. Any response-fixture round trip is consistency-only.")


def main() -> int:
    print("=" * 88)
    print("ORIENTED-CYCLE COORDINATE-EXTRACTION LEMMA")
    print("=" * 88)
    print()
    print("Scope:")
    print("  Exact finite matrix algebra for a supplied complex 3x3 block.")

    part0_source_scope_firewall()
    part1_supplied_projected_cycle_and_basis_identities()
    part2_generic_complex_matrix_coordinate_extraction()
    part3_projection_identities()
    part4_hostile_wrong_cycle_and_wrong_basis_controls()
    part5_result()

    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return result_exit_code(FAIL_COUNT)


if __name__ == "__main__":
    sys.exit(main())
