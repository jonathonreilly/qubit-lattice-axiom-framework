import sys, numpy as np
sys.path.insert(0, '.')
from d4q import Lsym, C, HC
itt, ixx, iyy, izz = HC.index((3, 3)), HC.index((0, 0)), HC.index((1, 1)), HC.index((2, 2))
for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
    Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    M = C.line_map(kk); Gk = C.gauge(kk); A = np.hstack([M, Gk]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    Lk = Lsym(kk); T = np.zeros(10); T[itt] = 1.0; J = Lk.conj().T @ T
    x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x); xg = x - xp
    hg, hp = Lk @ xg, Lk @ xp
    print(f"k={kk}: graviton h_tt {hg[itt].real:+.2f} h_xx {hg[ixx].real:+.2f} (gamma {hg[ixx].real/hg[itt].real:+.4f}); partner h_tt {hp[itt].real:+.2f} h_xx {hp[ixx].real:+.2f} (ratio {hp[ixx].real/hp[itt].real:+.4f}); total gamma {(hg+hp)[ixx].real/(hg+hp)[itt].real:+.4f}")
    print("   partner site-metric pattern (h/h_tt):", np.round((hp/hp[itt]).real, 3))
