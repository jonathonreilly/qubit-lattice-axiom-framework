"""R11-6: invertibility of R9-3's (S2) symmetric mean A2 = (1/6) sum_perm B_x B_y B_z and of (S3) A3 = 1 + sum (B_c - 1)."""
import numpy as np, itertools, sys
from r116_core import *
out = []
for L in (128, 160, 240):
    for P in (0.2, 0.4):
        F = Fibre(L, P, 0.55, 0.55).build()
        A2 = sum(F.Bc[i]@F.Bc[j]@F.Bc[k] for i, j, k in itertools.permutations(range(3)))/6
        s2 = np.linalg.svd(A2, compute_uv=False)[-1]
        s = 'L=%d P=%.1f N=%d  s_min(A_S2)=%.3e  s_min(A_S3)=%.3e  ||B_a-1||_2=%.3f  ||B_b-1||_2=%.3f' % (L, P, F.N, s2, F.smin, np.linalg.norm(F.Bm1[0], 2), np.linalg.norm(F.Bm1[1], 2))
        print(s, flush=True); out.append(s)
open('r116_s2check.out', 'w').write('\n'.join(out) + '\n')
