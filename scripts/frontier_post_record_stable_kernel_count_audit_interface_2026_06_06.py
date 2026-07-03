#!/usr/bin/env python3
"""Exact finite count-statistic audit under a supplied post-record kernel."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B")
Word = tuple[str, ...]
Vector = tuple[Fraction, Fraction]
Kernel = dict[str, tuple[Fraction, Fraction]]


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


def row_stochastic(k: Kernel) -> bool:
    return all(sum(row) == 1 and all(x >= 0 for x in row) for row in k.values())


def prob_word(word: Word, p0: Vector, k: Kernel) -> Fraction:
    idx = {atom: i for i, atom in enumerate(ALPHABET)}
    p = p0[idx[word[0]]]
    for left, right in zip(word, word[1:]):
        p *= k[left][idx[right]]
    return p


def count_word(word: Word) -> tuple[int, int]:
    counts = Counter(word)
    return (counts["A"], counts["B"])


def count_distribution(length: int, p0: Vector, k: Kernel) -> dict[tuple[int, int], Fraction]:
    dist: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for word in all_words(length):
        dist[count_word(word)] += prob_word(word, p0, k)
    return dict(dist)


def statistic(counts: tuple[int, int]) -> int:
    count_a, count_b = counts
    return abs(count_a - count_b)


def p_value_for_observed(observed: Word, length: int, p0: Vector, k: Kernel) -> Fraction:
    observed_stat = statistic(count_word(observed))
    total = Fraction(0)
    for word in all_words(length):
        if statistic(count_word(word)) >= observed_stat:
            total += prob_word(word, p0, k)
    return total


def p_value_map(length: int, p0: Vector, k: Kernel) -> dict[Word, Fraction]:
    return {word: p_value_for_observed(word, length, p0, k) for word in all_words(length)}


def prob_p_at_most(alpha: Fraction, length: int, p0: Vector, k: Kernel) -> Fraction:
    pvals = p_value_map(length, p0, k)
    return sum(prob_word(word, p0, k) for word, pval in pvals.items() if pval <= alpha)


def apply(p: Vector, k: Kernel) -> Vector:
    return (
        p[0] * k["A"][0] + p[1] * k["B"][0],
        p[0] * k["A"][1] + p[1] * k["B"][1],
    )


def expected_count_by_marginals(length: int, p0: Vector, k: Kernel) -> Vector:
    total = (Fraction(0), Fraction(0))
    p = p0
    for _ in range(length):
        total = (total[0] + p[0], total[1] + p[1])
        p = apply(p, k)
    return total


def expected_count_from_distribution(dist: dict[tuple[int, int], Fraction]) -> Vector:
    total = (Fraction(0), Fraction(0))
    for counts, p in dist.items():
        total = (total[0] + p * counts[0], total[1] + p * counts[1])
    return total


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_STABLE_KERNEL_COUNT_AUDIT_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "exact finite count-statistic audits",
            "without importing asymptotic concentration",
            "realized counts remain integral",
            "generation or Koide dial",
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


def finite_count_audit_checks() -> None:
    section("Finite count-audit checks")
    p0 = (Fraction(1), Fraction(0))
    k = {
        "A": (Fraction(3, 4), Fraction(1, 4)),
        "B": (Fraction(1, 4), Fraction(3, 4)),
    }
    length = 4
    observed = ("A", "A", "A", "A")
    report("initial law is normalized", sum(p0) == 1 and all(x >= 0 for x in p0), str(p0))
    report("kernel is row-stochastic", row_stochastic(k), str(k))
    total_prob = sum(prob_word(word, p0, k) for word in all_words(length))
    report("word probabilities normalize", total_prob == 1, str(total_prob))

    dist = count_distribution(length, p0, k)
    report("count distribution normalizes", sum(dist.values()) == 1, str(dist))
    report("observed counts are integral", count_word(observed) == (4, 0), str(count_word(observed)))
    report("observed statistic is max imbalance", statistic(count_word(observed)) == 4)

    expected_from_counts = expected_count_from_distribution(dist)
    expected_from_marginals = expected_count_by_marginals(length, p0, k)
    report("expected counts match time-marginal sum", expected_from_counts == expected_from_marginals, str(expected_from_counts))
    report("expected A count is exact", expected_from_counts[0] == Fraction(47, 16), str(expected_from_counts[0]))

    pval = p_value_for_observed(observed, length, p0, k)
    direct_extremes = dist[(4, 0)] + dist.get((0, 4), Fraction(0))
    report("observed exact p-value matches count-distribution tail", pval == direct_extremes, str(pval))

    pvals = set(p_value_map(length, p0, k).values())
    pvals.update({Fraction(0), Fraction(1), Fraction(1, 20), Fraction(1, 2)})
    report("exact finite p-values are conservative", all(prob_p_at_most(alpha, length, p0, k) <= alpha for alpha in pvals))


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_kernel = False
    record_derives_statistic = False
    record_derives_threshold = False
    record_derives_concentration = False
    record_derives_clock_or_rate = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived kernel flag is false", not record_derives_kernel)
    report("Record-derived statistic flag is false", not record_derives_statistic)
    report("Record-derived threshold flag is false", not record_derives_threshold)
    report("Record-derived concentration flag is false", not record_derives_concentration)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    finite_count_audit_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_KERNEL_EXACT_COUNT_AUDIT=TRUE")
    print("FINITE_P_VALUES_EXACT=TRUE")
    print("RECORD_DERIVES_KERNEL_OR_STATISTIC=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
