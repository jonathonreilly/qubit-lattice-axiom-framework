#!/usr/bin/env python3
"""Primary audit runner for the SU(3) Wigner Block 4/5 narrow split.

The source note has two computational limbs:
  - Block 4 staging claims (1)-(5), verified by the existing L=3 cube runner.
  - Block 5 orientation diagnostics claims (6)-(7), verified by the new
    geometry-only L=2 PBC runner.

The audit graph records one primary runner per note, so this wrapper makes the
whole cleanable core visible as one runner without re-implementing either limb.
Classification hint: finite plaquette enumeration and lattice configuration
counts are delegated to the two source runners below.
"""

from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "SU3_WIGNER_BLOCK4_STAGING_BLOCK5_ORIENTATION_DIAGNOSTICS_NARROW_THEOREM_NOTE_2026-05-10.md"
)

STATUS_PIN_RE = re.compile(
    r"\b(?:retained(?:_[a-z]+)?|unaudited|audited_[a-z_]+|"
    r"audit_in_progress|"
    r"(?:effective|intrinsic|audit)_status)\b",
    re.IGNORECASE,
)
REQUIRED_STATUS_BOUNDARIES = (
    "Current dependency status is pipeline-derived.",
    "This consumer does not inherit audit status from Blocks 1-3.",
    "It does not consume Block 1's corrected `H` values or channel ordering.",
)

RUNNERS = [
    (
        "Block 4 staging",
        "scripts/frontier_su3_wigner_l3_cube_partition.py",
        "SUMMARY: THEOREM PASS=5 FAIL=0",
    ),
    (
        "Block 5 orientation diagnostics",
        "scripts/frontier_su3_wigner_block5_orientation_diagnostics_narrow.py",
        "SUMMARY: PASS=11 FAIL=0",
    ),
]

FORBIDDEN_IMPORTS = {
    "frontier_su3_cube_index_graph_shortcut_open_gate",
    "frontier_su3_wigner_l2_cube_orientation_verification",
}


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            out.add(node.module)
    return out


def check_note_status_firewall() -> None:
    check("consumer note exists", NOTE_PATH.exists(), str(NOTE_PATH.relative_to(ROOT)))
    if not NOTE_PATH.exists():
        return

    note = NOTE_PATH.read_text(encoding="utf-8", errors="replace")
    normalized_note = " ".join(note.split())
    pinned = sorted({match.group(0) for match in STATUS_PIN_RE.finditer(note)})
    check(
        "consumer note contains no authored audit-status pins",
        not pinned,
        ", ".join(pinned),
    )
    check(
        "consumer note requires pipeline-derived current status",
        REQUIRED_STATUS_BOUNDARIES[0] in normalized_note,
        REQUIRED_STATUS_BOUNDARIES[0],
    )
    check(
        "consumer note states no-inheritance and H/order boundaries",
        all(marker in normalized_note for marker in REQUIRED_STATUS_BOUNDARIES[1:]),
        " | ".join(REQUIRED_STATUS_BOUNDARIES[1:]),
    )


def run_runner(label: str, rel_path: str, expected_summary: str) -> None:
    path = ROOT / rel_path
    check(f"{label} runner exists", path.exists(), rel_path)
    if not path.exists():
        return

    imports = imported_modules(path)
    forbidden = sorted(
        module for module in imports
        if module in FORBIDDEN_IMPORTS or module.split(".")[0] in FORBIDDEN_IMPORTS
    )
    check(f"{label} avoids open-gate runner imports", not forbidden, ", ".join(forbidden))

    env = dict(os.environ)
    env["PYTHONPATH"] = str(ROOT / "scripts")
    result = subprocess.run(
        [sys.executable, rel_path],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=AUDIT_TIMEOUT_SEC - 20,
        check=False,
    )
    print(f"\n--- {label} stdout tail ---")
    print("\n".join(result.stdout.splitlines()[-35:]))
    if result.stderr.strip():
        print(f"\n--- {label} stderr ---")
        print(result.stderr.strip())

    check(f"{label} exits 0", result.returncode == 0, f"returncode={result.returncode}")
    check(
        f"{label} expected summary present",
        expected_summary in result.stdout,
        expected_summary,
    )


def main() -> int:
    print("SU(3) Wigner Block 4/5 narrow split primary runner")
    print("=" * 72)
    check_note_status_firewall()
    for label, rel_path, expected_summary in RUNNERS:
        run_runner(label, rel_path, expected_summary)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
