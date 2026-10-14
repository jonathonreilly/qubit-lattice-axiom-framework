"""F2 case (i): GWs crossing the Earth, and the detector sitting on the ground.

Model (stated hypothesis, TESTS F2 setting): each TT polarisation obeys  h'' - lap h + m^2(x) h = 0,  m^2(x) = sigma*mu_rho*rho(x),
sigma = +1 (branch M, massive) or -1 (branch T, tachyonic). Along a straight ray / vertical line this is the 1D problem
psi'' + (k0^2 - k_perp^2 - m^2(z)) psi = 0 (k0 = omega/c).  Solved exactly for piecewise-constant layers by a backward
log-derivative (Riccati) recursion (stable for evanescent layers).  psi and psi' continuous (m^2 enters as a potential).

Parts:
 (A) GW170817 geometry: altitude of NGC 4993 at H1, L1, V1 at 2017-08-17 12:41:04.4 UTC; chord length; deepest radius.
     Also GW170814 (RA 03h11m, Dec -44d57m, 2017-08-14 10:30:43 UTC) at H1.
 (B) Through-Earth transmission t(f) on the GW170817 H1/L1 chords (PREM), both branches; SNR-weighted transmission
     with an aLIGO-like PSD; WKB phase integral; bound mu_rho_max from (S >= 0.7) and (int |m^2| ds <= m_LVK170817^2 D).
 (C) Placeholder (R19-34 H-cov) on those chords: WKB attenuation exponent (branch M); exact |t| (branch T).
 (D) Detector on the ground: vertical model (atmosphere + crust), field at 1 m above ground / vacuum incident, both branches.
 (E) Tachyonic instability of the PREM Earth: critical mu_rho for the first growing mode (l = 0, 2); growth time at placeholder.
"""
import numpy as np
from f2_common import (hbarc, hbar, c_light, R_E, prem_rho, MU_RHO_PLACEHOLDER, Mpc)

DEG = np.pi / 180


# ---------------- (A) geometry ----------------
def gmst_deg(jd):
    d = jd - 2451545.0
    T = d / 36525.0
    g = 280.46061837 + 360.98564736629 * d + 0.000387933 * T**2 - T**3 / 38710000.0
    return g % 360.0


def jd_utc(y, mo, d, h, mi, s):
    if mo <= 2:
        y -= 1; mo += 12
    A = y // 100; B = 2 - A + A // 4
    return int(365.25 * (y + 4716)) + int(30.6001 * (mo + 1)) + d + B - 1524.5 + (h + mi / 60 + s / 3600) / 24


def altitude(ra_deg, dec_deg, lat_deg, lon_deg, jd):
    lst = (gmst_deg(jd) + lon_deg) % 360
    ha = (lst - ra_deg) * DEG
    sa = np.sin(lat_deg * DEG) * np.sin(dec_deg * DEG) + np.cos(lat_deg * DEG) * np.cos(dec_deg * DEG) * np.cos(ha)
    return np.arcsin(sa) / DEG


SITES = {'H1': (46.4551, -119.4077), 'L1': (30.5629, -90.7742), 'V1': (43.6314, 10.5045)}


# ---------------- 1D layered solver ----------------
def layers_from_profile(zs, m2):
    """zs: layer boundaries (increasing, len n+1); m2: m^2 [1/m^2] per layer (len n)."""
    return np.diff(zs), m2


