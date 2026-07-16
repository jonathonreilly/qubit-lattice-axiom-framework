#!/usr/bin/env python3
"""
P1 I_S revision verification: conditional arithmetic and source-scope firewall.

This runner verifies only:

1. exact SU(3) and alpha-normalization arithmetic;
2. the historical delta_PT value under the separate I_S = 2 convention;
3. the conditional map of the supplied I_S in [4, 10] bracket;
4. explicit open source-action, NLO, Ward-cancellation, operator-transfer,
   selector, and publication-propagation gates; and
5. absence of stale UV-bridge attribution, retained-alpha authority wording,
   and unsupported same/additive/superseding semantic claims.

It does not perform a BZ integration or select a physical relationship between
the historical arithmetic and the supplied lattice-literature bracket.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Dict

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)


PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "YT_P1_I_S_REVISION_VERIFICATION_NOTE_2026-04-17.md"

STALE_BRIDGE_MARKERS = (
    "uv_gauge_to_yukawa_bridge_sc_vs_pert_note",
    "uv_gauge_to_yukawa_bridge)",
)
RETAINED_ALPHA_AUTHORITY_MARKERS = (
    "retained canonical coupling",
    "retained canonical-surface coupling",
    "retained canonical-surface anchor",
    "retained coupling `α_lm`",
    "retained `α_lm`",
    "retained alpha_lm",
)
FORBIDDEN_HISTORICAL_SEMANTICS = (
    "is a continuum vertex-correction magnitude",
    "lattice supersedes continuum",
    "superseded, not additive",
    "absorbed into the lattice matching",
    "contains the continuum vertex-correction content",
    "lower-bound sanity check",
    "lower-bound floor",
)

PI = math.pi
N_C = 3
C_F = (N_C * N_C - 1.0) / (2.0 * N_C)
C_A = float(N_C)
T_F = 0.5

ALPHA_BARE = CANONICAL_ALPHA_BARE
U_0 = CANONICAL_U0
ALPHA_LM = CANONICAL_ALPHA_LM
PLAQUETTE = CANONICAL_PLAQUETTE
ALPHA_LM_OVER_2PI = ALPHA_LM / (2.0 * PI)
ALPHA_LM_OVER_4PI = ALPHA_LM / (4.0 * PI)

I_S_HISTORICAL = 2.0
I_S_CITED_LOW = 4.0
I_S_CITED_CENTRAL = 6.0
I_S_CITED_HIGH = 10.0
DELTA_PT_HISTORICAL = ALPHA_LM * C_F / (2.0 * PI)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def pct(value: float) -> str:
    return f"{100.0 * value:.4f} %"


def conditional_p1(i_s: float) -> float:
    return ALPHA_LM_OVER_4PI * C_F * i_s


def read_note() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def part_a_structural_arithmetic() -> None:
    print("\n" + "=" * 72)
    print("PART A: Structural and conditional alpha arithmetic")
    print("=" * 72)

    check("C_F = 4/3 at SU(3)", abs(C_F - 4.0 / 3.0) < 1e-15)
    check("C_A = 3 at SU(3)", C_A == 3.0)
    check("T_F = 1/2", T_F == 0.5)
    check(
        "alpha_LM equals alpha_bare/u_0 arithmetically",
        abs(ALPHA_LM - ALPHA_BARE / U_0) < 1e-15,
        f"alpha_LM = {ALPHA_LM:.10f}",
    )
    check(
        "u_0 equals plaquette^(1/4) arithmetically",
        abs(U_0 - PLAQUETTE ** 0.25) < 1e-15,
        f"u_0 = {U_0:.10f}",
    )


def part_b_historical_delta_pt() -> None:
    print("\n" + "=" * 72)
    print("PART B: Historical delta_PT arithmetic under I_S = 2")
    print("=" * 72)

    rewritten = ALPHA_LM_OVER_4PI * C_F * I_S_HISTORICAL
    check(
        "alpha/(2 pi) = 2 alpha/(4 pi)",
        abs(ALPHA_LM_OVER_2PI - 2.0 * ALPHA_LM_OVER_4PI) < 1e-15,
    )
    check(
        "delta_PT rewrite at I_S=2 is exact",
        abs(DELTA_PT_HISTORICAL - rewritten) < 1e-15,
        f"delta_PT = {pct(DELTA_PT_HISTORICAL)}",
    )
    check(
        "historical arithmetic evaluates to 1.924%",
        abs(DELTA_PT_HISTORICAL - 0.01924) < 5e-5,
        pct(DELTA_PT_HISTORICAL),
    )


def part_c_conditional_bracket() -> Dict[float, float]:
    print("\n" + "=" * 72)
    print("PART C: Conditional supplied-bracket map")
    print("=" * 72)

    values = {
        i_s: conditional_p1(i_s)
        for i_s in (
            I_S_HISTORICAL,
            I_S_CITED_LOW,
            I_S_CITED_CENTRAL,
            8.0,
            I_S_CITED_HIGH,
        )
    }
    for i_s, value in values.items():
        print(f"  I_S = {i_s:>4.1f} -> conditional P1 arithmetic = {pct(value)}")

    check(
        "I_S=2 conditional map equals historical delta_PT",
        abs(values[I_S_HISTORICAL] - DELTA_PT_HISTORICAL) < 1e-15,
    )
    check(
        "I_S=4 maps to about 3.85%",
        abs(100.0 * values[I_S_CITED_LOW] - 3.85) < 0.05,
    )
    check(
        "I_S=6 maps to about 5.77%",
        abs(100.0 * values[I_S_CITED_CENTRAL] - 5.77) < 0.05,
    )
    check(
        "I_S=10 maps to about 9.62%",
        abs(100.0 * values[I_S_CITED_HIGH] - 9.62) < 0.05,
    )
    check(
        "factor-three comparison is exact arithmetic",
        abs(values[I_S_CITED_CENTRAL] / values[I_S_HISTORICAL] - 3.0) < 1e-15,
    )
    return values


def part_d_source_firewall() -> None:
    print("\n" + "=" * 72)
    print("PART D: Source-scope firewall")
    print("=" * 72)

    note = read_note()
    compact = " ".join(note.lower().split())
    check(
        "source note contains no stale UV bridge attribution",
        not any(marker in compact for marker in STALE_BRIDGE_MARKERS),
    )
    check(
        "source note contains no retained-alpha authority wording",
        not any(marker in compact for marker in RETAINED_ALPHA_AUTHORITY_MARKERS),
    )
    check(
        "source note contains no unsupported historical semantic selector",
        not any(marker in compact for marker in FORBIDDEN_HISTORICAL_SEMANTICS),
    )
    check(
        "source note links the unaudited conditional alpha certificate",
        "canonical_plaquette_alpha_lm_value_certificate_bounded_note_2026-06-16.md"
        in compact
        and "current ledger row is unaudited" in compact
        and "not retained authority for the physical/canonical choice" in compact,
    )


def part_e_open_gates() -> None:
    print("\n" + "=" * 72)
    print("PART E: Open selector and transport gates")
    print("=" * 72)

    note = read_note()
    compact = " ".join(note.split())
    check(
        "historical delta_PT is conditional arithmetic under I_S=2",
        "conditional arithmetic under the separate historical `I_S = 2` convention"
        in compact,
    )
    check(
        "historical delta_PT is explicitly not a lattice BZ result",
        "not a lattice BZ result" in compact,
    )
    check(
        "same/additive/superseding physical relation remains open",
        "same, additive, or superseding physical contribution remains open" in compact,
    )
    check(
        "source-action and NLO interpretations remain open",
        "source-action" in compact
        and "any NLO matching interpretation remain open" in compact,
    )
    check(
        "Ward cancellation remains open",
        "Ward-cancellation gate remains open" in compact,
    )
    check(
        "exact operator/scheme transfer remains open",
        "exact operator/scheme transfer remains open" in compact,
    )
    check(
        "publication propagation remains open",
        "Propagation of the conditional P1 map into any publication-surface table"
        in compact,
    )


def part_f_disposition(values: Dict[float, float]) -> None:
    print("\n" + "=" * 72)
    print("PART F: Arithmetic-only disposition")
    print("=" * 72)

    note = read_note()
    check(
        "safe claim is explicitly conditional arithmetic only",
        "This note claims only the conditional arithmetic statements" in note,
    )
    check(
        "no physical relationship is selected",
        "does not select a physical relationship between the two inputs" in note,
    )
    print(f"\n  Historical I_S=2 arithmetic = {pct(DELTA_PT_HISTORICAL)}")
    print(f"  Conditional I_S=6 map       = {pct(values[I_S_CITED_CENTRAL])}")
    print(
        "  Conditional I_S=[4,10] map = "
        f"[{pct(values[I_S_CITED_LOW])}, {pct(values[I_S_CITED_HIGH])}]"
    )
    print("  Physical relationship       = OPEN")


def main() -> int:
    print("=" * 72)
    print("P1 I_S revision verification -- conditional arithmetic runner")
    print("Authority: docs/YT_P1_I_S_REVISION_VERIFICATION_NOTE_2026-04-17.md")
    print("=" * 72)

    part_a_structural_arithmetic()
    part_b_historical_delta_pt()
    values = part_c_conditional_bracket()
    part_d_source_firewall()
    part_e_open_gates()
    part_f_disposition(values)

    print("\n" + "=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print("\nFINAL DISPOSITION:")
    print("  Historical delta_PT: conditional arithmetic under I_S = 2 only.")
    print("  Supplied I_S bracket: conditional arithmetic/provenance only.")
    print("  Same/additive/superseding physical relationship: OPEN.")
    print("  No source-action, NLO, operator-transfer, or physical selector is supplied.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
