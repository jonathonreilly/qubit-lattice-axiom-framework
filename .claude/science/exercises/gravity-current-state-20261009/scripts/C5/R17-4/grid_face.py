"""R17-4: independent 3D-grid evaluation (midpoint zone grid, x-slices) of the E1 closed form, U vertex, on R16-3's U zero law
(m = 0.1), for Eg, T2g, face1, face2: Xi = (5/32)<W S^2/e^7> - (1/32)<W/e^5> - (3/64)<DW S/e^5>. Checks the Laplace evaluator."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, Mix
from floor_scan import Zz
from offaxis import POLS
T0 = time.time(); NF = 1 << 16; m = 0.1
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF); C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
L = Mix([A, C2, C], [1-0.964879-0.007410, 0.964879, 0.007410])
def samp(N):
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; a = np.abs(kk); sg = np.sign(kk)
    s = sg*np.interp(a, L.k, L.sig); sp = np.interp(a, L.k, L.sp); spp = sg*np.interp(a, L.k, np.gradient(L.sp, L.k))
    return s*s, s*sp, sp*sp + s*spp
for N in [240, 480, 720]:
    g, f, fp = samp(N); out = {}
    for name in ['Eg', 'T2g', 'face1', 'face2']:
        n, e = POLS[name]; n = np.array(n, float); tot = 0.0
        gy, gz = np.meshgrid(g, g, indexing='ij'); fy, fz = np.meshgrid(f, f, indexing='ij'); fpy, fpz = np.meshgrid(fp, fp, indexing='ij')
        for i in range(N):
            F = [f[i], fy, fz]; FP = [fp[i], fpy, fpz]
            ep2 = m*m + g[i] + gy + gz
            V = sum(e[a, b]*F[a]*F[b] for a in range(3) for b in range(3) if e[a, b] != 0)
            DV = sum(n[c]*FP[c]*sum(e[c, b]*F[b] + e[b, c]*F[b] for b in range(3) if e[c, b] != 0 or e[b, c] != 0) for c in range(3) if n[c] != 0)
            S = sum(n[c]*F[c] for c in range(3) if n[c] != 0)
            W = V*V; DW = 2*V*DV
            tot += np.sum((5/32)*W*S*S/ep2**3.5 - (1/32)*W/ep2**2.5 - (3/64)*DW*S/ep2**2.5)
        out[name] = tot/N**3
    print('N=%d grid: %s (%.0fs)' % (N, ' '.join('%s %+.5e' % kv for kv in out.items()), time.time()-T0), flush=True)
