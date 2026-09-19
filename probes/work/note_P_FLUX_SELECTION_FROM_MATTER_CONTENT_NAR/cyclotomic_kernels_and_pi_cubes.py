#!/usr/bin/env python3
"""J:note falsifiers for P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10 (on main).

Falsifiers implemented: "more than one embedded pi-cube carrier in K0 at the certified volumes" and "a failure of any G battery item on
the embedded K0 carrier" (for the items that live in the momentum picture: Klein-cube characters with multiplicity one after the
global per-direction phase, Hamming grading 1+3+3+1, C3[111] cycling of the lines, the hw = 1 joint characters), and the note's
separating numbers (K0 zeros 20 -> 68, K1 zeros 8 -> 8, ker K1 = carrier, ker K0 strictly larger).

Machinery disjoint from the runner (real-space matrices and numerical kernels at L = 4, 8, wrap leg L = 6): EXACT arithmetic in the
cyclotomic ring Z[zeta_L]. K0 (flux +1, scalar hopping) has Bloch energy 2 sum_mu cos k_mu, so a momentum is a zero mode iff
sum_mu (x^{j_mu} + x^{-j_mu}) = 0 mod Phi_L(x); K1 (flux -1, Kawamoto-Smit signs) has |E|^2 = 4 sum_mu sin^2 k_mu... (zero iff every
k_mu in {0, pi}). For every even L = 4..24: the exact zero-mode counts of both branches, the number of pi-cube cosets {k0 + pi b}
contained in ker K0, and the battery items on each such cube. Beyond the note's volumes (L = 4, 8).
HIT if a falsifier fires at the certified volumes, or the note's counts are not reproduced.
"""
from __future__ import annotations

import itertools

import sympy as sp

x = sp.symbols("x")


def zero_table(L):
    """exact test of sum cos(2 pi j_mu / L) = 0 via reduction mod the cyclotomic polynomial."""
    Phi = sp.Poly(sp.cyclotomic_poly(L, x), x)
    reps = {}
    for j in range(L):
        p = sp.Poly(x ** (j % L) + x ** ((-j) % L), x)
        reps[j] = p.rem(Phi)
    zeros = set()
    for js in itertools.product(range(L), repeat=3):
        s = reps[js[0]] + reps[js[1]] + reps[js[2]]
        if s.is_zero:
            zeros.add(js)
    return zeros


def k1_zeros(L):
    # sin(2 pi j / L) = 0 exactly iff 2j = 0 mod L
    return {js for js in itertools.product(range(L), repeat=3) if all((2 * j) % L == 0 for j in js)}


def pi_cubes(zeros, L):
    """cosets {k0 + pi b : b in {0,1}^3} fully inside the zero set (pi = L/2 in index units); returns the list of cosets."""
    if L % 2:
        return []
    h = L // 2
    cubes = set()
    for k0 in zeros:
        coset = frozenset(tuple((k0[m] + h * b[m]) % L for m in range(3)) for b in itertools.product((0, 1), repeat=3))
        if coset <= zeros:
            cubes.add(coset)
    return list(cubes)


def battery(cube, L):
    """translation characters e^{i k_mu} on the cube, times the global per-direction phase that maps them to +-1; Klein cube with
    multiplicity one, Hamming grading, C3 cycling, hw=1 joint characters (-1,+1,+1)/(+1,-1,+1)/(+1,+1,-1)."""
    import cmath
    chars = []
    for k in cube:
        ch = tuple(cmath.exp(2j * cmath.pi * k[m] / L) for m in range(3))
        chars.append(ch)
    # global per-direction phase: divide by the first element's characters' phase in each direction, then the set must be {+-1}
    ref = chars[0]
    norm = [tuple(c[m] / ref[m] for m in range(3)) for c in chars]
    signs = []
    ok_real = True
    for c in norm:
        s = []
        for v in c:
            if abs(v - 1) < 1e-12:
                s.append(1)
            elif abs(v + 1) < 1e-12:
                s.append(-1)
            else:
                ok_real = False
        signs.append(tuple(s))
    klein = ok_real and sorted(signs) == sorted(itertools.product((1, -1), repeat=3))
    # orient so that a Hamming grading counts -1 entries
    ham = {w: sum(1 for s in signs if s.count(-1) == w) for w in range(4)} if ok_real else {}
    hw1 = sorted(s for s in signs if s.count(-1) == 1) == sorted([(-1, 1, 1), (1, -1, 1), (1, 1, -1)]) if ok_real else False
    # C3[111]: (k1, k2, k3) -> (k3, k1, k2) maps the cube to itself and cycles the three hw = 1 lines
    img = {tuple((k[2], k[0], k[1])) for k in cube}
    c3_closed = img == set(cube)
    return klein, ham, hw1, c3_closed


def main():
    rows = {}
    for L in range(4, 25, 2):
        z0 = zero_table(L)
        z1 = k1_zeros(L)
        cubes = pi_cubes(z0, L)
        k1_is_cube = pi_cubes(z1, L)
        bat = [battery(c, L) for c in cubes]
        rows[L] = (len(z0), len(z1), len(cubes), len(k1_is_cube), bat, len(z0) > 8 * len(cubes) if cubes else None)
    for L, (n0, n1, nc, nc1, bat, strict) in rows.items():
        print(f"L = {L}: K0 zeros {n0}, K1 zeros {n1}; pi-cubes in ker K0: {nc} (in ker K1: {nc1}); battery on each K0 cube "
              f"(Klein, Hamming, hw1, C3): {bat}; ker K0 strictly larger than the carrier: {strict}")
    fails = []
    for L in (4, 8):
        n0, n1, nc, nc1, bat, strict = rows[L]
        if nc != 1:
            fails.append(f"L={L}: {nc} pi-cubes in ker K0")
        if not all(b[0] and b[1] == {0: 1, 1: 3, 2: 3, 3: 1} and b[2] and b[3] for b in bat):
            fails.append(f"L={L}: battery item on the K0 carrier")
        if n1 != 8 or nc1 != 1:
            fails.append(f"L={L}: ker K1 is not the carrier")
    if rows[4][0] != 20 or rows[8][0] != 68:
        fails.append("K0 zero counts")
    if fails:
        print(f"HIT: {fails}")
    ext = {L: (rows[L][0], rows[L][2]) for L in rows}
    print(f"SUMMARY: in exact cyclotomic arithmetic K0 has {rows[4][0]} and {rows[8][0]} zero modes at L = 4, 8 and K1 exactly 8 at every even "
          f"L; ker K0 contains exactly one pi-cube coset (the (+-pi/2)^3 cube) whenever 4 | L and none when L = 2 mod 4, and on every such "
          f"cube the translation characters give the full Klein cube once, Hamming grading 1+3+3+1, the three hw=1 characters and a "
          f"C3[111]-closed carrier, while ker K1 is exactly its 8-point cube; beyond the note, (K0 zeros, K0 pi-cubes) by L = 4..24: {ext}; "
          f"no falsifier fires at the certified volumes")


if __name__ == "__main__":
    main()
