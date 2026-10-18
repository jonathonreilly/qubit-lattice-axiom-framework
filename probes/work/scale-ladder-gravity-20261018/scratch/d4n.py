import sys, numpy as np
sys.path.insert(0, '.')
from d4m import L, C, HC
itt = HC.index((3, 3))
for n in [(1,0,0), (1,1,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    row = []
    for km in (0.02, 0.5, 1.5):
        k = np.array([*(km*n), 0.0]); Q = C.Q(k); Lk = L(k)
        T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
        G = C.gauge(k); gres = np.linalg.norm(G.conj().T @ J)/np.linalg.norm(J)
        x = np.linalg.pinv(Q, rcond=1e-11) @ J; h = Lk @ x
        ph = np.sum(4*np.sin(km*n/2)**2)
        row.append(f"|k|={km}: h_tt k^2 {h[itt].real*km**2:+.5f}, h_tt phat^2 {h[itt].real*ph:+.5f} (gauge overlap {gres:.0e})")
    print(np.round(n, 2), "; ".join(row))
