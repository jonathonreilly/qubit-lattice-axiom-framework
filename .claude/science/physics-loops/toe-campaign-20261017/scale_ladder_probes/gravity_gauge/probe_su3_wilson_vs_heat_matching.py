#!/usr/bin/env python3
"""Probe T1 (native transfer lane): is the SU(3) Wilson one-link (plaquette) character
transfer the native heat-kernel transfer with a renormalised coupling, up to corrections
whose order identifies what is scheme (coupling redefinition) vs non-universal content?
Wilson weight exp((beta/3) Re tr U); coefficients c_lambda = sum_n det[I_{l_j+i-j+n}(beta/3)].
Normalised a_lambda = c_lambda/(d_lambda c_0). Heat kernel: a_lambda = exp(-C2(lambda) tau).
Match tau_eff(beta) on the fundamental; residual r_lambda = log a_lambda + C2 tau_eff.
Also: tau_eff vs naive tau0 = g^2/2 = 3/beta (beta=6/g^2) -> one-loop-like coupling shift."""
import numpy as np
from mpmath import mp, besseli, matrix, det, log
mp.dps = 40
def c(lam, beta, nmax=40):
    x = mp.mpf(beta) / 3
    s = 0
    for n in range(-nmax, nmax + 1):
        M = matrix(3, 3)
        for i in range(3):
            for j in range(3):
                M[i, j] = besseli(lam[j] + i - j + n, x)
        s += det(M)
    return s
reps = {"3 (1,0)": ((1, 0, 0), 3, mp.mpf(4) / 3), "8 (1,1)": ((2, 1, 0), 8, mp.mpf(3)),
        "6 (2,0)": ((2, 0, 0), 6, mp.mpf(10) / 3), "10 (3,0)": ((3, 0, 0), 10, mp.mpf(6)),
        "27 (2,2)": ((4, 2, 0), 27, mp.mpf(8))}
print(f"{'beta':>6} {'tau_eff*beta/3':>15} " + " ".join(f"{'beta^2*r['+k.split()[0]+']':>14}" for k in reps if not k.startswith('3 ')))
rows = []
for beta in [6, 12, 24, 48, 96, 192, 384]:
    c0 = c((0, 0, 0), beta)
    a = {k: c(l, beta) / (d * c0) for k, (l, d, C2) in reps.items()}
    tau = -log(a["3 (1,0)"]) / reps["3 (1,0)"][2]
    res = {k: log(a[k]) + reps[k][2] * tau for k in reps if not k.startswith("3 ")}
    rows.append((beta, tau, res))
    print(f"{beta:6d} {float(tau*beta/3):15.8f} " + " ".join(f"{float(beta**2*v):14.6f}" for v in res.values()))
print("\nInterpretation keys: tau_eff*beta/3 -> 1 means heat-kernel time = g^2/2 at leading order;")
print("its 1/beta deviation is a coupling redefinition (scheme). beta^2*r -> const means the")
print("rep-dependent non-universal (non-Casimir) content starts at O(1/beta^2).")
