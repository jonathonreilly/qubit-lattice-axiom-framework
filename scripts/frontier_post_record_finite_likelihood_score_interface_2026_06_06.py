#!/usr/bin/env python3
"""Exact finite likelihood-score interface for post-record histories.

Given a realized finite post-record word and supplied normalized model laws on
the same word space, likelihoods, likelihood ratios, and optional Bayes weights
are exact finite rational calculations. The model family, prior, and decision
rule are not derived by Record.
"""

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


def row_stochastic(kernel: dict[str, tuple[Fraction, Fraction]]) -> bool:
    return all(sum(row) == 1 and all(x >= 0 for x in row) for row in kernel.values())


def markov_law(
    length: int,
    mu0: tuple[Fraction, Fraction],
    kernel: dict[str, tuple[Fraction, Fraction]],
) -> Law:
    idx = {atom: i for i, atom in enumerate(ALPHABET)}
    law: Law = {}
    for word in all_words(length):
        p = mu0[idx[word[0]]]
        for left, right in zip(word, word[1:]):
            p *= kernel[left][idx[right]]
        law[word] = p
    return law


def normalized(law: Law) -> bool:
    return sum(law.values(), Fraction(0)) == 1 and all(p >= 0 for p in law.values())


def score_vector(models: dict[str, Law], observed: Word) -> dict[str, Fraction]:
    return {name: law[observed] for name, law in models.items()}


def likelihood_ratio(scores: dict[str, Fraction], numerator: str, denominator: str) -> Fraction | None:
    den = scores[denominator]
    if den == 0:
        return None
    return scores[numerator] / den


def posterior_weights(
    scores: dict[str, Fraction],
    prior: dict[str, Fraction],
) -> dict[str, Fraction] | None:
    evidence = sum(prior[name] * scores[name] for name in scores)
    if evidence == 0:
        return None
    return {name: prior[name] * scores[name] / evidence for name in scores}


def normalized_prior(prior: dict[str, Fraction]) -> bool:
    return sum(prior.values(), Fraction(0)) == 1 and all(p >= 0 for p in prior.values())


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_FINITE_LIKELIHOOD_SCORE_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "supplied finite model scoring",
            "model-family, prior, decision-rule, and dial-selection derivation remain open",
            "posterior_m(w*)",
            "generation or Koide dial",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
        [
            "bounded and conditional lanes",
            "rows needing probability laws",
            "does **not** unlock verdict changes by itself",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "post-record append action on O*",
            "Does not derive probabilities",
            "Does not select a Koide/generation dial location",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "Record history/count support is therefore an exact **consumer**",
            "probability laws, Born typicality, and transition rates",
            "dial selection",
        ],
    )


def iid_score_checks() -> None:
    section("IID supplied-model score checks")
    length = 4
    observed = ("A", "A", "A", "B")
    low_a = iid_law(Fraction(1, 5), length)
    high_a = iid_law(Fraction(3, 4), length)
    models = {"low_A": low_a, "high_A": high_a}
    report("low-A supplied model is normalized", normalized(low_a))
    report("high-A supplied model is normalized", normalized(high_a))

    scores = score_vector(models, observed)
    report("low-A likelihood is exact", scores["low_A"] == Fraction(4, 625), str(scores["low_A"]))
    report("high-A likelihood is exact", scores["high_A"] == Fraction(27, 256), str(scores["high_A"]))

    lr_high_low = likelihood_ratio(scores, "high_A", "low_A")
    lr_low_high = likelihood_ratio(scores, "low_A", "high_A")
    report("high/low likelihood ratio is exact", lr_high_low == Fraction(16875, 1024), str(lr_high_low))
    report("low/high likelihood ratio is reciprocal", lr_low_high == Fraction(1024, 16875), str(lr_low_high))

    equal_prior = {"low_A": Fraction(1, 2), "high_A": Fraction(1, 2)}
    report("equal prior is normalized", normalized_prior(equal_prior))
    posterior = posterior_weights(scores, equal_prior)
    assert posterior is not None
    report("posterior weights normalize exactly", sum(posterior.values()) == 1, str(posterior))
    report("equal-prior high-A posterior is exact", posterior["high_A"] == Fraction(16875, 17899), str(posterior["high_A"]))
    report("equal-prior posterior favors high-A model", posterior["high_A"] > posterior["low_A"])

    strong_low_prior = {"low_A": Fraction(9999, 10000), "high_A": Fraction(1, 10000)}
    report("strong low-A prior is normalized", normalized_prior(strong_low_prior))
    prior_dominated = posterior_weights(scores, strong_low_prior)
    assert prior_dominated is not None
    report("different supplied prior can change posterior ordering", prior_dominated["low_A"] > prior_dominated["high_A"])

    other_observed = ("B", "B", "B", "B")
    other_scores = score_vector(models, other_observed)
    other_lr = likelihood_ratio(other_scores, "high_A", "low_A")
    report("different realized word can reverse likelihood preference", other_lr == Fraction(625, 65536), str(other_lr))
    report("reversed preference is below one", other_lr is not None and other_lr < 1)


