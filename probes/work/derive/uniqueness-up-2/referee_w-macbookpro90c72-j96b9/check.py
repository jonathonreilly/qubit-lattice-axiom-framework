#!/usr/bin/env python3
"""Independent alpha_3 on (p,1,2): max TV of two three-parent kernels differing in one parent."""
from fractions import Fraction as F
import itertools

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def phi(a, b, p, q, r):
    if a == b:
        return p
    if a == tuple(-x for x in b):
        return q
    return r


def law(parents, p, q, r):
    w = []
    for s in DIRS:
        ww = F(1)
        for parent in parents:
            ww *= phi(parent, s, p, q, r)
        w.append(ww)
    z = sum(w)
    return [x / z for x in w]


def tv(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / 2


def alpha3(p, q=1, r=2):
    p, q, r = F(p), F(q), F(r)
    best = F(0)
    for parents in itertools.product(DIRS, repeat=3):
        for i in range(3):
            for alt in DIRS:
                if alt == parents[i]:
                    continue
                other = list(parents)
                other[i] = alt
                best = max(best, tv(law(parents, p, q, r), law(other, p, q, r)))
    return best


def main():
    targets = {
        5: "0.38791",
        F(23, 4): "0.42081",
        6: "0.43370",
        F(21, 2): "0.65303",
    }
    ok = True
    for p, shown in targets.items():
        a = alpha3(p)
        print(f"p={p} alpha3={float(a):.5f} exact={a} stated {shown}")
        ok &= abs(float(a) - float(shown)) < 5e-6
    # monotone in p
    seq = [alpha3(p) for p in (5, F(23, 4), 6, 7, F(21, 2))]
    ok &= seq == sorted(seq)
    print("increasing", seq == sorted(seq))
    if ok:
        print(
            "HIT: confirmed - alpha_3(p,1,2) matches the stated values at p=5, 23/4, 6 and 21/2 "
            "and increases with p, so the disagreement rate at p=10.5 is about 0.653"
        )
        print(
            "SUMMARY: confirmed the exact coupling-failure rates; the measured percolation window "
            "0.425 to 0.43 was not re-simulated, and the ceiling near p=5.9 follows if that window is right"
        )
    else:
        print("SUMMARY: fails at the alpha_3 census")


if __name__ == "__main__":
    main()
