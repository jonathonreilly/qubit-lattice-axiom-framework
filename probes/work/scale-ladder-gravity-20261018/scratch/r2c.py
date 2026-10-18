import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from r2 import R2
from d4q import Lsym, HC
OFF, S = RG.kuhn(); K = RG.Complex(OFF, S); D = pickle.load(open('d4.pkl', 'rb'))
itt, ixx = HC.index((3, 3)), HC.index((0, 0))
def comp_inv(Q, G, J):
    """solve Q x = J on the complement of the gauge directions G (exact null space)."""
    Pq, _ = np.linalg.qr(G); Pc = np.linalg.svd(np.eye(Q.shape[0]) - Pq @ Pq.conj().T)[0][:, :Q.shape[0] - G.shape[1]]
    return Pc @ np.linalg.solve(Pc.conj().T @ Q @ Pc, Pc.conj().T @ J)
for lam in (0.0, -0.1):
    for kk in [np.array([0, 0.04, 0, 0.0]), np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        k2 = kk @ kk
        # D4 cone with the face reading (which gave -2/3 partner contamination at lam = 0)
        Q = D.Q(kk) + lam*R2(D, kk); L = Lsym(kk); T = np.zeros(10); T[itt] = 1.0
        x = comp_inv(Q, D.gauge(kk), L.conj().T @ T); h = L @ x
        # Kuhn with the line-map source (fifth direction was sourced at lam = 0)
        Qk = K.Q(kk) + lam*R2(K, kk); M = K.line_map(kk); Jk = np.conj(M) @ T
        try:
            xk = comp_inv(Qk, K.gauge(kk), Jk); hk = np.linalg.lstsq(M, xk, rcond=None)[0]; kres = f"{hk[itt].real*k2:+.4f} (h_xx/h_tt {(hk[ixx]/hk[itt]).real:+.4f})"
        except np.linalg.LinAlgError:
            kres = "singular"
        print(f"lambda={lam:+.1f} |k|={np.sqrt(k2):.3f}: D4 face reading h_tt k^2 {h[itt].real*k2:+.4f} (h_xx/h_tt {(h[ixx]/h[itt]).real:+.4f}) | Kuhn line map h_tt k^2 {kres}")
