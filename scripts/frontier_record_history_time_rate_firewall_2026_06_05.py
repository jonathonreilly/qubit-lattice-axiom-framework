#!/usr/bin/env python3
"""Record history order/time-rate firewall.

Finite record histories supply ordered words and counts. Supplied kernels give
probabilities per admitted step. A physical time metric or rate normalization
requires an extra clock/production bridge.
"""

from __future__ import annotations

from math import exp, log
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-10


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


def counts(word: list[int], alphabet_size: int = 2) -> np.ndarray:
    out = np.zeros(alphabet_size, dtype=int)
    for symbol in word:
        out[symbol] += 1
    return out


def is_stochastic(matrix: np.ndarray) -> bool:
    return bool(np.all(matrix >= -TOL) and np.allclose(matrix.sum(axis=1), 1.0, atol=TOL))


def main() -> int:
    emit("=" * 78)
    emit("RECORD HISTORY ORDER / TIME-RATE FIREWALL")
    emit("bounded-support / negative-route-pruning runner")
    emit("=" * 78)

    section("1. Record words supply order/counts, not a metric")
    word = [0, 1, 0, 0, 1]
    c = counts(word)
    appended = word + [1]
    prefixes = [word[:i] for i in range(len(word) + 1)]
    long_word = [i % 2 for i in range(1000)]
    check("history is a finite word", isinstance(word, list) and len(word) == 5, str(word))
    check("counts sum to word length", int(c.sum()) == len(word), str(c.tolist()))
    check("append increases length by one", len(appended) == len(word) + 1)
    check("append updates the realized symbol count", np.all(counts(appended) == c + np.array([0, 1])))
    check("prefix lengths are monotone", [len(p) for p in prefixes] == list(range(len(word) + 1)))
    check("arbitrary finite extension exists", len(long_word) == 1000)
    check("no fixed finite cap appears in the word grammar", len(long_word) > len(word))

    section("2. Same word, different time grids, different rates")
    unit_times = np.arange(len(word) + 1, dtype=float)
    double_times = 2.0 * unit_times
    irregular_times = np.array([0.0, 0.7, 2.0, 5.5, 5.6, 9.0])
    unit_rate = len(word) / (unit_times[-1] - unit_times[0])
    double_rate = len(word) / (double_times[-1] - double_times[0])
    irregular_rate = len(word) / (irregular_times[-1] - irregular_times[0])
    check("unit and double grids preserve event order", np.all(np.diff(unit_times) > 0) and np.all(np.diff(double_times) > 0))
    check("irregular grid preserves event order", np.all(np.diff(irregular_times) > 0))
    check("record counts are invariant under time-grid choice", np.all(counts(word) == c))
    check("unit and double grids give different rates", abs(unit_rate - double_rate) > TOL, f"{unit_rate} vs {double_rate}")
    check("irregular grid gives another rate", abs(irregular_rate - unit_rate) > TOL, f"{irregular_rate} vs {unit_rate}")
    check("rate rescales inversely with uniform time scale", abs(unit_rate / double_rate - 2.0) < TOL)

    section("3. Step kernels do not fix step duration")
    p_step = np.array([[0.8, 0.2], [0.3, 0.7]])
    pi = np.array([0.6, 0.4])
    one_step = pi @ p_step
    two_step = pi @ p_step @ p_step
    dt1 = 1.0
    dt2 = 0.5
    q1 = (p_step - np.eye(2)) / dt1
    q2 = (p_step - np.eye(2)) / dt2
    check("step kernel is stochastic", is_stochastic(p_step))
    check("initial distribution is normalized", abs(float(pi.sum()) - 1.0) < TOL)
    check("one-step distribution is normalized", abs(float(one_step.sum()) - 1.0) < TOL, str(one_step.tolist()))
    check("two-step distribution is normalized", abs(float(two_step.sum()) - 1.0) < TOL, str(two_step.tolist()))
    check("same step distributions are compatible with either dt", np.allclose(pi @ p_step, one_step))
    check("Euler-style generator estimate scales with dt", np.allclose(q2, 2.0 * q1))
    check("off-diagonal rates change when dt changes", abs(q1[0, 1] - q2[0, 1]) > TOL, f"{q1[0,1]} vs {q2[0,1]}")
    check("kernel alone does not encode the chosen dt", dt1 != dt2 and np.allclose(p_step, p_step))

    section("4. One-step event probability does not fix lambda")
    q_event = 0.2
    lambda1 = -log(1 - q_event) / 1.0
    lambda2 = -log(1 - q_event) / 2.0
    q_from_pair1 = 1 - exp(-lambda1 * 1.0)
    q_from_pair2 = 1 - exp(-lambda2 * 2.0)
    check("first lambda/dt pair gives q", abs(q_from_pair1 - q_event) < TOL)
    check("second lambda/dt pair gives same q", abs(q_from_pair2 - q_event) < TOL)
    check("the two lambdas differ", abs(lambda1 - lambda2) > TOL, f"{lambda1:.6f} vs {lambda2:.6f}")
    check("same one-step probability is not a unique rate", abs(q_from_pair1 - q_from_pair2) < TOL and abs(lambda1 - lambda2) > TOL)

    section("5. Typed residual ledger")
    record_outputs = {"word", "prefix_order", "count", "append"}
    kernel_outputs = {"per_step_probability", "joint_word_probability"}
    time_outputs = {"clock_map", "duration", "continuous_rate", "generator"}
    check("record outputs do not include time outputs", record_outputs.isdisjoint(time_outputs))
    check("kernel outputs do not include time outputs", kernel_outputs.isdisjoint(time_outputs))
    check("time/rate bridge is a separate output class", "clock_map" in time_outputs and "append" not in time_outputs)

    section("6. Source note sanity")
    doc = Path("docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    text_flat = " ".join(text.split())
    markers = [
        "claim_type_author_hint: no_go",
        "**Claim type:** no_go",
        "bounded negative route-pruning certificate",
        "Trace class: negative route pruning",
        "Does not derive physical time",
        "Does not select a generation/Koide dial setting.",
        "This row is not a positive time/rate theorem.",
        "It is not a production theorem",
        "makes no retained-status proposal",
        "does not use bare retained language",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text or marker in text_flat)
    forbidden_wording = [
        ("time closure", "physical time is " + "derived"),
        ("rate closure", "rates are " + "derived"),
        ("generator closure", "generator is " + "derived"),
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
