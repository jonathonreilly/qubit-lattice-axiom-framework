"""STAGE 2 -- acceptance test: flat Minkowski must have zero deficit at every hinge."""
import math
import sys
from collections import defaultdict

import numpy as np

from lorentzian_angles import HingeFrame
from star import eval_star
from torus import kuhn_simplices, hinge_stars, star_is_complete, coords

TWOPI = 2.0 * math.pi


def run(B, N=3, label="", verbose=True):
    """B = lattice basis (columns = lattice vectors, Minkowski coords).
    Fundamental domain = cells {0..N-1}^4; surrounding cells supply the stars."""
    sims = kuhn_simplices(-2, N + 2)
    dom = set(range(N))

    def keep(tri):
        base = tuple(min(v[i] for v in tri) for i in range(4))
        return all(b in dom for b in base)

    star = hinge_stars(sims, keep)
    X = coords(B)
    pos = {}

    def P(n):
        if n not in pos:
            pos[n] = X(n)
        return pos[n]

    r = dict(n=0, nE=0, nL=0, nNullHinge=0, nIncomplete=0, nNullRayHinges=0,
             maxE=0.0, maxL=0.0, maxboost=0.0, maxbranch=0.0,
             cross=defaultdict(int), fail=0)

    for hinge, entries in star.items():
        r["n"] += 1
        if not star_is_complete(hinge, entries):
            r["nIncomplete"] += 1
            continue
        a, b, c = hinge
        fr = HingeFrame(P(b) - P(a), P(c) - P(a))
        if fr.kind == "N":
            r["nNullHinge"] += 1
            continue
        try:
            tot, m, nnull, worst = eval_star(fr, entries, P, a)
        except ValueError as ex:
            r["fail"] += 1
            continue
        r["maxbranch"] = max(r["maxbranch"], worst)
        delta = TWOPI - tot
        if fr.kind == "E":
            r["nE"] += 1
            r["maxE"] = max(r["maxE"], abs(delta))
        else:
            r["nL"] += 1
            r["cross"][m] += 1
            if nnull:
                r["nNullRayHinges"] += 1
            r["maxboost"] = max(r["maxboost"], abs(tot.imag))
            r["maxL"] = max(r["maxL"], abs(delta))

    if verbose:
        print("=" * 74)
        print("STAGE 2  %s" % label)
        print("  hinges in fundamental domain : %d   (incomplete stars %d, "
              "bookkeeping failures %d)" % (r["n"], r["nIncomplete"], r["fail"]))
        print("  null-PLANE hinges (angle genuinely undefined) : %d" % r["nNullHinge"])
        print("  EUCLIDEAN-orthogonal hinges (timelike hinge)  : %d" % r["nE"])
        print("      max|deficit|        = %.3e" % r["maxE"])
        print("  LORENTZIAN-orthogonal hinges (spacelike hinge): %d"
              "   (of which %d have lightlike bounding rays)"
              % (r["nL"], r["nNullRayHinges"]))
        print("      max|deficit|        = %.3e" % r["maxL"])
        print("      max|sum of boosts|  = %.3e" % r["maxboost"])
        print("      light-cone crossings per hinge: %s" % dict(sorted(r["cross"].items())))
        print("  cos+sin self-check max|cos,sin identities| = %.3e" % r["maxbranch"])
    return r


CASES = {}
CASES["A"] = (np.eye(4), "A: literal eta=diag(-1,1,1,1), unit cubic lattice")
CASES["B"] = (np.diag([0.6, 1.0, 1.0, 1.0]),
              "B: generic time spacing a_t=0.6 (still exactly flat)")
_rng = np.random.default_rng(20260829)
CASES["C"] = (np.eye(4) + 0.35 * _rng.standard_normal((4, 4)),
              "C: generic sheared/boosted flat lattice")

if __name__ == "__main__":
    which = sys.argv[1:] or ["A", "B", "C"]
    for k in which:
        B, lab = CASES[k]
        run(B, label=lab)
