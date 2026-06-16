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
  * the corrected full-staggered BZ cache and the 2026-06-16 correction
    surfaces that quarantine the earlier `I_S = 3.902` native-replacement
    route;
  * explicit firewalls against treating either surface as an audit-closed
    retained value before independent review.
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
CANONICAL_CERT_NOTE = ROOT / "docs" / "CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md"
PLAQUETTE_NOTE = ROOT / "docs" / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
MASTER_NOTE = ROOT / "docs" / "YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md"
CORRECTION_NOTE = ROOT / "docs" / "YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md"

SYMBOLIC_RUNNER = ROOT / "scripts" / "frontier_yt_p1_i1_lattice_pt_symbolic.py"
COLOR_RUNNER = ROOT / "scripts" / "frontier_yt_p1_color_factor_retention.py"
CITATION_RUNNER = ROOT / "scripts" / "frontier_yt_p1_i_s_lattice_pt_citation.py"
BZ_RUNNER = ROOT / "scripts" / "frontier_yt_p1_bz_quadrature_full_staggered_pt.py"

SYMBOLIC_LOG = ROOT / "logs" / "retained" / "yt_p1_i1_lattice_pt_symbolic_2026-04-17.log"
COLOR_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_color_factor_retention.txt"
CITATION_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_i_s_lattice_pt_citation.txt"
BZ_CACHE = ROOT / "logs" / "runner-cache" / "frontier_yt_p1_bz_quadrature_full_staggered_pt.txt"
CORRECTED_DELTA_CACHE = ROOT / "logs" / "runner-cache" / "yt_p1_delta_r_corrected_bound_memsafe.txt"
FERMION_REGULATOR_CACHE = ROOT / "logs" / "runner-cache" / "yt_p1_fermion_regulator_verification_memsafe.txt"

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
        CANONICAL_CERT_NOTE,
        PLAQUETTE_NOTE,
        MASTER_NOTE,
        CORRECTION_NOTE,
        SYMBOLIC_RUNNER,
        COLOR_RUNNER,
        CITATION_RUNNER,
        BZ_RUNNER,
        SYMBOLIC_LOG,
        COLOR_CACHE,
        CITATION_CACHE,
        BZ_CACHE,
        CORRECTED_DELTA_CACHE,
        FERMION_REGULATOR_CACHE,
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
    check("native BZ quarantine section present", "Quarantine of the native BZ certificate" in note)
    check("independent audit firewall present", "Independent audit remains required" in note)
    check("no audit verdict update claimed", "does not update any audit verdict" in note_flat)
    check("supplied bracket remains non-retained by default", "supplied bracket is not load-bearing" in note_flat)
    check("upper end not proved", "does not prove or import the upper end" in note_flat)
    check("obsolete native route is explicitly quarantined", "prior native-quadrature replacement route is now quarantined" in note_flat)
    check("obsolete native cache is not a bracket replacement", "no audit should treat the obsolete `3.902` native-BZ cache as a replacement" in note_flat)
    check("corrected native derivation gate explicit", "re-derived taste-normalized/full-doubler computation" in note_flat)
    check("master theorem not modified", "does not modify the master obstruction theorem" in note_flat)
    check("old proposed-retained marker absent from citation note", ("proposed_" + "retained") not in note)
    check("citation note remains bounded theorem", "**Claim type:** bounded_theorem" in note)
    check("citation note keeps legacy conditional arithmetic", "conditional arithmetic lemma" in note)
    check("citation note names quarantine repair witness", "quarantine/repair witness" in note)
    check("citation note links native BZ row as markdown dependency", "](YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md)" in note)
    check("citation note links canonical alpha certificate", "](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md)" in note)
    check("citation note links parent plaquette surface", "](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)" in note)
    check("citation note links correction surface", "](YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md)" in note)


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


def block_3b_canonical_alpha_certificate() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 3b: canonical alpha/plaquette value certificate")
    print("=" * 72)

    cert = text(CANONICAL_CERT_NOTE)
    cert_flat = compact(cert)
    bz = text(BZ_NOTE)
    p1 = text(NOTE)

    check("canonical certificate exists", CANONICAL_CERT_NOTE.exists())
    check("canonical certificate is bounded theorem", "**Claim type:** bounded_theorem" in cert)
    check("canonical certificate says no new axiom", "No new axiom" in cert)
    check("canonical certificate says parent plaquette is not derived", "does not derive the Wilson plaquette value" in cert_flat)
    check("canonical certificate links plaquette parent", "](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)" in cert)
    check("canonical certificate displays alpha_LM/(4pi)", "alpha_LM/(4pi)" in cert)
    check("BZ note links canonical certificate", "](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md)" in bz)
    check(
        "P1 note names canonical alpha certificate",
        "canonical arithmetic constants" in p1
        and "CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md" in p1,
    )


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
    check("note records supplied bracket I_S in [4, 10]", "I_S in [4, 10]" in note or "`I_S in [4,10]`" in note)
    check("low endpoint maps to about 3.85%", abs(100.0 * p1_low - 3.848) < 0.01)
    check("central maps to about 5.77%", abs(100.0 * p1_mid - 5.772) < 0.01)
    check("high endpoint maps to about 9.62%", abs(100.0 * p1_high - 9.620) < 0.01)
    check("central/standard revision factor is exactly 3", abs((p1_mid / p1_standard) - 3.0) < 1e-12)


