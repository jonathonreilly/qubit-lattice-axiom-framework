#!/usr/bin/env python3
"""Dimension upper-bound wrapper scope certificate.

This runner checks the 2026-06-12 repair to
DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md.
It does not apply an audit verdict. It verifies that the wrapper's
load-bearing upper edge is the native stable-circular-orbit calculation, while
the Coulomb side is only the Green-kernel scaling lemma and no longer imports a
hydrogenic spectrum or atomic-stability theorem.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


PATHS = {
    "wrapper": "docs/DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    "coulomb": "docs/COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "bertrand": "docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "gate": "docs/D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md",
    "edge_runner": "scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py",
    "coulomb_runner": "scripts/frontier_coulomb_stability_scaling_repair.py",
    "bertrand_cache": "logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt",
    "coulomb_cache": "logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt",
    "gate_cache": "logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt",
}


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def read(label: str) -> str:
    rel = PATHS[label]
    path = ROOT / rel
    check(f"{rel} exists", path.exists())
    return path.read_text(encoding="utf-8") if path.exists() else ""


def flat(text: str) -> str:
    return " ".join(text.split())


def source_boundary_checks() -> None:
    wrapper = read("wrapper")
    coulomb = read("coulomb")
    bertrand = read("bertrand")
    gate = read("gate")
    edge_runner = read("edge_runner")
    coulomb_runner = read("coulomb_runner")
    bertrand_cache = read("bertrand_cache")
    coulomb_cache = read("coulomb_cache")
    gate_cache = read("gate_cache")

    wrapper_flat = flat(wrapper)

    check(
        "wrapper has 2026-06-12 Coulomb scope narrowing",
        "2026-06-12 Coulomb companion scope narrowing" in wrapper
        and "Green-kernel scaling lemma" in wrapper,
    )
    check(
        "wrapper names this source-packet runner",
        Path(__file__).name in wrapper,
    )
    check(
        "wrapper keeps native stable orbit as decisive selector",
        "L_runner intersect U_stable = {3}" in wrapper
        and "decisive upper edge remains the\nnative stable-circular-orbit route" in wrapper,
    )
    check(
        "wrapper demotes Coulomb side to compatible support",
        "U_Coulomb_scaling = {d : d <= 4}" in wrapper
        and "L_runner intersect U_Coulomb_scaling = {3,4}" in wrapper
        and "compatible support, not the selector" in wrapper,
    )
    check(
        "wrapper no longer asserts hydrogenic spectrum as load-bearing",
        "standard atomic spectrum with bound states accumulating" not in wrapper
        and "stable hydrogen-like atoms require" not in wrapper
        and "canonical infinite-bound-state Coulomb spectrum" not in wrapper,
    )
    check(
        "wrapper explicitly forbids hydrogenic spectral theorem",
        "no normalizable-ground-state" in wrapper
        and "threshold-accumulation" in wrapper
        and "Rydberg-series claim is load-bearing" in wrapper,
    )
    check(
        "textbook references are parallel context only",
        "not load-bearing authority in this wrapper" in wrapper,
    )
    check(
        "Coulomb support note remains scaling-only",
        "Green-kernel scaling lemma" in coulomb
        and "does not prove a full hydrogenic `d = 3` spectrum" in coulomb
        and "does not establish a framework-native electromagnetic sector" in coulomb,
    )
    check(
        "stable support note keeps full Bertrand theorem out of scope",
        "does not prove the full Bertrand closed-orbit theorem" in bertrand
        and "stable-circular-orbit edge" in bertrand,
    )
    check(
        "D3 gate records finite-set composition",
        "L_runner = {3,4,5}" in gate
        and "L_runner intersect {d : d <= 3} = {3}" in gate
        and "L_runner intersect {d : d <= 4} = {3,4}" in gate,
    )
    check(
        "existing dependency-edge runner stays verdict-free",
        "AUDIT_VERDICT_APPLIED=FALSE" in edge_runner
        and "edit `docs/audit/**`" in (ROOT / "docs/DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md").read_text(encoding="utf-8"),
    )
    check(
        "Coulomb runner says no EM-sector claim",
        "no EM-sector claim" in coulomb_runner
        and "SUMMARY: PASS=53 FAIL=0" in coulomb_runner,
    )
    check("stable-orbit cache PASS=8", "SCORECARD: PASS=8" in bertrand_cache)
    check("Coulomb cache PASS=53 FAIL=0", "SUMMARY: PASS=53 FAIL=0" in coulomb_cache)
    check("D3 gate cache PASS=34 FAIL=0", "SUMMARY: PASS=34 FAIL=0" in gate_cache)
    check(
        "wrapper has no audit-retag authority language",
        "effective_status" not in wrapper
        and "audited_clean" not in wrapper
        and "retag" not in wrapper_flat.lower(),
    )


def finite_set_composition_checks() -> None:
    lower = {3, 4, 5}
    stable_upper = {d for d in range(1, 9) if d <= 3}
    coulomb_scaling_upper = {d for d in range(1, 9) if d <= 4}
    check("lower packet is {3,4,5}", lower == {3, 4, 5})
    check("native stable upper gives {3}", lower & stable_upper == {3})
    check("Coulomb scaling upper gives {3,4}", lower & coulomb_scaling_upper == {3, 4})
    check(
        "Coulomb scaling is not the selector",
        (lower & stable_upper) == {3}
        and (lower & coulomb_scaling_upper) != {3},
    )
    check("Coulomb scaling is compatible with d=3", 3 in (lower & coulomb_scaling_upper))


def main() -> int:
    print("Dimension upper-bound textbook-import wrapper scope certificate")
    print("=" * 72)
    source_boundary_checks()
    finite_set_composition_checks()
    print("=" * 72)
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
