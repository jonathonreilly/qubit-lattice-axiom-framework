"""Unit test of the complex-angle machinery on a bare Minkowski 2-plane."""
import math
import numpy as np
from lorentzian_angles import HingeFrame, wedge_angle, check_wedge_branch, ip

# hinge = span(e2,e3) (spacelike)  ->  Pperp = span(e0,e1) is Lorentzian
p1 = np.array([0.0, 0, 1, 0])
p2 = np.array([0.0, 0, 0, 1])
fr = HingeFrame(p1, p2)
print("hinge kind:", fr.kind, " detGperp = %.3f" % fr.detGperp)

rng = np.random.default_rng(7)


def ray(t, x):
    return np.array([t, x, 0.0, 0.0])


def tile_sum(rays):
    """rays given in counter-clockwise order around the origin; sum wedges."""
    tot = 0.0 + 0j
    cross = 0
    worst = 0.0
    n = len(rays)
    for i in range(n):
        D, E = rays[i], rays[(i + 1) % n]
        dphi, cr = wedge_angle(fr, D, E)
        worst = max(worst, check_wedge_branch(fr, D, E, dphi))
        tot += dphi
        cross += cr
    return tot, cross, worst


# --- test 1: the four coordinate rays -------------------------------------
rays = [ray(0, 1), ray(1, 0), ray(0, -1), ray(-1, 0)]
print("4 axis rays          :", tile_sum(rays))

# --- test 2: many random rays, sorted counter-clockwise --------------------
for trial in range(5):
    ang = np.sort(rng.uniform(0, 2 * math.pi, 12))
    # avoid landing on the light cone
    ang = ang[np.min(np.abs(((ang[:, None] - np.array([0.25, 0.75, 1.25, 1.75]) * math.pi)
                             + math.pi) % (2 * math.pi) - math.pi), axis=1) > 1e-3]
    rs = [ray(math.sin(a), math.cos(a)) * rng.uniform(0.3, 3.0) for a in ang]
    tot, cross, worst = tile_sum(rs)
    print("random %d rays        : sum=%s  crossings=%d  branch_err=%.2e"
          % (len(rs), np.round(tot, 14), cross, worst))

# --- test 3: Euclidean-orthogonal hinge for comparison ---------------------
# hinge = span(e0,e1) (timelike) -> Pperp = span(e2,e3) is Euclidean
frE = HingeFrame(np.array([1.0, 0, 0, 0]), np.array([0.0, 1, 0, 0]))
print("timelike hinge kind:", frE.kind)
tot = 0.0
angs = np.sort(rng.uniform(0, 2 * math.pi, 9))
rsE = [np.array([0.0, 0.0, math.cos(a), math.sin(a)]) * rng.uniform(.3, 3) for a in angs]
for i in range(len(rsE)):
    dphi, cr = wedge_angle(frE, rsE[i], rsE[(i + 1) % len(rsE)])
    tot += dphi
print("Euclidean-orthogonal sum:", tot, " (2pi = %.15f)" % (2 * math.pi))
