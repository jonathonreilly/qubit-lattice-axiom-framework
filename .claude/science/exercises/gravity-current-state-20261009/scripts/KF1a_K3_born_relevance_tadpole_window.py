"""K3 (kill agent, F1a): arithmetic of what a white random TT stiffness and a white random TT stress do.

Conventions (stated, so the factor 2 vs R3 c6 is visible):
  graviton TT action  S = (M^2/8) int (hdot_ij^2 - (grad h_ij)^2),  M = reduced Planck mass;
  medium (per configuration)  -int [tau_ij(x) h_ij + 1/2 mu(x) h_ij h_ij].
  With g = exp(t hhat), tr hhat^2 = 1, h_ij h_ij = t^2, so mu = E''/site and tau.hhat = E'/site
  (lattice units, density 1).  EOM: omega^2 = q^2 + V(x),  V = 4 mu / M^2   (R3 c6 used 8 mu / M^2).
White noise:  <dmu(x) dmu(y)> = sigma^2 delta(x-y)  (sigma = sd*sqrt(N) per site, K1 / R3 c2b).
 (i)  Born, scalar Helmholtz, white V:  1/l = W/(4 pi),  W = 16 sigma^2 / M^4 (per unit volume).
 (ii) Relevance (Harris power counting): coarse-grained random mass^2 over a box of side lam vs q^2 = (2pi/lam)^2:
      ratio(lam) = 4 sigma lam^{-3/2} / M^2 / (2 pi / lam)^2 = (sigma / (pi^2 M^2)) lam^{1/2}  -> grows in the IR.
 (iii) Tadpole: static TT response h(q) = -4 tau(q) / (M^2 q^2); 2 TT polarizations of 5;
      <h_ij h_ij> = 2 * 16 sigma_tau^2 / M^4 * (1/(2 pi^2)) int_{2pi/R} dq / q^2 = 16 sigma_tau^2 R / (2 pi^3 M^4) * ... (computed below).
 (iv) Physical-units window: l > D needs Lambda^5 < pi M^4 / (4 sigma^2 D)  (Lambda = 1/a);
      lattice bandwidth: any single-particle energy <~ pi Lambda (bounded hopping), so observed cosmic rays
      at 3e11 GeV need Lambda >~ 1e11 GeV (COMPARATOR: observed UHECR energies).
"""
import numpy as np
MPl = 1.221e19; M_phys = 2.435e18          # GeV
M = M_phys/MPl                             # reduced Planck mass in units a^-1 = M_Pl (scale-reference primitive)
print(f"M (reduced, lattice units at a^-1 = M_Pl) = {M:.4f};  M^4 = {M**4:.3e}")
for sig, src in [(0.035, 'R3 rot-avg, scalar m2=1'), (0.068, 'K1 per-direction, m2=1'), (0.081, 'K1 per-direction, m2=0.04'),
                 (0.34, 'K2 2D Delaunay stress (2D, indicative only)')]:
    W = 16*sig**2/M**4; l = 4*np.pi/W
    lam_star = (np.pi**2*M**2/sig)**2
    Vsite = 4*sig/M**2
    print(f"sigma={sig:5.3f} [{src}]: V per site = {Vsite:.2f} a^-2 (Born needs << 1), Born l = {l:.3g} a, "
          f"IR-relevance scale (ratio=1) = {lam_star:.3g} a, ratio at LIGO lam=6e40 a: {np.sqrt(6e40)*sig/(np.pi**2*M**2):.2e}")
# tadpole
for sig_tau in (0.068, 0.081):
    for R in (1e2, 1e10, 1.9e60):
        h2 = 2*16*sig_tau**2/M**4/(2*np.pi**2)*(R/(2*np.pi))
        print(f"tadpole sigma_tau={sig_tau}: <h_ij h_ij> over region R={R:.1e} a  = {h2:.2e}  (h_rms {np.sqrt(h2):.1e})")
# physical window
Gpc = 3.086e25/1.973e-16                    # GeV^-1
for sig in (0.035, 0.068):
    for D, name in ((Gpc, '1 Gpc'), (40e-3*Gpc, '40 Mpc')):
        Lam = (np.pi*M_phys**4/(4*sig**2*D))**0.2
        print(f"sigma={sig}: Born l > {name} needs Lambda < {Lam:.2g} GeV;  UHECR (3e11 GeV) needs Lambda >~ 1e11 GeV;"
              f" scale-reference primitive says Lambda = {MPl:.2g} GeV")
    for Lam, name in ((1e11, 'UHECR floor 1e11 GeV'), (MPl, 'a^-1 = M_Pl')):
        l = np.pi*M_phys**4/(4*sig**2*Lam**5)
        need = np.sqrt(l/Gpc)
        print(f"   at Lambda = {name}: Born l = {l:.2g} GeV^-1 = {l/Gpc:.2g} Gpc -> sigma must shrink by {1/need:.1e} to reach 1 Gpc")
