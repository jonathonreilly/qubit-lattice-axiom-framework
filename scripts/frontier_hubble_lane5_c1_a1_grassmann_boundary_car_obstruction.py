#!/usr/bin/env python3
"""Lane 5 (C1) A1 Grassmann-to-boundary CAR obstruction verifier.

The audit route A1 asks whether the finite local Grassmann / staggered-Dirac
partition in A_min forces CAR semantics on the rank-four primitive boundary
block P_A H_cell. This runner checks the finite-algebra obstruction:

bulk CAR descends to a projected rank-four block only when the projection is a
reducing Clifford-module morphism for the selected modes. Rank four and bulk
Grassmann/CAR structure alone do not force that property.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


TOL = 1.0e-10


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def kron_all(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for mat in mats[1:]:
        out = np.kron(out, mat)
    return out


def annihilation_operator(n_modes: int, mode: int) -> np.ndarray:
    ident = np.eye(2, dtype=complex)
    z = np.diag([1.0, -1.0]).astype(complex)
    sigma_minus = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    factors: list[np.ndarray] = []
    for idx in range(n_modes):
        if idx < mode:
            factors.append(z)
        elif idx == mode:
            factors.append(sigma_minus)
        else:
            factors.append(ident)
    return kron_all(factors)


def coordinate_projection(indices: list[int], dimension: int) -> np.ndarray:
    projection = np.zeros((dimension, dimension), dtype=complex)
    for idx in indices:
        projection[idx, idx] = 1.0
    return projection


def car_error(ops: list[np.ndarray], identity: np.ndarray) -> float:
    worst = 0.0
    zero = np.zeros_like(identity)
    for i, op_i in enumerate(ops):
        for j, op_j in enumerate(ops):
            anti_creation = op_i @ op_j.conj().T + op_j.conj().T @ op_i
            target = identity if i == j else zero
            worst = max(worst, float(np.linalg.norm(anti_creation - target)))
            anti_annihilation = op_i @ op_j + op_j @ op_i
            worst = max(worst, float(np.linalg.norm(anti_annihilation)))
    return worst


def compressed_ops(projection: np.ndarray, ops: list[np.ndarray]) -> list[np.ndarray]:
    return [projection @ op @ projection for op in ops]


def commutator_error(projection: np.ndarray, ops: list[np.ndarray]) -> float:
    return max(float(np.linalg.norm(projection @ op - op @ projection)) for op in ops)


def spectral_signature(matrix: np.ndarray) -> tuple[float, ...]:
    vals = np.linalg.eigvalsh(matrix)
    return tuple(float(np.round(v, 12)) for v in vals)


def main() -> int:
    checks: list[Check] = []

    dim_bulk = 8
    c0, c1, c2 = [annihilation_operator(3, idx) for idx in range(3)]
    bulk_identity = np.eye(dim_bulk, dtype=complex)
    bulk_error = car_error([c0, c1, c2], bulk_identity)
    checks.append(
        Check(
            "bulk_3_mode_car",
            bulk_error < TOL,
            f"worst CAR residual on F(C^3) = {bulk_error:.3e}",
        )
    )

    # Good projection: third occupation bit fixed. It reduces the c0,c1
    # subalgebra, so the compressed selected modes still obey CAR on the block.
    p_reducing = coordinate_projection([0, 2, 4, 6], dim_bulk)
    reducing_ops = compressed_ops(p_reducing, [c0, c1])
    reducing_car = car_error(reducing_ops, p_reducing)
    reducing_comm = commutator_error(p_reducing, [c0, c1])
    checks.append(
        Check(
            "reducing_projection_preserves_selected_car",
            reducing_car < TOL and reducing_comm < TOL,
            f"CAR residual={reducing_car:.3e}, commutator residual={reducing_comm:.3e}",
        )
    )

    # Bad projection: same rank, same trace, but not a reducing subspace for the
    # selected CAR modes. Compression no longer satisfies CAR on P H.
    p_nonreducing = coordinate_projection([0, 1, 2, 7], dim_bulk)
    nonreducing_ops = compressed_ops(p_nonreducing, [c0, c1])
    nonreducing_car = car_error(nonreducing_ops, p_nonreducing)
    nonreducing_comm = commutator_error(p_nonreducing, [c0, c1])
    checks.append(
        Check(
            "rank_four_projection_need_not_preserve_car",
            nonreducing_car > 1.0 and nonreducing_comm > 1.0,
            f"CAR residual={nonreducing_car:.3e}, commutator residual={nonreducing_comm:.3e}",
        )
    )

    # The same four-dimensional Hilbert space also supports commuting two-qubit
    # semantics with the same parity spectrum, so rank/parity do not select CAR.
    ident = np.eye(2, dtype=complex)
    x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    z = np.diag([1.0, -1.0]).astype(complex)
    x_left = np.kron(x, ident)
    x_right = np.kron(ident, x)
    two_qubit_comm = float(np.linalg.norm(x_left @ x_right - x_right @ x_left))
    two_qubit_anti = float(np.linalg.norm(x_left @ x_right + x_right @ x_left))
    qubit_parity = np.kron(z, z)

    fock_parity = np.diag([1.0, -1.0, -1.0, 1.0]).astype(complex)
    same_parity_spectrum = spectral_signature(qubit_parity) == spectral_signature(fock_parity)
    checks.append(
        Check(
            "same_rank_parity_allows_non_car_two_qubit_semantics",
            two_qubit_comm < TOL and two_qubit_anti > 1.0 and same_parity_spectrum,
            (
                f"commutator={two_qubit_comm:.3e}, anticommutator={two_qubit_anti:.3e}, "
                f"parity spectrum={spectral_signature(qubit_parity)}"
            ),
        )
    )

    # Logical conclusion: A1 requires a projection/morphism theorem, not only
    # the bulk Grassmann partition and rank(P_A)=4.
    exposed_import = nonreducing_car > 1.0 and reducing_car < TOL and same_parity_spectrum
    checks.append(
        Check(
            "a1_exposes_projection_morphism_import",
            exposed_import,
            "Need P_A to reduce the selected Clifford/CAR algebra, or an equivalent module-morphism theorem.",
        )
    )

    print("=" * 78)
    print("Lane 5 (C1) A1 Grassmann-to-boundary CAR obstruction verifier")
    print("=" * 78)
    passed = 0
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"[{status}] {check.name}: {check.detail}")
        passed += int(check.passed)
    failed = len(checks) - passed

    # N5 execution certificate. Print-only: no Check is appended, so the
    # PASS/FAIL tally above is untouched.
    print("-" * 78)
    print("N5 execution certificate: resolution granularity of this CAR obstruction")
    print("-" * 78)
    print(
        "per_element: checked — the two candidate projections differ in nothing but which basis elements "
        "they keep, and that alone flips the result: P_reducing keeps diagonal indices [0, 2, 4, 6] (the "
        "third occupation bit fixed) and P_nonreducing keeps [0, 1, 2, 7], both with exactly four unit "
        f"entries, identical rank and identical trace, yet the compressed CAR residual is "
        f"{reducing_car:.3e} for the first and {nonreducing_car:.3e} for the second. The obstruction is "
        "entirely in the choice of retained basis elements."
    )
    print(
        "per_site: checked and not executed — this runner works inside one cell only; every operator acts "
        f"on the single {dim_bulk}-dimensional Fock space F(C^3) of that cell, and the Jordan-Wigner Z "
        "strings run over the internal mode index, never over a lattice site index, so no site-resolved "
        "or multi-cell statement is made or attempted."
    )
    print(
        "per_mode: checked — the CAR relations are verified pair by pair over the modes rather than in "
        "aggregate: all 9 ordered pairs (i, j) drawn from the three bulk modes are tested for both "
        f"{{c_i, c_j^dagger}} - delta_ij I and {{c_i, c_j}}, giving worst bulk residual {bulk_error:.3e}; "
        f"the compression is then applied to the selected pair c0, c1, whose commutator residual with the "
        f"projection is {reducing_comm:.3e} for the reducing choice and {nonreducing_comm:.3e} for the "
        "non-reducing one."
    )
    print(
        "per_block: checked — three distinct rank-four blocks are compared as whole objects: the reducing "
        "compression which retains CAR, the non-reducing compression of the same rank and trace which "
        f"does not, and a two-qubit block on C^2 tensor C^2 whose generators commute "
        f"(commutator {two_qubit_comm:.3e}) rather than anticommute (anticommutator {two_qubit_anti:.3e}) "
        f"while carrying the identical parity spectrum {spectral_signature(qubit_parity)}. Rank, trace and "
        "parity therefore do not determine the block's algebra."
    )
    print(
        "lattice_wide: checked and not executed — nothing in this runner extends past the single cell: no "
        "cell-to-cell gluing rule, transfer operator, or global Fock space is constructed, and the "
        f"{passed} executed checks already settle the question locally by exhibiting a same-rank "
        "counterexample, so a lattice-wide statement would require the very P_A module-morphism theorem "
        "the note names as missing."
    )

    print("-" * 78)
    print(f"TOTAL: PASS={passed}, FAIL={failed}")
    if failed == 0:
        print(
            "Conclusion: bulk CAR plus rank-four support is insufficient; "
            "A1 needs a P_A module-morphism/reducing-subspace theorem."
        )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
