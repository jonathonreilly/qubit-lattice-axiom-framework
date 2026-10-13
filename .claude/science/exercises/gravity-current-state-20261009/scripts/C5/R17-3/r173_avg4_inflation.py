"""R17-3 probe (b), B4: a causal global constraint that is time-dependent: the running 4-volume average of the w ~ -1 part,
C(t) = int_0^t a^3 V dt' / int_0^t a^3 dt' (+ C(0) = V(0) start), applied in R16-6's inflation history with
R = rho_tot - C(t) (V_late = 0; the inflaton plateau counted as 'vacuum', i.e. the reader that does NOT know which
w ~ -1 stress is the late one).  Same m^2 phi^2 + reheating model as r173_records_inflation.py.
Output: accelerating e-folds, g/H^2 = C'/(3H^2) (nonzero => R15-1 signalling), late Lambda_late = C - V_late.
Subtraction named before the run: C(t) only.
"""
import numpy as np
from scipy.integrate import solve_ivp
m, Gam = 1.0, 0.05
def run(phi0=16.0, t1=400.0):
    pi0 = -np.sqrt(2/3)*m
    V0 = 0.5*m**2*phi0**2
    # state: phi, pi, rho_r, u, W = int a^3 dt, X = int a^3 V dt ; start with W = eps, X = eps*V0
    eps = 1e-3
    y0 = [phi0, pi0, 0.0, 0.0, eps, eps*V0]
    def C(y): return y[5]/y[4]
    def Rof(y): return 0.5*y[1]**2 + 0.5*m**2*y[0]**2 + y[2] - C(y)
    def rhs(t, y):
        R = Rof(y)
        if R <= 0: return [0.0]*6
        H = np.sqrt(R/3)
        a3 = np.exp(3*y[3]); V = 0.5*m**2*y[0]**2
        return [y[1], -(3*H + Gam)*y[1] - m**2*y[0], -4*H*y[2] + Gam*y[1]**2, H, a3, a3*V]
    ev = lambda t, y: Rof(y) - 1e-12; ev.terminal = True; ev.direction = -1
    ts = np.linspace(0, t1, 100001)
    s = solve_ivp(rhs, (0, t1), y0, t_eval=ts, rtol=1e-10, atol=1e-13, method='DOP853', max_step=0.02, events=ev)
    Y, t = s.y, s.t
    R = np.array([Rof(Y[:, i]) for i in range(Y.shape[1])])
    Cs = Y[5]/Y[4]
    H = np.sqrt(np.clip(R, 1e-300, None)/3)
    dRdu = np.gradient(R, t)/H
    acc = dRdu > -2*R
    u = Y[3]
    nacc = np.sum(np.gradient(u)[acc])
    gH2 = np.gradient(Cs, t)/(3*H)/H**2   # g = (1/3) dC/du
    print("AVG4 phi0=%.0f: t_end=%.1f%s | N_total=%.2f N_accel=%.2f | g/H^2 in [%+.2e, %+.2e] | C/V0 end = %.3e | min R/rho_nc = %.3g"
          % (phi0, t[-1], " (R hit 0)" if s.status == 1 else "", u[-1], nacc, gH2[10:-10].min(), gH2[10:-10].max(), Cs[-1]/V0,
             (R/(0.5*Y[1]**2 + 0.5*m**2*Y[0]**2 + Y[2])).min()))
run(16.0); run(12.0)
print("Reading: the a^3-weighted running average relaxes C onto the plateau within ~1/(3H), so the plateau is cancelled")
print("(no 60 e-folds) and C' != 0 (g != 0: R15-1 signalling).  Only a reader told which w = -1 stress is the LATE one avoids this.")
