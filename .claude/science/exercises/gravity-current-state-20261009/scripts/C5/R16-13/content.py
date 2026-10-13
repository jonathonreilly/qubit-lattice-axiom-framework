"""R16-13: mixed content solver. Content = Ns real scalars on G_w(bs, ws) [M vertex; zz.py Laplace] + ND 4-comp Dirac on DG(bf, wf, r)
[vielbein vertex V0; dfam GL quadrature]. Conditions at a common light mass m: Xi_T2g = Xi_Eg = mu_E = 0 (totals); mu_T2 reported."""
import numpy as np, sys, time
import dfam
from zz import ZLaw, xi_all, mu_E
from scipy.optimize import least_squares
def scalar_vals(bs, ws, m, vert='M'):
    L = ZLaw([1.0, 0.0], [bs + ws/2], ws)
    g, f = L.samples(1 << 14)
    x = xi_all(g, f, m, nu=1200)
    return np.array([x[vert+',T2g'], x[vert+',Eg'], mu_E(g, f, m, nu=1200), 0.0])
def fermion_vals(bf, wf, r, m, q=(3, 8)):
    o = dfam.evaluate(dfam.DG(bf, wf, r, nf=100001), m, *q)
    return np.array([o['T2g'], o['Eg'], o['muE'], o['muT2']])
def phys(x):
    bs, fs, bf, ff, r = x
    return bs, fs*(np.pi - bs), bf, ff*(np.pi/2 - bf), r
def total(x, Ns, ND, m, q=(3, 8), vert='M'):
    bs, ws, bf, wf, r = phys(x)
    return Ns*scalar_vals(bs, ws, m, vert) + ND*fermion_vals(bf, wf, r, m, q)
if __name__ == '__main__':
    Ns, ND, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    x0 = np.array([float(v) for v in sys.argv[4].split(',')])
    free = [int(v) for v in sys.argv[5].split(',')]       # indices of free knobs among (bs, ws, bf, wf, r)
    n4 = len(sys.argv) > 6 and sys.argv[6] == '4'
    lo = np.array([0.3, 0.03, 0.3, 0.05, 0.02]); hi = np.array([2.6, 1.0, 1.5, 1.0, 0.577])
    t0 = time.time()
    def F(z):
        x = x0.copy(); x[free] = z
        v = total(x, Ns, ND, m)
        return (v if n4 else v[:3])*1e3
    res = least_squares(F, x0[free], bounds=(lo[free], hi[free]), xtol=1e-12, ftol=1e-12, gtol=1e-12, diff_step=1e-4, max_nfev=60)
    x = x0.copy(); x[free] = res.x
    v = total(x, Ns, ND, m)
    print('Ns=%g ND=%g m=%g free=%s n4=%s' % (Ns, ND, m, free, n4))
    print('fractions x =', np.array2string(x, precision=10))
    print('knobs (bs, ws, bf, wf, r) = %s' % np.array2string(np.array(phys(x)), precision=10))
    xs = phys(x)
    print('totals: Xi_T2g %+.3e  Xi_Eg %+.3e  mu_E %+.3e  mu_T2 %+.3e   (nfev %d, %.1fs)' % (*v, res.nfev, time.time()-t0))
    print('scalar per real:', scalar_vals(xs[0], xs[1], m), ' fermion per Dirac:', fermion_vals(xs[2], xs[3], xs[4], m), flush=True)
