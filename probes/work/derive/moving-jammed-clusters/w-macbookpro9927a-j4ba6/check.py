#!/usr/bin/env python3
"""Moving jammed clusters: checks for ATTEMPT.md (attempt 3), worker w-macbookpro9927a-j4ba6 (claude-opus-5-5).

Object (block 39, PR #8530 head 31e5d0300e): records on Z^3, one per site; a bond with exactly one occupied end is visited and the
record moves with a positive probability (pair-weight transit), so the arrangements reachable in T moves are those reached by T
single moves of a record to an empty neighbour. The cluster: the full L x L x L box of aligned records in empty space, no formation.
Everything here is exact: breadth-first enumeration of arrangements as (vacated box sites, occupied outside sites), integer counts,
sympy polynomials and generating functions.
"""
from __future__ import annotations

import itertools
import json
import subprocess
import sys

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


NOTES = [
    ("b39", "31e5d0300e", "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_"
     "IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md",
     ["- **Pair-weight transit.** A bond with exactly one occupied end is visited (bonds at any symmetric rates)",
      "it moves with probability `w_y/(w_x + w_y)`"]),
    ("a2", "71382604f8", "probes/work/derive/moving-jammed-clusters/w-jonathonsmac4f50-j7b51/ATTEMPT.md",
     ["- **(a) beyond one move.** The number of arrangements reachable in `T > 1` moves is still only a1's bound."]),
]
TASK_Q = ["(a) which records can ever move (the surface), and how the number of arrangements reachable in a time T scales with the "
          "cluster's volume and with its surface"]


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:moving-jammed-clusters:a3"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 39's pair-weight transit (PR #8530 head 31e5d030), attempt 2's open item (ai/probes 71382604) and the task "
          f"quoted verbatim (4 lines){'; missing ' + str(miss) if miss else ''}")


E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(s, e):
    return (s[0] + e[0], s[1] + e[1], s[2] + e[2])


_CACHE: dict = {}


def bfs(L: int, T: int):
    """layers of arrangements first reached after exactly t moves, as (vacated box sites, occupied outside sites)."""
    for (L0, T0), lay in _CACHE.items():
        if L0 == L and T0 >= T:
            return lay[:T + 1]
    lay = _bfs(L, T)
    _CACHE[(L, T)] = lay
    return lay


def _bfs(L: int, T: int):
    inbox = lambda s: 0 <= s[0] < L and 0 <= s[1] < L and 0 <= s[2] < L
    surface = [s for s in itertools.product(range(L), repeat=3) if any(not inbox(add(s, e)) for e in E6)]
    start = (frozenset(), frozenset())
    seen = {start}
    layers = [[start]]
    for _ in range(T):
        nxt = []
        for rem, ad in layers[-1]:
            movers = set(s for s in surface if s not in rem)
            for v in rem:
                for e in E6:
                    u = add(v, e)
                    if inbox(u) and u not in rem:
                        movers.add(u)
            movers |= set(ad)
            for s in movers:
                for e in E6:
                    t = add(s, e)
                    if (inbox(t) and t not in rem) or t in ad:
                        continue
                    r2, a2 = set(rem), set(ad)
                    if s in a2:
                        a2.discard(s)
                    else:
                        r2.add(s)
                    if t in r2:
                        r2.discard(t)
                    else:
                        a2.add(t)
                    st = (frozenset(r2), frozenset(a2))
                    if st not in seen:
                        seen.add(st)
                        nxt.append(st)
        layers.append(nxt)
    return layers


Ls = sp.Symbol("L")
xg = sp.Symbol("x")


def gen_coeff(T: int):
    """[x^T] (1 + x)^(6(L-2)^2) (1 + 2x)^(12(L-2)) (1 + 3x)^8 as a polynomial in L (binomials as polynomials in the exponent)."""
    n1, n2 = 6 * (Ls - 2) ** 2, 12 * (Ls - 2)
    tot = 0
    for i in range(T + 1):
        for j in range(T + 1 - i):
            k = T - i - j
            tot += sp.binomial(8, k) * 3 ** k * sp.expand_func(sp.binomial(n2, j)) * 2 ** j * sp.expand_func(sp.binomial(n1, i))
    return sp.expand(sp.simplify(tot))


