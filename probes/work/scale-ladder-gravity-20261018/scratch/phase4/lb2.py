# non-static Euclidean exchange: fit alpha T.T + beta trT trT on conserved tensors at generic k (k_t != 0)
from common import *
SYM = [(a, b) for a in range(4) for b in range(a, 4)]
def cons_basis(k):
    # symmetric T with T k = 0: null space of the map T -> T k (10 -> 4)
    A = np.zeros((4, 10))
    for j, (a, b) in enumerate(SYM):
        E = np.zeros((4, 4)); E[a, b] = E[b, a] = 1; A[:, j] = E @ k
    N = np.linalg.svd(A)[2][4:]
    out = []
    for v in N:
        T = np.zeros((4, 4))
        for j, (a, b) in enumerate(SYM): T[a, b] = T[b, a] = v[j]
        out.append(T)
    return out
dirs = {'static axis': [0, 1, 0, 0], 'tick axis': [0, 0, 0, 1], 'tick-space face': [0, 1, 0, 1], 'generic': [0.3, -0.5, 0.6, 0.55], 'generic2': [0.7, 0.2, -0.4, -0.45]}
for nm, d in dirs.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    for s in (0.04, 0.02, 0.01):
        k = s * d; Q = Dc.Q(k); L = strain_metric(Dc, k); Qp = np.linalg.pinv(Q, rcond=1e-11); P2 = partners(k, Q)
        K = L @ Qp @ L.conj().T; Kp = L @ (P2 @ P2.conj().T) @ Qp @ (P2 @ P2.conj().T) @ L.conj().T
        Ts = cons_basis(k); C = np.array([cvec(T) for T in Ts])
        M = (C @ K @ C.T) * s * s; Mp = (C @ Kp @ C.T) * s * s
        X = np.array([[np.sum(Ti * Tj), np.trace(Ti) * np.trace(Tj)] for Ti in Ts for Tj in Ts])
        coef, res, *_ = np.linalg.lstsq(X, M.real.ravel(), rcond=None); a, b = coef
        resid = np.linalg.norm(X @ coef - M.real.ravel()) / np.linalg.norm(M.real.ravel())
        G = Dc.gauge(k); ward = np.linalg.norm(C @ L @ G) / np.linalg.norm(C @ L)
        print(f"{nm:16s} |k|={s:.2f}: alpha {a:+.5f} beta {b:+.5f} beta/alpha {b/a:+.5f} fit resid {resid:.1e} |Im| {np.abs(M.imag).max():.0e}; partner part max {np.abs(Mp).max():.1e}; |partner reading| {np.linalg.norm(L@P2,axis=0).max():.1e}; Ward |cLG|/|cL| {ward:.1e}")
