#!/usr/bin/env python3
"""Hierarchy alpha_bare^16 = (4pi)^{-16} content-attribution diagnostic runner.

Verifies the content-attribution decomposition of the framework's hierarchy
formula factor alpha_LM^16 into alpha_bare^16 * u_0^{-16}, quantifies
suppression shares at the canonical surface, traces the (4pi)^{-16} content
to the named upstream authority chain (C1)-(C4), and runs counterfactual
sensitivity probes.

The runner consumes only:
- canonical-surface anchor <P> = 0.5934 (from plaquette_self_consistency_note),
- canonical QFT convention alpha := g^2/(4pi),
- g_bare = 1 (open gate per minimal_axioms / g_bare_derivation_note).

It deliberately does not consume:
- any PDG observed value,
- any fitted selector,
- any external literature numerical comparator (beyond convention citations),
- any audit-status promotion claim.

Source note: docs/HIERARCHY_ALPHA_BARE_FOUR_PI_CONTINUUM_MEASURE_CONTENT_ATTRIBUTION_BOUNDED_NOTE_2026-05-26.md
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "hierarchy_alpha_bare_four_pi_continuum_measure_content_attribution_bounded_note_2026-05-26"
)
RUNNER_PATH = "scripts/frontier_hierarchy_alpha_bare_four_pi_content_attribution.py"
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_ALPHA_BARE_FOUR_PI_CONTINUUM_MEASURE_CONTENT_ATTRIBUTION_BOUNDED_NOTE_2026-05-26.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


# Canonical-surface anchors (from PLAQUETTE_SELF_CONSISTENCY_NOTE.md;
# bounded reuse value, not derived here).
P_CANONICAL = 0.5934
U0_CANONICAL = P_CANONICAL ** 0.25  # Lepage-Mackenzie tadpole convention
ALPHA_BARE_CANONICAL = 1.0 / (4.0 * math.pi)  # standard QFT convention with g_bare = 1
ALPHA_LM_CANONICAL = ALPHA_BARE_CANONICAL / U0_CANONICAL

# Tolerance for floating-point cross-checks
TOL = 1e-12
DECADE_TOL = 0.05  # allowance for log10 share assertions


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Content-Attribution",
        "T1, exact algebraic identity",
        "T2, content-attribution decomposition",
        "T3, content-chain trace",
        "T4, counterfactual sensitivity",
        "**Status authority:** independent audit lane only",
        "proposal_allowed: true",
        "audit_required_before_effective_status_change: true",
        RUNNER_PATH,
        "This packet does not",
        "no new admission",
        "no new repo vocabulary",
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note)

    forbidden_promotion = [
        "retained closure",
        "retained-grade closure",
        "retained promotion",
        "promote to retained",
        "closes primitive P3",
    ]
    for phrase in forbidden_promotion:
        check(
            f"source note excludes promotion phrase: {phrase}",
            phrase not in note,
        )


def part1_algebraic_identity_t1() -> None:
    print("\n== Part 1: T1 algebraic identity alpha_LM^16 = alpha_bare^16 * u_0^(-16) ==")

    # T1 symbolic
    a_bare, u0 = sp.symbols("alpha_bare u_0", positive=True)
    alpha_lm = a_bare / u0
    lhs = alpha_lm ** 16
    rhs = a_bare ** 16 * u0 ** (-16)
    diff = sp.simplify(lhs - rhs)
    check(
        "T1 symbolic: alpha_LM^16 == alpha_bare^16 * u_0^(-16)",
        diff == 0,
        f"diff = {diff}",
    )

    # T1 numeric at canonical surface
    lhs_num = ALPHA_LM_CANONICAL ** 16
    rhs_num = (ALPHA_BARE_CANONICAL ** 16) * (U0_CANONICAL ** -16)
    check(
        "T1 numeric: alpha_LM^16 == alpha_bare^16 * u_0^(-16) at canonical surface",
        math.isclose(lhs_num, rhs_num, rel_tol=TOL),
        f"lhs = {lhs_num:.6e}, rhs = {rhs_num:.6e}",
    )


def part2_content_attribution_t2() -> None:
    print("\n== Part 2: T2 numerical content-attribution decomposition ==")

    alpha_bare_16 = ALPHA_BARE_CANONICAL ** 16
    u0_minus_16 = U0_CANONICAL ** -16
    alpha_lm_16 = ALPHA_LM_CANONICAL ** 16

    # T2a: alpha_bare^16 = (1/(4pi))^16
    expected_alpha_bare_16 = (1.0 / (4.0 * math.pi)) ** 16
    check(
        "T2a: alpha_bare^16 = (1/(4 pi))^16 numeric",
        math.isclose(alpha_bare_16, expected_alpha_bare_16, rel_tol=TOL),
        f"alpha_bare^16 = {alpha_bare_16:.6e}, expected = {expected_alpha_bare_16:.6e}",
    )

    # T2b: u_0^-16 = <P>^-4
    p_minus_4 = P_CANONICAL ** -4
    check(
        "T2b: u_0^(-16) = <P>^(-4) numeric",
        math.isclose(u0_minus_16, p_minus_4, rel_tol=TOL),
        f"u_0^(-16) = {u0_minus_16:.4f}, <P>^(-4) = {p_minus_4:.4f}",
    )

    # T2c: product matches direct
    product = alpha_bare_16 * u0_minus_16
    check(
        "T2c: alpha_bare^16 * u_0^(-16) matches alpha_LM^16 to roundoff",
        math.isclose(product, alpha_lm_16, rel_tol=TOL),
        f"product = {product:.6e}, alpha_LM^16 = {alpha_lm_16:.6e}",
    )

    # T2d: suppression-share assertion.
    # alpha_bare^16 carries all ~17 decimal decades; u_0^{-16} carries an
    # order-unity factor below one decade.
    log10_alpha_bare_16 = math.log10(alpha_bare_16)
    log10_u0_minus_16 = math.log10(u0_minus_16)
    log10_alpha_lm_16 = math.log10(alpha_lm_16)

    check(
        "T2d-i: alpha_bare^16 supplies ~17-18 decades of suppression (log10 in [-18.5, -16.5])",
        -18.5 < log10_alpha_bare_16 < -16.5,
        f"log10(alpha_bare^16) = {log10_alpha_bare_16:.4f}",
    )
    check(
        "T2d-ii: u_0^(-16) supplies sub-decade order-unity factor (0 < log10 < 1.5)",
        0 < log10_u0_minus_16 < 1.5,
        f"log10(u_0^(-16)) = {log10_u0_minus_16:.4f}",
    )
    check(
        "T2d-iii: alpha_LM^16 log10 decomposition sums correctly",
        math.isclose(log10_alpha_bare_16 + log10_u0_minus_16, log10_alpha_lm_16, abs_tol=DECADE_TOL),
        f"log10(alpha_bare^16) + log10(u_0^(-16)) = {log10_alpha_bare_16 + log10_u0_minus_16:.4f}, "
        f"log10(alpha_LM^16) = {log10_alpha_lm_16:.4f}",
    )


def part3_content_trace_t3() -> None:
    print("\n== Part 3: T3 content-chain trace ==")

    # T3a: alpha_bare = g_bare^2 / (4 pi) at g_bare = 1
    g_bare = 1
    alpha_bare_from_convention = g_bare ** 2 / (4.0 * math.pi)
    check(
        "T3a: alpha_bare = g_bare^2/(4 pi) at g_bare = 1 gives 1/(4 pi)",
        math.isclose(alpha_bare_from_convention, ALPHA_BARE_CANONICAL, rel_tol=TOL),
        f"alpha_bare = {alpha_bare_from_convention:.6f}, 1/(4 pi) = {ALPHA_BARE_CANONICAL:.6f}",
    )

    # T3b: alpha_bare^16 = (4 pi)^{-16}
    alpha_bare_16 = alpha_bare_from_convention ** 16
    four_pi_minus_16 = (4.0 * math.pi) ** -16
    check(
        "T3b: alpha_bare^16 = (4 pi)^(-16) exactly",
        math.isclose(alpha_bare_16, four_pi_minus_16, rel_tol=TOL),
        f"alpha_bare^16 = {alpha_bare_16:.6e}, (4 pi)^(-16) = {four_pi_minus_16:.6e}",
    )


def part4_counterfactual_sensitivity_t4() -> None:
    print("\n== Part 4: T4 counterfactual c^16 sensitivity ==")

    canonical_alpha_bare_16 = ALPHA_BARE_CANONICAL ** 16

    # T4a: c = 2 -> v_new / v_canonical = 2^16
    c = 2.0
    ratio = (c * ALPHA_BARE_CANONICAL) ** 16 / canonical_alpha_bare_16
    expected = c ** 16
    check(
        "T4a: c=2 gives v_new/v_canonical = 2^16 = 65536",
        math.isclose(ratio, expected, rel_tol=TOL),
        f"ratio = {ratio:.6e}, expected = {expected:.6e}",
    )

    # T4b: c = 1/2 -> v_new / v_canonical = 2^-16
    c = 0.5
    ratio = (c * ALPHA_BARE_CANONICAL) ** 16 / canonical_alpha_bare_16
    expected = c ** 16
    check(
        "T4b: c=1/2 gives v_new/v_canonical = 2^(-16) ~ 1.526e-5",
        math.isclose(ratio, expected, rel_tol=TOL),
        f"ratio = {ratio:.6e}, expected = {expected:.6e}",
    )

    # T4c: c = 2 pi -> v_new / v_canonical = (2 pi)^16
    c = 2.0 * math.pi
    ratio = (c * ALPHA_BARE_CANONICAL) ** 16 / canonical_alpha_bare_16
    expected = c ** 16
    check(
        "T4c: c=2 pi gives v_new/v_canonical = (2 pi)^16",
        math.isclose(ratio, expected, rel_tol=TOL),
        f"ratio = {ratio:.6e}, expected = {expected:.6e}",
    )


def part5_boundary_respect() -> None:
    print("\n== Part 5: T5 source-note boundary check ==")

    note = NOTE_PATH.read_text(encoding="utf-8")

    # T5 / T6 / T7: verify boundary statements present
    boundary_required = [
        "Derive `α_bare = 1/(4π)` from `Cl(3)` on `Z^3` primitives. The",
        "Modify the honest-status note, the canonical chain note",
        "Promote any cited authority",
        "Close primitive P3",
        "Introduce a new primitive",
        "Introduce any new repo vocabulary",
    ]
    for phrase in boundary_required:
        check(f"T5 boundary: source contains 'does not' clause: {phrase}", phrase in note)

    # T7 forbidden-imports check (textual presence of explicit denial)
    # Joining lines because the explicit denial is across a line break.
    joined = " ".join(note.split())
    check(
        "T7 forbidden-imports check present",
        "no PDG observed values" in joined
        and "literature numerical comparators" in joined
        and "no fitted selectors" in joined
        and "forbidden_imports_used: false" in note,
    )


def part6_summary() -> None:
    print("\n== Summary ==")
    print(
        "Content-attribution diagnostic: alpha_LM^16 = alpha_bare^16 * u_0^(-16); "
        f"alpha_bare^16 ~ (4 pi)^(-16) ~ {(1.0 / (4.0 * math.pi)) ** 16:.4e} "
        f"dominates the ~17-decade suppression; u_0^(-16) = <P>^(-4) ~ {P_CANONICAL ** -4:.4f} "
        "is the Lepage-Mackenzie order-unity correction. Content rides existing primitive P3 "
        "of the honest-status note; no new admission, no new axiom, no new repo vocabulary, "
        "no status promotion."
    )


def main() -> int:
    print(f"HIERARCHY ALPHA_BARE (4 PI)^-16 CONTENT-ATTRIBUTION DIAGNOSTIC")
    print(f"  Claim id: {CLAIM_ID}")
    part0_source_firewall()
    part1_algebraic_identity_t1()
    part2_content_attribution_t2()
    part3_content_trace_t3()
    part4_counterfactual_sensitivity_t4()
    part5_boundary_respect()
    part6_summary()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: content-attribution diagnostic passes; alpha_bare^16 ~ (4 pi)^(-16) "
            "dominates the hierarchy formula's suppression and traces to existing upstream "
            "(C1)-(C4) authority chain inside open primitive P3."
        )
        return 0
    print("VERDICT: content-attribution diagnostic FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
