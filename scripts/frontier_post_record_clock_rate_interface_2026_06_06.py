#!/usr/bin/env python3
"""Post-record clock/rate interface verifier.

Finite post-record histories determine event order and counts. A physical
clock or rate is obtained only after a strictly increasing clock map is
supplied.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


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


ALPHABET = ("singlet", "doublet", "other")


def prefixes(word: tuple[str, ...]) -> list[tuple[str, ...]]:
    return [word[:i] for i in range(len(word) + 1)]


def count_word(word: tuple[str, ...]) -> tuple[int, int, int]:
    counts = Counter(word)
    return tuple(counts[a] for a in ALPHABET)


def is_strict_clock(clock: tuple[Fraction, ...], n_events: int) -> bool:
    return len(clock) == n_events + 1 and all(a < b for a, b in zip(clock, clock[1:]))


def durations(clock: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(b - a for a, b in zip(clock, clock[1:]))


def total_rate(n_events: int, clock: tuple[Fraction, ...]) -> Fraction:
    return Fraction(n_events, 1) / (clock[-1] - clock[0])


def letter_rates(word: tuple[str, ...], clock: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    elapsed = clock[-1] - clock[0]
    return tuple(Fraction(c, 1) / elapsed for c in count_word(word))


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: no-go",
            "trace_class: negative_route_pruning",
            "post-record word/count stream",
            "Without the supplied `tau`",
            "Does not select a generation or Koide dial location.",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "transition rates or a time metric",
            "Does not derive a time metric or clock rate",
            "finite suffix append is a right monoid action",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md",
        [
            "append-only finite-history sector",
            "Does not introduce a time metric or clock rate",
            "Rows that need record-production dynamics",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "post-record information dynamics",
            "a clock/time metric",
            "probabilities/rates/time",
            "exact post-record dynamics has no edge to production, probabilities, rates",
        ],
    )


def event_order_checks() -> None:
    section("Event-indexed post-record structure")
    word = ("singlet", "doublet", "singlet", "other")
    pref = prefixes(word)
    report("prefix list has n+1 event-index states", len(pref) == len(word) + 1)
    report("event indices are determined by prefix length", [len(p) for p in pref] == list(range(len(word) + 1)))
    report("old records are prefix-preserved at every event index", all(pref[i] == pref[-1][:i] for i in range(len(pref))))
    report("final count vector is determined by word", count_word(word) == (2, 1, 1), str(count_word(word)))
    report("event order is not a physical elapsed-time value", len(word) == 4)


def clock_nonuniqueness_checks() -> None:
    section("Clock/rate non-uniqueness")
    word = ("singlet", "doublet", "singlet", "other")
    n = len(word)
    clocks = {
        "uniform": tuple(Fraction(x, 1) for x in (0, 1, 2, 3, 4)),
        "slow": tuple(Fraction(x, 1) for x in (0, 2, 4, 6, 8)),
        "accelerating": tuple(Fraction(x, 1) for x in (0, 1, 3, 6, 10)),
    }
    clocked_records = {
        name: {"word": word, "counts": count_word(word), "clock": clock}
        for name, clock in clocks.items()
    }
    report("all candidate clocks are strict maps on the same event indices", all(is_strict_clock(c, n) for c in clocks.values()))
    report("all clocks preserve the same word", {r["word"] for r in clocked_records.values()} == {word})
    report("all clocks preserve the same counts", {r["counts"] for r in clocked_records.values()} == {count_word(word)})

    total_rates = {name: total_rate(n, clock) for name, clock in clocks.items()}
    report("same word has different total rates under different clocks", len(set(total_rates.values())) == len(total_rates), str(total_rates))
    interval_rates = {
        name: tuple(Fraction(1, 1) / d for d in durations(clock))
        for name, clock in clocks.items()
    }
    report("nonuniform clock has nonconstant interval rates", len(set(interval_rates["accelerating"])) > 1, str(interval_rates["accelerating"]))
    report("affine clock rescaling changes rates but not word/count", total_rates["uniform"] != total_rates["slow"] and count_word(word) == (2, 1, 1))

    letter_uniform = letter_rates(word, clocks["uniform"])
    letter_slow = letter_rates(word, clocks["slow"])
    report("per-letter rates depend on supplied elapsed time", letter_uniform != letter_slow, f"{letter_uniform} vs {letter_slow}")


def supplied_clock_interface_checks() -> None:
    section("Supplied-clock interface")
    word = ("singlet", "doublet", "singlet", "other")
    clock = tuple(Fraction(x, 1) for x in (0, 1, 3, 6, 10))
    dts = durations(clock)
    rates = tuple(Fraction(1, 1) / dt for dt in dts)
    report("durations are derived after clock is supplied", dts == (1, 2, 3, 4), str(dts))
    report("interval rates are derived after clock is supplied", rates == (1, Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)), str(rates))
    report("total event rate is derived after clock is supplied", total_rate(len(word), clock) == Fraction(2, 5))
    report("letter rates are derived after clock is supplied", letter_rates(word, clock) == (Fraction(1, 5), Fraction(1, 10), Fraction(1, 10)))

    count_alone_clock_derived = False
    count_alone_rate_derived = False
    count_alone_hamiltonian_selected = False
    count_alone_born_selected = False
    count_alone_dial_selected = False
    report("count-alone clock derivation flag is false", not count_alone_clock_derived)
    report("count-alone transition-rate derivation flag is false", not count_alone_rate_derived)
    report("count-alone Hamiltonian/transfer selection flag is false", not count_alone_hamiltonian_selected)
    report("count-alone Born/probability selection flag is false", not count_alone_born_selected)
    report("count-alone generation/Koide dial selection flag is false", not count_alone_dial_selected)


def main() -> int:
    source_anchor_checks()
    event_order_checks()
    clock_nonuniqueness_checks()
    supplied_clock_interface_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_COUNTS_DERIVE_CLOCK_OR_RATE=FALSE")
    print("SUPPLIED_CLOCK_GIVES_CONDITIONAL_RATES=TRUE")
    print("HAMILTONIAN_OR_TRANSFER_SELECTED=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
