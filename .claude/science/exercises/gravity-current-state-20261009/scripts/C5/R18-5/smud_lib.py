"""R18-5 (c): SM-count content under (U scalar, UD Dirac, VW vector).  m = 0.01.
4 real scalars on ONE edge G_w(b_s, w_s) [U vertex, SF]; 22.5 Dirac on D1(b_f, r) [UD (or mix-u) vertex, SF];
12 vectors on one photon edge gammaGw(b_g, w_g) [VW0 or VWa stencil; SF shear = 2 x scalar formula (R17-9/R17-12)].
Rows (FIXED): Xi_T2g, Xi_Eg, mu_E totals; mu_T2 reported (R17-13's row, not a FIXED row here)."""
import numpy as np, sys
sys.path.insert(0, '.')
import dfam
from content3 import D1q
from content4 import scalw
from r1712_lib import xi, photonGw
from zz import mu_E
from xiud import pointwise
NS, ND, NV = 4.0, 22.5, 12.0
def dirac(bf, r, m=0.01, vtx='UD', q=(3, 8)):
    law = D1q(bf, r)
    ref = dfam.evaluate(law, m, *q)
    out = []
    for pol in ('T2g', 'Eg'):
        pw = pointwise(law, m, ['V0', vtx], pol, *q)
        out.append(ref[pol] + pw[vtx] - pw['V0'])
    return np.array([out[0], out[1], ref['muE'], ref['muT2']])
def phot(bg, wg, N=48, var='VW0', lam=None):
    law = photonGw(bg, wg)
    if var == 'VWa':
        T = xi(law, N, 'T2g', 'VWa', lam=lam)[0]; E = xi(law, N, 'Eg', 'VWa', lam=lam)[0]
    else:
        T = xi(law, N, 'T2g', var)[0]; E = xi(law, N, 'Eg', var)[0]
    g, f = law.samples(1 << 14)
    return np.array([T, E, 2*mu_E(g, f, 1e-3), 0.0])
def scal(bs, ws, m=0.01):
    return scalw(bs, ws/(np.pi - bs), m, vert='U')[0]
