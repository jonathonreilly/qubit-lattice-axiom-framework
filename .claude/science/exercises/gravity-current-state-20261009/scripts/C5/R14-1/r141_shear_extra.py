"""R14-1: (1) convergence of the free-shear coefficient mu_E (zero-point vacuum Z, d = 3) for the subluminal profiles
S(1.4), G(1.4) (closed form of r92_shear.py at N = 160, 320, 480);  (2) whole-zone group velocity of R9-2's
tuned edge g_t = (1-t) g_L + t g_G at the root t* (0.287922 at m = 1; 0.297708 at m = 0.3) and along the family."""
import numpy as np, sys
sys.argv = ['x']
src = open('r141_shear.py').read().split("# ---- calibration")[0]
exec(src)
out2 = []
def pr2(*a):
    l = ' '.join(str(x) for x in a); print(l, flush=True); out2.append(l)
def mu_cf(g, gp, gpp, m, N):
    f = lambda k: 0.5*gp(k); fp = lambda k: 0.5*gpp(k)
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    gx, fx, fpx = g(kk), f(kk), fp(kk)
    GX, GY = np.meshgrid(gx, gx, indexing='ij'); FX, FY = np.meshgrid(fx, fx, indexing='ij'); PX, PY = np.meshgrid(fpx, fpx, indexing='ij')
    div = 0.5*(PX - PY); tot = 0.0
    for gz in gx:
        eps = np.sqrt(m*m + GX + GY + gz); tot += (div*0.5*0.5*(FX*FX - FY*FY)/eps).sum()
    return -tot/N**3
for name in ['S14', 'G14', 'G', 'L']:
    g, gp, gpp = profile(name)
    for m in [1.0, 0.3]:
        pr2('mu_E(Z, d=3) profile %-3s m=%.1f: ' % (name, m) + '  '.join('N=%d: %+.6e' % (N, mu_cf(g, gp, gpp, m, N)) for N in (160, 320, 480)))
gL, gpL, gppL = profile('L'); gG, gpG, gppG = profile('G')
k1 = np.linspace(-np.pi, np.pi, 400000, endpoint=False) + np.pi/400000
for m, ts in [(1.0, 0.287922), (0.3, 0.297708)]:
    for t in [0.0, 0.1, 0.2, ts, 0.4, 0.6, 0.8, 1.0]:
        g = (1-t)*gL(k1) + t*gG(k1); gp = (1-t)*gpL(k1) + t*gpG(k1)
        v1 = np.max(np.abs(gp)/(2*np.sqrt(m*m + g)))
        # d = 3 along body diagonal and axis are the extremes for separable laws with one hot axis; report the axis value
        pr2('tuned-edge family m=%.1f t=%.6f: v_max (axis, d=1) = %.4f%s' % (m, t, v1, '   <- root t*' if t == ts else ''))
open('r141_shear_extra.out', 'w').write('\n'.join(out2) + '\n')
