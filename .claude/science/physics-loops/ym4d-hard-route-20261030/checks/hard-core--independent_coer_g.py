#!/usr/bin/env python3
"""(COER-G) of parts/hard-core--independent.md, (CUT) item 1, abelian, on regions.

Claim under test. For B on the links R of a chart region, with Q_str B = 0 on
chart bonds,

    ||B||^2 <= C L^2 ( ||d B||^2 + tau ||d^* B||^2 ),

with d, d^* the free-boundary operators on R and C absolute, uniformly in L and
in the pattern of removed blocks. Equivalently lambda_min(H | ker Q) L^2 >= 1 / C.
The rate c / L of 7.3 and kappa = c M in (EI) rest on this.

Model. Periodic 4-torus of side n L, one scalar component (abelian). A pattern
is a set of removed blocks. R consists of the links inside kept blocks and the
crossing links of bonds with both blocks kept. Q_str(c) B is L^{-4} times the
sum over x in block y and s = 0..L-1 of B on link (x + s e_mu, mu), which is
what makes Q_str(d lambda) the coarse gradient of block averages.

The gauge term. The slice needs dim rho = dim Lie(G_0), so the form in the text is
H_0 = d^T d + tau (d^*)^T Pi_0 d^*, with Pi_0 the projection on zero block average.
Both that form ("pi0", the primary one) and the one with full d^* are reported.

Pre-registered criteria, written before the first run.
    Let v(L) := min over patterns of lambda_min L^2, with tau = 1, for the pi0 form.
    PASS-COER: v(7) >= v(3) / 2 and v(5) >= v(3) / 2, and v(L) > 0.02 for all L.
    FAIL-COER: v(7) < v(3) / 2. A decrease by more than a factor 2 between
    L = 3 and L = 7 would suggest a power of L beyond L^{-2}, and then kappa = c M
    is false as stated. A slow decrease within the factor 2 is a logarithm at
    worst, and it is harmless since M is a power of log L: report it.
    MODE: at the worst pattern, the fraction of the eigenvector norm on crossing
    links is reported, so that a failure can be read.
    At L = 3, 5, for patterns full, one, diag2, with H_1 := d^T d + tau (d^*)^T d^* + L^{-2}:
    PASS-WOOD: the smallest eigenvalue w(L) of 1 - tau V^T H_1^{-1} V, V := d^* u_y over
    blocks, has w >= 0.05 and w(5) >= 0.6 w(3). This is the Woodbury condition that lets
    the block-mean part of the gauge term be sampled by a strictly local chart.
    PASS-COND: the condition number c(L) of Q C_m Q^T, C_m := (H_0 + L^{-2})^{-1},
    has c <= 30 and c(5) <= 1.5 c(3). This is what bounds the degree of T.

Run under the numeric lock, with one job at a time, BLAS threads 1, nice, and
this script checks its own RSS against 2 GB.
"""
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl

DIM = 4
RSS_LIMIT_BYTES = 2 * 1024**3


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS
    if rss > RSS_LIMIT_BYTES:
        print(f"ABORT rss {rss}")
        sys.exit(3)


