"""C2: Kitaev Majorana Drude ratio vs L at fixed dilute flux density (proxy for any T>0: rho ~ exp(-Delta_flux/T)).
Flux pairs are created by flipping z-bond gauge signs with probability q (rho ~ 2q). Same definitions as c2_kitaev_majorana.py."""
import numpy as np
from c2_kitaev_majorana import build, drude_ratio, fluxes
rng = np.random.default_rng(777)
betas = (0.0, 1.0, 3.0)
print("Kitaev isotropic; z-bond flips with prob q; r = Drude ratio (ensemble sums) at Majorana beta = 0, 1, 3; mean +- sem")
for q in [0.5, 0.02, 0.005]:
    for L in [8, 12, 16, 24, 32, 40]:
        if q == 0.5 and L > 24: continue
        A0, B0, bonds = build(L)
        nb = len(bonds)
        zb = np.array([t == 2 for (_, _, t, _) in bonds])
        nsamp = {8: 16, 12: 12, 16: 8, 24: 5, 32: 3, 40: 2}[L]
        R = []; RH = []
        for s in range(nsamp):
            if q == 0.5:
                u = np.where(rng.random(nb) < 0.5, -1.0, 1.0)
            else:
                u = np.where((rng.random(nb) < q) & zb, -1.0, 1.0)
            A, B, _ = build(L, u=u)
            rs, c = drude_ratio(A, B, betas)
            R.append(rs); RH.append(np.mean(fluxes(L, bonds, u) < 0))
        R = np.array(R); m = R.mean(0); e = R.std(0)/np.sqrt(len(R))
        print(f"q={q:5.3f} L={L:3d} N_maj={2*L*L:5d} flux_density={np.mean(RH):.4f}  r=" +
              "  ".join(f"{mm:.3e}+-{ee:.1e}" for mm, ee in zip(m, e)), flush=True)
