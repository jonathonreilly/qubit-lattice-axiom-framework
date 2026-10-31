#!/usr/bin/env python3
"""Search for a wild Gaussian potential with the Wilson tree values, on a sparse family of plaquettes.

Exact reduction (parts/witness.md, Text 3, formula (3.7)). Let N plaquettes have pairwise disjoint corners, and a(q) := E_q + d_0 X(q), with X(q)
an arbitrary function on sites. For the plaquette p, let m_q(p) be the mean of X(q) over the corners of p and y_p^q in R^2 its mean gradient in the plane of p;
let c_p^q in R^2 be the mean in-plane value of the Feynman field E_q on p, and P_pq the flux. The staggered part of X(q) on p decouples. Then, with the antisymmetric
product u ^ v = u_1 v_2 - u_2 v_1,

  sum_p' V_p'(a(p), a(q), a(r)) = V_0(p, q, r) + sum_cyc(p, q, r) { 2 m_q(p) P_pr - 2 m_r(p) P_pq + 2 y_p^q ^ c_p^r - 2 y_p^r ^ c_p^q + 2 y_p^q ^ y_p^r }.   (E)

The Gaussian potential a has the Wilson tree values on the family exactly when (E) vanishes for all triples. Unknowns: 3 N (N - 1), equations N (N - 1) (N - 2) / 6.
The system is over-determined from N = 21.

PRE-REGISTERED CRITERIA (written before the first run).
 E0 FORMULA: (E) agrees with the brute-force sum over the lattice with random X on 10 random triples, relative 1e-9. FAIL means the reduction is wrong.
 E1 SOLVER: at N = 12, d = 4, under-determined, the solver reaches relative residual < 1e-8. FAIL means the solver is not to be trusted.
 E2 CONTROL d = 2: at N = 30 in d = 2 the relative residual is small, compared with its value at X = 0 (expected, since the axial gauge is a solution on the plane, up to -1/V tails).
 E3 DECISION d = 4, N = 30 and 40, 5 random starts, relative residual r := ||(E)|| / ||(E) at X = 0||:
    r_min < 1e-6: a sparse wild solution exists, and the finite-family route to a theorem with no symmetry cannot use sparse families;
    r_min > 1e-2: no solution found on this family (numerical evidence only, not a proof);
    otherwise unresolved.
 Also reports the size of the unknowns at the best point, since a solution with huge unknowns needs huge link variance.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import sys
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_tree_coeff import Lat, check_rss, current, field_E, path_links, plaq  # noqa: E402


def choose_family(lat, N, rng, min_sep=2):
    planes = list(itertools.combinations(range(lat.d), 2))
    out = []
    tries = 0
    while len(out) < N:
        tries += 1
        if tries > 200000:
            raise SystemExit("cannot place plaquettes")
        x = tuple(rng.integers(0, lat.T, size=lat.d))
        mu, nu = planes[rng.integers(len(planes))]
        ok = True
        for (y, m2, n2) in out:
            dist = max(min(abs(a - b), lat.T - abs(a - b)) for a, b in zip(x, y))
            if dist < min_sep:
                ok = False
                break
        if ok:
            out.append((x, mu, nu))
    return out


def corners(lat, x, mu, nu):
    x = np.array(x)
    e_m = np.eye(lat.d, dtype=int)[mu]
    e_n = np.eye(lat.d, dtype=int)[nu]
    return [tuple(x % lat.T), tuple((x + e_m) % lat.T), tuple((x + e_m + e_n) % lat.T), tuple((x + e_n) % lat.T)]


def incs_at(lat, E, x, mu, nu):
    """Increments of the field E on the plaquette, path order +mu +nu -mu -nu."""
    c = corners(lat, x, mu, nu)
    return np.array([E[(mu,) + c[0]], E[(nu,) + c[1]], -E[(mu,) + c[3]], -E[(nu,) + c[0]]])


def V_sum(lat, E1, E2, E3):
    """sum over all plaquettes of V_p, by the determinant definition."""
    total = 0.0
    Es = (E1, E2, E3)
    for mu in range(lat.d):
        for nu in range(mu + 1, lat.d):
            inc = []
            for E in Es:
                inc.append((E[mu], np.roll(E[nu], -1, axis=mu), -np.roll(E[mu], -1, axis=nu), -E[nu]))
            P = [sum(i) for i in inc]
            for s in range(4):
                for t in range(s + 1, 4):
                    a, b, c = P, [i[s] for i in inc], [i[t] for i in inc]
                    det = a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])
                    total += float(np.sum(det))
    return total


class System:
    def __init__(self, lat, family):
        self.lat = lat
        self.family = family
        N = self.N = len(family)
        self.E = []
        for (x, mu, nu) in family:
            self.E.append(field_E(lat, current(lat, path_links(lat, x, plaq(mu + 1, nu + 1)))))
        self.P = np.zeros((N, N))
        self.c = np.zeros((N, N, 2))
        for p, (x, mu, nu) in enumerate(family):
            for q in range(N):
                g = incs_at(lat, self.E[q], x, mu, nu)
                self.P[p, q] = np.sum(g)
                self.c[p, q] = [(g[0] - g[2]) / 2, (g[1] - g[3]) / 2]
        self.triples = list(itertools.combinations(range(N), 3))
        self.V0 = np.array([V_sum(lat, self.E[i], self.E[j], self.E[k]) for (i, j, k) in self.triples])
        check_rss()
        self.nv = 3 * N * N
        self._build_index()

    def _build_index(self):
        tr = np.array(self.triples)
        self.tr = tr
        rows, cols = [], []
        n = len(tr)
        # the cyclic images of (p, q, r)
        self.cyc = [(tr[:, 0], tr[:, 1], tr[:, 2]), (tr[:, 1], tr[:, 2], tr[:, 0]), (tr[:, 2], tr[:, 0], tr[:, 1])]
        self.n_eq = n

    def idx_m(self, p, q):
        return 3 * (self.N * p + q)

    def idx_y(self, p, q, comp):
        return 3 * (self.N * p + q) + 1 + comp

    def residual(self, z):
        N = self.N
        Z = z.reshape(N, N, 3)
        m = Z[:, :, 0]
        y = Z[:, :, 1:]
        r = self.V0.copy()
        for (p, q, s) in self.cyc:
            r += 2 * m[p, q] * self.P[p, s] - 2 * m[p, s] * self.P[p, q]
            r += 2 * (y[p, q, 0] * self.c[p, s, 1] - y[p, q, 1] * self.c[p, s, 0])
            r -= 2 * (y[p, s, 0] * self.c[p, q, 1] - y[p, s, 1] * self.c[p, q, 0])
            r += 2 * (y[p, q, 0] * y[p, s, 1] - y[p, q, 1] * y[p, s, 0])
        return r

    def jacobian(self, z):
        N = self.N
        Z = z.reshape(N, N, 3)
        y = Z[:, :, 1:]
        n = self.n_eq
        rows, cols, vals = [], [], []
        eq = np.arange(n)

        def add(col, val):
            rows.append(eq)
            cols.append(col)
            vals.append(val)

        for (p, q, s) in self.cyc:
            add(self.idx_m(p, q), 2 * self.P[p, s])
            add(self.idx_m(p, s), -2 * self.P[p, q])
            add(self.idx_y(p, q, 0), 2 * (self.c[p, s, 1] + y[p, s, 1]))
            add(self.idx_y(p, q, 1), 2 * (-self.c[p, s, 0] - y[p, s, 0]))
            add(self.idx_y(p, s, 0), 2 * (-self.c[p, q, 1] - y[p, q, 1]))
            add(self.idx_y(p, s, 1), 2 * (self.c[p, q, 0] + y[p, q, 0]))
        return sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, self.nv))

    def solve(self, z0, maxit=200, tol=1e-12):
        z = z0.copy()
        lam = 1e-3
        r = self.residual(z)
        c0 = r @ r
        for it in range(maxit):
            J = self.jacobian(z)
            sol = spla.lsmr(J, -r, damp=np.sqrt(lam), atol=1e-10, btol=1e-10, maxiter=2000)[0]
            rn = self.residual(z + sol)
            cn = rn @ rn
            if cn < c0:
                z = z + sol
                r = rn
                if abs(c0 - cn) < tol * max(c0, 1e-300) and lam < 1e-8:
                    c0 = cn
                    break
                c0 = cn
                lam = max(lam / 3, 1e-14)
            else:
                lam = min(lam * 4, 1e8)
                if lam >= 1e8:
                    break
        return z, np.sqrt(c0)


def check_formula(sys_, rng):
    lat, N = sys_.lat, sys_.N
    worst = 0.0
    # random X(q) on sites, one for each member of the family
    X = [rng.normal(size=lat.shape) * 0.1 for _ in range(N)]
    a = []
    for q in range(N):
        d = np.stack([np.roll(X[q], -1, axis=m) - X[q] for m in range(lat.d)])
        a.append(sys_.E[q] + d)
    Z = np.zeros((N, N, 3))
    for p, (x, mu, nu) in enumerate(sys_.family):
        c = corners(lat, x, mu, nu)
        for q in range(N):
            v = np.array([X[q][cc] for cc in c])
            Z[p, q, 0] = np.mean(v)
            Z[p, q, 1] = (v[1] + v[2] - v[0] - v[3]) / 2
            Z[p, q, 2] = (v[2] + v[3] - v[0] - v[1]) / 2
    r = sys_.residual(Z.ravel())
    for t in rng.choice(len(sys_.triples), size=min(10, len(sys_.triples)), replace=False):
        i, j, k = sys_.triples[t]
        brute = V_sum(lat, a[i], a[j], a[k])
        worst = max(worst, abs(brute - r[t]) / max(abs(brute), 1e-30))
    return worst


def run_case(d, T, N, starts, seed, label):
    rng = np.random.default_rng(seed)
    lat = Lat(d, T)
    t0 = time.time()
    fam = choose_family(lat, N, rng)
    S = System(lat, fam)
    e0 = check_formula(S, rng)
    r0 = np.linalg.norm(S.residual(np.zeros(S.nv)))
    print(f"{label}: d={d} T={T} N={N} unknowns={3*N*(N-1)} equations={S.n_eq} E0 worst={e0:.1e} |V0|={r0:.4e} setup={time.time()-t0:.0f}s rss={check_rss():.2f}GB", flush=True)
    best = np.inf
    best_z = None
    for s in range(starts):
        scale = r0 ** (1 / 2) / np.sqrt(S.n_eq) * (0.1 if s == 0 else 3.0 ** (s - 2))
        z0 = rng.normal(size=S.nv) * scale
        z, res = S.solve(z0)
        rel = res / r0
        Z = z.reshape(N, N, 3).copy()
        for q in range(N):
            Z[:, q, 0] -= np.mean(Z[:, q, 0])
        off = ~np.eye(N, dtype=bool)
        print(f"   start {s}: relative residual {rel:.3e}, max |m| {np.max(np.abs(Z[:,:,0][off])):.3e}, max |y| {np.max(np.abs(Z[:,:,1:][off])):.3e}, time={time.time()-t0:.0f}s", flush=True)
        if rel < best:
            best, best_z = rel, z
    return best


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "d3":
        # E4, added after E3 ran, before this ran: report only, where does the dimension enter. d = 3, T = 16, N = 30, 40.
        for N, seed in ((30, 5), (40, 6)):
            b = run_case(3, 16, N, 3, seed, "E4")
            print(f"E4 d=3 N={N}: r_min={b:.3e}", flush=True)
        return
    print("# E1 solver, under-determined", flush=True)
    b = run_case(4, 12, 12, 2, 1, "E1")
    print(f"E1 {'PASS' if b < 1e-8 else 'FAIL'}", flush=True)
    print("# E2 control d = 2", flush=True)
    b = run_case(2, 48, 30, 2, 2, "E2")
    print(f"E2 relative residual {b:.3e}", flush=True)
    print("# E3 decision d = 4", flush=True)
    for N, seed in ((30, 3), (40, 4)):
        b = run_case(4, 12, N, 5, seed, "E3")
        verdict = "a sparse wild solution exists" if b < 1e-6 else ("no solution found (numerical evidence only)" if b > 1e-2 else "unresolved")
        print(f"E3 N={N}: r_min={b:.3e}: {verdict}", flush=True)


if __name__ == "__main__":
    main()
