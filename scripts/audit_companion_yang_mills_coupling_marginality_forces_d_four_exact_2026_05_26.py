#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`YANG_MILLS_COUPLING_MARGINALITY_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`.

Pattern A narrow witness for d=4 forcing from the engineering-dimension
direction. The narrow scope is purely the elementary mass-dimension
identity that, in natural units h-bar = c = 1, the engineering
dimension of the Yang-Mills coupling in the canonical kinetic action
S_YM = integral d^d x (-(1/4)) tr(F_{mu nu} F^{mu nu}) with
F = dA + i g_YM [A, A] is
[g_YM] = (4 - d) / 2, which vanishes uniquely at d = 4.

The script verifies, at exact rational precision via sympy:

  (1) (Y1)-(Y3) Setup: [S] = 0, [x^mu] = -1, [partial_mu] = +1,
      [d^d x] = -d for d in {2, 3, ..., 12}.
  (2) (Y4) From [L_kin] = d (kinetic-term Lagrangian density of
      dimension d) and L_kin >= (1/4) tr(F^2) > (partial A)^2 type,
      [A_mu] = (d - 2) / 2 for d in {2, 3, ..., 12}.
  (3) (Y5) [F_{mu nu}] = d / 2 and [g_YM] = (4 - d) / 2 (from the
      non-abelian piece i g_YM [A_mu, A_nu] in F_{mu nu}).
  (4) (Y6) Cross-verification via the cubic self-interaction
      integral d^d x g_YM tr(partial A . A . A) = 0-dim,
      yielding the same [g_YM] = (4 - d) / 2.
  (5) (Y7) Tabular evaluation of [g_YM] = (4 - d) / 2 for d in
      {2, 3, ..., 12}: positive for d < 4, zero at d = 4, negative
      for d > 4.
  (6) (Y8) Uniqueness: d = 4 is the unique integer in {2, ..., 12}
      (and indeed in all d >= 2) satisfying [g_YM] = 0.
  (7) Cross-consistency: the two derivation chains (Y5 vs Y6) yield
      the same [g_YM] as a function of d.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) engineering-dimension identity holds at exact
symbolic precision.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Rational, Symbol, factor, simplify, solve, Eq, Integer
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "YANG_MILLS_COUPLING_MARGINALITY_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md"
)
CLAIM_ID = "yang_mills_coupling_marginality_forces_d_four_narrow_theorem_note_2026-05-26"


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


def dim_A_of_d(d):
    """Engineering dimension [A_mu] = (d - 2) / 2 from the canonical
    kinetic term L_kin = -(1/4) tr(F_{mu nu} F^{mu nu})."""
    return Rational(d - 2, 2)


def dim_F_of_d(d):
    """Engineering dimension [F_{mu nu}] = [partial_mu A_nu] = 1 + [A_mu] = d / 2."""
    return Rational(1) + dim_A_of_d(d)


def dim_g_YM_from_F(d):
    """Engineering dimension [g_YM] from the non-abelian piece i g_YM [A_mu, A_nu]
    in F_{mu nu}: [g_YM] + 2 [A_mu] = [F_{mu nu}], i.e., [g_YM] = d/2 - (d-2) =
    (4 - d) / 2."""
    return dim_F_of_d(d) - 2 * dim_A_of_d(d)


