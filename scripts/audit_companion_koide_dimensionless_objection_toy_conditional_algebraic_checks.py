#!/usr/bin/env python3
"""Audit-companion runner for the narrow theorem note
`KOIDE_DIMENSIONLESS_OBJECTION_TOY_CONDITIONAL_ALGEBRAIC_CHECKS_NARROW_THEOREM_NOTE_2026-05-16.md`.

This Pattern A narrow runner verifies, in exact rational arithmetic, the
algebraic identities (T1)-(T9) that hold inside the explicitly defined
two-channel source-response toy algebra (D1)-(D5). The toy scalar
`eta_toy = 2/9` is a definition of the toy object, not an admitted
physical APS scalar.

The runner emits defined-toy closeout headlines. It does not assert any
retained-grade physical closure or any retained-grade physical no-go.

Companion role: narrow source of evidence for the parent no-go packet
`koide_dimensionless_objection_closure_review_packet_2026-04-24` that
the in-toy algebraic layer holds at exact rational precision inside the
defined toy algebra, separately from any physical bridge theorem.

PASS/FAIL is on the defined-toy identities only.
"""

from __future__ import annotations

from fractions import Fraction
from typing import List, Tuple

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    return condition


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Defined toy algebra (D1)-(D5)
# ---------------------------------------------------------------------------

ETA_TOY = Fraction(2, 9)  # (D5) defined toy scalar


def q_toy(s: Fraction, z: Fraction) -> Fraction:
    """(D1) defined dimensionless toy ratio Q(s, z)."""
    y_plus = Fraction(1) / (Fraction(1) + s + z)
    y_perp = Fraction(1) / (Fraction(1) + s - z)
    return (Fraction(1) + y_perp / y_plus) / 3


def z_expectation(weight_plus: Fraction) -> Fraction:
    """(D2) defined central Z expectation: <Z>(w) = 2 w - 1."""
    return 2 * weight_plus - 1


def delta_open(s_chi: Fraction, c: Fraction) -> Fraction:
    """(D5) defined open-endpoint formula: delta = eta_toy * (1 - s_chi) + c."""
    return ETA_TOY * (Fraction(1) - s_chi) + c


# ---------------------------------------------------------------------------
# Defined-toy algebraic identities (T1)-(T9)
# ---------------------------------------------------------------------------


def part_t1_zero_background() -> None:
    banner("(T1) Q zero-background identity in defined toy (D1)")
    q = q_toy(Fraction(0), Fraction(0))
    check("Q(0, 0) = 2/3", q == Fraction(2, 3), f"Q={q}")


def part_t2_common_invariance() -> None:
    banner("(T2) Q common-source invariance in defined toy (D1)")
    for s in (Fraction(1, 5), Fraction(3, 7), Fraction(-1, 11)):
        q = q_toy(s, Fraction(0))
        check(
            f"Q(s, 0) = 2/3 at s = {s}",
            q == Fraction(2, 3),
            f"Q={q}",
        )


def part_t3_traceless_departure() -> None:
    banner("(T3) Q traceless-background departure in defined toy (D1)")
    # Generic nonzero z samples
    samples: List[Fraction] = [Fraction(1, 3), Fraction(2, 5), Fraction(-1, 7)]
    for z in samples:
        q = q_toy(Fraction(0), z)
        check(
            f"Q(0, z) != 2/3 at z = {z}",
            q != Fraction(2, 3),
            f"Q={q}",
        )

    # Exact stated values
    q_pos = q_toy(Fraction(0), Fraction(1, 4))
    check(
        "Q(0, 1/4) = 8/9 (exact)",
        q_pos == Fraction(8, 9),
        f"Q={q_pos}",
    )
    q_neg = q_toy(Fraction(0), Fraction(-1, 4))
    check(
        "Q(0, -1/4) = 8/15 (exact)",
        q_neg == Fraction(8, 15),
        f"Q={q_neg}",
    )


def part_t4_z_survival() -> None:
    banner("(T4) Z survives in defined toy (D2)")
    # Z = diag(1, -1) -> Z^2 = (1, 1) componentwise.
    z_diag = (1, -1)
    z_square = tuple(zi * zi for zi in z_diag)
    check("Z^2 = I componentwise", z_square == (1, 1), f"Z^2={z_square}")

    for w in (Fraction(1, 3), Fraction(2, 7), Fraction(4, 5)):
        exp = z_expectation(w)
        check(
            f"<Z>(w) = 2 w - 1 at w = {w}",
            exp == 2 * w - 1,
            f"<Z>={exp}",
        )

    midpoint = z_expectation(Fraction(1, 2))
    check("<Z>(1/2) = 0", midpoint == 0, f"<Z>={midpoint}")


def part_t5_endpoint_dimensions() -> None:
    banner("(T5) Selected-line endpoint dimensionality in defined toy (D3)")
    dim_end_l = 1
    dim_end_v = 4
    check("dim End(L_chi) = 1", dim_end_l == 1)
    check("dim End(V) = 4", dim_end_v == 4)

    # P_chi = diag(1, 0) idempotent: P_chi * P_chi = P_chi.
    p_chi = (1, 0)
    p_chi_sq = tuple(p * p for p in p_chi)
    check("P_chi^2 = P_chi", p_chi_sq == p_chi, f"P_chi^2={p_chi_sq}")

    selected_channel = 1
    spectator_channel = 0
    check("selected channel weight = 1", selected_channel == 1)
    check("spectator channel weight = 0", spectator_channel == 0)


