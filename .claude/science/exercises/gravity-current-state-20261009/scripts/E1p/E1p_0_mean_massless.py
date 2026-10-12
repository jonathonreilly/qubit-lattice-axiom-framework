"""E1' (a): mean massless link kernel, rho = 1:  E[a L(x,y)] = a exp(-pi tau^4/24) theta(y < x),  a = 1/(2 pi sqrt6).
(1) static potential  G_st(r) = int dt a e^{-rho V}  vs 1/(4 pi r): no Yukawa factor (massless in mean).
(2) weight on the cone: int over a spatial slice at distance r of the kernel vs delta(tau^2)/(2 pi) normalisation.
(3) width around the cone: sigma = tau^2 of the kernel ~ e^{-pi sigma^2/24}: <sigma> = 12/(pi sqrt6); time offset sigma/(2r)."""
import numpy as np
from scipy import integrate
a = 1 / (2 * np.pi * np.sqrt(6))
print("   r      G_st(r)*4 pi r     1 - <sigma>/(2 r^2) (leading correction)")
for r in [0.5, 1, 2, 5, 10, 100, 1e4]:
    f = lambda s: a * np.exp(-np.pi * s * s / 24) / (2 * np.sqrt(s + r * r))   # dt = ds/(2 sqrt(r^2+s))
    val, _ = integrate.quad(f, 0, 60, limit=200)
    print(f"{r:8g}   {val*4*np.pi*r:.8f}      {1 - (12/(np.pi*np.sqrt(6)))/(2*r*r):.8f}")
