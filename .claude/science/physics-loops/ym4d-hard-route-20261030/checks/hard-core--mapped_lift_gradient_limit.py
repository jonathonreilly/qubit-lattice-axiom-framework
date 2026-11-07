#!/usr/bin/env python3
"""Follow-up to `hard-core--mapped_lift_gradient.py`, which FAILED its criterion L2 (C(4, 11, 1) = 43.93, against a cap of 30 that I had guessed, and C(4, 11, 1)/C(4, 7, 1) = 1.17 against 1.15). Consumer: (LIFT-I) in `library/sector-values.md`, which needs C_0 L^-2 <= 1/2 with C_0 free of L.

Written before running. Does C(4, L, 1) stay bounded as L grows, or does it grow? The values 16.96, 30.28, 37.56, 41.57, 43.93 at L = 3, 5, 7, 9, 11 fit C_inf - A/L^2 with C_inf about 48.7, from L = 9, 11. The ratio has a limit as L -> infinity if the alias sums converge, which they should, as q(k) decays. Also reported: g(P) := L^4/(|P-hat|^2 G_perp(P)), the extreme eigenvalues over the grid, the symbol of the effective action on 2-forms that Step 3 of (LIFT-I) reads, and it must be bounded above and below.

PRE-STATED criteria.
 M1. C(4, L, 1) is increasing with falling increments at L = 13, 17, 21, 31, and C(4, 31, 1) <= 52.
 M2. The prediction C_inf - A/L^2, with C_inf, A fitted at L = 9, 11 only, is within 3 percent at L = 31.
 M3. g_max(L) and 1/g_min(L) at most 10 for each L.
FAIL if any fails. A failure of M1 means the constant grows with L and the geometric sum in Theorem VAL would have to be redone with its true power.

Limits. Abelian, grid of momenta as in the first script. RSS guard 2 GB.
"""
import importlib.util
import os
import sys

import numpy as np

spec = importlib.util.spec_from_file_location("lg", os.path.join(os.path.dirname(os.path.abspath(__file__)), "hard-core--mapped_lift_gradient.py"))
lg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lg)


def symbol_range(L, d=4):
    gmin, gmax = np.inf, 0.0
    for P in lg.grid(d):
        Pv = np.asarray(P, float)
        Phat = 2 * np.sin(Pv / 2)
        P2 = float(np.sum(Phat**2))
        k, q = lg.qvec(Pv, L, d)
        khat = 2 * np.sin(k / 2)
        k2 = np.sum(khat**2, axis=1)
        G = np.diag(np.sum(q * q / k2[:, None], axis=0))
        u = Phat / P2**0.5
        Perp = np.linalg.svd(np.eye(d) - np.outer(u, u))[0][:, : d - 1]
        ev = np.linalg.eigvalsh(Perp.T @ G @ Perp)
        vals = L**4 / (P2 * ev)
        gmin, gmax = min(gmin, float(vals.min())), max(gmax, float(vals.max()))
    return gmin, gmax


def main():
    C = {}
    ok = True
    for L in (9, 11, 13, 17, 21, 31):
        C[L] = lg.scan(4, L, 1)[0]
        gmin, gmax = symbol_range(L)
        good = gmax <= 10 and 1 / gmin <= 10
        ok = ok and good
        print(f"  L={L}: g in [{gmin:.4f}, {gmax:.4f}]: {good}", flush=True)
        lg.guard()
    Ls = (9, 11, 13, 17, 21, 31)
    inc = [(C[b] - C[a]) / (b - a) for a, b in zip(Ls, Ls[1:])]
    m1 = all(x > 0 for x in inc) and all(y < x for x, y in zip(inc, inc[1:])) and C[31] <= 52
    A = (C[11] - C[9]) / (1 / 81 - 1 / 121)
    Cinf = C[9] + A / 81
    pred = Cinf - A / 31**2
    m2 = abs(C[31] / pred - 1) <= 0.03
    ok = ok and m1 and m2
    print(f" M1 increments per unit of L {[round(x, 4) for x in inc]}, C(31)={C[31]:.3f}: {m1}", flush=True)
    print(f" M2 fit at L = 9, 11: C_inf={Cinf:.3f}, A={A:.1f}, predicted C(31)={pred:.3f}: {m2}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
