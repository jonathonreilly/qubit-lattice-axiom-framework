#!/usr/bin/env python3
"""Bounded Shapiro unique-discriminator boundary verifier.

This runner reads the SHA-pinned `shapiro_static_discriminator` cache instead
of hand-entering the phase curves. It verifies the narrow boundary result: the
detector-line proxy phase is reproduced by a static cone-shape lookalike, while
static scheduling remains separated. This is not a retained physical Shapiro
package and not a unique causal-propagation discriminator.
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
    causal = _extract_curve(cache_text, "causal mean curve")
    static_cone = _extract_curve(cache_text, "static cone curve")
    static_schedule = _extract_curve(cache_text, "static schedule curve")
    cone_rmse = _rmse(causal, static_cone)
    schedule_rmse = _rmse(causal, static_schedule)
    header_sha = _extract_header_value(cache_text, "runner_sha256")

    checks = [
        ("static-discriminator cache exits cleanly", _extract_header_value(cache_text, "exit_code") == "0" and _extract_header_value(cache_text, "status") == "ok"),
        ("static-discriminator cache is SHA-fresh", header_sha == _sha(STATIC_RUNNER)),
        ("causal and static-cone curves match to displayed precision", cone_rmse <= 5e-5),
        ("static scheduling remains separated from causal curve", schedule_rmse >= 5e-3),
        (
            "source note is bounded and does not use retained-chain wording",
            "**Claim type:** no_go" in note_text
            and "bounded no-unique-discriminator boundary verifier" in note_text
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
            "not a unique causal-propagation discriminator" in note_text
            and "static cone-shape" in note_text,
        ),
    ]
    payload: dict[str, list[float] | float] = {
        "causal": causal,
        "static_cone": static_cone,
        "static_schedule": static_schedule,
        "cone_rmse": cone_rmse,
        "schedule_rmse": schedule_rmse,
    }
    return checks, payload


def _fmt_curve(values: list[float]) -> str:
    return " ".join(f"{v:+10.4f}" for v in values)


def main() -> int:
    cache_text = STATIC_CACHE.read_text(encoding="utf-8")
    note_text = NOTE.read_text(encoding="utf-8")
    checks, payload = _checks(cache_text, note_text)
    causal = payload["causal"]
    static_cone = payload["static_cone"]
    static_schedule = payload["static_schedule"]
    assert isinstance(causal, list)
    assert isinstance(static_cone, list)
    assert isinstance(static_schedule, list)
    cone_rmse = float(payload["cone_rmse"])
    schedule_rmse = float(payload["schedule_rmse"])
    ok = all(flag for _label, flag in checks)

    print("=" * 88)
    print("SHAPIRO UNIQUE DISCRIMINATOR V2: BOUNDED BOUNDARY VERIFIER")
    print("  cache-backed check against the static-cone no-go boundary")
    print("=" * 88)
    print()
    print("Source cache:")
    print("  logs/runner-cache/shapiro_static_discriminator.txt")
    print()
    print(f"{'mode':>20s} {'c=2.0':>10s} {'c=1.0':>10s} {'c=0.5':>10s} {'c=0.25':>10s}")
    print("-" * 72)
    print(f"{'causal dynamic cone':>20s} {_fmt_curve(causal)}")
    print(f"{'static cone shape':>20s} {_fmt_curve(static_cone)}")
    print(f"{'static scheduling':>20s} {_fmt_curve(static_schedule)}")
    print()
    print("Boundary diagnostics:")
    print(f"  causal vs static-cone RMSE: {cone_rmse:.4f}")
    print(f"  causal vs static-schedule RMSE: {schedule_rmse:.4f}")
    print()
    print("RUNNER CHECKS")
    for label, flag in checks:
        print(f"  [{'PASS' if flag else 'FAIL'}] {label}")
    print()
    print("Safe read:")
    print("  - the detector-line proxy phase is not a unique causal-propagation discriminator")
    print("  - the static cone-shape proxy reproduces the displayed curve")
    print("  - static scheduling remains separated and near-flat")
    print("  - a stricter discriminator needs a second observable beyond this phase line")
    print()
    print(f"ASSERTIONS: {'PASS' if ok else 'FAIL'}")

    # N5 execution certificate (print-only; adds no check and no verdict)
    print()
    print("==============================================================================")
    print("N5 EXECUTION CERTIFICATE")
    print("==============================================================================")
    print(
        "  per_element: checked and not executed - this is a cache-and-note "
        "verifier, so it resolves no matrix element at all. It builds no array and "
        "no operator; its numeric content is three flat lists of four floats "
        "scraped out of an upstream cache file by regular expression, plus two "
        "root-mean-square differences between them."
    )
    print(
        "  per_site: checked and not executed - the four columns are values of the "
        "coupling c at 2.0, 1.0, 0.5 and 0.25, and the detector line referred to in "
        "the safe read lives in the upstream runner, not here. Nothing in this file "
        "carries a position label, and no geometry is constructed for anything to "
        "sit on."
    )
    print(
        "  per_mode: checked and not executed - the column headed mode in the "
        "printed table is a scheme label, listing causal dynamic cone, static cone "
        "shape and static scheduling; those are three ways of generating a curve, "
        "not eigenmodes, momentum labels or normal modes, and no decomposition of "
        "any operator is attempted."
    )
    print(
        "  per_block: checked and not executed - no partition into blocks or "
        "sectors is formed. The only grouping in the file is the three named curve "
        "rows, compared pairwise by the two thresholds this runner owns, cone RMSE "
        "at most 5e-5 and schedule RMSE at least 5e-3, which is a comparison of "
        "whole curves rather than of any block-resolved quantity."
    )
    print(
        "  lattice_wide: checked and not executed, and the important honesty here "
        "is about provenance - the curve agreement this runner reports is not "
        "computed by it. The three curves are read back out of the SHA-pinned cache "
        "of scripts/shapiro_static_discriminator.py, whose freshness is checked by "
        "rehashing that source, and the remaining three checks are substring "
        "presence and absence sweeps over the note markdown. A cache re-read plus a "
        "lexical document sweep is not a whole-system computation, and the runner's "
        "own safe read concedes that a stricter discriminator needs a second "
        "observable beyond this phase line."
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
