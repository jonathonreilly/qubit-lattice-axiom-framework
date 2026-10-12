"""R11-6: invertibility of A = 1 + sum_c (B_c - 1): smallest singular value vs P and L; location of the near-null vector."""
import numpy as np, sys
from r116_core import *
args = dict(a.split('=') for a in sys.argv[1:])
out = []
for L in [int(x) for x in args.get('Ls', '128,160,240').split(',')]:
    for P in [float(x) for x in args.get('Ps', '0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8').split(',')]:
        F = Fibre(L, P, 0.55, 0.55).build()
        A = np.eye(F.N) + sum(F.Bm1)
        U, S, Vh = np.linalg.svd(A)
        v = Vh[-1].conj(); inner = np.prod(np.abs(F.mom) < 0.30, axis=0)
        win = np.sum(np.abs(v[inner > 0])**2)
        # untapered interior block: restrict A to interior |p_i| < 0.30 (taper = 1 there)
        idx = np.where(inner > 0)[0]; Si = np.linalg.svd(A[np.ix_(idx, idx)], compute_uv=False)
        s = 'L=%d P=%.2f N=%d s_min(A)=%.4e (near-null vector weight in |p_i|<0.30: %.3f)  s_min(A restricted to interior)=%.4e  ||B_a-1||=%.3f' % (L, P, F.N, S[-1], win, Si[-1], np.linalg.norm(F.Bm1[0], 2))
        print(s, flush=True); out.append(s)
open('r116_smin.out', 'w').write('\n'.join(out) + '\n')