def build(L, n, removed):
    N = n * L
    nsites = N**DIM
    powers = np.array([N**i for i in range(DIM)])
    coords = np.array(np.unravel_index(np.arange(nsites), (N,) * DIM, order="F")).T
    blocks = coords // L
    bpowers = np.array([n**i for i in range(DIM)])
    block_id = blocks @ bpowers
    kept = np.ones(n**DIM, dtype=bool)
    for b in removed:
        kept[np.array(b) @ bpowers] = False
    site_ok = kept[block_id]

    def site_index(c):
        return (c % N) @ powers

    # links: index link (x, mu) as mu * nsites + x; keep those in R
    in_R = np.zeros(DIM * nsites, dtype=bool)
    for mu in range(DIM):
        e = np.zeros(DIM, dtype=int)
        e[mu] = 1
        y = site_index(coords + e)
        in_R[mu * nsites + np.arange(nsites)] = site_ok & site_ok[y]
    # a link between two kept blocks is a crossing link of a chart bond: in R
    lid = -np.ones(DIM * nsites, dtype=np.int64)
    lid[in_R] = np.arange(in_R.sum())
    nl = int(in_R.sum())

    # d^* with free boundary, on sites of kept blocks
    rows, cols, vals = [], [], []
    for mu in range(DIM):
        e = np.zeros(DIM, dtype=int)
        e[mu] = 1
        y = site_index(coords + e)
        idx = lid[mu * nsites + np.arange(nsites)]
        good = idx >= 0
        rows += [np.arange(nsites)[good], y[good]]
        cols += [idx[good], idx[good]]
        vals += [np.full(good.sum(), -1.0), np.full(good.sum(), 1.0)]
    Ds = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(nsites, nl))

    # d on plaquettes with all four links in R
    rows, cols, vals = [], [], []
    np_count = 0
    for mu, nu in itertools.combinations(range(DIM), 2):
        emu = np.zeros(DIM, dtype=int)
        emu[mu] = 1
        enu = np.zeros(DIM, dtype=int)
        enu[nu] = 1
        l1 = lid[mu * nsites + np.arange(nsites)]
        l2 = lid[nu * nsites + site_index(coords + emu)]
        l3 = lid[mu * nsites + site_index(coords + enu)]
        l4 = lid[nu * nsites + np.arange(nsites)]
        good = (l1 >= 0) & (l2 >= 0) & (l3 >= 0) & (l4 >= 0)
        k = int(good.sum())
        r = np.arange(np_count, np_count + k)
        rows += [r, r, r, r]
        cols += [l1[good], l2[good], l3[good], l4[good]]
        vals += [np.full(k, 1.0), np.full(k, 1.0), np.full(k, -1.0), np.full(k, -1.0)]
        np_count += k
    Dd = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(np_count, nl))

    # Q_str on chart bonds
    rows, cols, vals = [], [], []
    nb = 0
    for j, b in enumerate(itertools.product(range(n), repeat=DIM)):
        b = np.array(b)
        if not kept[b @ bpowers]:
            continue
        for mu in range(DIM):
            b2 = b.copy()
            b2[mu] = (b2[mu] + 1) % n
            if not kept[b2 @ bpowers]:
                continue
            members = np.where(block_id == b @ bpowers)[0]
            acc = {}
            for s in range(L):
                e = np.zeros(DIM, dtype=int)
                e[mu] = s
                z = site_index(coords[members] + e)
                ll = lid[mu * nsites + z]
                if (ll < 0).any():
                    raise RuntimeError("tube link not in R")
                for li in ll:
                    acc[li] = acc.get(li, 0.0) + L ** (-4.0)
            for li, v in acc.items():
                rows.append(nb)
                cols.append(li)
                vals.append(v)
            nb += 1
    Q = sp.csr_matrix((vals, (rows, cols)), shape=(nb, nl)) if nb else sp.csr_matrix((0, nl))
    # crossing-link mask, for the report
    cross = np.zeros(nl, dtype=bool)
    for mu in range(DIM):
        e = np.zeros(DIM, dtype=int)
        e[mu] = 1
        y = site_index(coords + e)
        idx = lid[mu * nsites + np.arange(nsites)]
        good = idx >= 0
        cross[idx[good]] = block_id[good] != block_id[y[good]]
    return Dd, Ds, Q, cross, nl, block_id, site_ok, nsites


def block_proj(block_id, kept_sites, nsites):
    """Return Pi_0 as a function on site vectors: remove the mean over each kept block."""
    ids = block_id
    nb = int(ids.max()) + 1
    counts = np.bincount(ids, weights=kept_sites.astype(float), minlength=nb)
    counts[counts == 0] = 1.0

    def pi0(u):
        means = np.bincount(ids, weights=u * kept_sites, minlength=nb) / counts
        return (u - means[ids]) * kept_sites

    return pi0, nb, counts


def lambda_min(Dd, Ds, Q, tau, nl, pi0=None):
    if Q.shape[0] > 0:
        QQinv = np.linalg.pinv((Q @ Q.T).toarray())
        Qd = Q.tocsr()
        Qt = Q.T.tocsr()

    def proj(v):
        if Q.shape[0] == 0:
            return v
        return v - Qt @ (QQinv @ (Qd @ v))

    sigma = 40.0

    def mv(v):
        w = proj(v)
        u = Ds @ w
        if pi0 is not None:
            u = pi0(u)
        hw = Dd.T @ (Dd @ w) + tau * (Ds.T @ u)
        return proj(hw) + sigma * (v - w)

    op = sl.LinearOperator((nl, nl), matvec=mv, dtype=float)
    k = 3
    vals, vecs = sl.eigsh(op, k=k, which="SA", tol=1e-5, ncv=min(120, nl - 1), maxiter=20000)
    order = np.argsort(vals)
    return vals[order], vecs[:, order]


def wood_cond(Dd, Ds, Q, tau, nl, L, block_id, site_ok, nb, counts, pi0):
    m2 = L ** (-2.0)

    def h1(v):
        return Dd.T @ (Dd @ v) + tau * (Ds.T @ (Ds @ v)) + m2 * v

    def h0m(v):
        return Dd.T @ (Dd @ v) + tau * (Ds.T @ pi0(Ds @ v)) + m2 * v

    H1 = sl.LinearOperator((nl, nl), matvec=h1, dtype=float)
    H0m = sl.LinearOperator((nl, nl), matvec=h0m, dtype=float)
    # Woodbury matrix on kept blocks
    kept = [b for b in range(nb) if np.any((block_id == b) & site_ok)]
    Vs = []
    for b in kept:
        u = ((block_id == b) & site_ok).astype(float)
        Vs.append(Ds.T @ (u / np.sqrt(u.sum())))
    Mw = np.zeros((len(kept), len(kept)))
    for j, vj in enumerate(Vs):
        x, info = sl.cg(H1, vj, rtol=1e-8, maxiter=5000)
        if info != 0:
            print("cg info", info)
        for i, vi in enumerate(Vs):
            Mw[i, j] = vi @ x
    Mw = 0.5 * (Mw + Mw.T)
    w = float(np.linalg.eigvalsh(np.eye(len(kept)) - tau * Mw).min())
    # Q C_m Q^T
    nbonds = Q.shape[0]
    if nbonds == 0:
        return w, 1.0
    Qt = Q.T.tocsc()
    G = np.zeros((nbonds, nbonds))
    for j in range(nbonds):
        rhs = np.asarray(Qt[:, j].todense()).ravel()
        x, info = sl.cg(H0m, rhs, rtol=1e-8, maxiter=5000)
        if info != 0:
            print("cg info", info)
        G[:, j] = Q @ x
    G = 0.5 * (G + G.T)
    ev = np.linalg.eigvalsh(G)
    return w, float(ev.max() / ev.min())


