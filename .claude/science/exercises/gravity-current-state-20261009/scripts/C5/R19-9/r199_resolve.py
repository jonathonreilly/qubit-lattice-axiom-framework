"""R19-9 (c): re-solve the 6-knob SM root (b_s, b_f, r_D, a, w_d, w_o) with the EXACT photon vertex (corner radius r).
Row model (all archived evaluators unmodified, resolutions as stated):
  axial T2g, Eg, mu_E, mu_T2: R18-9 lib9 (scalars U; Dirac UD at GL q=(4,10); photon Xi quadratic in a with N = 224 coefficients
     from arch18_9/solve4k_N224.out; mu rows from SF, band only);
  face1, face2: scalars R17-4 offaxis (U, E1); Dirac R18-13 dface GL(4,10); photon R18-13 photface_N224.out values at
     a0 = -0.1760950036 with its exact w-derivatives (Lemma O(ii): exactly linear in w), a-derivative from r199_facejac (N = 96);
  exact-vertex corner: + 12 * C_e(a, w_d, w_o) r^4 on T2g, Eg, face1, face2 (r199_corner_rows; C exactly linear in (a, w));
     mu rows unchanged (SF uses the band only).
Quasi-Newton with a fixed Jacobian (J_axial from r199_jac_refroot.out, J_face,axial from r199_facejac, exact w block)."""
import os, sys, re, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch18_9')); sys.path.insert(0, os.path.join(HERE, 'arch17_4'))
import lib9 as L9
import offaxis as O
from zz import ZLaw
sys.path.insert(0, os.path.join(HERE, 'arch18_13'))
import dface as DF
from content3 import D1q
import r199_corner_rows as CR
t0 = time.time()
z = np.load(os.path.join(HERE, 'arch18_13', 'root_refR18-9.npy')); x_ax0 = z[:4].copy(); fr, bg, fw, m = z[4], z[5], z[6], z[7]
line = open(os.path.join(HERE, 'arch18_9', 'solve4k_N224.out')).readline()
g = [float(v) for v in re.match(r'photon gGw\(([\d.]+), w=([\d.]+)\) N=(\d+): T \(([^ ]+) ([^ ]+) ([^)]+)\) E \(([^ ]+) ([^ ]+) ([^)]+)\) muE ([^ ]+)', line).groups()]
TC, EC, Vmu = np.array(g[3:6]), np.array(g[6:9]), g[9]
PQ = os.path.join(HERE, 'photquad_N224.npy')
if os.path.exists(PQ) and '--rounded' not in sys.argv:      # full-precision N = 224 coefficients (r199_photquad.py)
    v = np.load(PQ); TC, EC, Vmu = v[:3], v[3:6], v[6]
print('photon axial coefficients used:', TC, EC, Vmu)
A0 = -0.1760950036
F1_0, F2_0 = 2.182473207e-01, 1.092917123e-01            # photface_N224.out, per vector, (w_d, w_o) = (0, 0)
DF1_WD, DF1_WO, DF2_WO = 1.397040e-01, 2.892797e-01, 5.785714e-01
JF = np.load(os.path.join(HERE, 'facejac.npy'))         # totals, rows face1/face2, cols b_s, b_f, r_D, a (photon part at N = 96)
DF1_A, DF2_A = JF[0, 3]/12, JF[1, 3]/12                 # per vector
# corner coefficients and their exact linear dependence
C0 = CR.corner_coeffs(CR.L.A_R, CR.L.WD_R, CR.L.WO_R)
dCa = CR.corner_coeffs(CR.L.A_R + 1.0, CR.L.WD_R, CR.L.WO_R); dCd = CR.corner_coeffs(CR.L.A_R, CR.L.WD_R + 1.0, CR.L.WO_R)
dCo = CR.corner_coeffs(CR.L.A_R, CR.L.WD_R, CR.L.WO_R + 1.0)
def Ccorner(row, a, wd, wo):
    return C0[row] + (dCa[row] - C0[row])*(a - CR.L.A_R) + (dCd[row] - C0[row])*(wd - CR.L.WD_R) + (dCo[row] - C0[row])*(wo - CR.L.WO_R)

