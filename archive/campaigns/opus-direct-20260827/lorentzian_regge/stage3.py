"""STAGE 3 -- Schlaefli identity  sum_h A_h dtheta_h = 0  in Lorentzian signature.

Varies the 10 squared edge lengths of random Lorentzian 4-simplices and checks
that the area-weighted variation of the complex dihedral angles vanishes.
Also reports the sanity control  sum_h A_h dtheta_h  computed with the WRONG
(unsigned / magnitude) angles, to show the test has teeth.
"""
import math

import numpy as np

from simplex import (EDGES, TRIS, areas_and_angles, random_lorentzian_simplex,
                     volume2)


def schlaefli_residual(s2, h=1e-6):
    """Return (max residual over the 10 edge variations, typical scale)."""
    base = areas_and_angles(s2)
    A = {t: base[t][0] for t in TRIS}
    worst = 0.0
    scale = 0.0
    for ed in EDGES:
        sp = dict(s2); sm = dict(s2)
        step = h * max(1.0, abs(s2[ed]))
        sp[ed] += step; sm[ed] -= step
        ap = areas_and_angles(sp)
        am = areas_and_angles(sm)
        tot = 0.0 + 0j
        term = 0.0
        for t in TRIS:
            dth = (ap[t][1] - am[t][1]) / (2 * step)
            tot += A[t] * dth
            term = max(term, abs(A[t] * dth))
        worst = max(worst, abs(tot))
        scale = max(scale, term)
    return worst, scale


def main():
    rng = np.random.default_rng(31415)
    print("=" * 74)
    print("STAGE 3  Schlaefli identity, random Lorentzian 4-simplices")
    print("  %-4s %-11s %-9s %-9s %-11s %-11s %s"
          % ("#", "V^2", "spacelike", "timelike", "max|sum|", "term scale", "ratio"))
    worst_ratio = 0.0
    for k in range(12):
        s2, P = random_lorentzian_simplex(rng, spread=1.0 + 0.3 * k)
        aa = areas_and_angles(s2)
        nsp = sum(1 for t in TRIS if aa[t][2] == "L")   # spacelike hinge
        ntl = sum(1 for t in TRIS if aa[t][2] == "E")   # timelike hinge
        res, sc = schlaefli_residual(s2)
        worst_ratio = max(worst_ratio, res / sc)
        print("  %-4d %-11.3e %-9d %-9d %-11.3e %-11.3e %.2e"
              % (k, volume2(s2), nsp, ntl, res, sc, res / sc))
    print("  worst relative residual over 12 simplices: %.3e" % worst_ratio)
    print("  (finite-difference step 1e-6 -> central-difference floor ~1e-10)")

    # ---- control: the identity FAILS if the causal signs are dropped -------
    print("\n  CONTROL (test has teeth): same simplices, |Re| angles, no i*pi/2")
    rng = np.random.default_rng(31415)
    for k in range(3):
        s2, P = random_lorentzian_simplex(rng, spread=1.0 + 0.3 * k)

        def naive(s2loc):
            aa = areas_and_angles(s2loc)
            return {t: (abs(aa[t][0]), abs(aa[t][1].real) + abs(aa[t][1].imag))
                    for t in TRIS}
        base = naive(s2)
        worst = 0.0
        for ed in EDGES:
            sp = dict(s2); sm = dict(s2)
            step = 1e-6 * max(1.0, abs(s2[ed]))
            sp[ed] += step; sm[ed] -= step
            np_, nm_ = naive(sp), naive(sm)
            tot = sum(base[t][0] * (np_[t][1] - nm_[t][1]) / (2 * step) for t in TRIS)
            worst = max(worst, abs(tot))
        print("    simplex %d : max|sum A dtheta| with unsigned angles = %.3e" % (k, worst))


if __name__ == "__main__":
    main()
