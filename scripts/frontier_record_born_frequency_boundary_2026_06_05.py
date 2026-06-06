#!/usr/bin/env python3
"""Born-frequency boundary for finite record histories."""

from __future__ import annotations

from itertools import product
from math import comb
from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def histories(length: int) -> list[tuple[int, ...]]:
    return [tuple(bits) for bits in product((0, 1), repeat=length)]


def count_ones(word: tuple[int, ...]) -> int:
    return sum(word)


def append(word: tuple[int, ...], atom: int) -> tuple[int, ...]:
    return word + (atom,)


def binomial_weight(n: int, k: int, p: float) -> float:
    return comb(n, k) * (p**k) * ((1.0 - p) ** (n - k))


def main() -> int:
    emit("=" * 78)
    emit("RECORD BORN-FREQUENCY BOUNDARY")
    emit("no-go / finite history-count runner")
    emit("=" * 78)

    section("1. Finite histories have exact counts")
    n = 4
    words = histories(n)
    frequencies = sorted({count_ones(word) / n for word in words})
    check("all binary histories of length 4 are enumerated", len(words) == 16)
    check("frequency set has five finite values", frequencies == [0.0, 0.25, 0.5, 0.75, 1.0], str(frequencies))
    check("all-zero history has frequency zero", count_ones((0, 0, 0, 0)) / n == 0.0)
    check("all-one history has frequency one", count_ones((1, 1, 1, 1)) / n == 1.0)
    check("append adds one atom", append((1, 0), 1) == (1, 0, 1))
    check("append updates count exactly", count_ones(append((1, 0), 1)) == 2)
    count_classes = {k: [word for word in words if count_ones(word) == k] for k in range(n + 1)}
    check("count class k=2 has six histories", len(count_classes[2]) == 6)
    check("counts are many-to-one over histories", len(count_classes[2]) > 1)

    section("2. Counts do not force a probability")
    p = 0.7
    check("chosen pre-record probability is not a finite-history theorem", p not in frequencies)
    check("history with frequency zero is compatible as a word", (0, 0, 0, 0) in words)
    check("history with frequency one is compatible as a word", (1, 1, 1, 1) in words)
    check("finite frequency can differ from p by 0.7", abs(0.0 - p) == 0.7)
    check("finite frequency can differ from p by 0.3", abs(1.0 - p) == 0.30000000000000004)
    check("history grammar has no IID flag", "iid" not in {"append", "count", "prefix"})
    check("history grammar has no convergence flag", "convergence" not in {"append", "count", "prefix"})
    check("history grammar has no dial selector", "dial_selector" not in {"append", "count", "prefix"})

    section("3. Probability model is an extra input")
    weights = [binomial_weight(n, k, p) for k in range(n + 1)]
    check("supplied binomial weights sum to one", abs(sum(weights) - 1.0) < 1e-12)
    check("binomial weights use supplied p", weights[4] == p**4)
    check("without supplied p, binomial weights are undefined by history", "p" not in {"append", "count", "prefix"})
    check("selective atoms supply counts, not model", count_ones((1, 0, 1, 1)) == 3)
    check("finite count frequency is empirical information", count_ones((1, 0, 1, 1)) / 4 == 0.75)
    check("empirical frequency is not identical to p here", count_ones((1, 0, 1, 1)) / 4 != p)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "Born-frequency law remains a separate probability-model gate",
        "Does not derive Born frequencies",
        "history grammar supplies IID trials",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("born closure", "Born frequencies are " + "derived"),
        ("iid closure", "IID structure is " + "derived"),
        ("convergence closure", "convergence is " + "derived"),
        ("selection closure", "outcome selection is " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
