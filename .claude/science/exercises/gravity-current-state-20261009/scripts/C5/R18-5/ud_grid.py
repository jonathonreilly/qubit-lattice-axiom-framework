"""R18-5 (b): UD vs V0 per Dirac field on a D1(b_f, r) grid, m = 0.01 (GL (3,8); mu rows are SF, vertex-independent)."""
import numpy as np, time
import dfam
from content3 import D1q
from xiud import pointwise
t0 = time.time(); m = 0.01; rows = []
for bf in (0.15, 0.2, 0.3, 0.45, 0.6, 0.9, 1.2, 1.4):
    for r in (0.1, 0.3, 0.5, 0.5773):
        law = D1q(bf, r); ref = dfam.evaluate(law, m, 3, 8); v = {}
        for pol in ('T2g', 'Eg'):
            pw = pointwise(law, m, ['V0', 'UD', 'V0*'], pol, 3, 8)
            for n in ('V0', 'UD', 'V0*'): v[(n, pol)] = ref[pol] + pw[n] - pw['V0']
        rows.append((bf, r, v[('UD', 'T2g')], v[('UD', 'Eg')], v[('UD', 'T2g')] - v[('UD', 'Eg')], v[('V0', 'T2g')] - v[('V0', 'Eg')], v[('V0*', 'T2g')] - v[('V0*', 'Eg')], ref['muE'], ref['muT2']))
        print('D1(%.2f,%.4f): UD T2g %+.3e Eg %+.3e biref %+.3e | V0 biref %+.3e | V0* biref %+.3e | muE %+.3e muT2 %+.3e' % rows[-1], flush=True)
R = np.array(rows)
print('UD biref range [%.3e, %.3e]; UD T2g range [%.3e, %.3e]; V0 biref min %.3e; V0* biref max %.3e' % (R[:, 4].min(), R[:, 4].max(), R[:, 2].min(), R[:, 2].max(), R[:, 5].min(), R[:, 6].max()))
print('%.0fs' % (time.time() - t0))
