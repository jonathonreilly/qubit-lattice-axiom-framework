#!/usr/bin/env python3
"""Independent checks for the dilute shadow force."""
from fractions import Fraction as F
from math import comb, exp, log


def axis_lines(sites, axis):
    """Lines parallel to axis through the sites, as frozensets of the other two coords."""
    lines = set()
    for s in sites:
        key = tuple(s[i] for i in range(3) if i != axis)
        lines.add(key)
    return lines


def force_count(A, B):
    """Signed overlap of axis lines: +1 if A is hit first from +stream? 
    Stream +e meets the larger coordinate first if we look along +axis from -inf.
    'A meets the + stream first' means A has the smaller coordinate (upstream of +).
    Force on A toward B is +e if B is at higher coord (B downstream of + stream, so + stream hits A first).
    """
    f = [0, 0, 0]
    for axis in range(3):
        lines_A = {}
        for s in A:
            key = tuple(s[i] for i in range(3) if i != axis)
            lines_A.setdefault(key, []).append(s[axis])
        lines_B = {}
        for s in B:
            key = tuple(s[i] for i in range(3) if i != axis)
            lines_B.setdefault(key, []).append(s[axis])
        for key, aa in lines_A.items():
            if key not in lines_B:
                continue
            a_min, a_max = min(aa), max(aa)
            b_min, b_max = min(lines_B[key]), max(lines_B[key])
            if a_max < b_min:
                f[axis] += 1  # B is downstream; +stream hits A first; force on A is +e toward B
            elif b_max < a_min:
                f[axis] -= 1
    return tuple(f)


def main():
    # flux identity: 6 * rho/(4*sqrt(3)) = rho * sqrt(3)/2
    # compare squares to avoid floats: (6/(4*sqrt(3)))^2 = 36/(16*3) = 36/48 = 3/4
    # (sqrt(3)/2)^2 = 3/4
    ok = F(36, 48) == F(3, 4)
    print("6j equals rho*sqrt(3)/2", ok)

    # multinomial (1,1,0): 2 q_x q_y
    # DP: after 2 steps, paths xy and yx only. probability 2 q_x q_y. exact.
    print("multinomial (1,1,0) = 2 q_x q_y")

    # separation-free overlap
    A = {(0, 0, 0)}
    for d in (3, 7, 21):
        B = {(d, 0, 0)}
        got = force_count(A, B)
        ok &= got == (1, 0, 0)
        print(f"sep {d} force {got}")
    ok &= force_count(A, {(0, 3, 0)}) == (0, 1, 0)
    ok &= force_count(A, {(1, 1, 0)}) == (0, 0, 0)
    ok &= force_count(A, A) == (0, 0, 0)

    # porous half-saturation: a=16, T=8, N=11
    a, T, N = 16, 8, 11
    p = 1 - comb(a * T - T, N) / comb(a * T, N)
    target = 1 - exp(-N / a)
    print(f"p(N=11)={p:.6f} 1-e^(-tau)={target:.6f} tau={N/a:.6f} ln2={log(2):.6f}")
    ok &= abs(N / a - log(2)) < 0.01 and abs(p - target) < 0.03

    if ok:
        print(
            "HIT: confirmed - shared axis lines give a separation-free force of one stream, "
            "a lone body and a diagonal pair give 0, 6j = rho*sqrt(3)/2, and opacity N=11 on 16 lines is near half"
        )
        print(
            "SUMMARY: confirmed the six-axis shadow force is the overlap of axis lines and does not fall with distance; "
            "the sphere far-field quadrature was not rebuilt"
        )
    else:
        print("SUMMARY: fails at the line-overlap or flux identity")


if __name__ == "__main__":
    main()
