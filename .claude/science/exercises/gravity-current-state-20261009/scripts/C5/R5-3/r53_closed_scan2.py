"""R5-3: closed-FRW sequestering toy, accurate version. Integrals int a dt and int a adot^2 dt are
carried as ODE components (no grid quadrature). For each self-consistent history (C* with <R>=0):
(i) identity k int a dt = int a adot^2 dt - [a^3 H] (exact consequence of <R>=0),
(ii) the expanding-branch epoch where Omega_m is smallest, sampled on the solver's dense output on a
geometric time grid, with Omega_k = -k/(aH)^2 and q there; does Omega_m <= 0.315 with q<0 ever occur?"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
A, a_i = 1.0, 1e-3

def run(s, C, k, a_stop=1e-3):
    H_i = np.sqrt(A*a_i**-3/3); t_i = 2/(3*H_i)
    phid_i = s*t_i/3; phi_i = s*t_i**2/6
    rho_i = A*a_i**-3 + 0.5*phid_i**2 - s*phi_i + C
    y0 = [a_i, np.sqrt(a_i**2*rho_i/3 - k), phi_i, phid_i, 0, 0, 0, 0, 0, 0]
    def rhs(t, y):
        a, ad, ph, phd = y[:4]
        U = -s*ph + C
        rho = A/a**3 + 0.5*phd**2 + U; p = 0.5*phd**2 - U
        a3 = a**3
        return [ad, -a*(rho + 3*p)/6, phd, -3*(ad/a)*phd + s, a3, A, a3*phd**2, a3*ph, a, a*ad**2]
    def turn(t, y): return y[1]
    turn.terminal = True; turn.direction = -1
    s1 = solve_ivp(rhs, [t_i, 1e5], y0, method='DOP853', rtol=1e-11, atol=1e-14, events=turn, dense_output=True, max_step=0.5)
    if s1.status != 1: return None
    amax = s1.y[0, -1]
    def crunch(t, y): return y[0] - a_stop*amax
    crunch.terminal = True
    s2 = solve_ivp(rhs, [s1.t[-1], 1e5], s1.y[:, -1], method='DOP853', rtol=1e-11, atol=1e-14, events=crunch, max_step=0.5)
    if s2.status != 1: return None
    return s1, s2, t_i

def F(s, C, k):
    r = run(s, C, k)
    if r is None: return np.nan
    s1, s2, _ = r
    IV, Im, Ik, Iphi = s2.y[4:8, -1]
    return 0.25*(Ik - Im)/IV + s*Iphi/IV

print("s | k | C* | identity k*int(a) vs int(a adot^2)-[a^3H] | min Omega_m on expansion | Omega_k there | q there | ever (Omega_m<=0.315 & q<0)?")
for s in [0.5, 1.0, 2.0, 4.0]:
    for k in [0.8, 1.0, 1.5, 2.0]:
        Cs = np.linspace(-5, 60, 66)
        v = np.array([F(s, C, k) - C for C in Cs])
        roots = [brentq(lambda C: F(s, C, k) - C, Cs[j], Cs[j+1], xtol=1e-10)
                 for j in range(len(Cs)-1) if np.isfinite(v[j]) and np.isfinite(v[j+1]) and v[j]*v[j+1] < 0]
        if not roots:
            print(f"{s} | {k} | none (F-C in {np.nanmin(v):.3g}..{np.nanmax(v):.3g})"); continue
        for Cst in roots:
            s1, s2, t_i = run(s, Cst, k)
            a_e, ad_e = s2.y[0, -1], s2.y[1, -1]
            Ia, Iad = s2.y[8, -1], s2.y[9, -1]
            bnd = a_e**2*ad_e - s1.y[0, 0]**2*s1.y[1, 0]
            tt = np.geomspace(2*t_i, s1.t[-1]*0.999, 20000)
            a, ad, ph, phd = s1.sol(tt)[:4]
            H = ad/a
            U = -s*ph + Cst
            rho_m = A/a**3
            rho = rho_m + 0.5*phd**2 + U; p = 0.5*phd**2 - U
            add = -a*(rho + 3*p)/6
            q = -add*a/ad**2
            Om = rho_m/(3*H**2); Omk = -k/(a*H)**2
            j = np.argmin(Om)
            ok = np.any((Om <= 0.315) & (q < 0))
            print(f"{s} | {k} | {Cst:.4f} | {k*Ia:.5f} vs {Iad - bnd:.5f} | {Om[j]:.4f} | {Omk[j]:+.4f} | {q[j]:+.3f} | {ok}")
