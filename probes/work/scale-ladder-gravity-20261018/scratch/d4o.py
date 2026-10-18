import sys, numpy as np
sys.path.insert(0, '.')
from d4m import L, C, HC
k = np.array([0.02, 0.0, 0.0, 0.0]) * np.array([1, 1, 1, 1]); k = np.array([0.012, -0.009, 0.013, 0.0])
Q = C.Q(k); Qh = 0.5*(Q + Q.conj().T); w, V = np.linalg.eigh(Qh); idx = np.argsort(np.abs(w)); V = V[:, idx]; w = w[idx]
M = C.line_map(k); G = C.gauge(k); A = np.hstack([M, G]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
soft = V[:, 32:40]                                   # 8 massless non-gauge
u, s, vh = np.linalg.svd(P @ soft); partners = u[:, :2]
Lk = L(k)
print("|L partner| per partner (vs |L| on unit metric modes ~1):", np.round(np.linalg.norm(Lk @ partners, axis=0), 4))
print("L-metric content of the partners modulo gauge (h components):")
for j in range(2):
    h = Lk @ partners[:, j]; print("  ", np.round(h/np.max(np.abs(h)), 3))
# response decomposition: static T_tt through L, projected on partners vs the rest of the soft space
itt = HC.index((3, 3)); T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
x = np.linalg.pinv(Q, rcond=1e-11) @ J
cp = partners.conj().T @ x; xp = partners @ cp
print(f"h_tt k^2 total {np.real((Lk@x)[itt])*np.dot(k,k):+.4f}; partner contribution {np.real((Lk@xp)[itt])*np.dot(k,k):+.4f}; rest {np.real((Lk@(x-xp))[itt])*np.dot(k,k):+.4f}")
