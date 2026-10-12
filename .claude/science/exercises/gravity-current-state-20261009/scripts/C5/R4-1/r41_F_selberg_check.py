"""R4-1 (F): check of the small-beta asymptotics of the Selberg/Harish-Chandra transform used in Sec 4:
h(r, beta) = (4 pi / r) int_0^inf exp(-beta cosh 2d) sinh d sin(r d) dd   (tempered r > 0)
predicted:  (pi / r) Im[ Gamma(1/2 + i r/2) (2/beta)^(1/2 + i r/2) ]  * (1 + O(beta))
and the constant mode  h0(beta) = 4 pi int exp(-beta cosh 2d) sinh^2 d dd  ~  pi/beta  (mean term)."""
import numpy as np
from mpmath import mp, quad, gamma, exp, cosh, sinh, sin, im, mpf, inf, besselk
mp.dps = 30
for r in (1.0, 3.0, 6.0):
    for beta in (1e-2, 1e-3, 1e-4):
        f = lambda d: exp(-beta*cosh(2*d))*sinh(d)*sin(r*d)
        dmax = 0.5*mp.acosh(60/beta)
        val = 4*mp.pi/r*quad(f, mp.linspace(0, dmax, 200))
        pred = mp.pi/r*im(gamma(mpf(1)/2 + 1j*r/2)*(2/mpf(beta))**(mpf(1)/2 + 1j*r/2))
        print(f"r={r:4.1f} beta={beta:.0e}  h = {float(val):+.6e}   leading = {float(pred):+.6e}   diff/sqrt(1/beta) = {float((val-pred)*mp.sqrt(beta)):+.2e}")
for beta in (1e-2, 1e-3):
    h0 = 4*mp.pi*quad(lambda d: exp(-beta*cosh(2*d))*sinh(d)**2, [0, 0.5*mp.acosh(60/beta)])
    # exact: 4pi int e^{-b cosh2d} (cosh2d-1)/2 dd = pi (K1(b) - K0(b))
    print(f"constant mode beta={beta:.0e}: h0 = {float(h0):.6e}, exact pi(K1-K0) = {float(mp.pi*(besselk(1,beta)-besselk(0,beta))):.6e}, pi/beta = {float(mp.pi/beta):.6e}")
