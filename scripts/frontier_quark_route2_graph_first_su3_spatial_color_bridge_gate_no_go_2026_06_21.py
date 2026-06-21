#!/usr/bin/env python3
"""Graph-first SU(3) spatial-color bridge gate for Route-2 c_TE.

This runner steelmans the named escape in the existing c_TE=-R_conn
cross-domain no-go: grant the graph-first N_c=3-from-d=3 link and decompose
the same spatial 3x3 matrix space. The result is still negative for the
Route-2 bridge: 8/9 is the total traceless-adjoint fraction of End(R^3), while
c_TE is an E/T2 readout ratio inside the spin-2 symmetric-traceless sector.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def read_text(relpath: str) -> str:
    try:
        return (DOCS / relpath).read_text(encoding="utf-8")
    except OSError:
        return ""


def ratio(a: int, b: int) -> Fraction:
    return Fraction(a, b)


def part1_graph_first_steelman() -> None:
    print("PART 1: graph-first SU(3) steelman markers")
    required = {
        "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md": [
            "base splits as `3 \\oplus 1`",
            "compact semisimple part is:",
            "su(3)",
        ],
        "NATIVE_GAUGE_CLOSURE_NOTE.md": [
            "graph-first selected-axis structural `su(3)`",
            "nonabelian gauge-structure surface",
            "Excluded:",
        ],
        "CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md": [
            "only escape",
            "N_c=3",
            "spatial",
            "color",
        ],
        "CUBIC_ANISOTROPY_SECTIONS_SO3_FRAME_BOUNDED_THEOREM_NOTE_2026-06-17.md": [
            "spin-2",
            "E (2-dim)",
            "T2 (3-dim)",
        ],
    }
    for relpath, markers in required.items():
        text = read_text(relpath)
        check(f"{relpath} exists", bool(text))
        for marker in markers:
            check(f"{relpath} contains marker: {marker}", marker in text)


def part2_spatial_matrix_decomposition() -> None:
    print()
    print("PART 2: strongest same-3-space decomposition")
    dims = {
        "scalar_A1": 1,
        "antisymmetric_T1": 3,
        "symmetric_traceless_l2": 5,
        "cubic_E": 2,
        "cubic_T2": 3,
    }
    total = 9
    adjoint = dims["antisymmetric_T1"] + dims["symmetric_traceless_l2"]
    l2 = dims["symmetric_traceless_l2"]
    e = dims["cubic_E"]
    t2 = dims["cubic_T2"]

    check("End(R^3) has dimension 9", total == 9)
    check("scalar plus traceless split is 1 + 8", dims["scalar_A1"] + adjoint == total)
    check("traceless-adjoint split is T1 + l2 = 3 + 5", adjoint == 8)
    check("spin-2 l2 split is E + T2 = 2 + 3", e + t2 == l2)
    check("F_adj is total traceless-adjoint over total End", ratio(adjoint, total) == Fraction(8, 9))
    check("singlet fraction is the complementary 1/9", ratio(dims["scalar_A1"], total) == Fraction(1, 9))
    check("l2 fraction of total End is 5/9, not 8/9", ratio(l2, total) == Fraction(5, 9))
    check("T2 fraction of total End is 1/3, not 8/9", ratio(t2, total) == Fraction(1, 3))
    check("E fraction of total End is 2/9, not 8/9", ratio(e, total) == Fraction(2, 9))
    check("T2/E internal split ratio is 3/2, not 8/9", ratio(t2, e) == Fraction(3, 2))
    check("E/T2 internal split ratio is 2/3, not 8/9", ratio(e, t2) == Fraction(2, 3))
    check("T2/l2 internal fraction is 3/5, not 8/9", ratio(t2, l2) == Fraction(3, 5))
    check("E/l2 internal fraction is 2/5, not 8/9", ratio(e, l2) == Fraction(2, 5))
    check("l2/adjoint fraction is 5/8, not 8/9", ratio(l2, adjoint) == Fraction(5, 8))


def part3_bridge_failure() -> None:
    print()
    print("PART 3: bridge failure under the steelman")
    target_abs = Fraction(8, 9)
    candidate_ratios = {
        "adjoint_over_total": Fraction(8, 9),
        "singlet_over_total": Fraction(1, 9),
        "l2_over_total": Fraction(5, 9),
        "T1_over_total": Fraction(1, 3),
        "T2_over_total": Fraction(1, 3),
        "E_over_total": Fraction(2, 9),
        "T2_over_E": Fraction(3, 2),
        "E_over_T2": Fraction(2, 3),
        "T2_over_l2": Fraction(3, 5),
        "E_over_l2": Fraction(2, 5),
        "l2_over_adjoint": Fraction(5, 8),
        "T2_over_adjoint": Fraction(3, 8),
        "E_over_adjoint": Fraction(1, 4),
    }
    hits = [name for name, value in candidate_ratios.items() if value == target_abs]
    check("only adjoint_over_total equals 8/9", hits == ["adjoint_over_total"], str(hits))
    internal_hits = [
        name
        for name, value in candidate_ratios.items()
        if name != "adjoint_over_total" and value == target_abs
    ]
    check("no E/T2 or l2-internal ratio equals 8/9", not internal_hits, str(internal_hits))
    check(
        "there is no sign in dimension counting",
        all(value > 0 for value in candidate_ratios.values()),
        "dimension fractions are nonnegative; c_TE needs a signed orientation",
    )
    check(
        "typed graph-first link routes 8/9 to total adjoint count, not E/T2 readout",
        candidate_ratios["adjoint_over_total"] == target_abs
        and candidate_ratios["T2_over_E"] != target_abs
        and candidate_ratios["T2_over_l2"] != target_abs,
    )


def part4_companion_note() -> None:
    print()
    print("PART 4: companion note hygiene")
    relpath = "QUARK_ROUTE2_GRAPH_FIRST_SU3_SPATIAL_COLOR_BRIDGE_GATE_NO_GO_NOTE_2026-06-21.md"
    text = read_text(relpath)
    check(f"{relpath} exists", bool(text))
    required = [
        "Actual current-surface status: no-go for the graph-first spatial-color escape",
        "This is not an audit verdict",
        "Strongest Steelman",
        "Theorem",
        "negative_route_pruning",
        "does not close the parent S3/Route-2 open gate",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text)
    banned = [
        ("parent closure", "closes the " + "parent"),
        ("endpoint derivation", "derives the endpoint " + "triple"),
        ("rho_E derivation", "derives " + "rho_E = 21/4"),
        ("permanent no-go", "no future " + "spatial-color theorem can exist"),
    ]
    for label, phrase in banned:
        check(f"note avoids overclaim: {label}", phrase not in text)


def main() -> int:
    print("Route-2 graph-first SU(3) spatial-color bridge gate")
    print("Status: no-go for the graph-first spatial-color escape; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    print()
    part1_graph_first_steelman()
    part2_spatial_matrix_decomposition()
    part3_bridge_failure()
    part4_companion_note()
    print()
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "VERDICT: even granting the graph-first N_c=3-from-d=3 link, "
            "8/9 is the total traceless-adjoint fraction, while c_TE lives "
            "inside the E/T2 spin-2 split. The typed bridge still needs an "
            "extra readout functional or orientation selector."
        )
        return 0
    print("VERDICT: graph-first bridge gate checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