def transmit(d, m2, k0, kperp2=0.0):
    """Wave incident from vacuum at the start of the layer stack, exits into vacuum at the end.
    d, m2: layer thicknesses [m] and m^2 [1/m^2] (arrays, propagation order); k0: array of vacuum wavenumbers.
    Returns complex t (relative to vacuum propagation over the same length) and r."""
    k0 = np.atleast_1d(k0).astype(complex)
    kz0 = np.sqrt(k0**2 - kperp2)
    Y = 1j * kz0                       # outgoing at the exit
    lnpsi = np.zeros_like(Y)           # ln psi(z_end) - ln psi(z) accumulated
    for dj, m2j in zip(d[::-1], m2[::-1]):
        k = np.sqrt(k0**2 - kperp2 - m2j + 0j)
        k = np.where(k.imag < 0, -k, k)
        kd = k * dj
        cs, sn = np.cos(kd), np.where(np.abs(k) > 0, np.sin(kd) / np.where(np.abs(k) > 0, k, 1), dj)
        psi_a = cs - Y * sn
        dpsi_a = k * k * sn + Y * cs
        Y = dpsi_a / psi_a
        lnpsi = lnpsi - np.log(psi_a)  # ln psi(z_a) = ln psi(z_b) + ln psi_a with psi(z_b) normalised to 1 -> accumulate
    # lnpsi now = ln psi(z_start) - ln psi(z_end)  (sum of ln psi_a);  careful sign: we accumulated -ln psi_a
    psi0 = 2j * kz0 / (1j * kz0 + Y)   # psi(0) for unit incident amplitude
    r = psi0 - 1
    # psi(z_end) = psi(0) * exp(-(sum ln psi_a)) ... we stored lnpsi = -sum ln psi_a = ln psi(z_end) - ln psi(z_start)
    L = d.sum()
    t = psi0 * np.exp(lnpsi) * np.exp(-1j * kz0 * L)
    return t, r


def split_layers(z_edges, rho_mid, mu_rho, sigma, k0max, kfrac=0.3, dmax=5e3):
    """refine layers so |k| d <= kfrac for the largest |k| and d <= dmax."""
    d_out, m2_out = [], []
    for j in range(len(rho_mid)):
        dz = z_edges[j + 1] - z_edges[j]
        m2 = sigma * mu_rho * rho_mid[j] / hbarc**2
        kmax = np.sqrt(k0max**2 + abs(m2)) + 1e-30
        n = max(1, int(np.ceil(max(dz * kmax / kfrac, dz / dmax))))
        d_out += [dz / n] * n
        m2_out += [m2] * n
    return np.array(d_out), np.array(m2_out)


def chord_profile(alt_deg, nseg=4000):
    """density along the chord from the far-side entry (s=0) to the detector (s=L)."""
    L = -2 * R_E * np.sin(alt_deg * DEG)
    s = np.linspace(0, L, nseg + 1)
    sm = 0.5 * (s[1:] + s[:-1])
    # distance from detector = L - sm
    q = L - sm
    r = np.sqrt(R_E**2 + q**2 + 2 * R_E * q * np.sin(alt_deg * DEG))
    return s, prem_rho(r), L, R_E * np.cos(alt_deg * DEG)


def psd_aligo(f):
    x = f / 215.0
    return 1e-49 * (x**-4.14 - 5 * x**-2 + 111 * (1 - x**2 + x**4 / 2) / (1 + x**2 / 2))


def snr_weighted_T(fs, t):
    w = fs**(-7 / 3) / psd_aligo(fs)
    return np.sqrt(np.trapezoid(np.abs(t)**2 * w, fs) / np.trapezoid(w, fs))


