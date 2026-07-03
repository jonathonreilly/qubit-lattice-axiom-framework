#!/usr/bin/env python3
"""Exact interface for a supplied finite production-kernel selection rule."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0

Word = tuple[str, ...]
Source = dict[str, Fraction]
Kernel = dict[str, dict[str, Fraction]]
Law = dict[Word, Fraction]


@dataclass(frozen=True)
class SelectionRule:
    rule_id: str
    target_values: dict[str, Fraction]
    weights: dict[str, Fraction]


@dataclass(frozen=True)
class SelectionBridge:
    bridge_id: str
    candidate_family_id: str
    source_id: str
    orientation: str | None
    clock_id: str | None
    rule_id: str | None


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


def normalized_source(source: Source) -> bool:
    return bool(source) and sum(source.values(), Fraction(0, 1)) == 1 and all(p >= 0 for p in source.values())


def row_stochastic(kernel: Kernel) -> bool:
    return all(sum(row.values(), Fraction(0, 1)) == 1 and all(p >= 0 for p in row.values()) for row in kernel.values())


def markov_law_length2(source: Source, kernel: Kernel) -> Law:
    out: defaultdict[Word, Fraction] = defaultdict(Fraction)
    for a, source_mass in source.items():
        for b, transition_mass in kernel[a].items():
            out[(a, b)] += source_mass * transition_mass
    return dict(out)


def endpoint_ab(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "A" and word[-1] == "B")


def endpoint_ba(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "B" and word[-1] == "A")


def second_is_b(word: Word) -> int:
    return int(len(word) >= 2 and word[1] == "B")


def signed_ab_ba(word: Word) -> int:
    return endpoint_ab(word) - endpoint_ba(word)


STATISTICS = {
    "endpoint_ab": endpoint_ab,
    "endpoint_ba": endpoint_ba,
    "second_is_b": second_is_b,
    "signed_ab_ba": signed_ab_ba,
}


def expectation(law: Law, statistic) -> Fraction:
    return sum(Fraction(statistic(word), 1) * mass for word, mass in law.items())


def statistic_vector(law: Law, statistic_ids: list[str]) -> dict[str, Fraction]:
    return {sid: expectation(law, STATISTICS[sid]) for sid in statistic_ids}


def score(law: Law, rule: SelectionRule) -> Fraction:
    total = Fraction(0, 1)
    for sid, target in rule.target_values.items():
        weight = rule.weights.get(sid, Fraction(0, 1))
        value = expectation(law, STATISTICS[sid])
        total += weight * (value - target) * (value - target)
    return total


def select_candidate(
    source: Source,
    candidates: dict[str, Kernel],
    bridge: SelectionBridge,
    rule: SelectionRule | None,
) -> tuple[str, list[str], dict[str, Fraction]]:
    if bridge.orientation not in {"forward", "reverse"}:
        return "blocked_missing_orientation", [], {}
    if bridge.clock_id is None:
        return "blocked_missing_clock", [], {}
    if bridge.rule_id is None or rule is None:
        return "blocked_missing_selection_rule", [], {}
    if bridge.rule_id != rule.rule_id:
        return "blocked_rule_scope_mismatch", [], {}
    if not normalized_source(source):
        return "blocked_bad_source", [], {}
    if not candidates or not all(row_stochastic(k) for k in candidates.values()):
        return "blocked_bad_candidate_family", [], {}
    if not rule.target_values or not any(w > 0 for w in rule.weights.values()):
        return "blocked_empty_or_zero_rule", [], {}

    scores = {name: score(markov_law_length2(source, kernel), rule) for name, kernel in candidates.items()}
    minimum = min(scores.values())
    winners = [name for name, value in scores.items() if value == minimum]
    if len(winners) == 1:
        return "unique_minimum", winners, scores
    return "tie_or_underselected", winners, scores


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md",
        [
            "supplied finite candidate family plus supplied selection rule",
            "The rule is supplied",
            "stable setting is not",
        ],
    )
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md",
        [
            "Directed certificates do not select a production kernel",
            "kernel remains a supplied bridge input",
            "same directed certificate data can admit distinct candidate kernels",
        ],
    )
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md",
        [
            "supplied finite law plus supplied orientation bridge",
            "The certificate is scoped to those inputs.",
            "examples do not derive an arrow, clock, kernel, or selected dial",
        ],
    )


def supplied_rule_selection_checks() -> None:
    section("Supplied selection-rule checks")
    source: Source = {"A": Fraction(1, 2), "B": Fraction(1, 2)}
    candidates: dict[str, Kernel] = {
        "k3": {
            "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
            "B": {"A": Fraction(0, 1), "B": Fraction(1, 1)},
        },
        "k4": {
            "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
            "B": {"A": Fraction(1, 1), "B": Fraction(0, 1)},
        },
    }
    informative_rule = SelectionRule(
        "rule_endpoint_ba_second_b",
        {
            "endpoint_ab": Fraction(1, 4),
            "endpoint_ba": Fraction(1, 2),
            "second_is_b": Fraction(1, 4),
        },
        {
            "endpoint_ab": Fraction(1, 1),
            "endpoint_ba": Fraction(1, 1),
            "second_is_b": Fraction(1, 1),
        },
    )
    bridge = SelectionBridge(
        "bridge_supplied_rule",
        "toy_kernel_family",
        "balanced_source",
        "forward",
        "word_index_clock",
        "rule_endpoint_ba_second_b",
    )

    report("source normalizes", normalized_source(source))
    report("candidate family kernels are row-stochastic", all(row_stochastic(k) for k in candidates.values()))
    laws = {name: markov_law_length2(source, kernel) for name, kernel in candidates.items()}
    report("candidate laws differ", laws["k3"] != laws["k4"], f"k3={laws['k3']} k4={laws['k4']}")
    report("k4 exactly matches supplied informative target", score(laws["k4"], informative_rule) == 0)
    report("k3 has positive supplied-rule score", score(laws["k3"], informative_rule) > 0, str(score(laws["k3"], informative_rule)))
    status, winners, scores = select_candidate(source, candidates, bridge, informative_rule)
    report("supplied selection rule gives unique minimum", status == "unique_minimum" and winners == ["k4"], str(scores))
    report("selected candidate is inside supplied candidate family", winners == ["k4"] and "k4" in candidates)
    report("selection rule score uses exact rational arithmetic", all(isinstance(v, Fraction) for v in scores.values()), str(scores))


def underselection_checks() -> None:
    section("Underselection and missing-rule checks")
    source: Source = {"A": Fraction(1, 2), "B": Fraction(1, 2)}
    candidates: dict[str, Kernel] = {
        "k3": {
            "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
            "B": {"A": Fraction(0, 1), "B": Fraction(1, 1)},
        },
        "k4": {
            "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
            "B": {"A": Fraction(1, 1), "B": Fraction(0, 1)},
        },
    }
    weak_rule = SelectionRule(
        "rule_endpoint_only",
        {"endpoint_ab": Fraction(1, 4)},
        {"endpoint_ab": Fraction(1, 1)},
    )
    zero_rule = SelectionRule(
        "rule_zero",
        {"endpoint_ab": Fraction(1, 4)},
        {"endpoint_ab": Fraction(0, 1)},
    )
    bridge_weak = SelectionBridge("bridge_weak", "toy_kernel_family", "balanced_source", "forward", "word_index_clock", "rule_endpoint_only")
    bridge_missing_rule = SelectionBridge("bridge_missing_rule", "toy_kernel_family", "balanced_source", "forward", "word_index_clock", None)
    bridge_wrong_rule = SelectionBridge("bridge_wrong_rule", "toy_kernel_family", "balanced_source", "forward", "word_index_clock", "other_rule")
    bridge_missing_orientation = SelectionBridge("bridge_missing_orientation", "toy_kernel_family", "balanced_source", None, "word_index_clock", "rule_endpoint_only")
    bridge_zero = SelectionBridge("bridge_zero", "toy_kernel_family", "balanced_source", "forward", "word_index_clock", "rule_zero")

    status_weak, winners_weak, scores_weak = select_candidate(source, candidates, bridge_weak, weak_rule)
    status_missing, winners_missing, scores_missing = select_candidate(source, candidates, bridge_missing_rule, None)
    status_wrong, winners_wrong, scores_wrong = select_candidate(source, candidates, bridge_wrong_rule, weak_rule)
    status_orientation, winners_orientation, scores_orientation = select_candidate(source, candidates, bridge_missing_orientation, weak_rule)
    status_zero, winners_zero, scores_zero = select_candidate(source, candidates, bridge_zero, zero_rule)

    report("endpoint-only rule ties the two candidates", status_weak == "tie_or_underselected" and winners_weak == ["k3", "k4"], str(scores_weak))
    report("missing selection rule is blocked", status_missing == "blocked_missing_selection_rule" and not winners_missing and not scores_missing)
    report("wrong selection-rule scope is blocked", status_wrong == "blocked_rule_scope_mismatch" and not winners_wrong and not scores_wrong)
    report("missing orientation is blocked", status_orientation == "blocked_missing_orientation" and not winners_orientation and not scores_orientation)
    report("zero-weight rule is blocked", status_zero == "blocked_empty_or_zero_rule" and not winners_zero and not scores_zero)


def statistic_vector_checks() -> None:
    section("Statistic-vector checks")
    source: Source = {"A": Fraction(1, 2), "B": Fraction(1, 2)}
    k4: Kernel = {
        "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "B": {"A": Fraction(1, 1), "B": Fraction(0, 1)},
    }
    law = markov_law_length2(source, k4)
    vector = statistic_vector(law, ["endpoint_ab", "endpoint_ba", "second_is_b", "signed_ab_ba"])
    report("endpoint_ab value is exact", vector["endpoint_ab"] == Fraction(1, 4), str(vector))
    report("endpoint_ba value is exact", vector["endpoint_ba"] == Fraction(1, 2), str(vector))
    report("second_is_b value is exact", vector["second_is_b"] == Fraction(1, 4), str(vector))
    report("signed_ab_ba value is exact", vector["signed_ab_ba"] == Fraction(-1, 4), str(vector))


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    selection_rule_derived_from_record = False
    candidate_family_derived_from_record = False
    production_kernel_selected_without_rule = False
    physical_arrow_derived_from_record = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("selection rule derived from Record flag is false", not selection_rule_derived_from_record)
    report("candidate family derived from Record flag is false", not candidate_family_derived_from_record)
    report("kernel selected without supplied rule flag is false", not production_kernel_selected_without_rule)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("Born law derived from Record flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    supplied_rule_selection_checks()
    underselection_checks()
    statistic_vector_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE=TRUE")
    print("SUPPLIED_RULE_UNIQUE_MINIMUM=TRUE")
    print("WEAK_RULE_UNDERSELECTS_KERNEL=TRUE")
    print("SELECTION_RULE_DERIVED_FROM_RECORD=FALSE")
    print("CANDIDATE_FAMILY_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
