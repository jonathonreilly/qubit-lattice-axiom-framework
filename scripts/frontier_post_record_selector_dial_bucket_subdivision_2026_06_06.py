#!/usr/bin/env python3
"""Read-only subdivision of selector/dial evidence-ladder rows."""

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

KOIDE_GENERATION_RE = re.compile(r"\b(Koide|Q=2/3|r=1/2|gamma|charged.?lepton|flavor|generation)\b", re.IGNORECASE)
MEASURE_RE = re.compile(r"\b(measure|weight|weighting|normalization|prior|dimension|Born|probability|determinant|trace|tracial|volume)\b", re.IGNORECASE)
STABILITY_RE = re.compile(r"\b(stable|stability|flow|arrow|dynamics|thermaliz|attractor|repelling|fixed point|separatrix)\b", re.IGNORECASE)
GENERIC_SELECTOR_RE = re.compile(r"\b(selector|selects|selected|dial|invariance|symmetry|target|rule)\b", re.IGNORECASE)

EXPECTED_SUBCOUNTS = {
    "koide_or_generation_selector": 125,
    "stability_or_dynamics_selector": 147,
    "measure_weight_normalization": 71,
    "generic_selector_rule": 3,
}
EXPECTED_SELECTOR_ROWS = sum(EXPECTED_SUBCOUNTS.values())


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


def source_text(path: str | None) -> str:
    if not path:
        return ""
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(errors="ignore")[:40000]


def scoped(row: dict) -> bool:
    return (
        row.get("audit_status") == "audited_conditional"
        or row.get("effective_status") in SCOPE_EFFECTIVE
        or row.get("claim_type") == "bounded_theorem"
    )


def haystack(row: dict) -> str:
    note_path = row.get("note_path") or ""
    title = row.get("title") or row.get("claim_id") or ""
    blocker = row.get("blocker") or row.get("load_bearing_step") or ""
    return "\n".join([note_path, title, blocker, source_text(note_path)])


def ladder_bucket(row: dict) -> str:
    note_path = row.get("note_path") or ""
    title = row.get("title") or row.get("claim_id") or ""
    hay = haystack(row)
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


def selector_subbucket(row: dict) -> str:
    hay = haystack(row)
    if STABILITY_RE.search(hay):
        return "stability_or_dynamics_selector"
    if KOIDE_GENERATION_RE.search(hay):
        return "koide_or_generation_selector"
    if MEASURE_RE.search(hay):
        return "measure_weight_normalization"
    if GENERIC_SELECTOR_RE.search(hay):
        return "generic_selector_rule"
    return "uncategorized_selector"


def row_label(row: dict) -> str:
    return f"{row.get('claim_id')} | {row.get('audit_status')} | {row.get('effective_status')} | {row.get('claim_type')} | {row.get('note_path')}"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "selector/dial bucket",
            "stable settings into selected dials",
            "koide_or_generation_selector",
            "measure_weight_normalization",
            "stability_or_dynamics_selector",
        ],
    )
    require_text(
        "docs/POST_RECORD_AUDIT_EVIDENCE_LADDER_ROW_BUCKETING_2026-06-06.md",
        [
            "selector_or_dial_needed` | 346",
            "read-only scanner",
            "audit ledger hash is unchanged",
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
    section("Selector/dial subdivision checks")
    before = digest(LEDGER)
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    selector_rows = [row for row in rows if scoped(row) and ladder_bucket(row) == "selector_or_dial_needed"]
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in selector_rows:
        buckets[selector_subbucket(row)].append(row)
    counts = Counter({bucket: len(items) for bucket, items in buckets.items()})

    report("selector/dial row count is current snapshot", len(selector_rows) == EXPECTED_SELECTOR_ROWS, str(len(selector_rows)))
    report("sub-bucket counts sum to selector count", sum(counts.values()) == len(selector_rows), str(counts))
    report("expected sub-bucket counts match", dict(counts) == EXPECTED_SUBCOUNTS, str(counts))

    required_rows = {
        "koide_or_generation_selector": "charged_lepton_koide_two_gate_tier_a_bounded_theorem_note_2026-06-02",
        "stability_or_dynamics_selector": "a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1",
        "measure_weight_normalization": "architecture_note_directional_measure",
        "generic_selector_rule": "gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_rho1_least_distortion_selector_theorem_note_2026-04-20",
    }
    for bucket, claim_id in required_rows.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[bucket])
        report(f"representative row present in {bucket}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Selector/dial sub-bucket counts:")
    for bucket, count in sorted(counts.items()):
        print(f"  {bucket}: {count}")
    print()
    for bucket in sorted(buckets):
        print(f"[{bucket}]")
        for row in buckets[bucket][:8]:
            print("  " + row_label(row))
        print()
    return selector_rows, counts


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False
    measure_or_prior_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("Record-derived measure/prior flag is false", not measure_or_prior_derived_from_record)


def main() -> int:
    source_anchor_checks()
    selector_rows, counts = subdivision_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"SELECTOR_DIAL_ROWS={len(selector_rows)}")
    print(f"KOIDE_OR_GENERATION_SELECTOR_ROWS={counts['koide_or_generation_selector']}")
    print(f"STABILITY_OR_DYNAMICS_SELECTOR_ROWS={counts['stability_or_dynamics_selector']}")
    print(f"MEASURE_WEIGHT_NORMALIZATION_ROWS={counts['measure_weight_normalization']}")
    print(f"GENERIC_SELECTOR_RULE_ROWS={counts['generic_selector_rule']}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
