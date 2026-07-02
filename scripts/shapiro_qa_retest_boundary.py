#!/usr/bin/env python3
"""Bounded QA verifier for the Shapiro phase-lane retest note.

This runner checks the existing phase-lag and static-discriminator caches as
numeric QA evidence, while keeping status language out of scope. It does not
promote the Shapiro phase lag to retained physics and does not cite archived
failed bridge rows as live dependencies.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SHAPIRO_QA_RETEST_NOTE.md"
PHASE_RUNNER = ROOT / "scripts" / "shapiro_phase_lag_probe.py"
STATIC_RUNNER = ROOT / "scripts" / "shapiro_static_discriminator.py"
PHASE_CACHE = ROOT / "logs" / "runner-cache" / "shapiro_phase_lag_probe.txt"
STATIC_CACHE = ROOT / "logs" / "runner-cache" / "shapiro_static_discriminator.txt"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _header_value(text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def _curve(text: str, label: str) -> list[float]:
    m = re.search(rf"^\s*{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    if not m:
        raise AssertionError(f"missing curve line: {label}")
    return [float(x) for x in re.findall(r"[+-]\d+\.\d+", m.group(1))]


def _rmse(left: list[float], right: list[float]) -> float:
    return (sum((a - b) ** 2 for a, b in zip(left, right)) / len(left)) ** 0.5


def _phase_spreads(phase_text: str) -> list[float]:
    spreads: list[float] = []
    for line in phase_text.splitlines():
        if not re.match(r"^\|\s*\d", line):
            continue
        cells = [cell.strip(" `") for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            m = re.search(r"([0-9]+\.[0-9]+)", cells[2])
            if m:
                spreads.append(float(m.group(1)))
    return spreads


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    phase = PHASE_CACHE.read_text(encoding="utf-8")
    static = STATIC_CACHE.read_text(encoding="utf-8")
    causal = _curve(static, "causal mean curve")
    cone = _curve(static, "static cone curve")
    schedule = _curve(static, "static schedule curve")
    cone_rmse = _rmse(causal, cone)
    schedule_rmse = _rmse(causal, schedule)
    phase_spreads = _phase_spreads(phase)

    checks = [
        ("phase-lag cache exits cleanly", _header_value(phase, "exit_code") == "0" and _header_value(phase, "status") == "ok"),
        ("phase-lag cache is SHA-fresh", _header_value(phase, "runner_sha256") == _sha(PHASE_RUNNER)),
        ("static-discriminator cache exits cleanly", _header_value(static, "exit_code") == "0" and _header_value(static, "status") == "ok"),
        ("static-discriminator cache is SHA-fresh", _header_value(static, "runner_sha256") == _sha(STATIC_RUNNER)),
        ("phase replay has exact instantaneous zero control", "phase lag `0.000 rad`" in phase or "c = inst" in phase),
        ("phase replay family spread is bounded by 2.5e-4 rad", bool(phase_spreads) and max(phase_spreads) <= 2.5e-4),
        ("static cone reproduces causal curve to displayed precision", cone_rmse <= 5e-5),
        ("static scheduling remains separated", schedule_rmse >= 5e-3),
        (
            "source note is bounded QA and has no retained/archived live dependency wording",
            "bounded QA cache-verifier" in note
            and "archive_unlanded" not in note
            and "retained notes" not in note
            and "retained Shapiro" not in note,
        ),
        (
            "source note preserves claim boundary",
            "not a retained physical Shapiro package" in note
            and "not a unique" in note
            and "causal discriminator" in note,
        ),
    ]
    ok = all(flag for _label, flag in checks)

    print("=" * 88)
    print("SHAPIRO QA RETEST: BOUNDED CACHE VERIFIER")
    print("  phase-lag replay cache + static-discriminator cache")
    print("=" * 88)
    print()
    print(f"phase replay max spread: {max(phase_spreads) if phase_spreads else float('nan'):.4g}")
    print(f"static cone RMSE: {cone_rmse:.4f}")
    print(f"static schedule RMSE: {schedule_rmse:.4f}")
    print()
    print("RUNNER CHECKS")
    for label, flag in checks:
        print(f"  [{'PASS' if flag else 'FAIL'}] {label}")
    print()
    print("Safe read:")
    print("  - this is bounded QA over existing caches")
    print("  - archived failed bridge rows are not live dependencies")
    print("  - static-cone mimic remains the no-unique-discriminator boundary")
    print("  - no tracker issue is implied by the checked caches")
    print()
    print(f"ASSERTIONS: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
