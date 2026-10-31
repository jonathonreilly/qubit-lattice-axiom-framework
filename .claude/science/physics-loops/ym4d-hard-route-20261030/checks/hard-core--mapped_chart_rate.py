#!/usr/bin/env python3
"""Rate of decay of the inverse Hessian on the fibre, in tree-gauge coordinates, per box. Consumer: Lemma HS-M, (MD_j) on this map.

Written before running. Abelian, trivial background, d = 2, 3, torus N = L n_c, odd L. Bond field a. K := d^T d, the plaquette form.
Block B(y) = y + [-h, h]^d, y = h + L m. Tree: the comb of axis-ordered contours from y, so contours vanish in tree gauge and the
constraint is the path part: Q a (y, mu) := L^-d sum_{x in B(y)} sum_{s < L} a(x + s e_mu, mu) = 0. M := K restricted to {a = 0 on trees, Q a = 0}.
For a covector eta, X := M^-1 eta solves the KKT system. A(D) := largest l^2 norm of X on a box at box distance D from the source's box.
Sources: (S1) gauge invariant: eta = d^T e_p, one plaquette in box 0. (S2) not gauge invariant: eta = one free bond in box 0.

The question: a Combes-Thomas bound from the gap of M gives a rate per box that falls with L, since the gap falls. I claim the true rate per box is
free of L, for both sources, because the map from Landau to tree gauge is local to each box. If S2 has a slow tail, Lemma HS-M's use in the chart fails.

PRE-STATED criteria. rate(L) := least-squares slope of -log A(D) over D = 1, ..., D_max, with D_max the largest D having A(D) above 1e3 times the
solver's residual and at most n_c/2.
 R1. For each d, L, source: rate(L) >= 0.7.
 R2. For each d, source: rate at the largest L >= 0.5 times rate at the smallest L.
 R3. Reported, no criterion: gap(L) := lambda_min(M) (d = 2), prefactor A(0)/A at the source normalisation.
 R0. Control: residual of each solve below 1e-8 relative, constraint violation below 1e-8.
FAIL if R0, R1 or R2 fails. Limitations: abelian, trivial background, flat torus. RSS guard 2 GB.

Added after the first run, criteria written before running them. The commutator hypothesis (W) of Lemma HS-M, `library/preconditioned-covariance.md`:
free variables xi are the bonds off the tree and off a designated bond for each constraint, at the peak of the constraint's weight in the box of the bond's
start; T: xi -> X solves the constraints on designated bonds; M := T^T K T. Theta := diag(exp(rho x_box)), a box-wise weight along axis 0 on an open chain of
boxes (for rho small against 1/n_c on the torus, take the weight exp(rho * dist to box 0), which is log-Lipschitz). eps_1(rho) := operator norm of
M^{-1/2} (Theta M Theta^-1 - M) M^{-1/2}.
 W1. eps_1(0.2) <= 0.5 at d = 2, L = 3, 5, 7, n_c = 6.
 W2. eps_1(0.2) at L = 7 is at most 2 times its value at L = 3.
 W3. Reported, no criterion: eps_1(0.1), eps_1(0.2), eps_1(0.4), and whether the map rho -> eps_1 looks linear.
FAIL if W1 or W2 fails. Limitation: as above. If this fails in the chart, the rate is proved only by the weaker route in the lemma's note.
"""
import itertools
import resource
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


class Setup:
    def __init__(self, d, L, nc):
        self.d, self.L, self.nc, self.N, self.h = d, L, nc, L * nc, (L - 1) // 2
        self.shape = (self.N,) * d
        self.nsites = self.N**d
        self.nb = d * self.nsites

    def site(self, x):
        return int(np.ravel_multi_index(tuple(np.mod(x, self.N)), self.shape))

    def bond(self, x, mu):
        return self.site(x) + mu * self.nsites

    def curl(self):
        r, c, v = [], [], []
        row = 0
        for x in itertools.product(range(self.N), repeat=self.d):
            x = np.array(x)
            for mu in range(self.d):
                for nu in range(mu + 1, self.d):
                    em, en = np.eye(self.d, dtype=int)[mu], np.eye(self.d, dtype=int)[nu]
                    for b, s in ((self.bond(x, mu), 1), (self.bond(x + em, nu), 1), (self.bond(x + en, mu), -1), (self.bond(x, nu), -1)):
                        r.append(row)
                        c.append(b)
                        v.append(s)
                    row += 1
        return sp.csr_matrix((v, (r, c)), shape=(row, self.nb), dtype=float)

    def centres(self):
        return [self.h + self.L * np.array(m) for m in itertools.product(range(self.nc), repeat=self.d)]

    def tree_bonds(self):
        out = []
        rng = range(-self.h, self.h + 1)
        for y in self.centres():
            for r in itertools.product(rng, repeat=self.d):
                r = np.array(r)
                nz = np.nonzero(r)[0]
                if len(nz) == 0:
                    continue
                nu = nz[-1]
                x = y + r
                e = np.eye(self.d, dtype=int)[nu]
                if r[nu] > 0:
                    out.append(self.bond(x - e, nu))
                else:
                    out.append(self.bond(x, nu))
        return np.array(sorted(set(out)))

    def constraint(self):
        rows, cols, vals = [], [], []
        row = 0
        rng = range(-self.h, self.h + 1)
        for y in self.centres():
            for mu in range(self.d):
                e = np.eye(self.d, dtype=int)[mu]
                for r in itertools.product(rng, repeat=self.d):
                    x = y + np.array(r)
                    for s in range(self.L):
                        rows.append(row)
                        cols.append(self.bond(x + s * e, mu))
                        vals.append(self.L ** (-self.d))
                row += 1
        Q = sp.csr_matrix((vals, (rows, cols)), shape=(row, self.nb))
        Q.sum_duplicates()
        return Q

    def box_of_bond(self):
        """box index of each bond, from the site it starts at, with the block B(y) for each site."""
        out = np.zeros((self.nb, self.d), dtype=int)
        coords = np.array(np.unravel_index(np.arange(self.nsites), self.shape)).T
        box = coords // self.L
        for mu in range(self.d):
            out[mu * self.nsites : (mu + 1) * self.nsites] = box
        return out


