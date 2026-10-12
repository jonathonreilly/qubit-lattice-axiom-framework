"""C5 R11-3: the m^2 (phase-transition) step coefficients along the edge family u_t = (1-t)u_L + t u_G (U coupling), and the identity
c_rho + c_pU = d(rho+p_U)/dm^2 = -<trA/(12 eps)>  (derivative of rho+p_U = -<eps trA>/6).  m = 1e-3."""
import numpy as np
from r113_profiles import profile
from scipy.optimize import brentq
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
def coeffs(name, m=1e-3, N=160):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; u, up, upp = profile(name, k)
    Ux, Uy = np.meshgrid(u, u, indexing='ij'); Px, Py = np.meshgrid(up/2, up/2, indexing='ij'); Ax, Ay = np.meshgrid(upp/2-1, upp/2-1, indexing='ij')
    cr = cp = ca = 0.
    for iz in range(N):
        e = np.sqrt(m*m + Ux + Uy + u[iz]); p2 = Px**2 + Py**2 + (up[iz]/2)**2; trA = Ax + Ay + upp[iz]/2 - 1
        cr += (1/(4*e)).sum(); cp += (-p2/(12*e**3)).sum(); ca += (-trA/(12*e)).sum()
    n = float(N)**3; return cr/n, cp/n, ca/n
for t in [0.0, 0.05, 0.1, 0.2, 0.5, 1.0]:
    cr, cp, ca = coeffs('T%.4f' % t)
    pr('  t=%.2f: c_rho=%.5f c_pU=%+.5f ratio=%+.4f | c_rho+c_pU=%+.6f vs -<trA/(12eps)>=%+.6f' % (t, cr, cp, cp/cr, cr+cp, ca))
f = lambda t: (lambda c: c[0]+c[1])(coeffs('T%.6f' % t))
ts = brentq(f, 0.0, 0.2, xtol=1e-5)
pr('  step w = -1 (c_rho + c_pU = 0) at edge-family t* = %.5f (m -> 0): one edge tuning per species (U coupling); M coupling ratio is -1/3 for every profile' % ts)
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
