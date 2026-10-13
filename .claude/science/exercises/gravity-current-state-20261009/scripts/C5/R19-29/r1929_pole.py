"""R19-29 (b) check: exact A_1 face pole of s*K_EH(omega, q) - eps*Pi(omega, q) for the root scalar edge (U, E1, P1,
ultralocal seagull with total degree-0 block lam_b (tr h)^2), against row and row - Schur.
K_EH from R19-23's kernels.py (unchanged), evaluated at p = (-omega, q) so that it annihilates g = p x xi + xi x p.
usage: python r1929_pole.py m N"""
import sys, numpy as np
from a1lib import *
import kernels as KR
m = float(sys.argv[1]); N = int(sys.argv[2])
law, z = root_scalar_law(); sc = Scalar(law, m, N)
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]
H00 = np.outer(t4, t4); H0n = 0.5*(np.outer(t4, nx) + np.outer(nx, t4))
BAS = [E1F, H00, H0n, NN, TRP]
def Kmat(w, q):
    p = np.r_[-w, q]; K = KR.kernel(0*KR.Ab[0], KR.Beh, p)
    return KR.s_EH*np.array([[np.einsum('ij,ijkl,kl->', A, K, B) for B in BAS] for A in BAS])
q = 0.02; qv = q*n3
# check: K annihilates my gauge directions; TT normalization
Kq = KR.kernel(0*KR.Ab[0], KR.Beh, np.r_[-0.7*q, qv])
for xi, nm in ((t4, 'g0'), (nx, 'gn')):
    g = gauge(xi, 0.7*q, qv); print('K_EH . %s residual %.1e' % (nm, np.abs(np.einsum('ijkl,kl->ij', Kq, g)).max()))
print('TT normalization e1.(sK).e1 at (w, q) = (0.7q, q): %.6e vs w^2 - q^2 = %.6e' % (KR.s_EH*np.einsum('ij,ijkl,kl->', E1F, Kq, E1F), (0.49-1)*q*q))
for lam in (0.0, 1e-2):
    S = ultralocal_seagull(sc, lam)
    Pi = lambda w: sc.block(qv, w, BAS, seagull=S)
    for eps in (1e-6, 1e-7):
        f = lambda w2: np.linalg.det((Kmat(np.sqrt(w2), qv) - eps*Pi(np.sqrt(w2)))/(eps*q*q))
        # secant in w^2 near q^2 + eps*q^2*guess
        P = sc.block(qv, q, [E1F, gauge(t4, q, qv), gauge(nx, q, qv)], seagull=S)
        sch = P[0, 1:] @ np.linalg.solve(P[1:, 1:], P[0, 1:])
        x0 = q*q + eps*(P[0, 0] - sch); x1 = x0*(1 + 1e-9) + eps*q*q*1e-3
        f0, f1 = f(x0), f(x1)
        for it in range(40):
            x2 = x1 - f1*(x1 - x0)/(f1 - f0)
            x0, f0, x1, f1 = x1, f1, x2, f(x2)
            if abs(x1 - x0) < 1e-16*q*q: break
        P0 = sc.block(0*qv, 0.0, [E1F], seagull=S)[0, 0]
        print('lam_b=%g eps=%.0e q=%.3f: pole (w^2-q^2)/(eps q^2) = %+.6e | row Pi_11(q,q)/q^2 = %+.6e | (Pi_11 - Schur)/q^2 = %+.6e | Pi_11(0,0) = %+.1e'
              % (lam, eps, q, (x1 - q*q)/(eps*q*q), P[0, 0]/q**2, (P[0, 0] - sch)/q**2, P0))
