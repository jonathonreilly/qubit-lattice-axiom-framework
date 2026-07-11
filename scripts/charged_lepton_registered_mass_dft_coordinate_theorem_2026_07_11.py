#!/usr/bin/env python3
"""Exact checks for registered positive-mass C3 Fourier coordinates."""

from __future__ import annotations

import itertools
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md"

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


def coords(values: tuple[float, float, float]) -> tuple[float, complex, float]:
    omega = complex(-0.5, math.sqrt(3) / 2)
    a = sum(values) / 3
    c = (values[0] + omega**2 * values[1] + omega * values[2]) / 3
    r = abs(c) ** 2 / a**2
    return a, c, r


def fold_phase(phi: float) -> float:
    period = 2 * math.pi / 3
    representative = (phi + period / 2) % period - period / 2
    return abs(representative)


def main() -> int:
    print("Registered positive-mass C3 Fourier coordinate theorem")
    print("=" * 68)

    z0, z1, z2 = sp.symbols("z0 z1 z2", real=True, positive=True)
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    a = sp.simplify((z0 + z1 + z2) / 3)
    c = sp.simplify((z0 + omega**2 * z1 + omega * z2) / 3)
    cbar = sp.conjugate(c)
    zs = (z0, z1, z2)

    section("Part A: inverse C3 Fourier transform")
    check("omega has exact order three", sp.simplify(omega**3 - 1) == 0 and sp.simplify(1 + omega + omega**2) == 0)
    for j, zj in enumerate(zs):
        reconstructed = sp.simplify(a + c * omega**j + cbar * omega ** (-j))
        check(f"inverse transform reconstructs z{j}", sp.simplify(reconstructed - zj) == 0)
    check("Fourier mean is positive on a positive triple", a.is_positive is True)
    c_cycle = sp.simplify((z1 + omega**2 * z2 + omega * z0) / 3)
    c_reflection = sp.simplify((z0 + omega**2 * z2 + omega * z1) / 3)
    check("generating cycle sends c to omega c", sp.simplify(c_cycle - omega * c) == 0)
    check("generating reflection sends c to conjugate(c)", sp.simplify(c_reflection - cbar) == 0)

    section("Part B: symmetric r coordinate")
    abs_c_sq = sp.simplify(c * cbar)
    variance_sum = sp.simplify(sum((zj - a) ** 2 for zj in zs))
    check("variance identity is 6|c|^2", sp.simplify(variance_sum - 6 * abs_c_sq) == 0)
    r_fourier = sp.simplify(abs_c_sq / a**2)
    r_symmetric = sp.simplify(variance_sum / (6 * a**2))
    check("Fourier and symmetric formulas for r agree", sp.simplify(r_fourier - r_symmetric) == 0)
    scale = sp.symbols("scale", real=True, positive=True)
    r_scaled = sp.simplify(r_symmetric.subs({z0: scale * z0, z1: scale * z1, z2: scale * z2}))
    check("r is common-scale invariant", sp.simplify(r_scaled - r_symmetric) == 0)
    swap = sp.simplify(r_symmetric.xreplace({z0: z1, z1: z0}))
    check("r is invariant under a generating transposition", sp.simplify(swap - r_symmetric) == 0)
    cycle_r = sp.simplify(r_symmetric.xreplace({z0: z1, z1: z2, z2: z0}))
    check("r is invariant under a generating cycle", sp.simplify(cycle_r - r_symmetric) == 0)

    section("Part C: Koide identity")
    sum_sq = sp.simplify(sum(zj**2 for zj in zs))
    check("Parseval identity", sp.simplify(sum_sq - 3 * (a**2 + 2 * abs_c_sq)) == 0)
    q = sp.simplify(sum_sq / (z0 + z1 + z2) ** 2)
    check("Q equals 1/3+2r/3", sp.simplify(q - (sp.Rational(1, 3) + 2 * r_fourier / 3)) == 0)
    r_symbol = sp.symbols("r", real=True, nonnegative=True)
    q_of_r = sp.Rational(1, 3) + 2 * r_symbol / 3
    check("r=1/2 implies Q=2/3", q_of_r.subs(r_symbol, sp.Rational(1, 2)) == sp.Rational(2, 3))
    check("Q=2/3 has r=1/2", sp.solve(sp.Eq(q_of_r, sp.Rational(2, 3)), r_symbol) == [sp.Rational(1, 2)])
    check("Koide equivalence does not fix phase", not q_of_r.has(sp.Symbol("phi")))

    section("Part D: folded phase and unordered reconstruction")
    values = (1.0, 2.0, 4.0)
    a_num, c_num, r_num = coords(values)
    delta = fold_phase(math.atan2(c_num.imag, c_num.real))
    permutation_data = []
    for permuted in itertools.permutations(values):
        a_p, c_p, r_p = coords(permuted)
        delta_p = fold_phase(math.atan2(c_p.imag, c_p.real))
        permutation_data.append((a_p, r_p, delta_p))
    check("a is invariant under every permutation", all(math.isclose(item[0], a_num, abs_tol=1e-12) for item in permutation_data))
    check("r is invariant under every permutation", all(math.isclose(item[1], r_num, abs_tol=1e-12) for item in permutation_data))
    check("folded phase is invariant under every permutation", all(math.isclose(item[2], delta, abs_tol=1e-12) for item in permutation_data))
    phi = math.atan2(c_num.imag, c_num.real)
    reconstructed = tuple(a_num + 2 * abs(c_num) * math.cos(phi + 2 * math.pi * j / 3) for j in range(3))
    check("inverse cosine formula reconstructs ordered roots", all(math.isclose(x, y, abs_tol=1e-12) for x, y in zip(reconstructed, values)))
    reconstructed_folded = tuple(a_num + 2 * abs(c_num) * math.cos(delta + 2 * math.pi * j / 3) for j in range(3))
    check("folded phase reconstructs the unordered roots", all(math.isclose(x, y, abs_tol=1e-12) for x, y in zip(sorted(reconstructed_folded), sorted(values))))
    check("folded phase lies in [0,pi/3]", 0 <= delta <= math.pi / 3)
    boundary_values = (2.0, 1.0, 2.0)
    boundary_deltas = []
    for permuted in itertools.permutations(boundary_values):
        _, c_boundary, _ = coords(permuted)
        boundary_deltas.append(fold_phase(math.atan2(c_boundary.imag, c_boundary.real)))
    check("fold boundary is permutation invariant", all(math.isclose(item, math.pi / 3, abs_tol=1e-12) for item in boundary_deltas))
    check("both fold-boundary representatives give pi/3", math.isclose(fold_phase(math.pi / 3), math.pi / 3, abs_tol=1e-12) and math.isclose(fold_phase(-math.pi / 3), math.pi / 3, abs_tol=1e-12))
    masses = (1.0, 4.0, 16.0)
    scaled_masses = tuple(7.0 * mass for mass in masses)
    _, _, r_masses = coords(tuple(math.sqrt(mass) for mass in masses))
    _, _, r_scaled_masses = coords(tuple(math.sqrt(mass) for mass in scaled_masses))
    check("r is invariant under common positive mass scaling", math.isclose(r_masses, r_scaled_masses, abs_tol=1e-12))
    equal_a, equal_c, equal_r = coords((3.0, 3.0, 3.0))
    check("degenerate triple has c=0 and r=0", math.isclose(abs(equal_c), 0.0, abs_tol=1e-12) and math.isclose(equal_r, 0.0, abs_tol=1e-12) and equal_a == 3.0)
    equal_reconstruction_a = tuple(equal_a + 2 * abs(equal_c) * math.cos(0.17 + 2 * math.pi * j / 3) for j in range(3))
    equal_reconstruction_b = tuple(equal_a + 2 * abs(equal_c) * math.cos(1.91 + 2 * math.pi * j / 3) for j in range(3))
    check(
        "c=0 reconstruction is phase independent",
        all(math.isclose(x, equal_a, abs_tol=1e-12) for x in equal_reconstruction_a + equal_reconstruction_b),
    )

    section("Scope guards")
    note = NOTE.read_text(encoding="utf-8")
    check("source requires an independently defined mass functional", "independently defined registered-mass functional" in note)
    check("source says primitive is not a mathematical premise", "does not use that primitive as a mathematical premise" in note)
    check("source does not retire owner atoms", "does not retire AC(i) or AC(ii)" in note)
    check("source does not force r", "does not force `r=1/2`" in note)
    check("source excludes observed comparators", "No observed mass table, fit, comparator" in note)

    print("\n" + "=" * 68)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
