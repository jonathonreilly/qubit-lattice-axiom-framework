"""R17-3 probe (a): record sourcing (i) in R16-6's homogeneous H-Z model (3H^2 = kappa R, kappa = 1).
Same inflaton + perturbative reheating history as R16-6's runner (m^2 phi^2/2 above V_late, Gamma = 0.05 m),
but the reader R is "the recorded content" under three record rules:
  REC-S    : everything above the late vacuum is recorded:  R = pi^2/2 + m^2 phi^2/2 + rho_r   (= R16-6 G0; counted once)
  REC-vac  : the homogeneous potential (false vacuum / plateau) is NOT recorded; kinetic + radiation are:
             R = pi^2/2 + rho_r
  REC-mass : count-type permanent records with fixed nonnegative weight ("records are mass" literal form):
             a^3 R = running max over the past of a^3 rho_nc  (records form while comoving energy above V_late grows,
             are never erased, and keep their weight)  -> Lemma M: a^3 R is non-decreasing.
Diagnostics: accelerating e-folds; g/H^2 = (kappa/3)(rho_tot - R)'/H^2 (Theorem Z; nonzero g = R15-1 signalling);
for REC-mass after reheating: R/rho_nc and the effective w of R, w_R = -1 - (1/3) dlnR/du.
Subtraction named before the run: V_late (the inflaton minimum) only.  Nothing else is subtracted.
"""
import numpy as np
from scipy.integrate import solve_ivp
m, Gam = 1.0, 0.05

def run(rule, phi0=16.0, t1=400.0):
    pi0 = -np.sqrt(2/3)*m
    rho0 = 0.5*pi0**2 + 0.5*m**2*phi0**2
    # state: phi, pi, rho_r, u, Q (=a^3 R running max for REC-mass)
    y0 = [phi0, pi0, 0.0, 0.0, rho0]
    def rho_nc(y): return 0.5*y[1]**2 + 0.5*m**2*y[0]**2 + y[2]
    def Rof(y):
        if rule == 'REC-S': return rho_nc(y)
        if rule == 'REC-vac': return 0.5*y[1]**2 + y[2]
        return y[4]*np.exp(-3*y[3])
    def rhs(t, y):
        R = Rof(y)
        if R <= 0: return [0.0]*5
        H = np.sqrt(R/3)
        phi, pi, rr, u = y[0], y[1], y[2], y[3]
        dphi = pi; dpi = -(3*H + Gam)*pi - m**2*phi; drr = -4*H*rr + Gam*pi**2
        # comoving true energy above V_late: E = a^3 rho_nc ; dE/dt = a^3 (drho + 3H rho)
        dE = np.exp(3*u)*((pi*dpi + m**2*phi*dphi + drr) + 3*H*rho_nc(y))
        a3rho = np.exp(3*u)*rho_nc(y)
        dQ = max(dE, 0.0) if a3rho >= y[4]*(1 - 1e-12) else 0.0
        return [dphi, dpi, drr, H, dQ]
    ts = np.linspace(0, t1, 200001)
    s = solve_ivp(rhs, (0, t1), y0, t_eval=ts, rtol=1e-10, atol=1e-13, method='DOP853', max_step=0.02)
    Y = s.y; t = s.t
    u = Y[3]
    rnc = np.array([rho_nc(Y[:, i]) for i in range(Y.shape[1])])
    R = np.array([Rof(Y[:, i]) for i in range(Y.shape[1])])
    H = np.sqrt(np.clip(R, 1e-300, None)/3)
    dRdu = np.gradient(R, t)/H
    acc = dRdu > -2*R
    du = np.gradient(u)
    nacc = np.sum(du[acc])
    # g from Theorem Z: g = (1/3) d(rho_tot - R)/dt ; rho_tot - R = V_late + (rnc - R)
    gdiff = np.gradient(rnc - R, t)/3
    gH2 = gdiff/H**2
    return dict(t=t, u=u, R=R, rnc=rnc, nacc=nacc, Ntot=u[-1], gH2=gH2, rr=Y[2], H=H)

for rule in ['REC-S', 'REC-vac', 'REC-mass']:
    d = run(rule)
    sl = slice(20, -20)
    print("%-8s phi0=16 | N_total=%.2f N_accel=%.2f | R/rho_nc end=%.4g | rho_r/rho_nc end=%.3f | g/H^2 in [%+.2e, %+.2e]"
          % (rule, d['Ntot'], d['nacc'], d['R'][-1]/d['rnc'][-1], d['rr'][-1]/d['rnc'][-1], d['gH2'][sl].min(), d['gH2'][sl].max()))
    if rule == 'REC-mass':
        u, R, rnc = d['u'], d['R'], d['rnc']
        a3R = R*np.exp(3*u)
        print("   Lemma M check: min over steps of d(a^3 R) / max|a^3 R| = %+.2e (>= -round-off means non-decreasing)"
              % (np.min(np.diff(a3R))/np.max(np.abs(a3R))))
        late = u > u[-1] - 3
        lnR = np.log(R[late]); wR = -1 - np.gradient(lnR, u[late])/3
        lnr = np.log(rnc[late]); wt = -1 - np.gradient(lnr, u[late])/3
        print("   last 3 e-folds: w of the recorded (gravitating) source = %.4f ; w of the true content = %.4f" % (np.median(wR), np.median(wt)))
        # ratio growth: radiation-era requirement R ~ a^-4
        for du_ in [1, 2, 3]:
            i0 = np.searchsorted(u, u[-1] - du_)
            print("   R/rho_nc at %d e-folds before end: %.3f" % (du_, R[i0]/rnc[i0]))
print("Reading: REC-vac reproduces R16-6 sec 4.2 (an unrecorded plateau does not inflate);")
print("REC-mass inflates (records form on new sites) but cannot follow reheating: its source stays dust-like (w_R ~ 0)")
print("while the true content is radiation (w = 1/3); a^3 R never falls, so no w > 0 era exists for it (Lemma M).")
