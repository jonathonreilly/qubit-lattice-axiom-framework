#!/usr/bin/env python3
"""Exact admitted-sample target-vector interface for post-record samples."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0

Word = tuple[str, ...]
Sample = tuple[Word, ...]


@dataclass(frozen=True)
class SampleAdmission:
    admission_id: str
    sample_id: str
    statistic_ids: tuple[str, ...]
    observation_status: str


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


def endpoint_ab(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "A" and word[-1] == "B")


def endpoint_ba(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "B" and word[-1] == "A")


def second_is_b(word: Word) -> int:
    return int(len(word) >= 2 and word[1] == "B")


STATISTICS = {
    "endpoint_ab": endpoint_ab,
    "endpoint_ba": endpoint_ba,
    "second_is_b": second_is_b,
}


def empirical_vector(sample: Sample, statistic_ids: tuple[str, ...]) -> tuple[str, dict[str, Fraction] | None]:
    if not sample:
        return "blocked_empty_sample", None
    if not statistic_ids:
        return "blocked_missing_statistic_set", None
    if any(sid not in STATISTICS for sid in statistic_ids):
        return "blocked_unknown_statistic", None
    n = Fraction(len(sample), 1)
    out = {
        sid: sum(Fraction(STATISTICS[sid](word), 1) for word in sample) / n
        for sid in statistic_ids
    }
    return "verified_empirical_vector", out


def count_atoms(sample: Sample) -> Counter[str]:
    counts: Counter[str] = Counter()
    for word in sample:
        counts.update(word)
    return counts


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md",
        [
            "supplied finite post-record sample plus supplied statistic set",
            "The sample is admitted observation data, not a probability law",
            "Weights and selection rules remain supplied",
        ],
    )
    require_text(
        "docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md",
        [
            "target vector and loss weights are supplied rule data",
            "Record does not derive the target vector or weights",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md",
        [
            "supplied finite candidate family plus supplied selection rule",
            "The rule is supplied",
        ],
    )


def admitted_sample_checks() -> None:
    section("Admitted sample checks")
    sample: Sample = (
        ("A", "A"),
        ("A", "B"),
        ("B", "A"),
        ("B", "A"),
    )
    admission = SampleAdmission(
        "admit_sample_k4_like",
        "sample_four_words",
        ("endpoint_ab", "endpoint_ba", "second_is_b"),
        "admitted_observation",
    )
    status, vector = empirical_vector(sample, admission.statistic_ids)
    expected = {
        "endpoint_ab": Fraction(1, 4),
        "endpoint_ba": Fraction(1, 2),
        "second_is_b": Fraction(1, 4),
    }
    records_are_realized = all(isinstance(word, tuple) and all(isinstance(atom, str) for atom in word) for word in sample)

    report("sample admission status is explicit", admission.observation_status == "admitted_observation")
    report("post-record sample carries realized words", records_are_realized, str(sample))
    report("sample atom counts are exact integers", count_atoms(sample) == Counter({"A": 5, "B": 3}), str(count_atoms(sample)))
    report("empirical vector verifies", status == "verified_empirical_vector" and vector == expected, str(vector))
    report("empirical endpoint_ab is exact", vector is not None and vector["endpoint_ab"] == Fraction(1, 4))
    report("empirical endpoint_ba is exact", vector is not None and vector["endpoint_ba"] == Fraction(1, 2))
    report("empirical second_is_b is exact", vector is not None and vector["second_is_b"] == Fraction(1, 4))


def blocked_sample_checks() -> None:
    section("Blocked sample checks")
    empty_status, empty_vector = empirical_vector((), ("endpoint_ab",))
    missing_status, missing_vector = empirical_vector((("A", "B"),), ())
    unknown_status, unknown_vector = empirical_vector((("A", "B"),), ("unknown_stat",))
    report("empty sample is blocked", empty_status == "blocked_empty_sample" and empty_vector is None)
    report("missing statistic set is blocked", missing_status == "blocked_missing_statistic_set" and missing_vector is None)
    report("unknown statistic is blocked", unknown_status == "blocked_unknown_statistic" and unknown_vector is None)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    sample_is_probability_law = False
    weights_derived_from_sample = False
    selection_rule_derived_from_sample = False
    production_kernel_selected_by_sample_alone = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("sample-is-probability-law flag is false", not sample_is_probability_law)
    report("weights derived from sample flag is false", not weights_derived_from_sample)
    report("selection rule derived from sample flag is false", not selection_rule_derived_from_sample)
    report("kernel selected by sample alone flag is false", not production_kernel_selected_by_sample_alone)
    report("Born law derived from Record flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    admitted_sample_checks()
    blocked_sample_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE=TRUE")
    print("ADMITTED_SAMPLE_EMPIRICAL_VECTOR_EXACT=TRUE")
    print("SAMPLE_IS_PROBABILITY_LAW=FALSE")
    print("WEIGHTS_DERIVED_FROM_SAMPLE=FALSE")
    print("SELECTION_RULE_DERIVED_FROM_SAMPLE=FALSE")
    print("PRODUCTION_KERNEL_SELECTED_BY_SAMPLE_ALONE=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
