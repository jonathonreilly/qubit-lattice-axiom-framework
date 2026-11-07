#!/usr/bin/env python3
"""D3 check: normalized energy-kurtosis excess of a local one-link cubic map after the block B-1.

With X Feynman of covariance G per colour, Phi = sum_b w_b X_b (1 + kappa |X_b|^2), the slope at kappa = 0 of
E|Phi|^4 - (5/3)(E|Phi|^2)^2 is 120 sum_b w_b r_b^3, r_b = (G w)(b) (exact, C3c of nt2_algebra.py).
Reported: 120 sum w r^3 / u^2, u = <w, G w>, for the blocked plaquette Gamma_12.
"""
import json
import sys

import numpy as np

from nt2_blocked import corner, fine_current, inv_laplace, check_rss

out = []
for n, S in [(1, 16), (3, 8), (5, 8), (7, 8)]:
    N = n * S
    J = fine_current(N, n, corner(0, 1))
    E = inv_laplace(J, N)
    u = float(np.vdot(J, E))
    s = float(np.sum(J * E**3))
    r = {"n": n, "S": S, "u": u, "sum_w_r3": s, "normalized_excess_slope": 120 * s / u**2}
    print(r, flush=True)
    out.append(r)
    del J, E
    check_rss()
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1)
