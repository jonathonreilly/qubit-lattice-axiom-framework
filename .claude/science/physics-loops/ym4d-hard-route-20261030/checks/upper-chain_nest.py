#!/usr/bin/env python3
"""Nest coercivity at the trivial background: does the constant degrade with the depth of the nest? Text 23 of parts/upper-chain.md.

The claim tested is the one `library/fibre-propagator.md` calls its weakest point, and which my (MD*_j) reads on the map of
hard-core--mapped: with frozen data on nested layers of whole blocks, with clearance,
    || H / s ||^2 <= C ( ||d H||^2 + ||P_N D^* H||^2 ),   C absolute,
for H in the kernel of the constraints, s(x) the local constraint scale. That file tested two levels at L = 3 only.
Here: U = 1, one colour, d = 2 and 3, a fine torus periodic along the walls with Bloch phases, flat walls.

Setting. Fine sites x; level-l block B_l(y) := y + [0, L^l)^d, y in the level-l lattice. r^(l) w (y) := mean of w on B_l(y).
(Q^(l) H)(y, mu) := mean over x in B_l(y) of the sum of H on the straight line from x to x + L^l e_mu. Then exactly
Q^(l) D = D_l r^(l) (Cov). Layers: Sigma_l, level-l sites with normal index in [a_l, b_l), l < n; a frozen bond has both ends
in Sigma_l, as in Theorem F-D and Text 23. Constraints: Q^(n) H = 0 on all level-n bonds, Q^(l) H = 0 on frozen level-l bonds.
r_N: r^(n) on all level-n sites, r^(l) on sites of Sigma_l. P_N: the projector on ker r_N. s(x) := L^l for the least l >= 1 with
x in the shadow of Sigma_l, else L^n. c := min over H of ( ||d H||^2 + ||P_N D^* H||^2 ) / || H / s ||^2, so C = 1 / c.

Criteria, written before the run.
N0: validation. (a) || Q^(l) D - D_l r^(l) || <= 1e-11 at every l used. (b) d = 2, L = 3, no layer, n = 1: c within 1 percent of
    L^2 4 sin^2(pi / (2 L)) = 9.0, the value that file reports. n = 2: within 2 percent of its 9.78.
N1: the claim. With whole-block layers and clearance, for each (d, L, n), min over the Bloch phases used and over depths of
    c(depth) / c(depth 0) >= 1/2. Tested at d = 2, L = 3, n = 3, depth <= 3; d = 2, L = 5, n = 2, depth <= 2; d = 3, L = 3, n = 2,
    depth <= 2. FAIL would mean the constant degrades with the nest in the free theory, and I would then look for a counterexample.
N2: control. A strip of width 1 inside a level-1 block has c <= 1e-6, the stabiliser mode of that file's first run: the test can
    see the failure it is looking for.
N3: exactness at whole blocks. { w : D w in ker(constraints) } = ker r_N, plus constants at zero phase: dimensions agree.
"""
import math
import resource
import sys
import time

import numpy as np
import scipy.linalg as sl
import scipy.sparse as sp

RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


