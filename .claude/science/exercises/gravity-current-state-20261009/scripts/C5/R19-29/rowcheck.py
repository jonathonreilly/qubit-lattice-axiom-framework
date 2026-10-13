"""normalization check: TT rows of the A1-library bubble against R17-4's archived evaluator (U, E1), root scalar edge."""
import sys, numpy as np
from a1lib import *
import offaxis as O
m = float(sys.argv[1]); law, z = root_scalar_law()
Xr, _ = O.xi_off(law, m, 'U', names=('Eg', 'T2g', 'face1', 'face2'))
print('R17-4:', {k: '%+.8e' % v for k, v in Xr.items()})
z3 = np.array([0, 0, 1.])
Eg = emb(np.diag([1., -1, 0])); T2 = np.zeros((3, 3)); T2[0, 1] = T2[1, 0] = 1; T2 = emb(T2)
F2 = emb(np.outer(a3, b3) + np.outer(b3, a3))
for N in [int(x) for x in sys.argv[2:]]:
    sc = Scalar(law, m, N); out = {}
    for nm, e, nv in (('Eg', Eg, z3), ('T2g', T2, z3), ('face1', E1F, n3), ('face2', F2, n3)):
        v = []
        for s in (0.02, 0.01):
            P = sc.block(s*nv, s, [e])[0, 0] - sc.block(0*nv, 0.0, [e])[0, 0]; v.append(P/s**2)
        out[nm] = (4*v[1] - v[0])/3
    print('N=%d:' % N, {k: '%+.8e' % v for k, v in out.items()})
