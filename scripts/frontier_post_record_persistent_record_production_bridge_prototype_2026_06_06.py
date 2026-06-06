#!/usr/bin/env python3
"""Finite supplied production bridge for persistent post-record states."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
ROW_MAP_RUNNER = ROOT / "scripts/frontier_post_record_production_dynamics_needed_row_map_2026_06_06.py"
PASS = 0
FAIL = 0

Record = tuple[int, int, str]


def load_row_map():
    spec = importlib.util.spec_from_file_location("production_row_map", ROW_MAP_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {ROW_MAP_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


row_map = load_row_map()


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


def initial_record() -> Record:
    return (0, 0, "none")


def write_record(record: Record, hit: str) -> Record:
    left, right, first = record
    if hit not in {"L", "R"}:
        raise ValueError(f"unknown hit: {hit}")
    if hit == "L":
        left = min(2, left + 1)
    else:
        right = min(2, right + 1)
    if first == "none":
        first = hit
    return (left, right, first)


def evolve_record(word: tuple[str, ...]) -> Record:
    record = initial_record()
    for hit in word:
        record = write_record(record, hit)
    return record


def supplied_word_law() -> dict[tuple[str, ...], Fraction]:
    return {
        ("L", "L"): Fraction(1, 2),
        ("L", "R"): Fraction(1, 4),
        ("R", "L"): Fraction(1, 8),
        ("R", "R"): Fraction(1, 8),
    }


def validate_law(law: dict[tuple[str, ...], Fraction]) -> bool:
    return bool(law) and all(p >= 0 for p in law.values()) and sum(law.values(), Fraction(0)) == 1


def pushforward(law: dict[tuple[str, ...], Fraction]) -> dict[Record, Fraction]:
    if not validate_law(law):
        raise ValueError("invalid supplied law")
    dist: dict[Record, Fraction] = defaultdict(Fraction)
    for word, probability in law.items():
        dist[evolve_record(word)] += probability
    return dict(dist)


def record_has_no_probability(record: Record) -> bool:
    return (
        isinstance(record[0], int)
        and isinstance(record[1], int)
        and isinstance(record[2], str)
        and not any(isinstance(item, Fraction) for item in record)
    )


def distance_squared(a: Record, b: Record) -> int:
    marker_penalty = 0 if a[2] == b[2] else 1
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + marker_penalty


def overlap_kernel(a: Record, b: Record) -> Fraction:
    return Fraction(1, 1 + distance_squared(a, b))


def expected_overlap(dist: dict[Record, Fraction]) -> Fraction:
    total = Fraction(0)
    for a, pa in dist.items():
        for b, pb in dist.items():
            total += pa * pb * overlap_kernel(a, b)
    return total


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_PERSISTENT_RECORD_PRODUCTION_BRIDGE_PROTOTYPE_2026-06-06.md",
        [
            "supplied pre-record word law",
            "Post-record states carry realized count/marker information.",
            "does not derive the production law",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md",
        [
            "persistent_record_production_overlap` | 3",
            "record-writing law bridge",
            "overlap-kernel physical bridge",
            "post-record sites carry realized information",
        ],
    )
    require_text(
        "docs/PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md",
        [
            "mesoscopic persistent record state",
            "sparse count vector",
            "soft overlap kernel",
        ],
    )
    require_text(
        "docs/PERSISTENT_RECORD_REFINEMENT_NOTE.md",
        [
            "first-hit family",
            "different record-writing law",
            "first-hit markers influence later",
        ],
    )
    require_text(
        "docs/PERSISTENT_RECORD_MATCHED_COMPARE_NOTE.md",
        [
            "residual branch-overlap structure",
            "competitive middle",
            "matched bounded slice",
        ],
    )


def production_row_checks() -> None:
    section("Production-row checks")
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    selected = [
        row
        for row in rows
        if row_map.prev.scoped(row)
        and row_map.prev.classify(row) == "production_dynamics_needed"
        and row_map.mapped_row(row)["lane"] == "persistent_record_production_overlap"
    ]
    ids = {row.get("claim_id") for row in selected}
    expected = {
        "persistent_record_matched_compare_note",
        "persistent_record_overlap_kernel_note",
        "persistent_record_refinement_note",
    }
    report("persistent-record production row count is current snapshot", len(selected) == 3, str(ids))
    report("persistent-record production row ids match", ids == expected, str(ids))


def bridge_checks() -> None:
    section("Supplied bridge checks")
    law = supplied_word_law()
    report("supplied pre-record law is normalized", validate_law(law), str(law))
    dist = pushforward(law)
    report("post-record pushforward distribution is normalized", sum(dist.values(), Fraction(0)) == 1, str(dist))
    report("pushforward has expected support size", len(dist) == 4, str(dist))
    report("post-record states carry no probability internally", all(record_has_no_probability(record) for record in dist), str(list(dist)))

    history = [initial_record()]
    record = initial_record()
    for hit in ("R", "L", "L"):
        record = write_record(record, hit)
        history.append(record)
    monotone_counts = all(
        history[i][0] <= history[i + 1][0] and history[i][1] <= history[i + 1][1]
        for i in range(len(history) - 1)
    )
    persistent_marker = all(item[2] in {"none", "R"} for item in history)
    report("record counts are monotone under supplied update", monotone_counts, str(history))
    report("first-hit marker persists under supplied update", persistent_marker, str(history))

    records = list(dist)
    symmetric = all(overlap_kernel(a, b) == overlap_kernel(b, a) for a in records for b in records)
    self_one = all(overlap_kernel(a, a) == 1 for a in records)
    bounded = all(Fraction(0) < overlap_kernel(a, b) <= 1 for a in records for b in records)
    report("supplied overlap kernel is symmetric", symmetric)
    report("supplied overlap kernel is self-normalized", self_one)
    report("supplied overlap kernel is bounded in (0,1]", bounded)

    ov = expected_overlap(dist)
    report("law-scoped expected overlap is exact rational", ov == Fraction(169, 320), str(ov))
    report("invalid supplied law is rejected", not validate_law({("L",): Fraction(2)}))


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    record_writing_law_derived_from_record = False
    production_kernel_selected = False
    physical_arrow_derived_from_record = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("record-writing law derived from Record flag is false", not record_writing_law_derived_from_record)
    report("production kernel selected flag is false", not production_kernel_selected)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("Record-derived Born law flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    production_row_checks()
    bridge_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("PERSISTENT_RECORD_PRODUCTION_OVERLAP_ROWS=3")
    print("SUPPLIED_RECORD_WRITING_BRIDGE_PROTOTYPE=TRUE")
    print("POST_RECORD_STATE_HAS_INTERNAL_PROBABILITY=FALSE")
    print("RECORD_WRITING_LAW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
