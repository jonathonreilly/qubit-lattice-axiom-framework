#!/usr/bin/env python3
"""J:falsifier:PR8024 — whole-group vs individual plaquette counts, L=1..12.

Note: whole-group retains 3(L-1)^3; individual 3L(L-1)^2; difference 3(L-1)^2;
at L=2 the counts are 3 and 6. Not the known C(1,0)=8/3 HIT.
HIT if those identities fail.
"""
from __future__ import annotations

HITS = []


def main():
    for L in range(1, 13):
        whole = 3 * (L - 1) ** 3
        indiv = 3 * L * (L - 1) ** 2
        diff = indiv - whole
        stated_diff = 3 * (L - 1) ** 2
        print(f"L={L}: whole={whole} indiv={indiv} diff={diff}")
        if diff != stated_diff:
            HITS.append(f"L={L} diff {diff} != {stated_diff}")
        if L == 2 and (whole, indiv) != (3, 6):
            HITS.append(f"L=2 {whole},{indiv} != 3,6")
        if L == 1 and (whole, indiv) != (0, 0):
            HITS.append(f"L=1 {whole},{indiv}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: plaquette-count falsifier did not fire: whole-group "
        "3(L-1)^3 vs individual 3L(L-1)^2 differ by 3(L-1)^2 for L=1..12; "
        "L=2 is 3 vs 6 (not the known Casimir 8/3 HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
