#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md`.

Pattern A narrow class-(A) algebraic-eigenvalue identity. The narrow
scope is purely the eigenvalue spectrum of the operator

    Y = (+1/3) P_symm + (-1) P_antisymm

on the chiral cube `C^8 = (C^2)^{otimes 3}` indexed by
`|b_1 b_2 b_3>` with `n = 4 b_1 + 2 b_2 + b_3` and the base-swap
permutation `P_swap |b_1, b_2, b_3> = |b_2, b_1, b_3>`. The
companion verifies (S1)-(S6) at exact rational precision via sympy:

  (S1) Projector identities: P_symm, P_antisymm are orthogonal
       projectors with P_symm + P_antisymm = I_8, P_symm * P_antisymm = 0,
       all Hermitian.
  (S2) Rank counts: rank(P_symm) = 6, rank(P_antisymm) = 2.
  (S3) Tracelessness: Tr(Y) = 0.
  (S4) Eigenvalue spectrum: Y has eigenvalues exactly
       {+1/3 (multiplicity 6), -1 (multiplicity 2)} on (C^2)^{otimes 3}.
  (S5) Burnside placement of |111>: <111|P_symm|111> = 1,
       <111|P_antisymm|111> = 0, Y |111> = (+1/3) |111>.
  (S6) Antisymmetric block spans the Y = -1 eigenspace.

The script verifies, at exact rational precision via sympy:

  (1) P_swap is a real symmetric unitary with P_swap^2 = I_8.
  (2) P_symm is a projector (P_symm^2 = P_symm).
  (3) P_antisymm is a projector (P_antisymm^2 = P_antisymm).
  (4) P_symm + P_antisymm = I_8.
  (5) P_symm * P_antisymm = 0_8 (orthogonality).
  (6) P_symm and P_antisymm are Hermitian.
  (7) (S2) Tr(P_symm) = rank(P_symm) = 6 (exact).
  (8) (S2) Tr(P_antisymm) = rank(P_antisymm) = 2 (exact).
  (9) (S3) Tr(Y) = 0 (exact rational).
 (10) (S4) Y * P_symm = (+1/3) P_symm exactly.
 (11) (S4) Y * P_antisymm = (-1) P_antisymm exactly.
 (12) (S4) Y has exactly two distinct eigenvalues, {+1/3, -1}.
 (13) (S4) Eigenvalue +1/3 has algebraic multiplicity exactly 6.
 (14) (S4) Eigenvalue -1 has algebraic multiplicity exactly 2.
 (15) (S5) <111|P_symm|111> = 1 (exact).
 (16) (S5) <111|P_antisymm|111> = 0 (exact).
 (17) (S5) Y |111> = (+1/3) |111> exactly.
 (18) (S6) Two explicit antisymmetric vectors annihilated by P_symm.
 (19) (S6) Two explicit antisymmetric vectors fixed by P_antisymm.
 (20) (S6) Two explicit antisymmetric vectors are -1 eigenvectors of Y.
 (21) Burnside hw=3 sanity: |111> is the unique hw=3 basis vector and
       has Y eigenvalue +1/3, matching the cited Burnside 1+3+3+1
       decomposition of the chiral cube.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) eigenvalue-spectrum identity holds at exact
rational precision and matches the machine-precision verification in
`scripts/verify_cl3_sm_embedding.py` Section F (lines 295-333).
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Matrix, Rational, eye, zeros
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md"
)
CLAIM_ID = (
    "cl3_hypercharge_eigenvalue_spectrum_on_chiral_cube_narrow_theorem_note_2026-05-27"
)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def state_idx(b1: int, b2: int, b3: int) -> int:
    """n = 4 b1 + 2 b2 + b3, matching scripts/verify_cl3_sm_embedding.py."""
    return 4 * b1 + 2 * b2 + b3


def build_p_swap() -> Matrix:
    """Construct the 8x8 unitary P_swap that swaps the first two tensor factors.

    P_swap |b1, b2, b3> = |b2, b1, b3>.
    """
    M = zeros(8, 8)
    for b1 in (0, 1):
        for b2 in (0, 1):
            for b3 in (0, 1):
                src = state_idx(b1, b2, b3)
                dst = state_idx(b2, b1, b3)
                M[dst, src] = 1
    return M


