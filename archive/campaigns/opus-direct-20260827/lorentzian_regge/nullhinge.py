"""What happens at the 1458 null-PLANE hinges of the literal unit lattice?

At a_t = 1 exactly, 1458 of the 4050 hinges have a 2-plane tangent to the light
cone.  Their induced metric is degenerate, so no dihedral angle exists there.
Their AREA is also exactly zero, so the question is whether the action density
A_h * delta_h has a finite limit (harmless removable degeneracy) or blows up.
Approach a_t -> 1 and watch.
"""
import math

import numpy as np

from lorentzian_angles import HingeFrame
from star import eval_star
from torus import kuhn_simplices, hinge_stars, star_is_complete, coords
from lorentzian_angles import sqrt_mi0, gram

TWOPI = 2.0 * math.pi
N = 3


def run(at):
    sims = kuhn_simplices(-2, N + 2)
    dom = set(range(N))

    def keep(tri):
        return all(min(v[i] for v in tri) in dom for i in range(4))

    star = hinge_stars(sims, keep)
    X = coords(np.diag([at, 1.0, 1.0, 1.0]))
    pos = {}

    def P(n):
        if n not in pos:
            pos[n] = X(n)
        return pos[n]

    # hinges that are null-plane AT at=1 exactly
    X1 = coords(np.eye(4))
    out = []
    for hinge, entries in star.items():
        if not star_is_complete(hinge, entries):
            continue
        a, b, c = hinge
        g = np.linalg.det(gram([X1(b) - X1(a), X1(c) - X1(a)]))
        if abs(g) > 1e-9:
            continue                       # not one of the degenerate ones
        fr = HingeFrame(P(b) - P(a), P(c) - P(a))
        if fr.kind == "N":
            continue
        try:
            tot, m, nn, _ = eval_star(fr, entries, P, a)
        except ValueError:
            continue
        delta = TWOPI - tot
        A = 0.5 * sqrt_mi0(float(np.linalg.det(gram([P(b) - P(a), P(c) - P(a)]))))
        out.append((abs(delta), abs(A), abs(A * delta), m))
    return out


print("=" * 74)
print("Null-plane hinges of the unit lattice: behaviour as a_t -> 1")
print("  %-10s %-7s %-13s %-13s %-13s %s"
      % ("a_t", "n", "max|delta|", "max|A|", "max|A*delta|", "crossings"))
for at in (0.9, 0.99, 0.999, 0.9999, 0.99999):
    o = run(at)
    if not o:
        print("  %-10s none resolved" % at)
        continue
    cr = sorted({x[3] for x in o})
    print("  %-10s %-7d %-13.4e %-13.4e %-13.4e %s"
          % (at, len(o), max(x[0] for x in o), max(x[1] for x in o),
             max(x[2] for x in o), cr))
