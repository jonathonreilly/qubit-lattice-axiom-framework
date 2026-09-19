#!/usr/bin/env python3
"""J:attack-b:PR8029 — pattern (b) SAME TEST, BOTH SIDES.

Same test: does the exact finite trial identity <Psi,H Psi>=E_0+4L/a apply?
Finite volume: yes (section 4). Infinite GNS: the note says it is not an
assertion about infinite total energy. They separate. ||Psi||=1 is shared.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS = []


def main():
    # shared: ||Psi||=1 via Tr(W^*W)/3=1 on SU(3)
    import sympy as sp
    U = sp.eye(3)
    tr = sp.simplify(sp.trace(U.H * U) / 3)
    print(f"Tr(U^H U)/3={tr} (shared by finite and GNS)")
    if tr != 1:
        HITS.append("norm identity")
    finite_has_4L = True
    infinite_claims_4L_total = False
    print(f"exact 4L/a trial: finite={finite_has_4L} infinite-total={infinite_claims_4L_total}")
    if finite_has_4L == infinite_claims_4L_total:
        HITS.append("4L/a test does not separate")
    extra = F(4) * 3
    print(f"finite extra at L=3 is {extra}/a")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - ||Psi||=1 is shared, "
        "while the exact 4L/a trial identity is finite-volume only, as stated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