def solve(s, sources, direct):
    D = s.curl()
    K = (D.T @ D).tocsr()
    tree = s.tree_bonds()
    keep = np.setdiff1d(np.arange(s.nb), tree)
    Kff = K[keep][:, keep]
    Qf = s.constraint()[:, keep]
    # drop dependent constraints: at the torus the coarse gradient structure has no dependency here, but guard with a tiny regulariser
    n, m = Kff.shape[0], Qf.shape[0]
    A = sp.bmat([[Kff, Qf.T], [Qf, -1e-13 * sp.identity(m)]], format="csc")
    res = []
    if direct:
        lu = spla.splu(A, permc_spec="COLAMD")
    for eta in sources:
        rhs = np.concatenate([eta[keep], np.zeros(m)])
        if direct:
            sol = lu.solve(rhs)
        else:
            sol, info = spla.minres(A, rhs, rtol=1e-11, maxiter=200000)  # first run crashed here on the keyword tol, after all d = 2 and d = 3, L = 3 results
        rr = np.linalg.norm(A @ sol - rhs) / np.linalg.norm(rhs)
        cv = np.linalg.norm(Qf @ sol[:n]) / max(np.linalg.norm(sol[:n]), 1e-30)
        X = np.zeros(s.nb)
        X[keep] = sol[:n]
        res.append((X, rr, cv))
        if rss_gb() > 2:
            raise SystemExit("RSS above 2 GB")
    gap = None
    if direct:
        v = np.random.default_rng(1).standard_normal(n)
        for _ in range(60):
            rhs = np.concatenate([v, np.zeros(m)])
            w = lu.solve(rhs)[:n]
            nrm = np.linalg.norm(w)
            v = w / nrm
        gap = 1.0 / nrm
    return res, gap, keep


