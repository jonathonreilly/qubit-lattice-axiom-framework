#!/usr/bin/env python3
"""Read-only import map for production-dynamics-needed post-record rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
PREV = ROOT / "scripts/frontier_post_record_audit_evidence_ladder_row_bucketing_2026_06_06.py"
PASS = 0
FAIL = 0

ROW_MAP = {
    "chiral_3plus1d_boundary_phase_note": {
        "lane": "boundary_phase_finite_scan",
        "bridges": [
            "boundary_condition_bridge",
            "finite_size_or_continuum_bridge",
            "propagation_mode_or_transfer_bridge",
            "orientation_or_clock_bridge_if_time_directed",
        ],
    },
    "persistent_object_adaptive_readout_note": {
        "lane": "persistent_object_readout_kernel",
        "bridges": [
            "source_object_formation_bridge",
            "detector_readout_or_instrument_bridge",
            "kernel_normalization_bridge",
            "scale_or_generalization_bridge",
        ],
    },
    "persistent_object_readout_localization_note": {
        "lane": "persistent_object_readout_kernel",
        "bridges": [
            "source_object_formation_bridge",
            "detector_readout_or_instrument_bridge",
            "kernel_normalization_bridge",
            "scale_or_generalization_bridge",
        ],
    },
    "persistent_record_matched_compare_note": {
        "lane": "persistent_record_production_overlap",
        "bridges": [
            "record_writing_law_bridge",
            "persistence_or_preservation_bridge",
            "overlap_kernel_physical_bridge",
            "production_time_or_barrier_bridge",
            "comparison_baseline_bridge",
        ],
    },
    "persistent_record_overlap_kernel_note": {
        "lane": "persistent_record_production_overlap",
        "bridges": [
            "record_writing_law_bridge",
            "persistence_or_preservation_bridge",
            "overlap_kernel_physical_bridge",
            "production_time_or_barrier_bridge",
            "comparison_baseline_bridge",
        ],
    },
    "persistent_record_refinement_note": {
        "lane": "persistent_record_production_overlap",
        "bridges": [
            "record_writing_law_bridge",
            "persistence_or_preservation_bridge",
            "overlap_kernel_physical_bridge",
            "production_time_or_barrier_bridge",
            "comparison_baseline_bridge",
        ],
    },
}

EXPECTED_LANE_COUNTS = {
    "boundary_phase_finite_scan": 1,
    "persistent_object_readout_kernel": 2,
    "persistent_record_production_overlap": 3,
}


def load_previous():
    spec = importlib.util.spec_from_file_location("row_bucketing", PREV)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PREV}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prev = load_previous()


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


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def production_rows() -> list[dict]:
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    return [
        row
        for row in rows
        if prev.scoped(row) and prev.classify(row) == "production_dynamics_needed"
    ]


def mapped_row(row: dict) -> dict:
    claim_id = row.get("claim_id")
    item = ROW_MAP.get(claim_id)
    if item is None:
        return {"lane": "unmapped", "bridges": []}
    return item


def row_label(row: dict) -> str:
    mapped = mapped_row(row)
    return (
        f"{row.get('claim_id')} | {mapped['lane']} | "
        f"{row.get('audit_status')} | {row.get('effective_status')} | "
        f"{row.get('claim_type')} | {row.get('note_path')}"
    )


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md",
        [
            "production_dynamics_needed",
            "pre-record laws can carry probabilities",
            "post-record sites carry realized information",
            "Record does not derive the bridge",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/POST_RECORD_AUDIT_EVIDENCE_LADDER_ROW_BUCKETING_2026-06-06.md",
        [
            "production_dynamics_needed",
            "audit ledger hash is unchanged",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "production dynamics | supplied formation/kernel/time bridge",
            "bounded support with open imports",
            "stable settings are not selected dials",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_ORIENTATION_BRIDGE_INTERFACE_2026-06-06.md",
        [
            "production-kernel, Hamiltonian, transfer, or instrument id",
            "This branch does not derive an orientation, clock, or kernel.",
            "Does not derive or select a production kernel.",
        ],
    )


def row_map_checks() -> tuple[list[dict], Counter[str]]:
    section("Production-dynamics row-map checks")
    before = digest(LEDGER)
    rows = production_rows()
    observed_ids = [row.get("claim_id") for row in rows]
    expected_ids = list(ROW_MAP)

    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        buckets[mapped_row(row)["lane"]].append(row)
    counts = Counter({lane: len(items) for lane, items in buckets.items()})

    report("production-dynamics row count is current snapshot", len(rows) == sum(EXPECTED_LANE_COUNTS.values()), str(len(rows)))
    report("expected production-dynamics claim ids match", set(observed_ids) == set(expected_ids), str(observed_ids))
    report("each expected production row appears once", len(observed_ids) == len(set(observed_ids)) == len(expected_ids))
    report("lane counts match expected", dict(counts) == EXPECTED_LANE_COUNTS, str(counts))
    report("lane counts sum to production-dynamics count", sum(counts.values()) == len(rows), str(counts))

    for row in rows:
        claim_id = row.get("claim_id")
        item = mapped_row(row)
        report(f"{claim_id} is mapped", item["lane"] != "unmapped", item["lane"])
        report(f"{claim_id} has supplied-bridge imports", len(item["bridges"]) >= 4, ", ".join(item["bridges"]))

    bridge_counter = Counter()
    for row in rows:
        for bridge in mapped_row(row)["bridges"]:
            bridge_counter[bridge] += 1
    report("boundary bridge is represented", bridge_counter["boundary_condition_bridge"] == 1)
    report("readout instrument bridge is represented", bridge_counter["detector_readout_or_instrument_bridge"] == 2)
    report("record-writing law bridge is represented", bridge_counter["record_writing_law_bridge"] == 3)
    report("production time/barrier bridge is represented", bridge_counter["production_time_or_barrier_bridge"] == 3)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Production-dynamics lane counts:")
    for lane, count in sorted(counts.items()):
        print(f"  {lane}: {count}")
    print()
    print("Bridge import counts:")
    for bridge, count in sorted(bridge_counter.items()):
        print(f"  {bridge}: {count}")
    print()
    for lane in sorted(buckets):
        print(f"[{lane}]")
        for row in buckets[lane]:
            print("  " + row_label(row))
            print("    bridges: " + ", ".join(mapped_row(row)["bridges"]))
        print()
    return rows, counts


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    production_dynamics_derived = False
    production_kernel_selected = False
    physical_arrow_derived_from_record = False
    clock_or_rate_derived = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("production dynamics derived flag is false", not production_dynamics_derived)
    report("production kernel selected flag is false", not production_kernel_selected)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("clock/rate derived flag is false", not clock_or_rate_derived)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    rows, counts = row_map_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"PRODUCTION_DYNAMICS_NEEDED_ROWS={len(rows)}")
    for lane in sorted(EXPECTED_LANE_COUNTS):
        print(f"{lane.upper()}_ROWS={counts[lane]}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("CLOCK_OR_RATE_DERIVED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
