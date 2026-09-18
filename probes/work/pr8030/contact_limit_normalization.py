#!/usr/bin/env python3
"""J:attack:PR8030 - uniform weak continuum-boundary note (PR #8030), attack pattern (f) NORMALIZATION: the exact u = 0 contact
construction and its constants, recomputed by brute force with the SU(3) Weyl integration formula (disjoint from the note's Schur
orthogonality argument):
  * J = ReTr(U)/3 for a Haar SU(3) holonomy: E J = 0, E J^2 = 1/18, X = sqrt18 J with E X^2 = 1 and |X| <= B = sqrt18 (the maximum at
    U = I); E X^3 (the skew the note keeps as evidence) and E X^4, from exact trigonometric-polynomial quadrature on the maximal torus;
  * the characteristic function phi(z) = E e^{izX} by 400 x 400 torus quadrature (spectrally accurate): the stated remainders
    |phi(z) - 1 + z^2/2| <= B|z|^3/6 for all z, and for |z| <= 1/(2B): |w| <= 1/72, |log(1+w) - w| <= |w|^2 <= z^4 and
    |log phi(z) + z^2/2| <= (7B/36)|z|^3 <= (B/4)|z|^3, with 7B/36 = B/6 + 1/(2B) exactly (B^2 = 18);
  * the finite-mesh statements for f = 1 on the unit box: the variance of F_n(1) is exactly 1, and |log(phi(n^-3/2)^(n^3)) + 1/2| obeys the
    product bound (B/4) n^3 n^(-9/2) = (B/4) n^(-3/2), n up to 10^6; the error is about 0.12 n^-3/2 while n^3 log phi carries a
    double-precision rounding of about n^3 * 1e-16, so this check runs in 60-digit mpmath on a 64 x 64 Weyl grid (exact for trigonometric
    polynomials of degree < 64; the Taylor tail of e^{izX} past degree 59 is below 1.5^60/60! < 1e-70 for z <= 2^-3/2), cross-checked
    against the double-precision quadrature where that is resolved (n <= 100);
  * the sampled plaquettes are link-disjoint: xy plaquettes anchored at 2k (main construction) and at 3k (independent proof) for all
    k in {0..5}^3, with the repeated-plaquette adverse case (covariance 1);
  * the scale ratio of section 5: V/G = (32 e ell u/(a b))/(2/(a b)) = 16 e ell u, symbolically.
HIT if a stated constant or bound fails.
"""
import itertools
import math
import sys
import time

import numpy as np


def torus_average(fn, n=400):
    a = 2 * np.pi * np.arange(n) / n
    A, Bm = np.meshgrid(a, a, indexing="ij")
    z1, z2, z3 = np.exp(1j * A), np.exp(1j * Bm), np.exp(-1j * (A + Bm))
    vd = np.abs((z1 - z2) * (z1 - z3) * (z2 - z3)) ** 2
    tr = z1 + z2 + z3
    return np.sum(vd * fn(tr)) / (6 * n * n)


