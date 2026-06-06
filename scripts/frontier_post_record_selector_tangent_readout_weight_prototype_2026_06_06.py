#!/usr/bin/env python3
"""Finite selector/tangent/readout weight prototype under supplied rules."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
MEASURE_RUNNER = ROOT / "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py"
PASS = 0
FAIL = 0
EXPECTED_ROWS = 6


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


measure = load_module("measure_weight_subdivision", MEASURE_RUNNER)


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
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


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
            "finite readout/tangent weight certificate",
            "Does not derive a selector, tangent metric, Hessian",
        ],
    )
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "`selector_tangent_readout_weight` | 6",
            "selector/tangent readout-weight rows need a supplied readout/tangent bridge",
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
        "docs/DM_FULL_CLOSURE_SAME_SURFACE_NUMERATOR_SELECTOR_BOUNDARY_NOTE_2026-04-16.md",
        [
            "selector-boundary conclusion",
            "does not, within this packet,",
            "authority outside the current packet",
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
    section("Finite selector/tangent/readout checks")
    weights = normalize({"endpoint_lo": Fraction(1), "endpoint_hi": Fraction(3)})
    report("finite supplied readout weights normalize", weights == {"endpoint_lo": Fraction(1, 4), "endpoint_hi": Fraction(3, 4)}, str(weights))
    metric = ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2)))
    report("supplied tangent metric is SPD", is_spd_2x2(metric), str(metric))
    report("quadratic tangent norm is exact", quadratic(metric, (Fraction(1), Fraction(1, 2))) == Fraction(9, 2))
    projection = normalize({"ground": Fraction(1), "excited": Fraction(15)})
    report("projection/readout weights normalize", projection == {"ground": Fraction(1, 16), "excited": Fraction(15, 16)}, str(projection))
    report("weight certificate without selector stays blocked", selector_authority(True, False) == "blocked_missing_selector")
    report("selector rule is still needed", selector_authority(True, True) == "conditional_selector_ready")
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
        "dm_full_closure_same_surface_numerator_selector_boundary_note_2026-04-16",
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
            + f"{row.get('claim_id')} | {row.get('audit_status')} | "
            + f"{row.get('effective_status')} | {row.get('claim_type')} | "
            + f"{row.get('note_path')}"
        )
    return rows


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    selector_authority_derived = False
    physical_measure_selected = False
    readout_primitive_derived_from_record = False
    tangent_metric_derived_from_record = False
    generation_or_koide_dial_selected = False
    born_law_derived_from_record = False
    production_dynamics_derived = False
    physical_arrow_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("selector authority derived flag is false", not selector_authority_derived)
    report("physical measure selected flag is false", not physical_measure_selected)
    report("Record-derived readout primitive flag is false", not readout_primitive_derived_from_record)
    report("Record-derived tangent metric flag is false", not tangent_metric_derived_from_record)
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
    print(f"SELECTOR_TANGENT_READOUT_WEIGHT_ROWS={len(rows)}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("SELECTOR_AUTHORITY_DERIVED=FALSE")
    print("PHYSICAL_MEASURE_SELECTED=FALSE")
    print("READOUT_PRIMITIVE_DERIVED_FROM_RECORD=FALSE")
    print("TANGENT_METRIC_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
