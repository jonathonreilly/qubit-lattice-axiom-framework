#!/usr/bin/env python3
"""Bounded Shapiro unique-discriminator boundary verifier.

This runner reads the SHA-pinned `shapiro_static_discriminator` cache instead
of hand-entering phase curves. It verifies the narrow boundary result: the
position-only cone snapshot has an exact equal-array witness, while the configured
fixed-layer proxy remains separated. This is not a physical Shapiro package
or a causal-propagation theorem.
"""

from __future__ import annotations

import hashlib
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SHAPIRO_UNIQUE_DISCRIMINATOR_V2_NOTE.md"
STATIC_RUNNER = ROOT / "scripts" / "shapiro_static_discriminator.py"
STATIC_CACHE = ROOT / "logs" / "runner-cache" / "shapiro_static_discriminator.txt"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _extract_header_value(cache_text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", cache_text, re.MULTILINE)
    return m.group(1).strip() if m else None


def _extract_curve(cache_text: str, label: str) -> list[float]:
    m = re.search(rf"^\s*{re.escape(label)}:\s*(.+)$", cache_text, re.MULTILINE)
    if not m:
        raise AssertionError(f"missing curve line: {label}")
    return [float(x) for x in re.findall(r"[+-]\d+\.\d+", m.group(1))]


def _rmse(left: list[float], right: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)) / len(left))


def _checks(cache_text: str, note_text: str) -> tuple[list[tuple[str, bool]], dict[str, list[float] | float]]:
    snapshot = _extract_curve(cache_text, "cone snapshot mean curve")
    equal_array = _extract_curve(cache_text, "equal-array witness curve")
    fixed_layer = _extract_curve(cache_text, "fixed-layer proxy curve")
    equal_array_rmse = _rmse(snapshot, equal_array)
    snapshot_span = max(snapshot) - min(snapshot)
    fixed_layer_span = max(fixed_layer) - min(fixed_layer)
    header_sha = _extract_header_value(cache_text, "runner_sha256")

    checks = [
        ("static-discriminator cache exits cleanly", _extract_header_value(cache_text, "exit_code") == "0" and _extract_header_value(cache_text, "status") == "ok"),
        ("static-discriminator cache is SHA-fresh", header_sha == _sha(STATIC_RUNNER)),
        ("cone-snapshot and equal-array curves match to displayed precision", equal_array_rmse <= 5e-5),
        ("fixed-layer proxy span is below 1e-3 rad", fixed_layer_span < 1e-3),
        ("snapshot/fixed-layer span gap exceeds 2e-2 rad", snapshot_span - fixed_layer_span > 2e-2),
        ("static-discriminator cache carries an assertive pass certificate", "ASSERTIONS: PASS" in cache_text),
        (
            "source note is bounded and does not use retained-chain wording",
            "**Claim type:** no_go" in note_text
            and "bounded input-interface/history-label boundary verifier" in note_text
            and "retained Shapiro chain" not in note_text
            and "retained c-dependent" not in note_text
            and "proposed_retained" not in note_text,
        ),
        (
            "source note has no failed archive bridge dependency",
            "archive_unlanded" not in note_text
            and "SHAPIRO_COMPLEX_INTERACTION_NOTE" not in note_text
            and "SHAPIRO_DIAMOND_BRIDGE_NOTE" not in note_text,
        ),
        (
            "source note preserves the no-unique-causality boundary",
            "input-interface/history-label no-go" in note_text
            and "equal-array witness" in note_text,
        ),
    ]
    payload: dict[str, list[float] | float] = {
        "snapshot": snapshot,
        "equal_array": equal_array,
        "fixed_layer": fixed_layer,
        "equal_array_rmse": equal_array_rmse,
        "snapshot_span": snapshot_span,
        "fixed_layer_span": fixed_layer_span,
    }
    return checks, payload


def _fmt_curve(values: list[float]) -> str:
    return " ".join(f"{v:+10.4f}" for v in values)


def main() -> int:
    cache_text = STATIC_CACHE.read_text(encoding="utf-8")
    note_text = NOTE.read_text(encoding="utf-8")
    checks, payload = _checks(cache_text, note_text)
    snapshot = payload["snapshot"]
    equal_array = payload["equal_array"]
    fixed_layer = payload["fixed_layer"]
    assert isinstance(snapshot, list)
    assert isinstance(equal_array, list)
    assert isinstance(fixed_layer, list)
    equal_array_rmse = float(payload["equal_array_rmse"])
    snapshot_span = float(payload["snapshot_span"])
    fixed_layer_span = float(payload["fixed_layer_span"])
    ok = all(flag for _label, flag in checks)

    print("=" * 88)
    print("SHAPIRO UNIQUE DISCRIMINATOR V2: BOUNDED BOUNDARY VERIFIER")
    print("  cache-backed check of the input-interface/history-label no-go boundary")
    print("=" * 88)
    print()
    print("Source cache:")
    print("  logs/runner-cache/shapiro_static_discriminator.txt")
    print()
    print(f"{'mode':>20s} {'q=2.0':>10s} {'q=1.0':>10s} {'q=0.5':>10s} {'q=0.25':>10s}")
    print("-" * 72)
    print(f"{'cone snapshot':>20s} {_fmt_curve(snapshot)}")
    print(f"{'equal-array witness':>20s} {_fmt_curve(equal_array)}")
    print(f"{'fixed-layer proxy':>20s} {_fmt_curve(fixed_layer)}")
    print()
    print("Boundary diagnostics:")
    print(f"  snapshot vs equal-array RMSE: {equal_array_rmse:.4f}")
    print(f"  cone-snapshot span: {snapshot_span:.4f}")
    print(f"  fixed-layer span: {fixed_layer_span:.4f}")
    print()
    print("RUNNER CHECKS")
    for label, flag in checks:
        print(f"  [{'PASS' if flag else 'FAIL'}] {label}")
    print()
    print("Safe read:")
    print("  - the supplied kernel receives a position-only cone snapshot, not a causal history")
    print("  - the equal-array witness reproduces the displayed curve on the unconstrained input surface")
    print("  - the configured fixed-layer proxy remains separated and near-flat")
    print("  - no physically admissible static solution is constructed by this verifier")
    print()
    print(f"ASSERTIONS: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
