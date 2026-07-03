#!/usr/bin/env python3
"""Verify that the teleportation acceptance-suite note matches live probes.

The audited failure for ``docs/TELEPORTATION_ACCEPTANCE_SUITE_NOTE.md`` was a
documentation/source sync issue: the strict-lane profile in the note omitted
present runner probes. This guard executes the live list-probes surfaces and
checks that the note's strict-lane inventory table exactly matches the current
``--strict-lane --list-probes`` output.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


AUDIT_TIMEOUT_SEC = 30
ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "frontier_teleportation_acceptance_suite.py"
NOTE = ROOT / "docs" / "TELEPORTATION_ACCEPTANCE_SUITE_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")


def list_surface(*args: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(RUNNER), *args, "--list-probes"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


def parse_list_surface(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split(None, 2)
        if len(parts) != 3:
            raise ValueError(f"cannot parse list-probes row: {raw!r}")
        rows.append((parts[0], parts[1], parts[2].strip()))
    return rows


TABLE_ROW_RE = re.compile(
    r"^\|\s*`(?P<key>[^`]+)`\s*\|\s*(?P<category>[^|]+?)\s*\|\s*`(?P<script>[^`]+)`\s*\|\s*$"
)


def parse_note_strict_table(text: str) -> list[tuple[str, str, str]]:
    marker = "synchronized inventory:"
    start = text.find(marker)
    if start < 0:
        raise ValueError("note is missing the synchronized inventory marker")
    rows: list[tuple[str, str, str]] = []
    in_table = False
    for raw in text[start:].splitlines():
        line = raw.strip()
        if line.startswith("| probe key |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table:
            if not line.startswith("|"):
                break
            match = TABLE_ROW_RE.match(line)
            if not match:
                raise ValueError(f"cannot parse note inventory row: {raw!r}")
            rows.append(
                (
                    match.group("key").strip(),
                    match.group("category").strip(),
                    match.group("script").strip(),
                )
            )
    return rows


def main() -> int:
    print("=" * 96)
    print("TELEPORTATION ACCEPTANCE SUITE NOTE SYNC CHECK")
    print("=" * 96)

    default_code, default_stdout, default_stderr = list_surface()
    strict_code, strict_stdout, strict_stderr = list_surface("--strict-lane")

    check(
        "default --list-probes exits zero",
        default_code == 0,
        default_stderr.strip(),
    )
    check(
        "strict-lane --list-probes exits zero",
        strict_code == 0,
        strict_stderr.strip(),
    )

    default_rows = parse_list_surface(default_stdout)
    strict_rows = parse_list_surface(strict_stdout)
    note_rows = parse_note_strict_table(NOTE.read_text(encoding="utf-8"))

    default_keys = {key for key, _category, _script in default_rows}
    strict_keys = {key for key, _category, _script in strict_rows}
    optional_default_keys = {
        "adiabatic_prep_hook",
        "taste_readout_operator_hook",
        "bell_measurement_circuit_hook",
        "cross_encoding_hook",
    }

    check(
        "default surface still includes the documented optional hook keys",
        optional_default_keys.issubset(default_keys),
        f"missing={sorted(optional_default_keys - default_keys)}",
    )
    check(
        "strict-lane surface replaces default optional hooks with present-gated strict probes",
        optional_default_keys.isdisjoint(strict_keys),
        f"unexpected={sorted(optional_default_keys & strict_keys)}",
    )
    check(
        "note strict-lane inventory table exactly matches live strict-lane surface",
        note_rows == strict_rows,
        f"note_rows={len(note_rows)} live_rows={len(strict_rows)}",
    )
    check(
        "strict-lane live surface has the expected current row count",
        len(strict_rows) == 24,
        f"rows={len(strict_rows)}",
    )

    print()
    print("Strict-lane synchronized rows:")
    for key, category, script in strict_rows:
        print(f"  {key:38s} {category:19s} {script}")

    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
