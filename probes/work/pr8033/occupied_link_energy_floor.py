#!/usr/bin/env python3
"""J:attack-g:PR8033 — brute-force the charged free-floor energy identity.

Note §3: one-link electric energies are [p^2 + pq + q^2 + 3p + 3q]/a for the
SU(3) irrep (p,q) in the cutoff p+q <= R; every occupied (nontrivial) link has
energy at least 4/a even at finite R, attained at (1,0) and (0,1), both present
for every R>=1; hence a charged block connecting endpoints at distance d has
free floor at least 4d/a.

Enumerate all (p,q) in the cutoff for R=1..16. HIT if the minimum over
nontrivial irreps is not 4, or if (1,0) or (0,1) is missing for some R>=1.
"""
from __future__ import annotations


def C(p: int, q: int) -> int:
    return p * p + p * q + q * q + 3 * p + 3 * q


def main() -> None:
    bad = []
    for R in range(1, 17):
        irreps = [(p, q) for p in range(R + 1) for q in range(R + 1 - p)]
        nontrivial = [(p, q) for p, q in irreps if (p, q) != (0, 0)]
        vals = { (p, q): C(p, q) for p, q in nontrivial }
        m = min(vals.values())
        mins = [pq for pq, v in vals.items() if v == m]
        has10 = (1, 0) in vals
        has01 = (0, 1) in vals
        print(f"R={R} n_irreps={len(irreps)} minC={m} at {sorted(mins)}")
        if m != 4:
            bad.append(f"R={R} min={m} != 4")
        if not (has10 and has01 and C(1, 0) == 4 and C(0, 1) == 4):
            bad.append(f"R={R} (1,0)/(0,1) missing or not 4")
        if set(mins) != {(1, 0), (0, 1)}:
            bad.append(f"R={R} min attained at {sorted(mins)} not just (1,0),(0,1)")
        # C = (p+q)(p+q+3) - pq  (nonnegative integers)
        for p, q in irreps:
            if C(p, q) != (p + q) * (p + q + 3) - p * q:
                bad.append(f"algebra C({p},{q})")
    if bad:
        print("HIT: occupied-link energy floor " + "; ".join(bad[:6]))
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on the finite-R occupied-link "
            "energy [p^2+pq+q^2+3p+3q]/a >= 4/a (PR #8033): "
            + "; ".join(bad[:4])
        )
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on the finite-R occupied-link "
            "energy [p^2+pq+q^2+3p+3q]/a (PR #8033): min over p+q<=R, (p,q)!=(0,0) "
            "is 4 at (1,0) and (0,1) for every R=1..16; pattern has purchase and "
            "the step holds as written"
        )


if __name__ == "__main__":
    main()
