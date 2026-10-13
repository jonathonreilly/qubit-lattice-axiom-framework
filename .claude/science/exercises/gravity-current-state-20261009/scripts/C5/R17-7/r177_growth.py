"""R17-7 (a)/(d): linear growth under (S).  With g == 0 and C = E0 the theory is GR with one constant (Theorem Z,
counted once), so linear k != 0 perturbations are GR's.  For smooth dark energy (canonical scalar, c_s = 1, sub-horizon)
the matter growth obeys D'' + (2 + dlnH/dlna) D' = (3/2) Om(a) D (' = d/dlna).  Compared here: LCDM best fit,
CPL truth, and the two best-fit thawing scalars from r177_late_universe.out (parameters copied from that output).
Normalization (named before the run): D = a at a = 1e-3 for every model (same primordial amplitude, same early growth).
Reported: D(1) and f sigma8-proxy f(z) D(z) relative to LCDM(best Om) at z = 0, 0.5, 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
Or = 9e-5

def thaw_H(Om, lam, pot):
    rm0, rr0 = 3*Om, 3*Or
    if pot == 'exp':
        Vf = lambda p, V0: V0*np.exp(-lam*p); dVf = lambda p, V0: -lam*V0*np.exp(-lam*p); phi_i = 0.0
    else:
        f = 1/lam; Vf = lambda p, V0: V0*(1 + np.cos(p/f)); dVf = lambda p, V0: -V0/f*np.sin(p/f); phi_i = 0.3*f
    def run(V0, dense=False):
        def rhs(N, y):
            p, v = y
            rm, rr = rm0*np.exp(-3*N), rr0*np.exp(-4*N)
            H2 = (rm + rr + Vf(p, V0))/(3 - v**2/2)
            return [v, -(3 - 0.5*(rm + 4*rr/3)/H2 - v**2/2)*v - dVf(p, V0)/H2]
        Ns = np.linspace(np.log(1e-3), 0, 4001)
        s = solve_ivp(rhs, (Ns[0], 0), [phi_i, 0.0], t_eval=Ns, rtol=1e-10, atol=1e-12, method='DOP853')
        p, v = s.y; rm, rr = rm0*np.exp(-3*Ns), rr0*np.exp(-4*Ns)
        H2 = (rm + rr + Vf(p, V0))/(3 - v**2/2)
        return (H2[-1] - 1) if not dense else (Ns, np.sqrt(H2))
    V0 = brentq(run, 0.1, 50, xtol=1e-12)
    return run(V0, True)

def cpl_H(Om, w0=-0.75, wa=-0.86):
    Ns = np.linspace(np.log(1e-3), 0, 4001); a = np.exp(Ns)
    return Ns, np.sqrt(Om*a**-3 + Or*a**-4 + (1 - Om - Or)*a**(-3*(1 + w0 + wa))*np.exp(-3*wa*(1 - a)))

def lcdm_H(Om):
    Ns = np.linspace(np.log(1e-3), 0, 4001); a = np.exp(Ns)
    return Ns, np.sqrt(Om*a**-3 + Or*a**-4 + 1 - Om - Or)

def growth(Ns, H, Om):
    dlnH = np.gradient(np.log(H), Ns)
    Omfun = lambda N: Om*np.exp(-3*N)/np.interp(N, Ns, H)**2
    def rhs(N, y):
        D, Dp = y
        return [Dp, -(2 + np.interp(N, Ns, dlnH))*Dp + 1.5*Omfun(N)*D]
    a0 = np.exp(Ns[0])
    s = solve_ivp(rhs, (Ns[0], 0), [a0, a0], t_eval=Ns, rtol=1e-10, atol=1e-14)
    D, Dp = s.y
    return D, Dp/D

models = {'LCDM (Om=0.2823)': (lcdm_H(0.2823), 0.2823),
          'CPL truth (Om=0.31)': (cpl_H(0.31), 0.31),
          'thaw exp (Om=0.2850, lam=0.639)': (thaw_H(0.2850, 0.639, 'exp'), 0.2850),
          'thaw pngb (Om=0.2891, lam=2.804)': (thaw_H(0.2891, 2.804, 'pngb'), 0.2891)}
res = {}
for name, ((Ns, H), Om) in models.items():
    D, f = growth(Ns, H, Om); res[name] = (Ns, D, f)
ref = res['LCDM (Om=0.2823)']
print("Growth under (S) = GR + smooth content above E0 (no new k-dependence; Lemma S ultralocal at g = 0):")
for name, (Ns, D, f) in res.items():
    out = []
    for z in [0.0, 0.5, 1.0]:
        N = np.log(1/(1+z))
        fD = np.interp(N, Ns, f*D); fD0 = np.interp(N, ref[0], ref[2]*ref[1])
        out.append("z=%.1f: fD/fD_LCDM = %.4f" % (z, fD/fD0))
    print("   %-34s D(1)/D_LCDM(1) = %.4f ; %s" % (name, D[-1]/ref[1][-1], " ; ".join(out)))
