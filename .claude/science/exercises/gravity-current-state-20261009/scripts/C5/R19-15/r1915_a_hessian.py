"""R19-15 probe (a): is the archived shear row mu_E the vacuum's uniform-strain energy Hessian?
Separable one-band laws eps^2 = m^2 + sum g(k_i), f = g'/2 (R14-3 prof.py, archived copy, unmodified).
Strain flow SF for a unit E_g strain h = diag(1,-1,0): v = (1/2) h.f, i.e. dk_x/dt = f(k_x)/2, dk_y/dt = -f(k_y)/2.
T2g unit strain h_xy = h_yx = 1: dk_x/dt = f(k_y)/2, dk_y/dt = f(k_x)/2 (divergence-free).
Vacuum energy density of the strained law: e(t) = (1/2) < eps(Phi_t(k)) >.
Checks: (1) e''(0) by finite differences equals R14-3's closed form mu_E (and V3's NN comparator);
        (2) seagull + bubble split, seagull = <(eps^2)''/(4 eps)>, bubble = -<((eps^2)')^2/(8 eps^3)>;
        (3) T2g: e(t) - e(0) vanishes (Liouville) for every scalar law.
"""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '../arch14_3')
from prof import Law, G_law, grid, mu_E

T0 = time.time()

class NN:
    name = 'NN(sin)'
    def gff(self, k):
        k = np.asarray(k, float)
        return 2 - 2*np.cos(k), np.sin(k), np.cos(k)

def Gw(b, w):
    return Law([1.0, 0.0], [b], [w], 'G_w(%.2f,%.6f)' % (b, w))

def flow1d(law, k, t, nst=40):
    """integrate dk/dt = f(k)/2 from 0 to t (RK4)."""
    h = t/nst; x = k.copy()
    F = lambda y: 0.5*law.gff(y)[1]
    for _ in range(nst):
        a = F(x); b = F(x + 0.5*h*a); c = F(x + 0.5*h*b); d = F(x + h*c)
        x = x + h*(a + 2*b + 2*c + d)/6
    return x

def flowT2(law, kx, ky, t, nst=40):
    h = t/nst; x, y = kx.copy(), ky.copy()
    F = lambda y_: 0.5*law.gff(y_)[1]
    for _ in range(nst):
        a1, a2 = F(y), F(x)
        b1, b2 = F(y + 0.5*h*a2), F(x + 0.5*h*a1)
        c1, c2 = F(y + 0.5*h*b2), F(x + 0.5*h*b1)
        d1, d2 = F(y + h*c2), F(x + h*c1)
        x, y = x + h*(a1 + 2*b1 + 2*c1 + d1)/6, y + h*(a2 + 2*b2 + 2*c2 + d2)/6
    return x, y

def eE(law, m, N, t):
    k = grid(N); kx = flow1d(law, k, t); ky = flow1d(law, k, -t)
    gx = law.gff(kx)[0]; gy = law.gff(ky)[0]; gz = law.gff(k)[0]
    tot = 0.0
    for z in gz:
        tot += np.sqrt(m*m + gx[:, None] + gy[None, :] + z).sum()
    return 0.5*tot/N**3

def eT(law, m, N, t):
    k = grid(N); KX, KY = np.meshgrid(k, k, indexing='ij')
    x, y = flowT2(law, KX, KY, t)
    gxy = law.gff(x)[0] + law.gff(y)[0]; gz = law.gff(k)[0]
    tot = 0.0
    for z in gz:
        tot += np.sqrt(m*m + gxy + z).sum()
    return 0.5*tot/N**3

def split(law, m, N):
    """seagull and bubble pieces of the E_g Hessian (free field, dispersion change only)."""
    k = grid(N); g, f, fp = law.gff(k)
    FX, FY, PX, PY = f[:, None], f[None, :], fp[:, None], fp[None, :]
    G2 = g[:, None] + g[None, :]
    d1 = FX**2 - FY**2                      # (eps^2)' along the E_g flow
    d2 = FX**2*PX + FY**2*PY                # (eps^2)''
    sg = bb = 0.0
    for z in g:
        e = np.sqrt(m*m + G2 + z)
        sg += (d2/(4*e)).sum(); bb += (-(d1**2)/(8*e**3)).sum()
    return sg/N**3, bb/N**3

cases = [(NN(), 1.0), (G_law(1.4), 1.0), (G_law(1.4), 0.3), (Gw(1.4, 0.349416), 0.3), (Gw(1.4, 0.389587), 1.0), (Gw(1.4, 0.2), 0.3)]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 96
if len(sys.argv) > 3 and sys.argv[3] == 'gw':
    cases = cases[3:]
print('N = %d' % N)
for law, m in cases:
    if isinstance(law, NN):
        k = grid(N); g, f, fp = law.gff(k)
        t1 = t2 = 0.0
        for z in g:
            e = np.sqrt(m*m + g[:, None] + g[None, :] + z)
            t1 += ((fp[:, None] - fp[None, :])*(f[:, None]**2 - f[None, :]**2)/e).sum()
            t2 += ((3*f[:, None]**2*f[None, :]**2 - f[:, None]**4)/e**3).sum()
        cA, cB = -t1/8/N**3, t2/12/N**3
    else:
        cA, cB = mu_E(law, m, N)
    e0 = eE(law, m, N, 0.0)
    fd = {}
    for d in (4e-3, 2e-3):
        fd[d] = (eE(law, m, N, d) - 2*e0 + eE(law, m, N, -d))/d**2
    rich = (4*fd[2e-3] - fd[4e-3])/3
    sg, bb = split(law, m, N)
    dT = [eT(law, m, N, s) - eT(law, m, N, 0.0) for s in (0.05, 0.2)]
    print('%-22s m=%.2f  closed-form mu_E: A-form %+.9e  IBP %+.9e' % (law.name, m, cA, cB))
    print('   e\'\'(0) finite-diff (Richardson) %+.9e   diff vs closed %.2e' % (rich, rich - cA))
    print('   seagull %+.6e  bubble %+.6e  sum %+.9e   e0 = %.6f' % (sg, bb, sg + bb, e0))
    print('   T2g flow: e(0.05)-e(0) = %+.2e, e(0.2)-e(0) = %+.2e  (Liouville: 0)' % tuple(dT), flush=True)
print('V3 comparator (PRICE_NOTE v6 2a): NN m=1 mu_E = +1.97038864e-3')
print('runtime %.1fs' % (time.time() - T0))
