"""STAGE 4 -- the flat Lorentzian complex is a stationary point of S = sum A*delta.

Everything here runs on SQUARED EDGE LENGTHS ONLY: each 4-simplex is
reconstructed independently from its own 10 s_ij, so there is no global
embedding anywhere.  (That is forced -- once an edge is perturbed the complex
is no longer embeddable.)  It also proves the wedge angle is intrinsic: each
simplex around a hinge gets its own frame, related to its neighbours' by an
unknown boost, yet the deficits still cancel exactly.

Uses lattice case B (generic time spacing), which has no lightlike rays.
"""
import itertools
import math
from collections import defaultdict

import numpy as np

from lorentzian_angles import HingeFrame, wedge_angle, sqrt_mi0, ip, gram
from simplex import embed
from torus import kuhn_simplices, hinge_stars, star_is_complete, coords

TWOPI = 2.0 * math.pi
B_LATTICE = np.diag([0.6, 1.0, 1.0, 1.0])
N = 3


def build(Nl=N):
    sims = kuhn_simplices(-2, Nl + 2)
    dom = set(range(Nl))

    def keep(tri):
        base = tuple(min(v[i] for v in tri) for i in range(4))
        return all(b in dom for b in base)

    star = hinge_stars(sims, keep)
    star = {h: e for h, e in star.items() if star_is_complete(h, e)}
    X = coords(B_LATTICE)
    s2 = {}
    for s in sims:
        for u, v in itertools.combinations(s, 2):
            k = (u, v) if u < v else (v, u)
            if k not in s2:
                d = X(v) - X(u)
                s2[k] = ip(d, d)
    return sims, star, s2


def key(u, v):
    return (u, v) if u < v else (v, u)


def affected_stars(sims, edge):
    """Every hinge whose deficit or area can move when `edge` moves, with its
    FULL star.  The Schlaefli cancellation needs all 10 triangles of every
    simplex containing the edge -- dropping even one breaks stationarity."""
    sw = [s for s in sims if edge[0] in s and edge[1] in s]
    want = set()
    for s in sw:
        for tri in itertools.combinations(s, 3):
            want.add(tuple(sorted(tri)))
    st = defaultdict(list)
    for s in sims:
        for tri in itertools.combinations(range(5), 3):
            k = tuple(sorted(s[i] for i in tri))
            if k in want:
                st[k].append((s, tuple(s[i] for i in range(5) if i not in tri)))
    bad = [k for k in want
           if k not in st or not star_is_complete(k, st[k])]
    return dict(st), len(sw), bad


def local_s2(sim, s2):
    return {(i, j): s2[key(sim[i], sim[j])]
            for i, j in itertools.combinations(range(5), 2)}


def wedge_from_lengths(sim, hinge, others, s2):
    """Complex dihedral angle of one wedge, from that simplex's 10 lengths."""
    P = embed(local_s2(sim, s2))
    idx = {v: i for i, v in enumerate(sim)}
    a, b, c = hinge
    d, e = others
    ia, ib, ic, id_, ie = idx[a], idx[b], idx[c], idx[d], idx[e]
    fr = HingeFrame(P[ib] - P[ia], P[ic] - P[ia])
    if fr.kind == "N":
        raise ValueError("null hinge plane")
    D, E = fr.project(P[id_] - P[ia]), fr.project(P[ie] - P[ia])
    th, _ = wedge_angle(fr, D, E)
    return th, fr.kind


def hinge_area_from_lengths(hinge, s2):
    a, b, c = hinge
    sab, sac, sbc = s2[key(a, b)], s2[key(a, c)], s2[key(b, c)]
    G = np.array([[sab, 0.5 * (sab + sac - sbc)],
                  [0.5 * (sab + sac - sbc), sac]])
    return 0.5 * sqrt_mi0(float(np.linalg.det(G)))


def deficit(hinge, entries, s2):
    tot = 0.0 + 0j
    kind = None
    for sim, others in entries:
        th, kind = wedge_from_lengths(sim, hinge, others, s2)
        tot += th
    return TWOPI - tot, kind


