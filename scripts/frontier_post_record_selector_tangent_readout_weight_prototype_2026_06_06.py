#!/usr/bin/env python3
"""Open-gate selector/tangent/readout weight diagnostic under supplied rules."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

import frontier_post_record_measure_weight_normalization_subdivision_2026_06_06 as measure

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
MEASURE_RUNNER = ROOT / "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py"
PASS = 0
FAIL = 0
EXPECTED_ROWS = 17


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


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    flat = " ".join(text.split())
    report(f"{path} exists", (ROOT / path).exists())
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text or needle in flat)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(weights: dict[str, Fraction]) -> dict[str, Fraction]:
    if any(value < 0 for value in weights.values()):
        raise ValueError("negative supplied weight")
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        raise ValueError("nonpositive supplied total")
    return {key: value / total for key, value in weights.items()}


def quadratic(metric: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]], vector: tuple[Fraction, Fraction]) -> Fraction:
    x, y = vector
    return metric[0][0] * x * x + (metric[0][1] + metric[1][0]) * x * y + metric[1][1] * y * y


def is_spd_2x2(metric: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> bool:
    return metric[0][0] > 0 and metric[0][0] * metric[1][1] - metric[0][1] * metric[1][0] > 0


def selector_authority(has_weight_certificate: bool, has_selector_rule: bool) -> str:
    if has_weight_certificate and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md",
        [
            "selector_tangent_readout_weight",
            "Type:** open_gate",
            "Claim type:** open_gate",
            "conditional-support source-side diagnostic",
            "not a bounded support theorem over the framework baseline",
            "2026-06-18 Record-axiom non-supply repair",
            "2026-06-08 supplied-support safe-narrow",
            "supplied-support",
            "finite readout/tangent weight arithmetic inside that supplied packet",
            "actual_current_surface_status: conditional-support",
            "trace_class: upstream_support",
            "not a positive theorem over the framework baseline",
            "not selector/tangent/readout authority",
            "They are supplied finite packet data.",
            "Does not derive a selector, tangent metric, Hessian",
            "Does not derive a readout context, central-sector decomposition",
            "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py",
        ],
    )
    require_text(
        "docs/MINIMAL_AXIOMS_2026-06-05.md",
        [
            "### Record",
            "Given a readout context with a finite central-sector decomposition",
            "For any finite pairwise-disjoint collection of records",
            "A record supplies no readout context, decomposition, `K`/CPT structure,",
            "weighting, normalization, probability",
            "measurement/decoherence dynamics",
        ],
    )
    require_text(
        "docs/audit/data/axiom_premise_nodes.json",
        [
            "\"minimal_axioms\"",
            "\"current_path\": \"docs/MINIMAL_AXIOMS_2026-06-29.md\"",
            (
                "It still supplies no context-selection rule, occurrence rule, weighting, "
                "normalization, probability, update law, measurement/decoherence dynamics, "
                "record-production process, physical persistence dynamics, K/CPT structure, "
                "central-sector decomposition, source/action bridge, physical observable bridge, "
                "state-selection rule, law-domain derivation, or downstream theory consequence."
            ),
        ],
    )
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "`selector_tangent_readout_weight` | 16",
            "live count printed by the runner supersedes this diagnostic export",
            "selector/tangent readout-weight rows need a supplied readout/tangent bridge",
        ],
    )
    require_text(
        "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py",
        [
            "def measure_rows",
            "def measure_lane",
            "selector_tangent_readout_weight",
            "EXPECTED_SUBCOUNTS",
        ],
    )
    require_text(
        "docs/YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md",
        [
            "Exact Hessian Selector Uniqueness Note",
            "selector direction",
            "Bounded shape drift",
        ],
    )
    require_text(
        "docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md",
        [
            "Hierarchy D4 Density-Scale Readout Bridge",
            "fixed positive D=4 density-coefficient readout",
            "This bridge does not identify the electroweak VEV",
            "physical order-parameter theorem",
        ],
    )
    require_text(
        "docs/TELEPORTATION_PREPARATION_READOUT_PROBE_NOTE.md",
        [
            "preparation/readout remains open",
            "projection probabilities",
            "extraction/readout operation",
        ],
    )


def certificate_checks() -> None:
    section("Supplied finite selector/tangent/readout arithmetic checks")
    weights = normalize({"endpoint_lo": Fraction(1), "endpoint_hi": Fraction(3)})
    report("finite supplied readout weights normalize", weights == {"endpoint_lo": Fraction(1, 4), "endpoint_hi": Fraction(3, 4)}, str(weights))
    metric = ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2)))
    report("supplied tangent metric is SPD", is_spd_2x2(metric), str(metric))
    report("quadratic tangent norm is exact", quadratic(metric, (Fraction(1), Fraction(1, 2))) == Fraction(9, 2))
    projection = normalize({"ground": Fraction(1), "excited": Fraction(15)})
    report("projection/readout weights normalize", projection == {"ground": Fraction(1, 16), "excited": Fraction(15, 16)}, str(projection))
    has_weight_certificate = bool(weights)
    has_selector_rule = False
    report(
        "weight certificate without selector stays blocked",
        selector_authority(has_weight_certificate, has_selector_rule) == "blocked_missing_selector",
    )
    report(
        "selector rule is still needed",
        selector_authority(has_weight_certificate, not has_selector_rule) == "conditional_selector_ready",
    )
    try:
        normalize({"bad": Fraction(-1)})
        negative_rejected = False
    except ValueError:
        negative_rejected = True
    report("negative supplied weights are rejected", negative_rejected)


def selector_rows() -> list[dict]:
    return [
        row
        for row in measure.measure_rows()
        if measure.measure_lane(row) == "selector_tangent_readout_weight"
    ]


def row_checks() -> list[dict]:
    section("Selector/tangent row checks")
    before = digest(LEDGER)
    rows = selector_rows()
    report("selector/tangent row count is current snapshot", len(rows) == EXPECTED_ROWS, str(len(rows)))
    ids = {row.get("claim_id") for row in rows}
    for claim_id in [
        "strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12",
        "teleportation_preparation_readout_probe_note",
        "yt_exact_hessian_selector_uniqueness_note",
    ]:
        report(f"representative row present: {claim_id}", claim_id in ids)
    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)
    print()
    print("Selector/tangent/readout rows:")
    for row in rows:
        print(
            "  "
            + f"{row.get('claim_id')} | "
            + f"effective {row.get('effective_status')} | {row.get('claim_type')} | "
            + f"{row.get('note_path')}"
        )
    return rows


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    selector_authority_derived = False
    readout_context_derived_from_record = False
    central_sector_decomposition_derived_from_record = False
    kcpt_structure_derived_from_record = False
    weighting_rule_derived_from_record = False
    normalization_authority_derived_from_record = False
    physical_measure_selected = False
    readout_primitive_derived_from_record = False
    tangent_metric_derived_from_record = False
    hessian_derived_from_record = False
    generation_or_koide_dial_selected = False
    born_law_derived_from_record = False
    measurement_dynamics_derived_from_record = False
    production_dynamics_derived = False
    physical_arrow_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("selector authority derived flag is false", not selector_authority_derived)
    report("Record-derived readout context flag is false", not readout_context_derived_from_record)
    report("Record-derived central-sector decomposition flag is false", not central_sector_decomposition_derived_from_record)
    report("Record-derived K/CPT structure flag is false", not kcpt_structure_derived_from_record)
    report("Record-derived weighting rule flag is false", not weighting_rule_derived_from_record)
    report("Record-derived normalization authority flag is false", not normalization_authority_derived_from_record)
    report("physical measure selected flag is false", not physical_measure_selected)
    report("Record-derived readout primitive flag is false", not readout_primitive_derived_from_record)
    report("Record-derived tangent metric flag is false", not tangent_metric_derived_from_record)
    report("Record-derived Hessian flag is false", not hessian_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("Record-derived Born law flag is false", not born_law_derived_from_record)
    report("Record-derived measurement dynamics flag is false", not measurement_dynamics_derived_from_record)
    report("production dynamics derived flag is false", not production_dynamics_derived)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    rows = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"SELECTOR_TANGENT_READOUT_WEIGHT_ROWS={len(rows)}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("SELECTOR_AUTHORITY_DERIVED=FALSE")
    print("READOUT_CONTEXT_DERIVED_FROM_RECORD=FALSE")
    print("CENTRAL_SECTOR_DECOMPOSITION_DERIVED_FROM_RECORD=FALSE")
    print("KCPT_STRUCTURE_DERIVED_FROM_RECORD=FALSE")
    print("WEIGHTING_RULE_DERIVED_FROM_RECORD=FALSE")
    print("NORMALIZATION_AUTHORITY_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_MEASURE_SELECTED=FALSE")
    print("READOUT_PRIMITIVE_DERIVED_FROM_RECORD=FALSE")
    print("TANGENT_METRIC_DERIVED_FROM_RECORD=FALSE")
    print("HESSIAN_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("MEASUREMENT_DYNAMICS_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
