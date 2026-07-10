#!/usr/bin/env python3
"""Verify the Hypercharge GUT-Normalization 3/5 accepted-premise bridge.

The runner uses fractions.Fraction arithmetic only for the science checks.
It verifies (B1)-(B7), then pins the named-premise and dependency surfaces
of the bridge and its R_base consumer. It registers rather than derives the
(P1a) hypercharge multiset and (P1b) equal-family-trace scheme.

Outputs a check list and TOTAL line; exits nonzero if any check fails.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str = ""


ROOT = Path(__file__).resolve().parents[1]
BRIDGE_NAME = (
    "HYPERCHARGE_GUT_NORMALIZATION_THREE_FIFTHS_"
    "ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-07-10.md"
)
BRIDGE_PATH = ROOT / "docs" / BRIDGE_NAME
CONSUMER_PATH = (
    ROOT / "docs" / "R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md"
)
HYPERCHARGE_LINK = (
    "[HYPERCHARGE_IDENTIFICATION_NOTE.md]"
    "(HYPERCHARGE_IDENTIFICATION_NOTE.md)"
)
BRIDGE_LINK = f"[{BRIDGE_NAME}]({BRIDGE_NAME})"


def evaluate() -> list[Check]:
    # (B1)-(B3): family squared traces and the registered scheme composition.
    y_squared_trace = (
        6 * Fraction(1, 6) ** 2
        + 3 * Fraction(2, 3) ** 2
        + 3 * Fraction(1, 3) ** 2
        + 2 * Fraction(1, 2) ** 2
        + Fraction(1, 1)
    )
    t3_squared_trace = 8 * Fraction(1, 4)
    k_squared = t3_squared_trace / y_squared_trace

    # (B4): repeat the scheme in the doubled hypercharge table.
    y_prime_squared_trace = 4 * y_squared_trace
    k_prime_squared = t3_squared_trace / y_prime_squared_trace
    original_table_coupling_ratio = Fraction(1, 1) / k_squared
    rescaled_table_coupling_ratio = Fraction(1, 2) ** 2 / k_prime_squared

    # (B5): both table normalizations carry the same LH-doublet ratio.
    q_l_y = Fraction(1, 6)
    l_l_y = Fraction(-1, 2)
    q_l_y_prime = Fraction(1, 3)
    l_l_y_prime = Fraction(-1, 1)
    family_ratio = (q_l_y / q_l_y, l_l_y / q_l_y)
    retained_ratio = (q_l_y_prime / q_l_y_prime, l_l_y_prime / q_l_y_prime)

    # (B6): anomaly-consistency diagnostics in the all-left-handed convention.
    trace_y = (
        6 * Fraction(1, 6)
        + 3 * Fraction(-2, 3)
        + 3 * Fraction(1, 3)
        + 2 * Fraction(-1, 2)
        + Fraction(1, 1)
    )
    trace_y_cubed = (
        6 * Fraction(1, 6) ** 3
        + 3 * Fraction(-2, 3) ** 3
        + 3 * Fraction(1, 3) ** 3
        + 2 * Fraction(-1, 2) ** 3
        + Fraction(1, 1) ** 3
    )
    su3_squared_y = Fraction(1, 3) - Fraction(2, 3) + Fraction(1, 3)
    su2_squared_y = Fraction(1, 2) - Fraction(1, 2)

    # (B7): exact substitution into the registered R_base identity.
    r_base = Fraction(3, 5) * Fraction(155, 27)

    bridge_exists = BRIDGE_PATH.is_file()
    consumer_exists = CONSUMER_PATH.is_file()
    bridge_text = BRIDGE_PATH.read_text(encoding="utf-8") if bridge_exists else ""
    consumer_text = (
        CONSUMER_PATH.read_text(encoding="utf-8") if consumer_exists else ""
    )
    fenced_multiset_pins = (
        "```text\n(P1) Hypercharge GUT-normalization accepted-premise packet."
        in bridge_text
        and "Q_L : (SU(2) doublet, SU(3) triplet,  Y = +1/6)"
        in bridge_text
        and "e_R : (SU(2) singlet, color singlet,  Y = -1)" in bridge_text
    )

    return [
        Check("(B1) Tr_family(Y^2) = 10/3", y_squared_trace == Fraction(10, 3), str(y_squared_trace)),
        Check("(B2) Tr_family(T_3^2) = 2", t3_squared_trace == Fraction(2, 1), str(t3_squared_trace)),
        Check("(B3) equal-family-trace scheme gives k^2 = 3/5", k_squared == Fraction(3, 5), str(k_squared)),
        Check("(B4) doubled table has Tr(Y'^2) = 40/3", y_prime_squared_trace == Fraction(40, 3), str(y_prime_squared_trace)),
        Check("(B4) doubled table has k'^2 = 3/20", k_prime_squared == Fraction(3, 20), str(k_prime_squared)),
        Check("(B4) original table gives g_1^2/g_Y^2 = 5/3", original_table_coupling_ratio == Fraction(5, 3), str(original_table_coupling_ratio)),
        Check("(B4) doubled table gives the same physical coupling ratio 5/3", rescaled_table_coupling_ratio == Fraction(5, 3), str(rescaled_table_coupling_ratio)),
        Check("(B5) (1/6, -1/2) has ratio 1:(-3)", family_ratio == (Fraction(1, 1), Fraction(-3, 1)), str(family_ratio)),
        Check("(B5) retained (+1/3, -1) table has ratio 1:(-3)", retained_ratio == (Fraction(1, 1), Fraction(-3, 1)), str(retained_ratio)),
        Check("(B6) Tr(Y) = 0", trace_y == 0, str(trace_y)),
        Check("(B6) Tr(Y^3) = 0", trace_y_cubed == 0, str(trace_y_cubed)),
        Check("(B6) SU(3)^2-Y = 0", su3_squared_y == 0, str(su3_squared_y)),
        Check("(B6) SU(2)^2-Y = 0", su2_squared_y == 0, str(su2_squared_y)),
        Check("(B7) (3/5)*(155/27) = 31/9", r_base == Fraction(31, 9), str(r_base)),
        Check("bridge note exists", bridge_exists, str(BRIDGE_PATH)),
        Check("bridge registers the (P1a) tag", "(P1a)" in bridge_text),
        Check("bridge registers the (P1b) tag", "(P1b)" in bridge_text),
        Check("bridge contains the fenced (P1) multiset block", fenced_multiset_pins),
        Check("bridge boundary says it does NOT derive the premise", "does NOT derive (P1a) or (P1b)" in bridge_text),
        Check("bridge has the load-bearing hypercharge markdown link", HYPERCHARGE_LINK in bridge_text),
        Check("consumer note exists", consumer_exists, str(CONSUMER_PATH)),
        Check("consumer note links this bridge", BRIDGE_LINK in consumer_text),
    ]


def main() -> int:
    print("Hypercharge GUT-normalization 3/5 accepted-premise bridge")
    print("Exact Fraction arithmetic; (P1a) and (P1b) are registered inputs.")
    print()

    checks = evaluate()
    pass_count = 0
    fail_count = 0
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        detail = f" ({check.detail})" if check.detail else ""
        print(f"[{status}] {check.name}{detail}")
        if check.passed:
            pass_count += 1
        else:
            fail_count += 1

    print()
    print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
