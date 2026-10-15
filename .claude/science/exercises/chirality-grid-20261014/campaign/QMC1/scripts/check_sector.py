"""det = |det_sector|^2 check (task item 1: "exploit det = |det_sector|^2 where the theory allows it").

Claim (2+1D, walker sigma_x sin px + sigma_y sin py, filter f2 or f == 1, SINGLET-ONLY Fierz vertex
kappa = (sing8v 1.25, sing56v 0.25), which is sign-correct, x2model / fierz_points.py):
  J_d = (-1)^{x+y} sigma_z x diag(1_s, -1_c)   (d-frame one-body operator)
commutes with every slice B_l, and T2 J_d T2^-1 = -J_d. Hence the J_d = +1 and -1 sectors are exchanged by T2 and
det(1 + M) = |det(1 + M_+)|^2.  The production vertex (sing8v 1.5, trip8v -0.5) contains triplet x, y channels that
do not commute with J_d, so there the factorisation is NOT available (checked below too).
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice, AFQMC

fm = FlavourModel("spin10")
for filt in ("f2", "one"):
    lat = Lattice((4, 4), filt)
    eps = np.array([(-1.0) ** (c[0] + c[1]) for c in lat.coords])
    Jsite = np.kron(np.diag([1.0, -1.0]), np.diag(np.where(fm.Smask[:fm.nfl], 1.0, -1.0)))   # sigma_z x diag(1,-1)
    J = np.kron(np.diag(eps), Jsite)
    Th = np.kron(np.eye(lat.N), fm.T2())
    print(f"[{filt}] T2 J T2^-1 = -J: {np.allclose(Th @ J.conj() @ np.linalg.inv(Th), -J)}")
    for name, kap in (("singlet-only", {"sing:8v": 1.25, "trip:8v": 0.0, "sing:56v": 0.25, "trip:56v": 0.0}),
                      ("production", {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0})):
        sim = AFQMC(fm, kap, lat, W=2.0, beta=0.4, dtau=0.1, n_s=4, seed=7)
        comm, ratio = 0.0, []
        M = np.eye(sim.Nd, dtype=complex)
        for l in range(sim.Lt):
            B = sim.apply_B(l, np.eye(sim.Nd, dtype=complex))
            comm = max(comm, np.abs(J @ B - B @ J).max() / np.abs(B).max())
            M = B @ M
        if comm < 1e-10:
            w, V = np.linalg.eigh(J)
            Vp = V[:, w > 0]
            Mp = Vp.conj().T @ M @ Vp
            full = np.linalg.slogdet(np.eye(sim.Nd) + M)
            half = np.linalg.slogdet(np.eye(Mp.shape[0]) + Mp)
            msg = (f"log det(1+M) = {full[1]:.10f} (phase {np.angle(full[0]):.1e}); 2 log|det(1+M_+)| = {2 * half[1]:.10f}; "
                   f"sector dim {Mp.shape[0]} of {sim.Nd}")
        else:
            msg = "J does not commute: no factorisation"
        print(f"[{filt}] {name}: nch {sim.nch}; max ||[J, B_l]||/||B_l|| = {comm:.1e}; {msg}")