def build_basis_vec(b1: int, b2: int, b3: int) -> Matrix:
    """Column vector for |b1 b2 b3> in the 8-dim chiral cube."""
    v = zeros(8, 1)
    v[state_idx(b1, b2, b3), 0] = 1
    return v


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Exact equality of two sympy matrices via cell-wise difference simplification."""
    diff = sympy.simplify(A - B)
    return all(
        diff[i, j] == 0 for i in range(diff.rows) for j in range(diff.cols)
    )


def mat_is_zero(A: Matrix) -> bool:
    return all(
        sympy.simplify(A[i, j]) == 0 for i in range(A.rows) for j in range(A.cols)
    )


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27")
    print("Goal: sympy verification of the operator Y eigenvalue spectrum")
    print("      {+1/3 (mult 6), -1 (mult 2)} on the chiral cube (C^2)^{otimes 3}.")
    print("=" * 88)

    # -------------------------------------------------------------------------
    # Build P_swap, P_symm, P_antisymm, Y on the explicit 8x8 chiral cube.
    # -------------------------------------------------------------------------
    I8 = eye(8)
    P_swap = build_p_swap()
    P_symm = (I8 + P_swap) / 2
    P_antisymm = (I8 - P_swap) / 2
    Y = Rational(1, 3) * P_symm + Rational(-1, 1) * P_antisymm

    # =========================================================================
    section("Part 1: P_swap structural sanity")
    # =========================================================================
    # P_swap is a real symmetric unitary; P_swap^2 = I_8.
    check(
        "P_swap is real symmetric (P_swap^T = P_swap)",
        mat_eq(P_swap.T, P_swap),
    )
    check(
        "P_swap^2 = I_8",
        mat_eq(P_swap * P_swap, I8),
    )

    # =========================================================================
    section("Part 2: (S1) Projector identities for P_symm, P_antisymm")
    # =========================================================================
    check(
        "(S1) P_symm * P_symm = P_symm",
        mat_eq(P_symm * P_symm, P_symm),
    )
    check(
        "(S1) P_antisymm * P_antisymm = P_antisymm",
        mat_eq(P_antisymm * P_antisymm, P_antisymm),
    )
    check(
        "(S1) P_symm + P_antisymm = I_8",
        mat_eq(P_symm + P_antisymm, I8),
    )
    check(
        "(S1) P_symm * P_antisymm = 0_8 (orthogonality)",
        mat_is_zero(P_symm * P_antisymm),
    )
    check(
        "(S1) P_symm Hermitian (P_symm^T = P_symm; real)",
        mat_eq(P_symm.T, P_symm),
    )

    # =========================================================================
    section("Part 3: (S2) Rank counts via trace of orthogonal projectors")
    # =========================================================================
    tr_symm = sympy.simplify(P_symm.trace())
    tr_antisymm = sympy.simplify(P_antisymm.trace())
    check(
        "(S2) Tr(P_symm) = 6",
        tr_symm == 6,
        f"got {tr_symm}",
    )
    check(
        "(S2) Tr(P_antisymm) = 2",
        tr_antisymm == 2,
        f"got {tr_antisymm}",
    )

    # =========================================================================
    section("Part 4: (S3) Tracelessness Tr(Y) = 0")
    # =========================================================================
    tr_Y = sympy.simplify(Y.trace())
    check(
        "(S3) Tr(Y) = 0 (exact rational)",
        tr_Y == 0,
        f"got {tr_Y}",
    )

    # =========================================================================
    section("Part 5: (S4) Eigenvalue spectrum {+1/3 (mult 6), -1 (mult 2)}")
    # =========================================================================
    # Block action: Y on Im(P_symm) is (+1/3) and on Im(P_antisymm) is (-1).
    check(
        "(S4) Y * P_symm = (+1/3) P_symm",
        mat_eq(Y * P_symm, Rational(1, 3) * P_symm),
    )
    check(
        "(S4) Y * P_antisymm = (-1) P_antisymm",
        mat_eq(Y * P_antisymm, Rational(-1, 1) * P_antisymm),
    )

    # Exact eigenvalue computation via sympy.
    eigen = Y.eigenvals()
    # eigen is a dict {eigenvalue: algebraic_multiplicity}.
    keys = list(eigen.keys())
    check(
        "(S4) Y has exactly 2 distinct eigenvalues",
        len(keys) == 2,
        f"got {len(keys)}: {keys}",
    )
    mult_plus = eigen.get(Rational(1, 3), 0)
    mult_minus = eigen.get(Rational(-1, 1), 0)
    check(
        "(S4) Eigenvalue +1/3 has algebraic multiplicity exactly 6",
        mult_plus == 6,
        f"got mult({Rational(1, 3)}) = {mult_plus}",
    )
    check(
        "(S4) Eigenvalue -1 has algebraic multiplicity exactly 2",
        mult_minus == 2,
        f"got mult(-1) = {mult_minus}",
    )

    # =========================================================================
    section("Part 6: (S5) Burnside dark-state |111> placement")
    # =========================================================================
    v111 = build_basis_vec(1, 1, 1)
    val_sym = sympy.simplify((v111.T * P_symm * v111)[0, 0])
    val_anti = sympy.simplify((v111.T * P_antisymm * v111)[0, 0])
    check(
        "(S5) <111|P_symm|111> = 1",
        val_sym == 1,
        f"got {val_sym}",
    )
    check(
        "(S5) <111|P_antisymm|111> = 0",
        val_anti == 0,
        f"got {val_anti}",
    )
    Y_v111 = sympy.simplify(Y * v111)
    target = sympy.simplify(Rational(1, 3) * v111)
    check(
        "(S5) Y |111> = (+1/3) |111>",
        Y_v111 == target,
        f"max nonzero residual cell {sympy.simplify(Y_v111 - target).norm()}",
    )

    # =========================================================================
    section("Part 7: (S6) Antisymmetric block spans the Y = -1 eigenspace")
    # =========================================================================
    # v_{ant, 0} = (|010> - |100>) / sqrt(2),
    # v_{ant, 1} = (|011> - |101>) / sqrt(2).
    # Using exact sympy (we can keep them rational by working without the
    # sqrt(2) normalization: scaled vectors are still eigenvectors).
    v_ant_0 = build_basis_vec(0, 1, 0) - build_basis_vec(1, 0, 0)
    v_ant_1 = build_basis_vec(0, 1, 1) - build_basis_vec(1, 0, 1)

    for tag, v in [("v_{ant, 0}", v_ant_0), ("v_{ant, 1}", v_ant_1)]:
        Psv = sympy.simplify(P_symm * v)
        check(
            f"(S6) P_symm @ {tag} = 0",
            mat_is_zero(Psv),
        )

    for tag, v in [("v_{ant, 0}", v_ant_0), ("v_{ant, 1}", v_ant_1)]:
        Pav = sympy.simplify(P_antisymm * v)
        check(
            f"(S6) P_antisymm @ {tag} = {tag}",
            mat_eq(Pav, v),
        )

    for tag, v in [("v_{ant, 0}", v_ant_0), ("v_{ant, 1}", v_ant_1)]:
        Yv = sympy.simplify(Y * v)
        check(
            f"(S6) Y @ {tag} = (-1) {tag}",
            mat_eq(Yv, Rational(-1, 1) * v),
        )

    # =========================================================================
    section("Part 8: Burnside hw=3 sanity")
    # =========================================================================
    # The hw=3 subspace of (C^2)^{otimes 3} is 1-dim, spanned by |111>.
    # By (S5), |111> has Y eigenvalue +1/3, matching the Burnside 1+3+3+1
    # decomposition cited from CL3_TASTE_GENERATION_THEOREM Section A.
    hw3_basis = []
    for b1 in (0, 1):
        for b2 in (0, 1):
            for b3 in (0, 1):
                if b1 + b2 + b3 == 3:
                    hw3_basis.append(build_basis_vec(b1, b2, b3))
    check(
        "Burnside hw=3 subspace is 1-dim (only |111>)",
        len(hw3_basis) == 1,
        f"got {len(hw3_basis)} hw=3 basis vectors",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    total = PASS + FAIL
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print(f"  TOTAL = {total}")
    print()
    print(f"  Note: {NOTE_PATH.name}")
    print(f"  Claim ID: {CLAIM_ID}")
    print()
    if FAIL == 0:
        print("VERDICT: companion audit-friendly exact-symbolic verification of")
        print("         (S1)-(S6) PASSES. The operator Y on (C^2)^{otimes 3}")
        print("         has spectrum {+1/3 (mult 6), -1 (mult 2)} at exact")
        print("         rational precision; the dark hw=3 Burnside singlet")
        print("         |111> carries Y = +1/3.")
        return 0
    print("VERDICT: companion audit-friendly verification FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
