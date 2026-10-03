#!/usr/bin/env python3
"""A24 S7: injected energy vs registration resolution for a DIRECT Gaussian (unsharp, site-diagonal) Lueders cut on the
ticked toy (A19 core, energy E = W(K) on both branches).  The outcome-averaged cut multiplies the site density matrix by
C(d) = exp(-d^2/(8 sigma_s^2)); on cell-diagonal blocks this is a Gaussian kick of the cell momentum with variance
1/sigma_s^2, so (EXACT)  dE(sigma) = E_delta[W(K + delta)] - W(K),  delta ~ N(0, 1/sigma_s^2) wrapped.
Regimes: sigma >> 1/m: (1/2) cot m / sigma_s^2 (= hbar^2/(8 m sigma^2), sigma in cells);  1 << sigma << 1/m: ~ sqrt(2/pi) cos m
/ sigma_s (= O(hbar c / sigma));  sigma -> 0: pi/2 - W(K) (band centre)."""
import numpy as np
x, wq = np.polynomial.hermite_e.hermegauss(200)      # Gauss-Hermite for N(0,1)
wq = wq / wq.sum()
for m in (0.01, 0.1):
    print(f"m = {m} (Compton length 1/m = {1/m:.0f} cells), mover at K = 0 (W = m):")
    for sig in (0.25, 0.5, 1, 2, 4, 10, 30, 100, 300, 1000, 3000, 1e4):
        if sig < 1.0:
            K = np.linspace(-np.pi, np.pi, 200001)          # wide kicks: integrate the wrapped Gaussian directly
            dens = sum(np.exp(-(K + 2 * np.pi * n) ** 2 * sig ** 2 / 2) for n in range(-20, 21))
            dens /= np.trapezoid(dens, K)
            EW = np.trapezoid(dens * np.arccos(np.cos(m) * np.cos(K)), K)
        else:
            EW = np.dot(wq, np.arccos(np.cos(m) * np.cos(x / sig)))
        dE = EW - m
        nr = 0.5 / np.tan(m) / sig ** 2
        rel = np.sqrt(2 / np.pi) * np.cos(m) / sig
        print(f"   sigma_s={sig:8.2f} sites: dE={dE:.4e}   nonrel (1/2)cot m/sigma^2={nr:.4e}   rel sqrt(2/pi)cos m/sigma={rel:.4e}"
              f"   band-centre limit pi/2-m={np.pi/2-m:.4f}")
