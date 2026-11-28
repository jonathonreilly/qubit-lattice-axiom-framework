#!/usr/bin/env python3
"""Second registration after two_rate_weight.py read FAIL. Item rc-far. Written before running; the first run's criteria are unchanged and its FAIL stands.

What the first run left open. (i) T3 failed at L = 7: rate 0.445 on n = 1..4, with increments of -log a(n) of 0.27, 0.44, 0.63, rising. My guess,
to be tested and not assumed: a(n) saturates at the gap scale for small n, since E has a tail reaching the source box and A_1 E A_1 carries gap^-2. If
instead the true far rate falls with L, this run should show it. (ii) C1: N_s tracked N_2, so that far part made no slow region and T1 was close to vacuous.
Adding a positive Laplacian lifted the low modes of M_1 instead of delocalising them.

PART A, sparse, same family of far parts as the first run (E = t S X_0 S, s_i = exp(-0.5 r(i)), t = 1/2), to larger n. L = 3, 5, 7, nc = 16, n = 1..7.
 a(n) := max over i, j in box 0 of |A_t(i, j) - A_1(i, j)|. slope := least-squares slope of -log a(n) on the last three n, n = 5, 6, 7.
 A1. slope >= 0.5 at each L.
 A2. slope at L = 7 >= 0.5 times slope at L = 3.

PART B, dense, a far part that does make a slow region. For each box B let v_B be the lowest eigenvector of the principal block [M_1]_BB, with a sign fixed by
translation (v_B taken as the translate of v at box 0, on the free coordinates that match; coordinates that do not match are set to 0, and v_B is renormalised).
X_low := eps sum over neighbouring boxes B, B' of (v_B - v_B')(v_B - v_B')^T, eps = 1. So X_low hops the low modes between boxes without lifting the uniform
combination much. M_2 := M_1 + P X_low P with P the projector on free coordinates of boxes outside Q_n: no tail at all. M_t := M_1 + t P X_low P, t = 1/2.
Weights: rho = 0.8, rho_c = 0.02, R = n + 1. L = 3, 5 at nc = 10, n = 1..4; L = 7 at nc = 8, n = 1..3 (the first run reached 1.99 GB at L = 7, nc = 10).
 B1. N_2(nmax) / N_2(1) <= 4 at each L.
 B2. Vacuity control: at L = 5 or at L = 7, N_s(nmax) / N_s(1) >= 2 N_2(nmax) / N_2(1). If it holds at neither, B1 is declared vacuous and the run reads FAIL.
 B3. Reported, no criterion: slope of -log a(n) in Part B, the outer rate of M_t measured from a far free coordinate, and gap(M_t).
FAIL if A1, A2, B1 or B2 fails. Limits as before: abelian, trivial background, d = 2, one level, two families of far parts, Gaussian law only. RSS guard 2 GB.
"""
import importlib.util
import pathlib
import resource
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("chart_rate", HERE.parent / "hard-core--mapped_chart_rate.py")
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2.0:
        raise SystemExit("RSS above 2 GB")


def chart_sparse(s):
    D = s.curl()
    K = (D.T @ D).tocsr()
    used, Q = cr.designated(s)
    Q = Q.tocsc()
    tree = set(s.tree_bonds().tolist())
    des = np.array([used[r] for r in range(Q.shape[0])])
    dset = set(des.tolist())
    free = np.array([b for b in range(s.nb) if b not in tree and b not in dset])
    Ad = Q[:, des].tocsc()
    Bf = Q[:, free].tocsc()
    lu = spla.splu(Ad)
    rows, cols, vals = [], [], []
    Bd = Bf.tocsr()
    # designated rows of T, column by column through sparse right-hand sides
    Bc = Bf.tocsc()
    for k in range(Bc.shape[1]):
        idx = Bc.indices[Bc.indptr[k] : Bc.indptr[k + 1]]
        if len(idx) == 0:
            continue
        rhs = np.zeros(Ad.shape[0])
        rhs[idx] = Bc.data[Bc.indptr[k] : Bc.indptr[k + 1]]
        sol = -lu.solve(rhs)
        nz = np.nonzero(np.abs(sol) > 1e-13)[0]
        rows.extend(des[nz].tolist())
        cols.extend([k] * len(nz))
        vals.extend(sol[nz].tolist())
    rows.extend(free.tolist())
    cols.extend(range(len(free)))
    vals.extend([1.0] * len(free))
    T = sp.csr_matrix((vals, (rows, cols)), shape=(s.nb, len(free)))
    M = (T.T @ K @ T).tocsr()
    return 0.5 * (M + M.T), free


