#!/usr/bin/env python3
"""Bounded premise-packet bridge: alpha = 1/3 by exact arithmetic.

The runner checks only:

1. the retained 6+2 traceless ratio beta = -3 alpha;
2. the explicitly supplied P1-P4 premise packet in the source note;
3. the exact rational solve for alpha = 1/3;

It deliberately does not use quark charge cross-checks, fitted values, Monte
Carlo data, or any lattice-action input.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25"
RUNNER_PATH = "scripts/hypercharge_alpha_third_normalization_runner.py"
NOTE_PATH = ROOT / "docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"

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


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Supplied premise packet (not axioms)",
        "P1 Anti^2-as-L_L readout convention",
        "P2 Gell-Mann-Nishijima convention",
        "P3 weak-isospin assignment",
        "P4 electron-charge unit convention",
        "does not claim to derive the premise packet",
        "not registry accepted premises",
        "new repo-wide axiom",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "empirical SM electric " + "charges",
        "Q(" + "u_L)",
        "Q(" + "d_L)",
    ]
    for phrase in forbidden:
        check(f"source note excludes non-load-bearing cross-check phrase: {phrase}", phrase not in note)


def part1_exact_ratio() -> Fraction:
    print("\n== Part 1: retained 6+2 traceless ratio ==")
    sym_multiplicity = Fraction(6, 1)
    anti_multiplicity = Fraction(2, 1)
    beta_over_alpha = -sym_multiplicity / anti_multiplicity
    check("tracelessness on the 6+2 split gives beta/alpha = -3", beta_over_alpha == Fraction(-3, 1), str(beta_over_alpha))
    return beta_over_alpha


def part2_exact_solve(beta_over_alpha: Fraction) -> Fraction:
    print("\n== Part 2: exact rational solve from P1-P4 ==")
    t3_e_left = Fraction(-1, 2)
    q_e_left = Fraction(-1, 1)

    alpha = (q_e_left - t3_e_left) * Fraction(2, 1) / beta_over_alpha
    check("alpha = 1/3 follows from Q(e_L), T3(e_L), and Y(L_L)=beta", alpha == Fraction(1, 3), str(alpha))

    y_l_left = beta_over_alpha * alpha
    check("Y(L_L) = -1 at alpha = 1/3", y_l_left == Fraction(-1, 1), str(y_l_left))
    return alpha


def part3_result(alpha: Fraction) -> None:
    print("\n== Result ==")
    print(f"alpha = {alpha}")
    print("Bounded bridge: retained 6+2 split/tracelessness + supplied premise packet P1-P4.")
    print("No new repo-wide axiom and no claim to derive P1-P4.")


def main() -> int:
    print("HYPERCHARGE ALPHA=1/3 PREMISE-PACKET BRIDGE")
    part0_source_firewall()
    beta_over_alpha = part1_exact_ratio()
    alpha = part2_exact_solve(beta_over_alpha)
    part3_result(alpha)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded premise-packet bridge passes; alpha = 1/3 follows "
            "from retained 6+2 split/tracelessness + supplied premise packet P1-P4 "
            "by rational arithmetic."
        )
        return 0
    print("VERDICT: bounded premise-packet bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
