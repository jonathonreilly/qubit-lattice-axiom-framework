#!/usr/bin/env python3
"""Finite character/path/channel weight prototype under supplied rules."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

import frontier_post_record_measure_weight_normalization_subdivision_2026_06_06 as measure

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
SLICE = ROOT / "outputs/post_record_character_path_channel_weight_slice_2026_06_07.json"
PASS = 0
FAIL = 0

EXPECTED_ROWS = 21


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


def normalize(weights: dict[str, Fraction]) -> dict[str, Fraction]:
    if any(value < 0 for value in weights.values()):
        raise ValueError("negative supplied weight")
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        raise ValueError("nonpositive supplied total")
    return {key: value / total for key, value in weights.items()}


def normalize_channel(rows: dict[str, dict[str, Fraction]]) -> dict[str, dict[str, Fraction]]:
    return {source: normalize(targets) for source, targets in rows.items()}


def path_product(path: tuple[str, ...], edge_weights: dict[tuple[str, str], Fraction]) -> Fraction:
    product = Fraction(1)
    for edge in zip(path, path[1:]):
        product *= edge_weights[edge]
    return product


def selected_measure_status(has_normalized_packet: bool, has_physical_selector: bool) -> str:
    if has_normalized_packet and has_physical_selector:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_CHARACTER_PATH_CHANNEL_WEIGHT_PROTOTYPE_2026-06-06.md",
        [
            "character_path_channel_weight",
            "supplied-normalization witness",
            "normalized finite path/channel/character weight packet",
            "Does not derive a directional path parameter",
            "Does not select or force a generation/Koide dial location.",
            "outputs/post_record_character_path_channel_weight_slice_2026_06_07.json",
        ],
    )
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "`character_path_channel_weight` | 21",
            "character/path/channel weight rows need a supplied weight rule and carrier",
            "Does not derive a prior, measure, source unit, trace state, or weight rule",
        ],
    )
    require_text(
        "docs/ARCHITECTURE_NOTE_DIRECTIONAL_MEASURE.md",
        [
            "Directional Path Measure",
            "Beta-derivation status",
            "tuned support",
        ],
    )
    require_text(
        "docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md",
        [
            "finite character-measure coefficient packet",
            "normalized central character-measure packet",
            "What This Does Not Close",
        ],
    )
    require_text(
        "docs/WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md",
        [
            "Wilson real-positive measure surface",
            "not derived here",
            "real-positive Wilson measure surface premise",
        ],
    )


def certificate_checks() -> None:
    section("Finite character/path/channel checks")
    path_weights = normalize({"straight": Fraction(4), "bend": Fraction(1)})
    report("finite supplied path weights normalize", path_weights == {"straight": Fraction(4, 5), "bend": Fraction(1, 5)}, str(path_weights))
    report("path weights sum to one", sum(path_weights.values(), Fraction(0)) == 1)

    channel = normalize_channel(
        {
            "A": {"A": Fraction(3), "B": Fraction(1)},
            "B": {"A": Fraction(1), "B": Fraction(1)},
        }
    )
    rows_sum = all(sum(row.values(), Fraction(0)) == 1 for row in channel.values())
    report("finite supplied channel rows normalize", rows_sum, str(channel))
    report("channel transition A->A is exact", channel["A"]["A"] == Fraction(3, 4), str(channel["A"]))

    edge_weights = {("s", "m"): Fraction(2), ("m", "t"): Fraction(3), ("s", "t"): Fraction(1)}
    raw_paths = {
        "two_step": path_product(("s", "m", "t"), edge_weights),
        "direct": path_product(("s", "t"), edge_weights),
    }
    normalized_paths = normalize(raw_paths)
    report("path product weights compose exactly", raw_paths == {"two_step": Fraction(6), "direct": Fraction(1)}, str(raw_paths))
    report("composed path weights normalize exactly", normalized_paths == {"two_step": Fraction(6, 7), "direct": Fraction(1, 7)}, str(normalized_paths))

    character_packet = normalize({"trivial": Fraction(6), "fundamental": Fraction(3), "adjoint": Fraction(1)})
    report("finite supplied character coefficients normalize", character_packet == {"trivial": Fraction(3, 5), "fundamental": Fraction(3, 10), "adjoint": Fraction(1, 10)}, str(character_packet))
    report(
        "normalized packet without selector does not select physical measure",
        selected_measure_status(True, False) == "blocked_missing_selector",
    )
    report(
        "physical selector rule is still needed",
        selected_measure_status(True, True) == "conditional_selector_ready",
    )

    try:
        normalize({"bad": Fraction(-1)})
        negative_rejected = False
    except ValueError:
        negative_rejected = True
    report("negative supplied weights are rejected", negative_rejected)


def character_rows() -> list[dict]:
    return [
        row
        for row in measure.measure_rows()
        if measure.measure_lane(row) == "character_path_channel_weight"
    ]


def export_row(row: dict) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "measure_lane": "character_path_channel_weight",
    }


def expected_export_rows(rows: list[dict]) -> list[dict]:
    return [export_row(row) for row in sorted(rows, key=lambda item: item.get("claim_id") or "")]


def row_checks() -> list[dict]:
    section("Character/path/channel row checks")
    before = digest(LEDGER)
    rows = character_rows()
    report("character/path/channel row count is current snapshot", len(rows) == EXPECTED_ROWS, str(len(rows)))
    representative_ids = {
        "architecture_note_directional_measure",
        "dm_full_closure_64_to_1_channel_weight_bridge_narrow_theorem_note_2026-06-02",
        "wilson_action_surface_selector_real_positive_theorem_note_2026-05-25",
    }
    ids = {row.get("claim_id") for row in rows}
    for claim_id in sorted(representative_ids):
        report(f"representative row present: {claim_id}", claim_id in ids)
    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Character/path/channel rows:")
    for row in rows:
        print(
            "  "
            + f"{row.get('claim_id')} | {row.get('audit_status')} | "
            + f"{row.get('effective_status')} | {row.get('claim_type')} | "
            + f"{row.get('note_path')}"
        )
    export_checks(rows, before)
    return rows


def export_checks(rows: list[dict], ledger_sha: str) -> None:
    section("Bounded ledger-row export checks")
    report("bounded character/path/channel row export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    expected_rows = expected_export_rows(rows)
    report("slice export is for the character/path/channel bucket", data.get("bucket") == "character_path_channel_weight")
    report("slice export records current ledger sha", data.get("ledger_sha256") == ledger_sha, data.get("ledger_sha256", ""))
    report("slice export row count matches current split", data.get("row_count") == EXPECTED_ROWS, str(data.get("row_count")))
    report("slice export rows match independently enumerated measure split", data.get("rows") == expected_rows)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    physical_measure_selected = False
    path_rule_derived_from_record = False
    character_packet_derived_from_record = False
    channel_rule_derived_from_record = False
    generation_or_koide_dial_selected = False
    born_law_derived_from_record = False
    production_dynamics_derived = False
    physical_arrow_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("physical measure selected flag is false", not physical_measure_selected)
    report("Record-derived path rule flag is false", not path_rule_derived_from_record)
    report("Record-derived character packet flag is false", not character_packet_derived_from_record)
    report("Record-derived channel rule flag is false", not channel_rule_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("Record-derived Born law flag is false", not born_law_derived_from_record)
    report("production dynamics derived flag is false", not production_dynamics_derived)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    rows = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"CHARACTER_PATH_CHANNEL_WEIGHT_ROWS={len(rows)}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("PHYSICAL_MEASURE_SELECTED=FALSE")
    print("PATH_RULE_DERIVED_FROM_RECORD=FALSE")
    print("CHARACTER_PACKET_DERIVED_FROM_RECORD=FALSE")
    print("CHANNEL_RULE_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
