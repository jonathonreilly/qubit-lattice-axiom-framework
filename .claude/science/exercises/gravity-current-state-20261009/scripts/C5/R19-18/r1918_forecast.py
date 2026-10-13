#!/usr/bin/env python3
"""R19-18 [F]: expected (mock) sensitivity of BAO + compressed CMB to the L1 sink, independent of DR2's actual scatter.
 Mock data = the LCDM best fit to DESI DR2 (RECALLED) + compressed CMB, exactly (no noise); covariance = DR2's x {1, 1/2, 1/3}
 (DR2 now; ~DESI-final; ~DESI-final + Euclid/4MOST-class BAO: scalings are assumptions, not RECALLED forecasts).
 Delta chi2(g_L) profiled over (h, omega_m) = the Asimov significance of g_L = kappa_p gamma/H0.
 Functions copied verbatim from r1918_obs.py.  Run: OMP_NUM_THREADS=2 python3 r1918_forecast.py
"""

import numpy as np, time
from scipy import integrate, optimize, interpolate
t0 = time.time()
C_KMS = 299792.458
GRID = [0.016, 0.024, 0.032, 0.047]          # gamma/H0: R14-2 drag ceilings (signed 0.016-0.024; conservative 0.032-0.047), vR14-2:3

# ---------------------------------------------------------------- background
def solve_bg(Om, h, gL, Or_h2=4.18e-5, ai=1e-9, iters=6):
    Or = Or_h2 / h**2
    OL = 1 - Om - Or
    lna = np.linspace(np.log(ai), 0.0, 6001)
    for _ in range(iters):
        def rhs(x, y):
            a = np.exp(x)
            Os = y[0] / a**3
            E2 = Or / a**4 + Om / a**3 + OL + Os
            return [-2 * gL * np.sqrt(max(E2, 1e-300)) * a**3]
        sol = integrate.solve_ivp(rhs, (lna[0], 0.0), [0.0], t_eval=lna, rtol=1e-10, atol=1e-14)
        Y = sol.y[0]
        Os1 = Y[-1]
        OL_new = 1 - Om - Or - Os1
        if abs(OL_new - OL) < 1e-13:
            OL = OL_new
            break
        OL = OL_new
    a = np.exp(lna)
    Os = Y / a**3
    E = np.sqrt(Or / a**4 + Om / a**3 + OL + Os)
    return dict(a=a, lna=lna, E=E, Os=Os, OL=OL, Or=Or, Om=Om, h=h, gL=gL)

def dist_funcs(bg):
    z = 1 / bg['a'][::-1] - 1
    E = bg['E'][::-1]
    Ez = interpolate.interp1d(z, E, kind='cubic')
    zz = np.concatenate([np.linspace(0, 3, 3001), np.geomspace(3.001, 1200, 4000)])
    Ei = Ez(zz)
    chi = integrate.cumulative_trapezoid(1 / Ei, zz, initial=0.0)
    chi_f = interpolate.interp1d(zz, chi, kind='cubic')
    # lookback time (units 1/H0): t_lb = int dz /((1+z) E)
    tl = integrate.cumulative_trapezoid(1 / ((1 + zz) * Ei), zz, initial=0.0)
    tl_f = interpolate.interp1d(zz, tl, kind='cubic')
    # age t0 H0
    aa = bg['a']; EE = bg['E']
    t0H = integrate.trapezoid(1 / (aa * EE) * aa, np.log(aa))  # dt = da/(a E) = dlna / E
    return Ez, chi_f, tl_f, t0H

# DESI DR2 BAO (RECALLED, arXiv:2503.14738 Table IV): z, DM/rd, sig, DH/rd, sig, corr ; BGS DV/rd
DESI = [(0.510, 13.587, 0.169, 21.863, 0.427, -0.475), (0.706, 17.347, 0.180, 19.458, 0.332, -0.423),
        (0.934, 21.574, 0.153, 17.641, 0.193, -0.425), (1.321, 27.605, 0.320, 14.178, 0.217, -0.437),
        (1.484, 30.519, 0.758, 12.816, 0.513, -0.489), (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
BGS = (0.295, 7.944, 0.075)
RD, RSTAR, ZSTAR = 147.09, 144.43, 1089.92          # Planck 2018 (RECALLED)
TH, STH = 1.04110e-2, 0.00031e-2                    # theta_* (RECALLED)
WM, SWM = 0.1430, 0.0011                             # Omega_m h^2 (RECALLED)

def chi2(par, gL, inflate=1.0, use_cmb=True):
    h, wm = par
    if not (0.5 < h < 0.9 and 0.10 < wm < 0.20):
        return 1e9
    Om = wm / h**2
    bg = solve_bg(Om, h, gL, iters=4)
    Ez, chi, tl, tH = dist_funcs(bg)
    dh = C_KMS / (100 * h)
    c2 = 0.0
    for z, dm, sdm, dhh, sdh, r in DESI:
        DM = dh * chi(z) / RD; DH = dh / Ez(z) / RD
        cov = np.array([[sdm**2, r * sdm * sdh], [r * sdm * sdh, sdh**2]]) * inflate**2
        d = np.array([DM - dm, DH - dhh])
        c2 += d @ np.linalg.solve(cov, d)
    z, dv, sdv = BGS
    DV = (z * (dh * chi(z))**2 * dh / Ez(z))**(1 / 3) / RD
    c2 += ((DV - dv) / (sdv * inflate))**2
    if use_cmb:
        th = RSTAR / (dh * chi(ZSTAR))
        c2 += ((th - TH) / STH)**2 + ((wm - WM) / SWM)**2
    return c2

def prof(gL, inflate=1.0, x0=(0.68, 0.143)):
    r = optimize.minimize(chi2, x0, args=(gL, inflate), method='Nelder-Mead', options=dict(xatol=1e-6, fatol=1e-6, maxiter=400))
    return r.fun, r.x

def prof(gL, inflate=1.0, x0=(0.68, 0.143)):
    r = optimize.minimize(chi2, x0, args=(gL, inflate), method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-7, maxiter=600))
    return r.fun, r.x
c0, xb = prof(0.0)
h0, wm0 = xb
bgf = solve_bg(wm0 / h0**2, h0, 0.0)
Ezf, chif, _, _ = dist_funcs(bgf)
dh = C_KMS / (100 * h0)
DESI = [(z, dh * chif(z) / RD, sdm, dh / Ezf(z) / RD, sdh, r) for (z, dm, sdm, dhh, sdh, r) in DESI]
zb = BGS[0]
BGS = (zb, (zb * (dh * chif(zb))**2 * dh / Ezf(zb))**(1 / 3) / RD, BGS[2])
TH = RSTAR / (dh * chif(ZSTAR)); WM = wm0
print("[F] mock = LCDM best fit h = %.4f, omega_m = %.4f; Asimov Delta chi2 (profiled over h, omega_m):" % (h0, wm0))
for scale in (1.0, 0.5, 1 / 3):
    STH_s = STH
    row = []
    for g in (0.016, 0.024, 0.032, 0.047, -0.047):
        c, x = prof(g, scale, xb)
        row.append("g_L=%+.3f: %.2f" % (g, c))
    print("     BAO errors x%.2f (CMB fixed): %s" % (scale, " ; ".join(row)))
print("    runtime %.1f s" % (time.time() - t0))
