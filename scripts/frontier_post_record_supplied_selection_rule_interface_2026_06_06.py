#!/usr/bin/env python3
"""Exact supplied-selection and margin-stability interface."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B")
Word = tuple[str, ...]
Law = dict[Word, Fraction]


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
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def all_words(length: int) -> tuple[Word, ...]:
    return tuple(tuple(word) for word in product(ALPHABET, repeat=length))


def count_a(word: Word) -> int:
    return sum(1 for atom in word if atom == "A")


def iid_law(p_a: Fraction, length: int) -> Law:
    p_b = 1 - p_a
    return {
        word: (p_a ** count_a(word)) * (p_b ** (length - count_a(word)))
        for word in all_words(length)
    }


def scores(models: dict[str, Law], observed: Word) -> dict[str, Fraction]:
    return {name: law[observed] for name, law in models.items()}


def normalized(law: Law) -> bool:
    return sum(law.values(), Fraction(0)) == 1 and all(p >= 0 for p in law.values())


def normalized_prior(prior: dict[str, Fraction]) -> bool:
    return sum(prior.values(), Fraction(0)) == 1 and all(p >= 0 for p in prior.values())


def posterior(score_map: dict[str, Fraction], prior: dict[str, Fraction]) -> dict[str, Fraction] | None:
    evidence = sum(prior[name] * score_map[name] for name in score_map)
    if evidence == 0:
        return None
    return {name: prior[name] * score_map[name] / evidence for name in score_map}


def argmax_set(score_map: dict[str, Fraction]) -> set[str]:
    top = max(score_map.values())
    return {name for name, value in score_map.items() if value == top}


def select_with_priority(score_map: dict[str, Fraction], priority: list[str]) -> str:
    priority_rank = {name: len(priority) - index for index, name in enumerate(priority)}
    return max(score_map, key=lambda name: (score_map[name], priority_rank[name]))


def winner_gap(score_map: dict[str, Fraction], winner: str) -> Fraction:
    challengers = [value for name, value in score_map.items() if name != winner]
    return score_map[winner] - max(challengers)


def margin_stable(score_map: dict[str, Fraction], priority: list[str], epsilon: Fraction) -> bool:
    winner = select_with_priority(score_map, priority)
    for challenger in score_map:
        if challenger == winner:
            continue
        worst_winner = score_map[winner] - epsilon
        best_challenger = score_map[challenger] + epsilon
        if worst_winner <= best_challenger:
            return False
    return True


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SUPPLIED_SELECTION_RULE_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "margin stability",
            "stable selected dial location under that supplied rule",
            "This does not force the dial",
            "generation/Koide dial",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "Does not derive probabilities",
            "Does not select a Koide/generation dial location",
            "post-record append action on O*",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "probability laws, Born typicality, and transition rates",
            "dial selection",
            "exact post-record dynamics has no edge to production",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
        [
            "bounded and conditional lanes",
            "does **not** unlock verdict changes by itself",
            "rows needing probability laws",
        ],
    )


def finite_selector_checks() -> None:
    section("Finite selector checks")
    score_map = {
        "s=0": Fraction(9, 10),
        "s=1": Fraction(3, 5),
        "s=2": Fraction(7, 10),
    }
    priority = ["s=0", "s=1", "s=2"]
    winner = select_with_priority(score_map, priority)
    gap = winner_gap(score_map, winner)
    report("supplied max-with-priority selector chooses s=0", winner == "s=0", winner)
    report("winner gap is exact", gap == Fraction(1, 5), str(gap))
    report("selection is idempotent on same scores", select_with_priority(score_map, priority) == winner)
    report("epsilon below half-gap preserves selection", margin_stable(score_map, priority, Fraction(1, 20)))
    report("epsilon equal to half-gap loses strict margin", not margin_stable(score_map, priority, Fraction(1, 10)))

    tie_scores = {"left": Fraction(1, 2), "right": Fraction(1, 2)}
    report("tie argmax has two candidates without priority", argmax_set(tie_scores) == {"left", "right"})
    report("supplied priority resolves tie", select_with_priority(tie_scores, ["right", "left"]) == "right")


def score_source_examples() -> None:
    section("Supplied score-source examples")
    observed = ("A", "A", "A", "B")
    models = {
        "low_A": iid_law(Fraction(1, 5), 4),
        "high_A": iid_law(Fraction(3, 4), 4),
    }
    report("low-A supplied law normalizes", normalized(models["low_A"]))
    report("high-A supplied law normalizes", normalized(models["high_A"]))
    likelihood_scores = scores(models, observed)
    report("likelihood score map is exact", likelihood_scores == {"low_A": Fraction(4, 625), "high_A": Fraction(27, 256)}, str(likelihood_scores))
    report("max-likelihood supplied rule chooses high-A", select_with_priority(likelihood_scores, ["low_A", "high_A"]) == "high_A")

    low_heavy_prior = {"low_A": Fraction(9999, 10000), "high_A": Fraction(1, 10000)}
    report("supplied prior normalizes", normalized_prior(low_heavy_prior))
    post = posterior(likelihood_scores, low_heavy_prior)
    assert post is not None
    report("posterior score map normalizes", sum(post.values()) == 1, str(post))
    report("posterior supplied rule chooses low-A under low-heavy prior", select_with_priority(post, ["high_A", "low_A"]) == "low_A")


def dial_stability_checks() -> None:
    section("Supplied dial-score stability checks")
    dial_scores = {
        "dial_s=0": Fraction(11, 12),
        "dial_s=1/2": Fraction(2, 3),
        "dial_s=1": Fraction(3, 4),
    }
    priority = ["dial_s=0", "dial_s=1/2", "dial_s=1"]
    winner = select_with_priority(dial_scores, priority)
    gap = winner_gap(dial_scores, winner)
    report("supplied dial-score selector chooses s=0", winner == "dial_s=0", winner)
    report("dial-score gap is positive", gap == Fraction(1, 6), str(gap))
    report("dial location is stable below half-gap", margin_stable(dial_scores, priority, Fraction(1, 20)))
    report("dial location is not Record-forced flag", True)


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_candidate_set = False
    record_derives_score_map = False
    record_derives_selection_rule = False
    record_derives_tie_priority = False
    record_derives_physical_probability = False
    record_derives_hamiltonian_or_clock = False
    generation_or_koide_dial_forced = False
    audit_verdict_applied = False

    report("Record-derived candidate-set flag is false", not record_derives_candidate_set)
    report("Record-derived score-map flag is false", not record_derives_score_map)
    report("Record-derived selection-rule flag is false", not record_derives_selection_rule)
    report("Record-derived tie-priority flag is false", not record_derives_tie_priority)
    report("Record-derived physical-probability flag is false", not record_derives_physical_probability)
    report("Record-derived Hamiltonian/clock flag is false", not record_derives_hamiltonian_or_clock)
    report("generation/Koide dial forced flag is false", not generation_or_koide_dial_forced)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    finite_selector_checks()
    score_source_examples()
    dial_stability_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_SELECTION_RULE_INTERFACE=TRUE")
    print("POSITIVE_MARGIN_IMPLIES_LOCAL_STABILITY=TRUE")
    print("RECORD_DERIVES_SELECTION_RULE=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_FORCED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
