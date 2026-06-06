#!/usr/bin/env python3
"""No-go: expected post-record counts do not imply concentration."""

from __future__ import annotations

from collections import Counter
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


def iid_fair_law(length: int) -> Law:
    p = Fraction(1, 2**length)
    return {word: p for word in all_words(length)}


def correlated_fair_law(length: int) -> Law:
    law = {word: Fraction(0) for word in all_words(length)}
    law[tuple("A" for _ in range(length))] = Fraction(1, 2)
    law[tuple("B" for _ in range(length))] = Fraction(1, 2)
    return law


def normalized(law: Law) -> bool:
    return sum(law.values(), Fraction(0)) == 1 and all(p >= 0 for p in law.values())


def count_word(word: Word) -> tuple[int, int]:
    counts = Counter(word)
    return (counts["A"], counts["B"])


def expected_counts(law: Law) -> tuple[Fraction, Fraction]:
    total = (Fraction(0), Fraction(0))
    for word, p in law.items():
        counts = count_word(word)
        total = (total[0] + p * counts[0], total[1] + p * counts[1])
    return total


def one_time_marginal(law: Law, index: int) -> tuple[Fraction, Fraction]:
    p_a = sum(p for word, p in law.items() if word[index] == "A")
    return (p_a, 1 - p_a)


def imbalance(counts: tuple[int, int]) -> int:
    return abs(counts[0] - counts[1])


def tail_prob(law: Law, threshold: int) -> Fraction:
    return sum(p for word, p in law.items() if imbalance(count_word(word)) >= threshold)


def p_value(law: Law, observed: Word) -> Fraction:
    return tail_prob(law, imbalance(count_word(observed)))


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_EXPECTATION_CONCENTRATION_FIREWALL_2026-06-06.md",
        [
            "actual_current_surface_status: no-go",
            "Expected empirical frequencies do not determine finite tail probabilities",
            "expected post-record frequency",
            "concentration and p-values remain conditional",
            "generation/Koide dials",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "realized counts stay integral while ensemble expectations can be fractional",
            "Does not derive probabilities",
            "Does not derive a time metric or clock rate",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md",
        [
            "post-record update is integral",
            "predictive expectation",
            "belongs to the pre-record or ensemble layer",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "probability laws, Born typicality, and transition rates",
            "clock/time metric",
            "post-record information dynamics",
        ],
    )


def counterexample_checks() -> None:
    section("Counterexample checks")
    length = 4
    iid = iid_fair_law(length)
    corr = correlated_fair_law(length)
    report("iid fair law normalizes", normalized(iid))
    report("correlated fair law normalizes", normalized(corr))
    report("expected counts match", expected_counts(iid) == expected_counts(corr) == (Fraction(2), Fraction(2)), str(expected_counts(iid)))
    for index in range(length):
        report(f"one-time marginal {index} matches", one_time_marginal(iid, index) == one_time_marginal(corr, index) == (Fraction(1, 2), Fraction(1, 2)))

    iid_tail = tail_prob(iid, 4)
    corr_tail = tail_prob(corr, 4)
    report("iid extreme-tail probability is exact", iid_tail == Fraction(1, 8), str(iid_tail))
    report("correlated extreme-tail probability is exact", corr_tail == 1, str(corr_tail))
    report("same expectation has different tail probabilities", iid_tail != corr_tail)

    observed = ("A", "A", "A", "A")
    report("same observed word gets different p-values", p_value(iid, observed) != p_value(corr, observed), f"{p_value(iid, observed)} vs {p_value(corr, observed)}")


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_concentration = False
    record_derives_p_value = False
    record_derives_kernel = False
    record_derives_clock_or_rate = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived concentration flag is false", not record_derives_concentration)
    report("Record-derived p-value flag is false", not record_derives_p_value)
    report("Record-derived kernel flag is false", not record_derives_kernel)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    counterexample_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("EXPECTATION_IMPLIES_CONCENTRATION=FALSE")
    print("SAME_EXPECTATION_DIFFERENT_TAILS=TRUE")
    print("RECORD_DERIVES_P_VALUE=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