def patterns(n):
    """Removed-block sets. Each is chosen to expose a kind of geometry."""
    out = {"full": []}
    out["one"] = [(0, 0, 0, 0)]
    out["edge2"] = [(0, 0, 0, 0), (1, 0, 0, 0)]
    out["diag2"] = [(0, 0, 0, 0), (1, 1, 0, 0)]
    out["diag4"] = [(0, 0, 0, 0), (1, 1, 1, 1)]
    out["slab"] = [b for b in itertools.product(range(n), repeat=DIM) if b[0] == 0]
    out["twoslab"] = [b for b in itertools.product(range(n), repeat=DIM) if b[0] == 0 and b[1] == 0]
    # checkerboard: every kept block has no chart bond at all
    out["checker"] = [b for b in itertools.product(range(n), repeat=DIM) if sum(b) % 2 == 0]
    # single kept block
    out["single"] = [b for b in itertools.product(range(n), repeat=DIM) if b != (0, 0, 0, 0)]
    # kept: a one-dimensional chain of blocks along direction 0
    out["chain"] = [b for b in itertools.product(range(n), repeat=DIM) if not (b[1] == 0 and b[2] == 0 and b[3] == 0)]
    # kept: all but a shell leaving a thin neck
    out["neck"] = [b for b in itertools.product(range(n), repeat=DIM) if b[0] == 0 and b != (0, 0, 0, 0)]
    return out


def main():
    Ls = [int(a) for a in sys.argv[1:]] or [3, 5]
    n = 2
    tau = 1.0
    res = {}
    wood, cond = {}, {}
    for L in Ls:
        res[L] = {}
        for name, removed in patterns(n).items():
            Dd, Ds, Q, cross, nl, block_id, site_ok, nsites = build(L, n, removed)
            pi0, nb, counts = block_proj(block_id, site_ok, nsites)
            vals, vecs = lambda_min(Dd, Ds, Q, tau, nl, pi0=pi0)
            v = vecs[:, 0]
            fr = float((v[cross] ** 2).sum() / (v**2).sum())
            res[L][name] = float(vals[0] * L**2)
            check_rss()
            print(f"L={L} {name:8s} links={nl:7d} bonds={Q.shape[0]:3d} pi0: lam={vals[0]:.5f} lamL2={vals[0]*L**2:.4f} next={vals[1]:.5f} cross_frac={fr:.3f}", flush=True)
            vals2, _ = lambda_min(Dd, Ds, Q, tau, nl, pi0=None)
            print(f"L={L} {name:8s} full d*: lamL2={vals2[0]*L**2:.4f}", flush=True)
            if L in (3, 5) and name in ("full", "one", "diag2"):
                w, c = wood_cond(Dd, Ds, Q, tau, nl, L, block_id, site_ok, nb, counts, pi0)
                check_rss()
                wood.setdefault(L, []).append(w)
                cond.setdefault(L, []).append(c)
                print(f"L={L} {name:8s} wood_min={w:.4f} cond_QCQ={c:.3f}", flush=True)
    if 3 in wood and 5 in wood:
        w3, w5, c3, c5 = min(wood[3]), min(wood[5]), max(cond[3]), max(cond[5])
        print(f"wood {w3:.4f} {w5:.4f} cond {c3:.3f} {c5:.3f}")
        print("PASS-WOOD" if (min(w3, w5) >= 0.05 and w5 >= 0.6 * w3) else "FAIL-WOOD")
        print("PASS-COND" if (max(c3, c5) <= 30 and c5 <= 1.5 * c3) else "FAIL-COND")
    vs = {L: min(res[L].values()) for L in res}
    print("v(L) =", {L: round(x, 4) for L, x in vs.items()})
    if 3 in vs and 7 in vs:
        if vs[7] < vs[3] / 2:
            print("FAIL-COER")
        elif (5 not in vs or vs[5] >= vs[3] / 2) and min(vs.values()) > 0.02:
            print("PASS-COER")
        else:
            print("NEITHER: inspect")
    else:
        print("L = 7 not run: criterion not evaluated")


if __name__ == "__main__":
    main()
