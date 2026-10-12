"""2D control, EXACT variance law (pair-of-chains Volterra equation, see E1p_4_massive2d.py).
(i) relative variance vs m tau at several m*ell (ell = rho^{-1/2});
(ii) asymptotic growth rate gamma of Var(tau)/Kbar_env^2 vs the predicted gamma = m^3 ell^2/4 (ARGUED derivation:
     kernel average J0^2 -> 1/(pi m tau'), int K0 = pi/(2 gamma))."""
import numpy as np
from E1p_4_massive2d import exact_W
print("m*ell  m*tau  m^2*ell*tau  Var/Kbar_env^2   (Kbar_env^2 = (1/4) 2/(pi m tau))")
for ml in [0.05, 0.1, 0.2]:
    taus, S, W, it = exact_W(ml, 1.0, 40.0 / ml, ntau=500, nq=120)
    V = W - S
    for mt in [1, 2, 5, 10, 20, 40]:
        i = np.argmin(np.abs(ml * taus - mt))
        env2 = 0.25 * min(1.0, 2 / (np.pi * ml * taus[i]))
        print(f"{ml:5.2f} {ml*taus[i]:6.1f} {ml*ml*taus[i]:9.4f}   {V[i]/env2:.4e}")
print("\nasymptotic growth: m*ell, fitted gamma (d ln Var/d tau over last third), predicted m^3/4, ratio")
for ml, tmax in [(0.5, 160.0), (0.7, 100.0), (1.0, 60.0), (1.4, 40.0)]:
    taus, S, W, it = exact_W(ml, 1.0, tmax, ntau=900, nq=220)
    V = W - S
    sel = taus > 0.6 * tmax
    # Var = (W - S) oscillates mildly; fit ln(V*tau) linear
    p = np.polyfit(taus[sel], np.log(np.maximum(V[sel], 1e-300) * taus[sel]), 1)
    print(f"{ml:4.1f}  gamma_fit = {p[0]:.5f}   pred m^3/4 = {ml**3/4:.5f}   ratio = {p[0]/(ml**3/4):.3f}   (gamma*tau_max = {p[0]*tmax:.1f}, iters {it})")
