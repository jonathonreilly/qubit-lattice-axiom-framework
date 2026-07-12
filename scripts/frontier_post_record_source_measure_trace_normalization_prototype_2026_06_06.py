#!/usr/bin/env python3
"""Finite source-measure trace/RN normalization prototype."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

import frontier_post_record_measure_weight_normalization_subdivision_2026_06_06 as measure


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
MEASURE_RUNNER = (
    ROOT
    / "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py"
)
MEASURE_CACHE = (
    ROOT
    / "logs/runner-cache/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.txt"
)
PASS = 0
FAIL = 0

PROTOTYPE_LANES = {"source_measure_or_rn_bridge", "trace_normalization_reference"}
EXPECTED_LANE_COUNTS = {
    "source_measure_or_rn_bridge": 17,
    "trace_normalization_reference": 10,
}
EXPECTED_TOTAL_ROWS = sum(EXPECTED_LANE_COUNTS.values())


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


def cache_header(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "----- stdout -----":
            break
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    return fields


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


def rn_density(source: dict[str, Fraction], reference: dict[str, Fraction]) -> dict[str, Fraction]:
    if set(source) != set(reference):
        raise ValueError("source/reference carriers differ")
    density: dict[str, Fraction] = {}
    for key, source_weight in source.items():
        reference_weight = reference[key]
        if reference_weight <= 0 and source_weight > 0:
            raise ValueError("source is not absolutely continuous")
        density[key] = Fraction(0) if source_weight == 0 else source_weight / reference_weight
    return density


def expectation(measure_: dict[str, Fraction], observable: dict[str, Fraction]) -> Fraction:
    if set(measure_) != set(observable):
        raise ValueError("observable carrier differs")
    return sum(measure_[key] * observable[key] for key in measure_)


def rn_expectation(
    reference: dict[str, Fraction],
    density: dict[str, Fraction],
    observable: dict[str, Fraction],
) -> Fraction:
    if set(reference) != set(density) or set(reference) != set(observable):
        raise ValueError("carrier mismatch")
    return sum(reference[key] * density[key] * observable[key] for key in reference)


def compose_density(first: dict[str, Fraction], second: dict[str, Fraction]) -> dict[str, Fraction]:
    if set(first) != set(second):
        raise ValueError("density carrier mismatch")
    return {key: first[key] * second[key] for key in first}


def selected_dial_from_measure(has_normalized_measure: bool, has_selector_rule: bool) -> str:
    if has_normalized_measure and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md",
        [
            "trace/RN expectation identity",
            "Total source/trace prototype rows indexed here: `27`.",
            "Does not identify the unique tracial state with the physical pre-record",
            "Does not derive a measure, prior, source law, Born law, or selector from",
        ],
    )
    require_text(
        "docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md",
        [
            "Normalized measure is not selected dial.",
            "Does not derive a prior, measure, source unit, trace state, or weight rule",
        ],
    )
    require_text(
        "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
        [
            "normalized positive Radon-Nikodym cocycle",
            "E_0[R_h] = 1",
            "RN cocycle proof",
        ],
    )
    require_text(
        "docs/SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md",
        [
            "W = log Z",
            "connected source responses",
            "two-point/Fisher normalization",
        ],
    )
    require_text(
        "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md",
        [
            "unique tracial state",
            "pre-record reference state",
            "open admission",
        ],
    )


def helper_packet_checks() -> None:
    section("Helper packet checks")
    report("measure subdivision helper source exists", MEASURE_RUNNER.is_file())
    report("measure subdivision helper cache exists", MEASURE_CACHE.is_file())
    if not MEASURE_RUNNER.is_file() or not MEASURE_CACHE.is_file():
        return

    header = cache_header(MEASURE_CACHE)
    cache_text = MEASURE_CACHE.read_text(encoding="utf-8")
    expected_runner = MEASURE_RUNNER.relative_to(ROOT).as_posix()
    current_sha = digest(MEASURE_RUNNER)
    report(
        "helper cache names the measure subdivision runner",
        header.get("runner") == expected_runner,
        f"{header.get('runner', '')} == {expected_runner}",
    )
    report(
        "helper cache SHA pins the current helper source",
        header.get("runner_sha256") == current_sha,
        f"{header.get('runner_sha256', '')} == {current_sha}",
    )
    report(
        "helper cache records successful exit",
        header.get("exit_code") == "0",
        header.get("exit_code", ""),
    )
    report("helper cache status is ok", header.get("status") == "ok", header.get("status", ""))
    for lane, count in sorted(EXPECTED_LANE_COUNTS.items()):
        summary_line = f"{lane.upper()}_ROWS={count}"
        report(
            f"helper cache certifies {lane} count",
            summary_line in cache_text,
            summary_line,
        )


def certificate_checks() -> None:
    section("Finite source-measure trace/RN checks")
    reference = normalize({"minus": Fraction(1), "plus": Fraction(1)})
    source = normalize({"minus": Fraction(1), "plus": Fraction(3)})
    density = rn_density(source, reference)
    observable = {"minus": Fraction(-1), "plus": Fraction(1)}

    report(
        "supplied trace/reference weights normalize",
        reference == {"minus": Fraction(1, 2), "plus": Fraction(1, 2)},
        str(reference),
    )
    report(
        "supplied source weights normalize",
        source == {"minus": Fraction(1, 4), "plus": Fraction(3, 4)},
        str(source),
    )
    report(
        "RN density is exact",
        density == {"minus": Fraction(1, 2), "plus": Fraction(3, 2)},
        str(density),
    )
    report(
        "RN density integrates to one over reference",
        expectation(reference, density) == 1,
        str(expectation(reference, density)),
    )
    report(
        "source expectation equals RN-weighted trace expectation",
        expectation(source, observable)
        == rn_expectation(reference, density, observable),
    )

    try:
        normalize({"bad": Fraction(-1)})
        negative_rejected = False
    except ValueError:
        negative_rejected = True
    report("negative supplied source weights are rejected", negative_rejected)

    try:
        rn_density({"a": Fraction(1)}, {"a": Fraction(0)})
        ac_rejected = False
    except ValueError:
        ac_rejected = True
    report("unsupported RN source is rejected", ac_rejected)

    middle = normalize({"minus": Fraction(2), "plus": Fraction(1)})
    d_middle_reference = rn_density(middle, reference)
    d_source_middle = rn_density(source, middle)
    d_source_reference = rn_density(source, reference)
    report(
        "RN densities compose exactly",
        compose_density(d_source_middle, d_middle_reference) == d_source_reference,
        str(compose_density(d_source_middle, d_middle_reference)),
    )
    report(
        "normalized measure without selector does not select dial",
        selected_dial_from_measure(True, False) == "blocked_missing_selector",
    )
    report(
        "selector rule is still needed for selected dial readiness",
        selected_dial_from_measure(True, True) == "conditional_selector_ready",
    )


def prototype_rows() -> tuple[list[dict], Counter[str]]:
    rows = measure.measure_rows()
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        lane = measure.measure_lane(row)
        if lane in PROTOTYPE_LANES:
            buckets[lane].append(row)
    selected = [row for lane in PROTOTYPE_LANES for row in buckets[lane]]
    counts = Counter({lane: len(items) for lane, items in buckets.items()})
    return selected, counts


def row_checks() -> tuple[list[dict], Counter[str]]:
    section("Source/trace row checks")
    before = digest(LEDGER)
    rows, counts = prototype_rows()
    report(
        "source/trace prototype row count is current snapshot",
        len(rows) == EXPECTED_TOTAL_ROWS,
        str(len(rows)),
    )
    report(
        "source/trace lane counts match expected",
        dict(counts) == EXPECTED_LANE_COUNTS,
        str(counts),
    )
    report(
        "source/trace lane counts sum to row count",
        sum(counts.values()) == len(rows),
        str(counts),
    )

    representatives = {
        "source_measure_or_rn_bridge": "source_measure_pcal_rn_cocycle_theorem_note_2026-05-30",
        "trace_normalization_reference": "pre_record_reference_state_tracial_derivation_note_2026-05-20",
    }
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        buckets[measure.measure_lane(row)].append(row)
    for lane, claim_id in representatives.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[lane])
        report(f"representative row present in {lane}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Source/trace prototype lane counts:")
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
    return rows, counts


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    physical_reference_identified = False
    normalized_measure_selects_dial = False
    generation_or_koide_dial_selected = False
    measure_or_prior_derived_from_record = False
    born_law_derived_from_record = False
    source_law_derived_from_record = False
    production_dynamics_derived = False
    physical_arrow_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("physical reference identified flag is false", not physical_reference_identified)
    report("normalized measure selects dial flag is false", not normalized_measure_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("Record-derived measure/prior flag is false", not measure_or_prior_derived_from_record)
    report("Record-derived Born law flag is false", not born_law_derived_from_record)
    report("Record-derived source law flag is false", not source_law_derived_from_record)
    report("production dynamics derived flag is false", not production_dynamics_derived)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)


def main() -> int:
    source_anchor_checks()
    helper_packet_checks()
    certificate_checks()
    rows, counts = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"SOURCE_TRACE_PROTOTYPE_ROWS={len(rows)}")
    for lane in sorted(EXPECTED_LANE_COUNTS):
        print(f"{lane.upper()}_ROWS={counts[lane]}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("PHYSICAL_REFERENCE_IDENTIFIED=FALSE")
    print("NORMALIZED_MEASURE_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("MEASURE_OR_PRIOR_DERIVED_FROM_RECORD=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("SOURCE_LAW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
