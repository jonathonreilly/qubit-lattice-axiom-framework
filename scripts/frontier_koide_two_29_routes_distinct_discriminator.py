#!/usr/bin/env python3
"""The two Koide-phase 2/9 routes are DISTINCT, coinciding only at d=3.

Two index/anomaly objects both evaluate to 2/9 at the framework's d=3:
  * APS equivariant eta-defect of the C_d rotation with transverse weights
    (1, d-1) -- the geometric route (this session's APS-eta route, PR #1807);
  * Callan-Harvey hypercharge-cubed anomaly Tr[Y^3]_{Q_L} per generation -- the
    anomaly-inflow route (other worker's PR #1805).

A natural temptation is to treat them as "the same 2/9 from two sides of one
index theorem" and so as a single shared normalization residual. This
discriminator tests that and finds it FALSE: they are different functions of d
and coincide only at d=3.

  eta_defect(1, d-1; d)  =  (d^2 - 1) / (12 d)        [geometric, rotation order d]
  Tr[Y^3]_{Q_L}          =  2 N_c (1/N_c)^3 = 2/d^2   [anomaly, color rank d]

Equality  (d^2-1)/(12d) = 2/d^2  <=>  d^3 - d = 24  <=>  d = 3 (unique real root).

Honest consequence: the two routes are NOT one object; they are independent,
each carrying its own normalization residual. Their agreement is a consistency
that holds uniquely at the framework's (independently retained) d = 3 -- a
coincidence/consistency, NOT a derivation of d=3 and NOT a single shared 2/9.

Pure finite arithmetic. No PDG / fitted / scale input. Asserts no audit status.
"""

from __future__ import annotations

import cmath
import math

import numpy as np

TOL = 1.0e-9
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


def eta_defect(d):
    """APS equivariant eta-defect of C_d with transverse weights (1, d-1)."""
    z = cmath.exp(2j * math.pi / d)
    s = 0j
    for k in range(1, d):
        s += 1 / ((z ** k - 1) * (z ** (k * (d - 1)) - 1))
    return (s / d).real


def eta_closed(d):
    return (d * d - 1) / (12 * d)


def anomaly(d):
    """Tr[Y^3]_{Q_L} per generation = 2 N_c (1/N_c)^3 = 2/d^2  (color rank d)."""
    return 2 / d ** 2


def main() -> int:
    print("=" * 76)
    print("TWO KOIDE-PHASE 2/9 ROUTES ARE DISTINCT (COINCIDE ONLY AT d=3)")
    print("=" * 76)

    # (1) closed form for the APS eta-defect, verified against the sum
    print("\n" + "-" * 76)
    print("(1) APS eta-defect(1,d-1;d) = (d^2-1)/(12 d), verified d=2..7")
    print("-" * 76)
    for d in range(2, 8):
        check(f"eta_defect({d}) = (d^2-1)/(12d)",
              abs(eta_defect(d) - eta_closed(d)) < TOL,
              detail=f"{eta_defect(d):.6f}")

    # (2) the two routes agree at d=3, disagree elsewhere
    print("\n" + "-" * 76)
    print("(2) eta-defect vs anomaly 2/d^2: agree at d=3 only")
    print("-" * 76)
    for d in range(2, 8):
        e, a = eta_closed(d), anomaly(d)
        same = abs(e - a) < TOL
        check(f"d={d}: eta-defect={e:.4f}, anomaly={a:.4f} -> {'AGREE' if same else 'differ'}",
              same == (d == 3))
    check("both equal 2/9 exactly at d=3",
          abs(eta_closed(3) - 2 / 9) < TOL and abs(anomaly(3) - 2 / 9) < TOL)

    # (3) equality <=> d^3 - d = 24 <=> d = 3 (unique real root)
    print("\n" + "-" * 76)
    print("(3) equality (d^2-1)/(12d) = 2/d^2  <=>  d^3 - d = 24  <=>  d = 3")
    print("-" * 76)
    for d in range(2, 8):
        check(f"d={d}: d^3-d = {d**3 - d}  (==24 iff d=3)", (d**3 - d == 24) == (d == 3))
    roots = np.roots([1, 0, -1, -24])
    realroots = sorted(round(r.real, 6) for r in roots if abs(r.imag) < 1e-9)
    check("d^3 - d - 24 = 0 has unique real root d = 3", realroots == [3.0],
          detail=f"real roots = {realroots}")

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  THE TWO 2/9 ROUTES ARE DISTINCT -- NOT ONE SHARED OBJECT.\n"
            "  * geometric APS eta-defect (rotation order d): (d^2-1)/(12 d);\n"
            "  * hypercharge-cubed anomaly (color rank d):     2/d^2.\n"
            "  These are different functions of d. They coincide exactly at d=3\n"
            "  (= 2/9), and d=3 is the UNIQUE real root of d^3 - d = 24.\n\n"
            "  Honest consequences:\n"
            "   * PR #1807 (APS-eta) and PR #1805 (Callan-Harvey anomaly) are NOT\n"
            "     two views of one index-theory object; they are independent\n"
            "     routes, each with its own normalization residual. They must not\n"
            "     be treated as mutually-confirming the same 2/9.\n"
            "   * their agreement is a consistency at the framework's independently\n"
            "     retained d=3 (color rank N_c=3 = rotation order of C_3[111]); it\n"
            "     is a coincidence/consistency, NOT a derivation of d=3, and NOT a\n"
            "     single shared 2/9.\n"
            "   * the delta-closure still needs a normalization coefficient on EACH\n"
            "     route separately; getting one does not get the other for free.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
