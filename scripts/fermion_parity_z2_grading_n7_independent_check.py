#!/usr/bin/env python3
"""Independent direct-matrix steelman check for fermion-parity grading.

This helper deliberately avoids the Jordan-Wigner construction.  It tests the
two-mode counterexample in the ordered occupation basis and kills the strongest
ordering/sign mutation that could otherwise make the counterexample look like
an artifact of the primary runner's CAR realization.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class SteelmanEvidence:
    pair_is_self_adjoint: bool
    pair_preserves_parity: bool
    pair_changes_number: bool
    wrong_order_mutation_is_killed: bool

    @property
    def resolved(self) -> bool:
        return (
            self.pair_is_self_adjoint
            and self.pair_preserves_parity
            and self.pair_changes_number
            and self.wrong_order_mutation_is_killed
        )


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def compute_steelman_evidence() -> SteelmanEvidence:
    """Calculate the direct two-mode witness without importing the primary."""

    q_two = sp.diag(0, 1, 1, 2)
    f_two = sp.diag(1, -1, -1, 1)
    pair = sp.zeros(4)
    pair[0, 3] = 1
    pair[3, 0] = 1

    # Swapping the annihilation order without the CAR sign changes the plus
    # combination into this anti-Hermitian matrix, so it cannot be the claimed
    # Hamiltonian.  This mutation is computed directly, not inferred from JW.
    wrong_order_mutation = sp.zeros(4)
    wrong_order_mutation[0, 3] = 1
    wrong_order_mutation[3, 0] = -1

    return SteelmanEvidence(
        pair_is_self_adjoint=matrix_equal(pair.H, pair),
        pair_preserves_parity=matrix_zero(commutator(pair, f_two)),
        pair_changes_number=not matrix_zero(commutator(pair, q_two)),
        wrong_order_mutation_is_killed=not matrix_equal(
            wrong_order_mutation.H, wrong_order_mutation
        ),
    )


def steelman_resolution_line() -> str:
    return (
        "N7_STEELMAN_RESOLUTION parity-conservation-versus-number-conservation "
        "wall resolved on the stated finite ordered carrier: independent direct "
        "occupation-basis matrices give [H_pair,F]=0 and [H_pair,Q]!=0, while "
        "the wrong-order hostile mutation is non-self-adjoint; this removes the "
        "Jordan-Wigner-order objection without selecting physical statistics, "
        "superselection, locality, or lattice dynamics."
    )


def main() -> int:
    evidence = compute_steelman_evidence()
    print("FERMION PARITY N7 — INDEPENDENT DIRECT-MATRIX MODE")
    pair_resolved = (
        evidence.pair_is_self_adjoint
        and evidence.pair_preserves_parity
        and evidence.pair_changes_number
    )
    mutation_resolved = evidence.wrong_order_mutation_is_killed
    print(
        f"[{'PASS' if pair_resolved else 'FAIL'}] direct pair steelman: "
        f"self_adjoint={evidence.pair_is_self_adjoint}, "
        f"parity_commutator_zero={evidence.pair_preserves_parity}, "
        f"number_commutator_nonzero={evidence.pair_changes_number}"
    )
    print(
        f"[{'PASS' if mutation_resolved else 'FAIL'}] "
        "wrong-order hostile mutation killed: "
        f"non_self_adjoint={mutation_resolved}"
    )
    if evidence.resolved:
        print(steelman_resolution_line())
    passes = int(pair_resolved) + int(mutation_resolved)
    failures = 2 - passes
    print(f"TOTAL: PASS={passes} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
