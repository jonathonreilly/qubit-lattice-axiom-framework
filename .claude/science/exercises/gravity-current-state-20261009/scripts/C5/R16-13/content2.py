"""R16-13: content (Ns real scalars + ND 4-comp Dirac). Scalar edge = convex sigma'-mix of three 𝒮 laws
A = G(bA) [R14-1], B = G_w(bA, 0.3) [R14-3], C = G_w(0.67, 0.074) (sharp small-box flattening); weights (1-u-v, u, v).
Fermion = DG(bf, wf, r). Knobs: (u, v, bf); wf, r fixed. Root solve of Xi_T2g = Xi_Eg = mu_E = 0 at m."""
import numpy as np, sys, time
import dfam
from zz import ZLaw, Mix, xi_all, mu_E
from scipy.optimize import least_squares, fsolve
Ns, ND, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
bA, wf, r = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
x0 = np.array([float(v) for v in sys.argv[7].split(',')])
vert = sys.argv[8] if len(sys.argv) > 8 else 'M'
A = ZLaw([1.0, 0.0], [bA + (np.pi-bA)/2], np.pi-bA)
B = ZLaw([1.0, 0.0], [bA + 0.15], 0.3)
C = ZLaw([1.0, 0.0], [0.67 + 0.037], 0.074)
def scal(u, v, mm=m, n=1 << 14):
    L = Mix([A, B, C], [1-u-v, u, v]); g, f = L.samples(n)
    x = xi_all(g, f, mm, nu=1500)
    return np.array([x[vert+',T2g'], x[vert+',Eg'], mu_E(g, f, mm, nu=1500), 0.0]), L
def ferm(bf, mm=m, q=(3, 8)):
    o = dfam.evaluate(dfam.DG(bf, wf, r, nf=100001), mm, *q)
    return np.array([o['T2g'], o['Eg'], o['muE'], o['muT2']])
def F(z):
    u, v, bf = z
    return (Ns*scal(u, v)[0] + ND*ferm(bf))[:3]*1e3
t0 = time.time()
res = least_squares(F, x0, bounds=([0, 0, 0.6], [1, 1, np.pi/2 - wf - 1e-6]), xtol=1e-14, ftol=1e-14, gtol=1e-14, diff_step=1e-5, max_nfev=80)
u, v, bf = res.x
sv, L = scal(u, v); fv = ferm(bf)
tot = Ns*sv + ND*fv
print('content Ns=%g real scalars (vertex %s) + ND=%g Dirac, m=%g; bA=%.4f wf=%.6f r=%.4f' % (Ns, vert, ND, m, bA, wf, r))
print('knobs u=%.10f v=%.10f (1-u-v=%.10f) bf=%.10f  (nfev %d, %.1fs)' % (u, v, 1-u-v, bf, res.nfev, time.time()-t0))
print('scalar per real: Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % tuple(sv[:3]))
print('fermion per Dirac: Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e mu_T2 %+.6e' % tuple(fv))
print('TOTAL: Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.3e' % tuple(tot))
info = L.info(); print('scalar edge: max|sigma\'| %.9f, valleys %s, v_max(m) %.6f' % (info['maxabs'], info['valleys'], L.vmax(m)))
print('fermion DG W_pi %.4f, sampled v_max %.6f (Lemma V1 bound 1 since r<=1/sqrt3)' % (dfam.DG(bf, wf, r).Wpi, dfam.vmax_sample(dfam.DG(bf, wf, r), m)))
np.save('root_%g_%g_%s.npy' % (Ns, ND, vert), np.array([Ns, ND, m, bA, wf, r, u, v, bf]))
