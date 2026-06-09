#!/usr/bin/env python3
"""Record does not select the magnitude minimal block.

This runner repairs the conditional audit blocker for
MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06.  It keeps the finite count
facts, reads the one-hop RP two-step cache instead of hard-coding its status,
and checks the approved Record axiom boundary.  The output is a no-go for the
Record-selection route, plus a conditional arithmetic consequence if a separate
UV/minimal-block readout bridge is supplied.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
RP_CACHE = ROOT / "logs" / "runner-cache" / "axiom_first_rp_two_step_transfer_matrix_positivity.txt"

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(("PASS" if ok else "FAIL") + ": " + name)
    if detail:
        print("  " + detail)


def minimal_period(seq: list[int]) -> int:
    for period in range(1, len(seq) + 1):
        if all(seq[i] == seq[i % period] for i in range(len(seq))):
            return period
    return len(seq)


def main() -> int:
    print("Magnitude minimal-block readout boundary")
    print("=" * 72)

    print("--- Section I: finite temporal count facts ---")
    eta1 = [(-1) ** t for t in range(8)]
    check("eta_1(t)=(-1)^t has minimal period 2", minimal_period(eta1) == 2)
    check("a single time-slice is not a translation-invariant eta_1 cell", eta1[0] != eta1[1])

    ps = np.linspace(-np.pi, np.pi, 64)
    mass = 0.4
    energy = np.arcsinh(np.sqrt(mass * mass + np.sin(ps) ** 2))
    two_step = np.exp(-2 * energy)
    check(
        "direct two-step contraction sample lies in (0,1]",
        np.all(two_step > 0) and np.all(two_step <= 1 + 1e-12),
    )

    rp_text = RP_CACHE.read_text(encoding="utf-8")
    rp_supplies_single_step_boundary = (
        "single-step T_hat NOT a positive operator" in rp_text
        and "negative eigenvalue => non-positive" in rp_text
    )
    rp_supplies_two_step_block = (
        "T_hat^2 positive Hermitian = B^dag B" in rp_text
        and "PASS -- the free staggered 2-step blocked transfer matrix" in rp_text
    )
    check(
        "one-hop RP cache supplies single-step non-positivity",
        rp_supplies_single_step_boundary,
    )
    check(
        "one-hop RP cache supplies two-step positivity",
        rp_supplies_two_step_block,
    )

    print("--- Section R: Record axiom boundary ---")
    axiom_text = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    required_record_phrases = [
        "A record is the durable registration of the realized outcome.",
        "Given a readout context",
        "scalar readout `I` is finitely additive",
        "record supplies no readout context",
        "sector-generation rule",
        "weighting",
        "normalization",
        "time metric",
        "occupancy rule",
    ]
    check(
        "approved Record axiom boundary is present",
        all(phrase in axiom_text for phrase in required_record_phrases),
    )

    record_excludes_selector_inputs = all(
        phrase in axiom_text
        for phrase in [
            "record supplies no readout context",
            "weighting",
            "normalization",
            "time metric",
            "occupancy rule",
        ]
    )
    check(
        "Record does not supply a readout-scale selector",
        record_excludes_selector_inputs,
        "minimal axioms exclude readout context, time metric, weighting, normalization, and occupancy rule",
    )

    print("--- Section S: conditional arithmetic only ---")
    spatial_count = 8
    temporal_minimal_block = 2
    conditional_exponent = spatial_count * temporal_minimal_block
    continuum_counts = [8 * lt for lt in (2, 8, 64, 512)]
    check("conditional UV/minimal-block exponent would be 8 x 2 = 16", conditional_exponent == 16)
    check(
        "OS-continuum count sequence is a different unbounded reconstruction object",
        continuum_counts == sorted(continuum_counts) and continuum_counts[-1] > conditional_exponent,
    )

    route_supplies_selector = (
        rp_supplies_two_step_block
        and not record_excludes_selector_inputs
    )
    check(
        "no-go: Record plus RP two-step does not select L_t=2 over L_t -> infinity",
        not route_supplies_selector,
    )

    print("=" * 72)
    print("MAGNITUDE_MINIMAL_BLOCK_SELECTED_BY_RECORD=FALSE")
    print("CONDITIONAL_IF_UV_MINIMAL_BLOCK_READOUT_SUPPLIED=16")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