def graph_laplacian(s, free):
    nsites = s.nsites
    d = s.d
    pos = -np.ones(s.nb, dtype=int)
    pos[free] = np.arange(len(free))
    ends = {}
    coords = np.array(np.unravel_index(np.arange(nsites), s.shape)).T
    for mu in range(d):
        e = np.eye(d, dtype=int)[mu]
        ends_mu = np.array([s.site(c + e) for c in coords])
        for k in range(nsites):
            p = pos[k + mu * nsites]
            if p < 0:
                continue
            ends.setdefault(k, []).append(p)
            ends.setdefault(int(ends_mu[k]), []).append(p)
    rows, cols = [], []
    for lst in ends.values():
        for x in lst:
            for y in lst:
                if x != y:
                    rows.append(x)
                    cols.append(y)
    A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(free), len(free)))
    A.data[:] = 1.0
    return (sp.diags(np.asarray(A.sum(axis=1)).ravel()) - A).tocsr()


def box_distance(s, free):
    bb = s.box_of_bond()[free]
    db = np.minimum(bb, s.nc - bb)
    return db.max(axis=1).astype(float)


def part_a(L, nc, ns):
    s = cr.Setup(2, L, nc)
    M1, free = chart_sparse(s)
    guard()
    d0 = box_distance(s, free)
    X0 = graph_laplacian(s, free)
    box0 = np.nonzero(d0 == 0)[0]
    lu1 = spla.splu(M1.tocsc())
    rhs = np.zeros((len(free), len(box0)))
    rhs[box0, np.arange(len(box0))] = 1.0
    A1c = lu1.solve(rhs)
    del lu1
    a = {}
    for n in ns:
        r = np.maximum(n + 1 - d0, 0.0)
        S = sp.diags(np.exp(-0.5 * r))
        Mt = (M1 + 0.5 * (S @ X0 @ S)).tocsc()
        lu = spla.splu(Mt)
        Atc = lu.solve(rhs)
        del lu
        a[n] = float(np.abs((Atc - A1c)[box0, :]).max())
        guard()
        print(f"A L={L} n={n}: a(n)={a[n]:.4e} rss={rss_gb():.2f}GB", flush=True)
    return a


def low_modes(s, M1d, free):
    bb = s.box_of_bond()[free]
    key = {}
    idx0 = np.nonzero((bb == 0).all(axis=1))[0]
    w, v = np.linalg.eigh(M1d[np.ix_(idx0, idx0)])
    v0 = v[:, 0]
    # map a free coordinate to (bond type, offset inside its box)
    coords = np.array(np.unravel_index(free % s.nsites, s.shape)).T
    mu = free // s.nsites
    offs = coords - bb * s.L
    for i, f in enumerate(idx0):
        key[(int(mu[f]),) + tuple(offs[f].tolist())] = v0[i]
    vecs = {}
    for k in range(len(free)):
        kk = (int(mu[k]),) + tuple(offs[k].tolist())
        b = tuple(bb[k].tolist())
        if kk in key:
            vecs.setdefault(b, []).append((k, key[kk]))
    out = {}
    for b, lst in vecs.items():
        vv = np.zeros(len(free))
        ii = np.array([i for i, _ in lst])
        vv[ii] = np.array([x for _, x in lst])
        out[b] = vv / np.linalg.norm(vv)
    return out, float(w[0])


def opnorm(B, iters=400):
    rng = np.random.default_rng(0)
    v = rng.standard_normal(B.shape[1])
    v /= np.linalg.norm(v)
    last = 0.0
    for _ in range(iters):
        u = B.T @ (B @ v)
        nu = np.linalg.norm(u)
        v = u / nu
        val = np.sqrt(nu)
        if abs(val - last) < 1e-7 * val:
            break
        last = val
    return float(val)


