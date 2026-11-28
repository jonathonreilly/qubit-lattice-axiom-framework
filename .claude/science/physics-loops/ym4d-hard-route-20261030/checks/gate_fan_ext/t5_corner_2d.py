#!/usr/bin/env python3
"""T5: optimal extension, d = 2, Omega three quarters of 2 x 2 parents. See CRITERIA.md."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
from t2_opt_extension import watchdog, lap

def run(L, P=2, steps=60):
    n = P * L; a = 1.0 / L; d = 2
    idx = np.arange(n * n).reshape(n, n)
    X, Z = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    x, z = X - n // 2 + .5, Z - n // 2 + .5
    om = (~((z < 0) & (x > 0))).ravel()
    E = np.concatenate([np.stack([idx[:-1, :].ravel(), idx[1:, :].ravel()], 1), np.stack([idx[:, :-1].ravel(), idx[:, 1:].ravel()], 1)])
    par = (X // L + P * (Z // L)).ravel()
    N = n * n; w0, w1 = a ** d, a ** (d - 2)
    A = (w0 * sp.identity(N) + w1 * lap(N, E)).tocsr()
    both = om[E[:, 0]] & om[E[:, 1]]
    Gf = (w0 * sp.diags(om.astype(float)) + w1 * lap(N, E, both)).tocsr()
    iO, iY = np.where(om)[0], np.where(~om)[0]
    AOO, AOY, AYY, GOO = A[iO][:, iO].tocsc(), A[iO][:, iY].tocsc(), A[iY][:, iY].tocsc(), Gf[iO][:, iO].tocsc()
    def means(ix):
        u, inv = np.unique(par[ix], return_inverse=True)
        return sp.csc_matrix((np.ones(len(ix)), (inv, np.arange(len(ix)))), shape=(len(u), len(ix)))
    CO, CY = means(iO), means(iY)
    luY = sla.splu(sp.bmat([[AYY, CY.T], [CY, None]], format="csc"))
    luO = sla.splu(sp.bmat([[GOO, CO.T], [CO, None]], format="csc"))
    def S(u):
        w = luY.solve(np.concatenate([-(AOY.T @ u), np.zeros(CY.shape[0])]))[:len(iY)]
        return AOO @ u + AOY @ w
    G = lambda r: luO.solve(np.concatenate([r, np.zeros(CO.shape[0])]))[:len(iO)]
    v = G(np.random.default_rng(7).standard_normal(len(iO))); v /= np.sqrt(v @ (GOO @ v))
    V, al, be = [v], [], []
    for k in range(steps):
        w = G(S(V[-1]))
        for _ in range(2):
            for u in V:
                w -= (w @ (GOO @ u)) * u
        w = G(GOO @ w)
        al.append(V[-1] @ S(V[-1]))
        nb = np.sqrt(max(w @ (GOO @ w), 0.0))
        if nb < 1e-10: break
        be.append(nb); V.append(w / nb)
    m = len(al)
    return np.linalg.eigvalsh(np.diag(al) + np.diag(be[:m - 1], 1) + np.diag(be[:m - 1], -1))[-1]

if __name__ == "__main__":
    watchdog()
    r = {}
    for L in (4, 8, 16, 32, 64, 128, 256):
        r[L] = run(L); print("L", L, "A =", round(r[L], 4), flush=True)
    ok = max(r.values()) <= 4.5 and r[256] - r[128] < r[16] - r[8]
    print("T5", "PASS" if ok else "FAIL")
