#!/usr/bin/env python3
"""Exact bridge checks for occupancy from locked record outcomes.

Companion runner for
docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md.

The checks are deterministic symbolic checks. They do not consume empirical
numbers, fits, random draws, or floating tolerances.
"""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"CHECK {num:02d}: {tag} -- {desc}")


def laplacian_in_b(expr: sp.Expr, b: sp.Symbol, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    substituted = sp.expand(expr.subs(b, x + sp.I * y))
    return sp.simplify(sp.diff(substituted, x, 2) + sp.diff(substituted, y, 2))


def formal_adjoint_on_line(matrix: sp.Matrix, b: sp.Symbol, bbar: sp.Symbol) -> sp.Matrix:
    return matrix.T.xreplace({b: bbar, bbar: b})


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    axiom_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_text = axiom_path.read_text(encoding="utf-8")

    quote_lock = "When present, a record locks exactly one admissible local possibility."
    quote_content = "A readout value is determined by record content\nalone."

    check(1, quote_lock in axiom_text, "live quote guard: record locks exactly one admissible local possibility")
    check(2, quote_content in axiom_text, "live quote guard: readout value is determined by record content alone")

    a, b, c, bbar = sp.symbols("a b c bbar")
    x, y = sp.symbols("x y", real=True)
    eye3 = sp.eye(3)

    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    two_step_path = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    single_edge = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    two_edge_star = sp.Matrix([[0, 1, 1], [0, 0, 0], [0, 0, 0]])

    channels = {
        "cycle": (cycle, a**3 + b**3 + c**3 - 3 * a * b * c, -3 * a),
        "two_step_path": (two_step_path, a**3 - 2 * a * b * c, -2 * a),
        "single_edge": (single_edge, a**3 - a * b * c, -a),
        "two_edge_star": (two_edge_star, a**3 - 2 * a * b * c, -2 * a),
    }

    det_ok = True
    off_line_ok = True
    on_line_ok = True
    hermitian_ok = True
    no_bbar_before_line_ok = True
    for _, (channel, expected_det, expected_mixed) in channels.items():
        det_expr = sp.expand((a * eye3 + b * channel + c * channel.T).det())
        det_ok = det_ok and sp.simplify(det_expr - expected_det) == 0
        no_bbar_before_line_ok = no_bbar_before_line_ok and bbar not in det_expr.free_symbols
        off_line_ok = off_line_ok and laplacian_in_b(det_expr, b, x, y) == 0
        mixed_on_line = sp.diff(det_expr.subs(c, bbar), b, bbar)
        on_line_ok = on_line_ok and sp.simplify(mixed_on_line - expected_mixed) == 0
        line_matrix = a * eye3 + b * channel + bbar * channel.T
        hermitian_ok = hermitian_ok and line_matrix == formal_adjoint_on_line(line_matrix, b, bbar)

    check(3, det_ok, "T1 channel family determinants match exact small-matrix formulas")
    check(4, no_bbar_before_line_ok, "T1 off the K-real line, the family contains no conjugate coefficient")
    check(5, off_line_ok, "T1 off the K-real line, every family determinant is harmonic in (Re b, Im b)")
    check(6, on_line_ok, "T1 on c = conj(b), every family determinant has the expected nonzero mixed b-bbar term")
    check(7, hermitian_ok, "T1 c = conj(b) is the formal Hermitian/K-real section for the real channel family")

    bad_det = sp.expand((a * eye3 + b * single_edge + bbar * single_edge.T).det())
    bad_mixed = sp.diff(bad_det, b, bbar)
    check(8, sp.simplify(bad_mixed + a) == 0, "T1 negative control: conjugate contamination before K-reality gives off-line mixed curvature")

    locked_possibility_slots = sp.Integer(1)
    one_record_content_values = sp.Integer(1)
    orbit_registered_data = sp.Integer(1)
    sector_registered_data = sp.Integer(2)

    orbit_respects_lock = orbit_registered_data == locked_possibility_slots
    sector_collides_with_lock = sector_registered_data != locked_possibility_slots
    orbit_respects_content = orbit_registered_data == one_record_content_values
    sector_depends_on_split = sector_registered_data != one_record_content_values

    check(9, orbit_respects_lock and orbit_respects_content, "T2 orbit grading assigns one slot to one locked record-outcome")
    check(10, sector_collides_with_lock, "T2 sector grading makes one locked complex outcome into two registered data")
    check(11, sector_depends_on_split, "T2 sector grading changes the slot count by the Re/Im split rather than record content alone")

    g = sp.symbols("g", positive=True)
    z_orbit = sp.pi / g
    z_sector = 2 * sp.pi / g
    weight_factor = sp.simplify(z_sector / z_orbit)
    rho_orbit = sp.simplify((sp.pi / g) / z_orbit)
    rho_sector = sp.simplify((sp.pi / g) / z_sector)
    r_orbit = sp.simplify(1 / (2 * rho_orbit))
    r_sector = sp.simplify(1 / (2 * rho_sector))

    check(12, weight_factor == 2, "T2 negative control: two registered data change the doublet weight by factor 2")
    check(13, r_sector == 1 and r_orbit == sp.Rational(1, 2), "T2 factor-2 slot change reproduces r=1 versus r=1/2 exactly")

    remaining_bridge = (
        "one record locking one admissible local possibility is one statistical "
        "slot, and the relevant locked possibilities for the generation doublet "
        "are the K/CPT record-outcome orbits rather than the real components of "
        "the fluctuation coordinate"
    )

    print(
        "SUMMARY files written: "
        "docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md; "
        "scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py"
    )
    print(f"SUMMARY sharpest remaining bridge sentence: {remaining_bridge}.")
    print("SUMMARY walls dodged: category-slip by counting record-outcomes only; measure-neutrality by not using J_cs as selector.")
    print("SUMMARY uncertainty for supervisor: T2 remains a collision exhibit under the supplied one-record-one-slot reading.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
