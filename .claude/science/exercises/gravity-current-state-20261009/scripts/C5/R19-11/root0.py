"""R19-11 (b): the 4-row axial root at m -> 0+ (scalar mass m_s, Dirac mass m_f), photon edge and its massless VWa
coefficients fixed (R18-9's photon gGw(2.9435, fw=1), recomputed here at N = 224: phq_N224.npy).
Knobs (as R18-9): b_s (fr = 1), b_f, r, a. Rows: Xi_T2g, Xi_Eg, mu_E totals (4 + 22.5 + 12) and mu_T2 total (22.5 Dirac).
Newton with central-difference Jacobian at Dirac GL q1; final residual reported at q1 and q2."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch9'))
import lib9 as L
ms, mf = float(sys.argv[1]), float(sys.argv[2])
x = np.array([float(v) for v in sys.argv[3].split(',')]); q1 = tuple(int(v) for v in sys.argv[4].split(','))
q2 = tuple(int(v) for v in sys.argv[5].split(',')); tag = sys.argv[6]
P = np.load(os.path.join(HERE, 'phq_N224.npy')); T, E, Vmu = P[0:3], P[3:6], P[6]
def rows(x, q):
    bs, bf, r, a = x
    S = L.scal(bs, 1.0, ms); F = L.dirac(bf, r, m=mf, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu])
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]]), S, F, V
t0 = time.time(); h = np.array([1e-5, 1e-6, 1e-6, 1e-6])
for it in range(8):
    f = rows(x, q1)[0]; J = np.empty((4, 4))
    for j in range(4):
        dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx, q1)[0] - rows(x - dx, q1)[0])/(2*h[j])
    print('it %d x=(%.10f, %.10f, %.10f, %.10f) rows %s detJ %.4e sv %s' % (it, *x, np.array2string(f, precision=3), np.linalg.det(J), np.array2string(np.linalg.svd(J)[1], precision=4)), flush=True)
    if np.abs(f).max() < 1e-14: break
    x = x - np.linalg.solve(J, f)
f1, S, F, V = rows(x, q1); f2, _, F2, _ = rows(x, q2)
print('ROOT m_s=%g m_f=%g: (b_s, b_f, r, a) = (%.10f, %.10f, %.10f, %.10f); r < 1/sqrt3 (%.7f): %s' % (ms, mf, *x, 1/np.sqrt(3), x[2] < 1/np.sqrt(3)))
print('per scalar (T,E,muE) %s | per Dirac GL%s (T,E,muE,muT2) %s | per vector (T,E,muE) %s' % (S[:3], q1, F, V))
print('rows at GL%s: %s ; at GL%s: %s' % (q1, f1, q2, f2))
print('Dirac GL%s (T,E,muE,muT2) %s' % (q2, F2))
np.save(os.path.join(HERE, 'root0_%s.npy' % tag), np.r_[x, 1.0, 2.9435, 1.0, mf, ms])
print('[%.0fs]' % (time.time() - t0))
