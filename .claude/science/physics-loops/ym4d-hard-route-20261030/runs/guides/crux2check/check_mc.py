# Heat-bath guide for (4), (8) and (9) on a small periodic 4-torus.
# Guide only: a finite sample on a small torus proves nothing.
import math
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quat import *  # noqa
from trees import random_spanning_tree, transport_frame  # noqa

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
therm = int(sys.argv[2]) if len(sys.argv) > 2 else 60
nmeas = int(sys.argv[3]) if len(sys.argv) > 3 else 20
gap = 3


def sw_hol(lat, x):
    """holonomy based at x of the south-west square in plane (1,2)."""
    U = lat.U
    xm1 = lat.sh(x, 0, -1)
    xm12 = lat.sh(xm1, 1, -1)
    xm2 = lat.sh(x, 1, -1)
    # x -> x-e1 -> x-e1-e2 -> x-e2 -> x
    return qmul(qmul(qmul(qconj(U[(xm1, 0)]), qconj(U[(xm12, 1)])), U[(xm12, 0)]), U[(xm2, 1)])


for b in [2.3, 2.6]:
    rng = random.Random(int(1000*b))
    lat = Lattice([L]*4, rng=rng, cold=False)
    for s in range(therm):
        lat.sweep(b, rng)
    delta = 1/(8*(1+6*b))
    lam_sum = 0.0
    lam_min = 1e9
    nsite = 0
    good_nesw = 0
    good_1234 = 0
    plaq = 0.0
    c9 = []
    for m in range(nmeas):
        for s in range(gap):
            lat.sweep(b, rng)
        plaq += lat.mean_plaq()
        for x in lat.sites:
            fw = [im(lat.plaq(x, mu, nu)) for mu in range(4) for nu in range(mu+1, 4)]
            lam = lam_min_cross(fw)
            lam_sum += lam
            lam_min = min(lam_min, lam)
            nsite += 1
            u1 = im(lat.plaq(x, 0, 1))
            u2 = im(sw_hol(lat, x))
            if 4*lam_min_cross([u1, u2]) >= delta:
                good_nesw += 1
            if 4*lam_min_cross([im(lat.plaq(x, 0, 1)), im(lat.plaq(x, 2, 3))]) >= delta:
                good_1234 += 1
        # (9) guide on the whole torus: min over v of (1/V) sum_z |div j|^2 / b^2
        if m % 4 == 0:
            for t in range(3):
                tree = random_spanning_tree(lat, rng)
                root = lat.sites[0]
                n, g = transport_frame(lat, tree, root, (1.0, 0.0, 0.0))
                latg = Lattice(lat.sides, cold=True)
                for (x, mu) in lat.U:
                    yv = lat.sh(x, mu)
                    latg.U[(x, mu)] = qmul(qmul(g[x], lat.U[(x, mu)]), qconj(g[yv]))
                Bs = []
                for z in latg.sites:
                    B = (0.0, 0.0, 0.0)
                    for mu in range(4):
                        tt = latg.sh(z, mu, -1)
                        Nf = latg.force(tt, mu, b)
                        B = vadd(B, vsub(ad_inv(latg.U[(tt, mu)], Nf), Nf))
                    Bs.append(B)
                ev = sym3_eigs(outer_sum(Bs))
                c9.append(ev[0]/(len(latg.sites)*b*b))
    print("b=%.1f L=%d: <(1/2)tr U_p>=%.4f  E lambda_x=%.4f (min seen %.4f; bound (8) %.6f)"
          % (b, L, plaq/nmeas, lam_sum/nsite, lam_min, 1/(64*(1+6*b))))
    print("        P{D>=delta_b}: NE/SW pair %.4f, forward 12/34 pair %.4f (bound 1/2); delta_b=%.5f"
          % (good_nesw/nsite, good_1234/nsite, delta))
    print("        (9) guide, whole torus, random trees: min_v (1/V)sum|div j|^2/b^2: min %.4f, mean %.4f over %d trees"
          % (min(c9), sum(c9)/len(c9), len(c9)))
