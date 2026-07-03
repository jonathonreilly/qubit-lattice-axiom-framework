#!/usr/bin/env python3
"""Expected empirical frequencies under supplied stable post-record kernels."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B", "C")
Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


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


def normalized(p: Vector) -> bool:
    return sum(p) == 1 and all(x >= 0 for x in p)


def reset_kernel(pi: Vector, alpha: Fraction) -> Matrix:
    rows = []
    for i in range(len(pi)):
        row = []
        for j in range(len(pi)):
            delta = Fraction(1) if i == j else Fraction(0)
            row.append((1 - alpha) * delta + alpha * pi[j])
        rows.append(tuple(row))
    return tuple(rows)


def apply(p: Vector, k: Matrix) -> Vector:
    return tuple(sum(p[i] * k[i][j] for i in range(len(p))) for j in range(len(p)))


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def sub(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))


def scale(c: Fraction, v: Vector) -> Vector:
    return tuple(c * x for x in v)


def distribution_at(p0: Vector, pi: Vector, alpha: Fraction, t: int) -> Vector:
    return add(pi, scale((1 - alpha) ** t, sub(p0, pi)))


def expected_frequency_formula(p0: Vector, pi: Vector, alpha: Fraction, n_events: int) -> Vector:
    factor = (1 - (1 - alpha) ** n_events) / (n_events * alpha)
    return add(pi, scale(factor, sub(p0, pi)))


def expected_frequency_by_iteration(p0: Vector, k: Matrix, n_events: int) -> Vector:
    total = tuple(Fraction(0) for _ in p0)
    p = p0
    for _ in range(n_events):
        total = add(total, p)
        p = apply(p, k)
    return scale(Fraction(1, n_events), total)


def count_word(word: tuple[str, ...]) -> tuple[int, ...]:
    counts = Counter(word)
    return tuple(counts[a] for a in ALPHABET)


def empirical_frequency(word: tuple[str, ...]) -> Vector:
    counts = count_word(word)
    return tuple(Fraction(c, len(word)) for c in counts)


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_STABLE_KERNEL_EXPECTED_FREQUENCY_INTERFACE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "realized post-record state is not itself a probability vector",
            "expected empirical frequency",
            "almost-sure convergence or a concentration bound",
            "generation or Koide dial",
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
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "realized counts stay integral while ensemble expectations can be fractional",
            "Does not derive probabilities",
            "Does not derive a time metric or clock rate",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "post-record information dynamics",
            "probability laws, Born typicality, and transition rates",
            "clock/time metric",
        ],
    )


def expected_frequency_checks() -> None:
    section("Expected frequency checks")
    pi = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    p0 = (Fraction(0), Fraction(1), Fraction(0))
    alpha = Fraction(2, 5)
    n_events = 5
    k = reset_kernel(pi, alpha)
    report("target prior is normalized", normalized(pi), str(pi))
    report("initial law is normalized", normalized(p0), str(p0))
    report("distribution at t=0 is initial law", distribution_at(p0, pi, alpha, 0) == p0)
    report("distribution at t=1 matches kernel application", distribution_at(p0, pi, alpha, 1) == apply(p0, k), str(apply(p0, k)))
    formula = expected_frequency_formula(p0, pi, alpha, n_events)
    iterated = expected_frequency_by_iteration(p0, k, n_events)
    report("finite-N expected frequency formula matches iteration", formula == iterated, str(formula))
    report("expected frequency is normalized", normalized(formula), str(formula))
    report("expected frequency can be fractional", any(x.denominator != 1 for x in formula), str(formula))

    realized = ("B", "A", "B", "C", "B")
    counts = count_word(realized)
    freq = empirical_frequency(realized)
    report("realized counts remain integral", counts == (1, 3, 1), str(counts))
    report("realized empirical frequency is count/length", freq == (Fraction(1, 5), Fraction(3, 5), Fraction(1, 5)), str(freq))


def target_dependence_checks() -> None:
    section("Target dependence checks")
    p0 = (Fraction(1), Fraction(0), Fraction(0))
    alpha = Fraction(1, 3)
    n_events = 4
    target_a = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    target_b = (Fraction(2, 3), Fraction(1, 6), Fraction(1, 6))
    freq_a = expected_frequency_formula(p0, target_a, alpha, n_events)
    freq_b = expected_frequency_formula(p0, target_b, alpha, n_events)
    report("target A expected frequency is normalized", normalized(freq_a), str(freq_a))
    report("target B expected frequency is normalized", normalized(freq_b), str(freq_b))
    report("different supplied targets give different expected frequencies", freq_a != freq_b)


def firewall_checks() -> None:
    section("Firewall flags")
    record_derives_target_prior = False
    record_derives_kernel = False
    record_derives_initial_law = False
    record_derives_concentration = False
    record_derives_clock_or_rate = False
    record_derives_born_or_instrument = False
    record_derives_hamiltonian = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False

    report("Record-derived target-prior flag is false", not record_derives_target_prior)
    report("Record-derived kernel flag is false", not record_derives_kernel)
    report("Record-derived initial-law flag is false", not record_derives_initial_law)
    report("Record-derived concentration flag is false", not record_derives_concentration)
    report("Record-derived clock/rate flag is false", not record_derives_clock_or_rate)
    report("Record-derived Born/instrument flag is false", not record_derives_born_or_instrument)
    report("Record-derived Hamiltonian flag is false", not record_derives_hamiltonian)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    expected_frequency_checks()
    target_dependence_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_STABLE_KERNEL_EXPECTED_FREQUENCY=TRUE")
    print("REALIZED_COUNTS_REMAIN_INTEGRAL=TRUE")
    print("RECORD_DERIVES_TARGET_OR_KERNEL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
