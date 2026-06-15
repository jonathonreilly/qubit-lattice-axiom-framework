#!/usr/bin/env python3
"""Audit companion for the Wilson test-mass / finite-L distance-law packet.

The source note is a bounded Wilson companion. This runner checks the packet
surface that the note actually retains:

* test-mass source scaling from the completed test-mass cache;
* first-order perturbative mass scaling from the completed perturbative cache;
* the finite-L open-Wilson distance-law table from the completed continuum
  cache;
* explicit demotion of the L -> infinity extrapolation to diagnostic-only
  status.

It does not promote the Wilson lane to full Newton closure, does not close
both-masses or action-reaction, and does not turn the diagnostic extrapolation
into retained scope.
"""

from __future__ import annotations

import py_compile
import re
from pathlib import Path
from typing import TYPE_CHECKING

import runner_cache as rc

if TYPE_CHECKING:
    # Packet-visible helper references for build_citation_graph.py.
    import frontier_continuum_limit as _frontier_continuum_limit
    import frontier_newton_systematic as _frontier_newton_systematic
    import frontier_perturbative_mass_law as _frontier_perturbative_mass_law
    import frontier_test_mass_limit as _frontier_test_mass_limit


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_TEST_MASS_CONTINUUM_NOTE_2026-04-11.md"
RUNNERS = [
    "scripts/frontier_test_mass_limit.py",
    "scripts/frontier_perturbative_mass_law.py",
    "scripts/frontier_continuum_limit.py",
    "scripts/frontier_newton_systematic.py",
]

EXPECTED_TABLE = {
    12: (-1.827, 0.9991),
    15: (-1.932, 0.9993),
    18: (-1.973, 0.9997),
    20: (-1.965, 0.9999),
    22: (-1.982, 0.9999),
    25: (-2.002, 0.9999),
}

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def cache_text(runner: str) -> tuple[dict | None, str]:
    cache_path, header, text = rc.load_cache(runner)
    check(f"{runner} cache exists", cache_path.exists(), cache_path.relative_to(ROOT).as_posix())
    check(f"{runner} cache is SHA-fresh", rc.cache_status(runner) == "fresh", rc.cache_status(runner))
    if header is not None:
        check(f"{runner} cache header names runner", header.get("runner_path") == runner, str(header.get("runner_path")))
        check(
            f"{runner} cache header SHA matches source",
            header.get("runner_sha256") == rc.runner_sha256(runner),
        )
    else:
        check(f"{runner} cache header parses", False)
    return header, text or ""


def part0_note_boundaries() -> None:
    section("Part 0: source-note boundaries")
    check("source note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "**Claim type:** bounded_theorem",
        "finite-L distance-law table is the binding evidence",
        "continuum extrapolation becomes a diagnostic-only readout",
        "Diagnostic-only (out of audited scope)",
        "not as a retained",
        "continuum-limit fact",
        "does **not** promote",
        "as a retained repo truth",
        "both-masses closure is still open",
        "action-reaction remains unresolved",
        "same-convention Wilson result, not a global architecture claim",
        "scripts/audit_companion_wilson_test_mass_continuum_finite_l_packet_2026_06_15.py",
    ]
    for marker in required:
        check(f"note contains marker: {marker[:62]}", marker in text or marker in flat)
    forbidden = [
        "full Newton closure is retained",
        "action-reaction is closed",
        "both-masses closure is closed",
        "architecture-independent Newton closure is closed",
    ]
    for marker in forbidden:
        check(f"forbidden overclaim absent: {marker}", marker not in text)


def part1_supporting_sources_compile() -> None:
    section("Part 1: supporting source runners compile")
    for runner in RUNNERS:
        path = ROOT / runner
        check(f"{runner} exists", path.exists())
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            check(f"{runner} py_compile", False, str(exc))
        else:
            check(f"{runner} py_compile", True)


def part2_fast_completed_caches() -> None:
    section("Part 2: completed fast/cache-backed subclaims")
    header, text = cache_text("scripts/frontier_test_mass_limit.py")
    check("test-mass cache exited cleanly", header is not None and header.get("status") == "ok" and header.get("exit_code") == "0")
    check("test-mass source-mass exponent recorded", "|a_test| ~ M_source^1.002" in text)
    check("test-mass inward acceleration recorded", "[TOWARD]" in text and "Mass exponent fit" in text)

    header, text = cache_text("scripts/frontier_perturbative_mass_law.py")
    check("perturbative cache exited cleanly", header is not None and header.get("status") == "ok" and header.get("exit_code") == "0")
    check("perturbative exact mass exponent recorded", "MASS EXPONENT: |a_pert| ~ M_B^1.0000" in text)
    check("perturbative first-order boundary recorded", "At first order in G" in text)


