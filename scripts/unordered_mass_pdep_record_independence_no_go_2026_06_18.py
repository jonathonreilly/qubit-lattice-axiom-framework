#!/usr/bin/env python3
"""Record-independence no-go for unordered-mass P-dep.

This runner checks the countermodel in
docs/UNORDERED_MASS_PDEP_RECORD_INDEPENDENCE_NO_GO_NOTE_2026-06-18.md.

Claim boundary: Record finite additivity plus K/CPT orbit constancy do not
derive P-dep. The constructed q-scaled readouts are Record-compatible but are
not functions only of the registered sector datum ([k], lambda_k).
"""

from __future__ import annotations

import math
from pathlib import Path

PASS = 0
FAIL = 0
TOL = 1.0e-10

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "UNORDERED_MASS_PDEP_RECORD_INDEPENDENCE_NO_GO_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}" + (f": {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"[FAIL] {label}" + (f": {detail}" if detail else ""))


def sigma(k: int) -> int:
    return (-k) % 3


def orbit(k: int) -> tuple[int, ...]:
    return tuple(sorted({k, sigma(k)}))


def lam(delta: float, a: float, b: float, k: int) -> float:
    return a + 2.0 * b * math.cos(delta + 2.0 * math.pi * k / 3.0)


def readout(q: float, sectors: set[int], delta: float, a: float, b: float) -> float:
    return q * sum(lam(delta, a, b, k) for k in sectors)


def registered_datum(k: int, delta: float, a: float, b: float) -> tuple[tuple[int, ...], float]:
    return (orbit(k), round(lam(delta, a, b, k), 12))


def disjoint_pairs() -> list[tuple[set[int], set[int]]]:
    universe = {0, 1, 2}
    pairs: list[tuple[set[int], set[int]]] = []
    subsets = [set(), {0}, {1}, {2}, {0, 1}, {0, 2}, {1, 2}, {0, 1, 2}]
    for a_set in subsets:
        for b_set in subsets:
            if a_set.isdisjoint(b_set) and a_set.union(b_set).issubset(universe):
                pairs.append((a_set, b_set))
    return pairs


def main() -> int:
    print("=" * 88)
    print("UNORDERED MASS P-DEP RECORD-INDEPENDENCE NO-GO")
    print("=" * 88)

    params = [
        (0.7, 1.2, 0.37),
        (2.0, -0.4, 0.91),
        (-1.1, 0.8, -0.63),
        (0.2, 2.5, 1.17),
    ]
    q_values = [1.0, 2.0, -3.0]

    # Surface sanity: K/CPT acts as k -> -k and flips delta.
    check("sigma is an involution", all(sigma(sigma(k)) == k for k in range(3)))
    check("sigma fixes exactly the singlet label", sum(1 for k in range(3) if sigma(k) == k) == 1)
    check("orbits are singlet plus doublet", {orbit(k) for k in range(3)} == {(0,), (1, 2)})

    ok = True
    for a, b, delta in params:
        for k in range(3):
            ok &= abs(lam(-delta, a, b, sigma(k)) - lam(delta, a, b, k)) < TOL
    check("lambda_{sigma(k)}(-delta) == lambda_k(delta)", ok)

    # Record finite additivity for every q-scaled readout.
    ok = True
    for q in q_values:
        for a, b, delta in params:
            for left, right in disjoint_pairs():
                lhs = readout(q, left | right, delta, a, b)
                rhs = readout(q, left, delta, a, b) + readout(q, right, delta, a, b)
                ok &= abs(lhs - rhs) < TOL
    check("I_q is finitely additive over disjoint sector records", ok)

    ok = all(abs(readout(q, set(), delta, a, b)) < TOL
             for q in q_values for a, b, delta in params)
    check("I_q(empty) = 0", ok)

    # K/CPT orbit constancy for every fixed q.
    ok = True
    for q in q_values:
        for a, b, delta in params:
            for k in range(3):
                left = readout(q, {sigma(k)}, -delta, a, b)
                right = readout(q, {k}, delta, a, b)
                ok &= abs(left - right) < TOL
    check("I_q is constant on K/CPT-related single-sector records", ok)

    ok = True
    for q in q_values:
        for a, b, delta in params:
            # The doublet orbit as a collection is also invariant under the flip.
            ok &= abs(readout(q, {1, 2}, -delta, a, b)
                      - readout(q, {1, 2}, delta, a, b)) < TOL
            ok &= abs(readout(q, {0}, -delta, a, b)
                      - readout(q, {0}, delta, a, b)) < TOL
    check("I_q is orbit-constant on singlet and doublet record collections", ok)

    # The no-go witness: same registered datum, different unregistered q,
    # different scalar value.
    a, b, delta = params[0]
    k = 0
    datum_one = registered_datum(k, delta, a, b)
    datum_two = registered_datum(k, delta, a, b)
    value_one = readout(1.0, {k}, delta, a, b)
    value_two = readout(2.0, {k}, delta, a, b)
    check("two contexts have identical registered datum", datum_one == datum_two, detail=str(datum_one))
    check("the witness datum is nonzero", abs(value_one) > TOL, detail=f"I_1={value_one:.12g}")
    check("different unregistered q gives different readout value",
          abs(value_one - value_two) > TOL,
          detail=f"I_1={value_one:.12g}, I_2={value_two:.12g}")

    # Same conclusion on the doublet collection, so it is not a singlet accident.
    doublet_value_one = readout(1.0, {1, 2}, delta, a, b)
    doublet_value_two = readout(2.0, {1, 2}, delta, a, b)
    check("doublet witness also changes under unregistered q",
          abs(doublet_value_one - doublet_value_two) > TOL,
          detail=f"I_1={doublet_value_one:.12g}, I_2={doublet_value_two:.12g}")

    # Source-scope guards.
    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    parent_text = PARENT.read_text(encoding="utf-8")
    for phrase in [
        "Record alone cannot derive P-dep",
        "extra extensionality/readout-identification premise",
        "introduces no new axiom",
        "does not edit audit results",
        "does not dispute the existing conditional theorem",
    ]:
        check(f"note boundary phrase: {phrase}", phrase in note_flat)
    check("parent note links the P-dep independence no-go", NOTE.name in parent_text)

    print("=" * 88)
    print(f"SUMMARY: UNORDERED MASS P-DEP RECORD-INDEPENDENCE NO-GO PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
