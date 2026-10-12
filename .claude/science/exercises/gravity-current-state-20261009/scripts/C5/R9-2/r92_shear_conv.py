"""R9-2 (a) convergence: closed form vs grid N, and direct flow at N = 64, 128 (d = 3, m = 1 and 0.3, zero-point)."""
import numpy as np, sys
sys.argv = ['x']
exec(open('r92_shear.py').read().split("# ---- calibration")[0])
out2 = []
def pr2(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out2.append(line)
def cf(name, m, N, d=3, vac='Z'):
    g, gp, gpp = profile(name)
    f = lambda k: 0.5*gp(k); fp = lambda k: 0.5*gpp(k)
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    gx = g(kk); fx = f(kk); fpx = fp(kk)
    GX, GY = np.meshgrid(gx, gx, indexing='ij'); FX, FY = np.meshgrid(fx, fx, indexing='ij'); PX, PY = np.meshgrid(fpx, fpx, indexing='ij')
    cvac = 0.5 if vac == 'Z' else -1.0
    div = 0.5*(PX - PY); tot = 0.0
    for gz in (gx if d == 3 else [0.0]):
        eps = np.sqrt(m*m + GX + GY + gz); tot += (div*cvac*0.5*(FX*FX - FY*FY)/eps).sum()
    return -tot/N**d
for name in ['L', 'G']:
    g, gp, gpp = profile(name); f = lambda k: 0.5*gp(k)
    for m in [1.0, 0.3]:
        row = ['%s m=%.1f d=3 zero-point:' % (name, m)]
        for N in [160, 320, 640]:
            row.append('cf N=%d %+.7e' % (N, cf(name, m, N)))
        for N in [64, 128]:
            row.append('flow N=%d %+.7e' % (N, flow_direct(m, N, g, f, d=3, vac='Z')))
        pr2(' | '.join(row))
# shift of the closed form by the cell-centred grid offset (aliasing check): N=320 unshifted
with open('r92_shear_conv.out', 'w') as fh: fh.write('\n'.join(out2) + '\n')