def part_b(L, nc, ns, rho, rho_c, eps, t):
    s = cr.Setup(2, L, nc)
    M1s, free = chart_sparse(s)
    M1 = M1s.toarray()
    del M1s
    guard()
    d0 = box_distance(s, free)
    A1 = np.linalg.inv(M1)
    A1 = 0.5 * (A1 + A1.T)
    box0 = np.nonzero(d0 == 0)[0]
    vecs, lam0 = low_modes(s, M1, free)
    boxes = sorted(vecs)
    Vm = np.array([vecs[b] for b in boxes]).T
    index = {b: i for i, b in enumerate(boxes)}
    rows = {}
    for n in ns:
        out = d0 > n
        keep = [i for i, b in enumerate(boxes) if max(min(b[0], nc - b[0]), min(b[1], nc - b[1])) > n]
        keepset = set(keep)
        Lap = np.zeros((len(boxes), len(boxes)))
        for b in boxes:
            i = index[b]
            if i not in keepset:
                continue
            for mu in range(2):
                b2 = list(b)
                b2[mu] = (b2[mu] + 1) % nc
                j = index[tuple(b2)]
                if j in keepset:
                    Lap[i, i] += 1
                    Lap[j, j] += 1
                    Lap[i, j] -= 1
                    Lap[j, i] -= 1
        Vp = Vm.copy()
        Vp[~out, :] = 0.0
        E = t * eps * (Vp @ Lap @ Vp.T)
        Mt = M1 + E
        Mt = 0.5 * (Mt + Mt.T)
        gap_t = float(np.linalg.eigvalsh(Mt)[0])
        At = np.linalg.inv(Mt)
        At = 0.5 * (At + At.T)
        guard()
        R = n + 1
        f = rho * np.minimum(d0, R) + rho_c * np.maximum(d0 - R, 0.0)
        g = rho * d0
        N2 = opnorm((np.exp(f)[:, None] * At) * np.exp(-f)[None, :])
        Ns = opnorm((np.exp(g)[:, None] * At) * np.exp(-g)[None, :])
        a = float(np.abs((At - A1)[np.ix_(box0, box0)]).max())
        rows[n] = dict(N2=N2, Ns=Ns, a=a, gap_t=gap_t)
        print(f"B L={L} nc={nc} n={n}: lam0={lam0:.4e} gap(M_t)={gap_t:.4e} N_2={N2:.3f} N_s={Ns:.3f} a(n)={a:.3e} rss={rss_gb():.2f}GB", flush=True)
    return rows


def main():
    ok = True
    ns = tuple(range(1, 8))
    slopes = {}
    for L in (3, 5, 7):
        a = part_a(L, 16, ns)
        x = np.array([5.0, 6.0, 7.0])
        y = -np.log([a[5], a[6], a[7]])
        sl = float(np.polyfit(x, y, 1)[0])
        slopes[L] = sl
        good = sl >= 0.5
        ok = ok and good
        print(f"A1 L={L}: slope on n=5,6,7 = {sl:.3f}: {good}", flush=True)
    good = slopes[7] >= 0.5 * slopes[3]
    ok = ok and good
    print(f"A2 slope(7)/slope(3) = {slopes[7] / slopes[3]:.3f}: {good}", flush=True)
    vac = False
    for L, nc, nsb in ((3, 10, (1, 2, 3, 4)), (5, 10, (1, 2, 3, 4)), (7, 8, (1, 2, 3))):
        rows = part_b(L, nc, nsb, 0.8, 0.02, 1.0, 0.5)
        nmax = nsb[-1]
        r2 = rows[nmax]["N2"] / rows[1]["N2"]
        rs = rows[nmax]["Ns"] / rows[1]["Ns"]
        good = r2 <= 4
        ok = ok and good
        if L in (5, 7) and rs >= 2 * r2:
            vac = True
        sl = float(np.polyfit(np.array(nsb, dtype=float), -np.log([rows[n]["a"] for n in nsb]), 1)[0])
        print(f"B1 L={L}: N_2 ratio {r2:.3f}: {good}; N_s ratio {rs:.3f}; slope of a(n) {sl:.3f}", flush=True)
    ok = ok and vac
    print(f"B2 control (non-vacuous at L=5 or 7): {vac}", flush=True)
    print("PASS" if ok else "FAIL", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
