"""Interval certificate: Var_par(kappa) = R'(kappa) = 1 - R^2 - 3R/kappa <= 1/4 on (0, K], R = I2/I1.
Small kappa (<= k0): Taylor, Var even analytic, Var(0)=1/4, Var''(0)=kappa_4(0)=E t^4-3(E t^2)^2 = 1/8-3/16 = -1/16,
 |Var''''| = |kappa_6| <= 1082 (sum of |moment-cumulant coefficients| for n=6, all |moments|<=1)
 => Var <= 1/4 - k^2/32 + 1082 k^4/24 <= 1/4 for k <= sqrt(24/(32*1082)).
Large kappa cells [lo,hi]: R increasing (R'=Var>0) => Var <= 1 - R(lo)^2 - 3 R(lo)/hi, evaluated in arb.
"""
import json, math
from flint import arb, ctx
ctx.prec = 200
K = 1.2
k0 = math.sqrt(24/(32*1082)) * 0.999
R = lambda k: arb(k).bessel_i(2)/arb(k).bessel_i(1)
lo = k0; cells = 0; worst = -1.0; Rlo = R(lo)
while lo < K:
    h = min(1e-3, lo**3/40)
    while True:
        hi = min(lo + h, K)
        v = 1 - Rlo*Rlo - 3*Rlo/arb(hi)
        if v < arb(0.25): break
        h /= 2
        assert h > 1e-14, ("fail", lo)
    worst = max(worst, float(v.upper())); cells += 1
    lo = hi; Rlo = R(lo)
res = {"small_kappa_cutoff": k0, "K": K, "cells": cells, "certified": True, "max_cell_upper": worst}
print(res)
json.dump(res, open("data/var_certificate.json", "w"), indent=1)
