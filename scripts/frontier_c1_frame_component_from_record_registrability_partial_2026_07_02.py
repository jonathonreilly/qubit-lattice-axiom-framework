#!/usr/bin/env python3
"""Exact witnesses for the C1/R* partial registrability note."""

from __future__ import annotations

import sys
from fractions import Fraction

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" -- {detail}" if detail else ""))


def vec_equal(u: sp.Matrix, v: sp.Matrix) -> bool:
    return all(sp.simplify(a - b) == 0 for a, b in zip(u, v))


def main() -> int:
    sqrt2 = sp.sqrt(2)
    H = sp.Matrix([[1 / sqrt2, 1 / sqrt2], [1 / sqrt2, -1 / sqrt2]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)

    # T1: imported-basis orbit witness for S2.
    v_equal = sp.Matrix([1, 1])
    Hv_equal = sp.simplify(H * v_equal)
    check(
        "T1 Hadamard sends (1,1) to (sqrt(2),0)",
        vec_equal(Hv_equal, sp.Matrix([sqrt2, 0])),
        str(Hv_equal),
    )
    s2_before = sp.simplify(v_equal[0] ** 2 - v_equal[1] ** 2)
    s2_after = sp.simplify(Hv_equal[0] ** 2 - Hv_equal[1] ** 2)
    check("T1 S2 verdict true in original imported basis", s2_before == 0)
    check("T1 S2 verdict false in Hadamard imported basis", s2_after != 0)
    check("T1 S2 verdicts differ on same vector orbit", (s2_before == 0) != (s2_after == 0))

    # T2: supplied S1 algebraic partition data for N=3.
    N = 3
    I3 = sp.eye(N)
    J3 = sp.ones(N)
    B3 = J3 - I3
    hs = lambda A, B: sp.trace(A.T * B)
    norm_I = hs(I3, I3)
    norm_B = hs(B3, B3)
    ip_IB = hs(I3, B3)
    check("T2 ||I||^2 = 3", norm_I == 3)
    check("T2 ||B||^2 = 6", norm_B == 6)
    check("T2 <I,B> = 0", ip_IB == 0)
    r_s1 = Fraction(norm_I, norm_B)
    check("T2 S1 equal HS energy gives r=1/2", r_s1 == Fraction(1, 2), str(r_s1))

    mixed_1 = (I3 + B3) / sqrt2
    mixed_2 = (I3 - B3) / sqrt2
    check("T2 Hadamard first mixed cell is not unit", mixed_1 != I3)
    check("T2 Hadamard second mixed cell not HS-orthogonal to unit", sp.simplify(hs(I3, mixed_2)) != 0)

    # T3: S3 is Y/spectral-data dependent and orbit-constant under imported bases.
    t = -2 + sp.Rational(3, 2) * sqrt2
    Y3 = I3 + t * B3
    lam0 = 1 + 2 * t
    lam1 = 1 - t
    s3_relation = sp.simplify(lam0**2 - 2 * lam1**2)
    r_s3 = sp.simplify(t**2)
    check("T3 parent S3 spectral relation holds", s3_relation == 0)
    check("T3 S3 r equals 17/2 - 6*sqrt(2)", sp.simplify(r_s3 - (sp.Rational(17, 2) - 6 * sqrt2)) == 0)
    r_from_trace = sp.simplify(
        (sp.trace(Y3.T * Y3) - 3 * (sp.trace(Y3) / 3) ** 2)
        / (6 * (sp.trace(Y3) / 3) ** 2)
    )
    check("T3 trace formula recovers S3 r", sp.simplify(r_from_trace - r_s3) == 0)
    P3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Y3_rebased = sp.simplify(P3.T * Y3 * P3)
    r_rebased = sp.simplify(
        (sp.trace(Y3_rebased.T * Y3_rebased) - 3 * (sp.trace(Y3_rebased) / 3) ** 2)
        / (6 * (sp.trace(Y3_rebased) / 3) ** 2)
    )
    check("T3 S3 trace value is unchanged by imported-basis relabeling", sp.simplify(r_rebased - r_from_trace) == 0)

    # T4: exact finite subgroup average collapses per-mode squares to total energy.
    generators = [H, Z]
    group: list[sp.Matrix] = [I2]
    changed = True
    while changed:
        changed = False
        for g in list(group):
            for gen in generators:
                candidate = sp.simplify(g * gen)
                if not any(candidate.equals(existing) for existing in group):
                    group.append(candidate)
                    changed = True

    check("T4 Hadamard/sign subgroup has 16 elements", len(group) == 16, str(len(group)))
    check("T4 every subgroup element is orthogonal", all(sp.simplify(g.T * g - I2) == sp.zeros(2) for g in group))

    x, y = sp.symbols("x y", real=True)
    v = sp.Matrix([x, y])
    avg_first = sp.simplify(sum((g * v)[0] ** 2 for g in group) / len(group))
    avg_second = sp.simplify(sum((g * v)[1] ** 2 for g in group) / len(group))
    invariant_half = (x**2 + y**2) / 2
    check("T4 averaged first per-mode square is invariant total/2", sp.simplify(avg_first - invariant_half) == 0)
    check("T4 averaged second per-mode square is invariant total/2", sp.simplify(avg_second - invariant_half) == 0)
    check("T4 averaged S2 split is equal by construction", sp.simplify(avg_first - avg_second) == 0)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
