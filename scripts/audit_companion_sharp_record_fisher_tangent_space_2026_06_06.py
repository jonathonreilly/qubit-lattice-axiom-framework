#!/usr/bin/env python3
"""Exact finite sharp-record Fisher tangent theorem.

No physical source semantics, no Y_T closure, no fitted data. This runner
checks only finite probability/Radon-Nikodym/Fisher geometry.
"""

from __future__ import annotations

import sys
import sympy as sp


RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")


def part_1_probability_coordinates() -> None:
    print("\n[Part 1] probability-coordinate RN score")
    p1, p2, a, b = sp.symbols("p1 p2 a b", positive=True, real=True)
    p3 = 1 - p1 - p2
    dp = sp.Matrix([a, b, -a - b])
    p = sp.Matrix([p1, p2, p3])
    s = sp.Matrix([sp.simplify(dp[i] / p[i]) for i in range(3)])
    mean = sp.simplify(sum(p[i] * s[i] for i in range(3)))
    fisher = sp.simplify(sum(p[i] * s[i] ** 2 for i in range(3)))
    expected = sp.simplify(a**2 / p1 + b**2 / p2 + (a + b) ** 2 / p3)
    record("probability tangent dp sums to zero", sp.simplify(sum(dp)) == 0)
    record("RN score has zero P0-mean", mean == 0, f"mean={mean}")
    record("Fisher norm is sum dp_i^2/p_i", sp.simplify(fisher - expected) == 0, f"norm={fisher}")


def part_2_exponential_chart() -> None:
    print("\n[Part 2] normalized exponential chart")
    h = sp.symbols("h", real=True)
    p = [sp.Rational(1, 5), sp.Rational(3, 10), sp.Rational(1, 2)]
    o0, o1 = sp.symbols("o0 o1", real=True)
    # Choose o2 so E_0[O]=0 exactly.
    o2 = sp.simplify(-(p[0] * o0 + p[1] * o1) / p[2])
    o = [o0, o1, o2]
    mean_o = sp.simplify(sum(p[i] * o[i] for i in range(3)))
    w = sp.log(sum(p[i] * sp.exp(h * o[i]) for i in range(3)))
    r = [sp.exp(h * o[i] - w) for i in range(3)]
    norm = sp.simplify(sum(p[i] * r[i] for i in range(3)))
    score = [sp.simplify(sp.diff(sp.log(r[i]), h).subs(h, 0)) for i in range(3)]
    record("constructed score O has zero reference mean", mean_o == 0)
    record("exponential chart normalizes E_0[R_h]=1", sp.simplify(norm - 1) == 0)
    record("origin score of exponential chart is O", all(sp.simplify(score[i] - o[i]) == 0 for i in range(3)))


def part_3_two_outcome_signed_record() -> None:
    print("\n[Part 3] two-outcome sharp signed record")
    lam = sp.symbols("lambda", positive=True, real=True)
    p = [sp.Rational(1, 2), sp.Rational(1, 2)]
    eps = [sp.Integer(1), sp.Integer(-1)]
    mean = sp.simplify(sum(p[i] * eps[i] for i in range(2)))
    norm = sp.simplify(sum(p[i] * eps[i] ** 2 for i in range(2)))
    scaled = sp.simplify(sum(p[i] * (lam * eps[i]) ** 2 for i in range(2)))
    dp = [sp.simplify(p[i] * eps[i]) for i in range(2)]
    record("E_0[epsilon]=0", mean == 0)
    record("E_0[epsilon^2]=1", norm == 1)
    record("primitive signed score corresponds to dp=(1/2,-1/2)", dp == [sp.Rational(1, 2), sp.Rational(-1, 2)])
    record("lambda epsilon has Fisher norm lambda^2", sp.simplify(scaled - lam**2) == 0, f"norm={scaled}")
    record("unit scaled signed tangent selects lambda=1", sp.solve(sp.Eq(scaled, 1), lam) == [1])


def main() -> int:
    print("=" * 78)
    print("Sharp-record Fisher tangent theorem")
    print("Finite probability geometry only.")
    print("=" * 78)
    part_1_probability_coordinates()
    part_2_exponential_chart()
    part_3_two_outcome_signed_record()

    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    n_fail = sum(1 for _, ok, _ in RESULTS if not ok)
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for name, ok, detail in RESULTS:
        suffix = f" ({detail})" if detail else ""
        print(f"  {'PASS' if ok else 'FAIL'} {name}{suffix}")
    print(f"\nTOTAL: {n_pass} PASS / {n_fail} FAIL")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
