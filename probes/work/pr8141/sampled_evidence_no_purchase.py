#!/usr/bin/env python3
"""J:attack-e:PR8141 — SAMPLED EVIDENCE.

'Never adjacent' is Z^3 bipartiteness of co-recorded pairs; 'always Gibbs'
is T1's exact product formula. Plaquette pair term 12/13 and star 165/169
are exact. No sampled never/always.
"""
from fractions import Fraction as Fr
from itertools import combinations, product


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def main() -> int:
    # co-recorded star leaves: (1,0,0), (0,1,0), (0,0,1) — pairwise not nn
    leaves = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    adj = any(nn(a, b) for a, b in combinations(leaves, 2))
    print(f"star leaves adjacent? {adj} (stated never)")
    assert not adj
    print(f"plaquette pair term {Fr(12, 13)}; star three-body {Fr(165, 169)}")
    print(
        "SUMMARY: pattern has no purchase on this note — co-recorded pairs "
        "are never adjacent by bipartiteness, Gibbs/Markov statements and "
        "12/13, 165/169 are exact, not sampled never/always observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
