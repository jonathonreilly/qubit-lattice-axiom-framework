"""C3 -- flat-metric controls at EVERY production s.
   (i)  Bloch pipeline  vs  the closed-form Kuhn symbol D(k)=sum 2(1-cos k_mu)   [pipeline]
   (ii) that symbol      vs  the exact torus winding sum                         [physics]
Also: e2_sym (3 eps evaluations, using the verified eps-parity) vs e2_full (5 evaluations).
"""
import math
import numpy as np
from kx_base import (lat_trace, flat_lattice_trace, flat_exact_trace, CH_P, N_MODE,
                     XS, fmte, fmt, e2_sym, e2_full)

n = N_MODE
print("=== C3a  flat Kuhn heat trace: Bloch pipeline vs closed-form symbol vs winding sum ===")
for L in (32, 48, 64, 96):
    kap2 = (2 * math.pi * n / L) ** 2
    sv = XS / kap2
    print(f"\n  -- L={L}  kappa^2={kap2:.6f}")
    print("     x                    : " + " ".join(f"{q:10.2f}" for q in XS))
    print("     s                    : " + " ".join(f"{q:10.3f}" for q in sv))
    wind = flat_exact_trace(L, sv)
    for imp in (True, False):
        bl, _ = lat_trace(L, CH_P["CONFORMAL"], 0.0, n, sv, imp)
        sym = flat_lattice_trace(L, sv, improve=imp)
        tag = "IMPR " if imp else "plain"
        print(f"     {tag} Bloch/symbol -1 : " + fmte(bl / sym - 1))
        print(f"     {tag} symbol/winding-1: " + fmte(sym / wind - 1))
        print(f"     {tag} Tr               : " + " ".join(f"{q:10.4f}" for q in bl))

print("\n=== C3b  eps^2 extraction: 3-point (parity) vs 5-point, L=32 and L=48 ===")
for L in (32, 48):
    kap2 = (2 * math.pi * n / L) ** 2
    sv = XS / kap2
    for name, P in CH_P.items():
        for imp in (True, False):
            f = lambda e: lat_trace(L, P, e, n, sv, imp)[0]
            a = e2_sym(f)
            b = e2_full(f)
            print(f"  L={L} {name:13s} {'IMPR ' if imp else 'plain'} K2 rel diff : "
                  + fmte(a / b - 1))
