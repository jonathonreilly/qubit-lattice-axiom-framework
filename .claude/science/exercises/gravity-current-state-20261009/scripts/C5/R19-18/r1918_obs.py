#!/usr/bin/env python3
"""R19-18 [B]/[G]/[F]/[S]: observables of E2's friction lifted to FRW.
 [S1] sirens, both lifts: d_L^GW/d_L^EM = exp(gamma t_lb(z)/2) (r1918_lift [L3]); Xi_0, n of the Belgacem fit; numeric check by
      integrating h'' + (2 calH + a gamma) h' + k^2 h = 0 through a LCDM background (WKB amplitude ratio).
 [S2] toy siren Fisher (ET-like bright sirens; LISA-like MBHB) -- a TOY to calibrate the RECALLED forecasts, not a forecast.
 [S3] P-r14a (zero-integral kernel) sirens: Re gamma(w) = gamma0 w^2/(w^2 + wc^2), w = 2 pi f_obs (1+z') along the path.
 [B1] L1 background: friction pressure p_X = kappa_p gamma H/(4 pi G), Pi's k=0 part pressureless (lift A, Lemma F0):
      d(Omega_s a^3)/da = -2 g_L E a^2, g_L = kappa_p gamma/H0, flat, Omega_L fixed by E(1) = 1 (iterated).
 [B2] fit to DESI DR2 BAO (RECALLED) + compressed CMB (RECALLED: 100 theta_* , omega_m prior, r_d, r_s* fixed by early physics):
      profile chi^2(g_L) over (h, omega_m).  Errors x1.0 and x1.5 (robustness).
 [G1] growth: delta'' + (2 + dlnE/dlna) delta' = 1.5 Omega_m a^-3/E^2 delta (sink smooth), f sigma8 ratio vs g_L = 0 (same A_s, early norm).
 [G2] ISW proxy: change of the late potential decay 1 - (D/a)_0/(D/a)_early.
 [G3] L0 quasi-static friction on subhorizon potentials: relative (gamma/H)(1 - f)(aH/k)^2 (estimate, from the linear law).
 [M1] L1-M (global fixed reference, p_X ~ (a_ref/a)^6): size at CMB and BBN.
Subtraction: none.  Units: H0 = 1 in [B], distances in c/H0 then Mpc.  Run: OMP_NUM_THREADS=2 python3 r1918_obs.py
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

# ---------------------------------------------------------------- [S1]
print("[S1] sirens (both lifts): d_L^GW/d_L^EM = exp(gamma t_lb(z)/2); background Planck-like LCDM (Om = 0.3153, h = 0.6736; RECALLED)")
bg0 = solve_bg(0.3153, 0.6736, 0.0)
Ez0, chi0, tl0, t0H = dist_funcs(bg0)
print("     H0 t0 = %.4f ; H0 t_lb: z=0.0098 %.5f, 0.1 %.4f, 0.5 %.4f, 1 %.4f, 2 %.4f, 5 %.4f" % (t0H, tl0(0.0098), tl0(0.1), tl0(0.5), tl0(1.0), tl0(2.0), tl0(5.0)))
zs = [0.0098, 0.1, 0.3, 0.5, 1.0, 2.0, 5.0]
for gH in GRID + [1.0]:
    rat = [np.exp(gH * tl0(z) / 2) for z in zs]
    Xi0 = np.exp(gH * t0H / 2)
    # Belgacem fit Xi = Xi0 + (1 - Xi0)/(1+z)^n : n from least squares on z in [0, 5]
    zf = np.linspace(0.01, 5, 300)
    tgt = np.exp(gH * tl0(zf) / 2)
    nfit = optimize.minimize_scalar(lambda n: np.sum((Xi0 + (1 - Xi0) / (1 + zf)**n - tgt)**2), bounds=(0.1, 5), method='bounded').x
    resid = np.max(np.abs(Xi0 + (1 - Xi0) / (1 + zf)**nfit - tgt))
    print("     gamma = %.3f H0: ratio-1 at z=%s : %s ; Xi_0 - 1 = %.4f ; n = %.3f (max fit resid %.1e)" %
          (gH, zs, " ".join("%.5f" % (r - 1) for r in rat), Xi0 - 1, nfit, resid))
print("     RECALLED ET forecast sigma(Xi0) = 0.008 (Belgacem et al. 2018) -> sigma(gamma/H0) = %.4f if applied to Xi0 = exp(gamma t0/2): 0.047/0.032/0.024/0.016 H0 at %.1f/%.1f/%.1f/%.1f sigma"
      % (0.008 / (t0H / 2), *(g / (0.008 / (t0H / 2)) for g in (0.047, 0.032, 0.024, 0.016))))
print("     current: GWTC-3 Xi0 = 1.2 +- 0.7 (68%%, RECALLED via vR12-7:11) -> gamma < %.2f H0 (68%%) ; GW170817 ratio-1 at gamma = 0.047 H0: %.1e" % (2 * np.log(1.9) / t0H, np.exp(0.047 * tl0(0.0098) / 2) - 1))
print("     analytic small-z slope: Xi - 1 ~ (gamma/2H0) z => n = 1/(H0 t0) = %.3f" % (1 / t0H))
# numerical mode check: conformal time, k >> calH
def mode_ratio(gH, kc=400.0, z_em=1.0):
    # integrate in ln a from a_em to 1: h'' + (2 calH + a gamma) h' + k^2 h = 0 ; use variable x = ln a, d eta = dx/(a^2 H)... with H0 = 1
    a_em = 1 / (1 + z_em)
    def rhs(x, y):
        a = np.exp(x); E = Ez0(1 / a - 1); calH = a * E
        h, hp = y                       # hp = dh/deta
        deta_dx = 1 / calH
        return [hp * deta_dx, (-(2 * calH + a * gH) * hp - kc**2 * h) * deta_dx]
    out = []
    for g in (0.0, gH):
        global_g = g
        def r(x, y, g=g):
            a = np.exp(x); E = Ez0(1 / a - 1); calH = a * E
            h, hp = y
            return [hp / calH, (-(2 * calH + a * g) * hp - kc**2 * h) / calH]
        s = integrate.solve_ivp(r, (np.log(a_em), 0.0), [1.0, 0.0], rtol=1e-10, atol=1e-13, max_step=0.0005, dense_output=True)
        hh = s.sol(0.0)                         # WKB invariant at a = 1 (O((calH/k)^2) corrections)
        amp = np.sqrt(hh[0]**2 + (hh[1] / kc)**2)
        out.append(amp)
    return out[1] / out[0]
for gH in (0.047, 1.0):
    rr = mode_ratio(gH)
    print("     mode check (k = 400 H0, z_em = 1): A(gamma)/A(0) = %.6f vs exp(-gamma t_lb/2) = %.6f" % (rr, np.exp(-gH * tl0(1.0) / 2)))

# ---------------------------------------------------------------- [S2] toy Fisher
print("[S2] TOY siren Fisher for gamma/H0 (EM cosmology fixed by CMB+BAO; d ln(d_L^GW)/d(gamma/H0) = H0 t_lb/2):")
def sig_lens(z):
    return 0.066 * ((1 - (1 + z)**-0.25) / 0.25)**1.8      # RECALLED lensing fit (Tamanini et al. style)
def toy(N, zmax, sinst, label, zdist='vol'):
    zz = np.linspace(0.02, zmax, 400)
    if zdist == 'vol':
        w = np.array([chi0(z)**2 / Ez0(z) / (1 + z) for z in zz])
    else:
        w = np.ones_like(zz)
    w = w / w.sum() * N
    sig = np.sqrt(sinst(zz)**2 + sig_lens(zz)**2)
    der = np.array([tl0(z) / 2 for z in zz])
    F = np.sum(w * der**2 / sig**2)
    s = 1 / np.sqrt(F)
    print("     %-58s sigma(gamma/H0) = %.4f ; sigma(Xi0) ~ %.4f ; gamma = 0.047/0.032/0.024/0.016 H0 at %.1f/%.1f/%.1f/%.1f sigma"
          % (label, s, s * t0H / 2, 0.047 / s, 0.032 / s, 0.024 / s, 0.016 / s))
    print("       -> 2 sigma threshold gamma >= %.3f H0 ; 3 sigma threshold gamma >= %.3f H0" % (2 * s, 3 * s))
    return s
toy(1000, 2.0, lambda z: 0.05 + 0.05 * z, "ET-like: 1000 BNS+counterparts, z<2, sigma_inst = 5%+5%z")
toy(300, 2.0, lambda z: 0.05 + 0.05 * z, "ET-like: 300 BNS+counterparts")
toy(1000, 2.0, lambda z: 0.10 + 0.10 * z, "ET-like: 1000 BNS, sigma_inst = 10%+10%z")
toy(30, 6.0, lambda z: 0.02 + 0.0 * z, "LISA-like: 30 MBHB+counterparts, z<6, sigma_inst = 2% (lensing dominated)", zdist='flat')
toy(100, 6.0, lambda z: 0.02 + 0.0 * z, "LISA-like: 100 MBHB+counterparts", zdist='flat')

# ---------------------------------------------------------------- [S3] P-r14a
print("[S3] P-r14a zero-integral kernel (vR14-2:5): Re gamma(w)/gamma0 = w^2/(w^2 + wc^2), w = 2 pi f_obs (1+z') along the path")
def ratio_r14a(g0, wc, fobs, z):
    zz = np.linspace(0, z, 400)
    w = 2 * np.pi * fobs * (1 + zz)
    reg = w**2 / (w**2 + wc**2)
    integrand = reg / ((1 + zz) * Ez0(zz))
    return np.exp(g0 * integrate.trapezoid(integrand, zz) / 2)
for g0, wc, lab in ((7.0, 1e3, "gamma0 = 7 H0, wc = 1e3 (R14-2 example)"), (31.7, 3e3, "gamma0 = 31.7 H0, wc = 3e3 (signed-timing ceiling, vR14-2:5)"),
                    (62.0, 3e3, "gamma0 = 62 H0, wc = 3e3 (conservative ceiling)"), (1.0, 330.0, "gamma0 = 1 H0, wc = 330")):
    row = []
    for z in (0.0098, 0.1, 0.5, 1.0):
        r30, r300, r1k = (ratio_r14a(g0, wc, f, z) for f in (30.0, 300.0, 1000.0))
        row.append("z=%g: %.3f/%.3f/%.3f" % (z, r30, r300, r1k))
    lisa = ratio_r14a(g0, wc, 1e-3, 3.0)
    print("     %-58s d_L ratio at f = 30/300/1000 Hz: %s ; LISA (1 mHz, z=3): ratio-1 = %.1e" % (lab, " ; ".join(row), lisa - 1))

# ---------------------------------------------------------------- [B1]/[B2]
print("[B1] L1 background (p_X = kappa_p gamma H/4 pi G; lift A): Omega_s(z), Delta H/H at fixed (Om, h) = (0.3153, 0.6736)")
for gL in (0.047, -0.047):
    bg = solve_bg(0.3153, 0.6736, gL)
    Ez, chi, tl, tH = dist_funcs(bg)
    zsel = [0, 0.5, 1, 2, 5, 1089]
    Osz = interpolate.interp1d(1 / bg['a'][::-1] - 1, bg['Os'][::-1])
    print("     g_L = %+.3f: Omega_L = %.5f ; Omega_s(z)/E(z)^2 at z=%s: %s ; Delta H/H: %s ; w_DE,eff(z=0) = %.4f" % (
        gL, bg['OL'], zsel, " ".join("%+.2e" % (Osz(z) / Ez(z)**2) for z in zsel),
        " ".join("%+.2e" % (Ez(z) / Ez0(z) - 1) for z in zsel[1:]),
        (-bg['OL'] + (2 / 3) * gL * 1.0) / (bg['OL'] + Osz(0.0))))

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
print("[B2] DESI DR2 BAO + compressed CMB (all RECALLED), profiled over (h, omega_m); r_d, r_s* fixed (L1 is negligible at z > 10):")
for inflate in (1.0, 1.5):
    c0, x0 = prof(0.0, inflate)
    print("     errors x%.1f: LCDM chi2_min = %.2f at h = %.4f, omega_m = %.4f (Om = %.4f), 13 BAO + 2 CMB numbers" % (inflate, c0, x0[0], x0[1], x0[1] / x0[0]**2))
    gs = np.array([-0.10, -0.06, -0.047, -0.03, -0.016, -0.008, 0.0, 0.008, 0.016, 0.024, 0.032, 0.047, 0.06, 0.10, 0.14, 0.20])
    out = []
    for g in gs:
        c, x = prof(g, inflate, x0)
        out.append(c - c0)
    out = np.array(out)
    print("       g_L:      " + " ".join("%+7.3f" % g for g in gs))
    print("       dchi2:    " + " ".join("%+7.2f" % d for d in out))
    # 1D profile: best fit and 95% (dchi2 = 3.84) interval by interpolation
    fi = interpolate.interp1d(gs, out, kind='cubic')
    gg = np.linspace(gs[0], gs[-1], 4001)
    dd = fi(gg)
    gbest = gg[np.argmin(dd)]
    dmin = dd.min()
    ok = gg[dd - dmin <= 3.84]
    ok2 = gg[dd - dmin <= 1.0]
    print("       best g_L = %+.4f (dchi2 = %.2f) ; 68%%: [%+.4f, %+.4f] ; 95%%: [%+.4f, %+.4f] (kappa_p gamma/H0)" % (gbest, dmin, ok2[0], ok2[-1], ok[0], ok[-1]))
    print("       dchi2 relative to g_L = 0 at the drag ceilings (kappa_p = 1): 0.016 -> %+.2f, 0.024 -> %+.2f, 0.032 -> %+.2f, 0.047 -> %+.2f" %
          tuple(fi(g) for g in (0.016, 0.024, 0.032, 0.047)))
# BAO-only shape check (no CMB): does g_L degenerate with Om?
cB0 = optimize.minimize(lambda p: chi2(p, 0.0, 1.0, False), (0.68, 0.143), method='Nelder-Mead').fun
cB1 = optimize.minimize(lambda p: chi2(p, 0.047, 1.0, False), (0.68, 0.143), method='Nelder-Mead').fun
print("     BAO alone (h r_d and Om free): dchi2(g_L = 0.047) = %+.2f (h, omega_m degenerate; shape only)" % (cB1 - cB0))

# ---------------------------------------------------------------- [G1]/[G2]
print("[G1] growth under L1 (sink smooth; G_eff = G on subhorizon scales, [G3]); same early normalisation, fixed (Om, h) = (0.3153, 0.6736)")
def growth(bg):
    lna = bg['lna']; E = bg['E']; a = bg['a']
    sel = lna > np.log(1e-3)
    x = lna[sel]; Ex = E[sel]; ax = a[sel]
    dlnE = np.gradient(np.log(Ex), x)
    Ef = interpolate.interp1d(x, Ex, kind='cubic'); dEf = interpolate.interp1d(x, dlnE, kind='cubic')
    Om = bg['Om']
    def rhs(xx, y):
        aa = np.exp(xx)
        return [y[1], -(2 + dEf(xx)) * y[1] + 1.5 * Om / (aa**3 * Ef(xx)**2) * y[0]]
    s = integrate.solve_ivp(rhs, (x[0], 0.0), [np.exp(x[0]), np.exp(x[0])], rtol=1e-10, atol=1e-14, dense_output=True)
    return s
s0 = growth(bg0)
for gL in (0.016, 0.047, -0.047):
    bgL = solve_bg(0.3153, 0.6736, gL)
    sL = growth(bgL)
    row = []
    for z in (0.0, 0.3, 0.5, 0.7, 1.0, 1.5):
        x = -np.log(1 + z)
        D0, dD0 = s0.sol(x); DL, dDL = sL.sol(x)
        row.append("z=%g: %+.2e" % (z, dDL / dD0 - 1))      # f sigma8 propto dD/dlna
    x = 0.0
    D0 = s0.sol(x)[0]; DL = sL.sol(x)[0]
    isw0 = 1 - D0 / 1.0; iswL = 1 - DL / 1.0
    print("     g_L = %+.3f: Delta(f sigma8)/(f sigma8): %s ; sigma8(0) ratio-1 = %+.2e ; ISW proxy (1 - D/a at z=0) ratio-1 = %+.2e" %
          (gL, " ".join(row), DL / D0 - 1, iswL / isw0 - 1))
# also at each model's own best fit to BAO+CMB
cA, xA = prof(0.0); cB, xB = prof(0.047, 1.0, xA)
bgA = solve_bg(xA[1] / xA[0]**2, xA[0], 0.0); bgB = solve_bg(xB[1] / xB[0]**2, xB[0], 0.047)
sA = growth(bgA); sB = growth(bgB)
print("     at each model's own BAO+CMB best fit (g_L = 0.047 vs 0): " + " ".join("z=%g: %+.2e" % (z, sB.sol(-np.log(1 + z))[1] / sA.sol(-np.log(1 + z))[1] - 1) for z in (0.3, 0.5, 1.0)))
# [G3]
print("[G3] L0/L1 friction on subhorizon potentials (quasi-static, from (box - gamma u.d) hbar_00): relative (gamma/H)|1-f|(aH/k)^2")
for k in (0.01, 0.05, 0.2):
    aHk = (1.0 / 2997.9) / k          # aH/c at z=0 in h/Mpc over k
    print("     k = %.2f h/Mpc, gamma = 0.047 H0, |1-f| = 0.5: %.1e" % (k, 0.047 * 0.5 * aHk**2))
print("     horizon-scale (k ~ aH) ISW modes: relative O(gamma/H) <= 0.047 (suggested), vs ISW total S/N ~ 4-5 (RECALLED) -> shift <= 0.25 sigma")

# ---------------------------------------------------------------- [M1]
print("[M1] L1-M (global fixed reference, a_ref = a0, C = 1): p_X/rho_crit(z) = (2/3)(gamma/H(z))(1+z)^6")
for z in (1.0, 1089.92, 4e8):
    E = Ez0(z) if z < 1100 else np.sqrt(4.18e-5 / 0.6736**2) * (1 + z)**2
    print("     z = %.3g: p_X/rho_crit = %.2e x (gamma/H0) -> gamma < %.1e H0 for |p_X| < 1e-2 rho_crit" % (z, (2 / 3) * (1 + z)**6 / E, 1e-2 / ((2 / 3) * (1 + z)**6 / E)))
print("    runtime %.1f s" % (time.time() - t0))
