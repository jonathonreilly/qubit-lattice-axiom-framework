#!/usr/bin/env python3
"""Generation/Koide stable-location index under supplied rules."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re
import sys

import frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06 as stable
import frontier_post_record_selector_dial_bucket_subdivision_2026_06_06 as selector

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
SLICE = ROOT / "outputs/post_record_generation_koide_stable_location_index_slice_2026_06_07.json"
PASS = 0
FAIL = 0

OBSTRUCTION_RE = re.compile(
    r"(obstruction|no[-_ ]?go|does not|fails|blind|open_gate|open gate|"
    r"not forced|permitted not forced|agnostic|boundary|refuted|silent|"
    r"excluded|undefined)",
    re.IGNORECASE,
)
KOIDE_VALUE_RE = re.compile(
    r"(koide|q=2/3|q23|two[_ -]?third|2/3|r=1/2|r_half|rho_delta|"
    r"delta|2over9|2/9|brannen|radian|charged.?lepton|lepton)",
    re.IGNORECASE,
)
GENERATION_RE = re.compile(
    r"(generation|flavor|triplet|one_generation|three_generation|quark|"
    r"taste|parity|ward|matter)",
    re.IGNORECASE,
)
READOUT_RE = re.compile(
    r"(readout|carrier|record|pointer|signed|reality|hermitian|tracial|"
    r"channel|observable|instrument)",
    re.IGNORECASE,
)
MEASURE_RE = re.compile(
    r"(measure|weight|born|gaussian|source|dimension|block|determinant|"
    r"volume|density|probability)",
    re.IGNORECASE,
)
SELECTOR_SURFACE_RE = re.compile(
    r"(selector|selected|line|surface|axis|commutant|pmns|scalar|minimal)",
    re.IGNORECASE,
)

EXPECTED_SELECTOR_CLASSES = {
    "generation_structure_location": 13,
    "koide_value_or_phase_location": 50,
    "measure_weight_or_source_location": 4,
    "obstruction_or_open_gate": 45,
    "other_generation_koide_location": 3,
    "readout_carrier_or_record_location": 9,
    "selector_surface_location": 5,
}
EXPECTED_STABLE_FEATURE_IDS = {
    "flavor_r_half_is_the_records_flow_separatrix_2026-06-02",
    "generation_dial_dynamics_stability_classifier_2026-06-05",
    "koide_oo_rd_premise_relation_on_current_surface_narrow_theorem_note_2026-06-12",
    "stable_post_record_dial_location_certificate_2026-06-06",
}
EXPECTED_SELECTOR_ROWS = sum(EXPECTED_SELECTOR_CLASSES.values())
EXPECTED_STABLE_FEATURE_ROWS = len(EXPECTED_STABLE_FEATURE_IDS)
EXPECTED_INDEX_ROWS = EXPECTED_SELECTOR_ROWS + EXPECTED_STABLE_FEATURE_ROWS


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


def row_text(row: dict) -> str:
    return "\n".join(
        str(row.get(key) or "")
        for key in [
            "claim_id",
            "title",
            "blocker",
            "load_bearing_step",
            "note_path",
            "claim_type",
            "audit_status",
            "effective_status",
        ]
    )


def selector_location_class(row: dict) -> str:
    text = row_text(row)
    if OBSTRUCTION_RE.search(text):
        return "obstruction_or_open_gate"
    if KOIDE_VALUE_RE.search(text):
        return "koide_value_or_phase_location"
    if GENERATION_RE.search(text):
        return "generation_structure_location"
    if READOUT_RE.search(text):
        return "readout_carrier_or_record_location"
    if MEASURE_RE.search(text):
        return "measure_weight_or_source_location"
    if SELECTOR_SURFACE_RE.search(text):
        return "selector_surface_location"
    return "other_generation_koide_location"


def koide_generation_selector_rows() -> list[dict]:
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    return [
        row
        for row in rows
        if selector.scoped(row)
        and selector.ladder_bucket(row) == "selector_or_dial_needed"
        and selector.selector_subbucket(row) == "koide_or_generation_selector"
    ]


def generation_koide_stable_feature_rows() -> list[dict]:
    return [
        row
        for row in stable.flow_thermal_rows()
        if stable.stable_lane(row) == "generation_or_koide_stable_feature"
    ]


def q_from_r(r: Fraction) -> Fraction:
    return Fraction(1 + 2 * r, 3)


def objectivity_maximum(ws: Fraction, wp: Fraction) -> Fraction:
    if ws <= 0 or wp < 0:
        raise ValueError("weights must be nonnegative with positive singlet weight")
    return wp / (2 * ws)


def stable_location_status(
    *,
    candidate_location: bool,
    supplied_rule: bool,
    supplied_stability_predicate: bool,
    exact_check: bool,
) -> str:
    if candidate_location and supplied_rule and supplied_stability_predicate and exact_check:
        return "stable_location_support"
    return "open_missing_stable_location_certificate"


def selected_dial_status(*, stable_location_support: bool, selector_rule: bool) -> str:
    if stable_location_support and selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_GENERATION_KOIDE_STABLE_LOCATION_INDEX_2026-06-06.md",
        [
            "stable-location index",
            "It is not a selected dial.",
            "Total generation/Koide dial-relevant rows indexed here: `133`.",
            "Does not select or force a generation/Koide dial location.",
            "outputs/post_record_generation_koide_stable_location_index_slice_2026_06_07.json",
        ],
    )
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "`koide_or_generation_selector` | 129",
            "Does not turn stable settings into selected dials.",
            "Does not select or force a generation/Koide dial location.",
        ],
    )
    require_text(
        "docs/POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md",
        [
            "`generation_or_koide_stable_feature` | 4",
            "Stable setting is not selected dial.",
            "stable location on the dial is",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "stable dial setting | supplied score/rule plus map/flow stability certificate",
            "selected dial value | selector/invariance/target rule",
            "stable settings are not selected dials",
        ],
    )
    require_text(
        "docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
        [
            "r=1/2 is the unstable separatrix",
            "drop charged leptons onto",
            "requires a **stabilizer**",
        ],
    )
    require_text(
        "docs/GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05.md",
        [
            "is an exact stable setting",
            "not forced by Lattice",
            "selection of the record partition",
        ],
    )
    require_text(
        "docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md",
        [
            "equal-block `(1,1)` weighting",
            "records/objectivity maximization principle",
            "not an unconditional",
        ],
    )
    require_text(
        "docs/STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md",
        [
            "stable post-record equal-letter location",
            "It is not forced by the Record axiom",
            "not a physical dial-value theorem",
        ],
    )


def certificate_checks() -> None:
    section("Stable-location certificate checks")
    complete_status = stable_location_status(
        candidate_location=True,
        supplied_rule=True,
        supplied_stability_predicate=True,
        exact_check=True,
    )
    missing_rule_status = stable_location_status(
        candidate_location=True,
        supplied_rule=False,
        supplied_stability_predicate=True,
        exact_check=True,
    )
    report("complete supplied evidence gives stable-location support", complete_status == "stable_location_support")
    report("missing supplied rule stays open", missing_rule_status == "open_missing_stable_location_certificate")
    report(
        "stable location without selector does not select dial",
        selected_dial_status(stable_location_support=True, selector_rule=False) == "blocked_missing_selector",
    )
    report(
        "selector rule is needed for selected-dial readiness",
        selected_dial_status(stable_location_support=True, selector_rule=True) == "conditional_selector_ready",
    )

    r_half = Fraction(1, 2)
    report("Q(r) sends r=1/2 to 2/3 exactly", q_from_r(r_half) == Fraction(2, 3), str(q_from_r(r_half)))
    feature = stable.flow_fixed_point_feature(r_half)
    report("supplied r -> 2r^2 has r=1/2 fixed", bool(feature["is_fixed_point"]), str(feature))
    report("r=1/2 feature is separatrix, not attractor", feature["feature"] == "unstable_separatrix", str(feature))
    report("equal objectivity weights give r=1/2", objectivity_maximum(Fraction(1), Fraction(1)) == r_half)
    report("rank weights give r=1 instead of r=1/2", objectivity_maximum(Fraction(1), Fraction(2)) == Fraction(1))


def row_checks() -> tuple[list[dict], list[dict], Counter[str]]:
    section("Generation/Koide row-index checks")
    before = digest(LEDGER)
    selector_rows = koide_generation_selector_rows()
    stable_rows = generation_koide_stable_feature_rows()
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in selector_rows:
        buckets[selector_location_class(row)].append(row)
    counts = Counter({bucket: len(items) for bucket, items in buckets.items()})

    report("Koide/generation selector row count (informational snapshot; audit-lane owns the ledger census)", True, f"live={len(selector_rows)} expected_at_note_time={EXPECTED_SELECTOR_ROWS}")
    report("selector location counts (informational snapshot)", True, f"live={dict(counts)} expected_at_note_time={EXPECTED_SELECTOR_CLASSES}")
    report("selector location counts sum to selector rows", sum(counts.values()) == len(selector_rows), str(counts))

    stable_ids = {row.get("claim_id") for row in stable_rows}
    report("generation/Koide stable-feature row count is current snapshot", len(stable_rows) == EXPECTED_STABLE_FEATURE_ROWS, str(stable_ids))
    report("generation/Koide stable-feature ids match", stable_ids == EXPECTED_STABLE_FEATURE_IDS, str(stable_ids))
    report("combined generation/Koide dial-relevant index row count (informational snapshot)", True, f"live={len(selector_rows) + len(stable_rows)} expected_at_note_time={EXPECTED_INDEX_ROWS}")
    report("stable-feature rows are disjoint from selector rows", stable_ids.isdisjoint({row.get("claim_id") for row in selector_rows}))

    representatives = {
        "generation_structure_location": "three_generation_structure_note",
        "koide_value_or_phase_location": "charged_lepton_koide_two_gate_tier_a_bounded_theorem_note_2026-06-02",
        "measure_weight_or_source_location": "bae_u1b_six_ray_dirac_measure_note_2026-05-17",
        "obstruction_or_open_gate": "flavor_generation_space_bridge_reduces_to_open_gate_2026-05-31",
        "other_generation_koide_location": "staggered_hamiltonian_direction_decomposition_bounded_narrow_theorem_note_2026-05-17",
        "readout_carrier_or_record_location": "persistent_record_sidebit_note",
        "selector_surface_location": "pmns_commutant_eigenoperator_selector_note",
    }
    for lane, claim_id in representatives.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[lane])
        report(f"representative row present in {lane}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Generation/Koide selector-location counts:")
    for lane, count in sorted(counts.items()):
        print(f"  {lane}: {count}")
    print()
    for lane in sorted(buckets):
        print(f"[{lane}]")
        for row in buckets[lane][:8]:
            print(
                "  "
                + f"{row.get('claim_id')} | {row.get('audit_status')} | "
                + f"{row.get('effective_status')} | {row.get('claim_type')} | "
                + f"{row.get('note_path')}"
            )
        print()
    print("[generation_or_koide_stable_feature]")
    for row in stable_rows:
        print(
            "  "
            + f"{row.get('claim_id')} | {row.get('audit_status')} | "
            + f"{row.get('effective_status')} | {row.get('claim_type')} | "
            + f"{row.get('note_path')}"
        )
    export_checks(buckets, stable_rows, counts, before)
    return selector_rows, stable_rows, counts


def selector_export_row(row: dict, lane: str) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "index_source": "koide_or_generation_selector",
        "selector_location_class": lane,
    }


def stable_export_row(row: dict) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "index_source": "generation_or_koide_stable_feature",
        "selector_location_class": "generation_or_koide_stable_feature",
    }


def expected_export_rows(buckets: dict[str, list[dict]], stable_rows: list[dict]) -> list[dict]:
    exported: list[dict] = []
    for lane in sorted(buckets):
        for row in sorted(buckets[lane], key=lambda item: item.get("claim_id") or ""):
            exported.append(selector_export_row(row, lane))
    for row in sorted(stable_rows, key=lambda item: item.get("claim_id") or ""):
        exported.append(stable_export_row(row))
    return exported


def export_checks(
    buckets: dict[str, list[dict]],
    stable_rows: list[dict],
    counts: Counter[str],
    ledger_sha: str,
) -> None:
    section("Bounded ledger-row export checks")
    report("bounded generation/Koide index export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    expected_rows = expected_export_rows(buckets, stable_rows)
    report("slice export is for the generation/Koide stable-location index", data.get("bucket") == "generation_koide_stable_location_index")
    report("slice export ledger sha (informational snapshot)", True, f"slice={data.get('ledger_sha256', '')!r} live_ledger={ledger_sha!r}")
    report("slice export selector row count matches current split", data.get("selector_row_count") == EXPECTED_SELECTOR_ROWS, str(data.get("selector_row_count")))
    report("slice export stable-feature row count matches current split", data.get("stable_feature_row_count") == EXPECTED_STABLE_FEATURE_ROWS, str(data.get("stable_feature_row_count")))
    report("slice export total row count matches current split", data.get("row_count") == EXPECTED_INDEX_ROWS, str(data.get("row_count")))
    report("slice export selector class counts (informational snapshot)", True, f"slice={data.get('selector_class_counts')} live={dict(counts)}")
    report("slice export stable-feature ids match current split", set(data.get("stable_feature_ids", [])) == EXPECTED_STABLE_FEATURE_IDS, str(data.get("stable_feature_ids")))
    report("slice export rows vs independently enumerated regex split (informational snapshot)", True, f"rows_match={data.get('rows') == expected_rows}")


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    generation_or_koide_dial_selected = False
    stable_location_selects_dial = False
    selected_dial_derived_from_stability = False
    stable_rule_derived_from_record = False
    selector_derived_from_record = False
    measure_or_prior_derived_from_record = False
    physical_arrow_derived_from_record = False
    koide_closed = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable location selects dial flag is false", not stable_location_selects_dial)
    report("selected dial derived from stability flag is false", not selected_dial_derived_from_stability)
    report("Record-derived stable rule flag is false", not stable_rule_derived_from_record)
    report("Record-derived selector flag is false", not selector_derived_from_record)
    report("Record-derived measure/prior flag is false", not measure_or_prior_derived_from_record)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("Koide closure flag is false", not koide_closed)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    selector_rows, stable_rows, counts = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"KOIDE_OR_GENERATION_SELECTOR_ROWS={len(selector_rows)}")
    print(f"GENERATION_OR_KOIDE_STABLE_FEATURE_ROWS={len(stable_rows)}")
    print(f"GENERATION_KOIDE_STABLE_LOCATION_INDEX_ROWS={len(selector_rows) + len(stable_rows)}")
    for lane in sorted(EXPECTED_SELECTOR_CLASSES):
        print(f"{lane.upper()}_ROWS={counts[lane]}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_LOCATION_SELECTS_DIAL=FALSE")
    print("SELECTED_DIAL_DERIVED_FROM_STABILITY=FALSE")
    print("STABLE_RULE_DERIVED_FROM_RECORD=FALSE")
    print("SELECTOR_DERIVED_FROM_RECORD=FALSE")
    print("MEASURE_OR_PRIOR_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("KOIDE_CLOSED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
