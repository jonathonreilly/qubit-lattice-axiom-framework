"""R3-3 (b2): curvature carried by dislocations of an L7 crystal (teleparallel / Kroner-Katanaev-Volovich reading). SUGGESTED model.
Minimal torsion over a region of size L with curvature R ~ Phi/L^2:  |T| ~ R L ~ Phi/L  (loop holonomy R L^2 spread over perimeter L).
Dislocation worldsheet area density n_d = |T|/b, Burgers vector b ~ a (shortest L7 vector, |x|_E >= 1 lattice unit).
(N1) core-disorder fraction of events f = n_d a^2 ~ |T| a; RZ ladder rate ~ sqrt(rung) and rung ~ f (RL2: z ~ sqrt(eps)), so
     variance e-folds n ~ sqrt(f) * n_RZ, n_RZ = 45,258 proved rate e-folds at 1 s / 1 Gpc (RZ_referee.md:16); in-band penalty 122 e-folds.
(N2) granularity of Poisson-placed dislocations = classical random metric: Var(dphi) ~ omega^2 D n_d b^2 delta (two rays delta apart).
(N3) smooth strain eps: |S G|_E >= (1-|eps|)|G|_E >= (1-|eps|) 2 pi/(sqrt7 a) in the observer frame -> no in-band Bragg vector (proved, trivial).
Disclinations: Gamma_L holonomies are >= 90 deg rotations or cosh(eta) >= 8 boosts -> O(1) conical defects; not usable for weak curvature.
"""
import numpy as np
c = 2.998e8; G = 6.674e-11; lP = 1.616e-35
nRZ = 45258.0; pen = 122.0
lenses = [  # name, Phi, L [m], path D [m]
    ("Earth lab (atom interf.)", 7e-10, 6.4e6, 6.4e6),
    ("Sun (Cassini/deflection)", 2.1e-6, 7.0e8, 1.5e11),
    ("galaxy strong lens", 7e-7, 3e20, 3e20),
    ("cluster lens", 1.1e-5, 3e22, 3e22),
    ("M87* photon ring", 0.5, 1.9e13, 1.9e13),
    ("neutron star surface", 0.2, 1.2e4, 1.2e4),
]
H0 = 2.27e-18/c   # m^-1
print("a = l_P = %.3e m; also a = 1e-19 m column for the f-scaling" % lP)
print(f"{'object':28s} {'|T| [1/m]':>10s} {'n_d [1/m^2]':>12s} {'f=|T|a':>10s} {'(a/Lcurv)^2':>12s} {'e-folds sqrt(f)nRZ':>18s} {'f (a=1e-19)':>12s}")
rows = []
for name, Phi, L, D in lenses + [("cosmology (T~H0/c)", None, None, 3.086e25)]:
    if Phi is None:
        T = H0; Lc2 = 1/H0**2
    else:
        T = Phi/L; Lc2 = L**2/Phi
    nd = T/lP; f = T*lP; ac2 = lP**2/Lc2
    ne = np.sqrt(f)*nRZ
    rows.append((name, T, nd, f, D))
    print(f"{name:28s} {T:10.2e} {nd:12.2e} {f:10.2e} {ac2:12.2e} {ne:18.2e} {T*1e-19:12.2e}")
fstar1 = (1/nRZ)**2; fstar2 = (pen/nRZ)**2
print(f"thresholds: <=1 variance e-fold needs f < {fstar1:.1e};  N_B/S < 1 (with the 122 e-fold in-band penalty) needs f < {fstar2:.1e}")
print("\n(N2) classical granularity phase noise Var(dphi) = omega^2 D n_d b^2 delta, b = l_P, Poisson-placed dislocations:")
bands = [("optical 600 nm", 2*np.pi/6e-7, 1e1), ("VLBI 1.3 mm (EHT)", 2*np.pi/1.3e-3, 1e7), ("radio 21 cm", 2*np.pi/0.21, 1e7)]
for name, T, nd, f, D in rows:
    s = "  ".join(f"{bn}: {(om**2*D*nd*lP**2*dl):.1e}" for bn, om, dl in bands)
    print(f"  {name:28s} D={D:.1e} m  {s}  rad^2")
print("  (delta = 10 m aperture for optical, 1e7 m Earth baseline for VLBI/radio; D = path length through the curved region)")
# (N3) strain bound
for eps in (1e-6, 1e-5, 0.5):
    print(f"(N3) strain {eps:g}: min |G|_E >= {(1-eps)*2*np.pi/np.sqrt(7):.4f}/a vs in-band |q| <= 2 omega_max (omega_max a ~ 1e-28 optical)")