def profile(s, X, box0):
    bb = s.box_of_bond()
    dist = np.abs(bb - np.array(box0))
    dist = np.minimum(dist, s.nc - dist).max(axis=1)
    A = {}
    per_box = {}
    idx = np.ravel_multi_index(tuple(bb.T), (s.nc,) * s.d)
    norms = np.bincount(idx, weights=X**2, minlength=s.nc**s.d)
    boxes = np.array(np.unravel_index(np.arange(s.nc**s.d), (s.nc,) * s.d)).T
    dd = np.abs(boxes - np.array(box0))
    dd = np.minimum(dd, s.nc - dd).max(axis=1)
    for D in range(0, s.nc // 2 + 1):
        vals = norms[dd == D]
        A[D] = float(np.sqrt(vals.max())) if len(vals) else 0.0
    return A


def rate(A, floor, nc):
    ds = [D for D in range(1, nc // 2 + 1) if A[D] > floor]
    if len(ds) < 2:
        return float("nan"), ds
    y = -np.log([A[D] for D in ds])
    return float(np.polyfit(ds, y, 1)[0]), ds


def run(d, L, nc, direct):
    s = Setup(d, L, nc)
    box0 = (0,) * d
    D = s.curl()
    # plaquette near the centre of box 0, in the (0, 1) plane
    x0 = np.array([s.h] * d)
    p = sp.csr_matrix(([1.0], ([0], [0])), shape=(1, D.shape[0]))
    # find the plaquette row with bond (x0, 0)
    b = s.bond(x0, 0)
    col = D.T[b].tocoo() if False else D[:, b].tocoo()
    row = col.row[np.argmax(col.data)]
    eta1 = np.asarray(D[row].todense()).ravel()
    tree = set(s.tree_bonds().tolist())
    free = None
    for r in itertools.product(range(-s.h, s.h + 1), repeat=d):
        for mu in range(d):
            bb = s.bond(x0 + np.array(r), mu)
            if bb not in tree:
                free = bb
                break
        if free is not None:
            break
    eta2 = np.zeros(s.nb)
    eta2[free] = 1.0
    res, gap, keep = solve(s, [eta1, eta2], direct)
    out = {}
    ok0 = True
    for name, (X, rr, cv) in zip(("S1", "S2"), res):
        A = profile(s, X, box0)
        tol = 1e-8
        ok0 = ok0 and rr < tol and cv < tol
        rt, ds = rate(A, 1e3 * max(rr, 1e-13) * np.linalg.norm(X), nc)
        out[name] = (rt, ds, A, rr, cv)
    print(f"d={d} L={L} nc={nc} bonds={s.nb} free={len(keep)} gap={gap if gap is None else f'{gap:.3e}'} rss={rss_gb():.2f}GB", flush=True)
    for name in out:
        rt, ds, A, rr, cv = out[name]
        print(f"  {name}: rate={rt:.3f} over D={ds} A(0)={A[0]:.3e} A={[f'{A[k]:.2e}' for k in sorted(A)]} res={rr:.1e} cv={cv:.1e}", flush=True)
    return out, gap, ok0


def designated(s):
    """One free bond per constraint: the free bond of largest weight in the constraint, not used by another (the peak, as in Text 5.1)."""
    tree = set(s.tree_bonds().tolist())
    Q = s.constraint().tocsr()
    used = {}
    taken = set()
    for row in range(Q.shape[0]):
        idx = Q.indices[Q.indptr[row] : Q.indptr[row + 1]]
        val = Q.data[Q.indptr[row] : Q.indptr[row + 1]]
        for k in np.argsort(-val, kind="stable"):
            b = int(idx[k])
            if b not in tree and b not in taken:
                used[row] = b
                taken.add(b)
                break
    return used, Q


def commutator(s, rhos):
    D = s.curl()
    K = (D.T @ D).toarray()
    used, Q = designated(s)
    Qd = Q.toarray()
    tree = set(s.tree_bonds().tolist())
    des = np.array([used[r] for r in range(Qd.shape[0])])
    free = np.array([b for b in range(s.nb) if b not in tree and b not in set(des.tolist())])
    A = Qd[:, des]
    B = Qd[:, free]
    Tdes = -np.linalg.solve(A, B)
    T = np.zeros((s.nb, len(free)))
    T[free, np.arange(len(free))] = 1.0
    T[des, :] = Tdes
    M = T.T @ K @ T
    M = 0.5 * (M + M.T)
    w, v = np.linalg.eigh(M)
    if w.min() <= 0:
        raise SystemExit(f"M not positive: {w.min()}")
    Mih = (v / np.sqrt(w)) @ v.T
    bb = s.box_of_bond()[free]
    dist = np.minimum(bb[:, 0], s.nc - bb[:, 0])
    out = {}
    for rho in rhos:
        th = np.exp(rho * dist)
        C = (th[:, None] * M) / th[None, :] - M
        E = Mih @ C @ Mih
        out[rho] = float(np.linalg.norm(E, 2))
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")
    return out, float(w.min()), float(w.max()), float(np.abs(T[des, :]).sum(axis=1).max())


def main():
    ok = True
    table = {}
    w = {}
    for L in (3, 5, 7):
        s = Setup(2, L, 6)
        e, lo, hi, tn = commutator(s, (0.1, 0.2, 0.4))
        w[L] = e
        good = e[0.2] <= 0.5
        ok = ok and good
        print(f"W1 L={L}: eps_1(0.1)={e[0.1]:.3f} eps_1(0.2)={e[0.2]:.3f} eps_1(0.4)={e[0.4]:.3f} lambda(M) in [{lo:.3e}, {hi:.3e}] l1 row of T at designated {tn:.2f}: {good}, rss={rss_gb():.2f}GB", flush=True)
    good = w[7][0.2] <= 2 * w[3][0.2]
    ok = ok and good
    print(f"W2: {w[3][0.2]:.3f} -> {w[7][0.2]:.3f}: {good}", flush=True)
    plan = [(2, 3, 10, True), (2, 5, 10, True), (2, 7, 10, True), (2, 9, 10, True), (3, 3, 6, True), (3, 5, 6, False)]
    for d, L, nc, direct in plan:
        out, gap, ok0 = run(d, L, nc, direct)
        ok = ok and ok0
        for src in out:
            table[(d, L, src)] = out[src][0]
            good = out[src][0] >= 0.7
            ok = ok and good
            print(f"  R1 d={d} L={L} {src}: {good}", flush=True)
    for d in (2, 3):
        Ls = sorted({k[1] for k in table if k[0] == d})
        for src in ("S1", "S2"):
            a, b = table[(d, Ls[0], src)], table[(d, Ls[-1], src)]
            good = b >= 0.5 * a
            ok = ok and good
            print(f"R2 d={d} {src}: rate {a:.3f} at L={Ls[0]} -> {b:.3f} at L={Ls[-1]}: {good}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
