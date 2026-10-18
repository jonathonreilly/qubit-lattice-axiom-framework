import sys, numpy as np
sys.path.insert(0, '.')
from d4t import readings, C, HC
kk = np.array([0, 0.02, 0, 0.0]); R, D = readings(kk); cls = np.array([0]*4 + [1]*12 + [2]*8)
Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
A = np.hstack([C.line_map(kk), C.gauge(kk)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
itt, ixx = HC.index((3, 3)), HC.index((0, 0))
def run(wts):
    W = np.diag(np.sqrt(np.array([wts[c] for c in cls])))
    Lk = np.linalg.pinv(W @ D) @ (W @ R)
    T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
    x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x); k2 = kk @ kk
    hg, hp = Lk @ (x - xp), Lk @ xp
    return hp[itt].real*k2, ((hg+hp)[ixx]/(hg+hp)[itt]).real, np.linalg.norm(Lk @ partners, axis=0)
for name, wts in {'uniform in delta l^2': (1, 1, 1), 'relative strain (1/l^4)': (1, 1/4, 1/16), 'equal per class': (1/4, 1/12, 1/8), 'axis+face only': (1, 1, 0), 'axis+body only': (1, 0, 1)}.items():
    pp, g, nrm = run(wts); print(f"{name:26s}: partner h_tt k^2 {pp:+.4f}; total h_xx/h_tt {g:+.4f}; |L partners| {np.round(nrm,3)}")
# solve for the body weight that decouples (axis = face = 1)
lo, hi = 0.0, 50.0
f = lambda b: run((1, 1, b))[0]
for _ in range(60):
    mid = 0.5*(lo+hi)
    if f(lo)*f(mid) <= 0: hi = mid
    else: lo = mid
pp, g, nrm = run((1, 1, 0.5*(lo+hi))); print(f"decoupling body weight (axis = face = 1): {0.5*(lo+hi):.6f}; partner {pp:+.2e}; total h_xx/h_tt {g:+.6f}; |L partners| {np.round(nrm,4)}")
