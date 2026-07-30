#!/usr/bin/env python3
"""Independent N7 carrier check for the Clifford chirality parity theorem.

The primary runner works in a Clifford-basis coefficient system.  This helper
instead builds a faithful odd-dimensional representation by restricting the
standard even-dimensional Pauli-tensor tower.  The omitted final generator is
the strongest hostile-reviewer counterexample: it is a square-normalized
ambient matrix that anticommutes with every represented odd generator.  The
deterministic numerical rank smoke test below checks independently that this
operator is outside the represented internal Clifford-algebra span, so it
does not contradict the source theorem's internal-algebra boundary. The
symbolic proof remains in the source note.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md",
    "scripts/frontier_clifford_chirality_dimension_narrow.py",
)


I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def faithful_odd_generators_with_external(
    n: int,
) -> tuple[list[np.ndarray], np.ndarray]:
    """Restrict the standard Cl(n+1) tower to its first odd n generators."""
    if n < 1 or n % 2 == 0:
        raise ValueError("n must be positive and odd")
    qubits = (n + 1) // 2
    tower: list[np.ndarray] = []
    for mu in range(n + 1):
        site = mu // 2
        local = SIGMA_X if mu % 2 == 0 else SIGMA_Y
        factors = [SIGMA_Z] * site + [local] + [I2] * (qubits - site - 1)
        tower.append(kron_all(factors))
    return tower[:-1], tower[-1]


def internal_basis(generators: list[np.ndarray]) -> list[np.ndarray]:
    """Return every ordered Clifford monomial in the supplied generators."""
    dimension = generators[0].shape[0]
    basis: list[np.ndarray] = []
    for degree in range(len(generators) + 1):
        for subset in combinations(range(len(generators)), degree):
            monomial = np.eye(dimension, dtype=complex)
            for mu in subset:
                monomial = monomial @ generators[mu]
            basis.append(monomial)
    return basis


def flattened_rank(matrices: list[np.ndarray]) -> int:
    """Deterministic numerical SVD rank used only as a finite smoke test."""
    columns = np.column_stack([matrix.reshape(-1) for matrix in matrices])
    return int(np.linalg.matrix_rank(columns, tol=1e-10))


def steelman_resolution_line() -> str:
    return (
        "N7_STEELMAN_RESOLUTION no nonzero `M in Cl(n)` satisfies (5) internal "
        "wall resolved: an independently constructed square-normalized ambient "
        "matrix anticommutes with every odd generator, but adjoining it raises "
        "the faithful internal Clifford-span rank by one; the counterexample is "
        "therefore external to Cl(n), exactly as the theorem's scope requires."
    )


def main() -> int:
    failures = 0
    print("CLIFFORD CHIRALITY N7 -- INDEPENDENT EVEN-TOWER RESTRICTION")
    for n in (1, 3, 5):
        generators, external = faithful_odd_generators_with_external(n)
        dimension = generators[0].shape[0]
        identity = np.eye(dimension, dtype=complex)
        basis = internal_basis(generators)
        internal_rank = flattened_rank(basis)
        augmented_rank = flattened_rank([*basis, external])
        square_ok = np.allclose(external @ external, identity)
        anticommutation_ok = all(
            np.allclose(external @ generator + generator @ external, 0)
            for generator in generators
        )
        faithfulness_ok = internal_rank == 2**n
        outside_ok = augmented_rank == internal_rank + 1
        ok = square_ok and anticommutation_ok and faithfulness_ok and outside_ok
        failures += int(not ok)
        print(
            f"[{'PASS' if ok else 'FAIL'}] odd n={n}: dimension={dimension}, "
            f"numerical_internal_rank={internal_rank}, "
            f"numerical_augmented_rank={augmented_rank}, "
            f"external_square_I={square_ok}, external_anticommutes={anticommutation_ok}"
        )

    if failures == 0:
        print(steelman_resolution_line())
    print(f"TOTAL: PASS={3 - failures} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
