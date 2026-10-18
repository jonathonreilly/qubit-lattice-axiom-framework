# same as lb2, but conserved = lattice-conserved for the strain reading: c . (L G_site) = 0 exactly
from common import *
SYM = [(a, b) for a in range(4) for b in range(a, 4)]
def T_of_c(c):
    T = np.zeros((4, 4), complex)
    for i, (a, b) in enumerate(HC): T[a, b] = T[b, a] = c[i] / (1 if a == b else 2)
    return T
dirs = {'static axis': [0, 1, 0, 0], 'tick-space face': [0, 1, 0, 1], 'generic': [0.3, -0.5, 0.6, 0.55], 'generic2': [0.7, 0.2, -0.4, -0.45], 'body': [1, 1, 1, 1]}
for nm, d in dirs.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    for s in (0.08, 0.04, 0.02, 0.01):
        k = s * d; Q = Dc.Q(k); L = strain_metric(Dc, k); Qp = Qinv(k, Q); P2 = partners(k, Q)
        K = L @ Qp @ L.conj().T; Pp = P2 @ P2.conj().T; Kp = L @ Pp @ Qp @ Pp @ L.conj().T
        G = Dc.gauge(k); W = L @ G[:, :4]                       # 10 x 4 lattice gradient symbol
        Cb = np.linalg.svd(W.T)[2][4:]                          # rows c with c @ W = 0  (6 x 10)
        Cb = Cb.conj()                                           # svd null rows of W.T: W.T v = 0 -> use v.conj? check below
        if np.abs(Cb @ W).max() > 1e-10: Cb = Cb.conj()
        assert np.abs(Cb @ W).max() < 1e-10
        Ts = [T_of_c(c) for c in Cb]
        M = (Cb.conj() @ K @ Cb.T) * s * s; Mp = (Cb.conj() @ Kp @ Cb.T) * s * s
        X = np.array([[np.sum(Ti.conj() * Tj), np.conj(np.trace(Ti)) * np.trace(Tj)] for Ti in Ts for Tj in Ts])
        coef = np.linalg.lstsq(X, M.ravel(), rcond=None)[0]; a, b = coef
        resid = np.linalg.norm(X @ coef - M.ravel()) / np.linalg.norm(M.ravel())
        print(f"{nm:16s} |k|={s:.2f}: alpha {a.real:+.5f} beta {b.real:+.5f} beta/alpha {(b/a).real:+.5f} fit resid {resid:.1e}; partner part {np.abs(Mp).max()/np.abs(M).max():.1e}")