def parse_note_table(text: str) -> dict[int, tuple[float, float]]:
    rows: dict[int, tuple[float, float]] = {}
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*`(-?\d+\.\d+)`\s*\|\s*`(\d+\.\d+)`\s*\|", text, re.MULTILINE):
        rows[int(m.group(1))] = (float(m.group(2)), float(m.group(3)))
    return rows


def parse_continuum_cache_table(text: str) -> dict[int, tuple[float, float]]:
    rows: dict[int, tuple[float, float]] = {}
    pattern = re.compile(r"^\s*(\d+)\s*\|\s*(-\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|", re.MULTILINE)
    for m in pattern.finditer(text):
        side = int(m.group(1))
        if side in EXPECTED_TABLE:
            rows[side] = (float(m.group(2)), float(m.group(3)))
    return rows


def part3_finite_l_distance_table() -> None:
    section("Part 3: finite-L distance-law table")
    note_text = NOTE.read_text(encoding="utf-8")
    note_rows = parse_note_table(note_text)
    check("note table has expected L rows", set(note_rows) == set(EXPECTED_TABLE), str(sorted(note_rows)))
    for side, expected in EXPECTED_TABLE.items():
        observed = note_rows.get(side)
        check(
            f"note table L={side} alpha/R2 matches rounded retained row",
            observed == expected,
            f"observed={observed} expected={expected}",
        )

    header, text = cache_text("scripts/frontier_continuum_limit.py")
    check("continuum cache completed under long timeout", header is not None and header.get("status") == "ok" and header.get("exit_code") == "0")
    rows = parse_continuum_cache_table(text)
    check("continuum cache has all finite-L summary rows", set(rows) == set(EXPECTED_TABLE), str(sorted(rows)))
    for side, (expected_alpha, expected_r2) in EXPECTED_TABLE.items():
        alpha, r2 = rows.get(side, (999.0, 0.0))
        check(
            f"cache L={side} alpha rounds to source-note table",
            round(alpha, 3) == expected_alpha,
            f"cache={alpha:.4f} note={expected_alpha:.3f}",
        )
        check(
            f"cache L={side} R2 rounds to source-note table",
            round(r2, 4) == expected_r2,
            f"cache={r2:.6f} note={expected_r2:.4f}",
        )
    check("largest L finite table is near inverse square", abs(rows.get(25, (999.0, 0.0))[0] + 2.0) < 0.005)


def part4_diagnostic_firewall_and_nonbinding_sweep() -> None:
    section("Part 4: diagnostic/firewall checks")
    note_text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(note_text.split())
    header, text = cache_text("scripts/frontier_newton_systematic.py")
    check(
        "systematic cache is treated as nonbinding support if compute-limited",
        header is not None and header.get("status") in {"ok", "timeout"},
        str(header.get("status") if header else None),
    )
    systematic_text = (ROOT / "scripts/frontier_newton_systematic.py").read_text(encoding="utf-8")
    systematic_flat = " ".join(systematic_text.split())
    check(
        "systematic source boundary forbids global normalization verdict",
        "not to claim that `4*pi` was or was not the source of earlier discrepancies" in systematic_flat,
    )
    diagnostic_markers = [
        "extrapolation model selection",
        "independently",
        "justified in this note",
        "out of audited scope",
        "diagnostic-only readout",
        "Promoting that extrapolation to a continuum- limit fact requires a separately retained justification",
    ]
    for marker in diagnostic_markers:
        check(f"diagnostic firewall marker present: {marker[:58]}", marker in note_text or marker in flat)


def main() -> int:
    print("WILSON TEST-MASS / FINITE-L DISTANCE-LAW AUDIT PACKET")
    part0_note_boundaries()
    part1_supporting_sources_compile()
    part2_fast_completed_caches()
    part3_finite_l_distance_table()
    part4_diagnostic_firewall_and_nonbinding_sweep()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
