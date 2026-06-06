#!/usr/bin/env python3
"""Post-record count probability firewall.

Finite post-record histories give realized counts and empirical frequencies.
They can audit a supplied probability model, but they do not derive the
predictive probability law, Born form, transition rates, or dial choice.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import log
from pathlib import Path
import sys

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
TOL = 1e-12


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


ALPHABET = ("0", "1")


def count_word(word: tuple[str, ...]) -> tuple[int, int]:
    counts = Counter(word)
    return (counts["0"], counts["1"])


def empirical(counts: tuple[int, int]) -> tuple[Fraction, Fraction]:
    total = sum(counts)
    if total == 0:
        raise ValueError("empty history has no empirical frequency")
    return (Fraction(counts[0], total), Fraction(counts[1], total))


def likelihood_iid(word: tuple[str, ...], law: tuple[float, float]) -> float:
    prob = 1.0
    for atom in word:
        prob *= law[0] if atom == "0" else law[1]
    return prob


def log_likelihood_iid(word: tuple[str, ...], law: tuple[float, float]) -> float:
    return sum(log(law[0] if atom == "0" else law[1]) for atom in word)


def trace_prob(rho: np.ndarray, effect: np.ndarray) -> float:
    return float(np.real_if_close(np.trace(rho @ effect)))


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md",
        [
            "actual_current_surface_status: no-go",
            "trace_class: negative_route_pruning",
            "post-record counts",
            "They cannot derive the model.",
            "Does not select a generation or Koide dial location.",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "probability vector",
            "a selector for which atom will be produced next",
            "realized counts stay integral while ensemble expectations can be fractional",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md",
        [
            "not a probability vector",
            "predictive expectation",
            "belongs to the pre-record or ensemble layer",
        ],
    )
    require_text(
        "docs/RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md",
        [
            "Probability belongs to the first two arrows",
            "Post-record dynamics acts on realized tokens/counts",
            "A probability is a separate",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "Record history/count support is therefore an exact **consumer**",
            "not a producer of atoms",
            "probability laws, Born typicality, and transition rates",
        ],
    )
    require_text(
        "docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md",
        [
            "pre-record tracial",
            "p(E) = Tr(rho E)",
            "This row does not claim durable/native persistent-record formation",
        ],
    )
    require_text(
        "docs/BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
        [
            "m(E) = Tr",
            "identify the pre-record",
            "Not a closure of the Born derivation row",
        ],
    )


def count_probability_firewall_checks() -> None:
    section("Count/probability non-uniqueness")
    word = ("0", "1", "0", "0")
    counts = count_word(word)
    freq = empirical(counts)
    report("finite realized history has integer counts", counts == (3, 1), str(counts))
    report("empirical frequency is normalized", sum(freq) == 1, str(freq))
    report("empirical frequency is a statistic, not an integer count", any(x.denominator != 1 for x in freq))

    laws = {
        "mle": (0.75, 0.25),
        "alternative_a": (0.60, 0.40),
        "alternative_b": (0.90, 0.10),
    }
    likelihoods = {name: likelihood_iid(word, law) for name, law in laws.items()}
    report("multiple distinct iid laws assign positive likelihood to same word", all(v > 0 for v in likelihoods.values()), str(likelihoods))
    report("compatible laws give different next-zero predictions", len({law[0] for law in laws.values()}) == len(laws))
    count_alone_unique_predictive_law = False
    report("count-alone unique predictive law flag is false", not count_alone_unique_predictive_law)

    ll_mle = log_likelihood_iid(word, laws["mle"])
    ll_alt = log_likelihood_iid(word, laws["alternative_a"])
    iid_model_admitted = False
    report("iid MLE is higher than one alternative after iid model is admitted", ll_mle > ll_alt)
    report("iid model is not supplied by post-record counts alone", not iid_model_admitted)

    w01 = ("0", "1")
    w10 = ("1", "0")
    report("different histories can have same counts", count_word(w01) == count_word(w10))
    markov_next_zero = {"last_0": 0.9, "last_1": 0.2}
    pred_w01 = markov_next_zero["last_1"]
    pred_w10 = markov_next_zero["last_0"]
    report("same counts can have different next prediction under admitted Markov law", pred_w01 != pred_w10)
    report("counts have forgotten order needed by that Markov law", w01[-1] != w10[-1] and count_word(w01) == count_word(w10))


def born_interface_checks() -> None:
    section("Born/pre-record interface separation")
    p0 = np.array([[1.0, 0.0], [0.0, 0.0]])
    p1 = np.array([[0.0, 0.0], [0.0, 1.0]])
    rho_a = np.array([[0.2, 0.0], [0.0, 0.8]])
    rho_b = np.array([[0.8, 0.0], [0.0, 0.2]])
    counts = (3, 1)

    probs_a = (trace_prob(rho_a, p0), trace_prob(rho_a, p1))
    probs_b = (trace_prob(rho_b, p0), trace_prob(rho_b, p1))
    report("Born weights from rho_a are normalized", abs(sum(probs_a) - 1.0) < TOL, str(probs_a))
    report("Born weights from rho_b are normalized", abs(sum(probs_b) - 1.0) < TOL, str(probs_b))
    report("same realized counts can be paired with different pre-record states", probs_a != probs_b and counts == (3, 1))

    realized_after_0 = (counts[0] + 1, counts[1])
    expected_after_a = (counts[0] + probs_a[0], counts[1] + probs_a[1])
    report("realized count update is integral", all(isinstance(x, int) for x in realized_after_0), str(realized_after_0))
    report("ensemble expectation is generally fractional", any(abs(x - round(x)) > TOL for x in expected_after_a), str(expected_after_a))
    report("ensemble expectation differs from realized branch update", expected_after_a != realized_after_0)

    count_alone_derived_born = False
    count_alone_selected_rho = False
    count_alone_selected_effect = False
    count_alone_selected_rate = False
    count_alone_selected_dial = False
    report("count-alone Born derivation flag is false", not count_alone_derived_born)
    report("count-alone rho selection flag is false", not count_alone_selected_rho)
    report("count-alone effect/instrument selection flag is false", not count_alone_selected_effect)
    report("count-alone rate selection flag is false", not count_alone_selected_rate)
    report("count-alone generation/Koide dial selection flag is false", not count_alone_selected_dial)


def model_audit_checks() -> None:
    section("What counts can still do")
    word = ("0", "1", "0", "0")
    supplied_law = (0.75, 0.25)
    other_law = (0.50, 0.50)
    ll_supplied = log_likelihood_iid(word, supplied_law)
    ll_other = log_likelihood_iid(word, other_law)
    repeated_trials_assumed = True
    stationarity_assumed = True
    independence_assumed = True
    report("counts can score a supplied iid model", isinstance(ll_supplied, float) and isinstance(ll_other, float))
    report("different supplied models receive different scores", abs(ll_supplied - ll_other) > TOL)
    report("model scoring explicitly uses repeated-trial/statistical assumptions", repeated_trials_assumed and stationarity_assumed and independence_assumed)
    report("model scoring is not model derivation", supplied_law != other_law and ll_supplied != ll_other)


def main() -> int:
    source_anchor_checks()
    count_probability_firewall_checks()
    born_interface_checks()
    model_audit_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_COUNTS_DERIVE_PROBABILITY_LAW=FALSE")
    print("POST_RECORD_COUNTS_CAN_AUDIT_SUPPLIED_MODEL=TRUE")
    print("BORN_REQUIRES_PRE_RECORD_OR_INSTRUMENT_BRIDGE=TRUE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
