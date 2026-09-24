"""Supervisor control for block 103: on block 42's SIX-AXIS menu the ordered sea has no massless turn (a discrete menu
has no one-parameter family of turned solutions). Ordered uniform fixed point F = (K1 F)^6/<(K1 F)^6> on the six
contents, lean along +e3; per-neighbour linearization eta -> K1(F eta)/g - <.>_F; eigenvalues by sector."""
import numpy as np
E = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)


def run(p, q, r):
    T = p + q + 4 * r
    W = np.array([[p if np.allclose(a, b) else q if np.allclose(a, -b) else r for b in E] for a in E], float)
    K = W / T  # stochastic: rows sum to 1 (uniform average of the neighbour's distribution weighted by omega/T*6/6)
    F = np.array([1, 1, 1, 1, 1.5, 0.5])
    F /= F.mean()
    for _ in range(100000):
        g = K @ F
        Fn = g ** 6
        Fn /= Fn.mean()
        if np.abs(Fn - F).max() < 1e-15:
            F = Fn
            break
        F = Fn
    g = K @ F
    A = K * F[None, :] / g[:, None]
    Q = A - np.outer(np.ones(6), (F / 6) @ A)
    ev, V = np.linalg.eig(Q)
    tilt = np.array([1, -1, 0, 0, 0, 0.0])  # the lean tipping toward e1
    lam_tilt = (Q @ tilt) @ tilt / (tilt @ tilt)
    resid = np.abs(Q @ tilt - lam_tilt * tilt).max()
    lean = (F / 6) @ E[:, 2]
    l1 = (p - q) / T
    return 6 * l1, lean, 6 * lam_tilt, resid, sorted(6 * ev.real)[::-1]


for pqr in [(12, 1, 2), (6, 1, 2), (4, 1, 2), (3.2, 1, 2), (30, 1, 2), (12, 1, 6)]:
    s6, lean, t6, res, evs = run(*pqr)
    m2 = (1 - t6) / (t6 / 6)
    print(f"(p,q,r)={pqr}: 6 lambda1 = {s6:.4f}; lean {lean:.4f}; tilt sector 6mu = {t6:.6f} (eigenvector residual {res:.0e}), mass^2 = {m2:.4f}; all 6mu: " + " ".join(f"{e:.4f}" for e in evs))
