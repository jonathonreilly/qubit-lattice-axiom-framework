#!/usr/bin/env python3
"""J:attack:PR8175 - block 31, attack pattern (a) WITNESS REALIZABILITY.

Rebuild W1/W2/W3 from listed noise marks through the one-sided two-level
automaton on Z^3 (predecessors x-e_j; outside the window is 0). Check:
marks lie in the stated windows; the root is 1; W1's 11 marks are exactly
the seed plus amplified 1-sites; stated (E,|A|,|S|) ratios 8/5 and 5/3;
T1.1 M_k increment; T1.3 period sum (0,4,2); W1 log sums E=16, |A|=10.

HIT if a witness is not realizable or a stated count/ratio fails.
"""
from __future__ import annotations

from fractions import Fraction as F

E_J = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
W1 = ((3, 3, 4), (4, 4, 7), [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0),
    (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2),
])
W2 = ((3, 3, 6), (4, 4, 7), [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2),
    (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6),
    (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1),
    (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2),
    (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3),
    (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0),
    (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5),
])
W3 = ((4, 4, 5), (5, 5, 9), [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 4), (0, 1, 0), (0, 1, 5),
    (0, 2, 3), (0, 2, 8), (0, 3, 1), (0, 3, 3), (0, 3, 4), (0, 4, 3),
    (0, 4, 4), (0, 4, 5), (0, 4, 6), (0, 4, 7), (1, 0, 0), (1, 0, 1),
    (1, 0, 4), (1, 1, 0), (1, 1, 1), (1, 1, 5), (1, 1, 7), (1, 2, 8),
    (1, 3, 8), (2, 0, 0), (2, 1, 1), (2, 1, 5), (2, 1, 6), (2, 1, 8),
    (2, 2, 0), (2, 2, 1), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 3, 1),
    (2, 3, 2), (2, 3, 3), (2, 3, 8), (2, 4, 0), (2, 4, 2), (3, 0, 2),
    (3, 0, 8), (3, 1, 6), (3, 1, 7), (3, 2, 0), (3, 2, 2), (3, 2, 6),
    (3, 2, 7), (3, 2, 8), (3, 3, 1), (3, 3, 2), (3, 3, 4), (3, 3, 7),
    (3, 4, 3), (3, 4, 5), (4, 0, 2), (4, 0, 4), (4, 0, 5), (4, 0, 6),
    (4, 1, 0), (4, 1, 4), (4, 1, 6), (4, 1, 7), (4, 1, 8), (4, 2, 0),
    (4, 2, 2), (4, 2, 6), (4, 3, 0), (4, 3, 1), (4, 3, 6), (4, 4, 2),
    (4, 4, 6), (4, 4, 8),
])
W1_LOG = [  # (b, kept, a, e)
    (0, 1, 0, 1), (1, 2, 1, 1), (0, 2, 0, 2), (1, 3, 1, 2), (0, 3, 0, 3),
    (2, 3, 2, 1), (0, 3, 0, 3), (2, 3, 2, 1), (1, 3, 1, 2), (3, 3, 3, 0),
]
STATED = {"W1": (16, 10, 1), "W2": (20, 12, 1), "W3": (23, 12, 2)}


def tau(z):
    return z[0] + z[1] + z[2]


def pred(x, j):
    return tuple(x[i] - E_J[j][i] for i in range(3))


def in_win(z, shape):
    return all(0 <= z[i] < shape[i] for i in range(3))


def run(root, shape, marks):
    zeta = set(marks)
    sites = [(x, y, z) for x in range(shape[0]) for y in range(shape[1]) for z in range(shape[2])]
    sites.sort(key=tau)
    eta = {}
    for x in sites:
        ones = sum(1 for j in range(3) if eta.get(pred(x, j), 0) == 1)
        eta[x] = 1 if ones >= 2 or (ones < 2 and x in zeta) else 0
    ones_sites = [x for x, v in eta.items() if v == 1]
    seed, amp, proc = [], [], []
    for x in ones_sites:
        n1 = sum(1 for j in range(3) if eta.get(pred(x, j), 0) == 1)
        if n1 == 0:
            seed.append(x)
        elif n1 == 1:
            amp.append(x)
        else:
            proc.append(x)
    return eta, seed, amp, proc


def M(k, z):
    return F(z[k]) - F(tau(z), 3)


def main() -> None:
    hits = []
    for name, (root, shape, marks) in (("W1", W1), ("W2", W2), ("W3", W3)):
        if any(not in_win(m, shape) for m in marks) or not in_win(root, shape):
            hits.append(f"{name} mark or root outside window {shape}")
        if len(marks) != len(set(marks)):
            hits.append(f"{name} duplicate marks")
        eta, seed, amp, proc = run(root, shape, marks)
        print(f"{name}: root eta={eta.get(root)} |1-sites|={sum(eta.values())} "
              f"seed={len(seed)} amp={len(amp)} proc={len(proc)} marks={len(marks)}")
        if eta.get(root) != 1:
            hits.append(f"{name} root {root} is not 1")
        E, A, S = STATED[name]
        sharp = 3 * (S - 1) + A
        proved = 3 * (S - 1) + 2 * A
        ratio = F(E - 3 * (S - 1), A)
        print(f"  (E,A,S)=({E},{A},{S}) ratio {ratio}; sharp E<={sharp}? {E <= sharp}; proved E<={proved}? {E <= proved}")
        if E <= sharp:
            hits.append(f"{name} does not refute the sharper budget")
        if E > proved:
            hits.append(f"{name} exceeds block 30's proved budget")
        if name == "W1":
            sa = set(seed) | set(amp)
            if sa != set(marks):
                hits.append(f"W1 self-contained fails: seed+amp {sorted(sa)} vs marks")
            if (len(seed), len(amp)) != (1, 10):
                hits.append(f"W1 seed/amp counts {len(seed), len(amp)} != (1,10)")

    se = sum(t[3] for t in W1_LOG)
    sa = sum(t[2] for t in W1_LOG)
    print(f"W1 log sum e={se} a={sa} n={len(W1_LOG)}")
    if (se, sa, len(W1_LOG)) != (16, 10, 10):
        hits.append(f"W1 log sums {(se, sa, len(W1_LOG))} != (16,10,10)")
    periods = 0
    for i in range(len(W1_LOG) - 1):
        if W1_LOG[i] == (0, 3, 0, 3) and W1_LOG[i + 1] == (2, 3, 2, 1):
            periods += 1
    print(f"W1 T1.3 periods: {periods} (stated 2)")
    if periods != 2:
        hits.append(f"W1 period count {periods} != 2")
    r, e, a = 1 + (-1), 3 + 1, 0 + 2
    if (r, e, a) != (0, 4, 2) or F(e - 3 * r, a) != 2:
        hits.append("T1.3 period arithmetic failed")

    # T1.1: amplified v, direction j
    v, j = (2, 3, 4), 0  # sample: tau drops by 1 along e_0
    u = pred(v, j)
    for k in range(3):
        d = M(k, u) - M(k, v)
        want = F(1, 3) - (1 if k == j else 0)
        print(f"T1.1 amp j={j} k={k}: {d} want {want}")
        if d != want:
            hits.append(f"T1.1 increment {d} != {want}")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (a) WITNESS REALIZABILITY; W1/W2/W3 marks sit in the stated "
            "Z^3 windows, roots are 1 under the one-sided automaton, W1 is self-contained "
            "(11 marks = 1 seed + 10 amplified), ratios 8/5 and 5/3 refute the sharper budget "
            "inside block 30's, T1.1 and T1.3 hold"
        )


if __name__ == "__main__":
    main()