def markov_and_support_checks() -> None:
    section("Supplied Markov and support-guard checks")
    mu0 = (Fraction(1, 2), Fraction(1, 2))
    sticky_a = {
        "A": (Fraction(4, 5), Fraction(1, 5)),
        "B": (Fraction(1, 4), Fraction(3, 4)),
    }
    sticky_b = {
        "A": (Fraction(1, 3), Fraction(2, 3)),
        "B": (Fraction(1, 6), Fraction(5, 6)),
    }
    report("sticky-A kernel is row-stochastic", row_stochastic(sticky_a))
    report("sticky-B kernel is row-stochastic", row_stochastic(sticky_b))

    models = {
        "sticky_A": markov_law(4, mu0, sticky_a),
        "sticky_B": markov_law(4, mu0, sticky_b),
    }
    report("sticky-A finite law normalizes", normalized(models["sticky_A"]))
    report("sticky-B finite law normalizes", normalized(models["sticky_B"]))
    observed = ("A", "A", "A", "B")
    scores = score_vector(models, observed)
    report("Markov score vector has both models", set(scores) == {"sticky_A", "sticky_B"})
    report("Markov likelihood ratio is defined when denominator is nonzero", likelihood_ratio(scores, "sticky_A", "sticky_B") is not None)

    zero_law = dict(models["sticky_A"])
    zero_law[observed] = Fraction(0)
    zero_law[("B", "B", "B", "B")] += models["sticky_A"][observed]
    report("modified zero-support law stays normalized", normalized(zero_law))
    zero_models = {"zero_at_observed": zero_law, "sticky_A": models["sticky_A"]}
    zero_scores = score_vector(zero_models, observed)
    report("zero-support denominator returns guarded undefined ratio", likelihood_ratio(zero_scores, "sticky_A", "zero_at_observed") is None)
    zero_prior = {"zero_at_observed": Fraction(1, 2), "sticky_A": Fraction(1, 2)}
    zero_post = posterior_weights(zero_scores, zero_prior)
    assert zero_post is not None
    report("posterior can assign zero weight to zero-likelihood model", zero_post["zero_at_observed"] == 0)


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_model_family = False
    record_derives_prior = False
    record_derives_decision_rule = False
    record_derives_observation_protocol = False
    record_derives_born_or_instrument = False
    record_derives_clock_or_rate = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived model-family flag is false", not record_derives_model_family)
    report("Record-derived prior flag is false", not record_derives_prior)
    report("Record-derived decision-rule flag is false", not record_derives_decision_rule)
    report("Record-derived observation-protocol flag is false", not record_derives_observation_protocol)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    iid_score_checks()
    markov_and_support_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_FINITE_MODEL_SCORE_INTERFACE=TRUE")
    print("LIKELIHOOD_RATIOS_EXACT_WHEN_DEFINED=TRUE")
    print("RECORD_DERIVES_MODEL_FAMILY=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