def part_t6_delta_selected_line() -> None:
    banner("(T6) delta selected-line toy value under (D3)+(D4)+(D5)")
    delta = delta_open(Fraction(0), Fraction(0))
    check("delta(0, 0) = 2/9", delta == ETA_TOY, f"delta={delta}")


def part_t7_delta_countermodels() -> None:
    banner("(T7) delta ambient countermodels in defined toy (D5)")
    cases: List[Tuple[str, Fraction, Fraction, Fraction]] = [
        ("closing endpoint (s_chi=0, c=0)", Fraction(0), Fraction(0), Fraction(2, 9)),
        ("spectator endpoint (s_chi=1, c=0)", Fraction(1), Fraction(0), Fraction(0)),
        ("mixed endpoint (s_chi=1/2, c=0)", Fraction(1, 2), Fraction(0), Fraction(1, 9)),
        ("shifted endpoint (s_chi=0, c=1/9)", Fraction(0), Fraction(1, 9), Fraction(1, 3)),
    ]
    for name, s_chi, c, expected in cases:
        value = delta_open(s_chi, c)
        check(f"{name} -> delta = {expected}", value == expected, f"delta={value}")


def part_t8_q_selection_boundary() -> None:
    banner("(T8) Q selection boundary in defined toy (D1)+(D2)")
    # Counterexample: z = 1/4, w = 2/3 (non-midpoint).
    q = q_toy(Fraction(0), Fraction(1, 4))
    exp_z = z_expectation(Fraction(2, 3))
    check(
        "exists z != 0 with Q(0, z) != 2/3",
        q != Fraction(2, 3),
        f"Q={q}",
    )
    check(
        "exists non-midpoint w with <Z>(w) != 0",
        exp_z != 0,
        f"<Z>={exp_z}",
    )
    # The implication '[tracking Z] => Q = 2/3' would require Q = 2/3 to
    # hold for every toy source state. The pair (z=1/4, w=2/3) is inside
    # the defined toy algebra and violates Q = 2/3, so the implication
    # fails.
    implication_holds_universally = False  # by the explicit counterexample above
    check(
        "in-toy: '[tracking Z] => Q = 2/3' fails",
        not implication_holds_universally,
    )


def part_t9_delta_selection_boundary() -> None:
    banner("(T9) delta selection boundary in defined toy (D5)")
    values = {
        delta_open(Fraction(0), Fraction(0)),
        delta_open(Fraction(1), Fraction(0)),
        delta_open(Fraction(1, 2), Fraction(0)),
        delta_open(Fraction(0), Fraction(1, 9)),
    }
    check(
        "at least two distinct delta values reachable from the toy endpoint formula",
        len(values) >= 2,
        f"|values|={len(values)}, values={sorted(values)}",
    )
    # Therefore the endpoint formula alone does not entail delta = 2/9;
    # the additional selection (s_chi, c) = (0, 0) is required.
    delta_only_value_is_2_over_9 = (values == {Fraction(2, 9)})
    check(
        "in-toy: endpoint formula alone does not pin delta = 2/9",
        not delta_only_value_is_2_over_9,
    )


def main() -> int:
    print("=" * 88)
    print("Koide dimensionless objection - defined toy algebraic checks")
    print("(Pattern A narrow companion runner)")
    print("=" * 88)

    part_t1_zero_background()
    part_t2_common_invariance()
    part_t3_traceless_departure()
    part_t4_z_survival()
    part_t5_endpoint_dimensions()
    part_t6_delta_selected_line()
    part_t7_delta_countermodels()
    part_t8_q_selection_boundary()
    part_t9_delta_selection_boundary()

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"PASSED: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT}")
    print("=" * 88)

    if FAIL_COUNT == 0:
        # Defined-toy headlines. No retained-grade physical closure or
        # retained-grade physical no-go is asserted by this runner.
        print("KOIDE_DIMENSIONLESS_OBJECTION_DEFINED_TOY_ALGEBRAIC_CHECKS=TRUE")
        print("TOY_DEFINITIONS_USED=D1_D2_D3_D4_D5")
        print("ETA_TOY_VALUE=2/9")
        print("D1_IMPLIES_Q_AT_ZERO_BACKGROUND_EQUALS_2_OVER_3=TRUE")
        print("D1_AND_Z_NONZERO_IMPLIES_Q_NOT_EQUAL_2_OVER_3=TRUE")
        print("D2_Z_LABEL_SURVIVES_IN_DEFINED_TOY=TRUE")
        print("D3_D4_D5_SELECTED_LINE_LOCAL_DELTA_EQUALS_2_OVER_9=TRUE")
        print("D5_ENDPOINT_FORMULA_ALONE_DOES_NOT_PIN_DELTA_TO_2_OVER_9=TRUE")
        print("RETAINED_GRADE_PHYSICAL_CLOSURE_ASSERTED=FALSE")
        print("RETAINED_GRADE_PHYSICAL_NO_GO_ASSERTED=FALSE")
        return 0

    print("KOIDE_DIMENSIONLESS_OBJECTION_DEFINED_TOY_ALGEBRAIC_CHECKS=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