# ------------------------------------------------------------------------------------------------ D: who can move by move T
def family_d() -> None:
    ok = True
    rows = []
    for L, T in ((2, 3), (3, 3), (4, 3), (5, 3), (6, 2), (7, 2)):
        layers = bfs(L, T)
        inbox = lambda s: 0 <= s[0] < L and 0 <= s[1] < L and 0 <= s[2] < L
        depth = {s: min(s[0] + 1, L - s[0], s[1] + 1, L - s[1], s[2] + 1, L - s[2]) for s in itertools.product(range(L), repeat=3)}
        for t in range(1, T + 1):
            vac = set()
            for layer in layers[:t + 1]:
                for rem, _ in layer:
                    vac |= rem
            want = {s for s, dd in depth.items() if dd <= t}
            ok &= vac == want
        rows.append(L)
    check("D", ok, "the records that have left their sites within t moves are exactly those at graph distance <= t from the outside "
          f"(boxes L = {', '.join(map(str, rows))}, t up to 3): depth d needs exactly d moves; the movable set grows by one layer per move")


# ------------------------------------------------------------------------------------------------ N: the exact two-move census
def family_n() -> dict:
    ok = True
    data = {}
    for L in range(2, 11):
        layers = bfs(L, 2)
        one = len(layers[1])
        two = len(layers[2])
        n22 = sum(1 for rem, ad in layers[2] if len(rem) == 2 and len(ad) == 2)
        n11 = sum(1 for rem, ad in layers[2] if len(rem) == 1 and len(ad) == 1)
        ok &= one == 6 * L ** 2 and n22 + n11 == two
        ok &= two == 18 * L ** 4 + 33 * L ** 2 - 24 * L
        ok &= n22 == sp.binomial(6 * L ** 2, 2) - 12 * L == gen_coeff(2).subs(Ls, L)
        ok &= n11 == 36 * L ** 2 - 12 * L
        data[L] = (one, two, n22, n11)
    # the one-displacement part is local: for L >= 7 it is a polynomial of degree <= 2; L = 7, 8, 9 fix it, the rest confirm
    quad = sp.expand(sp.interpolate([(L, data[L][3]) for L in range(7, 10)], Ls))
    ok &= quad == 36 * Ls ** 2 - 12 * Ls and all(quad.subs(Ls, L) == data[L][3] for L in range(2, 11))
    check("N", ok, "exact enumeration, boxes L = 2..10: one move 6L^2; two moves N_2 = 18L^4 + 33L^2 - 24L exactly (e.g. L = 10: "
          f"{data[10][1]}), of which C(6L^2, 2) - 12L = [x^2] of the generating function have two displaced records and 36L^2 - 12L one")
    return data


# ------------------------------------------------------------------------------------------------ T: every T, and three moves
def family_t() -> None:
    ok = True
    for T in range(1, 6):
        c = sp.Poly(gen_coeff(T), Ls)
        deg = c.degree()
        lead = c.coeff_monomial(Ls ** (2 * T))
        sub = c.coeff_monomial(Ls ** (2 * T - 1))
        ok &= deg == 2 * T and lead == sp.Rational(6 ** T, sp.factorial(T)) and sub == 0
    three = {}
    for L in (2, 3, 4, 5):
        layers = bfs(L, 3)
        n33 = sum(1 for rem, ad in layers[3] if len(rem) == 3)
        ok &= n33 == gen_coeff(3).subs(Ls, L)
        three[L] = (len(layers[3]), n33)
    check("T", ok, "T displaced records after T moves = T outward moves by distinct surface records: [x^T](1+x)^{6(L-2)^2}(1+2x)^{12(L-2)}"
          "(1+3x)^8, leading term 6^T L^{2T}/T! with no L^{2T-1} term (T = 1..5); three moves, L = 2..5: "
          f"{', '.join(f'{three[L][0]} arrangements ({three[L][1]} with three displaced)' for L in (2, 3, 4, 5))}")


def main() -> int:
    family_q()
    family_d()
    data = family_n()
    family_t()
    print("Moving jammed clusters - checks; worker w-macbookpro9927a-j4ba6 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact for (a) beyond one move, for the L x L x L box of aligned records: a record at graph distance d from "
          "the outside first leaves its site at move d, so the movable set grows by one layer per move; the arrangements first reached "
          "after two moves number exactly 18L^4 + 33L^2 - 24L (checked L = 2..10), and after T moves (6L^2)^T/T! + O(L^{2T-2}), the "
          "leading part being [x^T](1+x)^{6(L-2)^2}(1+2x)^{12(L-2)}(1+3x)^8 (T outward moves by distinct records): a surface count "
          "with no volume term and no L^{2T-1} term")
    print("HIT: for an L x L x L cluster of aligned records under block 39's transit, the arrangements first reached after T moves number "
          "(6L^2)^T/T! + O(L^{2T-2}) - exactly 18L^4 + 33L^2 - 24L at T = 2 - so reachability counts the surface's one-move census and "
          "not the volume, and a record at depth d first moves at move d")
    return 0


if __name__ == "__main__":
    sys.exit(main())
