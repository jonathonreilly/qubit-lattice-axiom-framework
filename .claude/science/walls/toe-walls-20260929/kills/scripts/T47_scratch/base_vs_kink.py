"""T47 A3: size of the base trace-free Einstein entry vs the finite-difference step, and extrapolation of the ladder."""
import sys
sys.dont_write_bytecode=True
import numpy as np
import ladder_infvol as L
rh=L.rh
print("N, base xx(E0), base xx(S), EPS*|dxx/dq_TX| (E0), max-abs entry of TF at probe0 (E0)")
for N in (15,21,41,61,101):
    rh.ETA_CACHE.clear(); rh.ANCHOR_CACHE.clear()
    sysm = rh.build_size_system(N)
    def xx(q, radius=4.25):
        phi = rh.phi_from_q(sysm, q)
        pt = rh.probe_points(radius)[0]
        _, ein = rh.tcomp.ricci_and_einstein(lambda p: rh.tcomp.adm_metric(phi, p, 0.0,0.0,0.0), pt, h=rh.RICCI_H)
        return L.tf_spatial(ein)
    tE = xx(rh.E0); tS = xx(rh.S_UNIT)
    tEp = xx(rh.E0 + rh.EPS*rh.TX); tEm = xx(rh.E0 - rh.EPS*rh.TX)
    d = (tEp[0,0]-tEm[0,0])/2.0    # = EPS * dxx/dq
    print(f"{N:4d}  {tE[0,0]:+.3e}  {tS[0,0]:+.3e}   {abs(d):.3e}   {np.max(np.abs(tE)):.3e}   ratio |base|/|EPS*deriv| = {abs(tE[0,0])/abs(d):.2f}")
