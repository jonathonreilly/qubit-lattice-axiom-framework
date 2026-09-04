"""Kuhn (Freudenthal) triangulated flat 4-torus, Lorentzian signature."""
import itertools
from collections import defaultdict

import numpy as np

E4 = np.eye(4, dtype=int)


def kuhn_simplices(lo, hi):
    """All Kuhn 4-simplices of the unit cells n in [lo,hi)^4. Vertices are
    integer lattice points (tuples)."""
    sims = []
    perms = list(itertools.permutations(range(4)))
    for n in itertools.product(range(lo, hi), repeat=4):
        n = np.array(n)
        for perm in perms:
            vs = [tuple(int(z) for z in n)]
            cur = n.copy()
            for k in perm:
                cur = cur + E4[k]
                vs.append(tuple(int(z) for z in cur))
            sims.append(tuple(vs))
    return sims


def hinge_stars(sims, keep):
    """triangle -> list of (simplex, (d,e)).  `keep(tri)` selects the hinges."""
    star = defaultdict(list)
    for s in sims:
        for tri in itertools.combinations(range(5), 3):
            key = tuple(sorted(s[i] for i in tri))
            if not keep(key):
                continue
            others = tuple(s[i] for i in range(5) if i not in tri)
            star[key].append((s, others))
    return star


def star_is_complete(hinge, entries):
    """Each tetrahedron (hinge + one apex) must be shared by exactly two
    simplices of the star -- i.e. the wedges close up into a cycle."""
    cnt = defaultdict(int)
    for _, (d, e) in entries:
        cnt[d] += 1
        cnt[e] += 1
    return all(v == 2 for v in cnt.values())


def coords(B):
    """lattice point -> Minkowski 4-vector, using lattice basis matrix B."""
    Bf = np.asarray(B, dtype=float)

    def f(n):
        return Bf @ np.array(n, dtype=float)
    return f
