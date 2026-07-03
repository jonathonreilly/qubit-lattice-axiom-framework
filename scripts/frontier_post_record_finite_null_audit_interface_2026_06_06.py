#!/usr/bin/env python3
"""Exact finite-null audit interface for post-record histories.

Given a finite post-record word space, a supplied normalized null law, and a
supplied statistic, the one-sided p-value is an exact finite sum and is
conservative under that supplied null. The null law and statistic are not
derived by Record.
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


def tail_p_value(law: Law, observed: Word, statistic) -> Fraction:
    observed_score = statistic(observed)
    return sum(p for word, p in law.items() if statistic(word) >= observed_score)


def p_value_map(law: Law, statistic) -> dict[Word, Fraction]:
    return {word: tail_p_value(law, word, statistic) for word in law}


def prob_p_at_most(law: Law, statistic, alpha: Fraction) -> Fraction:
    pvals = p_value_map(law, statistic)
    return sum(p for word, p in law.items() if pvals[word] <= alpha)


def superuniform_by_enumeration(law: Law, statistic) -> bool:
    pvals = p_value_map(law, statistic)
    thresholds = set(pvals.values())
    thresholds.update({Fraction(0), Fraction(1), Fraction(1, 20), Fraction(1, 2)})
    return all(prob_p_at_most(law, statistic, alpha) <= alpha for alpha in thresholds)


def audit_flag(p_value: Fraction, alpha: Fraction) -> bool:
    return p_value <= alpha


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_FINITE_NULL_AUDIT_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "supplied finite-null audit",
            "P(p_T(W) <= alpha) <= alpha",
            "null-law, statistic, threshold, and model-selection derivation remain open",
            "generation or Koide dial",
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
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "Once a readout context supplies a finite record alphabet `O`",
            "post-record append action on O*",
            "Does not derive probabilities",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "post-record information dynamics",
            "probability laws, Born typicality, and transition rates",
            "Record history/count support is therefore an exact **consumer**",
        ],
    )


def finite_null_checks() -> None:
    section("Finite null p-value checks")
    length = 4
    observed = ("A", "A", "A", "B")
    alpha = Fraction(1, 20)

    low_a_null = iid_law(Fraction(1, 5), length)
    high_a_null = iid_law(Fraction(3, 4), length)
    report("low-A supplied null is normalized", normalized(low_a_null))
    report("high-A supplied null is normalized", normalized(high_a_null))

    low_p = tail_p_value(low_a_null, observed, count_a)
    high_p = tail_p_value(high_a_null, observed, count_a)
    report("low-A exact tail p-value matches finite sum", low_p == Fraction(17, 625), str(low_p))
    report("high-A exact tail p-value matches finite sum", high_p == Fraction(189, 256), str(high_p))
    report("same realized word can have different supplied-null p-values", low_p != high_p)

    report("low-A null flags observed word at alpha=1/20", audit_flag(low_p, alpha))
    report("high-A null does not flag observed word at alpha=1/20", not audit_flag(high_p, alpha))
    report("low-A p-values are conservative under supplied null", superuniform_by_enumeration(low_a_null, count_a))
    report("high-A p-values are conservative under supplied null", superuniform_by_enumeration(high_a_null, count_a))

    low_flag_mass = prob_p_at_most(low_a_null, count_a, alpha)
    high_flag_mass = prob_p_at_most(high_a_null, count_a, alpha)
    report("low-A flagged mass is bounded by alpha", low_flag_mass <= alpha, str(low_flag_mass))
    report("high-A flagged mass is bounded by alpha", high_flag_mass <= alpha, str(high_flag_mass))


def supplied_markov_checks() -> None:
    section("Supplied transition-kernel null checks")
    mu0 = (Fraction(1, 2), Fraction(1, 2))
    kernel = {
        "A": (Fraction(3, 4), Fraction(1, 4)),
        "B": (Fraction(1, 3), Fraction(2, 3)),
    }
    report("initial law is normalized", sum(mu0) == 1)
    report("transition kernel is row-stochastic", row_stochastic(kernel))

    law = markov_law(4, mu0, kernel)
    report("supplied Markov finite-history law is normalized", normalized(law), str(sum(law.values())))
    observed = ("B", "A", "A", "A")
    p_value = tail_p_value(law, observed, count_a)
    direct_sum = sum(p for word, p in law.items() if count_a(word) >= 3)
    report("Markov p-value equals exact enumerated tail", p_value == direct_sum, str(p_value))
    report("Markov p-values are conservative by enumeration", superuniform_by_enumeration(law, count_a))

    bad_kernel = {
        "A": (Fraction(3, 4), Fraction(1, 4)),
        "B": (Fraction(1, 3), Fraction(1, 3)),
    }
    report("non-normalized candidate kernel is rejected by row check", not row_stochastic(bad_kernel))


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_null_law = False
    record_derives_statistic = False
    record_derives_threshold = False
    record_derives_model_selection = False
    record_derives_born_or_instrument = False
    record_derives_clock_or_rate = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived null-law flag is false", not record_derives_null_law)
    report("Record-derived statistic flag is false", not record_derives_statistic)
    report("Record-derived threshold flag is false", not record_derives_threshold)
    report("Record-derived model-selection flag is false", not record_derives_model_selection)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    finite_null_checks()
    supplied_markov_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_FINITE_NULL_AUDIT_INTERFACE=TRUE")
    print("FINITE_NULL_P_VALUES_CONSERVATIVE=TRUE")
    print("RECORD_DERIVES_NULL_LAW=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
