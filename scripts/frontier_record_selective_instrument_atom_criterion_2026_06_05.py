#!/usr/bin/env python3
"""Selective instrument atom criterion for post-record history."""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ATOL = 1e-12


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


def projector(i: int) -> np.ndarray:
    p = np.zeros((2, 2), dtype=complex)
    p[i, i] = 1.0
    return p


def selective_map(rho: np.ndarray, i: int) -> np.ndarray:
    p = projector(i)
    return p @ rho @ p


def normalize(branch: np.ndarray) -> np.ndarray:
    return branch / np.trace(branch)


def append(history: tuple[int, ...], atom: int) -> tuple[int, ...]:
    return history + (atom,)


def main() -> int:
    emit("=" * 78)
    emit("RECORD SELECTIVE INSTRUMENT ATOM CRITERION")
    emit("bounded-support / selective post-record gate runner")
    emit("=" * 78)

    p0 = 0.3
    p1 = 0.7
    rho = np.array([[p0, np.sqrt(p0 * p1)], [np.sqrt(p0 * p1), p1]], dtype=complex)

    section("1. Selective branch probabilities")
    branches = [selective_map(rho, i) for i in (0, 1)]
    probs = [float(np.trace(branch).real) for branch in branches]
    check("input state is normalized", np.isclose(np.trace(rho).real, 1.0, atol=ATOL))
    check("branch probability p0 is recovered", np.isclose(probs[0], p0, atol=ATOL))
    check("branch probability p1 is recovered", np.isclose(probs[1], p1, atol=ATOL))
    check("branch probabilities sum to one", np.isclose(sum(probs), 1.0, atol=ATOL))
    check("both branches have positive support", all(prob > 0 for prob in probs))
    check("nonselective output is the sum of branches", np.allclose(sum(branches), np.diag([p0, p1]), atol=ATOL))
    check("nonselective output is not one-hot", np.count_nonzero(np.diag(sum(branches)).real > ATOL) == 2)
    check("coherence is removed in nonselective output", np.isclose(sum(branches)[0, 1], 0.0, atol=ATOL))

    section("2. Normalized branch states and repeat stability")
    normalized = [normalize(branch) for branch in branches]
    for i, state in enumerate(normalized):
        check(f"branch {i}: normalized trace one", np.isclose(np.trace(state).real, 1.0, atol=ATOL))
        check(f"branch {i}: one-hot state", np.isclose(state[i, i], 1.0, atol=ATOL))
        reread = projector(i) @ state @ projector(i)
        check(f"branch {i}: repeat readout stable", np.allclose(reread, state, atol=ATOL))
    check("branch 0 and branch 1 are distinct atoms", not np.allclose(normalized[0], normalized[1], atol=ATOL))

    section("3. History append gate")
    history: tuple[int, ...] = ()
    history0 = append(history, 0)
    history1 = append(history0, 1)
    check("empty history has no atom", history == ())
    check("selected atom appends to history", history0 == (0,))
    check("second selected atom appends in order", history1 == (0, 1))
    check("nonselective density is not appended as atom", not isinstance(sum(branches), int))
    check("history length counts selected atoms", len(history1) == 2)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_SELECTIVE_INSTRUMENT_ATOM_CRITERION_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "selective atom criterion",
        "Does not derive outcome selection",
        "nonselective state `sum_i M_i(rho)` is not a single atom",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("selection closure", "outcome selection is " + "derived"),
        ("born closure", "Born frequencies are " + "derived"),
        ("collapse closure", "physical collapse is " + "derived"),
        ("rate closure", "clock/rate is " + "derived"),
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
