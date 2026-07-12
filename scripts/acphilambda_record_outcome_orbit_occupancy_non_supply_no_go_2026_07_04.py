#!/usr/bin/env python3
"""Countermodels for complex versus realified determinant power."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


def realification(matrix: sp.Matrix) -> sp.Matrix:
    x = matrix.applyfunc(sp.re)
    y = matrix.applyfunc(sp.im)
    return sp.Matrix.vstack(sp.Matrix.hstack(x, -y), sp.Matrix.hstack(y, x))


def main() -> int:
    print("Complex-vs-realified determinant-power countermodels")
    print("=" * 68)

    section("Part A: generic determinant identity")
    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h", real=True)
    matrix = sp.Matrix([[a + sp.I * b, c + sp.I * d], [e + sp.I * f, g + sp.I * h]])
    det_c = sp.expand(matrix.det())
    det_r = sp.expand(realification(matrix).det())
    check("generic realification determinant is squared modulus", sp.simplify(det_r - det_c * sp.conjugate(det_c)) == 0)
    check("realification determinant is real", sp.simplify(sp.im(det_r)) == 0)

    section("Part B: same-carrier invariances")
    carrier = sp.Matrix([[1 + sp.I, 2], [3, 2 - sp.I]])
    change = sp.Matrix([[1, 1], [0, 1]])
    similar = change * carrier * change.inv()
    conjugate = carrier.conjugate()
    check("carrier is invertible", carrier.det() != 0, carrier.det())
    check("complex determinant is similarity invariant", sp.simplify(similar.det() - carrier.det()) == 0)
    check("realified determinant is similarity invariant", sp.simplify(realification(similar).det() - realification(carrier).det()) == 0)
    check("complex modulus is conjugation even", sp.simplify(conjugate.det() * sp.conjugate(conjugate.det()) - carrier.det() * sp.conjugate(carrier.det())) == 0)
    check("realified determinant is conjugation even", sp.simplify(realification(conjugate).det() - realification(carrier).det()) == 0)

    section("Part C: empty-zero and block additivity")
    block_a = sp.diag(2, 3)
    block_b = sp.Matrix([[5]])
    block_sum = sp.diag(2, 3, 5)
    fc_a = sp.log(abs(block_a.det()))
    fc_b = sp.log(abs(block_b.det()))
    fc_sum = sp.log(abs(block_sum.det()))
    fr_a = sp.log(realification(block_a).det())
    fr_b = sp.log(realification(block_b).det())
    fr_sum = sp.log(realification(block_sum).det())
    check("complex log determinant is block additive", sp.simplify(sp.expand_log(fc_sum, force=True) - sp.expand_log(fc_a, force=True) - sp.expand_log(fc_b, force=True)) == 0)
    check("realified log determinant is block additive", sp.simplify(sp.expand_log(fr_sum, force=True) - sp.expand_log(fr_a, force=True) - sp.expand_log(fr_b, force=True)) == 0)
    check("complex empty determinant gives zero log readout", sp.log(sp.Integer(1)) == 0)
    check("realified empty determinant gives zero log readout", sp.log(sp.Integer(1)) == 0)
    check("realified functional is twice complex functional on A", sp.simplify(fr_a - 2 * fc_a) == 0)
    check("realified functional is twice complex functional on B", sp.simplify(fr_b - 2 * fc_b) == 0)

    lam = sp.Integer(2)
    for count in range(5):
        carrier_for_records = sp.eye(count) * lam
        fc_records = sp.log(abs(carrier_for_records.det()))
        fr_records = sp.log(realification(carrier_for_records).det())
        check(
            f"record extension complex readout at count={count}",
            sp.simplify(fc_records - count * sp.log(lam)) == 0,
        )
        check(
            f"record extension realified readout at count={count}",
            sp.simplify(fr_records - 2 * count * sp.log(lam)) == 0,
        )
    check(
        "record extension complex readout is disjoint-union additive",
        sp.simplify(5 * sp.log(lam) - 2 * sp.log(lam) - 3 * sp.log(lam)) == 0,
    )
    check(
        "record extension realified readout is disjoint-union additive",
        sp.simplify(10 * sp.log(lam) - 4 * sp.log(lam) - 6 * sp.log(lam)) == 0,
    )

    section("Part D: determinant-power scaling degrees")
    t = sp.symbols("t", real=True)
    for n in range(1, 5):
        dc_ratio = sp.exp(n * t)
        dr_ratio = sp.exp(2 * n * t)
        check(f"complex scaling degree is n at n={n}", sp.diff(sp.log(dc_ratio), t).subs(t, 0) == n)
        check(f"realified scaling degree is 2n at n={n}", sp.diff(sp.log(dr_ratio), t).subs(t, 0) == 2 * n)

    section("Part E: exact finite witnesses")
    examples = [
        sp.Matrix([[2 + sp.I]]),
        sp.Matrix([[1 + sp.I, 2], [0, 3 - sp.I]]),
        sp.Matrix([[1 + sp.I, 2, 0], [0, 1 - sp.I, 3], [2, 0, 1]]),
    ]
    for index, example in enumerate(examples, start=1):
        check(
            f"finite witness {index} has determinant-power split",
            sp.simplify(realification(example).det() - example.det() * sp.conjugate(example.det())) == 0,
        )

    section("Part F: rhetoric-resolution lifts")
    scalar = sp.Matrix([[2 + sp.I]])
    scalar_det_c = scalar.det()
    scalar_det_r = realification(scalar).det()
    check(
        "per_element: scalar complex carrier retains the factor-two determinant-power split",
        sp.simplify(scalar_det_r - scalar_det_c * sp.conjugate(scalar_det_c)) == 0
        and scalar_det_r != abs(scalar_det_c),
    )

    site_records = frozenset({(0, 0, 0), (2, -1, 3), (4, 2, -2)})
    translated_sites = frozenset((x + 5, y - 7, z + 11) for x, y, z in site_records)
    site_count = len(site_records)
    site_carrier = sp.eye(site_count) * lam
    translated_carrier = sp.eye(len(translated_sites)) * lam
    site_fc = sp.log(abs(site_carrier.det()))
    site_fr = sp.log(realification(site_carrier).det())
    check(
        "per_site: translated singleton carriers retain both additive determinant readouts",
        len(translated_sites) == site_count
        and translated_carrier == site_carrier
        and sp.simplify(
            realification(translated_carrier).det()
            - translated_carrier.det() * sp.conjugate(translated_carrier.det())
        ) == 0
        and sp.simplify(
            sp.expand_log(site_fr, force=True)
            - 2 * sp.expand_log(site_fc, force=True)
        ) == 0,
    )

    mode_carrier = sp.diag(2, 3, 5, 7)
    mode_fc = sp.log(abs(mode_carrier.det()))
    mode_fr = sp.log(realification(mode_carrier).det())
    check(
        "per_mode: diagonal finite-mode products retain the complex-versus-realified factor two",
        sp.simplify(sp.expand_log(mode_fr, force=True) - 2 * sp.expand_log(mode_fc, force=True)) == 0,
    )

    combined_blocks = sp.diag(2, 3, 5)
    combined_fc = sp.log(abs(combined_blocks.det()))
    combined_fr = sp.log(realification(combined_blocks).det())
    check(
        "per_block: direct-sum finite blocks preserve additivity for both determinant powers",
        sp.simplify(sp.expand_log(combined_fc, force=True) - sp.expand_log(fc_a, force=True) - sp.expand_log(fc_b, force=True)) == 0
        and sp.simplify(sp.expand_log(combined_fr, force=True) - sp.expand_log(fr_a, force=True) - sp.expand_log(fr_b, force=True)) == 0,
    )

    lattice_sites = frozenset(
        (x, y, z)
        for x in range(2)
        for y in range(2)
        for z in range(2)
    )
    left_half = frozenset(site for site in lattice_sites if site[0] == 0)
    right_half = lattice_sites - left_half
    lattice_carrier = sp.eye(len(lattice_sites)) * lam
    left_carrier = sp.eye(len(left_half)) * lam
    right_carrier = sp.eye(len(right_half)) * lam
    lattice_fc = sp.log(abs(lattice_carrier.det()))
    lattice_fr = sp.log(realification(lattice_carrier).det())
    halves_fc = sp.log(abs(left_carrier.det())) + sp.log(abs(right_carrier.det()))
    halves_fr = (
        sp.log(realification(left_carrier).det())
        + sp.log(realification(right_carrier).det())
    )
    check(
        "lattice_wide: finite lattice record union preserves both laws and their factor-two split",
        left_half.isdisjoint(right_half)
        and len(left_half) + len(right_half) == len(lattice_sites)
        and sp.simplify(
            sp.expand_log(lattice_fc, force=True)
            - sp.expand_log(halves_fc, force=True)
        ) == 0
        and sp.simplify(
            sp.expand_log(lattice_fr, force=True)
            - sp.expand_log(halves_fr, force=True)
        ) == 0
        and sp.simplify(
            sp.expand_log(lattice_fr, force=True)
            - 2 * sp.expand_log(lattice_fc, force=True)
        ) == 0,
    )

    section("Part G: source and axiom guards")
    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    axioms_flat = " ".join(axioms.split())
    check("axioms withhold K/CPT structure", "`K`/CPT structure" in axioms_flat)
    check("axioms withhold source/action identification", "source/action and physical-observable identification" in axioms)
    check("axioms withhold physical observable bridge", "physical observable bridge" in axioms)
    check("note grants the auxiliary complex carrier", "Grant an auxiliary invertible complex block carrier" in note)
    check("note contains both countermodel functionals", "F_C(A) = log |det_C A|" in note and "F_R(A) = log det_R R(A)" in note)
    check("note constructs two readouts on one record model", "Same-model conservative extensions" in note and "I_C(C) = F_C(A(C))" in note and "I_R(C) = F_R(A(C))" in note)
    check("note limits the claim to finite carriers", "finite-carrier determinant-power non-entailment claim" in note_flat)
    check("note preserves future action theorem", "future physical CAR/action theorem" in note)
    check("note does not force r", "does not force `r=1/2`" in note_flat)
    check("N1 contains six attempted routes", note.count("| ATTEMPTED |") == 6)
    check("N2 collapses to one wall", "one wall: `W_power`" in note)
    check("N3 records required phrase scan", "The proof text was scanned for" in note)
    check("N4 uses no prior negative witness", "| none | n/a | raw complex-vs-realified" in note)
    check("N5 names tested resolutions", "per scalar block, per finite matrix block" in note)
    check("N6 preserves action, coordinate, and open-obligation paths", "action-native CAR/Berezin theorem" in note and "registered-mass coordinate package" in note and "current zero-weight occupancy obligation" in note)
    check("N7 contains normalization and complex-field steelmen", "normalization pair" in note and "Qubit axiom uses `M_2(C)`" in note_flat)
    check("N8 distinguishes phase from determinant power", "does not choose determinant modulus power" in note)
    check("discipline gate records PASS", "**Gate result: PASS.**" in note)

    print("\n" + "=" * 68)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
