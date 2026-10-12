"""Z1 (C): physical translation of the node-level in-band fraction.
  f_B = eps * dw / (4 pi^2 c2^2 g) * eta_b/sinh(eta_b)      (all in l_k units; g = variance growth rate = c * sqrt(eps))
      = sqrt(eps) * dw * eta_b / (4 pi^2 c2^2 c sinh eta_b),  dw = (half-width of the band, rad/s) * l_k / c_light.
Lower-bound form (Z1 Prop. 4, filtered top rung ARGUED): B >= kappa * f_low * V_low(x), f_low = f_B with c = c_low, kappa = (1-2 delta)^2/2.
In-band variance e-folds: n_B = n_var - Lambda_B,  Lambda_B = -ln f_B,  n_var = c sqrt(eps) tau / l_k (variance e-folds, RL3b/RL4/Y1 convention).
Geometry (Y1): tau = sqrt(2 D cT + (cT)^2) for emission a time T before the retarded time; growth-frame boost gamma_b = (D + cT)/tau.
"""
import numpy as np
cl = 2.99792458e8; lP = 1.616255e-35; Gpc = 3.0857e25; yr = 3.15576e7
c2 = [0.692180, 0.660865, 0.631121]; clow = [0.628, 0.670, 0.712]; kh = [2.7348, 2.8353, 3.2539]
eV = 1.519267e15   # rad/s per eV
bands = [("radio 1 Hz channel", 2*np.pi*0.5),
         ("radio 1 kHz channel (maser line)", 2*np.pi*500.),
         ("radio 5 GHz, 500 MHz continuum", 2*np.pi*250e6),
         ("optical 0.1 nm channel at 500 nm", np.pi*cl*0.1e-9/(500e-9)**2),
         ("optical V band 507-595 nm", 0.5*(2*np.pi*cl/507e-9 - 2*np.pi*cl/595e-9)),
         ("X-ray 0.5-2 keV", 0.75e3*eV),
         ("GW LIGO 20-1000 Hz", 2*np.pi*490.)]
def eta_of(gb): return np.arccosh(max(gb, 1.0))
def boostfac(eta): return 1.0 if eta < 1e-8 else eta/np.sinh(eta)
for lk in [7.9e-20, 1e-19]:
    eps = (lP/lk)**4; se = np.sqrt(eps)
    print("=== l_k = %.2e m: eps = %.3e, sqrt(eps) = %.3e" % (lk, eps, se))
    print("  band-only factor (no boost), op0..2:  -ln f_B with c_low [proved rate] / with k_h [node-ladder rate]")
    for name, dw in bands:
        dwt = dw*lk/cl
        fl = [se*dwt/(4*np.pi**2*c2[i]**2*clow[i]) for i in range(3)]
        fk = [se*dwt/(4*np.pi**2*c2[i]**2*kh[i]) for i in range(3)]
        print("   %-36s dw*l_k/c = %.2e : Lambda = %s / %s" % (name, dwt, " ".join("%.1f" % -np.log(x) for x in fl), " ".join("%.1f" % -np.log(x) for x in fk)))
    cases = [("lensed, 1 Gpc, T = 1 s", Gpc, 1.0), ("lensed, 1 Gpc, T = 8 h", Gpc, 8*3600.), ("lensed, 1 Gpc, T = 1 yr", Gpc, yr),
             ("lensed, 5 Gpc, T = 1 yr", 5*Gpc, yr), ("quasar, 1 Gpc, T = 1e7 yr", Gpc, 1e7*yr),
             ("on-cone radio emitter 1 Gpc, s = 3 m", Gpc, 3.0/cl), ("maser emitter 1 Gpc, s = 1 km", Gpc, 1e3/cl),
             ("GW merger 1 Gpc, s = 10 km (RL4 setting)", Gpc, 1e4/cl), ("GW inspiral 1 Gpc, 1 yr", Gpc, yr),
             ("lab lamp 1 m, on 1 h", 1.0, 3600.), ("lab lamp 1 m, on 1 day", 1.0, 86400.)]
    print("  case: tau [m], gamma_b, eta_b, boost penalty -ln(eta/sinh eta); then per band: n_var(c_low) - Lambda_B(c_low) = n_B  | same with k_h  (op0)")
    for cname, D, T in cases:
        cT = cl*T; tau = np.sqrt(2*D*cT + cT**2); gb = (D + cT)/tau; eta = eta_of(gb); bpen = -np.log(boostfac(eta))
        nl = clow[0]*se*tau/lk; nk = kh[0]*se*tau/lk
        print("  %-42s tau=%.2e gamma_b=%.2e eta_b=%.2f boost-pen=%.1f  n_var=%.3g (c_low) / %.3g (k_h)" % (cname, tau, gb, eta, bpen, nl, nk))
        for name, dw in bands:
            if ("GW" in cname) != ("GW" in name): continue
            dwt = dw*lk/cl
            LB_l = -np.log(se*dwt/(4*np.pi**2*c2[0]**2*clow[0])) + bpen
            LB_k = -np.log(se*dwt/(4*np.pi**2*c2[0]**2*kh[0])) + bpen
            print("      %-36s Lambda_B = %.1f / %.1f   n_B = %.4g / %.4g" % (name, LB_l, LB_k, nl - LB_l, nk - LB_k))
    # crossover emission duration T* at which n_B = 0 for optical V band and radio continuum, 1 Gpc (c_low / k_h)
    print("  crossover: emission duration T* before retarded time for which n_var = Lambda_B (1 Gpc, op0):")
    for name, dw in bands[2:5]:
        for lab, cc in [("c_low", clow[0]), ("k_h", kh[0])]:
            lo, hi = -12.0, 12.0
            for _ in range(200):
                mid = 0.5*(lo+hi); T = 10**mid; cT = cl*T; tau = np.sqrt(2*Gpc*cT + cT**2); gb = (Gpc+cT)/tau; eta = eta_of(gb)
                LB = -np.log(se*dw*lk/cl/(4*np.pi**2*c2[0]**2*cc)) - np.log(boostfac(eta))
                if cc*se*tau/lk > LB: hi = mid
                else: lo = mid
            print("      %-36s %s: T* = %.3g s" % (name, lab, 10**hi))
