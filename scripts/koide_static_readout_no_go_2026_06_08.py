#!/usr/bin/env python3
"""Aggregate runner for the tested static-readout Koide no-go.

Runs the two component checks that carry the claim:

* the rank-2 sesquilinear-modulus wall; and
* the measure-neutrality of the native complex structure J_cs.
"""

from __future__ import annotations

import koide_jcs_measure_neutral_2026_06_08 as jcs
import koide_polarization_wall_verification_2026_06_08 as wall


def n5_execution_certificate() -> None:
    """Granularity report for the aggregate. Prints only; no check, no count."""
    print("N5 execution certificate: what this aggregate runner resolves")
    print("=" * 78)
    print(
        "  per_element: resolved in the J_cs component, where the operators are small "
        "explicit real 3x3 matrices and the claims are entrywise. J_cs is required to equal "
        "minus its own transpose, J_cs^2 + (I - P_triv) is required to vanish as a matrix, "
        "and the two commutators that make J_cs C-linear on the generation matrix, "
        "[J_cs, C] and [J_cs, M] for a circulant M, are both required to be the zero matrix "
        "rather than merely small."
    )
    print(
        "  per_site: checked and not executed — neither component constructs a site index, "
        "a neighbour relation or a lattice. Both work on one C_3 generation triplet, which "
        "is where the claim lives: the question is which count a STATIC readout applies to "
        "that single triplet's doublet. The residual opening named by the components is a "
        "dynamical first-order or index realization, not a spatially resolved one."
    )
    print(
        "  per_mode: resolved, and the entire selector is a mode count. The wall component "
        "forms the Hessian of the Coleman-Weinberg modulus over the two real doublet fields "
        "Re b and Im b and finds rank 2 with two strictly positive eigenvalues, then shows "
        "a general smooth f(|b|^2) keeps a generically full-rank Hessian, so the modulus "
        "reading always counts two real modes. The J_cs component supplies the matching "
        "mode picture from the other side, spectrum {0, +i, -i}: a zero mode on the trivial "
        "isotype and a conjugate pair on the doublet."
    )
    print(
        "  per_block: resolved — the singlet and doublet blocks are carried with separate "
        "weights throughout. The wall component assigns (w_s, w_d) to the two block "
        "energies 3 a^2 and 6 |b|^2, derives the singlet fraction x = w_s/(w_s + w_d) and "
        "the stationary relation r = (1 - x)/(2 x), and evaluates it at three block "
        "weightings: (1, 2) gives r = 1, (1, 1) gives r = 1/2, and the uniform complex "
        "recount (1/2, 1) gives r = 1 again. The block split is also what J_cs^2 = "
        "-(I - P_triv) exhibits directly."
    )
    print(
        "  lattice_wide: checked and not executed — no volume, sum over sites or limit is "
        "formed, and neither half of the claim would gain from one. The wall is a rank "
        "statement about a 2x2 Hessian, which is a pointwise algebraic fact, and the "
        "measure-neutrality is an exact invariance, with the eigenvalue magnitudes, |det M| "
        "and the M^dag M spectrum all unchanged across the sampled flow parameters. A "
        "quantity that is already invariant at a point stays invariant under any aggregation."
    )


def main() -> int:
    print("=" * 78)
    print("Koide tested static-readout no-go aggregate runner")
    print("=" * 78)
    print()
    wall_rc = wall.main()
    print()
    print("-" * 78)
    print()
    jcs_rc = jcs.main()
    total_pass = wall.PASS + jcs.PASS
    total_fail = wall.FAIL + jcs.FAIL
    print()
    print("-" * 78)
    print()
    n5_execution_certificate()
    print()
    print("=" * 78)
    print(f"AGGREGATE TOTAL: PASS={total_pass} FAIL={total_fail}")
    print("=" * 78)
    return 0 if wall_rc == 0 and jcs_rc == 0 and total_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
