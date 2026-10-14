"""NF-1 (d): direct re-solve of the root's rows with the staggered edge (one fewer knob: no r; mu_T2 = 0 identically for the separable band).
Content: 4 real scalars (U, G_w(b_s, fr (pi - b_s))), N_s staggered fields (rows = N_s/4 x naive D1(b_f, 0) rows, UD), 12 vectors (VWa on
gammaG_w(b_g, fw (pi - b_g)), stencil weight a).  Rows Xi_T2g = Xi_Eg = mu_E = 0 at m = 0.01; knobs (b_s, b_f, a) at fixed fr and photon edge
(the photon edge from nf1_rows.out's sampled map).  Archived R18-9/R18-5 evaluators (lib9.phot_quad logic, content4.scalw, smud_lib.dirac).
argv: N_s fr b_g fw Nphot  [x0 = b_s,b_f,a]"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'flat')); os.chdir(os.path.join(HERE, '..', 'flat'))
import smud_lib
from content4 import scalw
from r1712_lib import xi, photonGw
from zz import mu_E
from scipy.optimize import least_squares
t00 = time.time()
Ns, fr, bg, fw, Nph = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5])
x0 = np.array([float(v) for v in sys.argv[6].split(',')]) if len(sys.argv) > 6 else np.array([1.5, 1.0, 0.0])
m = 0.01; NS, NV = 4.0, 12.0; wF = Ns/4.0
law = photonGw(bg, fw*(np.pi - bg))
P = {}
for pol in ('T2g', 'Eg'):
    v = np.array([xi(law, Nph, pol, 'VWa', lam=a)[0] for a in (0.0, 1.0, -1.0)])
    P[pol] = np.array([v[0], 0.5*(v[1] - v[2]), 0.5*(v[1] + v[2]) - v[0]])
g, f = law.samples(1 << 14); muG = 2*mu_E(g, f, 1e-3)
print('photon gammaG_w(%.3f, fw=%.2f) N=%d per vector: T2g(a) = %+.5e %+.5e a %+.2e a^2 ; Eg(a) = %+.5e %+.5e a %+.2e a^2 ; mu_E %+.5e  (%.0fs)'
      % (bg, fw, Nph, *P['T2g'], *P['Eg'], muG, time.time() - t00), flush=True)
def rows(z, parts=False):
    bs, bf, a = z
    S = scalw(bs, fr, m, vert='U')[0][:3]
    F = smud_lib.dirac(bf, 0.0, m=m)[:3]/4.0
    V = np.array([P['T2g'] @ [1, a, a*a], P['Eg'] @ [1, a, a*a], muG])
    tot = NS*S + wF*F + NV*V
    return (tot, S, F, V) if parts else tot*1e3
res = least_squares(rows, x0, bounds=([0.2, 0.3, -1.0], [3.12, 1.4, 1.0]), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-6, max_nfev=60)
z = res.x; tot, S, F, V = rows(z, True)
J = res.jac/1e3; sv = np.linalg.svd(J, compute_uv=False)
print('N_s = %.2f (w_F = %.4f), scalar fr = %.2f: knobs b_s = %.6f  b_f = %.6f  a = %+.6f   (nfev %d)' % (Ns, wF, fr, *z, res.nfev))
print('  per real scalar   : T2g %+.5e Eg %+.5e muE %+.5e' % tuple(S))
print('  per staggered fld : T2g %+.5e Eg %+.5e muE %+.5e  muT2 0 (separable band; R18-9 (S1))' % tuple(F))
print('  per vector        : T2g %+.5e Eg %+.5e muE %+.5e' % tuple(V))
print('  contributions T2g %+.4e/%+.4e/%+.4e  Eg %+.4e/%+.4e/%+.4e  muE %+.4e/%+.4e/%+.4e'
      % (NS*S[0], wF*F[0], NV*V[0], NS*S[1], wF*F[1], NV*V[1], NS*S[2], wF*F[2], NV*V[2]))
print('  TOTAL rows: T2g %+.2e  Eg %+.2e  muE %+.2e  muT2 0 ; Jacobian singular values %s ; det %+.3e' % (*tot, np.array2string(sv, precision=3), np.linalg.det(J)))
print('time %.0f s' % (time.time() - t00))
