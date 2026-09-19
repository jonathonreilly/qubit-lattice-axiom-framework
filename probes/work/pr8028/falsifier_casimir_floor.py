#!/usr/bin/env python3
"""J:falsifier:PR8028 — free charged threshold Q>=4 beyond small R.

Section 2: electric energy [p²+pq+q²+3p+3q]/a >=4/a, equality at (1,0),(0,1).
Scan p+q<=20. HIT if min over nontrivial irreps is not 4.
"""
from __future__ import annotations

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    for R in range(1, 21):
        nt = [(p, q) for p in range(R + 1) for q in range(R + 1 - p) if (p, q) != (0, 0)]
        m = min(Q(p, q) for p, q in nt)
        mins = [pq for pq in nt if Q(*pq) == m]
        print(f"R={R} minQ={m} at {sorted(mins)[:4]}")
        if m != 4:
            HITS.append(f"R={R} min={m}")
        if (1, 0) not in nt or Q(1, 0) != 4:
            HITS.append(f"R={R} fund")
    if HITS:
        print("HIT: " + "; ".join(HITS[:4]))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: Casimir-floor falsifier did not fire: min Q=4 at (1,0) and "
        "(0,1) for every cutoff R=1..20"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
