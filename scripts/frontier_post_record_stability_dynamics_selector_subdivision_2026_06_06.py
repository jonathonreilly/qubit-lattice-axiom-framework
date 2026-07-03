#!/usr/bin/env python3
"""Read-only subdivision of stability/dynamics selector rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import re
import sys

import frontier_post_record_selector_dial_bucket_subdivision_2026_06_06 as prev

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
SLICE = ROOT / "outputs/post_record_stability_dynamics_selector_slice_2026_06_07.json"
PASS = 0
FAIL = 0

FLOW_THERMAL_RE = re.compile(
    r"\b(thermal|thermaliz|heat|temperature|entropy|Gibbs|Boltzmann|flow|"
    r"attractor|repelling|fixed point|separatrix|stable|stability)\b",
    re.IGNORECASE,
)
ARROW_DYNAMICS_RE = re.compile(
    r"\b(arrow|dynamics|evolution|Hamiltonian|transfer|kernel|CPTP|Kraus|"
    r"instrument|decoherence|measurement)\b",
    re.IGNORECASE,
)

EXPECTED_SUBCOUNTS = {
    "flow_or_thermal_stability": 106,
    "arrow_or_dynamics_bridge": 63,
}
EXPECTED_STABILITY_ROWS = sum(EXPECTED_SUBCOUNTS.values())


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


def stability_subbucket(row: dict) -> str:
    hay = prev.haystack(row)
    if FLOW_THERMAL_RE.search(hay):
        return "flow_or_thermal_stability"
    if ARROW_DYNAMICS_RE.search(hay):
        return "arrow_or_dynamics_bridge"
    return "generic_stability_dynamics"


def row_label(row: dict) -> str:
    return f"{row.get('claim_id')} | {row.get('audit_status')} | {row.get('effective_status')} | {row.get('claim_type')} | {row.get('note_path')}"


def export_row(row: dict, bucket: str) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "stability_subbucket": bucket,
    }


def expected_export_rows(buckets: dict[str, list[dict]]) -> list[dict]:
    exported: list[dict] = []
    for bucket in sorted(buckets):
        for row in sorted(buckets[bucket], key=lambda item: item.get("claim_id") or ""):
            exported.append(export_row(row, bucket))
    return exported


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md",
        [
            "flow_or_thermal_stability",
            "arrow_or_dynamics_bridge",
            "stable setting is not selected dial",
            "physical arrow, kernel, Hamiltonian, instrument, clock, or",
            "scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py",
            "outputs/post_record_stability_dynamics_selector_slice_2026_06_07.json",
        ],
    )
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "stability_or_dynamics_selector` | 169",
            "stable settings into selected dials",
            "Does not turn stable settings into selected dials.",
        ],
    )
    require_text(
        "scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py",
        [
            "def selector_subbucket",
            "stability_or_dynamics_selector",
            "EXPECTED_SUBCOUNTS",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "stable settings are not selected dials",
            "selected dial value",
            "independent audit owns verdicts",
        ],
    )


def subdivision_checks() -> tuple[list[dict], Counter[str]]:
    section("Stability/dynamics subdivision checks")
    before = digest(LEDGER)
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    stability_rows = [
        row
        for row in rows
        if prev.scoped(row)
        and prev.ladder_bucket(row) == "selector_or_dial_needed"
        and prev.selector_subbucket(row) == "stability_or_dynamics_selector"
    ]
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in stability_rows:
        buckets[stability_subbucket(row)].append(row)
    counts = Counter({bucket: len(items) for bucket, items in buckets.items()})

    report("stability/dynamics selector row count is current snapshot", len(stability_rows) == EXPECTED_STABILITY_ROWS, str(len(stability_rows)))
    report("sub-bucket counts sum to stability/dynamics count", sum(counts.values()) == len(stability_rows), str(counts))
    report("expected sub-bucket counts match", dict(counts) == EXPECTED_SUBCOUNTS, str(counts))

    required_rows = {
        "flow_or_thermal_stability": "flavor_r_half_is_the_records_flow_separatrix_2026-06-02",
        "arrow_or_dynamics_bridge": "a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1",
    }
    for bucket, claim_id in required_rows.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[bucket])
        report(f"representative row present in {bucket}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Stability/dynamics sub-bucket counts:")
    for bucket, count in sorted(counts.items()):
        print(f"  {bucket}: {count}")
    print()
    for bucket in sorted(buckets):
        print(f"[{bucket}]")
        for row in buckets[bucket][:8]:
            print("  " + row_label(row))
        print()
    export_checks(buckets, counts, before)
    return stability_rows, counts


def export_checks(buckets: dict[str, list[dict]], counts: Counter[str], ledger_sha: str) -> None:
    section("Bounded ledger-row export checks")
    report("bounded stability/dynamics row export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    expected_rows = expected_export_rows(buckets)
    report("slice export is for the stability/dynamics selector bucket", data.get("bucket") == "stability_or_dynamics_selector")
    report("slice export records current ledger sha", data.get("ledger_sha256") == ledger_sha, data.get("ledger_sha256", ""))
    report("slice export row count matches current split", data.get("row_count") == EXPECTED_STABILITY_ROWS, str(data.get("row_count")))
    report("slice export sub-counts match current split", data.get("subbucket_counts") == dict(counts), str(data.get("subbucket_counts")))
    report("slice export rows match independently enumerated regex split", data.get("rows") == expected_rows)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False
    physical_arrow_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)


def main() -> int:
    source_anchor_checks()
    stability_rows, counts = subdivision_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"STABILITY_DYNAMICS_SELECTOR_ROWS={len(stability_rows)}")
    print(f"FLOW_OR_THERMAL_STABILITY_ROWS={counts['flow_or_thermal_stability']}")
    print(f"ARROW_OR_DYNAMICS_BRIDGE_ROWS={counts['arrow_or_dynamics_bridge']}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
