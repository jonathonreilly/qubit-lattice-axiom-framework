#!/usr/bin/env python3
"""T6: edge pattern against the balanced fan, literal control, top mode location. See CRITERIA.md."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
import t2_opt_extension as t

_build = t.build
def build(L, pattern):
    if pattern != "edge":
        return _build(L, pattern)
    n, a, om, E, par = _build(L, "flat")
    X, Y, Z = np.meshgrid(*[np.arange(n)] * 3, indexing="ij")
    x, z = (X - n // 2 + .5), (Z - n // 2 + .5)
    return n, a, (((z < 0) & (x < 0)) | (z > 0)).ravel(), E, par
t.build = build

def mode(L):
    n, a, om, E, par = _build(L, "fan")
    N = n ** 3; d = 3; w0, w1 = a ** d, a ** (d - 2)
    A = (w0 * sp.identity(N) + w1 * t.lap(N, E)).tocsr()
    both = om[E[:, 0]] & om[E[:, 1]]
    Gf = (w0 * sp.diags(om.astype(float)) + w1 * t.lap(N, E, both)).tocsr()
    iO, iY = np.where(om)[0], np.where(~om)[0]
    AOO, AOY, AYY, GOO = A[iO][:, iO].tocsc(), A[iO][:, iY].tocsc(), A[iY][:, iY].tocsc(), Gf[iO][:, iO].tocsc()
    def means(ix):
        u, inv = np.unique(par[ix], return_inverse=True)
        return sp.csc_matrix((np.ones(len(ix)), (inv, np.arange(len(ix)))), shape=(len(u), len(ix)))
    CO, CY = means(iO), means(iY)
    luY = sla.splu(sp.bmat([[AYY, CY.T], [CY, None]], format="csc"))
    luO = sla.splu(sp.bmat([[GOO, CO.T], [CO, None]], format="csc"))
    def ext(u):
        return luY.solve(np.concatenate([-(AOY.T @ u), np.zeros(CY.shape[0])]))[:len(iY)]
    S = lambda u: AOO @ u + AOY @ ext(u)
    G = lambda r: luO.solve(np.concatenate([r, np.zeros(CO.shape[0])]))[:len(iO)]
    v = G(np.random.default_rng(7).standard_normal(len(iO))); v /= np.sqrt(v @ (GOO @ v))
    V, al, be = [v], [], []
    for k in range(40):
        w = G(S(V[-1]))
        for _ in range(2):
            for u in V:
                w -= (w @ (GOO @ u)) * u
        w = G(GOO @ w)
        al.append(V[-1] @ S(V[-1]))
        nb = np.sqrt(w @ (GOO @ w)); be.append(nb); V.append(w / nb)
    m = len(al)
    ev, y = np.linalg.eigh(np.diag(al) + np.diag(be[:m - 1], 1) + np.diag(be[:m - 1], -1))
    u = sum(y[i, -1] * V[i] for i in range(m))
    full = np.zeros(N); full[iO] = u; full[iY] = ext(u)
    de = w1 * (full[E[:, 0]] - full[E[:, 1]]) ** 2
    dens = w0 * full ** 2
    np.add.at(dens, E[:, 0], de / 2); np.add.at(dens, E[:, 1], de / 2)
    X, Y, Z = np.meshgrid(*[np.arange(n)] * 3, indexing="ij")
    x, y_, z = [((c - n // 2 + .5) * a).ravel() for c in (X, Y, Z)]
    Ym = ~om
    tot = dens[Ym].sum()
    out = {"A": ev[-1], "Y/Om": tot / dens[om].sum()}
    for r in (1 / 8, 1 / 4, 1 / 2):
        vtx = np.maximum.reduce([abs(x), abs(y_), abs(z)]) < r
        ed = (np.maximum(abs(x), abs(z)) < r) | (np.maximum(abs(y_), abs(z)) < r)
        out[f"vertex<{r}"] = dens[Ym & vtx].sum() / tot
        out[f"edges<{r}"] = dens[Ym & ed].sum() / tot
    return out

if __name__ == "__main__":
    t.watchdog()
    e, f = {}, {}
    for L in (4, 8, 12, 16):
        e[L] = t.run(L, "edge"); print("L", L, "edge A =", round(e[L], 4), flush=True)
    F = {4: 1.9253, 8: 2.4551, 12: 2.7543, 16: 2.9589}
    diff = [F[L] - e[L] for L in F]
    print("fan minus edge", [round(x, 4) for x in diff], flush=True)
    lit = {L: t.run(L, "fan", literal=True) for L in (2, 4, 8)}
    print("literal", {k: round(v, 3) for k, v in lit.items()}, flush=True)
    print("fan mode L=16", {k: round(float(v), 3) for k, v in mode(16).items()}, flush=True)
    ok = max(diff) - min(diff) <= 0.5 and min(lit[4] / lit[2], lit[8] / lit[4]) >= 1.5
    print("T6", "PASS" if ok else "FAIL")
