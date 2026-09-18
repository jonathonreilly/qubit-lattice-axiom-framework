#!/usr/bin/env python3
"""J:attack-g:PR8155 - block 21 (PR #8155), pattern (g) PROOF STEP BY BRUTE FORCE on the W3/W5 walk bound.

The step as written (after W3): (C_Λ^k)_{xy} = c^k · #{nearest-neighbour walks of length k from x
to y inside Λ}, so Σ_y (C_Λ^k)_{xy} ≤ (6c)^k = α^k and (C_Λ^k)_{xy} = 0 for k < |x−y|_1; hence
Σ_k (C_Λ^k)_{xy} ≤ α^{|x−y|_1}/(1−α) when α < 1.

Verified literally by counting NN walks (integer DP on the adjacency, disjoint from the runner's
matvec of C) at the runner's D3 point α = 9/10, c = α/6:
  * Z^3, length ≤ 24 from the origin: total walk count = 6^k; vanishing for k < |x|_1 and the
    wrong parity; row sum of C^k equals α^k; Green partial sums ≤ α^{|x|_1}/(1−α); DP matches
    the multinomial count at small sites;
  * the 7^3 box of D3 (sites {0..6}^3, origin (3,3,3)), k ≤ 24: the same three inequalities,
    walks that leave the box discarded; row sum ≤ α^k (strict once walks can exit);
  * the W4 length claim that feeds the bound: on Λ_L = {|x|_∞ ≤ L}, a walk from Δ_ℓ = {|x|_∞ ≤ ℓ}
    to ∂_in Λ_L = {|x|_∞ = L} has length at least L−ℓ (L ≤ 4, every start);
  * the W5 neighbour step: c Σ_{z ~ x} Σ_k (C^k)_{0z} ≤ α^{|x|_1}/(6(1−α)) on Z^3.

HIT if a vanishing, a row-sum bound, a Green bound, the L−ℓ length, the neighbour step, or a
multinomial mismatch fails as written.
"""
from __future__ import annotations

import math
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import product

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
NMAX = 24
ALPHA = Fr(9, 10)
C = ALPHA / 6


def l1(p, q=(0, 0, 0)):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


def linf(p):
    return max(abs(p[0]), abs(p[1]), abs(p[2]))


def walk_layers(nmax, start=(0, 0, 0), allowed=None):
    """layers[k][site] = # of k-step NN walks start -> site staying in allowed (None = Z^3)."""
    cur = {start: 1}
    layers = [cur]
    for _ in range(nmax):
        nxt = defaultdict(int)
        for p, w in cur.items():
            for s in STEPS:
                q = (p[0] + s[0], p[1] + s[1], p[2] + s[2])
                if allowed is not None and q not in allowed:
                    continue
                nxt[q] += w
        cur = dict(nxt)
        layers.append(cur)
    return layers


def multinomial_walks(x, n):
    """# of n-step NN walks 0 -> x on Z^3 (extra round-trips)."""
    ax, ay, az = abs(x[0]), abs(x[1]), abs(x[2])
    d = ax + ay + az
    if n < d or (n - d) % 2:
        return 0
    extra = (n - d) // 2
    total = 0
    for p in range(extra + 1):
        for q in range(extra - p + 1):
            r = extra - p - q
            total += math.factorial(n) // (
                math.factorial(p + ax)
                * math.factorial(p)
                * math.factorial(q + ay)
                * math.factorial(q)
                * math.factorial(r + az)
                * math.factorial(r)
            )
    return total


def check_layers(layers, origin, name, hits, infinite):
    nmax = len(layers) - 1
    green = defaultdict(lambda: Fr(0))
    row_ok = True
    vanish_ok = True
    n_sites = 0
    first_exit = None
    for k in range(nmax + 1):
        layer = layers[k]
        nwalks = sum(layer.values())
        if infinite:
            if nwalks != 6 ** k:
                hits.append(f"{name}: total walks at k={k} is {nwalks} != 6^{k}")
                row_ok = False
        else:
            if nwalks > 6 ** k:
                hits.append(f"{name}: total walks at k={k} is {nwalks} > 6^{k}")
                row_ok = False
            if nwalks < 6 ** k and first_exit is None:
                first_exit = k
        ck = C ** k
        row = ck * nwalks
        if row > ALPHA ** k:
            hits.append(f"{name}: row sum C^{k} = {row} > alpha^{k} = {ALPHA ** k}")
            row_ok = False
        for site, n_w in layer.items():
            d = l1(site, origin)
            if k < d or (k - d) % 2:
                hits.append(f"{name}: N_{k}({site})={n_w} but k < |x|_1 or wrong parity (d={d})")
                vanish_ok = False
            if site != origin:
                green[site] += ck * n_w
                n_sites += 1
    green_ok = True
    worst = None
    for site, s in green.items():
        d = l1(site, origin)
        bound = (ALPHA ** d) / (1 - ALPHA)
        if s > bound:
            hits.append(f"{name}: Green at {site} |x|_1={d}: {s} > {bound}")
            green_ok = False
        gap = bound - s
        if worst is None or gap < worst[0]:
            worst = (gap, site, d, s, bound)
    print(
        f"[{name}] k=0..{nmax}: row-sum bound {row_ok}; vanishing {vanish_ok}; "
        f"Green at {len(green)} sites {green_ok}"
        + (f"; first exit k={first_exit}" if first_exit is not None else "; no exit (Z^3)")
        + (
            f"; tightest Green {worst[1]} d={worst[2]} sum={float(worst[3]):.8f} "
            f"bound={float(worst[4]):.8f}"
            if worst
            else ""
        )
    )
    return row_ok and vanish_ok and green_ok, green, layers


