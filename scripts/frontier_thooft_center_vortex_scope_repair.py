#!/usr/bin/env python3
"""Scope-boundary checker for the 't Hooft center-vortex open gate."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
PRIMARY = ROOT / "scripts" / "frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py"

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
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def has_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


def main() -> int:
    print("'t Hooft center-vortex open-gate scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")

    print()
    print("A. Permanent open-gate boundary")
    print("-" * 72)
    check("note declares open_gate", "**Claim type:** open_gate" in note)
    check("note has no source-local status authority", "Status authority" not in note)
    check(
        "note says permanent external-context catalogue",
        has_phrase(note, "permanent `open_gate` external-context catalogue"),
    )
    check(
        "note says audit should not close confinement theorem",
        has_phrase(note, "not treat the row as a confinement theorem"),
    )
    check(
        "note excludes all positive closure targets",
        has_phrase(note, "does not ask audit to close monopole condensation")
        and has_phrase(note, "center-vortex condensation/percolation")
        and has_phrase(note, "a Wilson-loop area law")
        and "`sigma > 0`" not in note,
    )
    check(
        "note leaves future bridge theorem route explicit",
        "future retained bridge theorem" in note
        and "framework observable identification" in note,
    )
    check(
        "source checker does not claim to apply audit result",
        has_phrase(note, "does not apply an audit result")
        and has_phrase(note, "promote the row beyond `open_gate`"),
    )
    check(
        "note declares pure-notation source boundary",
        "2026-06-07 Pure-Notation Source Boundary" in note
        and "P_THOOFT_REG" in note,
    )
    check(
        "note says references are labels, not retained authority",
        has_phrase(note, "bibliographic labels for the notation being catalogued")
        and has_phrase(note, "not a retained authority packet"),
    )
    check(
        "note excludes published-context support claim",
        has_phrase(note, "no published-context support claim")
        and has_phrase(note, "pure syntactic vocabulary registration"),
    )
    check(
        "note requires separate retained bridge for theorem use",
        has_phrase(note, "later use as a theorem input")
        and has_phrase(note, "separate retained bridge theorem"),
    )

    print()
    print("B. Primary runner replay")
    print("-" * 72)
    result = subprocess.run(
        [sys.executable, str(PRIMARY.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check("primary runner exits cleanly", result.returncode == 0, f"returncode={result.returncode}")
    check("primary runner reports no failures", "FAIL=0" in output)
    check("primary runner enforces open_gate declaration", "T8: boundary" in output and "open_gate" in output)
    check("primary runner enforces no substrate identification", "does NOT claim substrate identification" in output)
    check("primary runner enforces no hierarchy closure", "does NOT claim alpha_LM^16" in output)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: row is ready for re-audit as a permanent open_gate.")
        return 0
    print("VERDICT: center-vortex scope repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
