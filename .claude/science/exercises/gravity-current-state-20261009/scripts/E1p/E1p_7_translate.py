"""E1' (d): translation of the laws to physical numbers at ell = ell_P (rho = ell_P^-4).
Laws used (labels in the report):
  massless:  Var/mean^2 = (1 + kappa s/D)/Nbar,  Nbar = rho int_src e^{-rho V} ~ sqrt6 V_s/(2 D ell^2)  (EXACT mean, CHECKED Fano)
  link arrival offset: sigma-distribution of links ~ e^{-pi sigma^2/24}: <sigma> = 12/(pi sqrt6) ell^2, delay = sigma/(2 D) (EXACT)
  links per event, slab past of depth T: sqrt6 pi (T/ell)^2 (EXACT leading order)
  massive point-to-point floor: sd/envelope = sqrt(F) * sqrt(3pi)/(24 pi^2) * 4 pi sqrt(pi/2) (m tau)^{3/2} = 0.2036 sqrt(F) (m tau)^{3/2}
  compact-source seed (per end): Var/envelope^2 = (sqrt6/96) (m ell)^2 (m tau)^3
  packet seed: Var/mean^2 = (sqrt6/(24 pi)) (m^2 ell sigma)^2
  overlap-free renewal growth of variance: exp(gamma tau), gamma = (sqrt6/(12 pi))^{1/2} m^2 ell = 0.2552 m^2 ell (ARGUED)
  mean's slow growth: ~0.5 m^3 ell^2 (CHECKED for m ell = 0.1-0.4)
"""
import numpy as np
lP = 1.616255e-35; MPl = 1.220890e19; hbarc = 1.97327e-16   # m, GeV, GeV m
Gpc = 3.0857e25; Mpc = 3.0857e22; ct0 = 13.79e9 * 3.15576e7 * 2.99792458e8
c = 2.99792458e8
print("=== GW proxy (massless link field, single observation event) ===")
for name, Vs, s, D in [("BNS, two 12-km stars, 40 Mpc", 2 * 4 / 3 * np.pi * 1.2e4**3, 1.0e5, 40 * Mpc),
                       ("BNS, two 12-km stars, 1 Gpc", 2 * 4 / 3 * np.pi * 1.2e4**3, 1.0e5, Gpc),
                       ("100-km ball, 1 Gpc", 4 / 3 * np.pi * 1e5**3, 1e5, Gpc),
                       ("1-km ball, 1 Gpc", 4 / 3 * np.pi * 1e3**3, 1e3, Gpc)]:
    N = np.sqrt(6) * Vs / (2 * D * lP**2)
    for kappa in [6.0]:
        rel = np.sqrt((1 + kappa * s / D) / N)
    print(f"{name:32s}: Nbar = {N:.2e} links, rel noise = {rel:.2e} (x10 for (v/c)^-2 quadrupole suppression: {10*rel:.1e}); "
          f"kappa s/D = {6*s/D:.1e}")
sig_mean = 12 / (np.pi * np.sqrt(6)); sig_sd = np.sqrt(12 / np.pi - sig_mean**2)
for D, lab in [(40 * Mpc, "40 Mpc"), (Gpc, "1 Gpc")]:
    dt = sig_mean * lP**2 / (2 * D) / c
    print(f"arrival offset at {lab}: mean {dt:.2e} s, spread {sig_sd*lP**2/(2*D)/c:.2e} s; fractional speed offset {sig_mean*lP**2/(2*D*D):.1e}  (GW170817: |cg-c|/c < ~1e-15)")
print(f"links per event, slab past of depth c t0 = {ct0:.3e} m: {np.sqrt(6)*np.pi*(ct0/lP)**2:.2e}")
print(f"mean-kernel deviation from G_R at r = 1e-19 m: <sigma>/(2 r^2) = {sig_mean*lP**2/(2*1e-38):.1e}")

print("\n=== matter at ell = ell_P ===")
for name, mGeV in [("electron", 0.51099895e-3), ("proton", 0.938272)]:
    ml = mGeV / MPl; lam = hbarc / mGeV         # m ell, reduced Compton wavelength (m)
    m2l = ml**2 / lP                              # m^2 ell in 1/m
    # point-to-point floor: 0.2036 (m tau)^1.5 = 1
    mt_pp = (1 / 0.2036)**(2 / 3)
    # compact-source seed: c_e (m ell)^2 (m tau)^3 = 1, one end (c_e) or two ends (2 c_e), first-chaos lower bound c_e/sqrt2
    ce = np.sqrt(6) / 96
    taus = {k: (1 / (cc * ml**2))**(1 / 3) * lam for k, cc in [("2 ends", 2 * ce), ("1 end", ce), ("lower bound", ce / np.sqrt(2))]}
    print(f"{name}: m ell = {ml:.3e}, Compton lambda-bar = {lam:.3e} m, m^2 ell = {m2l:.3e} /m")
    print(f"   point-to-point G_m(x,y): noise > mean envelope at m tau > {mt_pp:.2f}  -> tau > {mt_pp*lam:.2e} m (any rho)")
    print("   compact-source G_m J, single event: noise = mean at tau = " + ", ".join(f"{k}: {v:.3e} m" for k, v in taus.items()))
    for sig in [1e-6, 1e-3, 1.0, 1e3]:
        R = np.sqrt(6) / (24 * np.pi) * (m2l * sig)**2
        print(f"   packet of size {sig:g} m: Var/mean^2 = {R:.2e}")
    g = 0.2552 * m2l
    print(f"   overlap-free renewal growth of variance: rate {g:.3e} /m -> e-fold every {1/g:.3e} m of proper time; at 1 km factor {np.exp(g*1e3):.3f}")
    print(f"   mean's slow growth ~0.5 m^3 ell^2 = {0.5*ml**2/lam:.2e} /m -> e-fold {lam/(0.5*ml**2):.2e} m")
