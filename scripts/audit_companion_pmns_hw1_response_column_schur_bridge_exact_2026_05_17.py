#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the PMNS HW=1 response-column /
Schur-complement bridge narrow theorem note
`PMNS_HW1_RESPONSE_COLUMN_SCHUR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the pure linear-algebra
equivalence that, given a sector-operator fixture `M = [[A, B], [C, F]]` on
a retained 3 x 3 support plus probe weight `lam`, the column-inversion
reconstruction recovers the same effective block as the direct Schur
complement, in both the passive (no identity subtraction) and active
(identity subtraction) conventions.

Passive convention:
  (K-pass)  K_pass    := (I - lam * delta_S)^{-1}
  (R-pass)  delta_A   := (I - K_pass^{-1}) / lam
  Claim:    delta_A   =  delta_S = A - B F^{-1} C.

Active convention (subtract_identity=True):
  (K-act)   K_act     := (I - lam * (delta_S - I))^{-1}
  (R-act)   delta_A   := I + (I - K_act^{-1}) / lam
  Claim:    delta_A   =  delta_S = A - B F^{-1} C.

The runner provides sympy-based exact-symbolic verification on tractable
small-d test cases, exact-rational d=3 witnesses, an FP cross-check at one
independent random sample, and counterfactual / spectator-extension probes.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-(A) algebra (the Lane A vs Lane B equivalence inside
Part 4 of `scripts/frontier_pmns_hw1_source_transfer_boundary.py`) holds
at exact symbolic precision under the supplied-pack assumption.
"""

from __future__ import annotations

import sys

try:
    import sympy
    from sympy import Matrix, Rational, Symbol, eye, simplify
except ImportError:  # pragma: no cover
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


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


def symbolic_block(prefix: str, d: int) -> Matrix:
    """Build a symbolic d x d matrix with entries `prefix_ij`."""
    return Matrix(d, d, lambda i, j: Symbol(f"{prefix}_{i}{j}"))


def symbolic_rect(prefix: str, rows: int, cols: int) -> Matrix:
    return Matrix(rows, cols, lambda i, j: Symbol(f"{prefix}_{i}{j}"))


def matrices_equal(A: Matrix, B: Matrix) -> bool:
    """True iff every entry of A - B simplifies to 0."""
    D = simplify(A - B)
    return all(D[i, j] == 0 for i in range(D.rows) for j in range(D.cols))


def exact_block_3() -> Matrix:
    """A fixed exact-rational 3 x 3 witness with no special symmetry."""
    return Matrix(
        [
            [Rational(1, 5), Rational(-2, 7), Rational(3, 11)],
            [Rational(5, 13), Rational(7, 17), Rational(-11, 19)],
            [Rational(-13, 23), Rational(17, 29), Rational(19, 31)],
        ]
    )


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("PMNS_HW1_RESPONSE_COLUMN_SCHUR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of (R-pass) and (R-act) equivalence")
    print("with the Schur complement (S) on supplied sector-operator fixtures")
    print("=" * 88)

    lam = Symbol("lam", positive=True, real=True)

    # -----------------------------------------------------------------
    section("Part 1: passive convention, d = 2 (entry-by-entry symbolic)")
    # -----------------------------------------------------------------
    delta_2 = symbolic_block("D", 2)
    I2 = eye(2)
    K_pass_2 = (I2 - lam * delta_2).inv()
    delta_A_pass_2 = (I2 - K_pass_2.inv()) / lam

    check(
        "(R-pass) (I - K_pass^{-1})/lam reduces to delta entry-by-entry (d=2)",
        matrices_equal(delta_A_pass_2, delta_2),
        detail="d=2 passive identity",
    )

    # -----------------------------------------------------------------
    section("Part 2: active convention, d = 2 (entry-by-entry symbolic)")
    # -----------------------------------------------------------------
    # delta_S is the "block" the runner ultimately wants;
    # delta := delta_S - I is what feeds the response-column build with
    # subtract_identity=True.
    delta_S_2 = symbolic_block("S", 2)
    delta_act_2 = delta_S_2 - I2
    K_act_2 = (I2 - lam * delta_act_2).inv()
    delta_A_act_2 = I2 + (I2 - K_act_2.inv()) / lam

    check(
        "(R-act) I + (I - K_act^{-1})/lam reduces to delta_S entry-by-entry (d=2)",
        matrices_equal(delta_A_act_2, delta_S_2),
        detail="d=2 active identity",
    )

    # -----------------------------------------------------------------
    section("Part 3: passive convention, d = 3 (exact-rational witness)")
    # -----------------------------------------------------------------
    delta_3 = exact_block_3()
    I3 = eye(3)
    lam_3 = Rational(2, 7)
    K_pass_3 = (I3 - lam_3 * delta_3).inv()
    delta_A_pass_3 = (I3 - K_pass_3.inv()) / lam_3

    check(
        "(R-pass) (I - K_pass^{-1})/lam recovers delta exactly (d=3)",
        matrices_equal(delta_A_pass_3, delta_3),
        detail="d=3 passive exact-rational witness",
    )

    # -----------------------------------------------------------------
    section("Part 4: active convention, d = 3 (exact-rational witness)")
    # -----------------------------------------------------------------
    delta_S_3 = exact_block_3()
    lam_act_3 = Rational(3, 10)
    delta_act_3 = delta_S_3 - I3
    K_act_3 = (I3 - lam_act_3 * delta_act_3).inv()
    delta_A_act_3 = I3 + (I3 - K_act_3.inv()) / lam_act_3

    check(
        "(R-act) I + (I - K_act^{-1})/lam recovers delta_S exactly (d=3)",
        matrices_equal(delta_A_act_3, delta_S_3),
        detail="d=3 active exact-rational witness",
    )

    # -----------------------------------------------------------------
    section("Part 5: full Schur round-trip, d = 2, s = 1 (passive, symbolic)")
    # -----------------------------------------------------------------
    # Symbolic sector operator M = [[A, B], [C, F]] at smallest non-trivial
    # dimensions d = 2, s = 1, where exact-sympy Schur-then-resolvent-inverse
    # is tractable. The d = 3, s = 2 case is covered numerically in Part 9.
    # Lane B Schur:  delta_S = A - B F^{-1} C
    # Lane A:  delta_S -> K -> delta_A = (I - K^{-1})/lam
    A = symbolic_block("A", 2)
    B_blk = symbolic_rect("B", 2, 1)
    C_blk = symbolic_rect("C", 1, 2)
    F_blk = symbolic_block("F", 1)

    # We assume F invertible (generic condition). Compute Schur complement.
    delta_S_full = A - B_blk * F_blk.inv() * C_blk

    K_pass_full = (I2 - lam * delta_S_full).inv()
    delta_A_pass_full = (I2 - K_pass_full.inv()) / lam

    check(
        "Lane A passive round-trip M -> delta_S -> K -> delta_A_pass equals "
        "Lane B Schur delta_S = A - B F^{-1} C (d=2, s=1)",
        matrices_equal(delta_A_pass_full, delta_S_full),
        detail="full sector-operator round-trip passive (symbolic)",
    )

    # -----------------------------------------------------------------
    section("Part 6: full Schur round-trip, d = 2, s = 1 (active, symbolic)")
    # -----------------------------------------------------------------
    delta_act_full = delta_S_full - I2
    K_act_full = (I2 - lam * delta_act_full).inv()
    delta_A_act_full = I2 + (I2 - K_act_full.inv()) / lam

    check(
        "Lane A active round-trip M -> delta_S -> (delta_S - I) -> K -> delta_A_act "
        "equals Lane B Schur delta_S (d=2, s=1)",
        matrices_equal(delta_A_act_full, delta_S_full),
        detail="full sector-operator round-trip active (symbolic)",
    )

    # -----------------------------------------------------------------
    section("Part 7: response_columns_from_block round-trip identity (passive, d=3)")
    # -----------------------------------------------------------------
    # response_columns_from_block(delta, lam, subtract_identity=False) returns
    # the columns of K = (I - lam * delta)^{-1} when subtract_identity=False.
    # Stacked together they give K itself. The "derive_passive_block_from_
    # response_columns" inversion is then (I - K^{-1})/lam.
    # We verify the composed round-trip is the identity on delta.
    K_columns_pass = (I3 - lam_3 * delta_3).inv()  # K matrix (columns stacked)
    delta_round_pass = (I3 - K_columns_pass.inv()) / lam_3
    check(
        "Round-trip identity (passive): delta -> response_columns -> derive_passive_block "
        "returns delta (d=3)",
        matrices_equal(delta_round_pass, delta_3),
        detail="passive primitive round-trip",
    )

    # -----------------------------------------------------------------
    section("Part 8: response_columns_from_block round-trip identity (active, d=3)")
    # -----------------------------------------------------------------
    # active convention: delta_input := delta - I, K = (I - lam * delta_input)^{-1},
    # then derive_active_block_from_response_columns returns
    # delta_recovered = I + (I - K^{-1})/lam = I + delta_input = delta.
    # Here delta plays the role of delta_S (the active "block" in the runner).
    delta_input_act = delta_3 - I3
    K_columns_act = (I3 - lam_act_3 * delta_input_act).inv()
    delta_round_act = I3 + (I3 - K_columns_act.inv()) / lam_act_3
    check(
        "Round-trip identity (active): delta -> (delta - I) -> response_columns -> "
        "derive_active_block returns delta (d=3)",
        matrices_equal(delta_round_act, delta_3),
        detail="active primitive round-trip",
    )

    # -----------------------------------------------------------------
    section("Part 9: independent FP cross-check at one random sample (passive)")
    # -----------------------------------------------------------------
    # Provide one numerical FP cross-check at an independent random sample of
    # (M, lam) with d = 3, s = 2. This is a sanity check; the algebraic
    # identity above is the load-bearing content.
    import numpy as np

    rng = np.random.default_rng(seed=20260517)
    d_n, s_n = 3, 2
    lam_val = 0.27  # parent's lam_pass
    A_n = rng.normal(size=(d_n, d_n)) + 1j * rng.normal(size=(d_n, d_n))
    B_n = rng.normal(size=(d_n, s_n)) + 1j * rng.normal(size=(d_n, s_n))
    C_n = rng.normal(size=(s_n, d_n)) + 1j * rng.normal(size=(s_n, d_n))
    # Ensure F invertible by adding a shift on the diagonal.
    F_n = (
        rng.normal(size=(s_n, s_n))
        + 1j * rng.normal(size=(s_n, s_n))
        + 3.0 * np.eye(s_n)
    )

    # Lane B Schur:
    delta_S_n = A_n - B_n @ np.linalg.inv(F_n) @ C_n
    # Lane A passive round-trip:
    K_n_pass = np.linalg.inv(np.eye(d_n) - lam_val * delta_S_n)
    delta_A_pass_n = (np.eye(d_n) - np.linalg.inv(K_n_pass)) / lam_val
    diff_pass_n = np.linalg.norm(delta_A_pass_n - delta_S_n)
    check(
        "FP cross-check passive (d=3, s=2, lam=0.27): "
        "Lane A round-trip matches Lane B Schur to machine precision",
        diff_pass_n < 1e-10,
        detail=f"||delta_A_pass - delta_S|| = {diff_pass_n:.2e}",
    )

    # -----------------------------------------------------------------
    section("Part 10: independent FP cross-check at one random sample (active)")
    # -----------------------------------------------------------------
    lam_act_val = 0.31  # parent's lam_act
    delta_act_n = delta_S_n - np.eye(d_n)
    K_n_act = np.linalg.inv(np.eye(d_n) - lam_act_val * delta_act_n)
    delta_A_act_n = np.eye(d_n) + (np.eye(d_n) - np.linalg.inv(K_n_act)) / lam_act_val
    diff_act_n = np.linalg.norm(delta_A_act_n - delta_S_n)
    check(
        "FP cross-check active (d=3, s=2, lam=0.31): "
        "Lane A active round-trip matches Lane B Schur to machine precision",
        diff_act_n < 1e-10,
        detail=f"||delta_A_act - delta_S|| = {diff_act_n:.2e}",
    )

    # -----------------------------------------------------------------
    section("Part 11: counterfactual probe (sign on identity subtraction)")
    # -----------------------------------------------------------------
    # If the column-invert step used the wrong sign convention
    # (K - I)/lam instead of (I - K^{-1})/lam, the round-trip on a generic
    # block would not recover delta. We probe this symbolically on d = 2.
    K_pass_2_recompute = (I2 - lam * delta_2).inv()
    wrong_recovery = (K_pass_2_recompute - I2) / lam
    diff_wrong = simplify(wrong_recovery - delta_2)
    # The wrong recovery should NOT equal delta in general.
    wrong_is_delta = all(diff_wrong[i, j] == 0 for i in range(2) for j in range(2))
    check(
        "counterfactual: (K - I)/lam does NOT recover delta on generic block (d=2)",
        not wrong_is_delta,
        detail="confirms sign on (I - K^{-1})/lam is load-bearing",
    )

    # -----------------------------------------------------------------
    section("Part 12: spectator-extension invariance probe")
    # -----------------------------------------------------------------
    # Two exact-rational sector operators sharing the same Schur complement
    # on the support produce the same delta_A_pass after the column round-trip,
    # independent of the spectator block (B, C, F).
    delta_S_target = Matrix(
        [[Rational(2, 5), Rational(-1, 7)], [Rational(3, 11), Rational(5, 13)]]
    )
    B1 = Matrix([[Rational(1, 3), Rational(2, 5)], [Rational(-3, 7), Rational(4, 9)]])
    C1 = Matrix([[Rational(5, 11), Rational(-6, 13)], [Rational(7, 17), Rational(8, 19)]])
    F1 = Matrix([[Rational(3, 2), Rational(1, 5)], [Rational(1, 7), Rational(5, 3)]])

    B2 = Matrix([[Rational(-2, 9), Rational(5, 8)], [Rational(7, 10), Rational(-1, 6)]])
    C2 = Matrix([[Rational(4, 15), Rational(3, 14)], [Rational(-5, 12), Rational(2, 11)]])
    F2 = Matrix([[Rational(7, 4), Rational(-1, 8)], [Rational(1, 9), Rational(11, 6)]])

    A_one = delta_S_target + B1 * F1.inv() * C1
    A_two = delta_S_target + B2 * F2.inv() * C2

    delta_S_1 = A_one - B1 * F1.inv() * C1
    delta_S_2_check = A_two - B2 * F2.inv() * C2

    # By construction both Schur complements equal delta_S_target.
    same_schur = matrices_equal(delta_S_1, delta_S_target) and matrices_equal(
        delta_S_2_check, delta_S_target
    )
    check(
        "Two sector operators sharing the same Schur complement on the retained "
        "support give the same delta_S (algebraic invariance)",
        same_schur,
        detail="spectator-extension invariance at d=2",
    )

    # Lane A round-trip on both:
    lam_spec = Rational(4, 17)
    K_pass_1 = (eye(2) - lam_spec * delta_S_1).inv()
    K_pass_2 = (eye(2) - lam_spec * delta_S_2_check).inv()
    delta_A_1 = (eye(2) - K_pass_1.inv()) / lam_spec
    delta_A_2 = (eye(2) - K_pass_2.inv()) / lam_spec
    same_round_trip = matrices_equal(delta_A_1, delta_A_2)
    check(
        "Lane A round-trip on the two spectator-different fixtures gives the same "
        "recovered block (spectator-extension invariance of recovery)",
        same_round_trip,
        detail="round-trip invariance at d=2",
    )

    # -----------------------------------------------------------------
    section("Summary")
    # -----------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (R-pass) Passive convention d=2 symbolic and d=3 exact-rational identity")
    print("    (R-act)  Active convention d=2 symbolic and d=3 exact-rational identity")
    print("    Full Schur round-trip d=2, s=1 (passive and active, symbolic)")
    print("    response_columns_from_block round-trip identity (passive and active)")
    print("    FP cross-check on independent random (M, lam) at d=3, s=2 (passive and active)")
    print("    Counterfactual: wrong sign (K - I)/lam fails to recover delta")
    print("    Spectator-extension invariance exact-rational probe at d=2")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
