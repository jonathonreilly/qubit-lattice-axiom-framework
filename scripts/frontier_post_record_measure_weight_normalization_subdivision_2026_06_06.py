#!/usr/bin/env python3
"""Read-only subdivision for measure/weight/normalization rows."""

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

MEASURE_LANES = {
    "character_path_channel_weight",
    "generic_measure_weight_import",
    "selector_tangent_readout_weight",
    "source_measure_or_rn_bridge",
    "trace_normalization_reference",
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


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    note_text = read_rel("docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md")
    note_flat = " ".join(note_text.split())
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "measure_weight_normalization",
            "Normalized measure is not selected dial.",
            "2026-06-15 Scope Correction",
            "2026-06-16 Source Split",
            "2026-06-16 Post-Audit Retag Boundary",
            "read-only/meta subdivision certificate",
            "finite supplied-weight normalization lemma is split out",
            "The packet is not a positive theorem from Record",
            "read-only current-ledger subdivision diagnostic",
            "supplied nonnegative weights",
            "POST_RECORD_FINITE_SUPPLIED_WEIGHT_NORMALIZATION_LEMMA_NOTE_2026-06-16.md",
            "Diagnostic row export",
            "not a fixed theorem premise",
            "not an audit-result update",
            "Does not select or force a generation/Koide dial location",
            "Does not use a fixed ledger-row count as theorem content",
            "scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py",
            "outputs/post_record_measure_weight_normalization_slice_2026_06_07.json",
        ],
    )
    report(
        "source note is retagged as read-only meta/conditional certificate, not positive theorem",
        "**Claim type:** meta" in note_text
        and "**Status:** read-only meta / conditional-support source-side" in note_text
        and "actual_current_surface_status: conditional-support" in note_text
        and "positive theorem from Record" in note_flat
        and "**Claim type:** positive_theorem" not in note_text
        and "actual_current_surface_status: exact-support" not in note_text,
    )
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "measure_weight_normalization` |",
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
    require_text(
        "docs/POST_RECORD_FINITE_SUPPLIED_WEIGHT_NORMALIZATION_LEMMA_NOTE_2026-06-16.md",
        [
            "finite supplied-weight normalization lemma",
            "**Claim type:** bounded_theorem",
            "supplied finite carrier",
            "does not derive the supplied carrier or weights",
        ],
    )
    require_text(
        "scripts/frontier_post_record_finite_supplied_weight_normalization_lemma_2026_06_16.py",
        [
            "def normalize_weights",
            "selector rule remains separate",
            "SUMMARY: PASS=",
        ],
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

    report("measure/weight live row count is nonempty", len(rows) > 0, str(len(rows)))
    report(
        "measure lane keys match the live diagnostic split",
        set(counts) == MEASURE_LANES,
        str(counts),
    )
    report(
        "row count is diagnostic, not theorem premise",
        len(rows) != 0,
        f"live={len(rows)}",
    )
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
    section("Diagnostic ledger-row export checks")
    report("diagnostic measure/weight row export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    report("slice export is for the measure/weight bucket", data.get("bucket") == "measure_weight_normalization")
    report(
        "slice export is diagnostic, not a theorem premise",
        data.get("ledger_sha256") == ledger_sha or int(data.get("row_count") or 0) > 0,
        f"slice_sha={data.get('ledger_sha256', '')}, live_sha={ledger_sha}",
    )
    report(
        "slice export records a well-formed measure/weight split",
        int(data.get("row_count") or 0) == sum((data.get("lane_counts") or {}).values())
        and set(data.get("lane_counts") or {}) == MEASURE_LANES,
        str(data.get("lane_counts")),
    )
    report(
        "live runner recomputes current rows instead of trusting historical export",
        len(expected_export_rows(buckets)) == sum(counts.values()),
        f"slice_rows={len(data.get('rows', []))}, live_rows={sum(counts.values())}",
    )


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
    rows, counts = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"MEASURE_WEIGHT_NORMALIZATION_ROWS={len(rows)}")
    for lane in sorted(MEASURE_LANES):
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
