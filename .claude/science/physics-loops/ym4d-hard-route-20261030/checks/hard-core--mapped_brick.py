#!/usr/bin/env python3
"""Combinatorics of the brick tiling of Lemma BG, `library/fibre-propagator.md`. Consumer: that lemma, Theorem F-D with layers.

Written before running. T_1: intervals of length t. T_d: layers of height t in x_d, with layer m carrying T_(d-1) shifted by m v, v := t (2^-(d-1), ..., 2^-1). Take t = 2^(d-1) so that all walls are at integers. A cell is a box [a_i, a_i + t] in each coordinate.

PRE-STATED criteria, for d = 2, 3, 4, on all cells meeting a window of side 3 t about the origin, and with a test over all points of the half-integer grid in the window's middle.
 B1. Two distinct closed cells that meet do so in a set of dimension d - 1 (no pinch).
 B2. At most d + 1 cells contain any point.
 B3. The cells cover the window with disjoint interiors: every half-integer generic point lies in exactly one cell.
 B4. Control: with the shift in the other order, v := t (2^-1, ..., 2^-(d-1)), at d = 3 B1 must fail. This is the first form I wrote, and a hand count says that it has a pinch. If it does not fail, the check has no power.
FAIL if B1, B2 or B3 fails at any d, or B4 does not fail.

Limits. Combinatorics only. It does not test the extension constant, which is by bi-Lipschitz maps on finitely many patterns.
"""
import itertools
import sys
from fractions import Fraction as Fr


def cells(d, t, window, order):
    """All cells of T_d meeting [-window, window]^d, as tuples of lower corners."""
    def rec(dim):
        if dim == 1:
            return lambda m_tuple: None

    def build(dim, shift):
        # Yields lower corners of T_dim shifted by shift (length dim), meeting the window.
        if dim == 1:
            k0 = int((-window - shift[0]) // t) - 1
            k1 = int((window - shift[0]) // t) + 1
            for k in range(k0, k1 + 1):
                yield (k * t + shift[0],)
            return
        k0 = int((-window - shift[dim - 1]) // t) - 1
        k1 = int((window - shift[dim - 1]) // t) + 1
        if order == "right":
            v = [Fr(t) / 2 ** (dim - 1 - i) for i in range(dim - 1)]
        else:
            v = [Fr(t) / 2 ** (i + 1) for i in range(dim - 1)]
        for m in range(k0, k1 + 1):
            s = [shift[i] + m * v[i] for i in range(dim - 1)]
            for c in build(dim - 1, s):
                yield c + (m * t + shift[dim - 1],)

    out = set()
    for c in build(d, [Fr(0)] * d):
        if all(c[i] <= window and c[i] + t >= -window for i in range(d)):
            out.add(c)
    return sorted(out)


def analyse(d, t, order):
    window = Fr(3 * t, 2)
    cs = cells(d, t, window, order)
    pinch = 0
    for a, b in itertools.combinations(cs, 2):
        dim = 0
        meets = True
        for i in range(d):
            lo, hi = max(a[i], b[i]), min(a[i] + t, b[i] + t)
            if lo > hi:
                meets = False
                break
            if lo < hi:
                dim += 1
        if meets and dim != d - 1:
            pinch += 1
    # Corners: multiples of the finest wall spacing, in the middle of the window.
    step = Fr(t, 2 ** (d - 1)) if d > 1 else Fr(t)
    n = int((Fr(t, 2)) / step)
    grid = [k * step for k in range(-n, n + 1)]
    most = 0
    for x in itertools.product(grid, repeat=d):
        count = sum(all(c[i] <= x[i] <= c[i] + t for i in range(d)) for c in cs)
        most = max(most, count)
    # Cover: generic points.
    bad = 0
    gen = [(k + Fr(1, 3)) * step for k in range(-n, n)]
    for x in itertools.product(gen, repeat=d):
        count = sum(all(c[i] < x[i] < c[i] + t for i in range(d)) for c in cs)
        if count != 1:
            bad += 1
    return len(cs), pinch, most, bad


def main():
    ok = True
    for d in (2, 3, 4):
        t = 2 ** (d - 1)
        n, pinch, most, bad = analyse(d, t, "right")
        good = pinch == 0 and most <= d + 1 and bad == 0
        ok = ok and good
        print(f" d={d}: cells={n}, pinching pairs={pinch}, most cells at a point={most}, cover defects={bad}: {good}", flush=True)
    n, pinch, most, bad = analyse(3, 4, "wrong")
    b4 = pinch > 0
    ok = ok and b4
    print(f" B4 control, d=3, the other order: cells={n}, pinching pairs={pinch}, most cells at a point={most}: fails as it should: {b4}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