def main():
    t0 = time.time()
    hits = []
    B = math.sqrt(18)
    one = torus_average(lambda tr: np.ones_like(tr.real), 48).real
    EJ = torus_average(lambda tr: tr.real / 3, 48).real
    EJ2 = torus_average(lambda tr: (tr.real / 3) ** 2, 48).real
    EJ3 = torus_average(lambda tr: (tr.real / 3) ** 3, 48).real
    EJ4 = torus_average(lambda tr: (tr.real / 3) ** 4, 48).real
    EX2, EX3, EX4 = 18 * EJ2, 18 ** 1.5 * EJ3, 18 ** 2 * EJ4
    print(f"[moments] Weyl quadrature (exact for these trigonometric polynomials): normalization {one:.15f}, E J = {EJ:.1e}, E J^2 = {EJ2:.15f} "
          f"(1/18 = {1 / 18:.15f}), E X^2 = {EX2:.15f}, E X^3 = {EX3:.12f} (= sqrt18/6 = {B / 6:.12f}), E X^4 = {EX4:.12f}")
    ok = abs(one - 1) < 1e-12 and abs(EJ) < 1e-12 and abs(EJ2 - 1 / 18) < 1e-14 and abs(EX2 - 1) < 1e-12
    a = np.linspace(0, 2 * np.pi, 721)
    AA, BB = np.meshgrid(a, a)
    rt = (np.cos(AA) + np.cos(BB) + np.cos(AA + BB)) / 3
    print(f"[bound] max |ReTr U/3| over a 721^2 torus grid = {np.abs(rt).max():.15f} (attained at U = I): |X| <= B = sqrt18 = {B:.12f}")
    ok = ok and np.abs(rt).max() <= 1 + 1e-15
    if not ok:
        hits.append(f"moments or bound: E J = {EJ}, E J^2 = {EJ2}, E X^2 = {EX2}, max |ReTr/3| = {np.abs(rt).max()}")
    # characteristic function and the remainders
    worst_taylor, worst_w, worst_log, worst_log2 = 0.0, 0.0, 0.0, 0.0
    zs = np.concatenate([np.linspace(-3, 3, 121), np.linspace(-1 / (2 * B), 1 / (2 * B), 81)])
    for z in zs:
        phi = torus_average(lambda tr: np.exp(1j * z * B * tr.real / 3))
        if abs(z) > 0:
            worst_taylor = max(worst_taylor, abs(phi - 1 + z * z / 2) / (B * abs(z) ** 3 / 6))
        if 0 < abs(z) <= 1 / (2 * B) + 1e-15:
            w = phi - 1
            worst_w = max(worst_w, abs(w) / (1 / 72), abs(w) / z ** 2)
            worst_log = max(worst_log, abs(np.log(1 + w) - w) / abs(w) ** 2 if abs(w) > 0 else 0, abs(np.log(1 + w) - w) / z ** 4)
            worst_log2 = max(worst_log2, abs(np.log(phi) + z * z / 2) / (7 * B / 36 * abs(z) ** 3))
    const_ok = abs((B / 6 + 1 / (2 * B)) - 7 * B / 36) < 1e-15 and 7 * B / 36 <= B / 4
    print(f"[phi] 202 values of z: max |phi - 1 + z^2/2| / (B|z|^3/6) = {worst_taylor:.6f}; for |z| <= 1/(2B): max |w|/(1/72 or z^2) = "
          f"{worst_w:.6f}, max |log(1+w) - w| / (|w|^2 or z^4) = {worst_log:.6f}, max |log phi + z^2/2| / ((7B/36)|z|^3) = {worst_log2:.6f} "
          f"(all must be <= 1); B/6 + 1/(2B) = 7B/36 <= B/4: {const_ok}  ({time.time() - t0:.0f}s)")
    if max(worst_taylor, worst_w, worst_log, worst_log2) > 1 + 1e-9 or not const_ok:
        hits.append(f"Taylor/log remainders: {worst_taylor}, {worst_w}, {worst_log}, {worst_log2}, constants {const_ok}")
    # finite mesh, f = 1, in 60-digit arithmetic (n^3 log phi is below double-precision resolution for n >~ 10^3)
    import mpmath as mp
    mp.mp.dps = 60
    m = 64
    grid = []
    for i in range(m):
        for j in range(m):
            ai, bj = 2 * mp.pi * i / m, 2 * mp.pi * j / m
            w1, w2, w3 = mp.expj(ai), mp.expj(bj), mp.expj(-(ai + bj))
            grid.append((abs((w1 - w2) * (w1 - w3) * (w2 - w3)) ** 2, mp.sqrt(18) * mp.re(w1 + w2 + w3) / 3))

    def phi_mp(z):
        return mp.fsum(v * mp.expj(z * x) for v, x in grid) / (6 * m * m)

    norm_mp = phi_mp(0)
    rows = []
    worst_prod, worst_agree = 0.0, 0.0
    for n in (2, 5, 10, 30, 100, 1000, 10000, 100000, 1000000):
        z = 1 / (mp.mpf(n) * mp.sqrt(n))
        phi = phi_mp(z)
        err = abs(n ** 3 * mp.log(phi) + mp.mpf(1) / 2)
        bound = mp.sqrt(18) / 4 * z
        worst_prod = max(worst_prod, float(err / bound))
        if n <= 100:
            phi_f = torus_average(lambda tr: np.exp(1j * float(z) * B * tr.real / 3))
            worst_agree = max(worst_agree, abs(complex(phi) - phi_f))
        rows.append(f"n={n}: |log prod + 1/2| = {mp.nstr(err, 4)} vs (B/4) n^-3/2 = {mp.nstr(bound, 4)} (ratio {mp.nstr(err / bound, 4)})")
    print(f"[mesh f=1] 60-digit Weyl grid 64^2: normalization - 1 = {mp.nstr(norm_mp - 1, 3)}; double vs 60-digit phi at n <= 100: max "
          f"|difference| = {worst_agree:.1e}; variance n^-3 * n^3 * E X^2 = {EX2:.15f} at every n; " + "; ".join(rows))
    if worst_prod > 1 + 1e-9 or abs(norm_mp - 1) > mp.mpf(10) ** -50:
        hits.append(f"product bound exceeded: ratio {worst_prod} (normalization {norm_mp})")
    # disjointness of the sampled plaquettes
    def plaquette_links(anchor):
        x, y, z = anchor
        return {((x, y, z), (x + 1, y, z)), ((x + 1, y, z), (x + 1, y + 1, z)), ((x, y + 1, z), (x + 1, y + 1, z)), ((x, y, z), (x, y + 1, z))}
    disj = {}
    for sp in (2, 3):
        links = [plaquette_links(tuple(sp * c for c in k)) for k in itertools.product(range(6), repeat=3)]
        allf = [l for L in links for l in L]
        disj[sp] = len(allf) == len(set(allf))
    print(f"[plaquettes] anchors at 2k: link-disjoint for k in {{0..5}}^3: {disj[2]}; anchors at 3k: {disj[3]}; adjacent anchors at spacing 1 "
          f"share a link: {bool(plaquette_links((0, 0, 0)) & plaquette_links((1, 0, 0)))}; a repeated plaquette gives Cov(X, X) = E X^2 = {EX2:.12f}")
    if not (disj[2] and disj[3]):
        hits.append(f"sampled plaquettes not link-disjoint: spacing 2 {disj[2]}, spacing 3 {disj[3]}")
    # section 5
    import sympy as sp_
    e, ell, u, a_, b_ = sp_.symbols("e ell u a b", positive=True)
    ratio = sp_.simplify((32 * e * ell * u / (a_ * b_)) / (2 / (a_ * b_)))
    print(f"[scale] V/G = {ratio} (the note: 16 e ell u)")
    if sp_.simplify(ratio - 16 * e * ell * u) != 0:
        hits.append(f"scale ratio {ratio}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - the u = 0 contact construction recomputed with the Weyl integration formula: E J = 0, "
          f"E J^2 = 1/18, E X^2 = 1, |X| <= sqrt18, E X^3 = sqrt18/6 (skew); the remainders |phi - 1 + z^2/2| <= B|z|^3/6, |w| <= 1/72, "
          f"|log(1+w) - w| <= z^4 and |log phi + z^2/2| <= (7B/36)|z|^3 hold at 202 values of z (largest ratios {worst_taylor:.3f}, {worst_w:.3f}, "
          f"{worst_log:.3f}, {worst_log2:.3f}); the f = 1 product error is within (B/4) n^-3/2 to n = 10^6 in 60-digit arithmetic (largest ratio {worst_prod:.3f}); the "
          f"sampled plaquettes are link-disjoint at spacings 2 and 3; V/G = 16 e ell u; {len(hits)} failures; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
