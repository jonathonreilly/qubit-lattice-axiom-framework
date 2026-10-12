"""R16-6: inflation + reheating with the reader setting the expansion (R14-5 zero-mode law 3H^2 = kappa R, kappa = 1).
Inflaton phi, V(phi) = V_min + m^2 phi^2/2 (m = 1), decay Gamma*phidot^2 into radiation rho_r.  Cosmic time t, u = ln a.
  phidot = pi ; pidot = -(3H + Gamma) pi - m^2 phi ; rho_r dot = -4 H rho_r + Gamma pi^2 ; udot = H = sqrt(R/3).
Readers:
  G0  : state reader, R = pi^2/2 + m^2 phi^2/2 + rho_r (energy above the late vacuum V_min).            class (ii)
  IE  : R(t0) = G0(t0) once, then dR/du = -3h, h = pi^2 + (4/3) rho_r (integrator; only h after the start).
  LIN : two-register linear reader of E = 3h exact on dust and radiation, G(0)=0, G(3)=G(4)=1,
        beta = (5, 10), k = (-1/3, 7/2); registers start at the constant-E steady state (R15-4/R15-6 class).
V_min enters no reader that uses only h.  Output: e-folds of acceleration (R' > -2R in u), N total,
Lam_late = (R - rho_nc)/rho_nc (rho_nc = energy above V_min), g/H^2 = (-3h - dR/du)/R.
"""
import numpy as np
from scipy.integrate import solve_ivp
m, Gam = 1.0, 0.05
beta = np.array([5.0, 10.0]); kk = np.array([-1/3, 3.5])
Gx = lambda x: x*np.sum(kk/(beta - x))
print("LIN transfer: G(0)=%.3g G(3)=%.6f G(4)=%.6f G(0.01)=%.4f" % (Gx(0), Gx(3), Gx(4), Gx(0.01)))
def run(reader, phi0=16.0, t1=400.0):
    pi0 = -np.sqrt(2/3)*m
    rho0 = 0.5*pi0**2 + 0.5*m**2*phi0**2
    h0 = pi0**2
    y0 = [phi0, pi0, 0.0, 0.0]                  # phi, pi, rho_r, u
    if reader == 'IE': y0 += [rho0]
    if reader == 'LIN': y0 += list(3*h0/beta)
    def Rof(y):
        if reader == 'G0': return 0.5*y[1]**2 + 0.5*m**2*y[0]**2 + y[2]
        if reader == 'IE': return y[4]
        return kk[0]*y[4] + kk[1]*y[5]
    def rhs(t, y):
        R = Rof(y)
        if R <= 0: return [0.0]*len(y)
        H = np.sqrt(R/3)
        phi, pi, rr = y[0], y[1], y[2]
        h = pi**2 + 4/3*rr
        out = [pi, -(3*H + Gam)*pi - m**2*phi, -4*H*rr + Gam*pi**2, H]
        if reader == 'IE': out.append(-3*H*h)
        if reader == 'LIN': out += list(H*(3*h - beta*np.array(y[4:6])))
        return out
    ev = lambda t, y: Rof(y); ev.terminal = True; ev.direction = -1
    ts = np.linspace(0, t1, 400001)
    s = solve_ivp(rhs, (0, t1), y0, t_eval=ts, rtol=1e-11, atol=1e-14, method='DOP853', events=ev, max_step=0.02)
    Y = s.y; t = s.t
    phi, pi, rr, u = Y[0], Y[1], Y[2], Y[3]
    rho_nc = 0.5*pi**2 + 0.5*m**2*phi**2 + rr
    h = pi**2 + 4/3*rr
    R = np.array([Rof(Y[:, i]) for i in range(Y.shape[1])])
    H = np.sqrt(np.clip(R, 1e-300, None)/3)
    dRdt = np.gradient(R, t)
    dRdu = dRdt/H
    if reader == 'IE': dRdu = -3*h
    gH2 = (-3*h - dRdu)/R
    acc = (dRdu > -2*R)
    du = np.gradient(u)
    nacc = np.sum(du[acc])
    Lam = (R - rho_nc)/rho_nc
    D = (R - rho_nc)/rho0
    print("%-4s phi0=%.0f t_end=%.1f %s| N_total=%.2f N_accel=%.2f | rho_r/rho_nc end=%.3f | Lam_late end=%+.2e | (R-rho_nc)/rho0 end=%+.1e | g/H^2 in [%+.2e, %+.2e] | min R/rho_nc=%.3g"
          % (reader, phi0, t[-1], "(R<=0) " if s.status == 1 else "", u[-1], nacc, rr[-1]/rho_nc[-1], Lam[-1], D[-1],
             gH2[10:-10].min(), gH2[10:-10].max(), (R/rho_nc).min()))
for rd in ['G0', 'IE', 'LIN']:
    run(rd)
run('LIN', phi0=12.0); run('IE', phi0=12.0)
print("Identifiability on the quadratic attractor (G0 background): h after 2 time units vs phi0")
for p0 in [12.0, 16.0, 20.0]:
    def rhs(t, y):
        R = 0.5*y[1]**2 + 0.5*m**2*y[0]**2; H = np.sqrt(R/3)
        return [y[1], -3*H*y[1] - m**2*y[0]]
    s = solve_ivp(rhs, (0, 2), [p0, -np.sqrt(2/3)*m], rtol=1e-12, atol=1e-14)
    ph, pp = s.y[:, -1]
    print("  phi0=%.0f: h = pi^2 = %.6f  (2m^2/3 = %.6f), rho above V_min = %.3f" % (p0, pp**2, 2/3, 0.5*pp**2 + 0.5*ph**2))
