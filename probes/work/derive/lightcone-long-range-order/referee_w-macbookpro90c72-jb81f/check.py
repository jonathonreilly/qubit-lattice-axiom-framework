#!/usr/bin/env python3
"""Referee for lightcone-long-range-order a3.

Author w-jonathonsmac4f50-j3a1d (claude-opus-5).
S1 and S2 are exact. The universal hedge removal does not follow from seven tori.
"""
from fractions import Fraction as Fr

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def cos_table(L):
    if L == 4:
        return {0: Fr(1), 1: Fr(0), 2: Fr(-1), 3: Fr(0)}
    return {0: Fr(1), 1: Fr(1, 2), 2: Fr(-1, 2), 3: Fr(-1), 4: Fr(-1, 2), 5: Fr(1, 2)}


def sums(L):
    c = cos_table(L)
    N = L ** 3
    G = H14 = H2 = Fr(0)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                E = 6 - 2 * (c[x] + c[y] + c[z])
                H14 += Fr(1, 14 - E)
                H2 += Fr(1, 2 + E)
                if (x, y, z) != (0, 0, 0):
                    G += Fr(1, E)
    return G / N, H14 / N, H2 / N


def main():
    g4, h14_4, h2_4 = sums(4)
    g6, h14_6, h2_6 = sums(6)
    report(
        "step1 two forms of H",
        h14_4 == h2_4 and h14_6 == h2_6,
        "on even L=4 and L=6, sum 1/(14-E) equals sum 1/(2+E) after k -> k+pi",
    )
    report(
        "step2 small tori",
        g4 == Fr(1517, 7680) and h14_4 == Fr(127, 896)
        and g6 == Fr(1289503, 5987520) and h14_6 == Fr(30479, 216216),
        "G_4=1517/7680, H_4=127/896, G_6=1289503/5987520, H_6=30479/216216",
    )
    # Their E3 loop is L = 4,6,8,10,12,16,20. An increasing check on that list
    # does not bound the next even torus.
    checked = (4, 6, 8, 10, 12, 16, 20)
    report(
        "step3 every even L",
        False,
        "G_L < I_0 and G_L increasing are computed only at "
        + ",".join(str(L) for L in checked)
        + "; that list does not imply the inequality at every even L, so the sufficiently-large-L hedge is not removed",
    )
    if fails:
        print("SUMMARY: fails at step 3 - G_L < I_0 for every even L is checked only through L=20, and the removal of the sufficiently-large-L hedge does not follow")
        return
    print("SUMMARY: confirmed")


if __name__ == "__main__":
    main()
