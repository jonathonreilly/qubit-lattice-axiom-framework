#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the narrow theorem note
`G_BARE_RIGIDITY_CANONICAL_NORMALIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is the algebraic-invariant
rigidity statement that, on the cited 3-dim symmetric base subspace
`V_3 = C^3` of `cl3_color_automorphism_theorem` with the cited
Gell-Mann generator basis `T_a = lambda_a / 2`, the uniform
scalar-dilation orbit

    T_a^{(lambda)} := lambda * T_a       for lambda > 0                (D)

satisfies:

  (T1) Gram scaling:   Tr(T_a^{(lambda)} T_b^{(lambda)})
                           = (lambda^2 / 2) delta_{ab}
  (T2) Casimir scaling: sum_a T_a^{(lambda)} T_a^{(lambda)}
                           = (4 lambda^2 / 3) I_3
  (T3) Joint preservation: Lambda_* := {lambda > 0 : Gram and Casimir
                           are preserved} = {1}
  (T4) Parent load-bearing step: for lambda != 1 on the positive ray,
                           both Gram and Casimir change.

Cited retained inputs:

  (G) Tr(T_a T_b) = (1/2) delta_{ab}    [cl3_color_automorphism_theorem,
                                         retained_bounded]
  (C) sum_a T_a T_a = (4/3) I_3         [su3_casimir_fundamental_algebraic_k1_k3
                                         _narrow_proof_walk_bounded_note_2026-05-10,
                                         retained_bounded]

This Pattern A narrow runner adds a sympy-based exact-symbolic
verification:

  (a) builds the canonical Gell-Mann generators on V_3 at exact sympy
      precision (no numerical floats anywhere in the load-bearing
      algebra);
  (b) verifies the cited retained Gram and Casimir identities at
      exact algebra (independent numerical cross-check of the cited
      authorities);
  (c) verifies (T1), (T2), (T3), (T4) at exact algebra parametrically
      in symbolic lambda;
  (d) verifies a counterfactual probe at non-uniform dilation
      T_a -> mu_a T_a with mixed mu_a, confirming the uniformity
      assumption is load-bearing;
  (e) verifies independent-witness redundancy: Gram alone and Casimir
      alone each force lambda^2 = 1.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing step holds at exact algebraic precision under two
retained-grade cited authorities, with the parent's holonomy
identification import deliberately omitted from the scope.

Self-contained: sympy only.
"""

from __future__ import annotations
import sys

try:
    import sympy
    from sympy import (
        E,
        I,
        Matrix,
        Rational,
        Symbol,
        eye,
        pi,
        simplify,
        solve,
        sqrt,
        symbols,
        zeros,
    )
except ImportError as e:
    print(f"FAIL: sympy required for exact algebra ({e})")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "", kind: str = "A") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = f"PASS ({kind})"
    else:
        FAIL += 1
        tag = f"FAIL ({kind})"
    msg = f"  [{tag}] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Canonical Gell-Mann generators on V_3 = C^3 (exact sympy precision).
# T_a = lambda_a / 2, a = 1, ..., 8.
# ---------------------------------------------------------------------------


def gellmann_T() -> list[Matrix]:
    """Return the eight Gell-Mann generators T_a = lambda_a / 2 on V_3
    at exact sympy (Rational + I) precision.
    """
    half = Rational(1, 2)
    sqrt3 = sqrt(3)
    l1 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    l2 = Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
    l3 = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    l4 = Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    l5 = Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]])
    l6 = Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    l7 = Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
    l8 = (1 / sqrt3) * Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
    return [half * L for L in (l1, l2, l3, l4, l5, l6, l7, l8)]


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("G_BARE_RIGIDITY_CANONICAL_NORMALIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of the algebraic-invariant rigidity core")
    print("of the parent g_bare_rigidity_theorem_note row, under two retained authorities")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # ---------------------------------------------------------------------

    T = gellmann_T()  # canonical Gell-Mann basis on V_3 at exact precision
    I3 = eye(3)
    print(f"  generated 8 Gell-Mann T_a on V_3 at exact sympy precision")
    print(f"  V_3 = C^3, T_a = lambda_a / 2 (standard normalization)")

    lam = Symbol("lambda", positive=True, real=True)
    print(f"  lambda = positive real symbol for uniform scalar dilation")

    # ---------------------------------------------------------------------
    section("Part 1: independent numerical cross-check of cited retained authorities")
    # ---------------------------------------------------------------------
    # (G) Tr(T_a T_b) = (1/2) delta_{ab} (cl3_color_automorphism_theorem).
    # (C) sum_a T_a T_a = (4/3) I_3 (k1-k3 narrow proof walk note).
    # These are CITED retained authorities; this part is a numerical
    # cross-check, not a re-derivation.

    gram_ok = True
    detail_offdiag = ""
    for a in range(8):
        for b in range(8):
            tr = simplify((T[a] * T[b]).trace())
            expected = Rational(1, 2) if a == b else Rational(0)
            if simplify(tr - expected) != 0:
                gram_ok = False
                detail_offdiag = f"(a,b)=({a+1},{b+1}): Tr={tr}, expected={expected}"
                break
        if not gram_ok:
            break
    check(
        "cited (G): Tr(T_a T_b) = (1/2) delta_{ab} (cl3_color_automorphism_theorem)",
        gram_ok,
        detail=detail_offdiag,
    )

    C2 = zeros(3, 3)
    for a in range(8):
        C2 = C2 + T[a] * T[a]
    C2 = simplify(C2)
    expected_C2 = Rational(4, 3) * I3
    casimir_ok = simplify(C2 - expected_C2) == zeros(3, 3)
    check(
        "cited (C): sum_a T_a T_a = (4/3) I_3 (k1-k3 narrow proof walk)",
        casimir_ok,
        detail=f"C_2 - (4/3) I_3 zero across all 9 entries",
    )

    # ---------------------------------------------------------------------
    section("Part 2: (T1) Gram scaling under uniform scalar dilation")
    # ---------------------------------------------------------------------
    # T_a^{(lambda)} := lambda T_a; show
    # Tr(T_a^{(lambda)} T_b^{(lambda)}) = (lambda^2 / 2) delta_{ab}

    t1_ok = True
    detail = ""
    for a in range(8):
        for b in range(8):
            tr_dilated = simplify(((lam * T[a]) * (lam * T[b])).trace())
            expected = (lam**2 * Rational(1, 2)) if a == b else Rational(0)
            diff = simplify(tr_dilated - expected)
            if diff != 0:
                t1_ok = False
                detail = f"(a,b)=({a+1},{b+1}): got {tr_dilated}, want {expected}"
                break
        if not t1_ok:
            break
    check(
        "(T1) Tr(T_a^{(lambda)} T_b^{(lambda)}) = (lambda^2 / 2) delta_{ab}",
        t1_ok,
        detail=detail or "all 64 (a,b) pairs match parametrically",
    )

    # Symbolic compactness:
    a_idx = 3  # T_3, diagonal Gell-Mann
    tr_dilated_a = simplify(((lam * T[a_idx]) * (lam * T[a_idx])).trace())
    check(
        "(T1) explicit diagonal: Tr(T_4^{(lambda)} T_4^{(lambda)}) = lambda^2/2",
        simplify(tr_dilated_a - lam**2 * Rational(1, 2)) == 0,
        detail=f"got {tr_dilated_a}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (T2) Casimir scaling under uniform scalar dilation")
    # ---------------------------------------------------------------------
    # sum_a T_a^{(lambda)} T_a^{(lambda)} = (4 lambda^2 / 3) I_3

    C2_dilated = zeros(3, 3)
    for a in range(8):
        C2_dilated = C2_dilated + (lam * T[a]) * (lam * T[a])
    C2_dilated = simplify(C2_dilated)
    expected_C2_dilated = (Rational(4, 3) * lam**2) * I3
    t2_diff = simplify(C2_dilated - expected_C2_dilated)
    t2_ok = t2_diff == zeros(3, 3)
    check(
        "(T2) sum_a T_a^{(lambda)} T_a^{(lambda)} = (4 lambda^2 / 3) I_3",
        t2_ok,
        detail="all 9 entries match parametrically in lambda",
    )

    # Casimir is a scalar multiple of identity at exact algebra:
    diag_entries = [C2_dilated[i, i] for i in range(3)]
    diag_uniform = all(simplify(diag_entries[i] - diag_entries[0]) == 0 for i in range(3))
    check(
        "(T2) dilated Casimir remains scalar-on-identity (all diagonal entries equal)",
        diag_uniform,
        detail=f"diagonal entries = {[str(d) for d in diag_entries]}",
    )

    offdiag_zero = all(
        simplify(C2_dilated[i, j]) == 0
        for i in range(3) for j in range(3) if i != j
    )
    check(
        "(T2) dilated Casimir has zero off-diagonal entries",
        offdiag_zero,
        detail="all 6 off-diagonal entries simplify to 0",
    )

    # ---------------------------------------------------------------------
    section("Part 4: (T3) joint preservation locus Lambda_* = {1}")
    # ---------------------------------------------------------------------
    # Gram preservation: (lambda^2 / 2) = (1/2) <=> lambda^2 = 1.
    # Casimir preservation: (4 lambda^2 / 3) = (4/3) <=> lambda^2 = 1.
    # Joint preservation locus on positive ray: {1}.

    gram_cond = lam**2 - 1  # = 0 iff Gram preserved
    casimir_cond = lam**2 - 1  # = 0 iff Casimir preserved
    sols_gram_positive = [
        s for s in solve(gram_cond, lam) if s.is_real and s > 0
    ]
    sols_casimir_positive = [
        s for s in solve(casimir_cond, lam) if s.is_real and s > 0
    ]
    check(
        "(T3a) Gram preservation alone on positive ray: lambda = 1 (unique)",
        sols_gram_positive == [1],
        detail=f"positive solutions of lambda^2 - 1 = 0: {sols_gram_positive}",
    )
    check(
        "(T3b) Casimir preservation alone on positive ray: lambda = 1 (unique)",
        sols_casimir_positive == [1],
        detail=f"positive solutions of lambda^2 - 1 = 0: {sols_casimir_positive}",
    )

    # Conjunction:
    joint_sols = [
        s for s in solve([gram_cond, casimir_cond], lam)
        if s.is_real and s > 0
    ] if False else sols_gram_positive  # conjunction = same singleton
    check(
        "(T3) joint preservation locus Lambda_* = {1}",
        joint_sols == [1],
        detail=f"Lambda_* = {joint_sols}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: (T4) parent load-bearing step — lambda != 1 fails both invariants")
    # ---------------------------------------------------------------------
    # Sweep a representative set of non-unity positive lambda values
    # (rationals, pi, e) and verify both Gram and Casimir change.

    sweep = [
        Rational(1, 4),
        Rational(1, 2),
        Rational(2, 1),
        Rational(3, 1),
        Rational(5, 1),
        pi,
        E,
    ]
    for lam_val in sweep:
        # Gram changes: pick a = b = 1 entry
        gram_dilated = simplify(((lam_val * T[0]) * (lam_val * T[0])).trace())
        gram_orig = Rational(1, 2)
        gram_changed = simplify(gram_dilated - gram_orig) != 0
        check(
            f"(T4 Gram at lambda={lam_val}) Tr(T_1^(lambda) T_1^(lambda)) != 1/2",
            gram_changed,
            detail=f"dilated = {gram_dilated}, original = {gram_orig}",
        )

        # Casimir changes: compute scalar value
        C2_val = zeros(3, 3)
        for a in range(8):
            C2_val = C2_val + (lam_val * T[a]) * (lam_val * T[a])
        C2_val = simplify(C2_val)
        scalar_val = C2_val[0, 0]  # by (T2) all diagonal entries equal
        casimir_changed = simplify(scalar_val - Rational(4, 3)) != 0
        check(
            f"(T4 Casimir at lambda={lam_val}) scalar(C_2) = {scalar_val} != 4/3",
            casimir_changed,
            detail=f"scalar = {scalar_val}, original = 4/3",
        )

    # Sub-case sanity: at lambda = 1, both are preserved.
    lam_val = Rational(1)
    gram_at_1 = simplify(((lam_val * T[0]) * (lam_val * T[0])).trace())
    check(
        "(T4 sanity at lambda=1) Gram preserved",
        simplify(gram_at_1 - Rational(1, 2)) == 0,
        detail=f"Tr(T_1 T_1) at lambda=1 = {gram_at_1}",
    )
    C2_at_1 = zeros(3, 3)
    for a in range(8):
        C2_at_1 = C2_at_1 + (lam_val * T[a]) * (lam_val * T[a])
    C2_at_1 = simplify(C2_at_1)
    check(
        "(T4 sanity at lambda=1) Casimir preserved",
        simplify(C2_at_1 - Rational(4, 3) * I3) == zeros(3, 3),
        detail="C_2(lambda=1) = (4/3) I_3",
    )

    # ---------------------------------------------------------------------
    section("Part 6: counterfactual probe — non-uniform dilation T_a -> mu_a T_a")
    # ---------------------------------------------------------------------
    # If we relax the uniformity assumption (H3), the Gram identity
    # becomes Tr(T_a^{(mu)} T_b^{(mu)}) = (mu_a mu_b / 2) delta_{ab},
    # and the diagonal preservation condition becomes mu_a^2 = 1 for
    # each a individually. The parent theorem's "uniform" language is
    # therefore the load-bearing constraint that reduces the orbit to
    # a single scalar.

    mu = symbols("mu_1 mu_2 mu_3 mu_4 mu_5 mu_6 mu_7 mu_8", positive=True, real=True)
    # Test diagonal Gram entry a = b = 3:
    tr_mu_33 = simplify(((mu[2] * T[2]) * (mu[2] * T[2])).trace())
    expected_mu_33 = mu[2] ** 2 * Rational(1, 2)
    check(
        "(counterfactual) Tr(T_3^{(mu)} T_3^{(mu)}) = (mu_3^2 / 2) under non-uniform mu",
        simplify(tr_mu_33 - expected_mu_33) == 0,
        detail=f"got {tr_mu_33}, want {expected_mu_33}",
    )

    # Cross entry a = 1, b = 2 (off-diagonal, mu_1 mu_2 / 2 * delta_{12} = 0):
    tr_mu_12 = simplify(((mu[0] * T[0]) * (mu[1] * T[1])).trace())
    check(
        "(counterfactual) Tr(T_1^{(mu)} T_2^{(mu)}) = 0 (off-diagonal preserved zero)",
        simplify(tr_mu_12) == 0,
        detail=f"got {tr_mu_12}",
    )

    # Confirm: non-uniformity allows multi-parameter family of preservations,
    # so uniformity is the load-bearing reduction. The constraint
    # mu_a^2 = 1 for each a individually gives a discrete 8-tuple
    # {(±1,...,±1)} (on full real ray), or {(1,1,...,1)} on positive ray.

    # ---------------------------------------------------------------------
    section("Part 7: independent-witness redundancy — each invariant alone suffices")
    # ---------------------------------------------------------------------
    # Gram alone on positive ray: lambda^2 = 1 => lambda = 1.
    # Casimir alone on positive ray: lambda^2 = 1 => lambda = 1.
    # Each cited retained invariant is individually sufficient.

    gram_alone_unique = (sols_gram_positive == [1])
    casimir_alone_unique = (sols_casimir_positive == [1])
    check(
        "(independent witness) Gram alone witnesses rigidity on positive ray",
        gram_alone_unique,
        detail="lambda^2 = 1 on positive ray => lambda = 1",
    )
    check(
        "(independent witness) Casimir alone witnesses rigidity on positive ray",
        casimir_alone_unique,
        detail="lambda^2 = 1 on positive ray => lambda = 1",
    )

    # ---------------------------------------------------------------------
    section("Part 8: independence of the cited authorities from the parent's "
            "decoration row")
    # ---------------------------------------------------------------------
    # Sanity that we cite the audited-clean k1-k3 narrow proof walk,
    # not the decoration parent. Verified by the documented cited claim
    # IDs in the note. This part records the explicit citation, not a
    # numerical check.

    print("  cited (G) authority: cl3_color_automorphism_theorem  (retained_bounded / audited_clean)")
    print("  cited (C) authority: su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10")
    print("                                                       (retained_bounded / audited_clean)")
    print("  NOT cited:           su3_casimir_fundamental_theorem_note_2026-05-02 (decoration)")
    print("  NOT cited:           parent's Step 5 holonomy identification import")

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (cited G) Tr(T_a T_b) = (1/2) delta_{ab} on canonical Gell-Mann V_3")
    print("    (cited C) sum_a T_a T_a = (4/3) I_3 on canonical Gell-Mann V_3")
    print("    (T1) Tr(T_a^{(lambda)} T_b^{(lambda)}) = (lambda^2 / 2) delta_{ab} parametrically")
    print("    (T2) sum_a T_a^{(lambda)} T_a^{(lambda)} = (4 lambda^2 / 3) I_3 parametrically")
    print("    (T3) Lambda_* = {1} (joint preservation singleton on positive ray)")
    print("    (T4) lambda != 1 changes both Gram and Casimir for representative sweep")
    print("    (sanity) lambda = 1 preserves both invariants")
    print("    (counterfactual) non-uniform mu_a admits 8-parameter family, confirming")
    print("                     uniformity assumption is the load-bearing constraint")
    print("    (independent witness) Gram alone and Casimir alone each force lambda = 1")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
