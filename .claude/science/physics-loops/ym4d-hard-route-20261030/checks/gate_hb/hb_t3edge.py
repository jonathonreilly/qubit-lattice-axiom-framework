#!/usr/bin/env python3
"""T3'' of REGISTRATION.md: the edge of the geometric series in (SUM)."""
import importlib.util
import json
import math
import os
import sys
from itertools import product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("hb_checks", os.path.join(HERE, "hb_checks.py"))
hb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hb)


def ratio_cg(X, N, B, bp, cG):
    Y = X / 2
    return math.log(N) + B / (2 * Y) - 3 * cG * bp * math.sqrt(Y) / 16


def solve_x(target, N, B, bp, cG):
    lo, hi = 1.0, 1e40
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if ratio_cg(mid, N, B, bp, cG) > math.log(target):
            lo = mid
        else:
            hi = mid
    return hi


def main():
    a = np.arange(1, 20001)
    worst, solved = 0.0, 0
    for N, B, bp, cG, l1, target, mode, SoN, Aval in product(
            (1e2, 1e4, 1e8), (1.0, 5.0), (0.2, 1.0), (1e-5, 1e-2), (1e-3, 0.1),
            (0.6, 0.8, 0.95), ("cg", "l0"), (1.0, 3.0), (20.0,)):
        if mode == "cg":
            X = solve_x(target, N, B, bp, cG)
            Y = X / 2
            D = N * math.exp(B / (2 * Y))
            l0 = 16 * (math.log(D) + 5)
        else:
            X = max(1e6, solve_x(0.01, N, B, bp, cG) * 2)
            Y = X / 2
            D = N * math.exp(B / (2 * Y))
            l0 = 8 * (math.log(D) - math.log(target))
        es = hb.e_star(X, N, B, bp, cG, l0)
        if es is None or es == 0:
            continue
        solved += 1
        for xJ, K_J in ((Y, 0), (2 * X, 0)):
            y = Y + bp * K_J
            lpsi = hb.log_psi(a, l0, y, bp, cG, l1)
            lw = a * math.log(N) + 0.5 * np.log1p(B * a / xJ)
            direct = hb.log_sum(lw + lpsi / 4)
            good = lw + lpsi / 4 + math.log(1 / 8)
            src = ((a - 1) * math.log(N) + 0.5 * np.log1p(B * (a - 1) / xJ)
                   + lpsi / 4 + math.log(SoN * N))
            bottom = a * math.log(N) + math.log(12 / (Aval * math.sqrt(xJ))) + lpsi / 4
            full = float(np.logaddexp(np.logaddexp(hb.log_sum(good), hb.log_sum(src)), bottom.max()))
            bound = (1 / 8 + SoN + 12 / (Aval * math.sqrt(Y))) * es
            worst = max(worst, math.exp(direct - math.log(es)) - 1,
                        math.exp(full - math.log(bound)) - 1)
    res = {"solved": solved, "max_excess": worst, "pass": bool(worst <= 1e-9 and solved >= 200)}
    print("T3pp", json.dumps(res), flush=True)
    with open(os.path.join(HERE, "results_t3edge.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    return 0 if res["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
