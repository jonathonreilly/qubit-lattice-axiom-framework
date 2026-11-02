#!/usr/bin/env python3
"""T2: optimal exact extension constant, d = 3, balanced fan. See CRITERIA.md."""
import resource, sys
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

P = 2  # parents per side (amended, see CRITERIA.md)


def watchdog():
    import os, subprocess, threading, time

    def loop():
        while True:
            rss = int(subprocess.check_output(["ps", "-o", "rss=", "-p", str(os.getpid())]))
            if rss > 2_000_000:
                print("watchdog: RSS above 2 GB, stopping", flush=True)
                os._exit(3)
            time.sleep(1.0)

    threading.Thread(target=loop, daemon=True).start()


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > 2e9:
        sys.exit("RSS above 2 GB")


def build(L, pattern):
    n = P * L
    a = 1.0 / L
    idx = np.arange(n ** 3).reshape(n, n, n)
    X, Y, Z = np.meshgrid(*[np.arange(n)] * 3, indexing="ij")
    x, y, z = [(c - n // 2 + 0.5) for c in (X, Y, Z)]
    if pattern == "fan":
        om = ((z < 0) & (x < 0)) | ((z > 0) & (y > 0))
    elif pattern == "flat":
        om = z < 0
    om = om.ravel()
    E = []
    for ax in range(3):
        s0 = [slice(None)] * 3
        s1 = [slice(None)] * 3
        s0[ax] = slice(0, n - 1)
        s1[ax] = slice(1, n)
        E.append(np.stack([idx[tuple(s0)].ravel(), idx[tuple(s1)].ravel()], 1))
    E = np.concatenate(E)
    par = (X // L + P * (Y // L) + P * P * (Z // L)).ravel()
    return n, a, om, E, par


def lap(N, E, keep=None):
    if keep is not None:
        E = E[keep]
    i, j = E[:, 0], E[:, 1]
    A = sp.coo_matrix((np.ones(len(i)), (i, j)), shape=(N, N))
    A = A + A.T
    return sp.diags(np.asarray(A.sum(1)).ravel()) - A


def run(L, pattern, literal=False, steps=40):
    n, a, om, E, par = build(L, pattern)
    N = n ** 3
    d = 3
    w0, w1 = a ** d, a ** (d - 2)
    Afull = (w0 * sp.identity(N) + w1 * lap(N, E)).tocsr()
    both = om[E[:, 0]] & om[E[:, 1]]
    Aom_full = (w0 * sp.diags(om.astype(float)) + w1 * lap(N, E, both)).tocsr()
    iO, iY = np.where(om)[0], np.where(~om)[0]
    AOO = Afull[iO][:, iO].tocsc()
    AOY = Afull[iO][:, iY].tocsc()
    AYY = Afull[iY][:, iY].tocsc()
    GOO = Aom_full[iO][:, iO].tocsc()

    def means(ix):
        u, inv = np.unique(par[ix], return_inverse=True)
        return sp.csc_matrix((np.ones(len(ix)), (inv, np.arange(len(ix)))), shape=(len(u), len(ix)))

    CO = means(iO)
    if literal:
        # literal condition: w = 0 on all Y sites
        def S(u):
            return AOO @ u
    else:
        CY = means(iY)
        KY = sp.bmat([[AYY, CY.T], [CY, None]], format="csc")
        luY = sla.splu(KY + 1e-14 * sp.identity(KY.shape[0], format="csc"))

        def S(u):
            rhs = np.concatenate([-(AOY.T @ u), np.zeros(CY.shape[0])])
            sol = luY.solve(rhs)
            wY = sol[: len(iY)]
            return AOO @ u + AOY @ wY

    KO = sp.bmat([[GOO, CO.T], [CO, None]], format="csc")
    luO = sla.splu(KO + 1e-14 * sp.identity(KO.shape[0], format="csc"))
    guard()

    def G(r):
        return luO.solve(np.concatenate([r, np.zeros(CO.shape[0])]))[: len(iO)]

    # Lanczos in the GOO inner product on ker CO
    rng = np.random.default_rng(7)
    v = G(rng.standard_normal(len(iO)))
    v /= np.sqrt(v @ (GOO @ v))
    V = [v]
    al, be = [], []
    for k in range(steps):
        w = G(S(V[-1]))
        for u in V:
            w -= (w @ (GOO @ u)) * u
        for u in V:
            w -= (w @ (GOO @ u)) * u
        h = V[-1] @ (S(V[-1]))
        al.append(h)
        nb = np.sqrt(max(w @ (GOO @ w), 0.0))
        if nb < 1e-10:
            break
        be.append(nb)
        V.append(w / nb)
    m = len(al)
    T = np.diag(al) + np.diag(be[: m - 1], 1) + np.diag(be[: m - 1], -1)
    ev = np.linalg.eigvalsh(T)
    guard()
    return ev[-1]


if __name__ == "__main__":
    watchdog()
    res = {}
    for L in (4, 8, 12, 16, 24):
        for pat in ("flat", "fan"):
            res[(L, pat)] = run(L, pat)
            print("L", L, pat, "A =", round(res[(L, pat)], 4), flush=True)
    lit = {}
    for L in (2, 4, 8):
        lit[L] = run(L, "fan", literal=True)
        print("L", L, "literal control =", round(lit[L], 3), flush=True)
    r1 = res[(8, "fan")] / res[(4, "fan")]
    r2 = res[(16, "fan")] / res[(8, "fan")]
    c = min(lit[4] / lit[2], lit[8] / lit[4])
    print("ratios fan", r1, r2, "24/16", res[(24, "fan")] / res[(16, "fan")], "literal min ratio", c)
    print("T2", "PASS" if r1 <= 1.25 and r2 <= 1.25 and c >= 1.5 else "FAIL")