def rows(x, r):
    bs, bf, rD, a, wd, wo = x
    S = L9.scal(bs, fr, m); F = L9.dirac(bf, rD, m=m, q=(4, 10))
    V = np.array([TC[0] + TC[1]*a + TC[2]*a*a, EC[0] + EC[1]*a + EC[2]*a*a, Vmu])
    t = L9.NS*S[:3] + L9.ND*F[:3] + L9.NV*V
    wA = fr*(np.pi - bs); Xs, _ = O.xi_off(ZLaw([1.0, 0.0], [bs + wA/2], wA), m, 'U')
    Xd = DF.xi_dirac(D1q(bf, rD), m, rows=('face1', 'face2'), npan=4, ngl=10)
    f1v = F1_0 + DF1_WD*wd + DF1_WO*wo + DF1_A*(a - A0); f2v = F2_0 + DF2_WO*wo + DF2_A*(a - A0)
    f1 = L9.NS*Xs['face1'] + L9.ND*Xd['face1'] + L9.NV*f1v
    f2 = L9.NS*Xs['face2'] + L9.ND*Xd['face2'] + L9.NV*f2v
    R = np.array([t[0], t[1], t[2], L9.ND*F[3], f1, f2])
    if r > 0:
        R += 12*r**4*np.array([Ccorner('T2g', a, wd, wo), Ccorner('Eg', a, wd, wo), 0, 0, Ccorner('face1', a, wd, wo), Ccorner('face2', a, wd, wo)])
    return R

# fixed Jacobian
Jax = np.array([[-5.6655e-04, 1.1701e-01, 8.2232e-03, 1.3886e+01], [-3.4987e-04, 7.8186e-02, 4.6650e-02, 1.3412e+01],
                [3.0830e-02, -5.6584e-01, 3.1372e-01, 0.0], [0.0, -3.2764e-02, 6.2509e-02, 0.0]])   # r199_jac_refroot.out
J = np.zeros((6, 6)); J[:4, :4] = Jax; J[4:, :4] = JF
J[4:, 4:] = 12*np.array([[DF1_WD, DF1_WO], [0.0, DF2_WO]])
print('J (rows T2g, Eg, muE, muT2, face1, face2; cols b_s, b_f, r_D, a, w_d, w_o):\n', np.array2string(J, precision=4), '\n det %.4e, singular values %s' % (np.linalg.det(J), np.linalg.svd(J, compute_uv=False)), flush=True)
x0 = np.r_[x_ax0, -1.17155412, -0.19541845]
sols = {}
for r in [0.0] + [float(v) for v in (sys.argv[1].split(',') if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else ['0.05', '0.1'])]:
    x = x0.copy()
    for it in range(6):
        R = rows(x, r)
        print(f'  r={r:<5} it {it}: x = ({", ".join(f"{v:.10f}" for v in x)}) rows {np.array2string(R, precision=3)} max|.| {np.abs(R).max():.2e} [{time.time()-t0:.0f}s]', flush=True)
        if np.abs(R).max() < 1e-10: break
        x = x - np.linalg.solve(J, R)
    sols[r] = (x, R)
x_ref = sols[0.0][0]
print('\nSUMMARY (model rows at stated resolution; r = 0 is the O(q)-convention root of the same model):')
for r, (x, R) in sols.items():
    print(f'  r = {r:<5}: knobs ({", ".join(f"{v:+.10f}" for v in x)}) | all six rows max|.| {np.abs(R).max():.1e} | shift vs r=0: {np.array2string(x - x_ref, precision=3)}')
np.save('resolve_sols.npy', np.array([np.r_[r, x, R] for r, (x, R) in sols.items()]))
print(f'time {time.time()-t0:.0f} s')
