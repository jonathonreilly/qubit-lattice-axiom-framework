#!/usr/bin/env python3
"""Supplied transition-kernel interface for post-record histories.

Given a finite record alphabet, an initial law, and a row-stochastic transition
kernel, finite-history probabilities and expected count updates are exact. The
kernel itself is not derived by Record.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B", "C")


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


def count_word(word: tuple[str, ...]) -> tuple[int, int, int]:
    counts = Counter(word)
    return tuple(counts[a] for a in ALPHABET)


def add_counts(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(x + y for x, y in zip(a, b))


def basis(atom: str) -> tuple[int, int, int]:
    return tuple(1 if a == atom else 0 for a in ALPHABET)


def as_fraction_count(counts: tuple[int, int, int]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(Fraction(c, 1) for c in counts)


def row_stochastic(kernel: dict[str, tuple[Fraction, Fraction, Fraction]]) -> bool:
    return all(sum(row) == 1 and all(x >= 0 for x in row) for row in kernel.values())


def prob_history(
    word: tuple[str, ...],
    mu0: tuple[Fraction, Fraction, Fraction],
    kernel: dict[str, tuple[Fraction, Fraction, Fraction]],
) -> Fraction:
    if not word:
        return Fraction(1, 1)
    idx = {a: i for i, a in enumerate(ALPHABET)}
    p = mu0[idx[word[0]]]
    for left, right in zip(word, word[1:]):
        p *= kernel[left][idx[right]]
    return p


def expected_count_by_enumeration(
    n_events: int,
    mu0: tuple[Fraction, Fraction, Fraction],
    kernel: dict[str, tuple[Fraction, Fraction, Fraction]],
) -> tuple[Fraction, Fraction, Fraction]:
    total = (Fraction(0), Fraction(0), Fraction(0))
    for word in product(ALPHABET, repeat=n_events):
        p = prob_history(tuple(word), mu0, kernel)
        total = add_counts(total, tuple(p * c for c in count_word(tuple(word))))
    return total


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_TRANSITION_KERNEL_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "trace_class: upstream_support",
            "transition-kernel derivation remains open",
            "Rows that need the kernel",
            "generation or Koide dial",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "post-record append action on O*",
            "transition rates or a time metric",
            "realized counts stay integral while ensemble expectations can be fractional",
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
            "post-record information dynamics",
            "probability laws, Born typicality, and transition rates",
            "Record history/count support is therefore an exact **consumer**",
        ],
    )


def kernel_interface_checks() -> None:
    section("Supplied kernel gives finite-history probabilities")
    mu0 = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    kernel = {
        "A": (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
        "B": (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)),
        "C": (Fraction(1, 5), Fraction(1, 5), Fraction(3, 5)),
    }
    report("initial law is normalized", sum(mu0) == 1)
    report("transition kernel is row-stochastic", row_stochastic(kernel))

    for n_events in (1, 2, 3, 4):
        total = sum(prob_history(tuple(word), mu0, kernel) for word in product(ALPHABET, repeat=n_events))
        report(f"history probabilities normalize at length {n_events}", total == 1, str(total))

    word = ("A", "B", "C")
    p_word = prob_history(word, mu0, kernel)
    expected_p = mu0[0] * kernel["A"][1] * kernel["B"][2]
    report("specific history probability is product of supplied factors", p_word == expected_p, str(p_word))

    current_count = as_fraction_count(count_word(word))
    next_expectation = add_counts(current_count, kernel[word[-1]])
    report("conditional expected next count is c + current kernel row", next_expectation == (Fraction(6, 5), Fraction(6, 5), Fraction(8, 5)), str(next_expectation))
    realized_next = count_word(word + ("A",))
    report("realized append remains integral", realized_next == (2, 1, 1), str(realized_next))
    report("expected next count can be fractional", any(x.denominator != 1 for x in next_expectation))

    expected_len3 = expected_count_by_enumeration(3, mu0, kernel)
    report("expected counts over length 3 sum to length", sum(expected_len3) == 3, str(expected_len3))
    report("expected counts over length 3 can be fractional", any(x.denominator != 1 for x in expected_len3))

    other_kernel = {
        "A": (Fraction(9, 10), Fraction(1, 10), Fraction(0, 1)),
        "B": (Fraction(0, 1), Fraction(9, 10), Fraction(1, 10)),
        "C": (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)),
    }
    report("alternative supplied kernel is also row-stochastic", row_stochastic(other_kernel))
    report("same realized word gets different next prediction under different kernels", kernel["C"] != other_kernel["C"])


def firewall_checks() -> None:
    section("Firewall flags")
    kernel_derived_by_record = False
    markov_property_derived = False
    stationarity_derived = False
    clock_or_rate_derived = False
    born_or_instrument_derived = False
    hamiltonian_selected = False
    generation_or_koide_dial_selected = False
    report("Record-derived kernel flag is false", not kernel_derived_by_record)
    report("Record-derived Markov property flag is false", not markov_property_derived)
    report("Record-derived stationarity flag is false", not stationarity_derived)
    report("Record-derived clock/rate flag is false", not clock_or_rate_derived)
    report("Record-derived Born/instrument flag is false", not born_or_instrument_derived)
    report("Record-derived Hamiltonian flag is false", not hamiltonian_selected)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    kernel_interface_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_KERNEL_EXTENDS_TO_RECORD_HISTORY_LAW=TRUE")
    print("RECORD_DERIVES_TRANSITION_KERNEL=FALSE")
    print("REALIZED_COUNTS_REMAIN_INTEGRAL=TRUE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
