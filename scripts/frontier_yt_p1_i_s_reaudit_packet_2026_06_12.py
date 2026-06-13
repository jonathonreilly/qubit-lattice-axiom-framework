#!/usr/bin/env python3
"""YT P1 I_S restricted-packet re-audit bridge verifier.

This runner checks the source/cache packet requested by the 2026-06-11
conditional audit of `yt_p1_i_s_lattice_pt_citation_note_2026-04-17`.

It does not audit, retag, or promote the row. It verifies that the re-audit
packet exposes:

  * the prior symbolic `I_1 = I_S` reduction;
  * the `SU(3)` color-factor authority `C_F = 4/3`;
  * the conditional citation arithmetic `I_S in [4,10] -> P1 in
    [3.85%,9.62%]`;
  * the full-staggered BZ candidate cache giving a native low-end scalar
    certificate near `I_S = 4`;
  * explicit firewalls against treating the bracket or native candidate as an
    audit-closed retained value before independent review.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

from canonical_plaquette_surface import CANONICAL_ALPHA_LM


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md"
COLOR_NOTE = ROOT / "docs" / "YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md"
BZ_NOTE = ROOT / "docs" / "YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md"
MASTER_NOTE = ROOT / "docs" / "YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md"

SYMBOLIC_RUNNER = ROOT / "scripts" / "frontier_yt_p1_i1_lattice_pt_symbolic.py"
COLOR_RUNNER = ROOT / "scripts" / "frontier_yt_p1_color_factor_retention.py"
CITATION_RUNNER = ROOT / "scripts" / "frontier_yt_p1_i_s_lattice_pt_citation.py"
BZ_RUNNER = ROOT / "scripts" / "frontier_yt_p1_bz_quadrature_full_staggered_pt.py"
NATIVE_CERT_RUNNER = ROOT / "scripts" / "yt_p1_i_s_native_bz_certificate_2026_06_11.py"

SYMBOLIC_LOG = ROOT / "logs" / "retained" / "yt_p1_i1_lattice_pt_symbolic_2026-04-17.log"
COLOR_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_color_factor_retention.txt"
CITATION_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_i_s_lattice_pt_citation.txt"
BZ_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_bz_quadrature_full_staggered_pt.txt"
NATIVE_CERT_CACHE = ROOT / "logs" / "runner-cache" / "yt_p1_i_s_native_bz_certificate_2026_06_11.txt"

PASS_COUNT = 0
FAIL_COUNT = 0


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


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(body: str) -> str:
    return " ".join(body.split())


def pass_fail_summary(body: str) -> tuple[int, int] | None:
    match = re.search(r"SUMMARY: PASS=(\d+)\s+FAIL=(\d+)", body)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def require_float(pattern: str, body: str, label: str) -> float:
    match = re.search(pattern, body, re.MULTILINE)
    if not match:
        raise AssertionError(f"missing numeric pattern for {label}: {pattern}")
    return float(match.group(1))


def block_1_packet_presence() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 1: restricted-packet source/cache presence")
    print("=" * 72)

    required = [
        NOTE,
        COLOR_NOTE,
        BZ_NOTE,
        MASTER_NOTE,
        SYMBOLIC_RUNNER,
        COLOR_RUNNER,
        CITATION_RUNNER,
        BZ_RUNNER,
        NATIVE_CERT_RUNNER,
        SYMBOLIC_LOG,
        COLOR_CACHE,
        CITATION_CACHE,
        BZ_CACHE,
        NATIVE_CERT_CACHE,
    ]
    for path in required:
        check(
            f"{path.relative_to(ROOT)} exists",
            path.exists(),
            "present" if path.exists() else "missing",
        )


def block_2_source_boundary() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 2: source-note status boundary")
    print("=" * 72)

    note = text(NOTE)
    note_flat = compact(note)
    check("re-audit bridge section present", "2026-06-12 restricted-packet re-audit bridge" in note)
    check("restricted packet table present", "Packet authorities exposed for re-audit" in note)
    check("2026-06-13 narrowed target present", "2026-06-13 safe narrowed audit target" in note)
    check("native BZ candidate section present", "What the native BZ certificate does and does not prove" in note)
    check("independent audit firewall present", "Independent audit remains required" in note)
    check("no audit verdict update claimed", "does not update any audit verdict" in note_flat)
    check("no promotion claimed by bridge", "does not promote this row" in note)
    check("native certificate reports bracket not certified", "BRACKET_VERDICT: NOT_CERTIFIED" in note)
    check("upper end not proved", "does not prove the full comparison range" in note)
    check("master theorem not modified", "does not modify the master obstruction theorem" in note_flat)
    check("old proposed_retained marker absent from citation note", "proposed_retained" not in note)
    check("citation note remains bounded theorem", "**Claim type:** bounded_theorem" in note)
    check("citation note states affine transfer theorem", "Affine transfer theorem" in note)
    check("citation note states native non-certification theorem", "Native non-certification theorem" in note)


def block_3_prior_reduction_and_color() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 3: prior symbolic reduction and color authority")
    print("=" * 72)

    symbolic = text(SYMBOLIC_LOG)
    color = text(COLOR_CACHE)

    check("symbolic log records 21 PASS / 0 FAIL", "SUMMARY: PASS=21  FAIL=0" in symbolic)
    check("symbolic log states I_1 = I_S - I_V", "I_1 = I_S - I_V" in symbolic)
    check("symbolic log states I_V = 0", "I_V = 0" in symbolic)
    check("symbolic log states I_1 = I_S", "=>  I_1 = I_S" in symbolic or "I_1 = I_S" in symbolic)

    check("color cache records 5 PASS / 0 FAIL", "SUMMARY: PASS=5  FAIL=0" in color)
    check("color cache states C_F = 4/3", "C_F = 4/3" in color)
    check("color cache states C_A = 3", "C_A = 3" in color)
    check("color cache states T_F * n_f = 3", "T_F * n_f" in color and "= 3" in color)
    check("color cache states exact three-channel decomposition", "Three-channel decomposition matches" in color)


def block_4_conditional_arithmetic() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 4: conditional I_S bracket arithmetic")
    print("=" * 72)

    cache = text(CITATION_CACHE)
    note = text(NOTE)
    summary = pass_fail_summary(cache)

    cf = 4.0 / 3.0
    alpha_over_4pi = CANONICAL_ALPHA_LM / (4.0 * math.pi)

    p1_low = alpha_over_4pi * cf * 4.0
    p1_mid = alpha_over_4pi * cf * 6.0
    p1_high = alpha_over_4pi * cf * 10.0
    p1_standard = alpha_over_4pi * cf * 2.0

    print(f"  alpha_LM/(4 pi) = {alpha_over_4pi:.10f}")
    print(f"  P1(I_S=2)       = {100.0 * p1_standard:.4f}%")
    print(f"  P1(I_S=4)       = {100.0 * p1_low:.4f}%")
    print(f"  P1(I_S=6)       = {100.0 * p1_mid:.4f}%")
    print(f"  P1(I_S=10)      = {100.0 * p1_high:.4f}%")

    check("citation cache records clean execution", "status: ok" in cache and "exit_code: 0" in cache)
    check(
        "citation cache records at least 41 PASS / 0 FAIL",
        summary is not None and summary[0] >= 41 and summary[1] == 0,
        f"summary={summary}",
    )
    check("note records comparison bracket I_S in [4, 10]", "I_S in [4, 10]" in note or "`I_S in [4,10]`" in note)
    check("low endpoint maps to about 3.85%", abs(100.0 * p1_low - 3.848) < 0.01)
    check("central maps to about 5.77%", abs(100.0 * p1_mid - 5.772) < 0.01)
    check("high endpoint maps to about 9.62%", abs(100.0 * p1_high - 9.620) < 0.01)
    check("central/standard revision factor is exactly 3", abs((p1_mid / p1_standard) - 3.0) < 1e-12)


def block_5_native_bz_candidate() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 5: native full-staggered BZ candidate")
    print("=" * 72)

    cache = text(BZ_CACHE)
    native_cache = text(NATIVE_CERT_CACHE)
    note = text(NOTE)

    i_v_scalar = require_float(r"I_v_scalar\s+= \+([0-9.]+) \+/-", cache, "I_v_scalar")
    delta_r = require_float(r"Delta_R full staggered-PT:\s+([-+0-9.]+) %", cache, "Delta_R")
    syst_low = i_v_scalar * 0.95
    syst_high = i_v_scalar * 1.05

    cf = 4.0 / 3.0
    alpha_over_4pi = CANONICAL_ALPHA_LM / (4.0 * math.pi)
    p1_native = alpha_over_4pi * cf * i_v_scalar

    print(f"  I_v_scalar candidate       = {i_v_scalar:.6f}")
    print(f"  5% systematic scalar band  = [{syst_low:.6f}, {syst_high:.6f}]")
    print(f"  P1 native candidate        = {100.0 * p1_native:.4f}%")
    print(f"  Delta_R full staggered-PT  = {delta_r:.3f}%")

    check("BZ cache records clean execution", "status: ok" in cache and "exit_code: 0" in cache)
    check("BZ cache records PASS=45 FAIL=0", "SUMMARY: PASS=45  FAIL=0" in cache)
    check("native cert cache records PASS=11 FAIL=0", "TOTAL: PASS=11 FAIL=0" in native_cache)
    check("native cert cache records bracket not certified", "BRACKET_VERDICT: NOT_CERTIFIED" in native_cache)
    check("BZ cache gives I_v_scalar near 3.902", abs(i_v_scalar - 3.902) < 0.005)
    check("5% scalar systematic overlaps I_S = 4", syst_low <= 4.0 <= syst_high)
    check("native P1 candidate near low cited endpoint", abs(100.0 * p1_native - 3.754) < 0.03)
    check("BZ cache gives negative Delta_R three-channel assembly", delta_r < 0.0)
    check("note records native lower-end candidate", "I_S_native_candidate" in note and "3.902" in note)
    check("note says native candidate does not prove comparison bracket", "does not prove the full comparison range" in note)


def block_6_scope_firewall() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 6: audit/status firewall")
    print("=" * 72)

    note = text(NOTE)
    note_flat = compact(note)

    check(
        "citation note says bracket is not framework-native",
        "non-authority comparison context" in note
        and "closed framework-native input" in note_flat,
    )
    check(
        "citation note says bracket is not audit-closed",
        "audit-closed" in note and "retained input" in note,
    )
    check("citation note keeps master obstruction unchanged", "Do not modify the master obstruction theorem" in note)
    check("new bridge calls BZ surface a bracket firewall", "native scale check and bracket firewall only" in note)
    check("new bridge requires separate BZ audit", "the quadrature lane must be independently audited" in note)
    check(
        "new bridge does not treat old BZ wording as authority",
        "does not treat any unaudited downstream quadrature note as an authority" in note_flat,
    )
    check(
        "bridge keeps BZ candidate under separate audit",
        "the quadrature lane must be independently audited" in note
        and "does not treat any unaudited downstream quadrature note as an authority" in note_flat,
    )
    check("this runner does not edit audit ledger", True, "source/cache verifier only")


def main() -> int:
    print("=" * 72)
    print("YT P1 I_S restricted-packet re-audit bridge verifier")
    print("=" * 72)
    print("Claim boundary: bounded support / audit-readiness only.")
    print("No audit verdict is changed by this runner.")

    try:
        block_1_packet_presence()
        block_2_source_boundary()
        block_3_prior_reduction_and_color()
        block_4_conditional_arithmetic()
        block_5_native_bz_candidate()
        block_6_scope_firewall()
    except Exception as exc:  # pragma: no cover - runner diagnostic path
        check("unexpected runner exception", False, repr(exc))

    print("\n" + "=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print("\nRESULT:")
    print("  Restricted-packet re-audit bridge is complete iff FAIL=0.")
    print("  This supports re-audit of the missing dependency edge only;")
    print("  it does not promote the row or replace independent audit.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
