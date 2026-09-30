import numpy as np
from test_C_tails_flux import *
coef = fourier_coeffs(); M = hop_matrices(coef)
def V_tails(kz):
    return polar(build_Q(M, kz))[0]
for nk in (96, 240, 480):
    print("nk =", nk, " winding det V (tails) =", winding(V_tails, nk=nk), flush=True)
# max phase increment per step at nk=480
ks = 2*np.pi*np.arange(481)/480
ang = np.unwrap(np.array([np.angle(np.linalg.slogdet(V_tails(k))[0]) for k in ks[:120]]))
print("max |increment| per step (first 120 steps of 480):", np.abs(np.diff(ang)).max(), " (pi = aliasing threshold)")
