#!/usr/bin/env python3
"""J:attack-a:PR8170 — pattern (a) WITNESS REALIZABILITY.

Level-time formation on Z^3: 3 predecessors x-e_j exist; the 2d level plane
is Z^2; A(kappa)=coth kappa - 1/kappa has A'(0)=1/3. Do not re-find the
exponents-vs-gamma HIT.
"""
from __future__ import annotations

import sympy as sp

HITS = []


def main():
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    x = (0, 0, 0)
    preds = [tuple(x[i] - e[j][i] for i in range(3)) for j in range(3)]
    print(f"predecessors of origin: {preds}")
    if len(set(preds)) != 3:
        HITS.append("not 3 distinct predecessors")
    # Z^3 NN bipartite
    print("Z^3 NN is bipartite (no triangles)")
    k = sp.symbols("k", positive=True)
    A = 1 / sp.tanh(k) - 1 / k
    series = A.series(k, 0, 4).removeO()
    print(f"A(k) series {series}")
    # A = k/3 + O(k^3)
    coeff = series.coeff(k)
    print(f"A'(0)={coeff} stated 1/3")
    if coeff != sp.Rational(1, 3):
        HITS.append(f"A'(0)={coeff}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the 3-predecessor "
        "stencil exists in Z^3, the level plane is Z^2, and A'(0)=1/3; not a "
        "re-find of the exponents-vs-gamma HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
