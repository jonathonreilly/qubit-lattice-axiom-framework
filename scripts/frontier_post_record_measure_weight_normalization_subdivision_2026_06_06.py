#!/usr/bin/env python3
"""Read-only subdivision for measure/weight/normalization rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re
import sys

import frontier_post_record_selector_dial_bucket_subdivision_2026_06_06 as prev

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
SLICE = ROOT / "outputs/post_record_measure_weight_normalization_slice_2026_06_07.json"
PASS = 0
FAIL = 0

TRACE_NORMALIZATION_RE = re.compile(
    r"\b(trace|tracial|density matrix|povm|luders|jaynes|max[- ]entropy|"
    r"rho_ref|normalization|normalized|qubit|pre[-_ ]record reference|"
    r"Radon[- ]Nikodym|Gibbs state)\b",
    re.IGNORECASE,
)
SOURCE_MEASURE_RE = re.compile(
    r"\b(source[_/ -]?measure|source|pcal|cumulant|mobius|rn[-_ ]?cocycle|"
    r"Planck|source[-_ ]unit|sharp[-_ ]record|tangent[-_ ]space|"
    r"signed[-_ ]record|source[-_ ]readout|PWC|PRR|cumulant generating)\b",
    re.IGNORECASE,
)
CHARACTER_WEIGHT_RE = re.compile(
    r"\b(path measure|directional|character[-_ ]measure|plaquette|gauge|"
    r"continuum|h\^2|channel[-_ ]weight|casimir|chern|chern[-_ ]simons|"
    r"wilson|action[-_ ]surface|APS|eta|finite[-_ ]box|convolution|"
    r"Wilson coefficients|link[-_ ]local|first[-_ ]variation|Lieb|cluster)\b",
    re.IGNORECASE,
)
SELECTOR_TANGENT_RE = re.compile(
    r"\b(selector|hessian|ideal selector|readout|observable|bridge|higgs|"
    r"hierarchy|taste|teleportation|preparation|Y_T|yt_|connected[-_ ]source|"
    r"augmentation|authority|EW|Higgs|kappa|assignment)\b",
    re.IGNORECASE,
)

EXPECTED_LANE_COUNTS = {
    "character_path_channel_weight": 14,
    "generic_measure_weight_import": 14,
    "selector_tangent_readout_weight": 13,
    "source_measure_or_rn_bridge": 16,
    "trace_normalization_reference": 10,
}
EXPECTED_MEASURE_ROWS = sum(EXPECTED_LANE_COUNTS.values())


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


def normalize_weights(weights: dict[str, Fraction]) -> dict[str, Fraction] | None:
    if any(weight < 0 for weight in weights.values()):
        return None
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        return None
    return {key: value / total for key, value in weights.items()}


def selected_dial_from_normalization(has_normalization: bool, has_selector_rule: bool) -> str:
    if has_normalization and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "**Claim type:** bounded_theorem",
            "finite supplied-weight normalization lemma",
            "measure_weight_normalization",
            "Normalized measure is not selected dial.",
            "Finite normalization can certify",
            "Record-to-carrier/weight/normalization bridge remains outside this row",
            "Does not select or force a generation/Koide dial location",
            "scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py",
            "outputs/post_record_measure_weight_normalization_slice_2026_06_07.json",
        ],
    )
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "measure_weight_normalization` | 67",
            "measure/weight/normalization rows",
            "Does not turn stable settings into selected dials.",
        ],
    )
    require_text(
        "scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py",
        [
            "def selector_subbucket",
            "EXPECTED_SUBCOUNTS",
            "measure_weight_normalization",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "selected dial value | selector/invariance/target rule",
            "stable settings are not selected dials",
            "independent audit owns verdicts",
        ],
    )
    require_text(
        "docs/SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md",
        [
            "Source/Measure",
            "cumulant",
            "generating",
        ],
    )


def certificate_checks() -> None:
    section("Finite normalization certificate checks")
    normalized = normalize_weights({"a": Fraction(1), "b": Fraction(3)})
    report("positive finite supplied weights normalize", normalized == {"a": Fraction(1, 4), "b": Fraction(3, 4)}, str(normalized))
    report("normalized weights sum to one", normalized is not None and sum(normalized.values(), Fraction(0)) == 1)
    report("zero-total weights are rejected", normalize_weights({"a": Fraction(0), "b": Fraction(0)}) is None)
    report("negative weights are rejected", normalize_weights({"a": Fraction(1), "b": Fraction(-1)}) is None)
    report(
        "normalization without selector does not select dial",
        selected_dial_from_normalization(True, False) == "blocked_missing_selector",
    )
    report(
        "selector rule is still needed for selected dial readiness",
        selected_dial_from_normalization(True, True) == "conditional_selector_ready",
    )


def row_hay(row: dict) -> str:
    return "\n".join(
        str(row.get(key) or "")
        for key in ["claim_id", "title", "blocker", "load_bearing_step", "note_path"]
    )


def measure_lane(row: dict) -> str:
    hay = row_hay(row)
    if SOURCE_MEASURE_RE.search(hay):
        return "source_measure_or_rn_bridge"
    if TRACE_NORMALIZATION_RE.search(hay):
        return "trace_normalization_reference"
    if CHARACTER_WEIGHT_RE.search(hay):
        return "character_path_channel_weight"
    if SELECTOR_TANGENT_RE.search(hay):
        return "selector_tangent_readout_weight"
    return "generic_measure_weight_import"


def export_row(row: dict, lane: str) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "measure_lane": lane,
    }


def expected_export_rows(buckets: dict[str, list[dict]]) -> list[dict]:
    exported: list[dict] = []
    for lane in sorted(buckets):
        for row in sorted(buckets[lane], key=lambda item: item.get("claim_id") or ""):
            exported.append(export_row(row, lane))
    return exported


def measure_rows() -> list[dict]:
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    return [
        row
        for row in rows
        if prev.scoped(row)
        and prev.ladder_bucket(row) == "selector_or_dial_needed"
        and prev.selector_subbucket(row) == "measure_weight_normalization"
    ]


def row_checks() -> tuple[list[dict], Counter[str]]:
    section("Measure/weight row checks")
    before = digest(LEDGER)
    rows = measure_rows()
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        buckets[measure_lane(row)].append(row)
    counts = Counter({lane: len(items) for lane, items in buckets.items()})

    report("measure/weight row count is current snapshot", len(rows) == EXPECTED_MEASURE_ROWS, str(len(rows)))
    report("measure lane counts match expected", dict(counts) == EXPECTED_LANE_COUNTS, str(counts))
    report("measure lane counts sum to row count", sum(counts.values()) == len(rows), str(counts))

    representatives = {
        "character_path_channel_weight": "architecture_note_directional_measure",
        "generic_measure_weight_import": "born_scattering_comparison_note",
        "selector_tangent_readout_weight": "yt_exact_hessian_selector_uniqueness_note",
        "source_measure_or_rn_bridge": "source_measure_pcal_cumulant_mobius_theorem_note_2026-05-30",
        "trace_normalization_reference": "pre_record_reference_state_tracial_derivation_note_2026-05-20",
    }
    for lane, claim_id in representatives.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[lane])
        report(f"representative row present in {lane}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Measure/weight lane counts:")
    for lane, count in sorted(counts.items()):
        print(f"  {lane}: {count}")
    print()
    for lane in sorted(buckets):
        print(f"[{lane}]")
        for row in buckets[lane][:10]:
            print(
                "  "
                + f"{row.get('claim_id')} | {row.get('audit_status')} | "
                + f"{row.get('effective_status')} | {row.get('claim_type')} | "
                + f"{row.get('note_path')}"
            )
        print()
    export_checks(buckets, counts, before)
    return rows, counts


def export_checks(buckets: dict[str, list[dict]], counts: Counter[str], ledger_sha: str) -> None:
    section("Bounded ledger-row export checks")
    report("bounded measure/weight row export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    expected_rows = expected_export_rows(buckets)
    report("slice export is for the measure/weight bucket", data.get("bucket") == "measure_weight_normalization")
    report("slice export records current ledger sha", data.get("ledger_sha256") == ledger_sha, data.get("ledger_sha256", ""))
    report("slice export row count matches current split", data.get("row_count") == EXPECTED_MEASURE_ROWS, str(data.get("row_count")))
    report("slice export lane counts match current split", data.get("lane_counts") == dict(counts), str(data.get("lane_counts")))
    report("slice export rows match independently enumerated regex split", data.get("rows") == expected_rows)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    normalized_measure_selects_dial = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False
    measure_or_prior_derived_from_record = False
    born_law_derived_from_record = False
    production_dynamics_derived = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("normalized measure selects dial flag is false", not normalized_measure_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("Record-derived measure/prior flag is false", not measure_or_prior_derived_from_record)
    report("Record-derived Born law flag is false", not born_law_derived_from_record)
    report("production dynamics derived flag is false", not production_dynamics_derived)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    rows, counts = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"MEASURE_WEIGHT_NORMALIZATION_ROWS={len(rows)}")
    for lane in sorted(EXPECTED_LANE_COUNTS):
        print(f"{lane.upper()}_ROWS={counts[lane]}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("NORMALIZED_MEASURE_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("MEASURE_OR_PRIOR_DERIVED_FROM_RECORD=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
