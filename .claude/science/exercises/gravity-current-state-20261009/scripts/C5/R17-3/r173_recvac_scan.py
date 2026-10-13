"""R17-3 check of the dilemma's first horn: REC-vac (plateau unrecorded, R = pi^2/2 + rho_r) for larger phi0.
Analytic expectation (suggested): on the friction-balanced track phidot^2 ~ (sqrt6/3) m^2 phi, H^2 = phidot^2/6, so
dN = H dt = dphi/sqrt6 and N ~ phi0/sqrt6; the expansion is quasi-de Sitter for large phi only because energy is
pumped from the unrecorded potential into recorded kinetic energy, i.e. g = (1/3)(rho_unrec)' != 0 throughout.
Subtraction: V_late = 0 only.
"""
import numpy as np
from scipy.integrate import solve_ivp
m, Gam = 1.0, 0.05
def run(phi0):
    pi0 = -np.sqrt(2/3)*m
    def rhs(t, y):
        phi, pi, rr, u = y
        R = 0.5*pi**2 + rr
        H = np.sqrt(max(R, 1e-300)/3)
        return [pi, -(3*H + Gam)*pi - m**2*phi, -4*H*rr + Gam*pi**2, H]
    t1 = 40 + 2.0*phi0
    ts = np.linspace(0, t1, 200001)
    s = solve_ivp(rhs, (0, t1), [phi0, pi0, 0.0, 0.0], t_eval=ts, rtol=1e-10, atol=1e-13, method='DOP853', max_step=0.02)
    phi, pi, rr, u = s.y; t = s.t
    R = 0.5*pi**2 + rr
    H = np.sqrt(R/3)
    dRdu = np.gradient(R, t)/H
    acc = dRdu > -2*R
    nacc = np.sum(np.gradient(u)[acc])
    V = 0.5*m**2*phi**2
    gH2 = np.gradient(V, t)/(3*H)/H**2     # g = (1/3) d(rho_unrec)/du, rho_unrec = V (unrecorded plateau)
    mid = slice(len(t)//10, len(t)//3)
    print("REC-vac phi0=%5.0f: N_total=%6.2f N_accel=%6.2f (phi0/sqrt6 = %5.2f) | g/H^2 median in early-mid run = %+.3e, range [%+.2e, %+.2e]"
          % (phi0, u[-1], nacc, phi0/np.sqrt(6), np.median(gH2[mid]), gH2[10:-10].min(), gH2[10:-10].max()))
for p0 in [16, 50, 100, 150]:
    run(float(p0))
print("Reading: an unrecorded plateau can drive many accelerating e-folds for large phi0, but only through g != 0 at every")
print("instant (energy leaking from the unrecorded plateau into recorded kinetic energy): R15-1 signalling, excluded by H-g0.")
