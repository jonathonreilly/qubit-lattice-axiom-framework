#!/usr/bin/env python3
"""Bridge verifier for the architecture-portability live re-audit target."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded/work-history-unverifiable-portability-2026-04-30/ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md"
LIVE_NOTE = ROOT / "docs/ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md"
BRIDGE_NOTE = ROOT / "docs/ARCHITECTURE_PORTABILITY_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md"
RUNNER = ROOT / "scripts/frontier_architecture_portability_sweep.py"
CACHE = ROOT / "logs/runner-cache/frontier_architecture_portability_sweep.txt"
FIREWALL = ROOT / "scripts/archive_architecture_portability_firewall_2026_06_16.py"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}" + (f": {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"[FAIL] {label}" + (f": {detail}" if detail else ""))


def read(path: Path) -> str:
    check(f"path exists: {path.relative_to(ROOT)}", path.exists())
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_field(cache: str, field: str) -> str | None:
    m = re.search(rf"^{re.escape(field)}: (.+)$", cache, re.MULTILINE)
    return m.group(1).strip() if m else None


def main() -> int:
    print("=" * 88)
    print("ARCHITECTURE PORTABILITY LIVE REAUDIT BRIDGE")
    print("=" * 88)

    archive = read(ARCHIVE)
    live = read(LIVE_NOTE)
    bridge = read(BRIDGE_NOTE)
    runner = read(RUNNER)
    cache = read(CACHE)
    firewall = read(FIREWALL)

    for phrase in [
        "RETRACTED 2026-04-30",
        "archived `audited_failed` / retracted",
        "not a live authority",
        "must not be",
        "ARCHITECTURE_PORTABILITY_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md",
    ]:
        check(f"archive boundary phrase: {phrase}", phrase in archive)

    for phrase in [
        "scripts/frontier_architecture_portability_sweep.py",
        "Architecture Portability Sweep",
        "ordered 3D cubic",
        "staggered 3D cubic",
        "Wilson 3D cubic",
        "Random geometric",
        "This is a portability companion, not a standalone Newton closure.",
        "Wilson Born rule is not measured",
        "mass exponent beta measures deflection proportional to source mass",
    ]:
        check(f"live note phrase: {phrase}", phrase in live)

    for phrase in [
        "source-side re-audit bridge",
        "old archived row remains a failed historical packet",
        "bounded finite configured sweep",
        "does not edit audit results",
        "standalone Newton closure",
        "Wilson Born-rule measurement",
        "retained or retained-bounded effective status",
    ]:
        check(f"bridge boundary phrase: {phrase}", phrase in bridge)

    for phrase in [
        "class Ordered3D",
        "class Staggered3D",
        "class Wilson3D",
        "class RandomGeometric",
        "SOURCE_AMPLITUDES",
        "born_rule_i3",
        "overall = gate_beta and gate_attract and gate_born",
    ]:
        check(f"runner substantive marker: {phrase}", phrase in runner)

    check("firewall checks archive retirement", "archived-audit evidence firewall holds" in firewall)
    check("cache points to primary runner", cache_field(cache, "runner") == "scripts/frontier_architecture_portability_sweep.py")
    check("cache exits cleanly", cache_field(cache, "exit_code") == "0")
    check("cache status ok", cache_field(cache, "status") == "ok")
    check("cache sha matches runner", cache_field(cache, "runner_sha256") == sha256(RUNNER))

    for phrase in [
        "ARCHITECTURE PORTABILITY SWEEP",
        "ordered_3d               0.9999",
        "staggered_3d             1.0125",
        "wilson_3d                1.0005",
        "random_geometric         0.9989",
        "beta within 10% of 1.0: 4/4 architectures",
        "Attractive force:       4/4 architectures",
        "Born rule I_3 < 1e-6:   all measured pass",
        "OVERALL: PASS",
        "bounded source-mass portability companion established",
    ]:
        check(f"cache result phrase: {phrase}", phrase in cache)

    # Guard the boundary that the random-geometric row and Wilson Born row do
    # not silently become stronger claims.
    check("random geometric row is scoped to 2D mass-only", "Random Geometric Graph (2D mass-only" in cache)
    check("Wilson row has no Born I3 measurement", "wilson_3d" in cache and "wilson_3d                1.0005   1.0000       YES          n/a      PASS" in cache)

    print("=" * 88)
    print(f"SUMMARY: ARCHITECTURE PORTABILITY LIVE REAUDIT BRIDGE PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
