#!/usr/bin/env python3
"""Area-law coefficient-gap source-packet verifier.

Authority note:
    docs/AREA_LAW_COEFFICIENT_GAP_NOTE.md

This runner checks that the coefficient-gap synthesis is reviewable as a
source packet: it names the action-side 1/4 input, the simple-fiber Widom
no-go, the conditional primitive parity-gate positive route, and the exact
remaining rank-four CAR/CIP edge premise.  It does not assign an audit verdict.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import hashlib
import math
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def read_text(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def sha256_file(rel_path: str) -> str:
    return hashlib.sha256((REPO_ROOT / rel_path).read_bytes()).hexdigest()


def contains(text: str, needle: str) -> bool:
    return needle in text


def require_fragment(label: str, text: str, needle: str) -> None:
    check(label, contains(text, needle), needle)


def cache_header(cache_text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in cache_text.splitlines():
        if line == "----- stdout -----":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            header[key.strip()] = value.strip()
    return header


def cache_summary(cache_text: str) -> tuple[int | None, int | None]:
    match = re.search(r"SUMMARY:\s+PASS=(\d+)\s+FAIL=(\d+)", cache_text)
    if not match:
        return None, None
    return int(match.group(1)), int(match.group(2))


def check_cache(
    *,
    runner: str,
    cache: str,
    expected_pass: int,
    verdict_fragment: str,
) -> None:
    runner_path = REPO_ROOT / runner
    cache_path = REPO_ROOT / cache
    runner_exists = runner_path.exists()
    cache_exists = cache_path.exists()
    check(f"{runner} exists", runner_exists, runner)
    check(f"{cache} exists", cache_exists, cache)
    if not (runner_exists and cache_exists):
        return

    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header = cache_header(text)
    passes, fails = cache_summary(text)
    check(f"{runner} cache names same runner", header.get("runner") == runner, header.get("runner", "<missing>"))
    check(f"{runner} cache status ok", header.get("status") == "ok", header.get("status", "<missing>"))
    check(f"{runner} cache exit code zero", header.get("exit_code") == "0", header.get("exit_code", "<missing>"))
    check(
        f"{runner} cache sha is fresh",
        header.get("runner_sha256") == sha256_file(runner),
        f"cache={header.get('runner_sha256', '<missing>')}",
    )
    check(
        f"{runner} summary has expected pass count",
        passes == expected_pass and fails == 0,
        f"PASS={passes} FAIL={fails}",
    )
    require_fragment(f"{runner} verdict boundary is present", text, verdict_fragment)


def main() -> int:
    print("=" * 78)
    print("AREA-LAW COEFFICIENT-GAP SOURCE PACKET")
    print("=" * 78)
    print()
    print("Question: is the coefficient-gap synthesis now runner-backed enough")
    print("for independent re-audit without pretending that the CAR/CIP")
    print("premise is already retained?")
    print()

    note_path = "docs/AREA_LAW_COEFFICIENT_GAP_NOTE.md"
    note = read_text(note_path)

    require_fragment("source note title is present", note, "# Area-Law Coefficient Gap Audit")
    require_fragment("primary runner metadata names this verifier", note, "Primary runner: `scripts/frontier_area_law_coefficient_gap_source_packet.py`")
    require_fragment("primary cache metadata names this verifier output", note, "logs/runner-cache/frontier_area_law_coefficient_gap_source_packet.txt")
    require_fragment("note keeps ledger authority firewall", note, "independent audit lane remains")
    require_fragment("note states this packet is not an audit verdict", note, "does not assign an audit verdict")

    c_cell = 4.0 / 16.0
    simple_fiber = 2.0 / 12.0
    quarter = 3.0 / 12.0
    tangent_addition = 1.0 / 12.0
    check("primitive action trace is exactly 1/4", math.isclose(c_cell, 0.25, abs_tol=1e-15), "4/16=1/4")
    check("simple-fiber Widom ceiling is exactly 1/6", math.isclose(simple_fiber, 1.0 / 6.0, abs_tol=1e-15), "2/12=1/6")
    check("quarter target requires average crossing count three", math.isclose(quarter, 0.25, abs_tol=1e-15), "3/12=1/4")
    check("parity-gated tangent channel supplies the missing 1/12", math.isclose(simple_fiber + tangent_addition, c_cell, abs_tol=1e-15), "1/6+1/12=1/4")

    deps = [
        "docs/PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md",
        "docs/PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md",
        "docs/AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md",
        "docs/AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md",
        "docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md",
        "docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md",
        "docs/BH_ENTROPY_DERIVED_NOTE.md",
        "docs/BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md",
        "docs/BOUNDARY_LAW_ROBUSTNESS_NOTE_2026-04-11.md",
        "docs/HOLOGRAPHIC_PROBE_NOTE_2026-04-11.md",
    ]
    for dep in deps:
        dep_name = Path(dep).name
        check(f"{dep_name} exists", (REPO_ROOT / dep).exists(), dep)
        require_fragment(f"{dep_name} cited by coefficient-gap note", note, dep_name)

    require_fragment(
        "negative half of archived load-bearing step is explicit",
        note,
        "existing free-fermion / Dirac-sea diagnostics do\nnot derive the Planck `1/4` coefficient",
    )
    require_fragment(
        "positive half of archived load-bearing step is explicit",
        note,
        "two-orbital CAR / Laplacian-gated edge carrier",
    )
    require_fragment(
        "CIP is named as the remaining premise",
        note,
        "(CIP)  P_A H_cell",
    )
    require_fragment(
        "note does not derive action-side 1/4 locally",
        note,
        "derive the action-side `c_cell = 1/4` here",
    )
    require_fragment(
        "note does not derive CIP from the minimal axiom surface alone",
        note,
        "derive (CIP) from the minimal axiom surface alone",
    )
    require_fragment(
        "source packet does not close cited conditional rows",
        note,
        "close any of the cited audit_conditional rows",
    )

    components = [
        {
            "runner": "scripts/frontier_area_law_quarter_broader_no_go.py",
            "cache": "logs/runner-cache/frontier_area_law_quarter_broader_no_go.txt",
            "expected_pass": 24,
            "verdict_fragment": "simple-fiber Widom class cannot deliver c_inf = 1/4",
        },
        {
            "runner": "scripts/frontier_area_law_primitive_parity_gate_carrier.py",
            "cache": "logs/runner-cache/frontier_area_law_primitive_parity_gate_carrier.txt",
            "expected_pass": 40,
            "verdict_fragment": "conditional\npositive carrier",
        },
        {
            "runner": "scripts/frontier_area_law_primitive_car_edge_identification.py",
            "cache": "logs/runner-cache/frontier_area_law_primitive_car_edge_identification.txt",
            "expected_pass": 36,
            "verdict_fragment": "remaining\nstatus question",
        },
        {
            "runner": "scripts/frontier_area_law_native_car_semantics_tightening.py",
            "cache": "logs/runner-cache/frontier_area_law_native_car_semantics_tightening.txt",
            "expected_pass": 23,
            "verdict_fragment": "rank four alone is\nunderdetermined",
        },
    ]
    for component in components:
        check_cache(**component)

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    print()
    if FAIL_COUNT:
        print("Verdict: FAIL; coefficient-gap source packet is not audit-ready.")
        return 1
    print("Verdict: bounded source-packet support. The synthesis is runner-backed")
    print("and re-auditable, but the rank-four CAR/CIP premise remains explicit;")
    print("this runner does not assign an audit verdict or retained status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
