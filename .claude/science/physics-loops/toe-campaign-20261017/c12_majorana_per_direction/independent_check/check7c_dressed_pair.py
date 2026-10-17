"""Diagnostic for (7): a pair creator that also leaves plaquette (flux) violations
next to the endpoints can give the opposite lambda.  Example: S = gamma_{x,d} gamma_{Rx,Rd}
(two bare Majoranas: B-violations at x, Rx PLUS violated plaquettes around them)."""
import sys
sys.argv = [sys.argv[0], "10"]
from mpd_core import *
import check7_fractionalization as c7
lat = c7.lat
for cls, Ms in [("axis", c7.axisC2), ("edge", c7.edgeC2)]:
    for M in Ms[:2]:
        G = c7.good[0]
        eps = next(g[1] for g in G if g[0] == dir_perm(M))
        x = (1, 0, 0) if cls == "axis" else (2, 0, 1)
        y = apply(M, x)
        dp = dir_perm(M)
        for d in range(6):
            Smono = (0, [(x, d), (y, dp[d])])
            S = lat.to_pauli(Smono); SR = lat.to_pauli(act_mono(lat, M, eps, Smono))
            nflux = sum(anticommute(S, s) for s in c7.Sp)
            lam = c7.tabs[(1, 1, 1)].sign_of(mul(dag(S), SR))
            print(cls, M, "S=gamma_{x,%d}gamma_{Rx,%d}" % (d, dp[d]), "violated plaquettes:", nflux, "lambda:", lam)
