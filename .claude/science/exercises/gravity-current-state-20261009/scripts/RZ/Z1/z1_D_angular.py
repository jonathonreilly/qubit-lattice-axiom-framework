"""Z1 (D): angular distribution of the in-band node-level noise in the observer frame.
Per unit solid angle the low-frequency PSD is proportional to 1/D(theta), D = cosh(eta_b) - cos(theta) sinh(eta_b),
theta measured from the source direction (the growth direction N points from the source's past edge to the observer).
Fraction within theta of the source direction: F = ln[(cosh e - cos t sinh e) e^e]/(2e), stable form 1 + 2 sin^2(t/2) sinh(e) e^e.
"""
import numpy as np
for gb, lab in [(2.27e8, '1 Gpc, 1 s'), (1.34e6, '1 Gpc, 8 h'), (4.04e4, '1 Gpc, 1 yr'), (12.8, 'quasar 1e7 yr')]:
    e = np.arccosh(gb)
    for th, tl in [(4.85e-9, '1 mas'), (2.42e-7, '0.05 arcsec'), (4.85e-6, '1 arcsec'), (1.0, '1 rad')]:
        fr = np.log1p(2*np.sin(th/2)**2*np.sinh(e)*np.exp(e))/(2*e)
        print('%-14s gamma_b=%.2e (1/gamma_b = %.2g arcsec) within %-11s : fraction %.3g  (-ln = %.1f)' % (lab, gb, 206265/gb, tl, fr, -np.log(fr)))
