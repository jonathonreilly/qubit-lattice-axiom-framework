"""R19-26 rows: the archived off-axis photon row evaluator (R18-13 vwface.xi_geo, unmodified) with the analytic law (R0), run
with VW as archived ('noF') or with the re-placement factor F(q_i)F(q_j) on every off-diagonal T^{ij} ('F'; q = wrap(k1 + k2),
the graviton momentum of the pair, = lib1926's F(wrap(k1 - k2)) in the stress convention).  vertex_geo is linear in e, so the
wrapper splits e into its diagonal and its symmetric (i, j) pairs and scales each pair's output.  Axial rows (T2g, Eg, mu_E;
q || z) and the xz row (q || y) see F(0)^2 = 1 exactly, so only face1/face2 (q || (1,1,0)) can move.
argv: N mode [rows]."""
import os, sys, time, numpy as np
import lib1926 as R
HERE = R.HERE
sys.path.insert(0, os.path.join(HERE, 'orig', 'arch18_13'))
import vwface as V
from r99_profiles import wrap
N = int(sys.argv[1]); mode = sys.argv[2]; rows = sys.argv[3].split(',') if len(sys.argv) > 3 else ['face1', 'face2']
V0 = V.vertex_geo
def vertex_geo_F(e, c1, c2, s, a, wd=0.0, wo=0.0):
    ME, MB = V0(np.diag(np.diag(e)), c1, c2, s, a, wd, wo)
    f = R.Fplace(wrap(s))
    for i in range(3):
        for j in range(i + 1, 3):
            if e[i, j] == 0 and e[j, i] == 0: continue
            eij = np.zeros((3, 3)); eij[i, j] = e[i, j]; eij[j, i] = e[j, i]
            Mo, Bo = V0(eij, c1, c2, s, a, wd, wo); fac = (f[..., i]*f[..., j])[..., None, None]
            ME = ME + fac*Mo; MB = MB + fac*Bo
    return ME, MB
if mode == 'F': V.vertex_geo = vertex_geo_F
# linearity control of the wrapper with F == 1
if mode == 'lin':
    R.Fplace = lambda q: np.ones_like(np.asarray(q, float)); V.vertex_geo = vertex_geo_F
t0 = time.time()
LAWA = R.R16.AnalyticPhotonLaw(); a = -0.1760950036
sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
out = []
for row in rows:
    X = V.xi_geo(LAWA, N, row, a, sets, (1, 2)); out.append(X)
    print(f'N={N} mode={mode} {row}: per vector at (wd,wo)=(0,0) {X[0]:+.12e} | d/dwd {X[1]-X[0]:+.12e} | d/dwo {X[2]-X[0]:+.12e} [{time.time()-t0:.0f}s]', flush=True)
np.save(os.path.join(HERE, f'rows_{mode}_N{N}.npy'), np.array(out))
