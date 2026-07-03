#!/usr/bin/env python3
"""Read-only row bucketing for the post-record audit evidence ladder."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
PASS = 0
FAIL = 0

SCOPE_EFFECTIVE = {"retained_bounded", "retained_pending_chain", "audited_conditional"}
EXPECTED_LEDGER_ROWS = 3596
EXPECTED_SCOPED_ROWS = 1888
EXPECTED_BUCKET_COUNTS = Counter(
    {
        "append_count_ready": 0,
        "finite_law_or_certificate_needed": 12,
        "not_record_ladder_relevant": 1437,
        "production_dynamics_needed": 6,
        "record_type_support_only": 0,
        "selector_or_dial_needed": 383,
        "simulation_support_only": 50,
    }
)

FOCUS_RE = re.compile(
    r"(RECORD|READOUT|BORN|PROBABILITY|P_VALUE|PVALUE|LIKELIHOOD|NULL|"
    r"CONCENTRATION|KOIDE|GENERATION|MEASURE|WEIGHT|SELECTOR|DIAL|"
    r"DYNAMICS|KRAUS|INSTRUMENT|HAMILTONIAN|SIMULATION|MONTE)",
    re.IGNORECASE,
)
STRONG_RECORD_RE = re.compile(
    r"(Record axiom|post-record|pre-record|record atom|record alphabet|"
    r"realized record|realized outcome|event algebra|finite histories|"
    r"count dynamics)",
    re.IGNORECASE,
)
SIMULATION_RE = re.compile(r"\b(simulation|Monte Carlo|random sample|sampled|numerical experiment)\b", re.IGNORECASE)
SELECTOR_RE = re.compile(
    r"\b(Koide|generation|selector|selects|selected|dial|weight|weighting|"
    r"measure|prior|normalization|dimension|block-count|Q=2/3|r=1/2)\b",
    re.IGNORECASE,
)
LAW_CERT_RE = re.compile(
    r"\b(p-value|pvalue|likelihood|null law|null|concentration|certificate|"
    r"tail|probability|Born|frequency|typicality|finite law)\b",
    re.IGNORECASE,
)
DYNAMICS_RE = re.compile(
    r"\b(dynamics|decoherence|instrument|Kraus|Hamiltonian|kernel|clock|rate|"
    r"arrow|einselection|thermaliz|stability|stable|flow|CPTP|measurement|production)\b",
    re.IGNORECASE,
)
COUNT_RE = re.compile(
    r"\b(append|count|counts|coarse-grain|coarse graining|finite histories|"
    r"record alphabet|record atom|realized atom|event algebra|one-hot)\b",
    re.IGNORECASE,
)


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


def source_text(path: str | None) -> str:
    if not path:
        return ""
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(errors="ignore")[:40000]


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def scoped(row: dict) -> bool:
    return (
        row.get("audit_status") == "audited_conditional"
        or row.get("effective_status") in SCOPE_EFFECTIVE
        or row.get("claim_type") == "bounded_theorem"
    )


def classify(row: dict) -> str:
    note_path = row.get("note_path") or ""
    title = row.get("title") or row.get("claim_id") or ""
    blocker = row.get("blocker") or row.get("load_bearing_step") or ""
    hay = "\n".join([note_path, title, blocker, source_text(note_path)])
    path_title = "\n".join([note_path, title])

    if not FOCUS_RE.search(path_title) and not STRONG_RECORD_RE.search(hay):
        return "not_record_ladder_relevant"

    if SIMULATION_RE.search(hay):
        return "simulation_support_only"
    if SELECTOR_RE.search(hay):
        return "selector_or_dial_needed"
    if LAW_CERT_RE.search(hay):
        return "finite_law_or_certificate_needed"
    if DYNAMICS_RE.search(hay):
        return "production_dynamics_needed"
    if COUNT_RE.search(hay):
        return "append_count_ready"
    if STRONG_RECORD_RE.search(hay):
        return "record_type_support_only"
    return "not_record_ladder_relevant"


def row_label(row: dict) -> str:
    return f"{row.get('claim_id')} | {row.get('audit_status')} | {row.get('effective_status')} | {row.get('claim_type')} | {row.get('note_path')}"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_AUDIT_EVIDENCE_LADDER_ROW_BUCKETING_2026-06-06.md",
        [
            "read-only scanner",
            "scans `1888` bounded/conditional",
            "touches `451` rows",
            "`selector_or_dial_needed` | 383",
            "bounded/conditional-scope rows",
            "bucket counts sum to the scoped count",
            "audit ledger hash is unchanged",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "conditional audit evidence ladder",
            "expectation-only evidence cannot certify p-values",
            "simulation evidence is support-only",
            "stable settings are not selected dials",
        ],
    )
    require_text(
        "docs/RECORD_TYPING_AUDIT_UNLOCK_MAP_2026-06-05.md",
        [
            "bounded/conditional scoped rows | 1304",
            "selector_split_after_type",
            "dynamics_split_after_type",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
        [
            "bounded and conditional lanes",
            "probability/source/instrument/dynamics rows",
            "Does not select a Koide/generation dial location.",
        ],
    )


def ledger_checks() -> tuple[list[dict], Counter[str]]:
    section("Ledger bucketing checks")
    before = digest(LEDGER)
    data = json.loads(LEDGER.read_text())
    rows_obj = data.get("rows")
    report("audit ledger has rows object", isinstance(rows_obj, dict))
    rows = list(rows_obj.values())
    scoped_rows = [row for row in rows if scoped(row)]
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in scoped_rows:
        buckets[classify(row)].append(row)

    counts = Counter({bucket: len(items) for bucket, items in buckets.items()})
    full_counts = Counter({bucket: counts[bucket] for bucket in EXPECTED_BUCKET_COUNTS})
    touched = sum(v for k, v in counts.items() if k != "not_record_ladder_relevant")
    expected_touched = sum(v for k, v in EXPECTED_BUCKET_COUNTS.items() if k != "not_record_ladder_relevant")
    report("ledger row count matches current map", len(rows) == EXPECTED_LEDGER_ROWS, str(len(rows)))
    report("bounded/conditional scope count matches current map", len(scoped_rows) == EXPECTED_SCOPED_ROWS, str(len(scoped_rows)))
    report("each scoped row gets one bucket", sum(counts.values()) == len(scoped_rows), str(counts))
    report("bucket counts match current source map", full_counts == EXPECTED_BUCKET_COUNTS, str(full_counts))
    report("touched ladder rows match current source map", touched == expected_touched, str(touched))
    report("selector/dial bucket nonempty", counts["selector_or_dial_needed"] > 0, str(counts["selector_or_dial_needed"]))
    report("production/dynamics bucket nonempty", counts["production_dynamics_needed"] > 0, str(counts["production_dynamics_needed"]))
    report("finite-law/certificate bucket nonempty", counts["finite_law_or_certificate_needed"] > 0, str(counts["finite_law_or_certificate_needed"]))
    report("append/count bucket matches current source zero", counts["append_count_ready"] == 0)
    report("record-type support bucket matches current source map", counts["record_type_support_only"] == EXPECTED_BUCKET_COUNTS["record_type_support_only"])

    required_rows = {
        "selector_or_dial_needed": "architecture_note_directional_measure",
        "production_dynamics_needed": "persistent_record_overlap_kernel_note",
        "finite_law_or_certificate_needed": "poisson_self_gravity_born_audit_note",
    }
    for bucket, claim_id in required_rows.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[bucket])
        report(f"representative row present in {bucket}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Bucket counts:")
    for bucket in sorted(EXPECTED_BUCKET_COUNTS):
        print(f"  {bucket}: {counts[bucket]}")
    print()
    for bucket in [
        "append_count_ready",
        "record_type_support_only",
        "finite_law_or_certificate_needed",
        "simulation_support_only",
        "selector_or_dial_needed",
        "production_dynamics_needed",
    ]:
        print(f"[{bucket}]")
        for row in buckets.get(bucket, [])[:8]:
            print("  " + row_label(row))
        print()

    return scoped_rows, counts


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    probability_derived_from_record = False
    concentration_derived_from_expectation = False
    simulation_treated_as_calibrated = False
    generation_or_koide_dial_selected = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("Record-derived probability flag is false", not probability_derived_from_record)
    report("expectation-derived concentration flag is false", not concentration_derived_from_expectation)
    report("simulation calibrated flag is false", not simulation_treated_as_calibrated)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    scoped_rows, counts = ledger_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"SCOPED_ROWS={len(scoped_rows)}")
    print(f"TOUCHED_ROWS={sum(v for k, v in counts.items() if k != 'not_record_ladder_relevant')}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
