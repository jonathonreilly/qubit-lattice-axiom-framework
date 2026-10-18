import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import chk
lat = chk.Lat((2, 2, 2))
s0 = chk.simple_ice(lat)
S, nf, mv = chk.component(lat, s0)
print("component size", len(S), "W", lat.winding(s0))
c = lat.harm(0)
for V in (1.0, 0.0, -0.5):
    E = lambda b, imag: (np.linalg.eigvals(chk.H_twist(len(S), nf, mv, V, b, c, imag=True)).real.min() if imag
                         else np.linalg.eigvalsh(chk.H_twist(len(S), nf, mv, V, b, c, imag=False))[0])
    E0 = E(0.0, False); h = 1e-3
    chi = (E(h, False) + E(-h, False) - 2 * E0) / h ** 2
    print(f"V={V}: E0={E0:.6f} chi(real b FD)={chi:.6f}", " E(i eta): ", [(eta, round(E(eta, True), 6), round(-2 * (E(eta, True) - E0) / eta ** 2, 5)) for eta in (0.5, 1.0, 2.0)])
