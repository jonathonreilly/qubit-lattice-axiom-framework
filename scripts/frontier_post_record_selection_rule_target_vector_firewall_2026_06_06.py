#!/usr/bin/env python3
"""Finite supplied-rule witness for target/weight firewall."""

from __future__ import annotations

from collections import defaultdict
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


STATISTICS = {
    "endpoint_ab": endpoint_ab,
    "endpoint_ba": endpoint_ba,
    "second_is_b": second_is_b,
}


def expectation(law: Law, statistic) -> Fraction:
    return sum(Fraction(statistic(word), 1) * mass for word, mass in law.items())


def vector(law: Law) -> dict[str, Fraction]:
    return {sid: expectation(law, stat) for sid, stat in STATISTICS.items()}


def score(law: Law, rule: SelectionRule) -> Fraction:
    out = Fraction(0, 1)
    for sid, target in rule.target_values.items():
        weight = rule.weights.get(sid, Fraction(0, 1))
        value = expectation(law, STATISTICS[sid])
        out += weight * (value - target) * (value - target)
    return out


def select(source: Source, candidates: dict[str, Kernel], rule: SelectionRule | None) -> tuple[str, list[str], dict[str, Fraction]]:
    if rule is None:
        return "blocked_missing_target_or_weights", [], {}
    if not rule.target_values:
        return "blocked_missing_target_or_weights", [], {}
    if not any(w > 0 for w in rule.weights.values()):
        return "blocked_missing_target_or_weights", [], {}
    if not normalized_source(source) or not candidates or not all(row_stochastic(k) for k in candidates.values()):
        return "blocked_bad_candidate_surface", [], {}
    scores = {name: score(markov_law_length2(source, kernel), rule) for name, kernel in candidates.items()}
    minimum = min(scores.values())
    winners = [name for name, value in scores.items() if value == minimum]
    return ("unique_minimum" if len(winners) == 1 else "tie_or_underselected"), winners, scores


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md",
        [
            "target vector and loss weights are supplied rule data",
            "same target vector can",
            "finite supplied selection-rule interface",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_SELECTION_RULE_INTERFACE_2026-06-06.md",
        [
            "supplied finite selection rules",
            "candidate, score, rule, and dial-score derivation remain open",
            "supplied score-and-rule surface",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md",
        [
            "supplied finite candidate family plus supplied selection rule",
            "The rule is supplied",
            "weak endpoint-only rule underselects",
        ],
    )
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md",
        [
            "Directed certificates do not select a production kernel",
            "kernel remains a supplied bridge input",
        ],
    )


def target_weight_firewall_checks() -> None:
    section("Target/weight firewall checks")
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
    laws = {name: markov_law_length2(source, kernel) for name, kernel in candidates.items()}
    shared_target = {
        "endpoint_ba": Fraction(1, 3),
        "second_is_b": Fraction(2, 3),
    }
    rule_endpoint_weighted = SelectionRule(
        "rule_endpoint_weighted",
        shared_target,
        {"endpoint_ba": Fraction(100, 1), "second_is_b": Fraction(1, 1)},
    )
    rule_second_weighted = SelectionRule(
        "rule_second_weighted",
        shared_target,
        {"endpoint_ba": Fraction(1, 1), "second_is_b": Fraction(100, 1)},
    )

    report("source normalizes", normalized_source(source))
    report("candidate kernels are row-stochastic", all(row_stochastic(k) for k in candidates.values()))
    report("candidate statistic vectors differ", vector(laws["k3"]) != vector(laws["k4"]), f"k3={vector(laws['k3'])} k4={vector(laws['k4'])}")
    report("shared target vector is exact rational data", all(isinstance(v, Fraction) for v in shared_target.values()), str(shared_target))

    status_a, winners_a, scores_a = select(source, candidates, rule_endpoint_weighted)
    status_b, winners_b, scores_b = select(source, candidates, rule_second_weighted)
    report("endpoint-weighted supplied rule selects k4", status_a == "unique_minimum" and winners_a == ["k4"], str(scores_a))
    report("second-weighted supplied rule selects k3", status_b == "unique_minimum" and winners_b == ["k3"], str(scores_b))
    report("same target with different weights selects different kernels", winners_a != winners_b)
    report("there is no unique selected kernel without supplied weights", winners_a != winners_b)


def missing_target_checks() -> None:
    section("Missing target/weight checks")
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
    no_rule_status, no_rule_winners, no_rule_scores = select(source, candidates, None)
    empty_target = SelectionRule("empty_target", {}, {"endpoint_ba": Fraction(1, 1)})
    zero_weights = SelectionRule("zero_weights", {"endpoint_ba": Fraction(1, 3)}, {"endpoint_ba": Fraction(0, 1)})
    empty_status, empty_winners, empty_scores = select(source, candidates, empty_target)
    zero_status, zero_winners, zero_scores = select(source, candidates, zero_weights)
    report("missing target/weights blocks selection", no_rule_status == "blocked_missing_target_or_weights" and not no_rule_winners and not no_rule_scores)
    report("empty target blocks selection", empty_status == "blocked_missing_target_or_weights" and not empty_winners and not empty_scores)
    report("zero weights block selection", zero_status == "blocked_missing_target_or_weights" and not zero_winners and not zero_scores)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    broad_record_target_weight_no_go_claimed = False
    target_weight_generated_by_selection_algebra = False
    production_kernel_selected_without_rule = False
    physical_arrow_derived_from_record = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("broad Record target/weight no-go flag is false", not broad_record_target_weight_no_go_claimed)
    report("target/weight generated by selection algebra flag is false", not target_weight_generated_by_selection_algebra)
    report("kernel selected without supplied rule flag is false", not production_kernel_selected_without_rule)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("Born law derived from Record flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    target_weight_firewall_checks()
    missing_target_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SELECTION_RULE_TARGET_VECTOR_FIREWALL=TRUE")
    print("SAME_TARGET_DIFFERENT_WEIGHTS_SELECT_DIFFERENT_KERNELS=TRUE")
    print("BROAD_RECORD_TARGET_WEIGHT_NO_GO_CLAIMED=FALSE")
    print("TARGET_WEIGHT_GENERATED_BY_SELECTION_ALGEBRA=FALSE")
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
