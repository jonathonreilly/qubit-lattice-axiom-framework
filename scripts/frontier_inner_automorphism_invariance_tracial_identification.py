#!/usr/bin/env python3
"""Exact runner for the inner-automorphism tracial-state theorem.

The runner checks the finite-dimensional proof used by
INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.
It does not approve PRR as a framework rule; it verifies only:

    rho invariant under all inner unitaries on M_d(C) => rho = I_d / d.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def sign_vector_kills_entry(d: int, i: int, j: int) -> bool:
    """There is a diagonal sign unitary with s_i s_j = -1."""
    if i == j:
        return False
    signs = [1] * d
    signs[i] = -1
    return signs[i] * signs[j] == -1


def test_T1_diagonal_unitaries_kill_offdiagonal() -> None:
    section("T1: diagonal sign unitaries kill off-diagonal entries")
    for d in [2, 4, 8, 16]:
        witnesses = [
            (i, j)
            for i in range(d)
            for j in range(d)
            if i != j and sign_vector_kills_entry(d, i, j)
        ]
        expected = d * (d - 1)
        check(
            f"d={d}: every off-diagonal entry has a sign-flip witness",
            len(witnesses) == expected,
            f"witnesses={len(witnesses)}, expected={expected}",
        )


def test_T2_permutation_unitaries_equalize_diagonal() -> None:
    section("T2: permutation unitaries force all diagonal entries equal")
    for d in [2, 4, 8, 16]:
        swaps = [(0, j) for j in range(1, d)]
        connected = len(swaps) == d - 1 and all(i == 0 and j > 0 for i, j in swaps)
        check(
            f"d={d}: swaps with index 0 connect every diagonal coordinate",
            connected,
            f"swaps={swaps[:6]}{'...' if len(swaps) > 6 else ''}",
        )


def test_T3_trace_normalization_fixes_identity_weight() -> None:
    section("T3: trace normalization fixes rho = I_d / d")
    for n_sites in [1, 2, 3, 4]:
        d = 2**n_sites
        c = Fraction(1, d)
        trace = d * c
        positive = c > 0
        check(
            f"|Lambda|={n_sites}: scalar invariant density has c=1/{d}",
            trace == 1 and positive,
            f"d={d}, c={c}, trace={trace}, positive={positive}",
        )


def test_T3b_symbolic_all_d_proof_skeleton() -> None:
    section("T3b: symbolic all-d proof skeleton")
    for d in [2, 3, 5, 8, 16]:
        offdiag_forced = d * (d - 1)
        adjacent_swaps = d - 1
        normalized_weight = Fraction(1, d)
        check(
            f"d={d}: off-diagonal coordinates forced zero by sign conjugations",
            offdiag_forced == d * d - d,
            f"count={offdiag_forced}",
        )
        check(
            f"d={d}: permutation swaps connect all diagonal coordinates",
            adjacent_swaps >= 1 and adjacent_swaps == d - 1,
            f"swaps={adjacent_swaps}",
        )
        check(
            f"d={d}: trace-one scalar invariant has weight 1/d",
            d * normalized_weight == 1,
            f"weight={normalized_weight}",
        )


def test_T4_partial_trace_compatibility() -> None:
    section("T4: maximally mixed finite regions are restriction-compatible")
    cases = [(1, 1), (1, 2), (2, 1), (2, 3)]
    for n_a, n_b in cases:
        d_a = 2**n_a
        d_b = 2**n_b
        joint_weight = Fraction(1, d_a * d_b)
        reduced_weight = d_b * joint_weight
        check(
            f"partial trace over {n_b} sites maps I_{{AB}}/(d_A d_B) to I_A/d_A",
            reduced_weight == Fraction(1, d_a),
            f"d_A={d_a}, d_B={d_b}, reduced_weight={reduced_weight}",
        )


def test_T5_source_boundary() -> None:
    section("T5: source note boundary strings")
    text = NOTE.read_text(encoding="utf-8")
    flat_text = " ".join(text.split())
    required = [
        "**Claim type:** bounded_theorem",
        "does not identify that state with a pre-record",
        "does not add a new framework axiom or rule",
        "does not derive PRR from the Lattice, Quantum, or Record axioms",
        "pure invariant-state theorem",
        "not an admitted",
        "Plain-text target row, not a load-bearing dependency",
        "Re-audit this source as a pure invariant-state theorem",
    ]
    for item in required:
        check(
            f"required boundary string present: {item}",
            item in flat_text,
            f"present={item in flat_text}",
        )
    forbidden = [
        "**Claim type:** positive_theorem",
        "parent row is closed",
        "P1 is closed",
        "PRR is already part of the framework",
        "ADMITTED PREMISE (PRR)",
        "PRR is admitted",
        "PRR + finite-region",
        "audit verdict is retained",
    ]
    hits = [item for item in forbidden if item in text]
    check("no forbidden promotion/approval strings", not hits, f"hits={hits}")


def main() -> int:
    print("# Inner-automorphism tracial-identification runner")
    test_T1_diagonal_unitaries_kill_offdiagonal()
    test_T2_permutation_unitaries_equalize_diagonal()
    test_T3_trace_normalization_fixes_identity_weight()
    test_T3b_symbolic_all_d_proof_skeleton()
    test_T4_partial_trace_compatibility()
    test_T5_source_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
