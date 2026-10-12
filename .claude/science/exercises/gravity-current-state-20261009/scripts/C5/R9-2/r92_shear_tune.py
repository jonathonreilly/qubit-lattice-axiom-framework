"""R9-2 (a): the E_g coefficient along the edge family g_t = (1-t) g_L + t g_G (box fixed: g_t = k^2 on |k| <= 2),
d = 3, zero-point vacuum, RN-L1 normalisation.  mu_E(0) < 0 < mu_E(1), so a root t* exists (intermediate value):
the shear can be removed only by choosing the edge (a one-parameter tuning per species, as V3's a*)."""
import numpy as np, sys
sys.argv = ['x']
exec(open('r92_shear.py').read().split("# ---- calibration")[0])
out2 = []
def pr2(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out2.append(line)
gL, gpL, gppL = profile('L'); gG, gpG, gppG = profile('G')
def mu(t, m=1.0, N=320):
    g = lambda k: (1-t)*gL(k) + t*gG(k); f = lambda k: 0.5*((1-t)*gpL(k) + t*gpG(k)); fp = lambda k: 0.5*((1-t)*gppL(k) + t*gppG(k))
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    gx = g(kk); fx = f(kk); fpx = fp(kk)
    if np.min(gx) < -0.99*m*m/3: return np.nan
    GX, GY = np.meshgrid(gx, gx, indexing='ij'); FX, FY = np.meshgrid(fx, fx, indexing='ij'); PX, PY = np.meshgrid(fpx, fpx, indexing='ij')
    div = 0.5*(PX - PY); tot = 0.0
    for gz in gx:
        eps = np.sqrt(m*m + GX + GY + gz); tot += (div*0.5*0.5*(FX*FX - FY*FY)/eps).sum()
    return -tot/N**3
for m in [1.0, 0.3]:
    ts = np.linspace(0, 1, 11); vals = [mu(t, m) for t in ts]
    pr2('m = %.1f: ' % m + ', '.join('t=%.1f: %+.4e' % (t, v) for t, v in zip(ts, vals)))
    i = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
    if len(i):
        a, b = ts[i[0]], ts[i[0]+1]
        for _ in range(40):
            c = 0.5*(a+b)
            if np.sign(mu(c, m)) == np.sign(mu(a, m)): a = c
            else: b = c
        pr2('   root t* = %.6f (mu_E(t*) = %+.1e); V3 NN-scalar reference mu_E = +1.970389e-03 (m = 1)' % (0.5*(a+b), mu(0.5*(a+b), m)))
with open('r92_shear_tune.out', 'w') as fh: fh.write('\n'.join(out2) + '\n')
