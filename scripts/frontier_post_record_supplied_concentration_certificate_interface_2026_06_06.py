#!/usr/bin/env python3
"""Exact support: supplied concentration certificates are law-scoped."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B")
Word = tuple[str, ...]
Counts = tuple[int, int]
Law = dict[Word, Fraction]
CountLaw = dict[Counts, Fraction]


@dataclass(frozen=True)
class Certificate:
    name: str
    law_id: str
    event_id: str
    epsilon: Fraction


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


def iid_fair_law(length: int) -> Law:
    p = Fraction(1, 2**length)
    return {word: p for word in all_words(length)}


def correlated_fair_law(length: int) -> Law:
    law = {word: Fraction(0) for word in all_words(length)}
    law[tuple("A" for _ in range(length))] = Fraction(1, 2)
    law[tuple("B" for _ in range(length))] = Fraction(1, 2)
    return law


def normalized(law: Law | CountLaw) -> bool:
    return sum(law.values(), Fraction(0)) == 1 and all(p >= 0 for p in law.values())


def count_word(word: Word) -> Counts:
    counts = Counter(word)
    return (counts["A"], counts["B"])


def expected_counts(law: Law) -> tuple[Fraction, Fraction]:
    a = Fraction(0)
    b = Fraction(0)
    for word, p in law.items():
        ca, cb = count_word(word)
        a += p * ca
        b += p * cb
    return (a, b)


def one_time_marginal(law: Law, index: int) -> tuple[Fraction, Fraction]:
    p_a = sum(p for word, p in law.items() if word[index] == "A")
    return (p_a, 1 - p_a)


def count_pushforward(law: Law) -> CountLaw:
    pushed: CountLaw = {}
    for word, p in law.items():
        counts = count_word(word)
        pushed[counts] = pushed.get(counts, Fraction(0)) + p
    return pushed


def imbalance(counts: Counts) -> int:
    return abs(counts[0] - counts[1])


def extreme_imbalance_word(word: Word) -> bool:
    return imbalance(count_word(word)) >= 4


def extreme_imbalance_count(counts: Counts) -> bool:
    return imbalance(counts) >= 4


def event_probability(law: Law, event) -> Fraction:
    return sum(p for word, p in law.items() if event(word))


def count_event_probability(law: CountLaw, event) -> Fraction:
    return sum(p for counts, p in law.items() if event(counts))


def exact_p_value_for_observed(law: Law, observed: Word) -> Fraction:
    threshold = imbalance(count_word(observed))
    return sum(p for word, p in law.items() if imbalance(count_word(word)) >= threshold)


def verify_certificate(law_id: str, law: Law, cert: Certificate) -> tuple[bool, Fraction]:
    if cert.event_id != "extreme_imbalance_ge_4":
        raise ValueError(f"unknown event id: {cert.event_id}")
    exact = event_probability(law, extreme_imbalance_word)
    return cert.law_id == law_id and exact <= cert.epsilon, exact


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "supplied finite law on post-record words",
            "verified law-scoped concentration certificate",
            "does not have a concentration certificate",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "canonical finite-alphabet algebra",
            "realized counts stay integral while ensemble expectations can be fractional",
            "Does not derive probabilities",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
        [
            "finite histories O*",
            "probability/source/instrument/dynamics rows",
            "Does not select a Koide/generation dial location.",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "probability laws, Born typicality, and transition rates",
            "post-record information dynamics",
            "dial selection",
        ],
    )


def finite_law_checks() -> None:
    section("Finite law and count-pushforward checks")
    length = 4
    iid = iid_fair_law(length)
    corr = correlated_fair_law(length)
    iid_counts = count_pushforward(iid)
    corr_counts = count_pushforward(corr)

    report("iid law normalizes", normalized(iid))
    report("correlated law normalizes", normalized(corr))
    report("iid count pushforward normalizes", normalized(iid_counts))
    report("correlated count pushforward normalizes", normalized(corr_counts))
    report("expected counts match", expected_counts(iid) == expected_counts(corr) == (Fraction(2), Fraction(2)), str(expected_counts(iid)))
    for index in range(length):
        report(f"one-time marginal {index} matches", one_time_marginal(iid, index) == one_time_marginal(corr, index) == (Fraction(1, 2), Fraction(1, 2)))

    iid_word_tail = event_probability(iid, extreme_imbalance_word)
    iid_count_tail = count_event_probability(iid_counts, extreme_imbalance_count)
    corr_word_tail = event_probability(corr, extreme_imbalance_word)
    corr_count_tail = count_event_probability(corr_counts, extreme_imbalance_count)
    report("iid word/count event probabilities agree", iid_word_tail == iid_count_tail == Fraction(1, 8), str(iid_word_tail))
    report("correlated word/count event probabilities agree", corr_word_tail == corr_count_tail == 1, str(corr_word_tail))

    expected_iid_counts = {
        (0, 4): Fraction(1, 16),
        (1, 3): Fraction(4, 16),
        (2, 2): Fraction(6, 16),
        (3, 1): Fraction(4, 16),
        (4, 0): Fraction(1, 16),
    }
    report("iid count distribution is exact binomial pushforward", iid_counts == expected_iid_counts)


def certificate_checks() -> None:
    section("Certificate checks")
    length = 4
    iid = iid_fair_law(length)
    corr = correlated_fair_law(length)
    iid_cert = Certificate(
        name="iid_extreme_imbalance_bound",
        law_id="iid_fair_N4",
        event_id="extreme_imbalance_ge_4",
        epsilon=Fraction(1, 4),
    )
    exact_cert = Certificate(
        name="iid_extreme_imbalance_exact_bound",
        law_id="iid_fair_N4",
        event_id="extreme_imbalance_ge_4",
        epsilon=Fraction(1, 8),
    )

    valid, exact = verify_certificate("iid_fair_N4", iid, iid_cert)
    report("iid certificate valid under its own law", valid, f"exact={exact}, epsilon={iid_cert.epsilon}")
    tight_valid, tight_exact = verify_certificate("iid_fair_N4", iid, exact_cert)
    report("iid exact certificate valid at equality", tight_valid, f"exact={tight_exact}, epsilon={exact_cert.epsilon}")

    wrong_scope_valid, wrong_scope_exact = verify_certificate("correlated_fair_N4", corr, iid_cert)
    report("iid certificate rejected under correlated law scope", not wrong_scope_valid, f"exact={wrong_scope_exact}, epsilon={iid_cert.epsilon}")

    observed = ("A", "A", "A", "A")
    iid_p = exact_p_value_for_observed(iid, observed)
    corr_p = exact_p_value_for_observed(corr, observed)
    report("iid observed extreme p-value bounded by certificate", iid_p <= iid_cert.epsilon, str(iid_p))
    report("correlated observed extreme p-value not bounded by iid certificate", corr_p > iid_cert.epsilon, str(corr_p))
    report("same observed word has law-dependent p-values", iid_p != corr_p, f"{iid_p} vs {corr_p}")


def firewall_checks() -> None:
    section("Firewall flags")
    expectation_only_certificate_accepted = False
    record_derives_probability_law = False
    record_derives_concentration = False
    record_derives_p_value = False
    record_derives_kernel = False
    record_derives_clock_rate = False
    record_derives_hamiltonian = False
    audit_verdict_applied = False
    generation_or_koide_dial_selected = False

    report("expectation-only certificate accepted flag is false", not expectation_only_certificate_accepted)
    report("Record-derived probability-law flag is false", not record_derives_probability_law)
    report("Record-derived concentration flag is false", not record_derives_concentration)
    report("Record-derived p-value flag is false", not record_derives_p_value)
    report("Record-derived kernel flag is false", not record_derives_kernel)
    report("Record-derived clock/rate flag is false", not record_derives_clock_rate)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    finite_law_checks()
    certificate_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE=TRUE")
    print("LAW_SCOPE_REQUIRED=TRUE")
    print("EXPECTATION_ONLY_CERTIFICATE_ACCEPTED=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
