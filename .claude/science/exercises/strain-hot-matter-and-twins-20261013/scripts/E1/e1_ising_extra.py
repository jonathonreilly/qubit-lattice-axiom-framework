#!/usr/bin/env python3
"""E1 (D2) and (a4), 2D Ising, exact.
(D2) Symmetric stretch with an O(t^2) isotropic part: Kx = Kc(1 + t + k t^2), Ky = Kc(1 - t + k t^2).
  Gap condition at O(t^2): Ky* - Kx = 0 at O(t^2)  -> k_gap = sqrt2 Kc / 2 (analytic).
  Stiffness: d2 lnZ/dt2 = [linear-param value] + 2 * (2 Kc k) * dlnZ/dK_j   (dlnZ/dK_j = <s s>_j per site).
  Is there one k that keeps the gap AND makes the stretch free (d2 lnZ/dt2 = 0)?
(a4) Mass-shell decay rate along the diagonal vs -ln(sinh2Kx sinh2Ky) (comparator: diagonal correlations
  depend only on the product, RECALLED).
"""
import numpy as np
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from e1_ising_stretch import lnZ, dual, Kc

if __name__ == "__main__":
    h = 1e-4
    dK = (lnZ(Kc + h, Kc) - lnZ(Kc - h, Kc)) / (2 * h)
    print(f"(D2) dlnZ/dKx at Kc (per site) = {dK:.8f}   (<s s>_nn at Tc = 1/sqrt2 = {1/np.sqrt(2):.8f}, RECALLED)")
    k_gap = np.sqrt(2) * Kc / 2
    for k in (0.0, k_gap):
        out = []
        for hh in (0.02, 0.01):
            fx = lambda t: Kc * (1 + t + k * t * t); fy = lambda t: Kc * (1 - t + k * t * t)
            out.append((lnZ(fx(hh), fy(hh)) + lnZ(fx(-hh), fy(-hh)) - 2 * lnZ(Kc, Kc)) / hh**2)
        # gap check at small t
        t = 1e-3
        gap_o2 = (dual(Kc * (1 - t + k * t * t)) - Kc * (1 + t + k * t * t)) / t**2
        print(f"  k={k:.6f}: d2lnZ/dt2 = {out[0]:+.6f} (h=.02) {out[1]:+.6f} (h=.01);  (Ky*-Kx)/t^2 at t=1e-3 = {gap_o2:+.6f}")
    base = 0.10618
    k_stiff = -base / (4 * Kc * dK)
    print(f"  predicted from linear value: d2lnZ/dt2(k) = {base} + 4 Kc k <ss> ; k_stiff (zero stiffness) = {k_stiff:+.6f}; k_gap = {k_gap:+.6f}")
    print("  -> with nearest-neighbour couplings only, keeping the gap and freeing the stretch need different k: two conditions per order")
    print("\n(a4) diagonal decay rate of the D-propagator (support function along (1,1), per diagonal step) vs -ln(sinh2Kx sinh2Ky)")
    for (Kx, Ky) in ((0.40, 0.30), (0.42, 0.40), (0.55, 0.30), (0.30, 0.30)):
        sx, sy, C = np.sinh(2 * Kx), np.sinh(2 * Ky), np.cosh(2 * Kx) * np.cosh(2 * Ky)
        kxm = np.arccosh((C - sy) / sx)
        kx = np.linspace(-kxm, kxm, 2000001)
        ky = np.arccosh(np.maximum((C - sx * np.cosh(kx)) / sy, 1.0))
        hdiag = np.max(kx + ky)
        print(f"  Kx={Kx} Ky={Ky}: support (1,1) = {hdiag:.10f}   -ln(sx*sy) = {-np.log(sx*sy):.10f}")