class Lat:
    def __init__(self, d, L, n, X, k):
        self.d, self.L, self.n = d, L, n
        self.P = L**n
        self.shape = (X * self.P,) + (self.P,) * (d - 1)
        self.ns = int(np.prod(self.shape))
        self.nb = self.ns * d
        self.k = (0.0,) + tuple(k)
        self.cplx = any(abs(q) > 0 for q in k)

    def wrap(self, x):
        """Site index and Bloch phase of a coordinate tuple outside the domain."""
        ph = 1.0 + 0j
        c = []
        for a, (v, m) in enumerate(zip(x, self.shape)):
            q, r = divmod(v, m)
            c.append(r)
            if q and a > 0:
                ph *= np.exp(1j * q * self.k[a])
        return int(np.ravel_multi_index(c, self.shape)), ph

    def coords(self):
        return np.array(np.unravel_index(np.arange(self.ns), self.shape)).T

    def D(self):
        rows, cols, vals = [], [], []
        for s, x in enumerate(self.coords()):
            for mu in range(self.d):
                y = list(x)
                y[mu] += 1
                t, ph = self.wrap(y)
                b = s * self.d + mu
                rows += [b, b]
                cols += [t, s]
                vals += [ph, -1.0]
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.nb, self.ns), dtype=complex)

    def curl(self):
        rows, cols, vals = [], [], []
        r = 0
        for s, x in enumerate(self.coords()):
            for mu in range(self.d):
                for nu in range(mu + 1, self.d):
                    y = list(x)
                    y[mu] += 1
                    t1, p1 = self.wrap(y)
                    y = list(x)
                    y[nu] += 1
                    t2, p2 = self.wrap(y)
                    rows += [r] * 4
                    cols += [s * self.d + mu, t1 * self.d + nu, t2 * self.d + mu, s * self.d + nu]
                    vals += [1.0, p1, -p2, -1.0]
                    r += 1
        return sp.csr_matrix((vals, (rows, cols)), shape=(r, self.nb), dtype=complex)

    def level_sites(self, l):
        s = self.L**l
        return [tuple(c * s for c in idx) for idx in np.ndindex(*[m // s for m in self.shape])]

    def block(self, y, l):
        s = self.L**l
        return [tuple(a + b for a, b in zip(y, off)) for off in np.ndindex(*([s] * self.d))]

    def r_row(self, y, l):
        cols, vals = [], []
        w = self.L ** (-l * self.d)
        for x in self.block(y, l):
            t, ph = self.wrap(x)
            cols.append(t)
            vals.append(w * ph)
        return cols, vals

    def q_row(self, y, mu, l):
        cols, vals = [], []
        w = self.L ** (-l * self.d)
        for x in self.block(y, l):
            for s in range(self.L**l):
                z = list(x)
                z[mu] += s
                t, ph = self.wrap(z)
                cols.append(t * self.d + mu)
                vals.append(w * ph)
        return cols, vals


def stack(rows, ncol):
    r, c, v = [], [], []
    for i, (cols, vals) in enumerate(rows):
        r += [i] * len(cols)
        c += cols
        v += vals
    return sp.csr_matrix((v, (r, c)), shape=(len(rows), ncol), dtype=complex)


def cov_defect(lat, l):
    """|| Q^(l) D - D_l r^(l) ||_max at the given phase."""
    D = lat.D()
    sites = lat.level_sites(l)
    index = {y: i for i, y in enumerate(sites)}
    R = stack([lat.r_row(y, l) for y in sites], lat.ns)
    Q = stack([lat.q_row(y, mu, l) for y in sites for mu in range(lat.d)], lat.nb)
    rows, cols, vals = [], [], []
    s = lat.L**l
    for i, y in enumerate(sites):
        for mu in range(lat.d):
            z = list(y)
            z[mu] += s
            ph = 1.0 + 0j
            for a in range(lat.d):
                q, rr = divmod(z[a], lat.shape[a])
                z[a] = rr
                if q and a > 0:
                    ph *= np.exp(1j * q * lat.k[a])
            b = i * lat.d + mu
            rows += [b, b]
            cols += [index[tuple(z)], i]
            vals += [ph, -1.0]
    Dl = sp.csr_matrix((vals, (rows, cols)), shape=(len(sites) * lat.d, len(sites)), dtype=complex)
    diff = (Q @ D - Dl @ R).tocoo()
    return float(np.abs(diff.data).max()) if diff.nnz else 0.0


def constraints(lat, layers):
    """Rows of bC and of r_N. layers: {l: (a_l, b_l)} in level-l units along the normal axis."""
    rows, rn = [], []
    n = lat.n
    for y in lat.level_sites(n):
        rn.append(lat.r_row(y, n))
        for mu in range(lat.d):
            rows.append(lat.q_row(y, mu, n))
    for l, (a, b) in layers.items():
        s = lat.L**l
        for y in lat.level_sites(l):
            i = y[0] // s
            if not a <= i < b:
                continue
            rn.append(lat.r_row(y, l))
            for mu in range(lat.d):
                if mu == 0 and not i + 1 < b:
                    continue
                rows.append(lat.q_row(y, mu, l))
    return stack(rows, lat.nb), stack(rn, lat.ns)


def weights(lat, layers):
    s = np.full(lat.ns, float(lat.P))
    x0 = lat.coords()[:, 0]
    for l in sorted(layers, reverse=True):
        if l == 0:
            continue
        a, b = layers[l]
        sl_ = lat.L**l
        s[(x0 >= a * sl_) & (x0 < b * sl_)] = float(sl_)
    # level-0 layer: free bonds next to it sit under frozen level-1 parents, already s = L
    return 1.0 / np.repeat(s, lat.d) ** 2


def coercivity(d, L, n, X, layers, k, check_exact=False):
    lat = Lat(d, L, n, X, k)
    D = lat.D()
    C = lat.curl()
    bC, rN = constraints(lat, layers)
    Z = sl.null_space(bC.toarray(), rcond=1e-10)
    U = sl.orth(rN.conj().T.toarray(), rcond=1e-10)
    Y = D.conj().T @ Z
    Y = Y - U @ (U.conj().T @ Y)
    dZ = C @ Z
    A = dZ.conj().T @ dZ + Y.conj().T @ Y
    w = weights(lat, layers)
    B = Z.conj().T @ (w[:, None] * Z)
    if not lat.cplx:
        A, B = A.real, B.real
    A = (A + A.conj().T) / 2
    B = (B + B.conj().T) / 2
    ev = sl.eigh(A, B, eigvals_only=True, subset_by_index=[0, 1])
    rss_guard()
    extra = None
    if check_exact:
        G = (bC @ D).toarray()
        dim_g = lat.ns - np.linalg.matrix_rank(G, tol=1e-9)
        dim_r = lat.ns - U.shape[1]
        extra = (dim_g, dim_r)
    return float(ev[0]), extra


def main():
    t0 = time.time()
    # N0
    defect = 0.0
    for d, L, n, X, k in [(2, 3, 2, 2, (0.7,)), (3, 3, 1, 2, (0.4, 1.1))]:
        lat = Lat(d, L, n, X, k)
        for l in range(0, n + 1):
            defect = max(defect, cov_defect(lat, l))
    print(f"N0(a) largest Cov defect = {defect:.2e} (claim <= 1e-11)")
    c1, _ = coercivity(2, 3, 1, 3, {}, (0.0,))
    c1b, _ = coercivity(2, 3, 1, 3, {}, (1.0,))
    c2, _ = coercivity(2, 3, 2, 3, {}, (0.0,))
    c2b, _ = coercivity(2, 3, 2, 3, {}, (1.0,))
    print(f"N0(b) d=2 L=3 no layer: n=1 c = {c1:.4f}, {c1b:.4f} (k=1); n=2 c = {c2:.4f}, {c2b:.4f} (k=1); that file: 9.0, 9.78")
    ok0 = defect <= 1e-11 and abs(min(c1, c1b) - 9.0) <= 0.09 and abs(min(c2, c2b) - 9.78) <= 0.2
    print(f"elapsed {time.time() - t0:.0f} s", flush=True)

    # N2
    c, _ = coercivity(2, 3, 1, 3, {0: (4, 5)}, (0.0,))
    print(f"N2 thin strip inside a block: c = {c:.3e} (claim <= 1e-6)")
    ok2 = c <= 1e-6

    # N1, N3
    cases = [
        ("d=2 L=3 n=3", 2, 3, 3, 3, [{}, {2: (3, 6)}, {2: (3, 6), 1: (12, 15)}, {2: (3, 6), 1: (12, 15), 0: (39, 42)}], [(0.0,), (0.8,)]),
        ("d=2 L=5 n=2", 2, 5, 2, 3, [{}, {1: (5, 10)}, {1: (5, 10), 0: (35, 40)}], [(0.0,), (0.8,)]),
        ("d=3 L=3 n=2", 3, 3, 2, 2, [{}, {1: (3, 6)}, {1: (3, 6), 0: (12, 15)}], [(0.0, 0.0)]),
    ]
    ok1, ok3 = True, True
    for name, d, L, n, X, depth_layers, phases in cases:
        base = None
        for dep, layers in enumerate(depth_layers):
            vals = []
            for k in phases:
                exact = dep > 0 and all(abs(q) == 0 for q in k)
                v, extra = coercivity(d, L, n, X, layers, k, check_exact=exact)
                vals.append(v)
                if extra is not None:
                    match = extra[0] == extra[1] + 1
                    ok3 = ok3 and match
                    print(f"N3 {name} depth {dep}: dim gauge {extra[0]}, dim ker r_N + 1 = {extra[1] + 1}, {'ok' if match else 'MISMATCH'}")
            cmin = min(vals)
            if dep == 0:
                base = cmin
            ratio = cmin / base
            ok1 = ok1 and ratio >= 0.5
            print(f"N1 {name} depth {dep}: c by phase {[round(x, 4) for x in vals]}, ratio to depth 0 = {ratio:.4f} (claim >= 0.5); elapsed {time.time() - t0:.0f} s", flush=True)
    print("N0", "PASS" if ok0 else "FAIL")
    print("N1", "PASS" if ok1 else "FAIL")
    print("N2", "PASS" if ok2 else "FAIL")
    print("N3", "PASS" if ok3 else "FAIL")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
