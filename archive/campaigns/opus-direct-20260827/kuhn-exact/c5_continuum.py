"""C5 -- controls on the EXACT continuum reference and on the analytic Seeley-DeWitt
coefficients.  Nothing here touches the lattice.
   (a) momentum cutoff convergence  J = 30 vs 45 (= 1.5 J)
   (b) Rcont independent of L (it may depend only on x and n)   -- L = 48 vs 64
   (c) longitudinal traceless polarisations must give b1 = 0 exactly
"""
import math, time
import numpy as np
from kx_base import CH_T206, N_MODE, XS, fmt, fmte, e2_sym, e2_full
from opus_t205 import coeffs
from opus_t206 import cont_heat

n = N_MODE


def rcont(L, ch, J, xs=XS, e2=e2_sym):
    kap2 = (2 * math.pi * n / L) ** 2
    sv = xs / kap2
    V2c, b1, b2 = coeffs(ch, L, n)
    Vol2 = (V2c / L) * L ** 4
    return (4 * np.pi * sv) ** 2 * e2(lambda e: cont_heat(L, ch, e, n, sv, J)) / Vol2


print("=== C5c  Seeley-DeWitt b1, b2 from opus_t205 (Riemann tensor, explicit loops) ===")
CASES = {
    "conformal      diag(+1,+1,+1,+1)": {0: 1, 1: 1, 2: 1, 3: 1},
    "traceless-TT   diag( 0,+1,-1, 0)": {1: 1, 2: -1},
    "longitudinal   diag(+1,-1, 0, 0)": {0: 1, 1: -1},
    "longitudinal   diag(+1, 0, 0,-1)": {0: 1, 3: -1},
}
print(f"  {'channel':34s} {'Vol2/L^4':>12s} {'b1':>14s} {'b2':>14s}")
B = {}
for nm, ch in CASES.items():
    V2c, b1, b2 = coeffs(ch, 64, n)
    B[nm] = (V2c / 64.0, b1, b2)
    print(f"  {nm:34s} {V2c/64.0:12.8f} {b1:14.9f} {b2:14.9f}")
print("  conformal validation: |Vol2/L^4-0.5|=%.2e  |b1-0.25|=%.2e  |b2-0.125|=%.2e"
      % (abs(B["conformal      diag(+1,+1,+1,+1)"][0] - 0.5),
         abs(B["conformal      diag(+1,+1,+1,+1)"][1] - 0.25),
         abs(B["conformal      diag(+1,+1,+1,+1)"][2] - 0.125)))
print("  longitudinal b1 (must be 0): %.3e and %.3e"
      % (B["longitudinal   diag(+1,-1, 0, 0)"][1], B["longitudinal   diag(+1, 0, 0,-1)"][1]))

print("\n=== C5a/b  Rcont: cutoff J=30 vs 45, and L=48 vs L=64 ===")
print("  x                : " + " ".join(f"{q:10.2f}" for q in XS))
for nm, ch in CH_T206.items():
    print(f"  -- {nm}")
    res = {}
    for L in (48, 64):
        for J in (30, 45):
            t0 = time.time()
            res[(L, J)] = rcont(L, ch, J)
            print(f"     L={L} J={J}       : " + " ".join(f"{q:10.6f}" for q in res[(L, J)])
                  + f"   [{time.time()-t0:.0f}s]")
    print("     |J45/J30-1| L=64 : " + fmte(res[(64, 45)] / res[(64, 30)] - 1))
    print("     |J45/J30-1| L=48 : " + fmte(res[(48, 45)] / res[(48, 30)] - 1))
    print("     |L64/L48-1| J=45 : " + fmte(res[(64, 45)] / res[(48, 45)] - 1))
    print("     |L64/L48-1| J=30 : " + fmte(res[(64, 30)] / res[(48, 30)] - 1))
    a = rcont(64, ch, 30, e2=e2_full)
    print("     3pt vs 5pt eps   : " + fmte(res[(64, 30)] / a - 1))
