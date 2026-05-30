#!/usr/bin/env python3
"""Verifier for PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.

This is a meta-scope verifier, not a physics theorem runner. It checks that the
note stays inside dimensional-analysis and repo-language boundaries.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess

PASS = 0
FAIL = 0


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def has(path: str) -> bool:
    return (ROOT / path).is_file()


def git_origin_has(path: str) -> bool:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "origin/main", path],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    return result.returncode == 0 and path in result.stdout.splitlines()


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")

    check("note exists", NOTE.is_file())
    check("claim type is meta", "**Claim type:** meta" in text)
    check("explicitly no audit verdict", "no audit verdict" in text)
    check("explicitly no new axiom", "adds no axiom" in text and "change the minimal axiom surface" in text)
    check("explicitly no dimensional derivation", "does not derive" in text)
    check("uses native Planck-mass conventional anchor wording", "Planck-mass conventional anchor" in text)
    check("states Buckingham-Pi dimensional-analysis boundary", "Buckingham-Pi" in text)
    check("does not claim zero-anchor SI prediction", "still may not claim a\nzero-anchor SI prediction" in text)
    check("does not include PR-local P1 label", not re.search(r"\\bP1\\b", text))
    check("does not propose retained/effective status", "effective_status_proposal" not in text)
    check("does not hand-author audit status", "audited_clean" not in text and "retained_bounded" not in text)
    check("does not cite PDG as derivation input", "PDG" not in text)

    precedents = [
        "docs/CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md",
        "docs/RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md",
    ]
    for rel in precedents:
        check(f"precedent exists locally: {Path(rel).name}", has(rel))
        check(f"precedent exists on origin/main: {Path(rel).name}", git_origin_has(rel))

    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
