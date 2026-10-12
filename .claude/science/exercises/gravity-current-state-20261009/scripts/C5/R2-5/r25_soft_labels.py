"""R2-5 check 8 (route P3): SOFT direction-labelled records that are reflection positive.
Single column, values B (blank), U (+t record), D (-t record).  Time-bond weights w0(a, b):
  B->B 1, B->U f (U tail = formation), B->D e1 (D without D below),
  U->B e1 (U without U above = un-formation), U->U 1, U->D e (label clash),
  D->B f (D tail; theta image of B->U), D->U x (turning point), D->D 1.
theta (t -> -t, U <-> D) covariance: w0(a, b) = w0(theta b, theta a).  Bond-RP <=> M(a', b) =
w0(theta a', b) PSD.  Choice: f = r, e = u/r, e1 = u, x = (1 + eta)/e  -> det M = eta(1 - r u) > 0.
In 1+1 / 3+1 the spatial labels (R, L, ...) have all-1 weights against B, U, D across time bonds
except the tail/end entries; among {B, U, D} the spatial weights are all 1 (rotation images), so
columns decouple when no spatial-labelled records are present; those need two spatial ends
(weight f * e1 = r u per segment) and are dropped here (reported as a bound).
Half-line: blank boundary at t = 0, free top, T steps; exact forward-backward.
Reported: eig(M), record density m(t), formation per blank site per step, un-formation per
record per step, net arrow, and the strict limit u -> 0 (x -> infinity) for comparison.
"""
import numpy as np
B, U, D = 0, 1, 2
th = [B, D, U]
def law(r, u, eta):
    f, e, e1 = r, u / r, u
    x = (1 + eta) / e
    w = np.array([[1.0, f, e1], [e1, 1.0, e], [f, x, 1.0]])
    for a in range(3):
        for b in range(3):
            assert abs(w[a, b] - w[th[b], th[a]]) < 1e-15 * max(1, w[a, b])
    M = w[th, :]
    return w, M
def halfline(w, T):
    n = 3
    alpha = [np.array([1.0, 0, 0])]
    for t in range(1, T + 1):
        a = alpha[-1] @ w; alpha.append(a / a.sum())
    beta = [None] * (T + 1); beta[T] = np.ones(n)
    for t in range(T - 1, -1, -1):
        b = w @ beta[t + 1]; beta[t] = b / b.sum()
    m, fr, ur, flip = [], [], [], []
    for t in range(T):
        P = alpha[t][:, None] * w * beta[t + 1][None, :]; P /= P.sum()
        pB = P[B].sum(); pR = P[U].sum() + P[D].sum()
        fr.append((P[B, U] + P[B, D]) / max(pB, 1e-300))
        ur.append((P[U, B] + P[D, B]) / max(pR, 1e-300))
        m.append(pR)
    return np.array(m), np.array(fr), np.array(ur)
if __name__ == "__main__":
    for r, u, eta in ((1e-2, 1e-6, 0.1), (1e-3, 1e-8, 0.1), (1e-3, 1e-10, 1.0)):
        w, M = law(r, u, eta)
        ev = np.linalg.eigvalsh(M)
        T = int(8 / r)
        m, fr, ur = halfline(w, T)
        k = T // 4
        print(f"r={r:.0e} u={u:.0e} eta={eta}: eig(M) = {ev}  (min >= 0: {ev.min() >= -1e-12*abs(ev).max()})")
        print(f"   T={T}: m(1)={m[1]:.3e} m(T/4)={m[k]:.3f} m(T/2)={m[T//2]:.3f}; formation per blank site-step at T/4 = {fr[k]:.3e} (2r={2*r:.1e}); "
              f"un-formation per record-step at T/4 = {ur[k]:.3e} (2u={2*u:.1e}); at T/2: {ur[T//2]:.3e}")
    # strict limit: u -> 0 forces x -> infinity (unbounded weight) or loses RP
    for u in (1e-6, 1e-12, 0.0):
        r = 1e-3
        if u == 0.0:
            w = np.array([[1.0, r, 0.0], [0.0, 1.0, 0.0], [r, 1e30, 1.0]])
            M = w[th, :]
            print(f"strict u=0 with finite x=1e30: eig(M) = {np.linalg.eigvalsh(M)} -> not PSD (M[D,D] = w(U,D) = 0 forces row M[D,:] = w(U,:) = 0)")
        else:
            print(f"u={u:.0e}: required turning weight x = (1+eta) r/u = {1.1*r/u:.1e}")
