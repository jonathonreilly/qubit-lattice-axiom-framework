#!/usr/bin/env python3
"""K4b: robustness of K4's path-induced O(e^2) TT stiffness.
 (i) photon IR regulator mu -> 0 (gauge invariance restored as mu -> 0): s = 1.5, L = 32;
 (ii) a different gauge-covariant path ensemble: the two L-shaped paths (x-then-y, y-then-x), averaged.
"""
import sys
import numpy as np
import K4_gauge_paths_oe2_stiffness_2d as K4

def lshape_flow(a, b, L):
    rho = np.zeros((2, L, L))
    sa, sb = (1 if a >= 0 else -1), (1 if b >= 0 else -1)
    for order in (0, 1):
        x, y = 0, 0
        steps = ([(0, sa)] * abs(a) + [(1, sb)] * abs(b)) if order == 0 else ([(1, sb)] * abs(b) + [(0, sa)] * abs(a))
        for mu, sg in steps:
            if mu == 0:
                if sg > 0: rho[0, x % L, y % L] += 0.5
                else: rho[0, (x - 1) % L, y % L] -= 0.5
                x += sg
            else:
                if sg > 0: rho[1, x % L, y % L] += 0.5
                else: rho[1, x % L, (y - 1) % L] -= 0.5
                y += sg
    return rho

which = sys.argv[1]
L = 32
if which == "mu":
    for mu in (0.3, 0.15, 0.075):
        m = K4.Model(L, 15, mu=mu)
        for s in (1.5,):
            o = K4.hessians(m, s, "paths"); c = K4.hessians(m, s, "smooth")
            print(f"mu={mu:5.3f} s={s} paths O(e2) TOTAL H_X1={o['X1'][4]:+.3e} H_X2={o['X2'][4]:+.3e} | smooth H_X1={c['X1'][4]:+.3e} H_X2={c['X2'][4]:+.3e}", flush=True)
else:
    K4.staircase_flow = lshape_flow
    m = K4.Model(L, 15)
    print(f"L-shaped average paths, Ward residual={m.ward:.1e}")
    for s in (1.0, 1.5, 2.0):
        o = K4.hessians(m, s, "paths")
        print(f"s={s} Lshape paths O(e2) TOTAL H_X1={o['X1'][4]:+.3e} H_X2={o['X2'][4]:+.3e}", flush=True)
