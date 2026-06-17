#!/usr/bin/env python3
"""Conditional residue coefficient algebra for the two-Ward g_bare route.

This runner checks only the narrow repaired claim:

  * retained Rep-B input F_Htt^(0)^2 = 1/6;
  * admitted same-1PI residue identity F_Htt^(0)^2 = g_bare^2/(2 N_c);
  * exact rational consequence g_bare = 1 on the positive branch;
  * source text keeps the residue premise conditional;
  * exact residue-normalization obstruction: current cited inputs allow an
    undetermined same-direction multiplier R(g_bare), so g_bare = 1 is pinned
    only after adding the extra normalization R(g_bare) = 1.
  * actual-surface scope lock: this packet is a conditional map plus
    no-admission obstruction, not an unconditional pinning theorem.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19"
DEP_ID = "g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19"
RUNNER_PATH = "scripts/frontier_gbare_same_1pi_admitted_residue_repair.py"
NOTE_PATH = ROOT / "docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "**Claim type:** bounded_theorem",
        "conditional-use firewall",
        "conditional Path-2 support theorem",
        "actual-surface scope lock",
        "not an unconditional pinning theorem",
        "H_unit-residue admission",
        "residue-normalization obstruction",
        "residue-normalization degree of freedom",
        "free multiplier family `R(g_bare)=g_bare^2`",
        "R(g_bare)",
        "Downstream firewall",
        "They may not cite it as an actual-surface theorem deriving `g_bare = 1`",
        "present packet cannot derive `g_bare = 1`",
        "not an actual-surface pinning theorem",
        "This note does not derive the complete same-projected 1PI exhaustion theorem",
        "The `g_bare = 1` closure is **conditional on the H_unit-residue",
        "does not prove the missing same-projected 1PI exhaustion bridge",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note contains boundary phrase: {phrase}", phrase in flat_note)

    forbidden_note_phrases = [
        "This proves the theorem.",
        "mathematically unavoidable",
        "cannot represent different quantities",
        "H_unit-residue is the complete same-projected 1PI",
        "promoted to retained",
        "R(g_bare) is fixed by D17",
        "This packet proves an actual-surface theorem deriving `g_bare = 1`",
    ]
    for phrase in forbidden_note_phrases:
        check(f"source note excludes overclaim phrase: {phrase}", phrase not in flat_note)

    forbidden_runner_phrases = [
        "observ" + "ed",
        "Standard Model top " + "mass",
        "Planck-surface " + "transport",
        "apply_" + "audit",
    ]
    for phrase in forbidden_runner_phrases:
        check(f"runner source excludes non-load-bearing phrase: {phrase}", phrase not in source)


def part1_exact_coefficient_algebra() -> None:
    section("PART 1: EXACT COEFFICIENT ALGEBRA")

    n_c = Fraction(3)
    f_htt_squared = Fraction(1, 6)
    g_bare_squared = Fraction(2) * n_c * f_htt_squared

    check("color dimension is N_c = 3", n_c == 3, f"N_c={n_c}")
    check("retained Rep-B input is F_Htt^(0)^2 = 1/6", f_htt_squared == Fraction(1, 6), f"F^2={f_htt_squared}")
    check(
        "admitted same-1PI identity forces g_bare^2 = 2 N_c F^2 = 1",
        g_bare_squared == 1,
        f"2*{n_c}*{f_htt_squared}={g_bare_squared}",
    )

    g_bare_positive = Fraction(1)
    check("positive branch gives g_bare = 1", g_bare_positive == 1, f"g_bare={g_bare_positive}")

    coefficient_at_solution = g_bare_positive**2 / (Fraction(2) * n_c)
    check(
        "canonical positive solution matches Rep-B coefficient",
        coefficient_at_solution == f_htt_squared,
        f"g^2/(2 N_c)={coefficient_at_solution}",
    )

    for sample in [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(7, 11)]:
        required_f2 = sample**2 / (Fraction(2) * n_c)
        check(
            f"sample g_bare={sample} would require F^2 != 1/6",
            required_f2 != f_htt_squared,
            f"required F^2={required_f2}",
        )


def part2_residue_normalization_obstruction() -> None:
    section("PART 2: RESIDUE-NORMALIZATION OBSTRUCTION")

    n_c = Fraction(3)
    f_htt_squared = Fraction(1, 6)
    note = NOTE_PATH.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())

    check(
        "source note states D17 fixes direction, not scalar residue multiplier",
        "D17 rules out" in flat_note
        and "operator direction" in flat_note
        and "does not prove that the coefficient" in flat_note,
    )
    check(
        "source note identifies R(g_bare)=1 as the extra bridge",
        "If the H_unit-residue admission supplies the extra normalization" in flat_note
        and "`R(g_bare) = 1`" in flat_note,
    )

    # Canonical-surface agreement only enforces R(1)=1.
    r_at_one = Fraction(1) ** 2
    check("free multiplier family R(g)=g^2 obeys canonical R(1)=1", r_at_one == 1)

    for sample in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(7, 11)]:
        rep_a = sample**2 / (Fraction(2) * n_c)
        residue_multiplier = sample**2
        rep_b_general = residue_multiplier * f_htt_squared
        check(
            f"R(g)=g^2 makes same-direction Rep-B_R equal Rep A at g={sample}",
            rep_b_general == rep_a,
            f"R={residue_multiplier}, B_R={rep_b_general}, A={rep_a}",
        )

    # In contrast, the constant multiplier R(g)=1 is exactly the H_unit-residue
    # admission and pins only the canonical positive branch.
    for sample in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(7, 11)]:
        rep_a = sample**2 / (Fraction(2) * n_c)
        rep_b_admitted = f_htt_squared
        expected = sample == 1
        check(
            f"constant R(g)=1 equality holds iff g=1 for sample g={sample}",
            (rep_a == rep_b_admitted) == expected,
            f"A={rep_a}, B_admitted={rep_b_admitted}",
        )


def main() -> int:
    print("Admitted-residue same-1PI g_bare repair")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_exact_coefficient_algebra()
    part2_residue_normalization_obstruction()

    print("\n" + "=" * 88)
    print("SUMMARY")
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
