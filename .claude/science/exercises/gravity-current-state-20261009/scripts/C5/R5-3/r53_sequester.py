"""R5-3 toy (library + flat and closed drivers): Kaloper-Padilla sequestering, self-consistent history (checked toy, not a fit).
Flat FRW, 8 pi G = 1 (H^2 = rho/3), dust rho_m = a^-3, scalar with U(phi) = -s phi + C.
Sequestering (KP 2014, verified: Lambda_eff = (1/4)<tau>, <Q> = int a^3 Q dt / int a^3 dt over the whole history)
=> the constant C in U must equal (1/4)<phidot^2 - rho_m> + s <phi>   (constant part of V cancels: sequestered).
(tau = trace of matter+scalar stress, mostly-plus: dust -rho_m, scalar phidot^2 - 4V.)
We solve the fixed point C = F(C) for each slope s, integrate Big Bang -> crunch (cut at a_stop),
locate 'today' on the expanding branch where Omega_m = 0.315, and report H0 t0, w_DE(z), CPL fit, lifetime.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

A = 1.0
a_i = 1e-3

def run(s, C, a_stop=1e-3, dense=False, k=0.0):
    """Big Bang (a_i) -> turnaround -> contraction until a = a_stop * a_max (relative crunch cutoff)."""
    H_i = np.sqrt(A*a_i**-3/3)
    t_i = 2/(3*H_i)
    phid_i = s*t_i/3
    phi_i = s*t_i**2/6   # particular matter-era solution phi = s t^2/6 (phi(0)=0)
    rho_i = A*a_i**-3 + 0.5*phid_i**2 - s*phi_i + C
    y0 = [a_i, np.sqrt(a_i**2*rho_i/3 - k), phi_i, phid_i, 0, 0, 0, 0]
    def rhs(t, y):
        a, ad, ph, phd = y[:4]
        U = -s*ph + C
        rho = A/a**3 + 0.5*phd**2 + U
        p = 0.5*phd**2 - U
        add = -a*(rho + 3*p)/6
        H = ad/a
        phdd = -3*H*phd + s
        a3 = a**3
        return [ad, add, phd, phdd, a3, a3*A/a**3, a3*phd**2, a3*ph]
    def turn(t, y):
        return y[1]
    turn.terminal = True
    turn.direction = -1
    s1 = solve_ivp(rhs, [t_i, 1e5], y0, method='DOP853', rtol=1e-11, atol=1e-14,
                   events=turn, dense_output=dense, max_step=0.5)
    if s1.status != 1:
        return s1, t_i
    amax = s1.y[0, -1]
    def crunch(t, y):
        return y[0] - a_stop*amax
    crunch.terminal = True
    s2 = solve_ivp(rhs, [s1.t[-1], 1e5], s1.y[:, -1], method='DOP853', rtol=1e-11, atol=1e-14,
                   events=crunch, dense_output=dense, max_step=0.5)
    class R: pass
    r = R()
    r.status = s2.status
    r.t = np.concatenate([s1.t, s2.t[1:]])
    r.y = np.concatenate([s1.y, s2.y[:, 1:]], axis=1)
    if dense:
        def solf(tt):
            tt = np.atleast_1d(tt)
            out = np.where(tt <= s1.t[-1], 0, 1)
            res = np.empty((8, len(tt)))
            m = out == 0
            res[:, m] = s1.sol(tt[m]); res[:, ~m] = s2.sol(tt[~m])
            return res
        r.sol = solf
    return r, t_i

def F(s, C, a_stop=1e-3, k=0.0):
    sol, t_i = run(s, C, a_stop, k=k)
    if sol.status != 1:
        return np.nan, sol
    IV, Im, Ik, Iphi = sol.y[4:, -1]
    return 0.25*(Ik - Im)/IV + s*Iphi/IV, sol

def analyse(s, C, a_stop=1e-3, k=0.0):
    sol, t_i = run(s, C, a_stop, dense=True, k=k)
    t = np.linspace(sol.t[0], sol.t[-1], 400001)
    a, ad, ph, phd = sol.sol(t)[:4]
    H = ad/a
    U = -s*ph + C
    rho_m = A/a**3
    rho_de = 0.5*phd**2 + U
    p_de = 0.5*phd**2 - U
    Om = rho_m/(3*H**2)
    # constraint check
    con = np.max(np.abs(3*H**2 + 3*k/a**2 - (rho_m + rho_de))/(rho_m + rho_de))
    exp = H > 0
    idx = np.where(exp & (Om <= 0.315))[0]
    if len(idx) == 0:
        return None
    k = idx[0]
    a0, H0, t0 = a[k], H[k], t[k]
    z = a0/a - 1
    w = p_de/rho_de
    # CPL least squares over 0<z<2 on the expanding branch, rho_de>0
    m = exp & (z >= 0) & (z <= 2) & (rho_de > 0) & (t <= t0)
    X = np.vstack([np.ones(m.sum()), 1 - a[m]/a0]).T
    w0, wa = np.linalg.lstsq(X, w[m], rcond=None)[0]
    kmax = np.argmax(a)
    q0 = -(1 + (np.gradient(H, t)[k])/H0**2)
    return dict(H0t0=H0*(t0 - 0) , w_today=w[k], w0=w0, wa=wa, q0=q0,
                t_total_H0=H0*(t[-1]), t_turn_H0=H0*t[kmax], amax_over_a0=a[kmax]/a0,
                Ude_today=U[k]/(3*H0**2), KE_today=0.5*phd[k]**2/(3*H0**2), con=con,
                C_over_rhoc=C/(3*H0**2), w_z05=np.interp(0.5, z[m][::-1], w[m][::-1]),
                w_z1=np.interp(1.0, z[m][::-1], w[m][::-1]), Omk0=-k/(a0**2*H0**2))


def fixed_points(s, k, Cs):
    g = lambda C: F(s, C, k=k)[0] - C
    vals = []
    for C in Cs:
        try:
            vals.append(g(C))
        except Exception:
            vals.append(np.nan)
    vals = np.array(vals)
    roots = []
    for j in range(len(Cs) - 1):
        if np.isfinite(vals[j]) and np.isfinite(vals[j+1]) and vals[j]*vals[j+1] < 0:
            roots.append(brentq(g, Cs[j], Cs[j+1], xtol=1e-10))
    return roots, vals

print("== identity check: F(C) - C = (1/4)<tau_total> = -(1/4)<R>; flat FRW: int a^3 R dt = 6[a^3 H] - 6 int a adot^2 dt < 0")
for s, C in [(1.0, 2.0), (2.0, 10.0)]:
    sol, _ = run(s, C)
    a, ad = sol.y[0], sol.y[1]
    IV = sol.y[4, -1]
    v, _ = F(s, C)
    # direct: int a^3 R dt with R = 6(addot/a + H^2) computed through the identity
    t = sol.t
    integrand = a*ad**2
    I2 = np.trapezoid(integrand, t)
    bnd = a[-1]**2*ad[-1] - a[0]**2*ad[0]
    R_avg_identity = (6*bnd - 6*I2)/IV
    print(f"  s={s}, C={C}: F-C = {v-C:.5f} ; -(1/4)<R> from identity = {-0.25*R_avg_identity:.5f} (trapezoid on solver nodes)")

print("\n== flat (k=0): fixed points of C = (1/4)<phidot^2 - rho_m> + s<phi>  (equivalently <R> = 0)")
Cs = np.linspace(-5, 60, 66)
for s in [0.5, 1.0, 2.0, 4.0]:
    roots, vals = fixed_points(s, 0.0, Cs)
    print(f"  s={s}: roots={roots} ; min over grid of F-C = {np.nanmin(vals):.4f} (positive => none)")

print("\n== closed (k>0): self-consistent histories; Omega_k0 = -k/(a0 H0)^2 at the epoch Omega_m = 0.315")
print("  s | k | C* | H0 t0 | q0 | w(0) | w(0.5) | w(1) | CPL w0, wa | Omega_k0 | t_total H0 | a_max/a0")
for s in [1.0, 2.0, 4.0]:
    for k in [0.05, 0.2, 0.5, 1.0, 2.0]:
        try:
            roots, vals = fixed_points(s, k, np.linspace(-5, 60, 66))
        except Exception as e:
            print(f"  s={s}, k={k}: error {e}"); continue
        if not roots:
            print(f"  s={s}, k={k}: no fixed point (F-C range {np.nanmin(vals):.3g}..{np.nanmax(vals):.3g})")
            continue
        for Cst in roots:
            r = analyse(s, Cst, k=k)
            if r is None:
                print(f"  s={s}, k={k}, C*={Cst:.4f}: Omega_m never 0.315 while expanding"); continue
            print(f"  {s} | {k} | {Cst:.4f} | {r['H0t0']:.3f} | {r['q0']:+.3f} | {r['w_today']:+.3f} | {r['w_z05']:+.3f} | {r['w_z1']:+.3f} |"
                  f" {r['w0']:+.3f}, {r['wa']:+.3f} | {r['Omk0']:+.4f} | {r['t_total_H0']:.3f} | {r['amax_over_a0']:.3f}  (con {r['con']:.1e})")
