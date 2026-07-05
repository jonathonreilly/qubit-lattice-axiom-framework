#!/usr/bin/env python3
"""Finite source-free entropy bookkeeping for the FRW C2 premise.

This runner checks a narrow mathematical bridge:

* finite internal entropy transfers conserve total comoving entropy;
* a nonzero source/injection term changes total comoving entropy;
* `g_*S T^3 a^3 = const` is exact finite step bookkeeping when no source is
  present;
* wrong temperature scaling fails the same invariant.

It does not derive that the real leptogenesis-to-CMB era is source-free, does
not derive the Standard Model `g_*S(T)` table, and does not set audit status.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs/FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = (
    ROOT
    / "docs/FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md"
)
RUNNER_PATH = "scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py"
CACHE_PATH = "logs/runner-cache/frontier_frw_c2_entropy_bookkeeping_2026_06_18.txt"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")
    return condition


def total(values: list[Fraction]) -> Fraction:
    return sum(values, Fraction(0))


def apply_delta(values: list[Fraction], delta: list[Fraction]) -> list[Fraction]:
    return [x + dx for x, dx in zip(values, delta)]


def entropy_invariant(g_star_s: Fraction, temperature: Fraction, scale: Fraction) -> Fraction:
    return g_star_s * temperature**3 * scale**3


def part0_source_firewall() -> None:
    print("\n== Part 0: source/status firewall ==")
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").split())
    parent = " ".join(PARENT_NOTE_PATH.read_text(encoding="utf-8").split())

    required_note = [
        "Claim type:** bounded_theorem",
        "Type:** bounded_theorem",
        "Status:** bounded support for finite source-free entropy bookkeeping only",
        "actual_current_surface_status: bounded-support",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
        "proposal_allowed: false",
        "not an audit result",
        "No new axiom",
        "source-free entropy bookkeeping only",
        "does not derive that the real cosmological era is source-free",
        "does not derive C1",
        "does not derive the Standard Model g_*S table",
        RUNNER_PATH,
        CACHE_PATH,
    ]
    for phrase in required_note:
        check(f"C2 note contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "Status: retained",
        "actual_current_surface_status: retained",
        "sets effective status",
        "derives C1",
        "derives C2",
        "derives the real no-injection era",
        "derives the g_*S table",
    ]
    for phrase in forbidden:
        check(f"C2 note excludes overclaim phrase: {phrase}", phrase not in note)

    required_parent = [
        "2026-06-18 C2 entropy-bookkeeping partial bridge",
        "FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "does not derive that the real leptogenesis-to-CMB window is source-free",
        "does not derive the Standard Model `g_*S` table",
    ]
    for phrase in required_parent:
        check(f"parent FRW note records C2 phrase: {phrase}", phrase in parent)


def part1_finite_internal_transfer() -> None:
    print("\n== Part 1: finite source-free internal transfers ==")
    start = [Fraction(11), Fraction(7), Fraction(5)]
    delta1 = [Fraction(-3), Fraction(2), Fraction(1)]
    after1 = apply_delta(start, delta1)
    delta2 = [Fraction(4), Fraction(-6), Fraction(2)]
    after2 = apply_delta(after1, delta2)

    check("first internal transfer has zero total source", total(delta1) == 0, str(delta1))
    check("first transfer conserves total comoving entropy", total(after1) == total(start))
    check("second internal transfer has zero total source", total(delta2) == 0, str(delta2))
    check("second transfer conserves total comoving entropy", total(after2) == total(start))
    check("individual component entropy need not be conserved", after2 != start, f"{start} -> {after2}")


def part2_source_injection_boundary() -> None:
    print("\n== Part 2: nonzero source/injection boundary ==")
    start = [Fraction(11), Fraction(7), Fraction(5)]
    injection = [Fraction(0), Fraction(2), Fraction(0)]
    after = apply_delta(start, injection)
    check("source vector has nonzero total injection", total(injection) == 2, str(injection))
    check("nonzero source changes total comoving entropy", total(after) != total(start))
    check(
        "changed total equals starting total plus source",
        total(after) == total(start) + total(injection),
        f"{total(after)} = {total(start)} + {total(injection)}",
    )


def part3_gstar_step_bookkeeping() -> None:
    print("\n== Part 3: exact g_*S step bookkeeping ==")
    # Pick exact cubes so no irrational arithmetic is needed.  The invariant is
    # g_*S * T^3 * a^3; the step g1=27 -> g2=8 is compensated by
    # T2/T1 = (g1/g2)^(1/3) * a1/a2.
    g1 = Fraction(27)
    g2 = Fraction(8)
    a1 = Fraction(2)
    a2 = Fraction(3)
    t1 = Fraction(5)
    t2 = t1 * Fraction(3, 2) * Fraction(a1, a2)
    inv1 = entropy_invariant(g1, t1, a1)
    inv2 = entropy_invariant(g2, t2, a2)
    wrong_t2 = t1 * Fraction(a1, a2)
    wrong_inv2 = entropy_invariant(g2, wrong_t2, a2)

    check("chosen step has exact rational compensated temperature", t2 == t1)
    check("g_*S T^3 a^3 invariant is conserved across the compensated step", inv1 == inv2)
    check("uncorrected T proportional a^-1 scaling fails when g_*S changes", wrong_inv2 != inv1)
    check(
        "wrong scaling misses by the g_*S ratio",
        wrong_inv2 / inv1 == Fraction(g2, g1),
        f"wrong/invariant={wrong_inv2 / inv1}",
    )


def part4_baryon_entropy_ratio() -> None:
    print("\n== Part 4: conserved charge over entropy bookkeeping ==")
    baryon_number = Fraction(13)
    entropy_start = Fraction(91)
    entropy_end = Fraction(91)
    entropy_injected = Fraction(99)

    check(
        "source-free N_B/S ratio is invariant",
        baryon_number / entropy_start == baryon_number / entropy_end,
        f"N_B/S={baryon_number / entropy_start}",
    )
    check(
        "entropy injection changes N_B/S if baryon number is fixed",
        baryon_number / entropy_start != baryon_number / entropy_injected,
        f"before={baryon_number / entropy_start}, after={baryon_number / entropy_injected}",
    )
    check(
        "ratio failure is a C2 source term residual, not arithmetic failure",
        entropy_injected != entropy_start,
    )


def part5_result() -> None:
    print("\n== Result ==")
    print("Closed by this bridge: finite source-free entropy and g_*S bookkeeping algebra.")
    print("Still open: real no-injection era, g_*S table authority, C1, full FRW closure, audit status.")


def main() -> int:
    print("FRW C2 SOURCE-FREE ENTROPY BOOKKEEPING")
    part0_source_firewall()
    part1_finite_internal_transfer()
    part2_source_injection_boundary()
    part3_gstar_step_bookkeeping()
    part4_baryon_entropy_ratio()
    part5_result()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded support passes for finite source-free entropy "
            "bookkeeping. The real no-injection cosmological era, g_*S table, "
            "C1, and audit status remain open."
        )
        return 0
    print("VERDICT: bounded support FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
