#!/usr/bin/env python3
"""Exact companion for the C3 body-diagonal fixed-locus density theorem.

The audited algebraic surface is deliberately small: the proper cubic
rotation by 2*pi/3 about the body diagonal, its real two-dimensional normal
plane, and the finite C3 group average of the inverse normal determinant.
No APS/global-PL statement or charged-lepton readout identification is used.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact algebra")
    raise SystemExit(1)


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        mark = f"PASS ({kind})"
    else:
        FAIL += 1
        mark = f"FAIL ({kind})"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{mark}] {label}{suffix}")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def section(label: str) -> None:
    print()
    print(label)
    print("-" * len(label))


def main() -> int:
    print("=" * 88)
    print("C3 body-diagonal fixed locus and local inverse-determinant density")
    print("=" * 88)

    section("Part A: proper cubic body-diagonal rotation")
    permutation = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    identity3 = sp.eye(3)
    check(
        "the cyclic axis map is an orientation-preserving orthogonal matrix",
        permutation.T * permutation == identity3 and permutation.det() == 1,
    )
    check(
        "the cyclic axis map has exact order three",
        permutation**3 == identity3 and permutation != identity3,
    )

    axis = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    cross = sp.Matrix(
        [
            [0, -axis[2], axis[1]],
            [axis[2], 0, -axis[0]],
            [-axis[1], axis[0], 0],
        ]
    )
    angle = 2 * sp.pi / 3
    rodrigues = sp.simplify(
        sp.cos(angle) * identity3
        + sp.sin(angle) * cross
        + (1 - sp.cos(angle)) * axis * axis.T
    )
    check(
        "Rodrigues rotation by 2*pi/3 about (1,1,1) equals the cyclic axis map",
        matrix_zero(rodrigues - permutation),
    )

    x = sp.symbols("x")
    characteristic = sp.expand((permutation - x * identity3).det())
    check(
        "the characteristic polynomial is 1-x^3",
        sp.simplify(characteristic - (1 - x**3)) == 0,
        detail=f"det(P-xI)={characteristic}",
    )
    check(
        "the fixed subspace is the one-dimensional body diagonal",
        (permutation - identity3).rank() == 2
        and matrix_zero(permutation * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1])),
    )

    section("Part B: exact real normal-plane determinant")
    normal_basis = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
    gram = normal_basis.T * normal_basis
    check(
        "the two displayed vectors span the body-diagonal orthogonal plane",
        normal_basis.rank() == 2
        and matrix_zero(sp.Matrix([[1, 1, 1]]) * normal_basis),
    )

    # Solve P B = B N for the exact matrix N of P on the real normal plane.
    normal_action = gram.inv() * normal_basis.T * permutation * normal_basis
    check(
        "the normal-plane action is exact and preserves the induced metric",
        matrix_zero(permutation * normal_basis - normal_basis * normal_action)
        and matrix_zero(normal_action.T * gram * normal_action - gram),
        detail=f"N={normal_action}",
    )
    normal_characteristic = sp.expand((normal_action - x * sp.eye(2)).det())
    check(
        "the normal-plane characteristic polynomial is x^2+x+1",
        sp.simplify(normal_characteristic - (x**2 + x + 1)) == 0,
        detail=f"det(N-xI)={normal_characteristic}",
    )

    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    omega_bar = sp.conjugate(omega)
    check(
        "the complexified normal eigenvalues are the conjugate weights omega and omega^2",
        sp.simplify(omega**3 - 1) == 0
        and sp.simplify(omega_bar - omega**2) == 0
        and sp.simplify(omega * omega_bar - 1) == 0,
    )
    determinant_k1 = sp.simplify((sp.eye(2) - normal_action).det())
    determinant_k2 = sp.simplify((sp.eye(2) - normal_action**2).det())
    check(
        "both nonidentity C3 elements have real normal determinant three",
        determinant_k1 == 3 and determinant_k2 == 3,
        detail=f"det(I-N)={determinant_k1}, det(I-N^2)={determinant_k2}",
    )
    check(
        "the complex eigenvalue product reproduces det_R(I-N)=3",
        sp.simplify((1 - omega) * (1 - omega_bar) - 3) == 0,
    )

    section("Part C: finite C3 inverse-determinant density")
    density = sp.simplify(
        sp.Rational(1, 3)
        * (sp.Rational(1, determinant_k1) + sp.Rational(1, determinant_k2))
    )
    check(
        "the group-averaged inverse normal determinant is 2/9",
        density == sp.Rational(2, 9),
        detail=f"L=(1/3)(1/{determinant_k1}+1/{determinant_k2})={density}",
    )
    check(
        "the density is real, positive, and invariant under reversing the C3 generator",
        density.is_real is True
        and density > 0
        and determinant_k1 == determinant_k2,
    )

    check(
        "the computed fixed-locus density has no free parameters",
        density.free_symbols == set(),
    )

    section("Scope guard")
    note_path = (
        Path(__file__).resolve().parents[1]
        / "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
    )
    note = note_path.read_text(encoding="utf-8")
    normalized_note = " ".join(note.split())
    stale_link_targets = (
        "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md",
        "THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md",
        "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md",
        "HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md",
        "KOIDE_RETAINED_WILSON_APS_SCALAR_ACTION_ON_RANK_TWO_MULTIPLICITY_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "S3_GENERAL_R_DERIVATION_NOTE.md",
    )
    check(
        "source note has no load-bearing links to the former seven-row supplier stack",
        all(f"]({target})" not in note for target in stale_link_targets),
        kind="B",
    )
    check(
        "source note excludes physical R-eta and charged-lepton angle identification",
        "does not identify this number with a physical charged-lepton angle"
        in normalized_note,
        kind="B",
    )

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
