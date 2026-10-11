"""Z2 (D): physical translation at l_k = 7.9e-20 m (photon, collider-bounded; X1), l = l_P.
In-band fraction (node ladder, far field; z2_B):  S(w)/V = pi Wh^2 sqrt(eps) l_k / k  (flat for w << 1/l_k)
   real field, physical band w0 +- Dw counted at +-w0 (Dk = Dw/c half-width):  f = 2 Dk (S/V)/pi = 2 Dk Wh^2 sqrt(eps) l_k / k.
   (complex-carrier one-band fraction is half of this.)
Rates: proved c_low = 0.628 (RL4, op0), derived k_h = 2.7348 (RL3b, op0); gamma = c sqrt(eps)/l_k (variance e-folds per metre of proper time).
Proper time from an edged emission event Dt before the retarded time to the observer at distance D: tau = sqrt((D + c Dt)^2 - D^2).
Polynomial prefactor budget (ARGUED; z2 report section 4): per-emitter incoherent-cell factor l_k^3/v, the (gamma tau)^p factor with
|p| <= 3, an eps^a factor with |a| <= 5 (a*ln(1/eps) <= 725), and the geometric D^2/l_k^2 or 1/(gamma tau) factors; all enter ln linearly.
"""
import numpy as np
lP = 1.616255e-35; lk = 7.9e-20; c = 2.998e8; Gpc = 3.0857e25
eps = (lP/lk)**4; se = np.sqrt(eps)
Wh_lo, Wh_hi = 0.22993, 0.24193        # 1/(2 pi c2) and the Volterra value (op0)
k_h = 2.7348; c_low = 0.628
SV_lo = np.pi*Wh_lo**2*se*lk/k_h; SV_hi = np.pi*Wh_hi**2*se*lk/k_h
print("eps = %.4g, sqrt(eps) = %.4g, sqrt(eps)/l_k = %.4g /m" % (eps, se, se/lk))
print("gamma_low = %.4g /m (proved), gamma_h = %.4g /m (derived)" % (c_low*se/lk, k_h*se/lk))
print("S(0)/V = pi Wh^2 sqrt(eps) l_k / k_h = %.3g .. %.3g m  (= %.3g .. %.3g s)" % (SV_lo, SV_hi, SV_lo/c, SV_hi/c))
bands = [("optical V band, lambda 550 nm, FWHM 90 nm", np.pi*90e-9/(550e-9)**2),
         ("optical narrow filter, 1 nm at 550 nm", np.pi*1e-9/(550e-9)**2),
         ("radio 1 GHz, 100 MHz bandwidth", 2*np.pi*50e6/c),
         ("radio 1 GHz, 1 MHz channel", 2*np.pi*0.5e6/c),
         ("VLBI 1 GHz, 1 kHz fringe-rate/channel", 2*np.pi*500/c)]
print("\nIn-band fraction (real field) f = 2 Dk (S/V)/pi  (Dk = half-width wavenumber)")
F = {}
for name, Dk in bands:
    f_lo, f_hi = 2*Dk*SV_lo/np.pi, 2*Dk*SV_hi/np.pi; F[name] = (f_lo, f_hi)
    print("  %-45s Dk=%.3g /m : f = %.3g .. %.3g  (ln f = %.1f .. %.1f)" % (name, Dk, f_lo, f_hi, np.log(f_lo), np.log(f_hi)))
cases = []
for DG in [1, 3, 5]:
    for Tobs, lab in [(1.0, "1 s"), (3600.0, "1 h"), (3.156e7, "1 yr")]:
        cases.append(("lensed source D=%d Gpc, emission %s before retarded time" % (DG, lab), DG*Gpc, c*Tobs))
cases.append(("lab lamp at 1 m, on for 1 h", 1.0, c*3600))
cases.append(("lab lamp at 1 m, on for 1 day", 1.0, c*86400))
cases.append(("lab lamp at 1 m, on for 1 yr", 1.0, c*3.156e7))
print("\nVariance e-fold budgets gamma*tau (rate only) and in-band log relative variance ln(f) + gamma tau (prefactor budget separate)")
for name, D, cdt in cases:
    tau = np.sqrt(2*D*cdt + cdt**2)
    nl = c_low*se/lk*tau; nh = k_h*se/lk*tau
    fo = F["optical V band, lambda 550 nm, FWHM 90 nm"]; fr = F["radio 1 GHz, 100 MHz bandwidth"]
    print("  %-60s tau=%.3g m  gamma tau = %.3g (proved) / %.3g (derived)  ln(f_opt)+gt = %.4g ; ln(f_radio)+gt = %.4g"
          % (name, tau, nl, nh, np.log(fo[0]) + nl, np.log(fr[0]) + nl))
# threshold emission delay for which the proved exponent pays the in-band fraction plus a prefactor budget B
print("\nEmission delay Dt* at which gamma_low*tau = |ln f| + B  (B = prefactor budget in e-folds)")
for B in [0, 300, 1000]:
    for name in ["optical V band, lambda 550 nm, FWHM 90 nm", "radio 1 GHz, 100 MHz bandwidth"]:
        need = -np.log(F[name][0]) + B; tau = need/(c_low*se/lk)
        for DG in [1, 5]:
            D = DG*Gpc; cdt = tau**2/(np.sqrt(D**2 + tau**2) + D)
            print("  B=%4d %-45s D=%d Gpc: tau*=%.3g m, Dt*=%.3g s ; lab (D=1 m): Dt*=%.3g s (%.3g days)" %
                  (B, name, DG, tau, cdt/c, (np.sqrt(1 + tau**2) - 1)/c, (np.sqrt(1 + tau**2) - 1)/c/86400))

# full log budget for the in-band relative noise N_in/S (per emitter, phase-averaged; Y1 2.1):
#   ln(N_in/S) >= gamma_low tau - 1.5 ln(tau/l_k) + ln f - B   (B = remaining polynomial prefactor budget, ARGUED <= 1000)
print("\nFull budget ln(N_in/S) >= gamma_low*tau - 1.5 ln(tau/l_k) + ln f - B, with B = 1000 (optical V band / radio 100 MHz)")
for name, D, cdt in cases:
    tau = np.sqrt(2*D*cdt + cdt**2); nl = c_low*se/lk*tau; lt = 1.5*np.log(tau/lk)
    fo = F["optical V band, lambda 550 nm, FWHM 90 nm"][0]; fr = F["radio 1 GHz, 100 MHz bandwidth"][0]
    print("  %-60s gamma tau=%.3g  -1.5 ln(tau/l_k)=%.0f  => optical %.4g ; radio %.4g" % (name, nl, -lt, nl - lt + np.log(fo) - 1000, nl - lt + np.log(fr) - 1000))
