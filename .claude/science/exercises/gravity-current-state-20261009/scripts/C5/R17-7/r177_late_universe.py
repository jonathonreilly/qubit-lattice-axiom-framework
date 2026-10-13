"""R17-7 probe (a): the late universe under (S) "the law's lowest state weighs nothing" (C = E0[H]).
Setting: homogeneous GR (R16-6 Theorem Z with g == 0, counted once), kappa = 1, flat, H0 = 1.
Under (S) + P93 (our vacuum = global minimum) the late constant is Lambda_late = kappa (V_ours - E0) = 0, so the
observed acceleration must be content above E0.  The minimal such content is a canonical scalar not yet at its
minimum (thawing; w >= -1 by NEC).  Question checked here: how close can (S)'s minimal content come to the
DESI-DR2-like CPL history that R15-4/R16-6 used ((w0, wa) = (-0.75, -0.86), Om = 0.31; RECALLED), compared with
LCDM (a pure Lambda, which (S)+P93 forbids)?
PROXY, stated before the run: the "data" are the CPL model's own BAO distances at the DESI DR2 effective redshifts
with RECALLED approximate DR2 fractional errors, diagonal, no CMB, no SN; one free amplitude A = c/(H0 r_d).
This is not a DESI likelihood; it measures model distances, not significance.
Subtraction: none; every model is compared to the CPL curve only.
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import brentq, minimize

Or = 9.0e-5
w0, wa, Om_c = -0.75, -0.86, 0.31            # RECALLED DESI-DR2-like CPL (as R16-6, counted once)
# DESI DR2 effective redshifts and approximate fractional errors (RECALLED; approximate; diagonal)
# (z, kind, frac_err): kind V = D_V, M = D_M, H = D_H
DATA = [(0.295, 'V', 0.009),
        (0.510, 'M', 0.012), (0.510, 'H', 0.019),
        (0.706, 'M', 0.010), (0.706, 'H', 0.017),
        (0.934, 'M', 0.007), (0.934, 'H', 0.011),
        (1.321, 'M', 0.012), (1.321, 'H', 0.016),
        (1.484, 'M', 0.025), (1.484, 'H', 0.040),
        (2.330, 'M', 0.014), (2.330, 'H', 0.012)]
zgrid = np.linspace(0, 2.4, 4801)

def E_cpl(z, Om=Om_c, w0=w0, wa=wa):
    a = 1/(1+z); Ode = 1 - Om - Or
    return np.sqrt(Om*a**-3 + Or*a**-4 + Ode*a**(-3*(1+w0+wa))*np.exp(-3*wa*(1-a)))

def E_lcdm(z, Om):
    a = 1/(1+z)
    return np.sqrt(Om*a**-3 + Or*a**-4 + 1 - Om - Or)

def thaw_solution(Om, lam, pot='exp'):
    """Canonical scalar, frozen at a = 1e-3 (thawing), GR.  V = V0 exp(-lam phi) ('exp')
    or V = V0 (1 + cos(phi/f)) with f = 1/lam started at phi_i = 0.5 f? -> 'pngb' uses phi_i = 0.3 rad from the top.
    Units: 3 H0^2 = 3, rho_m0 = 3 Om.  Shoot V0 so that H(N=0) = 1.  Returns z grid, E(z), w(z)."""
    rm0, rr0 = 3*Om, 3*Or
    if pot == 'exp':
        Vf = lambda p, V0: V0*np.exp(-lam*p); dVf = lambda p, V0: -lam*V0*np.exp(-lam*p); phi_i = 0.0
    else:
        f = 1/lam
        Vf = lambda p, V0: V0*(1 + np.cos(p/f)); dVf = lambda p, V0: -V0/f*np.sin(p/f); phi_i = 0.3*f
    def run(V0, dense=False):
        def rhs(N, y):
            p, v = y
            rm, rr = rm0*np.exp(-3*N), rr0*np.exp(-4*N)
            H2 = (rm + rr + Vf(p, V0))/(3 - v**2/2)
            dlnH = -0.5*(rm + 4*rr/3)/H2 - v**2/2
            return [v, -(3 + dlnH)*v - dVf(p, V0)/H2]
        Ns = np.linspace(np.log(1e-3), 0, 3001)
        s = solve_ivp(rhs, (Ns[0], 0), [phi_i, 0.0], t_eval=Ns, rtol=1e-10, atol=1e-12, method='DOP853')
        p, v = s.y
        rm, rr = rm0*np.exp(-3*Ns), rr0*np.exp(-4*Ns)
        H2 = (rm + rr + Vf(p, V0))/(3 - v**2/2)
        if not dense:
            return H2[-1] - 1.0
        kin = H2*v**2/2; Vv = Vf(p, V0)
        return Ns, np.sqrt(H2), (kin - Vv)/(kin + Vv)
    V0 = brentq(run, 0.1, 50.0, xtol=1e-12)
    Ns, H, w = run(V0, dense=True)
    z = np.exp(-Ns) - 1
    return z[::-1], H[::-1], w[::-1]

def distances(Efun_on_grid):
    E = Efun_on_grid
    DM = np.concatenate([[0], cumulative_trapezoid(1/E, zgrid)])
    return DM, 1/E

def model_vector(E):
    DM, DH = distances(E)
    out = []
    for z, k, _ in DATA:
        i = np.searchsorted(zgrid, z)
        dm, dh = np.interp(z, zgrid, DM), np.interp(z, zgrid, DH)
        out.append({'M': dm, 'H': dh, 'V': (z*dm**2*dh)**(1/3)}[k])
    return np.log(np.array(out))

sig = np.array([d[2] for d in DATA])
target = model_vector(E_cpl(zgrid))

def chi2_of(E):
    r = model_vector(E) - target
    A = np.sum(r/sig**2)/np.sum(1/sig**2)        # free log-amplitude (c/(H0 r_d))
    return np.sum(((r - A)/sig)**2)

# LCDM
resL = minimize(lambda q: chi2_of(E_lcdm(zgrid, q[0])), [0.30], method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-8})
print("a1. CPL truth (w0, wa, Om) = (%.2f, %.2f, %.2f); w crosses -1 at z = %.3f" % (w0, wa, Om_c, wa/(1+w0+wa) - 1))
print("    LCDM (pure Lambda; forbidden under (S)+P93): best Om = %.4f, chi2_proxy = %.3f" % (resL.x[0], resL.fun))

def thaw_E_on_grid(Om, lam, pot):
    z, H, w = thaw_solution(Om, lam, pot)
    return np.interp(zgrid, z, H), z, w

best = {}
for pot in ['exp', 'pngb']:
    def f(q):
        Om, lam = q
        if not (0.2 < Om < 0.45 and 0.0 < lam < 4.0):
            return 1e9
        try:
            E, _, _ = thaw_E_on_grid(Om, lam, pot)
        except Exception:
            return 1e9
        return chi2_of(E)
    starts = [(0.31, 0.8), (0.32, 1.2), (0.30, 1.6)] if pot == 'exp' else [(0.31, 0.6), (0.32, 1.0), (0.30, 1.4)]
    rs = [minimize(f, s0, method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-7, 'maxiter': 400}) for s0 in starts]
    r = min(rs, key=lambda t: t.fun)
    E, z, w = thaw_E_on_grid(r.x[0], r.x[1], pot)
    w_today = w[0]
    # CPL-equivalent (w0, wa) from w(a) near today: fit w = w0 + wa (1 - a) on 0 < z < 1
    sel = z < 1.0
    a = 1/(1+z[sel]); A = np.vstack([np.ones_like(a), 1 - a]).T
    w0f, waf = np.linalg.lstsq(A, w[sel], rcond=None)[0]
    best[pot] = (r, E)
    print("    thawing canonical scalar (%s): best Om = %.4f, lam = %.3f, chi2_proxy = %.3f; w(z=0) = %.3f, min w = %.4f (>= -1), "
          "CPL-equivalent (w0, wa) on z<1 = (%.3f, %.3f)" % (pot, r.x[0], r.x[1], r.fun, w_today, w.min(), w0f, waf))

# max fractional deviations of H(z) and D_M(z) from CPL after the free amplitude, 0.1 < z < 2.33
Ec = E_cpl(zgrid); DMc, _ = distances(Ec)
sel = (zgrid > 0.1) & (zgrid < 2.33)
def devs(E):
    DM, _ = distances(E)
    rH = np.log(Ec/E); rM = np.log(DM[1:]/DMc[1:])
    return np.abs(rH[sel]).max(), np.abs(rM[sel[1:]]).max()
print("a2. max |ln(model/CPL)| for 0.1<z<2.33 (H, D_M), no amplitude freedom (H0 fixed common):")
print("    LCDM best-fit Om: H %.4f, D_M %.4f" % devs(E_lcdm(zgrid, resL.x[0])))
for pot in best:
    print("    thawing %-4s     : H %.4f, D_M %.4f" % ((pot,) + devs(best[pot][1])))
print("a3. Fraction of the LCDM-vs-CPL chi2_proxy gap recovered by (S)'s minimal content: exp %.2f, pngb %.2f"
      % tuple(1 - best[p][0].fun/resL.fun for p in ['exp', 'pngb']))
print("    (proxy only: diagonal RECALLED DR2-like errors, BAO-only, no CMB/SN; DESI's 2.8-4.2 sigma preference (RECALLED)"
      " comes mostly from BAO+CMB+SN combinations, which this does not model)")
