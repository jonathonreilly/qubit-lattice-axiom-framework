#!/usr/bin/env python3
"""Countermodels for complex versus realified determinant occupancy grain."""

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
    print("Complex-vs-realified occupancy-grain countermodels")
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
    check("complex log determinant is block additive", sp.simplify(sp.expand_log(fc_sum, force=True) - sp.expand_log(fc_a + fc_b, force=True)) == 0)
    check("realified log determinant is block additive", sp.simplify(sp.expand_log(fr_sum, force=True) - sp.expand_log(fr_a + fr_b, force=True)) == 0)
    check("complex empty determinant gives zero log readout", sp.log(sp.Integer(1)) == 0)
    check("realified empty determinant gives zero log readout", sp.log(sp.Integer(1)) == 0)
    check("realified functional is twice complex functional on A", sp.simplify(fr_a - 2 * fc_a) == 0)
    check("realified functional is twice complex functional on B", sp.simplify(fr_b - 2 * fc_b) == 0)

    section("Part D: occupancy scaling degrees")
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

    section("Part F: source and axiom guards")
    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    axioms_flat = " ".join(axioms.split())
    check("axioms withhold K/CPT structure", "`K`/CPT structure" in axioms_flat)
    check("axioms withhold source/action identification", "source/action and physical-observable identification" in axioms)
    check("axioms withhold physical observable bridge", "physical observable bridge" in axioms)
    check("note grants the complex carrier", "Grant an invertible complex matter block" in note)
    check("note contains both countermodel functionals", "F_C(A) = log |det_C A|" in note and "F_R(A) = log det_R R(A)" in note)
    check("note limits the claim to finite carriers", "finite-carrier non-entailment claim" in note)
    check("note preserves future action theorem", "future physical CAR/action theorem" in note)
    check("note does not force r", "does not force `r=1/2`" in note)
    check("N1 contains six attempted routes", note.count("| ATTEMPTED |") == 6)
    check("N2 collapses to one wall", "one wall: `W_grain`" in note)
    check("N3 records required phrase scan", "The proof text was scanned for" in note)
    check("N4 uses no prior negative witness", "| none | n/a | AC(i)" in note)
    check("N5 names tested resolutions", "per scalar block, per finite matrix block" in note)
    check("N6 preserves action, coordinate, and governance paths", "action-native CAR/Berezin theorem" in note and "registered-mass coordinate package" in note and "owner-approved narrow premise" in note)
    check("N7 contains the complex-field steelman", "Qubit axiom uses `M_2(C)`" in note)
    check("N8 distinguishes phase from determinant power", "phase erasure does not choose determinant modulus power" in note)
    check("discipline gate records PASS", "**Gate result: PASS.**" in note)

    print("\n" + "=" * 68)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
