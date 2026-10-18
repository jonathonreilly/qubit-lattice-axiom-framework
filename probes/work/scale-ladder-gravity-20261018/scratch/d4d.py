import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('d4.pkl', 'rb'))
def soft_space(k, n=40):
    Q = C.Q(k); Q = 0.5*(Q + Q.conj().T); w, V = np.linalg.eigh(Q); idx = np.argsort(np.abs(w))
    return V[:, idx[:n]]   # 32 gauge + 8 soft
for s in (0.05, 0.01):
    k = s*np.array([0.3, -0.5, 0.6, 0.55])/np.linalg.norm([0.3, -0.5, 0.6, 0.55])
    V = soft_space(k); A = np.hstack([C.line_map(k), C.gauge(k)])
    P = A @ np.linalg.pinv(A, rcond=1e-10)
    out = np.linalg.svd((np.eye(C.E) - P) @ V, compute_uv=False)
    print(f"s={s}: components of the 40-dim soft space outside im M + im G (singular values):", " ".join(f"{x:.2e}" for x in out[:4]))
