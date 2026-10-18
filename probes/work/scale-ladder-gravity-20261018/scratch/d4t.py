import sys, itertools, numpy as np
sys.path.insert(0, '.')
from d4q import C, HC, eidx, hole_type
from d4s import body_reading, SIGNS
pairs = list(itertools.combinations(range(4), 2)); E = np.eye(4, dtype=int); Z = (0,0,0,0)
def readings(k):
    """rows = measured delta(l^2) for 24 site-site segments; cols = edge variables. Also the design matrix in h."""
    k = np.asarray(k, complex); R = []; D = []
    def seg(parts, coef):
        r = np.zeros(C.E, complex)
        for (p, q) in parts:
            c, anc = eidx(p, q); r[c] += coef*np.exp(1j*k @ anc)
        return r
    for mu in range(4):                                     # axis: l=1, delta(l^2) = 2 dl
        R.append(seg([((Z, 0), (tuple(E[mu]), 0))], 2.0)); v = E[mu].astype(float); D.append([v[a]*v[b]*(2 if a != b else 1) for a, b in HC])
    for h, (m, n) in enumerate(pairs):                      # face diagonals, l = sqrt2: delta(l^2) = 2 sqrt2 dl
        hv = (Z, 2+h)
        R.append(seg([((Z, 0), hv), (hv, (tuple(E[m]+E[n]), 0))], 2*np.sqrt(2))); v = (E[m]+E[n]).astype(float); D.append([v[a]*v[b]*(2 if a != b else 1) for a, b in HC])
        R.append(seg([((tuple(E[n]), 0), hv), (hv, (tuple(E[m]), 0))], 2*np.sqrt(2))); v = (E[m]-E[n]).astype(float); D.append([v[a]*v[b]*(2 if a != b else 1) for a, b in HC])
    B = body_reading(k); R += list(B)                       # body: l = 2, delta(l^2) = 4 dl  (already)
    for s in SIGNS: D.append([s[a]*s[b]*(2 if a != b else 1) for a, b in HC])
    return np.array(R), np.array(D, float)
R0, D = readings(np.zeros(4))
print("design rank", np.linalg.matrix_rank(D), "of 24 rows; constant-metric exactness:", np.abs(R0 @ C.line_map(np.zeros(4)) - D).max())
Lls = lambda k: np.linalg.pinv(D) @ readings(k)[0]          # least-squares metric (uniform weights on delta l^2)
for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0.012, -0.009, 0.013, 0.004])]:
    Q = C.Q(kk); w, V = np.linalg.eigh(0.5*(Q + Q.conj().T)); V = V[:, np.argsort(np.abs(w))]
    A = np.hstack([C.line_map(kk), C.gauge(kk)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    partners = np.linalg.svd(P @ V[:, 32:40])[0][:, :2]
    print(f"k={kk}: |L_LS partners| = {np.round(np.linalg.norm(Lls(kk) @ partners, axis=0), 4)}")
    itt, ixx = HC.index((3, 3)), HC.index((0, 0)); T = np.zeros(10); T[itt] = 1.0; Lk = Lls(kk); J = Lk.conj().T @ T
    x = np.linalg.pinv(Q, rcond=1e-11) @ J; xp = partners @ (partners.conj().T @ x); k2 = kk @ kk
    hg, hp = Lk @ (x - xp), Lk @ xp
    print(f"   static T_tt: graviton h_tt k^2 {hg[itt].real*k2:+.4f}; partner {hp[itt].real*k2:+.4f}; total h_xx/h_tt {((hg+hp)[ixx]/(hg+hp)[itt]).real:+.4f}")
