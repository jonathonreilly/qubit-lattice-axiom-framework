#!/usr/bin/env python3
"""J:attack-g:PR8155 — proof step by brute force.

W5/W3 walk bound (note): (C^n)_{0x} uses nearest-neighbour adjacency of Lambda
with C_xy = c = alpha/6, and sum_n (C^n)_{0x} <= alpha^{|x|_1}/(1-alpha).
Verified LITERALLY by enumerating walks on Z^3 and on the 7^3 box of the
control (alpha=9/10), exactly as written, with Fraction arithmetic.

HIT if the enumerated sum exceeds the stated geometric bound.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import product

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def walks_to(target, nmax, box=None):
    """N_n = number of n-step NN walks 0 -> target staying in box (None=Z^3)."""
    t = tuple(target)
    cur = {(0, 0, 0): 1}
    out = []
    for n in range(1, nmax + 1):
        nxt = defaultdict(int)
        for p, w in cur.items():
            for s in STEPS:
                q = (p[0] + s[0], p[1] + s[1], p[2] + s[2])
                if box is not None and not all(0 <= q[i] < box for i in range(3)):
                    continue
                nxt[q] += w
        cur = nxt
        out.append(cur.get(t, 0))
    return out


def main() -> None:
    hits = []
    alpha = F(9, 10)
    c = alpha / 6
    # Z^3: x with |x|_1 = 1,2,3; n up to 24 as in the control
    targets = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (3, 0, 0)]
    nmax = 24
    for x in targets:
        d = sum(abs(v) for v in x)
        Ns = walks_to(x, nmax)
        s = sum((c ** n) * Ns[n - 1] for n in range(1, nmax + 1) if Ns[n - 1])
        bound = (alpha ** d) / (1 - alpha)
        print(f"Z^3 x={x} |x|_1={d}: sum_{{n<=24}} C^n = {float(s):.8f} <= {float(bound):.8f}? {s <= bound}")
        if s > bound:
            hits.append(f"Z^3 {x}: {s} > {bound}")

    # 7^3 box, origin at center (3,3,3); control: |x|_1=3 => 0.05841 <= 7.29
    box = 7
    origin = (3, 3, 3)
    xloc = (6, 3, 3)  # |x-origin|_1 = 3 along an axis
    # shift so origin is 0 for the walker, box coords 0..6, start at (3,3,3)
    # walks_to from 0 with box restriction is wrong if start isn't 0.
    # Re-run DP from origin inside the box.
    cur = {origin: 1}
    Ns = []
    for n in range(1, nmax + 1):
        nxt = defaultdict(int)
        for p, w in cur.items():
            for s in STEPS:
                q = (p[0] + s[0], p[1] + s[1], p[2] + s[2])
                if all(0 <= q[i] < box for i in range(3)):
                    nxt[q] += w
        cur = nxt
        Ns.append(cur.get(xloc, 0))
    sbox = sum((c ** n) * Ns[n - 1] for n in range(1, nmax + 1) if Ns[n - 1])
    bound3 = (alpha ** 3) / (1 - alpha)
    print(f"7^3 box |x|_1=3: sum={float(sbox):.8f} (control ~0.05841) bound={float(bound3):.8f}")
    if sbox > bound3:
        hits.append(f"7^3 |x|_1=3: {sbox} > {bound3}")

    # geometric sum identity used in the proof: sum_{n in Z} a^{|n|} = (1+a)/(1-a)
    a = alpha
    # truncated check vs closed form
    trunc = 1 + sum(2 * (a ** n) for n in range(1, 80))
    closed = (1 + a) / (1 - a)
    print(f"sum a^{{|n|}} trunc={float(trunc):.10f} closed={float(closed):.10f}")
    if abs(float(trunc - closed)) > 1e-6:
        hits.append("geometric-sum identity failed")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: proof-step brute force (walk bound); " + "; ".join(hits))
    else:
        print(
            "SUMMARY: proof-step brute force — W5 walk bound sum_n (C^n)_{0x} <= "
            "alpha^{|x|_1}/(1-alpha) holds by exact walk counts on Z^3 and the 7^3 box "
            "at alpha=9/10 (n<=24); geometric sum (1+a)/(1-a) holds"
        )


if __name__ == "__main__":
    main()