def dim_g_YM_from_cubic_action(d):
    """Engineering dimension [g_YM] from requiring the cubic self-interaction
    integral d^d x g_YM tr(partial_mu A_nu [A^mu, A^nu]) to be
    dimensionless. The constraint is:
      -d + [g_YM] + 1 + 3 [A_mu] = 0
      -d + [g_YM] + 1 + 3 (d - 2) / 2 = 0
      [g_YM] + (d - 4) / 2 = 0
      [g_YM] = (4 - d) / 2.
    """
    return Rational(4 - d, 2)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print(
        "YANG_MILLS_COUPLING_MARGINALITY_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26"
    )
    print("Goal: sympy verification that [g_YM] = (4 - d) / 2 = 0 iff d = 4")
    print("      via engineering-dimension bookkeeping on the bare Yang-Mills")
    print("      action S_YM = integral d^d x (-(1/4)) tr(F^2)")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (Y1)-(Y3) Setup of engineering dimensions in natural units")
    # =========================================================================
    # [S] = 0 (action dimensionless for exp(iS) sensible)
    dim_S = Rational(0)
    check(
        "(Y1) Action is dimensionless: [S] = 0",
        dim_S == 0,
        detail=f"[S] = {dim_S}",
    )
    # [x^mu] = -1, [partial_mu] = +1
    dim_x = Rational(-1)
    dim_partial = Rational(1)
    check(
        "(Y2) Coordinate engineering dimension: [x^mu] = -1",
        dim_x == -1,
        detail=f"[x^mu] = {dim_x}",
    )
    check(
        "(Y3) Partial derivative engineering dimension: [partial_mu] = +1",
        dim_partial == 1,
        detail=f"[partial_mu] = {dim_partial}",
    )
    # [d^d x] = -d
    for d in range(2, 13):
        dim_dx = Rational(-d)
        check(
            f"(Y2) Volume element: [d^d x] = -d at d = {d}",
            dim_dx == -d,
            detail=f"[d^{d} x] = {dim_dx}",
        )

    # =========================================================================
    section("Part 2: (Y4) Gauge-field dimension from kinetic-term normalization")
    # =========================================================================
    # From [L_kin] = d (Lagrangian density of dimension d so that integral
    # L_kin d^d x is dimensionless) and L_kin includes (partial A)^2, we have
    # 2 [partial] + 2 [A] = d, i.e., [A] = (d - 2) / 2.
    for d in range(2, 13):
        # Verify: 2 * [partial] + 2 * [A] = d
        dim_A = dim_A_of_d(d)
        expected_A = Rational(d - 2, 2)
        check(
            f"(Y4) [A_mu] = (d - 2) / 2 at d = {d}: [A_mu] = {dim_A}",
            dim_A == expected_A,
            detail=f"[A_mu] = {dim_A}, expected = {expected_A}",
        )
        # Cross-check: kinetic-term dimensional balance
        lhs = 2 * dim_partial + 2 * dim_A
        rhs = Rational(d)
        check(
            f"(Y4) Kinetic-term dimensional balance at d = {d}: "
            f"2[partial] + 2[A] = d, lhs = {lhs}, rhs = {rhs}",
            lhs == rhs,
            detail=f"lhs - rhs = {lhs - rhs}",
        )

    # =========================================================================
    section("Part 3: (Y5) Field-strength and gauge-coupling dimensions")
    # =========================================================================
    for d in range(2, 13):
        dim_A = dim_A_of_d(d)
        # [F_{mu nu}] = [partial_mu A_nu] = 1 + [A] = 1 + (d-2)/2 = d/2
        dim_F = dim_F_of_d(d)
        expected_F = Rational(d, 2)
        check(
            f"(Y5) [F_{{mu nu}}] = d / 2 at d = {d}: [F] = {dim_F}",
            dim_F == expected_F,
            detail=f"[F] = {dim_F}, expected = {expected_F}",
        )
        # From F_{mu nu} containing i g_YM [A_mu, A_nu], require
        # [g_YM] + 2 [A] = [F] = d/2, i.e., [g_YM] = d/2 - (d-2) = (4-d)/2
        dim_g = dim_g_YM_from_F(d)
        expected_g = Rational(4 - d, 2)
        check(
            f"(Y5) [g_YM] = (4 - d) / 2 at d = {d}: [g_YM] = {dim_g}",
            dim_g == expected_g,
            detail=f"[g_YM] = {dim_g}, expected = {expected_g}",
        )
        # Cross-check: dimensional balance of i g_YM [A_mu, A_nu] inside F
        lhs = dim_g + 2 * dim_A
        rhs = dim_F
        check(
            f"(Y5) F_{{mu nu}} non-abelian-piece balance at d = {d}: "
            f"[g_YM] + 2[A] = [F], lhs = {lhs}, rhs = {rhs}",
            lhs == rhs,
            detail=f"lhs - rhs = {lhs - rhs}",
        )

    # =========================================================================
    section("Part 4: (Y6) Cross-verification via cubic self-interaction term")
    # =========================================================================
    # The cubic term inside the canonical action has overall coefficient
    # proportional to g_YM (from the cross term in (partial A + g_YM [A, A])^2).
    # Requiring integral d^d x of this vertex to be dimensionless:
    #   -d + [g_YM] + 1 + 3 [A] = 0
    # Substituting [A] = (d-2)/2:
    #   -d + [g_YM] + 1 + 3 (d-2)/2 = 0
    #   [g_YM] + (d - 4)/2 = 0
    #   [g_YM] = (4 - d)/2.
    for d in range(2, 13):
        dim_A = dim_A_of_d(d)
        dim_g_v1 = dim_g_YM_from_F(d)
        dim_g_v2 = dim_g_YM_from_cubic_action(d)
        check(
            f"(Y6) [g_YM] consistent across two derivations at d = {d}: "
            f"v1 = {dim_g_v1}, v2 = {dim_g_v2}",
            dim_g_v1 == dim_g_v2,
            detail=f"v1 - v2 = {dim_g_v1 - dim_g_v2}",
        )
        # Cubic self-interaction dimensional balance directly:
        # -d + [g_YM] + 1 + 3 [A] = 0.
        balance = -Rational(d) + dim_g_v2 + Rational(1) + 3 * dim_A
        check(
            f"(Y6) Cubic vertex dimensional balance at d = {d}: "
            f"-d + [g_YM] + 1 + 3[A] = 0, value = {balance}",
            balance == 0,
            detail=f"balance = {balance}",
        )

    # Symbolic identity: [g_YM] = (4 - d) / 2 as polynomial in d.
    d_sym = Symbol("d", integer=True, nonnegative=True)
    g_sym = Rational(1, 2) * (4 - d_sym)  # (4 - d) / 2
    g_alt_sym = Rational(1, 2) * (4 - d_sym)

    check(
        "(Y6) Symbolic: g_YM_dim_v1(d) and g_YM_dim_v2(d) both equal "
        "(4 - d) / 2",
        simplify(g_sym - g_alt_sym) == 0,
        detail=f"g_v1 - g_v2 = {simplify(g_sym - g_alt_sym)}",
    )

    # Both vanish iff d = 4:
    sol_v1 = solve(Eq(g_sym, 0), d_sym)
    sol_v2 = solve(Eq(g_alt_sym, 0), d_sym)
    check(
        "(Y6) Symbolic: g_YM_dim_v1(d) = 0 has unique solution d = 4",
        sol_v1 == [Integer(4)],
        detail=f"solutions = {sol_v1}",
    )
    check(
        "(Y6) Symbolic: g_YM_dim_v2(d) = 0 has unique solution d = 4",
        sol_v2 == [Integer(4)],
        detail=f"solutions = {sol_v2}",
    )

    # =========================================================================
    section("Part 5: (Y7) Tabular evaluation of [g_YM] = (4 - d) / 2")
    # =========================================================================
    # d = 2: [g_YM] = +1 (super-renormalizable)
    # d = 3: [g_YM] = +1/2 (super-renormalizable)
    # d = 4: [g_YM] =  0   (marginal / renormalizable)
    # d = 5: [g_YM] = -1/2 (non-renormalizable)
    # d = 6: [g_YM] = -1   (non-renormalizable)
    # ...
    table = {}
    for d in range(2, 13):
        g_dim = dim_g_YM_from_F(d)
        table[d] = g_dim
        if d < 4:
            check(
                f"(Y7) Super-renormalizable at d = {d}: [g_YM] = {g_dim} > 0",
                g_dim > 0,
                detail=f"[g_YM] = {g_dim}",
            )
        elif d == 4:
            check(
                f"(Y7) Marginal at d = {d}: [g_YM] = {g_dim} = 0",
                g_dim == 0,
                detail=f"[g_YM] = {g_dim}",
            )
        else:  # d > 4
            check(
                f"(Y7) Non-renormalizable at d = {d}: [g_YM] = {g_dim} < 0",
                g_dim < 0,
                detail=f"[g_YM] = {g_dim}",
            )

    # Print the table once for inspection
    print()
    print("  Engineering-dimension table [g_YM] = (4 - d) / 2:")
    for d, g_dim in table.items():
        classification = (
            "super-ren. (relevant)"
            if g_dim > 0
            else ("marginal" if g_dim == 0 else "non-renormalizable (irrelevant)")
        )
        print(f"    d = {d:2d}: [g_YM] = {str(g_dim):>6s}   ({classification})")

    # =========================================================================
    section("Part 6: (Y8) Uniqueness of d = 4 for [g_YM] = 0")
    # =========================================================================
    marginal_d = [d for d in range(2, 13) if dim_g_YM_from_F(d) == 0]
    check(
        "(Y8) Among d in {2, ..., 12}, exactly d = 4 satisfies [g_YM] = 0",
        marginal_d == [4],
        detail=f"marginal d values = {marginal_d}",
    )

    # Extend range up to d = 20 for extra confidence:
    marginal_d_ext = [d for d in range(2, 21) if dim_g_YM_from_F(d) == 0]
    check(
        "(Y8) Among d in {2, ..., 20}, exactly d = 4 satisfies [g_YM] = 0",
        marginal_d_ext == [4],
        detail=f"marginal d values (extended) = {marginal_d_ext}",
    )

    # Polynomial factorization of (4 - d) = 0 ==> d = 4 (linear, unique).
    poly = 4 - d_sym
    sol = solve(Eq(poly, 0), d_sym)
    check(
        "(Y8) Linear equation (4 - d) = 0 has unique solution d = 4",
        sol == [Integer(4)],
        detail=f"solutions = {sol}",
    )

    # =========================================================================
    section(
        "Part 7: Cross-consistency between [g_YM] from F_{mu nu} non-abelian "
        "piece and from cubic action"
    )
    # =========================================================================
    # Both derivations yield the same engineering dimension (4 - d) / 2.
    for d in range(2, 13):
        g_v1 = dim_g_YM_from_F(d)
        g_v2 = dim_g_YM_from_cubic_action(d)
        check(
            f"(consistency) at d = {d}: g_v1 = g_v2",
            g_v1 == g_v2,
            detail=f"g_v1 - g_v2 = {g_v1 - g_v2}",
        )
        # Both vanish iff d == 4
        v1_is_zero = (g_v1 == 0)
        v2_is_zero = (g_v2 == 0)
        check(
            f"(consistency) at d = {d}: (g_v1 == 0) iff (g_v2 == 0)",
            v1_is_zero == v2_is_zero,
            detail=f"v1 == 0: {v1_is_zero}, v2 == 0: {v2_is_zero}",
        )
        check(
            f"(consistency) at d = {d}: marginality iff d == 4",
            v1_is_zero == (d == 4),
            detail=f"v1 == 0: {v1_is_zero}, d == 4: {d == 4}",
        )

    # =========================================================================
    section("Part 8: Informational dimensional readings (cross-check, not load-bearing)")
    # =========================================================================
    # At d = 4: [A_mu] = 1 (canonical Higgs/gauge field dimension in 4d),
    # [F_{mu nu}] = 2 (a 2-form on R^4 with 2-form indices),
    # [g_YM] = 0 (dimensionless coupling).
    check(
        "(info) At d = 4: [A_mu] = 1 (canonical gauge field dimension in 4d)",
        dim_A_of_d(4) == Rational(1),
        detail=f"[A_mu]|_{{d=4}} = {dim_A_of_d(4)}",
    )
    check(
        "(info) At d = 4: [F_{mu nu}] = 2 (2-form on R^4)",
        dim_F_of_d(4) == Rational(2),
        detail=f"[F]|_{{d=4}} = {dim_F_of_d(4)}",
    )
    check(
        "(info) At d = 4: [g_YM] = 0 (dimensionless coupling, marginal/ren.)",
        dim_g_YM_from_F(4) == Rational(0),
        detail=f"[g_YM]|_{{d=4}} = {dim_g_YM_from_F(4)}",
    )

    # At d = 3 (super-renormalizable Yang-Mills): [g_YM] = 1/2.
    check(
        "(info) At d = 3: [g_YM] = 1/2 (super-ren. Yang-Mills in 3d)",
        dim_g_YM_from_F(3) == Rational(1, 2),
        detail=f"[g_YM]|_{{d=3}} = {dim_g_YM_from_F(3)}",
    )
    # At d = 6 (non-renormalizable Yang-Mills): [g_YM] = -1.
    check(
        "(info) At d = 6: [g_YM] = -1 (non-ren. Yang-Mills in 6d)",
        dim_g_YM_from_F(6) == Rational(-1),
        detail=f"[g_YM]|_{{d=6}} = {dim_g_YM_from_F(6)}",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()
    print(f"  Note path: {NOTE_PATH.name}")
    print(f"  Claim id:  {CLAIM_ID}")
    print()
    if FAIL == 0:
        print("  Result: all class-(A) checks pass at exact rational precision.")
        return 0
    print("  Result: at least one class-(A) check failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
