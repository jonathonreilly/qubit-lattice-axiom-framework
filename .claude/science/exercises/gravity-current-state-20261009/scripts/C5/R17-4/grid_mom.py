"""R17-4: 3D-grid check of the derivative-free U moment form (fastU) on R16-3's U zero law, m = 0.1:
face1 = -a6/128 + 45 a42/128 - 5 a222/16 - 3 b4/64 + b22/64; T2g = 5 a222/8 - b22/8; Eg = 5(a42-a222)/16 - (b4-b22)/16 (symmetrized averages)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, Mix
from floor_scan import Zz
from fastU import rowsU
T0 = time.time(); NF = 1 << 16; m = 0.1
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF); C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
L = Mix([A, C2, C], [1-0.964879-0.007410, 0.964879, 0.007410])
g1, f1 = L.samples(1 << 14); R = rowsU(g1, f1, m, nu=3000, umin=-20)
print('Laplace (fastU, n=2^14, nu=3000): Eg %+.6e T2g %+.6e face1 %+.6e K6row %+.6e' % (R['Eg'], R['T2g'], R['face1'], R['K6row']))
for N in [240, 480, 720]:
    g, f = L.samples(N); f2 = f*f
    gy, gz = np.meshgrid(g, g, indexing='ij'); Y, Z = np.meshgrid(f2, f2, indexing='ij')
    acc = dict(a6=0.0, a42=0.0, a222=0.0, b4=0.0, b22=0.0)
    for i in range(N):
        X = f2[i]; e2 = m*m + g[i] + gy + gz; e7 = e2**3.5; e5 = e2**2.5
        acc['a6'] += np.sum((X**3 + Y**3 + Z**3)/3/e7); acc['a42'] += np.sum((X*X*Y + X*X*Z + Y*Y*X + Y*Y*Z + Z*Z*X + Z*Z*Y)/6/e7)
        acc['a222'] += np.sum(X*Y*Z/e7); acc['b4'] += np.sum((X*X + Y*Y + Z*Z)/3/e5); acc['b22'] += np.sum((X*Y + Y*Z + X*Z)/3/e5)
    a = {k: v/N**3 for k, v in acc.items()}
    face1 = -a['a6']/128 + 45*a['a42']/128 - 5*a['a222']/16 - 3*a['b4']/64 + a['b22']/64
    T2g = 5*a['a222']/8 - a['b22']/8; Eg = 5*(a['a42']-a['a222'])/16 - (a['b4']-a['b22'])/16
    print('N=%d grid: Eg %+.6e T2g %+.6e face1 %+.6e K6row %+.6e (%.0fs)' % (N, Eg, T2g, face1, -(a['a6'] - 15*a['a42'] + 30*a['a222'])/128, time.time()-T0), flush=True)