def block_5_native_bz_quarantine() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 5: corrected native full-staggered BZ quarantine")
    print("=" * 72)

    cache = text(BZ_CACHE)
    note = text(NOTE)
    correction = text(CORRECTION_NOTE)
    correction_flat = compact(correction)
    corrected_delta = text(CORRECTED_DELTA_CACHE)
    fermion_regulator = text(FERMION_REGULATOR_CACHE)

    i_v_scalar = require_float(r"I_v_scalar\s+= \+([0-9.]+) \+/-", cache, "I_v_scalar")
    delta_r = require_float(r"Delta_R full staggered-PT:\s+([-+0-9.]+) %", cache, "Delta_R")
    corrected_i_s = require_float(
        r"corrected I_S \(no /N_TASTE\) = ([0-9.]+)",
        corrected_delta,
        "corrected I_S",
    )

    print(f"  corrected I_v_scalar cache = {i_v_scalar:.6f}")
    print(f"  corrected Delta_R cache    = {delta_r:.3f}%")
    print(f"  corrected scalar I_S scale = {corrected_i_s:.3f}")

    check("BZ cache records clean execution", "status: ok" in cache and "exit_code: 0" in cache)
    check("BZ cache records PASS=44 FAIL=0", "SUMMARY: PASS=44  FAIL=0" in cache)
    check("corrected BZ cache gives I_v_scalar near 32.435", abs(i_v_scalar - 32.435) < 0.005)
    check("corrected BZ cache gives positive Delta_R diagnostic", delta_r > 0.0)
    check("correction cache records clean execution", "status: ok" in corrected_delta and "exit_code: 0" in corrected_delta)
    check("fermion regulator cache records clean execution", "status: ok" in fermion_regulator and "exit_code: 0" in fermion_regulator)
    check("corrected scalar I_S is about 32.4, not 3.90", abs(corrected_i_s - 32.432) < 0.01)
    check("corrected BZ cache marks old scalar bracket invalid", "corrected full-BZ = 32.435 is outside prior [3.0, 7.0]" in cache)
    check("corrected BZ cache marks fermion channel as artifact", "not a matching constant" in cache)
    check("correction note names /N_TASTE double-count", "/N_TASTE = 16" in correction and "double-count" in correction)
    check("correction note records fermion regulator dependence", "IR-regulator-dependent" in correction or "regulator-dependent" in correction_flat)
    check("corrected Delta_R cache records uncontrolled O(50%) bound", "O(50%) uncontrolled quantity" in corrected_delta)
    check("fermion regulator cache records doubler-log disease", "15 unsubtracted doubler-logs" in fermion_regulator)
    check("note records obsolete 3.902 quarantine", "obsolete `3.902` native-BZ cache" in note)
    check("note records corrected scalar cache value", "corrected scalar cache value       =  32.435" in note)
    check("note blocks P1_native arithmetic from obsolete value", "must not compute or advertise a `P1_native` number from `3.902`" in compact(note))
    check("old native P1 central value absent", "3.754%" not in note)
    check("old native P1 systematic band absent", "[3.566%, 3.942%]" not in note)
    check("old native candidate variable absent", "I_S_native_candidate" not in note)
    check("old bracket-import removal claim absent", "removes the need to import that range for the native candidate" not in note)


def block_6_scope_firewall() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 6: audit/status firewall")
    print("=" * 72)

    note = text(NOTE)
    note_flat = compact(note)

    check("citation note says legacy bracket is not retained by default", "no audit should treat the bracket as retained unless the bracket itself is separately accepted" in note_flat)
    check("citation note keeps master obstruction unchanged", "Do not modify the master obstruction theorem" in note)
    check("new bridge quarantines obsolete BZ surface", "quarantined obsolete supplier" in note)
    check("new bridge requires future native replacement audit", "Independent audit remains required" in note and "future native-BZ replacement" in note)
    check(
        "new bridge does not treat literature bracket as native authority",
        "literature bracket remains parallel context only" in note_flat,
    )
    check(
        "bridge does not treat obsolete BZ candidate as retained authority",
        "Independent audit remains required" in note
        and "obsolete native-BZ cache as authority" in note,
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
        block_3b_canonical_alpha_certificate()
        block_4_conditional_arithmetic()
        block_5_native_bz_quarantine()
        block_6_scope_firewall()
    except Exception as exc:  # pragma: no cover - runner diagnostic path
        check("unexpected runner exception", False, repr(exc))

    print("\n" + "=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print("\nRESULT:")
    print("  Restricted-packet quarantine bridge is complete iff FAIL=0.")
    print("  This supports re-audit of the repaired dependency boundary only;")
    print("  it does not promote the row, restore the obsolete native value,")
    print("  or replace independent audit.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