def w4_length(hits):
    ok = True
    for L in range(1, 5):
        box = {
            (x, y, z)
            for x in range(-L, L + 1)
            for y in range(-L, L + 1)
            for z in range(-L, L + 1)
        }
        din = {p for p in box if linf(p) == L}
        for ell in range(L):
            starts = [p for p in box if linf(p) <= ell]
            dist = {p: 0 for p in starts}
            q = list(starts)
            qi = 0
            while qi < len(q):
                p = q[qi]
                qi += 1
                for s in STEPS:
                    r = (p[0] + s[0], p[1] + s[1], p[2] + s[2])
                    if r in box and r not in dist:
                        dist[r] = dist[p] + 1
                        q.append(r)
            reached = [dist[p] for p in din if p in dist]
            m = min(reached) if reached else None
            print(f"[W4] L={L} ell={ell}: min walk Delta_ell -> inner boundary = {m} (stated L-ell={L - ell})")
            if m != L - ell:
                hits.append(f"W4 length L={L} ell={ell}: min={m} != {L - ell}")
                ok = False
    return ok


def w5_neighbour(layers, origin, hits, nmax_use=16):
    ok = True
    # sites reached by length <= nmax_use with d >= 1
    sites = set()
    for k in range(1, nmax_use + 1):
        sites.update(layers[k])
    sites.discard(origin)
    worst = None
    nchk = 0
    for x in sites:
        d = l1(x, origin)
        if d == 0:
            continue
        acc = Fr(0)
        min_k = None
        for k in range(0, nmax_use + 1):
            layer = layers[k]
            sub = 0
            for s in STEPS:
                z = (x[0] + s[0], x[1] + s[1], x[2] + s[2])
                sub += layer.get(z, 0)
            if sub and min_k is None:
                min_k = k
            acc += (C ** k) * sub
        lhs = C * acc
        bound = (ALPHA ** d) / (6 * (1 - ALPHA))
        nchk += 1
        if min_k is not None and min_k < d - 1:
            hits.append(f"W5: min walk 0 -> neighbour of {x} is {min_k} < |x|_1-1={d - 1}")
            ok = False
        if lhs > bound:
            hits.append(f"W5 neighbour step at {x} d={d}: {lhs} > {bound}")
            ok = False
        gap = bound - lhs
        if worst is None or gap < worst[0]:
            worst = (gap, x, d, lhs, bound, min_k)
    print(
        f"[W5] neighbour step on {nchk} sites, k<= {nmax_use}: "
        f"tightest {worst[1]} d={worst[2]} min_k={worst[5]} lhs={float(worst[3]):.8f} "
        f"bound={float(worst[4]):.8f}; ok={ok}"
    )
    return ok


def main():
    hits = []
    # Z^3
    z3 = walk_layers(NMAX)
    check_layers(z3, (0, 0, 0), "Z^3", hits, infinite=True)

    # multinomial cross-check at small sites / lengths
    multi_ok = True
    samples = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (3, 0, 0), (2, 1, 0), (4, 0, 0)]
    for x in samples:
        for n in range(0, 13):
            got = z3[n].get(x, 0)
            exp = multinomial_walks(x, n)
            if got != exp:
                hits.append(f"multinomial {x} n={n}: DP {got} != {exp}")
                multi_ok = False
    print(f"[multinomial] DP vs extra-round-trip formula at {len(samples)} sites, n<=12: {multi_ok}")

    # 7^3 box of D3
    box = set(product(range(7), repeat=3))
    origin = (3, 3, 3)
    b7 = walk_layers(NMAX, start=origin, allowed=box)
    check_layers(b7, origin, "7^3 box", hits, infinite=False)

    # W4 length used to convert the walk bound into alpha^{L-ell+1}/(1-alpha)
    w4_length(hits)

    # W5 neighbour contraction on Z^3
    w5_neighbour(z3, (0, 0, 0), hits, nmax_use=16)

    if hits:
        for h in hits:
            print("HIT: " + h)
        print(
            "SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on the W3/W5 walk bound - "
            + "; ".join(hits)
        )
        return 1
    print(
        "SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on the W3/W5 walk bound - "
        "(C^k)_{xy}=c^k #NN-walks, row sum <= alpha^k, vanishing for k<|x|_1, and "
        "sum_k (C^k)_{0x} <= alpha^{|x|_1}/(1-alpha) hold by exact walk counts on Z^3 and the "
        f"7^3 box at alpha=9/10 (n<={NMAX}); W4 min length Delta_ell -> inner boundary is L-ell "
        "for L<=4; W5 neighbour step holds; multinomial cross-check holds; the step holds as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
