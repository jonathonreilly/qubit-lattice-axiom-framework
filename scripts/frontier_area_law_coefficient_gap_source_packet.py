#!/usr/bin/env python3
"""Verify the bounded area-law coefficient-gap source packet.

Authority note:
    docs/AREA_LAW_COEFFICIENT_GAP_NOTE.md

The runner checks arithmetic, direct authority links, claim-scope firewalls,
and the fresh caches of the component runners. It writes no audit data and
assigns no audit disposition.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import hashlib
import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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
    return (ROOT / rel_path).read_text(encoding="utf-8")


def sha256_file(rel_path: str) -> str:
    return hashlib.sha256((ROOT / rel_path).read_bytes()).hexdigest()


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
    *, runner: str, cache: str, expected_pass: int, verdict_fragment: str
) -> None:
    runner_path = ROOT / runner
    cache_path = ROOT / cache
    check(f"{runner} exists", runner_path.exists(), runner)
    check(f"{cache} exists", cache_path.exists(), cache)
    if not (runner_path.exists() and cache_path.exists()):
        return

    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header = cache_header(text)
    passes, fails = cache_summary(text)
    check(
        f"{runner} cache names the same runner",
        header.get("runner") == runner,
        header.get("runner", "<missing>"),
    )
    check(
        f"{runner} cache records success",
        header.get("status") == "ok" and header.get("exit_code") == "0",
        f"status={header.get('status')} exit={header.get('exit_code')}",
    )
    check(
        f"{runner} cache SHA is fresh",
        header.get("runner_sha256") == sha256_file(runner),
        f"cache={header.get('runner_sha256', '<missing>')}",
    )
    check(
        f"{runner} cache summary matches",
        passes == expected_pass and fails == 0,
        f"PASS={passes} FAIL={fails}",
    )
    check(
        f"{runner} cache preserves its claim boundary",
        verdict_fragment in text,
        verdict_fragment,
    )


def main() -> int:
    print("=" * 78)
    print("AREA-LAW COEFFICIENT-GAP CONDITIONAL SOURCE PACKET")
    print("=" * 78)
    print()

    note_path = "docs/AREA_LAW_COEFFICIENT_GAP_NOTE.md"
    note = read_text(note_path)
    check(
        "source title is the conditional synthesis",
        note.startswith("# Area-Law Coefficient-Gap Conditional Synthesis"),
        note_path,
    )
    check("source has explicit theorem type", "**Type:** positive_theorem" in note, "positive_theorem")
    check(
        "source names the primary runner and cache",
        "**Primary runner:** `scripts/frontier_area_law_coefficient_gap_source_packet.py`" in note
        and "**Primary cache:** `logs/runner-cache/frontier_area_law_coefficient_gap_source_packet.txt`" in note,
        "runner/cache metadata",
    )
    check(
        "source distinguishes supplied conditions from the four-axiom foundation",
        "not supplied by the four framework axioms" in note
        and "They remain\nexplicit premises" in note,
        "premise provenance",
    )

    c_cell = 4.0 / 16.0
    c_simple = 2.0 / 12.0
    half_zone = 0.5
    average_crossings = 2.0 + 2.0 * half_zone
    c_conditional = average_crossings / 12.0
    check("event-cell trace is one quarter", math.isclose(c_cell, 0.25), "4/16")
    check("simple-fiber ceiling is one sixth", math.isclose(c_simple, 1.0 / 6.0), "2/12")
    check("supplied half-zone gives three crossings", math.isclose(average_crossings, 3.0), "2+2*(1/2)")
    check("conditional Widom coefficient is one quarter", math.isclose(c_conditional, 0.25), "3/12")
    check(
        "alternative selector fractions are not fixed by CAR",
        len({round((2.0 + 2.0 * p) / 12.0, 12) for p in (0.25, 0.5, 0.75)}) == 3,
        "p=1/4,1/2,3/4 give distinct coefficients",
    )

    dependencies = [
        "docs/PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md",
        "docs/PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md",
        "docs/AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md",
        "docs/AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md",
        "docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md",
        "docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md",
    ]
    for dependency in dependencies:
        name = Path(dependency).name
        check(f"{name} exists", (ROOT / dependency).exists(), dependency)
        check(f"{name} is cited", name in note, name)

    check(
        "source scopes the representation obstruction exactly",
        "specifically supplied exterior one-form event-cell representation" in note
        and "This exhausts that representation/action" in note,
        "specified action only",
    )
    check(
        "source leaves alternate actions and intrinsic carriers open",
        "other substrate actions" in note and "intrinsic `M_4(C)`" in note,
        "non-universal no-go firewall",
    )
    check(
        "source denies CAR-to-channel laundering",
        "it does not select\nthe normal/tangent channel laws" in note,
        "CAR does not determine dispersions",
    )
    check(
        "source contains no authored audit-history pins",
        all(
            forbidden not in note
            for forbidden in (
                "audited_conditional",
                "retained status",
                "audit verdict on this row",
                "Post-audit update",
            )
        ),
        "no audit-grade or status-history prose",
    )

    components = [
        (
            "scripts/frontier_area_law_quarter_broader_no_go.py",
            "logs/runner-cache/frontier_area_law_quarter_broader_no_go.txt",
            24,
            "simple-fiber Widom class cannot deliver c_inf = 1/4",
        ),
        (
            "scripts/frontier_area_law_primitive_parity_gate_carrier.py",
            "logs/runner-cache/frontier_area_law_primitive_parity_gate_carrier.txt",
            40,
            "under the full supplied\ncarrier-identification premise",
        ),
        (
            "scripts/frontier_area_law_primitive_car_edge_identification.py",
            "logs/runner-cache/frontier_area_law_primitive_car_edge_identification.txt",
            46,
            "CONDITIONAL INSIDE SUPPLIED RANK-FOUR CAR EDGE CONDITIONS",
        ),
        (
            "scripts/frontier_area_law_native_car_semantics_tightening.py",
            "logs/runner-cache/frontier_area_law_native_car_semantics_tightening.txt",
            29,
            "CONDITIONAL ALGEBRAIC EQUIVALENCE ONLY",
        ),
    ]
    for runner, cache, expected_pass, verdict_fragment in components:
        check_cache(
            runner=runner,
            cache=cache,
            expected_pass=expected_pass,
            verdict_fragment=verdict_fragment,
        )

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    if FAIL_COUNT:
        print("Verdict: FAIL; the conditional source packet is inconsistent.")
        return 1
    print("Verdict: bounded conditional source packet.")
    print("The arithmetic and source links are checkable, while physical carrier,")
    print("channel, Widom, and representation premises remain explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