if __name__ == '__main__':
    print('=== (A) geometry ===')
    jd817 = jd_utc(2017, 8, 17, 12, 41, 4.4)
    ra, dec = 197.4488, -23.3839   # NGC 4993 (RA 13h09m47.7s, Dec -23d23m02s; RECALLED)
    alts = {}
    for k, (la, lo) in SITES.items():
        a = altitude(ra, dec, la, lo, jd817)
        alts[k] = a
        if a < 0:
            print('  GW170817 at %s: altitude %+.1f deg -> chord %.0f km, closest approach to centre r = %.0f km' % (
                k, a, -2 * R_E * np.sin(a * DEG) / 1e3, R_E * np.cos(a * DEG) / 1e3))
        else:
            print('  GW170817 at %s: altitude %+.1f deg (above horizon)' % (k, a))
    jd814 = jd_utc(2017, 8, 14, 10, 30, 43)
    for dd in (-44.95, -40.0, -49.0):
        print('  GW170814 (RA 03h11m, Dec %.2f) at H1: altitude %+.1f deg (max altitude at H1 = %+.1f deg)' % (
            dd, altitude(47.75, dd, *SITES['H1'], jd814), 90 - 46.4551 + dd))

    print('\n=== (B) through-Earth transmission on the GW170817 chords: bound on mu_rho ===')
    fs = np.geomspace(30, 1000, 120)
    k0 = 2 * np.pi * fs / c_light
    mLVK, D817 = 9.51e-22, 40.0 * Mpc   # LVK GW170817 TGR (arXiv:1811.00364) dispersion bound, D ~ 40 Mpc
    phase_budget = mLVK**2 * D817          # eV^2 m  allowed  int |m^2| ds
    print('  GW170817 dispersion budget int|m^2|ds <= %.3e eV^2 m' % phase_budget)
    res = {}
    for det in ('H1', 'L1'):
        s, rho, L, rmin = chord_profile(alts[det])
        colrho = np.sum(np.diff(s) * rho)
        rhomax = rho.max()
        print('  %s: L = %.0f km, column = %.3e kg/m^2, rho_max on chord = %.0f kg/m3' % (det, L / 1e3, colrho, rhomax))
        for sigma, lab in ((+1, 'M'), (-1, 'T')):
            rows = []
            for mu in np.geomspace(1e-31, 1e-24, 29):
                d, m2 = split_layers(s, rho, mu, sigma, k0.max())
                t, r = transmit(d, m2, k0)
                S = snr_weighted_T(fs, t)
                disp = mu * colrho     # int |m^2| ds in eV^2 m
                rows.append((mu, S, np.abs(t[0]), np.abs(t[np.argmin(abs(fs - 100))]), disp))
            ok = [r_ for r_ in rows if r_[1] >= 0.7 and r_[4] <= phase_budget]
            muA = max([r_[0] for r_ in rows if r_[1] >= 0.7], default=np.nan)
            muB = phase_budget / colrho
            mumax = min(muA, muB)
            res[(det, lab)] = (muA, muB, mumax)
            print('   branch %s: largest mu (grid) with S_SNR >= 0.7: %.2e; dispersion-budget mu <= %.2e  =>  mu_rho_max = %.2e eV^2 m^3/kg'
                  % (lab, muA, muB, mumax))
            for mu, S, t30, t100, disp in rows[::2]:
                print('      mu=%.1e  S_SNR=%.3f  |t(30Hz)|=%.3e |t(100Hz)|=%.3e  int|m2|ds=%.2e  |m_g(5500)|=%.2e eV'
                      % (mu, S, t30, t100, disp, np.sqrt(mu * 5500)))
    mu_earth = min(v[2] for v in res.values() if np.isfinite(v[2]))
    mu_earth_M = min(res[('H1', 'M')][2], res[('L1', 'M')][2])
    mu_earth_T = min(res[('H1', 'T')][2], res[('L1', 'T')][2])
    print('  BOUND (i)-chord: mu_rho <= %.2e (M), %.2e (T) eV^2 m^3/kg; |m_g| at 5500 kg/m3 <= %.2e (M), %.2e (T) eV'
          % (mu_earth_M, mu_earth_T, np.sqrt(mu_earth_M * 5500), np.sqrt(mu_earth_T * 5500)))
    print('  placeholder mu_rho = %.3e -> ratio placeholder/bound = %.1e (M), %.1e (T)'
          % (MU_RHO_PLACEHOLDER, MU_RHO_PLACEHOLDER / mu_earth_M, MU_RHO_PLACEHOLDER / mu_earth_T))

    print('\n=== (C) placeholder on the GW170817 chords ===')
    for det in ('H1', 'L1'):
        s, rho, L, rmin = chord_profile(alts[det], nseg=20000)
        ds = np.diff(s)
        for f in (30., 100., 300.):
            kk = 2 * np.pi * f / c_light
            m2 = MU_RHO_PLACEHOLDER * rho / hbarc**2
            kappa = np.sqrt(np.maximum(m2 - kk**2, 0))
            print('  %s f=%5.0f Hz  branch M: WKB attenuation exponent int kappa ds = %.3e  (|t| ~ e^-%.2e)' % (det, f, np.sum(kappa * ds), np.sum(kappa * ds)))
    # branch T exact on the L1 chord, band of frequencies (resonances) -- coarse sampling
    s, rho, L, rmin = chord_profile(alts['L1'], nseg=4000)
    fsT = np.linspace(30, 300, 64)
    d, m2 = split_layers(s, rho, MU_RHO_PLACEHOLDER, -1, 2 * np.pi * 300 / c_light, kfrac=0.5, dmax=1e9)
    print('  branch T, L1 chord: %d layers' % len(d))
    t, r = transmit(d, m2, 2 * np.pi * fsT / c_light)
    print('  branch T, L1 chord: |t| over 30-300 Hz: median %.3e, max %.3e, rms %.3e; SNR-weighted %.3e'
          % (np.median(abs(t)), abs(t).max(), np.sqrt(np.mean(abs(t)**2)), snr_weighted_T(fsT, t)))
    print('     single-interface estimate 4 k0 M/(k0+M)^2 per interface at 100 Hz, rock 2600: %.2e'
          % (4 * (2 * np.pi * 100 / c_light) * np.sqrt(MU_RHO_PLACEHOLDER * 2600) / hbarc / (np.sqrt(MU_RHO_PLACEHOLDER * 2600) / hbarc)**2))
    print('     WKB extra phase int (k - k0) ds at 100 Hz = %.3e rad' % np.sum(np.diff(s) * (np.sqrt((2 * np.pi * 100 / c_light)**2 + MU_RHO_PLACEHOLDER * rho / hbarc**2) - 2 * np.pi * 100 / c_light)))

    print('\n=== (D) detector on the ground (vertical model) ===')
    # z measured upward; incident from z = +ztop (vacuum) downward; ground at z = 0; detector at z = +1 m.
    # Layers from top (z=ztop) down to z = -zbot; bottom half-space: outgoing (T) / decaying (M) via a thick last layer
    def vertical_profile(zdet=1.0, ztop=150e3, zbot=-30e3):
        zA = np.concatenate([np.linspace(ztop, 2e3, 600), np.linspace(2e3, zdet, 200)[1:]])
        zB = np.linspace(zdet, 0.0, 5)[1:]
        zC = np.concatenate([np.linspace(0, -12e3, 1200)[1:], np.linspace(-12e3, zbot, 400)[1:]])
        z = np.concatenate([zA, zB, zC])
        zm = 0.5 * (z[1:] + z[:-1])
        rho = np.where(zm > 0, 1.225 * np.exp(-zm / 8.5e3), np.where(zm > -12e3, 2600.0, 2900.0))
        return z, rho
    z, rho = vertical_profile()
    idx_det = np.argmin(abs(z - 1.0))

    def field_at(z, rho, mu, sigma, f, theta=0.0):
        """|psi| at z[idx_det] relative to unit incident amplitude; propagate (top -> bottom order).
        Bottom: we treat the stack as ending in a half-space with the last layer's m^2 (outgoing / decaying)."""
        k0 = 2 * np.pi * f / c_light
        kp2 = (k0 * np.sin(theta))**2
        d = -np.diff(z)              # thicknesses in propagation order (downward)
        m2 = sigma * mu * rho / hbarc**2
        # refine
        dd, mm = [], []
        for dj, mj in zip(d, m2):
            kk = np.sqrt(abs(k0**2 - kp2 - mj)) + 1e-30
            n = max(1, int(np.ceil(dj * kk / 0.3)))
            dd += [dj / n] * n; mm += [mj] * n
        dd, mm = np.array(dd), np.array(mm)
        # exit half-space = bottom layer medium (not vacuum): start the Riccati with that medium's outgoing/decaying root
        kb = np.sqrt(k0**2 - kp2 - mm[-1] + 0j)
        kb = kb if kb.imag >= 0 else -kb
        Y = 1j * kb
        # record cumulative ln psi from bottom upward
        lnpsi_b = 0.0 + 0j
        cum = np.zeros(len(dd) + 1, dtype=complex)
        for j in range(len(dd) - 1, -1, -1):
            k = np.sqrt(k0**2 - kp2 - mm[j] + 0j)
            k = k if k.imag >= 0 else -k
            kd = k * dd[j]
            cs = np.cos(kd); sn = np.sin(kd) / k if abs(k) > 0 else dd[j]
            psi_a = cs - Y * sn
            Y = (k * k * sn + Y * cs) / psi_a
            lnpsi_b += np.log(psi_a)
            cum[j] = lnpsi_b       # ln psi(top of layer j) - ln psi(bottom)
        kz0 = np.sqrt(k0**2 - kp2)
        psi_top = 2j * kz0 / (1j * kz0 + Y)
        # psi at boundary index i (top of layer i): psi_top * exp(cum[i] - cum[0])
        zb = np.concatenate([[z[0]], z[0] - np.cumsum(dd)])
        i = np.argmin(abs(zb - 1.0))
        return abs(psi_top * np.exp(cum[i] - cum[0])), zb[i]

    for sigma, lab in ((+1, 'M'), (-1, 'T')):
        for mu in (MU_RHO_PLACEHOLDER, 1e-28, 1e-30, 1e-31, 1e-32):
            vals = []
            for f in (30., 100., 300.):
                a0, zz = field_at(z, rho, mu, sigma, f)
                a60, _ = field_at(z, rho, mu, sigma, f, theta=60 * DEG)
                vals.append('%3.0fHz: %.2e (60deg %.2e)' % (f, a0, a60))
            print('  branch %s mu=%.2e (|m_g| rock %.1e eV, air %.1e eV): |h(1 m)|/|h_inc| = %s' % (
                lab, mu, np.sqrt(mu * 2600), np.sqrt(mu * 1.225), '; '.join(vals)))
    print('  (vacuum reference with no ground would be 1; a perfectly transparent ground gives 1; a rigid node gives ~0)')

    print('\n=== (E) tachyonic instability of the PREM Earth ===')
    from scipy.integrate import solve_ivp

    rgrid = np.linspace(0, R_E, 25485)
    rhogrid = prem_rho(rgrid)

    def uR(s, l):
        # u'' = (l(l+1)/r^2 - s*rho(r)) u, regular start u ~ r^(l+1)
        def rhs(r, y):
            return [y[1], (l * (l + 1) / r**2 - s * np.interp(r, rgrid, rhogrid)) * y[0]]
        r0 = 1.0
        sol = solve_ivp(rhs, [r0, R_E], [r0**(l + 1), (l + 1) * r0**l], rtol=1e-9, atol=1e-30, max_step=2e4)
        u, up = sol.y[0, -1], sol.y[1, -1]
        return up / u + l / R_E   # threshold when u'/u = -l/R (matches r^-l exterior)

    for l in (0, 2):
        lo, hi = 1e-20, 1e-12
        flo = uR(lo, l)
        # scan for first sign change
        grid = np.geomspace(lo, hi, 33)
        prev = flo; sprev = lo; found = None
        for sv in grid[1:]:
            fv = uR(sv, l)
            if np.sign(fv) != np.sign(prev):
                found = (sprev, sv); break
            prev, sprev = fv, sv
        a, b = found
        for _ in range(36):
            mid = np.sqrt(a * b)
            if np.sign(uR(mid, l)) == np.sign(uR(a, l)):
                a = mid
            else:
                b = mid
        s_crit = np.sqrt(a * b)                       # 1/m^2 per kg/m^3
        mu_crit = s_crit * hbarc**2                   # eV^2 m^3/kg
        print('  l=%d: critical mu_rho = %.3e eV^2 m^3/kg  (|m_g| at 5500 = %.3e eV; uniform-sphere pi/2 rule: %.3e eV)' % (
            l, mu_crit, np.sqrt(mu_crit * 5500), np.pi / 2 * hbarc / R_E))
    Mc = np.sqrt(MU_RHO_PLACEHOLDER * 13088.0)
    print('  placeholder: centre |m_g| = %.3e eV -> fastest growth rate ~ %.3e /s (e-fold time %.2e s); bound states ~ (M R)^2 ~ %.1e'
          % (Mc, Mc / hbar, hbar / Mc, (Mc * R_E / hbarc)**2))
