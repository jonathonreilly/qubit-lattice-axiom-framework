"""Same split as g3_epsU_mu.py but with the SLAC dispersion w^2 = m^2 + |saw(k)|^2 (the dispersion forced by (E) when the
energy current must equal the sawtooth), sawtooth T2 flow (unitary, measure-preserving, tears at the faces)."""
import numpy as np, time
import g3_epsU_mu as G
t0 = time.time()
G.w_kg = lambda kx, ky, kz, m: np.sqrt(m**2 + G.saw(kx)**2 + G.saw(ky)**2 + G.saw(kz)**2)
for m in [1.0]:
    for L in [11, 15, 19]:
        I0, mu = G.mu_split(L, m, 'T2', 'saw')
        print(f"SLAC m={m} flow saw T2 L={L}: I4_N={I0[0]:.6e} I4_U={I0[1]:.6e} | mu_N={mu[0]:+.4e} mu_U={mu[1]:+.4e} [{time.time()-t0:.0f}s]", flush=True)
