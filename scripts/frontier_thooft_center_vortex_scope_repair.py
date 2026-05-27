#!/usr/bin/env python3
"""Scope-boundary checker for the 't Hooft center-vortex open gate."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
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


def main() -> int:
    print("'t Hooft center-vortex open-gate scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][
        "thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow_theorem_note_2026-05-16"
    ]

    print()
    print("A. Permanent open-gate boundary")
    print("-" * 72)
    check("note declares open_gate", "**Claim type:** open_gate" in note)
    check(
        "note says permanent external-context catalogue",
        "permanent\n`open_gate` external-context catalogue" in note,
    )
    check(
        "note says audit should not close confinement theorem",
        "not treat the row as a confinement theorem" in note,
    )
    check(
        "note excludes all positive closure targets",
        "does not ask audit to close monopole condensation" in note
        and "center-vortex condensation/percolation" in note
        and "a Wilson-loop area law" in note
        and "`sigma > 0`" not in note,
    )
    check(
        "note leaves future bridge theorem route explicit",
        "future retained bridge theorem" in note
        and "framework observable identification" in note,
    )

    print()
    print("B. Current ledger row")
    print("-" * 72)
    check("row audit_status is audited_conditional before pipeline", row.get("audit_status") == "audited_conditional", str(row.get("audit_status")))
    check("row claim_type is open_gate", row.get("claim_type") == "open_gate", str(row.get("claim_type")))
    check("row has no open dependency paths", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check(
        "row records missing bridge theorem",
        "missing_bridge_theorem" in (row.get("notes_for_re_audit_if_any") or ""),
    )

    print()
    print("C. Primary runner replay")
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