def main():
    sims, star, s2 = build()
    print("=" * 74)
    print("STAGE 4  stationarity of S = sum_h A_h delta_h  (lattice case B)")
    print("  simplices %d, hinges with complete stars %d" % (len(sims), len(star)))

    # ---- (c) intrinsic cross-check: deficits from squared lengths alone ----
    mx = {"E": 0.0, "L": 0.0}
    cnt = defaultdict(int)
    for h, e in star.items():
        d, k = deficit(h, e, s2)
        mx[k] = max(mx[k], abs(d))
        cnt[k] += 1
    print("\n  INTRINSIC CHECK (per-simplex reconstruction, no global embedding)")
    print("    Euclidean-orthogonal  %4d hinges : max|deficit| = %.3e"
          % (cnt["E"], mx["E"]))
    print("    Lorentzian-orthogonal %4d hinges : max|deficit| = %.3e"
          % (cnt["L"], mx["L"]))

    # ---- (a) teeth: a perturbed edge must give NONZERO deficits -----------
    interior = [e for e in sorted(s2.keys())
                if all(c in (1, 2) for v in e for c in v)]
    edge = interior[len(interior) // 2]
    aff, nsim, bad = affected_stars(sims, edge)
    print("\n  CURVED CONTROL: perturb one squared edge length by eps")
    print("    edge %s -> %s   (in %d simplices, %d affected hinges, "
          "%d incomplete)" % (edge[0], edge[1], nsim, len(aff), len(bad)))

    def action(eps, aff=aff, edge=edge):
        sp = dict(s2)
        sp[edge] = s2[edge] + eps
        S = 0.0 + 0j
        worst = 0.0
        for h, ent in aff.items():
            d, _ = deficit(h, ent, sp)
            S += hinge_area_from_lengths(h, sp) * d
            worst = max(worst, abs(d))
        return S, worst

    for eps in (0.0, 1e-3, 1e-2, 1e-1):
        _, w = action(eps)
        print("      eps=%-8.0e max|deficit| over affected hinges = %.3e" % (eps, w))

    # ---- (b) stationarity --------------------------------------------------
    print("\n  STATIONARITY  S = sum_h A_h delta_h   (S(0) = %s)"
          % np.round(action(0.0)[0], 15))
    print("    %-9s %-14s %-14s %s" % ("eps", "|dS/deps|", "|d2S/deps2|", "ratio"))
    S0 = action(0.0)[0]
    for eps in (1e-2, 1e-3, 1e-4, 1e-5):
        Sp = action(eps)[0]
        Sm = action(-eps)[0]
        d1 = (Sp - Sm) / (2 * eps)
        d2 = (Sp + Sm - 2 * S0) / eps ** 2
        print("    %-9.0e %-14.3e %-14.3e %.2e"
              % (eps, abs(d1), abs(d2), abs(d1) / max(abs(d2), 1e-300)))

    # ---- stationarity in EVERY edge direction ------------------------------
    print("\n  dS/deps for 12 independent edge directions (eps=1e-3)")
    rng = np.random.default_rng(5)
    picks = [interior[i] for i in rng.choice(len(interior),
                                             min(12, len(interior)), replace=False)]
    w1 = w2 = 0.0
    for ed in picks:
        a2, _, bad2 = affected_stars(sims, ed)
        if bad2:
            print("    skipped %s (incomplete stars)" % (ed,))
            continue

        def act(eps, a2=a2, ed=ed):
            sp = dict(s2)
            sp[ed] = s2[ed] + eps
            return sum(hinge_area_from_lengths(h, sp) * deficit(h, e_, sp)[0]
                       for h, e_ in a2.items())
        e0 = 1e-3
        d1 = abs((act(e0) - act(-e0)) / (2 * e0))
        d2 = abs((act(e0) + act(-e0) - 2 * act(0.0)) / e0 ** 2)
        w1, w2 = max(w1, d1), max(w2, d2)
    print("    max |dS/deps|    = %.3e   <- must vanish" % w1)
    print("    max |d2S/deps^2| = %.3e   <- must NOT vanish" % w2)


if __name__ == "__main__":
    main()
