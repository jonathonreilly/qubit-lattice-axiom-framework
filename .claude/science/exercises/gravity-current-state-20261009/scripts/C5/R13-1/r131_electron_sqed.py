"""R13-1 (c): one-loop c_e - c_gamma in minimal N=1 box SQED on Z^3 x R (electron, 2 selectrons, photon, photino).

Content (free level matched by the untwisted spinor supercharge, report section 3.1):
  electron  h_e(k) = sum_j S(k_j) alpha_j + beta M(k), M = m + sum_j W(k_j)      (R8-5 BQ; r = 0 literal, r > 0 gapped)
  selectrons phi_L, phi_R: eps(k) = E_e(k); scalar gauging factorized (r131_photon_sqed.py)
  photon: R8-5's box photon, omega^2 = sum_j d(q_j)^2, d = rho_g q + (1-rho_g) 2 sin(q/2)      (doubler-free)
  photino: Majorana, 4-comp form h_l(q) = sum_j Sg(q_j) alpha_j + beta Wl(q), Sg = rho_g q + (1-rho_g) sin q,
           Wl = sqrt(sum_j [d(q_j)^2 - Sg(q_j)^2])  ->  E_l(q) = omega(q) exactly (matched, doubler-free)
  Yukawa (N=1 SQED): y [phi_L^* lambdabar P_L psi + phi_R^* lambdabar P_R psi] + h.c.,  y^2 = 2 e^2  (constant vertex:
           the D1-supersymmetric value, continued unchanged to the whole zone -- a CHOICE off D1).
One-loop electron speed: photon loop (R8-5 fermion(), Feynman gauge, photon mass lam = m) + selectron-photino loop
(R10-5 old-fashioned PT, normal + Z graphs, adapted to 4x4 Dirac matrices; average over the 2 positive states).
Photon speed: Dirac loop + 2 selectron loops (r131_photon_sqed.selectron).  All x 16 pi^2 per e^2.
"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r85_box_qed_copy import Law, photon, fermion, plateau
from r131_photon_sqed import selectron

U = 16 * np.pi ** 2
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
alpha = [np.block([[Z2, sj], [sj, Z2]]) for sj in s]
beta = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
g5 = np.block([[Z2, I2], [I2, Z2]]).astype(complex)
assert all(np.allclose(g5 @ a, a @ g5) for a in alpha) and np.allclose(g5 @ beta, -beta @ g5)
PL, PR = (np.eye(4) - g5) / 2, (np.eye(4) + g5) / 2

def photino_funcs(law):
    def Sg(q):
        rg = plateau(q, law.c1, law.c2)
        return rg * q + (1 - rg) * np.sin(q)
    return Sg

def he(law, k):
    out = (law.m + law.W(np.array(k[0])) + law.W(np.array(k[1])) + law.W(np.array(k[2]))) * beta
    for j in range(3):
        out = out + law.S(np.array(k[j])) * alpha[j]
    return out

def dE_partner(law, p, N, axis=0, dm2=0.0):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Sg = photino_funcs(law)(k); d = law.d(k)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    I = [IX, IY, IZ]
    Wl = np.sqrt(np.maximum(d[IX] ** 2 - Sg[IX] ** 2, 0) + np.maximum(d[IY] ** 2 - Sg[IY] ** 2, 0)
                 + np.maximum(d[IZ] ** 2 - Sg[IZ] ** 2, 0))
    El = np.sqrt(Sg[IX] ** 2 + Sg[IY] ** 2 + Sg[IZ] ** 2 + Wl ** 2)        # = omega(q) exactly
    # selectron at p - k, p along 'axis'
    pv = [0.0, 0.0, 0.0]; pv[axis] = p
    comp = []
    for j in range(3):
        kk = pv[j] - k
        comp.append((law.S(kk), law.W(kk)))
    Sx = [comp[j][0][I[j]] for j in range(3)]
    Ms = law.m + comp[0][1][IX] + comp[1][1][IY] + comp[2][1][IZ]
    eps = np.sqrt(Sx[0] ** 2 + Sx[1] ** 2 + Sx[2] ** 2 + Ms ** 2 + dm2)
    H = he(law, pv)
    w, V = np.linalg.eigh(H)
    Pe = V[:, 2:] @ V[:, 2:].conj().T
    Ep = w[-1]
    tot = 0.0
    for Y in (beta @ PL, beta @ PR):
        Xm = Y @ Pe @ Y.conj().T
        trX = np.trace(Xm).real
        ta = [np.trace(alpha[j] @ Xm).real for j in range(3)]; tb = np.trace(beta @ Xm).real
        c = Sg[IX] * ta[0] + Sg[IY] * ta[1] + Sg[IZ] * ta[2] + Wl * tb
        tp = 0.5 * (trX + c / El); tm = 0.5 * (trX - c / El)
        tot += np.mean(tp / (2 * eps * (Ep - El - eps)) + tm / (2 * eps * (Ep + El + eps)))
    return Ep, tot / 2

def dc_partner(law, N, h=0.02, axis=0, dm2=0.0):
    E0, d0 = dE_partner(law, 0.0, N, axis, dm2)
    vals = []
    for hh in (h, 2 * h):
        Ep, d = dE_partner(law, hh, N, axis, dm2)
        vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2

if __name__ == '__main__':
    t0 = time.time()
    shapes = [('S1', 1.0, 2.0), ('S3', 2.0, 3.0), ('S5', 0.5, 1.5), ('S7', 1.0, 3.0)]
    runs = [(0.2, 64), (0.2, 96)] if len(sys.argv) < 2 else [(float(sys.argv[1]), int(sys.argv[2]))]
    print('minimal N=1 box SQED, one loop, x16pi^2 per e^2 (y^2 = 2e^2):')
    print('shape | r | m | N | dc_gamma (Dirac+2sel) | dc_e photon loop | dc_e partner (2 sel, y^2=2e^2) | [axis-y check] | dc_e total | DELTA = dc_e - dc_gamma')
    for lab, b1, b2 in shapes:
        for r in (0.0, 1.0):
            for (m, N) in runs:
                law = Law(b1, b2, r, b1, b2, m)
                ph = photon(law, N); dS, _ = selectron(law, N)
                dcg = ph['dcg'] + 2 * dS
                fe = fermion(law, N, m)
                pa = 2.0 * dc_partner(law, N)
                pay = 2.0 * dc_partner(law, N, axis=1) if N == 64 else float('nan')
                dce = fe['dce'] + pa
                print('%s | %.1f | %.2f | %3d | %+9.4f | %+9.4f | %+9.4f | [%+9.4f] | %+9.4f | %+9.4f' % (
                    lab, r, m, N, U * dcg, U * fe['dce'], U * pa, U * pay, U * dce, U * (dce - dcg)), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
