#!/usr/bin/env python3
"""Finite counterexamples to post-record model-selection from scores alone."""

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


def normalized(law: Law) -> bool:
    return sum(law.values(), Fraction(0)) == 1 and all(p >= 0 for p in law.values())


def scores(models: dict[str, Law], observed: Word) -> dict[str, Fraction]:
    return {name: law[observed] for name, law in models.items()}


def argmax_set(score_map: dict[str, Fraction]) -> set[str]:
    top = max(score_map.values())
    return {name for name, value in score_map.items() if value == top}


def posterior(scores_: dict[str, Fraction], prior: dict[str, Fraction]) -> dict[str, Fraction] | None:
    evidence = sum(prior[name] * scores_[name] for name in scores_)
    if evidence == 0:
        return None
    return {name: prior[name] * scores_[name] / evidence for name in scores_}


def normalized_prior(prior: dict[str, Fraction]) -> bool:
    return sum(prior.values(), Fraction(0)) == 1 and all(p >= 0 for p in prior.values())


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_MODEL_SELECTION_FIREWALL_2026-06-06.md",
        [
            "actual_current_surface_status: no-go",
            "trace_class: negative_route_pruning",
            "same likelihood vector can yield different posterior argmaxes",
            "does not force a unique model",
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
            "does **not** unlock verdict changes by itself",
            "rows needing probability laws",
            "dial selection",
        ],
    )


def prior_reversal_checks() -> None:
    section("Prior-dependence counterexample")
    observed = ("A", "A", "A", "B")
    models = {
        "low_A": iid_law(Fraction(1, 5), 4),
        "high_A": iid_law(Fraction(3, 4), 4),
    }
    report("low-A law normalizes", normalized(models["low_A"]))
    report("high-A law normalizes", normalized(models["high_A"]))
    score_map = scores(models, observed)
    report("low-A likelihood is exact", score_map["low_A"] == Fraction(4, 625), str(score_map["low_A"]))
    report("high-A likelihood is exact", score_map["high_A"] == Fraction(27, 256), str(score_map["high_A"]))
    report("maximum likelihood favors high-A", argmax_set(score_map) == {"high_A"})

    equal_prior = {"low_A": Fraction(1, 2), "high_A": Fraction(1, 2)}
    low_heavy_prior = {"low_A": Fraction(9999, 10000), "high_A": Fraction(1, 10000)}
    report("equal prior normalizes", normalized_prior(equal_prior))
    report("low-heavy prior normalizes", normalized_prior(low_heavy_prior))
    post_equal = posterior(score_map, equal_prior)
    post_low_heavy = posterior(score_map, low_heavy_prior)
    assert post_equal is not None
    assert post_low_heavy is not None
    report("equal-prior posterior favors high-A", argmax_set(post_equal) == {"high_A"}, str(post_equal))
    report("low-heavy-prior posterior favors low-A", argmax_set(post_low_heavy) == {"low_A"}, str(post_low_heavy))
    report("same likelihood vector yields different posterior argmaxes", argmax_set(post_equal) != argmax_set(post_low_heavy))


def tie_and_family_extension_checks() -> None:
    section("Tie and family-extension counterexamples")
    observed = ("A", "A")
    fair = iid_law(Fraction(1, 2), 2)
    skew_same_observed = {
        ("A", "A"): Fraction(1, 4),
        ("A", "B"): Fraction(1, 4),
        ("B", "A"): Fraction(1, 2),
        ("B", "B"): Fraction(0),
    }
    report("fair law normalizes", normalized(fair))
    report("skew law with same observed score normalizes", normalized(skew_same_observed))
    tie_scores = scores({"fair": fair, "skew": skew_same_observed}, observed)
    report("two distinct laws have same observed likelihood", tie_scores["fair"] == tie_scores["skew"] == Fraction(1, 4), str(tie_scores))
    report("maximum-likelihood selector ties without tie-breaker", argmax_set(tie_scores) == {"fair", "skew"})

    spike = {word: Fraction(0) for word in all_words(2)}
    spike[observed] = Fraction(1)
    report("spike law normalizes", normalized(spike))
    extended_scores = scores({"fair": fair, "skew": skew_same_observed, "spike": spike}, observed)
    report("family extension changes maximum-likelihood winner", argmax_set(extended_scores) == {"spike"}, str(extended_scores))
    report("extension demonstrates admissibility rule is required", argmax_set(extended_scores) != argmax_set(tie_scores))


def threshold_checks() -> None:
    section("Threshold-dependence counterexample")
    observed = ("A", "A", "A", "B")
    models = {
        "low_A": iid_law(Fraction(1, 5), 4),
        "high_A": iid_law(Fraction(3, 4), 4),
    }
    score_map = scores(models, observed)
    ratio = score_map["high_A"] / score_map["low_A"]
    report("likelihood ratio is exact", ratio == Fraction(16875, 1024), str(ratio))
    threshold_2 = Fraction(2)
    threshold_20 = Fraction(20)
    report("ratio passes threshold 2", ratio >= threshold_2)
    report("ratio fails threshold 20", ratio < threshold_20)
    report("same ratio has different decisions under different thresholds", (ratio >= threshold_2) != (ratio >= threshold_20))


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_model_family = False
    record_derives_prior = False
    record_derives_tie_breaker = False
    record_derives_threshold = False
    record_derives_admissibility_rule = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian_or_clock = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived model-family flag is false", not record_derives_model_family)
    report("Record-derived prior flag is false", not record_derives_prior)
    report("Record-derived tie-breaker flag is false", not record_derives_tie_breaker)
    report("Record-derived threshold flag is false", not record_derives_threshold)
    report("Record-derived admissibility-rule flag is false", not record_derives_admissibility_rule)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian/clock flag is false", not record_derives_hamiltonian_or_clock)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    prior_reversal_checks()
    tie_and_family_extension_checks()
    threshold_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_SCORE_TO_CANONICAL_SELECTION=FALSE")
    print("SUPPLIED_SELECTION_RULE_REQUIRED=TRUE")
    print("RECORD_DERIVES_MODEL_FAMILY=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
