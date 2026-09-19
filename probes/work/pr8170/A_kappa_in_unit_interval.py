#!/usr/bin/env python3
"""J:attack-d:PR8170 — QUANTIFIER SCOPE on Langevin A(kappa)=coth kappa - 1/kappa.

Typical block-26 claim: 0 < A(kappa) < 1 for every kappa>0 (gain < 1 off
the aligned direction). HIT if A<=0 or A>=1 at a positive kappa.
Not the known executed-exponent-below-gamma HIT.
"""
from __future__ import annotations

import sympy as sp

k = sp.symbols("kappa", positive=True)
A = sp.coth(k) - 1 / k
# A = (k coth k - 1)/k; k coth k > 1 for k>0
diff = sp.simplify(sp.series(k * sp.coth(k) - 1, k, 0, 6).removeO())


def main():
    hits = []
    print(f"series k coth k - 1 = {diff}")
    pts = [sp.Rational(1, 100), sp.Rational(1, 10), 1, 2, 5, 10, 30]
    for p in pts:
        val = A.subs(k, p).evalf(40)
        print(f"A({p})={val}")
        if val <= 0 or val >= 1:
            hits.append(f"A({p})={val} not in (0,1)")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8170): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on 0<A(kappa)<1 for kappa>0 (PR #8170): "
            "holds at the tested positive kappas; no in-range failure of the "
            "Langevin bound (known exponent-vs-gamma HIT not re-found)"
        )


if __name__ == "__main__":
    main()
