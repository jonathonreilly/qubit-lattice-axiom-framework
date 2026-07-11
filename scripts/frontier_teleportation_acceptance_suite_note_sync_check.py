#!/usr/bin/env python3
"""Verify that the teleportation acceptance-suite note matches live probes.

The audited failure for ``docs/TELEPORTATION_ACCEPTANCE_SUITE_NOTE.md`` was a
documentation/source sync issue: the strict-lane profile in the note omitted
present runner probes. This guard executes both live list-probes surfaces and
checks that the note's default and strict-lane inventory tables exactly match
them. It also checks the strict-lane profile composition so a table update
cannot silently change the default-required prefix or retain default-only
optional hooks.
"""

from __future__ import annotations

import hashlib
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


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
DEFAULT_TABLE_MARKER = "Current synchronized default inventory:"
STRICT_TABLE_MARKER = "Current synchronized strict inventory:"


def parse_note_table(text: str, marker: str) -> list[tuple[str, str, str]]:
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"note is missing inventory marker: {marker!r}")
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
    print(f"acceptance_runner_sha256: {file_sha256(RUNNER)}")
    print(f"note_sha256: {file_sha256(NOTE)}")
    print()

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
    note_text = NOTE.read_text(encoding="utf-8")
    note_default_rows = parse_note_table(note_text, DEFAULT_TABLE_MARKER)
    note_strict_rows = parse_note_table(note_text, STRICT_TABLE_MARKER)

    default_required_rows = [row for row in default_rows if row[1] == "required"]
    default_optional_rows = [row for row in default_rows if row[1] == "optional"]
    default_optional_keys = {
        key for key, _category, _script in default_optional_rows
    }
    strict_keys = {key for key, _category, _script in strict_rows}
    strict_additions = strict_rows[len(default_required_rows) :]

    check(
        "note default inventory table exactly matches live default surface",
        note_default_rows == default_rows,
        f"note_rows={len(note_default_rows)} live_rows={len(default_rows)}",
    )
    check(
        "note strict-lane inventory table exactly matches live strict-lane surface",
        note_strict_rows == strict_rows,
        f"note_rows={len(note_strict_rows)} live_rows={len(strict_rows)}",
    )
    check(
        "default surface is exactly eight required rows then four optional rows",
        len(default_required_rows) == 8
        and len(default_optional_rows) == 4
        and default_rows == default_required_rows + default_optional_rows,
        f"required_rows={len(default_required_rows)} optional_rows={len(default_optional_rows)}",
    )
    check(
        "strict-lane surface retains the default required prefix in order",
        strict_rows[: len(default_required_rows)] == default_required_rows,
        f"required_rows={len(default_required_rows)}",
    )
    check(
        "strict-lane surface replaces default optional hooks with present-gated strict probes",
        default_optional_keys.isdisjoint(strict_keys),
        f"unexpected={sorted(default_optional_keys & strict_keys)}",
    )
    check(
        "strict-lane has exactly sixteen required-if-present additions",
        len(strict_additions) == 16
        and all(row[1] == "required-if-present" for row in strict_additions),
        f"addition_rows={len(strict_additions)}",
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
