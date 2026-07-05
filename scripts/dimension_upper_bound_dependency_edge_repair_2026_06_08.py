#!/usr/bin/env python3
"""Verify the dimension upper-bound dependency-edge repair note."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


PATHS = {
    "repair": "docs/DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md",
    "wrapper": "docs/DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    "lower": "docs/DIMENSION_SELECTION_NOTE.md",
    "bertrand": "docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "coulomb": "docs/COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "gate": "docs/D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md",
    "bertrand_runner": "scripts/bertrand_stable_orbit_green_kernel_bridge.py",
    "coulomb_runner": "scripts/frontier_coulomb_stability_scaling_repair.py",
    "gate_runner": "scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py",
    "repair_cache": "logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt",
    "bertrand_cache": "logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt",
    "coulomb_cache": "logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt",
    "gate_cache": "logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt",
}


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def text(label: str) -> str:
    rel = PATHS[label]
    path = ROOT / rel
    report(f"{rel} exists", path.exists())
    return path.read_text(encoding="utf-8") if path.exists() else ""


def flat(s: str) -> str:
    return " ".join(s.split())


def cites(body: str, rel: str) -> bool:
    return rel in body or Path(rel).name in body


def source_anchor_checks() -> None:
    repair = text("repair")
    wrapper = text("wrapper")
    lower = text("lower")
    bertrand = text("bertrand")
    coulomb = text("coulomb")
    gate = text("gate")

    for label in (
        "bertrand_runner",
        "coulomb_runner",
        "gate_runner",
        "bertrand_cache",
        "coulomb_cache",
        "gate_cache",
    ):
        text(label)

    repair_paths = [
        PATHS["wrapper"],
        PATHS["bertrand"],
        PATHS["coulomb"],
        PATHS["gate"],
        PATHS["bertrand_runner"],
        PATHS["coulomb_runner"],
        PATHS["gate_runner"],
        PATHS["bertrand_cache"],
        PATHS["coulomb_cache"],
        PATHS["gate_cache"],
    ]
    for path in repair_paths:
        report(f"repair note cites {path}", cites(repair, path))

    wrapper_paths = [
        PATHS["repair"],
        PATHS["bertrand"],
        PATHS["coulomb"],
        PATHS["gate"],
    ]
    for path in wrapper_paths:
        report(f"wrapper cites {path}", cites(wrapper, path))

    report(
        "repair note states source-only boundary",
        "apply an audit verdict" in repair
        and "edit `docs/audit/**`" in repair
        and "audit_required_before_effective_retained: true" in repair
        and "bare_retained_allowed: false" in repair,
    )
    report(
        "repair note is classified as meta dependency-edge certificate, not theorem queue",
        "claim_type_author_hint: meta" in repair
        and "**Claim type:** meta" in repair
        and "**Type:** meta / dependency-edge certificate" in repair
        and "canonical claim type is `meta`" in repair
        and "not a positive theorem" in flat(repair)
        and "not a theorem-grade dimension-selection claim" in flat(repair)
        and "separate parent dimension-selection theorem" in repair
        and "prove the parent dimension-selection theorem" in repair
        and "actual_current_surface_status: bounded-support" in repair
        and "claim_type_author_hint: bounded_theorem" not in repair
        and "**Type:** bounded source-graph repair" not in repair,
    )
    report(
        "wrapper has 2026-06-08 repair section",
        "2026-06-08 dependency-edge source repair" in wrapper
        and "one-hop bounded support packets" in flat(wrapper),
    )
    report(
        "wrapper records native stable-orbit import retirement",
        "native stable-orbit import retirement" in wrapper
        and "U_stable = {d : d <= 3}" in wrapper
        and "full Bertrand closed-orbit theorem as an imported premise" in wrapper,
    )
    report(
        "lower note remains finite lower-bound support",
        "lower-bound support only" in lower
        and "not a unique-dimension\ntheorem" in lower,
    )
    report(
        "stable support keeps full closed-orbit boundary",
        "does not prove the full Bertrand closed-orbit theorem" in bertrand
        and "not consumed by the current finite-set composition" in bertrand
        and "not claim a complete framework-internal proof" in bertrand,
    )
    report(
        "Coulomb support remains bounded",
        "does not establish a framework-native electromagnetic sector" in coulomb
        and "does not prove a full hydrogenic `d = 3` spectrum" in coulomb,
    )
    report(
        "D3 gate records finite composition",
        "L_runner = {3,4,5}" in gate
        and "L_runner intersect {d : d <= 3} = {3}" in gate
        and "L_runner intersect {d : d <= 4} = {3,4}" in gate,
    )
    report(
        "no status retag language in wrapper repair",
        "effective_status" not in wrapper
        and "audited_clean" not in wrapper
        and "retag" not in flat(wrapper).lower(),
    )


def composition_checks() -> None:
    lower_set = {3, 4, 5}
    checked = set(range(1, 9))
    stable_upper = {d for d in checked if d <= 3}
    atomic_weak_upper = {d for d in checked if d <= 4}
    atomic_strict = {3}

    report("lower support set is {3,4,5}", lower_set == {3, 4, 5})
    report("native stable upper set is d<=3", stable_upper == {1, 2, 3})
    report("weak atomic upper set is d<=4", atomic_weak_upper == {1, 2, 3, 4})
    report("lower intersect native stable edge is {3}", lower_set & stable_upper == {3})
    report("lower intersect weak atomic is {3,4}", lower_set & atomic_weak_upper == {3, 4})
    report("lower intersect strict atomic spectrum is {3}", lower_set & atomic_strict == {3})
    report(
        "native stable route is decisive under weak atomic scope",
        (lower_set & stable_upper) == {3}
        and (lower_set & atomic_weak_upper) != {3},
    )
    report("atomic route is compatible with selected d=3", 3 in (lower_set & atomic_weak_upper))


def cache_checks() -> None:
    bertrand_cache = text("bertrand_cache")
    coulomb_cache = text("coulomb_cache")
    gate_cache = text("gate_cache")
    report("stable-orbit cache certifies PASS=8", "SCORECARD: PASS=8" in bertrand_cache)
    report("Coulomb cache certifies PASS=53 FAIL=0", "SUMMARY: PASS=53 FAIL=0" in coulomb_cache)
    report("D3 gate cache certifies PASS=34 FAIL=0", "SUMMARY: PASS=34 FAIL=0" in gate_cache)


def main() -> int:
    print("Dimension upper-bound dependency-edge repair")
    print("=" * 72)
    source_anchor_checks()
    composition_checks()
    cache_checks()
    print("=" * 72)
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
