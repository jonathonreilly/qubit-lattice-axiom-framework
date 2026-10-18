import sys, numpy as np
sys.path.insert(0, '.')
from d4t import readings, C, HC
cls = np.array([0]*4 + [1]*12 + [2]*8); wrel = np.array([1, 1/4, 1/16])[cls]
itt, ixx, iyy = HC.index((3, 3)), HC.index((0, 0)), HC.index((1, 1))
def Lrel(k):
    R, D = readings(k); W = np.diag(np.sqrt(wrel)); return np.linalg.pinv(W @ D) @ (W @ R)
for kk in [np.array([0, 0.04, 0, 0.0]), np.array([0, 0.02, 0, 0.0]), np.array([0, 0.01, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0]), np.array([0, 0.006, 0.0045, 0.0]), np.array([0, 0.3, 0.2, 0.0])]:
    Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    A = np.hstack([C.line_map(kk), C.gauge(kk)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    Lk = Lrel(kk); T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
    gov = np.linalg.norm(C.gauge(kk).conj().T @ J)/np.linalg.norm(J)
    x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x); k2 = kk @ kk
    h = Lk @ x; hp = Lk @ xp
    print(f"|k|={np.sqrt(k2):.4f}: null overlap {gov:.0e}; |L partners| {np.round(np.linalg.norm(Lk @ partners, axis=0), 5)}; h_tt k^2 {h[itt].real*k2:+.5f} (partner {hp[itt].real*k2:+.1e}); h_xx/h_tt {(h[ixx]/h[itt]).real:+.5f}")
