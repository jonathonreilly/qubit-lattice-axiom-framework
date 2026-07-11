#!/usr/bin/env python3
"""Exact checks for complex versus realified determinant power."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md"

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


def gr_mul(p: dict[int, sp.Expr], q: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            inversions = 0
            bits = m2
            while bits:
                low = bits & -bits
                bit = low.bit_length() - 1
                inversions += (m1 >> (bit + 1)).bit_count()
                bits ^= low
            sign = -1 if inversions % 2 else 1
            mask = m1 | m2
            out[mask] = sp.simplify(out.get(mask, 0) + sign * c1 * c2)
    return {mask: value for mask, value in out.items() if value != 0}


def berezin_top_coefficient(k_mat: list[list[sp.Expr]]) -> sp.Expr:
    """Coefficient for exp(-chibar K chi) in chi_1,chibar_1,... order."""
    n = len(k_mat)
    action: dict[int, sp.Expr] = {}
    for i in range(n):
        for j in range(n):
            # Generator order is chi_1,chibar_1,...,chi_n,chibar_n.
            chi = 2 * j
            chibar = 2 * i + 1
            mask = (1 << chi) | (1 << chibar)
            sign = -1 if chibar > chi else 1
            action[mask] = sp.simplify(action.get(mask, 0) - sign * k_mat[i][j])

    exponential: dict[int, sp.Expr] = {0: sp.Integer(1)}
    power: dict[int, sp.Expr] = {0: sp.Integer(1)}
    factorial = sp.Integer(1)
    for degree in range(1, n + 1):
        power = gr_mul(power, action)
        factorial *= degree
        for mask, value in power.items():
            exponential[mask] = sp.simplify(
                exponential.get(mask, 0) + value / factorial
            )
    return sp.simplify(exponential.get((1 << (2 * n)) - 1, 0))


def main() -> int:
    print("Complex determinant and realification determinant power")
    print("=" * 64)

    section("Part A: generic realification identity")
    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h", real=True)
    k = sp.Matrix([[a + sp.I * b, c + sp.I * d], [e + sp.I * f, g + sp.I * h]])
    rk = realification(k)
    det_c = sp.expand(k.det())
    det_r = sp.expand(rk.det())
    abs_sq = sp.expand(det_c * sp.conjugate(det_c))
    check("generic 2x2 determinant identity", sp.simplify(det_r - abs_sq) == 0)
    check("realified determinant is real", sp.simplify(sp.im(det_r)) == 0)

    x, y, lam = sp.symbols("x y lam", real=True)
    z = x + sp.I * y
    rz = realification(sp.Matrix([[z]]))
    check("scalar realification gives x^2+y^2", sp.simplify(rz.det() - x**2 - y**2) == 0)
    check("singular scalar is included", realification(sp.Matrix([[0]])).det() == 0)
    check(
        "complex determinant scales to first power per complex mode",
        sp.simplify((lam * sp.Matrix([[z]])).det() - lam * z) == 0,
    )
    check(
        "realified determinant scales to second power per complex mode",
        sp.simplify(realification(lam * sp.Matrix([[z]])).det() - lam**2 * rz.det()) == 0,
    )

    section("Part B: exact finite examples")
    diagonal = sp.diag(1 + sp.I, 2 - sp.I)
    check(
        "diagonal 2x2 example",
        realification(diagonal).det()
        == sp.simplify(diagonal.det() * sp.conjugate(diagonal.det())),
    )
    exact3 = sp.Matrix([[1 + sp.I, 2, 0], [0, 1 - sp.I, 3], [2, 0, 1]])
    check(
        "exact 3x3 example",
        sp.simplify(
            realification(exact3).det()
            - exact3.det() * sp.conjugate(exact3.det())
        )
        == 0,
    )
    singular2 = sp.Matrix([[1 + sp.I, 2], [2 + 2 * sp.I, 4]])
    check("singular 2x2 example has both determinants zero", singular2.det() == 0 and realification(singular2).det() == 0)
    check(
        "multiplication by i changes the complex determinant phase in odd size",
        sp.det(sp.I * exact3) == -sp.I * exact3.det(),
    )
    check(
        "multiplication by i leaves the realified determinant unchanged",
        sp.simplify(realification(sp.I * exact3).det() - realification(exact3).det()) == 0,
    )

    section("Part C: Berezin first power")
    k0 = sp.Symbol("k0")
    scalar_top = berezin_top_coefficient([[k0]])
    check("generic 1x1 top coefficient is det_C(K)", scalar_top == k0, scalar_top)

    k00, k01, k10, k11 = sp.symbols("k00 k01 k10 k11")
    entries = [[k00, k01], [k10, k11]]
    top = berezin_top_coefficient(entries)
    expected = sp.Matrix(entries).det()
    check("generic 2x2 top coefficient is det_C(K)", sp.simplify(top - expected) == 0, top)
    check("Berezin result has first determinant power", sp.Poly(top, k00, k01, k10, k11).total_degree() == 2)

    entries3 = [
        [sp.Symbol(f"q{i}{j}") for j in range(3)]
        for i in range(3)
    ]
    top3 = berezin_top_coefficient(entries3)
    expected3 = sp.Matrix(entries3).det()
    check("generic 3x3 top coefficient is det_C(K)", sp.simplify(top3 - expected3) == 0)

    section("Scope guards")
    note = NOTE.read_text(encoding="utf-8")
    former_links = (
        "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md",
        "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
        "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md",
    )
    check("source note has no load-bearing links to former context stack", all(link not in note for link in former_links))
    check("source excludes a physical occupancy selector", "does not select a\nK/CPT-orbit occupancy grain" in note)
    check("source does not force r=1/2", "force `r=1/2`" in note)

    print("\n" + "=" * 64)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
