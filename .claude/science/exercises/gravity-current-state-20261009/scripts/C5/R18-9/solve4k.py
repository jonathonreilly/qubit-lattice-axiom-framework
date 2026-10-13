"""R18-9 step 2: the 4-knob solve at a FIXED photon edge.
Photon gammaGw(b_g, fw*(pi-b_g)) fixed (argv), its VWa coefficients computed exactly at N (argv) (Xi exactly quadratic in a).
Declared knobs (pre-registered): scalar edge b_s (fr fixed), Dirac b_f, Dirac r, stencil a.  Rows: Xi_T2g, Xi_Eg, mu_E, mu_T2 (totals).
Content 4 real scalars (U) + 22.5 Dirac (UD) + 12 vectors (VWa), m from argv. Newton with finite-difference Jacobian; det J reported."""
import sys, time, numpy as np, lib9 as L
bg, fw, N, m = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
fr = float(sys.argv[5]); x = np.array([float(v) for v in sys.argv[6].split(',')]); tag = sys.argv[7]
q = (4, 10)
t0 = time.time(); P = L.phot_quad(bg, fw, N); T, E, Vmu = P['T2g'], P['Eg'], P['muE']
print('photon gGw(%.6f, w=%.6f) N=%d: T (%+.6e %+.6e %+.2e) E (%+.6e %+.6e %+.2e) muE %+.6e [%.0fs]' % (bg, fw*(np.pi-bg), N, *T, *E, Vmu, time.time()-t0), flush=True)
def parts(x):
    bs, bf, r, a = x
    S = L.scal(bs, fr, m); F = L.dirac(bf, r, m=m, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu, 0.0])
    return S, F, V
def rows(x):
    S, F, V = parts(x); t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V[:3]
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
h = np.array([1e-5, 1e-6, 1e-6, 1e-6])
for it in range(8):
    f = rows(x); J = np.empty((4, 4))
    for j in range(4):
        dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx) - rows(x - dx))/(2*h[j])
    print('it %d x=(b_s %.9f, b_f %.9f, r %.9f, a %.9f) rows %s |.|=%.2e detJ %.3e' % (it, *x, np.array2string(f, precision=3), np.abs(f).max(), np.linalg.det(J)), flush=True)
    if np.abs(f).max() < 1e-13: break
    x = x - np.linalg.solve(J, f)
S, F, V = parts(x)
print('ROOT (b_s, b_f, r, a) = (%.10f, %.10f, %.10f, %.10f), fr = %.4f, photon b_g = %.6f fw = %.4f, m = %g' % (*x, fr, bg, fw, m))
print('per real scalar  (T, E, muE)       %+.6e %+.6e %+.6e' % tuple(S[:3]))
print('per Dirac field  (T, E, muE, muT2) %+.6e %+.6e %+.6e %+.6e' % tuple(F))
print('per vector       (T, E, muE)       %+.6e %+.6e %+.6e' % tuple(V[:3]))
c = np.array([L.NS*S[:3], L.ND*F[:3], L.NV*V[:3]])
print('contributions (scal / dirac / vec): T %s E %s muE %s' % (c[:, 0], c[:, 1], c[:, 2]))
print('TOTAL rows %s ; detJ (knobs b_s,b_f,r,a) %.4e ; r < 1/sqrt3: %s ; lam = 1/4 + 2a = %.5f' % (rows(x), np.linalg.det(J), x[2] < 1/np.sqrt(3), 0.25 + 2*x[3]))
np.save('root4k_%s.npy' % tag, np.r_[x, fr, bg, fw, m])
print('%.0fs' % (time.time()-t0))
