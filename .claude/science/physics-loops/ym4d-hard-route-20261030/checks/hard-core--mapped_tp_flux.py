#!/usr/bin/env python3
"""Lemma TP at a non-trivial background: constant flux, charged components, d = 2. Consumer: Text 5.9, (H1); its hostile note (b) names this.

Written before running. Fine torus N = L n_c, odd L. SU(2) background U_F in the Cartan, so charged components carry a phase; theta is the adjoint phase
per fine plaquette, theta = 2 pi m / N^2, and a' := L^2 theta the adjoint flux per coarse plaquette. T_mu psi(x) := u_mu(x) psi(x + e_mu). Charged bond field H.
 D psi := (T_mu - 1) psi,  d H (x) := H_1(x) + T_1 H_2 (x) - T_2 H_1 (x) - H_2(x).
Q_f is the exact linearisation of the log-average at U_F on charged components, with contours: for a parent bond (y, mu), and x in B(y), path_x := contour from y to x, line
to x' = x + L e_mu, reversed contour of y' to x'. Omega_x := holonomy phase of path_x, Omega_0 that of the centre line, vartheta_x := arg(Omega_x / Omega_0), A := avg vartheta_x,
eps_x := sum along path_x of (transport from y) H, with sign. Then
 Q_f H (y, mu) = dexp(A) avg_x ell(vartheta_x) (eps_x - e^{i vartheta_x} eps_0) + e^{i A} eps_0,  ell(v) := i v/(e^{i v} - 1),  dexp(A) := (e^{i A} - 1)/(i A).
Coarse link phase: Omega' := e^{i A} Omega_0. D' := T' - 1 at coarse level.

Space S := { H : D^* H = 0, and Q_f H in the range of D' }. This is the Landau representative of a variation with fixed parent: Q H_L = D' alpha, for some alpha.
lambda := min on S of ||d H||^2 / ||H||^2. Lemma TP claims L^2 lambda >= 1/C, with C free of L. At flux the worry is a low mode of size about a'/L^2: the proof at a background needs
curl' Y = [F', alpha] to be bounded by Y, and a coefficient that the Fourier argument at U = 1 does not see.

PRE-STATED criteria.
 F0 (control). ||Q_f D omega - D' r omega|| <= 1e-10 ||omega|| for random omega: the exact covariance.
 F1. L^2 lambda(m) >= 0.5 L^2 lambda(0) for all m with a' <= 0.2.
 F2. At the smallest non-zero a', L^2 lambda >= 0.8 L^2 lambda(0).
 F3. Reported: L^2 lambda against a'; the same at larger a' with no criterion.
FAIL if any of F0, F1, F2 fails. A failure of F1, F2 would mean Lemma TP fails at a background as stated, and (H1)'s gap must be re-derived.
Limitations: d = 2, one level (fine to level 1), constant flux, the form ||d H||^2 only. RSS guard 2 GB.

Also, written before running: the fibre's inverse Hessian in tree-gauge coordinates at flux. M_f := d^dagger d on { H = 0 on the combs from block centres, Q_f H = 0 }.
For a covector eta, X := M_f^-1 eta, by the KKT system. A(D) := largest l^2 norm of X on a box at box distance D from the source. Sources: S1 := d^dagger e_p, S2 := one free bond.
 RF1. rate per box, as in `hard-core--mapped_chart_rate.py`, is at least 0.7, for S1, S2, at all m with a' <= 0.2.
 RF2. rate(m) >= 0.5 rate(0), for S1, S2, at those m.
FAIL if RF1 or RF2 fails. Consumer: Lemma HS-P on a fibre at a background.
"""
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


class Bg:
    def __init__(self, L, nc, m):
        self.L, self.nc, self.N, self.h = L, nc, L * nc, (L - 1) // 2
        N = self.N
        self.theta = 2 * np.pi * m / N**2
        a = np.arange(N)
        ca = np.where(a < N // 2, a, a - N)
        self.u = np.ones((2, N, N), dtype=complex)
        A, B = np.meshgrid(a, a, indexing="ij")
        self.u[1] = np.exp(1j * self.theta * ca[A])
        self.u[0] = np.where(A == N // 2 - 1, np.exp(-1j * self.theta * N * B), 1.0)

    def idx(self, x, y):
        return (x % self.N) * self.N + (y % self.N)

    def T(self, mu):
        N = self.N
        M = np.zeros((N * N, N * N), dtype=complex)
        for x in range(N):
            for y in range(N):
                i = self.idx(x, y)
                j = self.idx(x + (mu == 0), y + (mu == 1))
                M[i, j] = self.u[mu, x, y]
        return M

    def path(self, y0, x, mu):
        """List of (site, direction, +1/-1) along the path from y0 to y0 + L e_mu through x."""
        out = []
        (a, b) = y0
        (c, d) = x
        def walk(p, q, r, s):
            res = []
            # axis 0 then axis 1, from (p, q) to (r, s)
            cur = [p, q]
            step = 1 if r >= p else -1
            while cur[0] != r:
                if step > 0:
                    res.append(((cur[0], cur[1]), 0, 1))
                else:
                    res.append(((cur[0] - 1, cur[1]), 0, -1))
                cur[0] += step
            step = 1 if s >= q else -1
            while cur[1] != s:
                if step > 0:
                    res.append(((cur[0], cur[1]), 1, 1))
                else:
                    res.append(((cur[0], cur[1] - 1), 1, -1))
                cur[1] += step
            return res
        out += walk(a, b, c, d)
        e = (self.L if mu == 0 else 0, self.L if mu == 1 else 0)
        cur = [c, d]
        for _ in range(self.L):
            out.append(((cur[0], cur[1]), mu, 1))
            cur[mu] += 1
        # reversed contour of y' to x'
        back = walk(a + e[0], b + e[1], c + e[0], d + e[1])
        for (site, nu, sg) in reversed(back):
            out.append((site, nu, -sg))
        return out

    def row_data(self, y0, mu):
        """Returns dict x -> (Omega_x, coefficients of eps_x on bonds)."""
        h = self.h
        res = {}
        for r0 in range(-h, h + 1):
            for r1 in range(-h, h + 1):
                x = (y0[0] + r0, y0[1] + r1)
                om = 1.0 + 0j
                coef = {}
                for (site, nu, sg) in self.path(y0, x, mu):
                    s0, s1 = site[0] % self.N, site[1] % self.N
                    b = self.idx(s0, s1) + nu * self.N**2
                    if sg > 0:
                        coef[b] = coef.get(b, 0) + om
                        om = om * self.u[nu, s0, s1]
                    else:
                        om = om * np.conj(self.u[nu, s0, s1])
                        coef[b] = coef.get(b, 0) - om
                res[(r0, r1)] = (om, coef)
        return res


def build(L, nc, m):
    g = Bg(L, nc, m)
    N, n = g.N, nc
    nb = 2 * N * N
    T0, T1 = g.T(0), g.T(1)
    I = np.eye(N * N, dtype=complex)
    D = np.vstack([T0 - I, T1 - I])
    d = np.zeros((N * N, nb), dtype=complex)
    d[:, : N * N] = I - T1
    d[:, N * N :] = T0 - I
    centres = [(g.h + L * i, g.h + L * j) for i in range(n) for j in range(n)]
    Q = np.zeros((2 * n * n, nb), dtype=complex)
    omp = np.zeros((2, n, n), dtype=complex)
    for ci, y0 in enumerate(centres):
        i, j = ci // n, ci % n
        for mu in range(2):
            data = g.row_data(y0, mu)
            om0, c0 = data[(0, 0)]
            vs = {k: np.angle(v[0] / om0) for k, v in data.items()}
            A = np.mean(list(vs.values()))
            row = np.zeros(nb, dtype=complex)
            e0 = np.zeros(nb, dtype=complex)
            for b, v in c0.items():
                e0[b] += v
            for k, (om, c) in data.items():
                v = vs[k]
                ell = 1.0 if abs(v) < 1e-12 else 1j * v / (np.exp(1j * v) - 1)
                ex = np.zeros(nb, dtype=complex)
                for b, w in c.items():
                    ex[b] += w
                row += ell * (ex - np.exp(1j * v) * e0)
            row /= len(data)
            dex = 1.0 if abs(A) < 1e-12 else (np.exp(1j * A) - 1) / (1j * A)
            row = dex * row + np.exp(1j * A) * e0
            Q[ci + mu * n * n] = row
            omp[mu, i, j] = np.exp(1j * A) * om0
    Dc = np.zeros((2 * n * n, n * n), dtype=complex)
    for ci in range(n * n):
        i, j = ci // n, ci % n
        for mu in range(2):
            ni, nj = (i + (mu == 0)) % n, (j + (mu == 1)) % n
            Dc[ci + mu * n * n, ci] -= 1
            Dc[ci + mu * n * n, ni * n + nj] += omp[mu, i, j]
    r = np.zeros((n * n, N * N), dtype=complex)
    for ci, y0 in enumerate(centres):
        r[ci, g.idx(*y0)] = 1
    return g, D, d, Q, Dc, r


def lowest(L, nc, m, rng):
    g, D, d, Q, Dc, r = build(L, nc, m)
    om = rng.standard_normal(g.N**2) + 1j * rng.standard_normal(g.N**2)
    cov = np.linalg.norm(Q @ (D @ om) - Dc @ (r @ om)) / np.linalg.norm(om)
    u, sv, _ = np.linalg.svd(Dc, full_matrices=True)
    rank = int(np.sum(sv > 1e-10 * max(sv[0], 1e-30)))
    Pc = u[:, rank:]  # orthonormal basis of the complement of the range of D'
    C = np.vstack([D.conj().T, Pc.conj().T @ Q])
    _, s2, vh = np.linalg.svd(C, full_matrices=True)
    rk = int(np.sum(s2 > 1e-10 * s2[0]))
    Z = vh[rk:].conj().T
    G = Z.conj().T @ (d.conj().T @ d) @ Z
    G = 0.5 * (G + G.conj().T)
    w = np.linalg.eigvalsh(G)
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")
    return float(w[0]), float(w[1]), cov, Z.shape[1]


def comb_bonds(g):
    """Tree bonds: last step of the axis-ordered contour from the block centre to each site of the block."""
    out = set()
    N = g.N
    for i in range(g.nc):
        for j in range(g.nc):
            y0 = (g.h + g.L * i, g.h + g.L * j)
            for r0 in range(-g.h, g.h + 1):
                for r1 in range(-g.h, g.h + 1):
                    x = (y0[0] + r0, y0[1] + r1)
                    if r1 != 0:
                        z = (x[0], x[1] - 1) if r1 > 0 else x
                        out.add(g.idx(z[0], z[1]) + N * N)
                    elif r0 != 0:
                        z = (x[0] - 1, x[1]) if r0 > 0 else x
                        out.add(g.idx(z[0], z[1]))
    return np.array(sorted(out))


def chart_rate(L, nc, m):
    g, D, d, Q, Dc, r = build(L, nc, m)
    N = g.N
    nb = 2 * N * N
    tree = comb_bonds(g)
    keep = np.setdiff1d(np.arange(nb), tree)
    K = d.conj().T @ d
    Kff = K[np.ix_(keep, keep)]
    Qf = Q[:, keep]
    n1, m1 = Kff.shape[0], Qf.shape[0]
    A = np.zeros((n1 + m1, n1 + m1), dtype=complex)
    A[:n1, :n1] = Kff
    A[:n1, n1:] = Qf.conj().T
    A[n1:, :n1] = Qf
    # plaquette at the centre of box 0, and a free bond near it
    x0 = (g.h, g.h)
    e_p = np.zeros(N * N, dtype=complex)
    e_p[g.idx(*x0)] = 1
    eta1 = d.conj().T @ e_p
    free = None
    tset = set(tree.tolist())
    for r0 in range(-g.h, g.h + 1):
        for r1 in range(-g.h, g.h + 1):
            for mu in range(2):
                b = g.idx(x0[0] + r0, x0[1] + r1) + mu * N * N
                if b not in tset:
                    free = b
                    break
            if free is not None:
                break
        if free is not None:
            break
    eta2 = np.zeros(nb, dtype=complex)
    eta2[free] = 1
    a = np.arange(N)
    AA, BB = np.meshgrid(a, a, indexing="ij")
    boxes = np.stack([AA // L, BB // L], axis=-1).reshape(-1, 2)
    bb = np.vstack([boxes, boxes])
    out = {}
    sol = np.linalg.lstsq(A, np.column_stack([np.concatenate([eta1[keep], np.zeros(m1)]), np.concatenate([eta2[keep], np.zeros(m1)])]), rcond=1e-12)[0]
    for name, col in (("S1", 0), ("S2", 1)):
        X = np.zeros(nb, dtype=complex)
        X[keep] = sol[:n1, col]
        idx = bb[:, 0] * nc + bb[:, 1]
        norms = np.bincount(idx, weights=np.abs(X) ** 2, minlength=nc * nc)
        bx = np.array(np.unravel_index(np.arange(nc * nc), (nc, nc))).T
        dd = np.minimum(bx, nc - bx).max(axis=1)
        prof = [float(np.sqrt(norms[dd == k].max())) for k in range(nc // 2 + 1)]
        ds = [k for k in range(1, nc // 2 + 1) if prof[k] > 1e-9 * prof[0]]
        rt = float(np.polyfit(ds, -np.log([prof[k] for k in ds]), 1)[0]) if len(ds) >= 2 else float("nan")
        out[name] = (rt, prof)
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")
    return out


def main():
    rng = np.random.default_rng(31)
    ok = True
    for L, nc, ms in ((3, 12, (0, 1, 2, 4)), (5, 8, (0, 1, 2))):
        base = {}
        for m in ms:
            res = chart_rate(L, nc, m)
            ap = L**2 * 2 * np.pi * m / (L * nc) ** 2
            for name, (rt, prof) in res.items():
                if m == 0:
                    base[name] = rt
                good = True
                if ap <= 0.2:
                    good = rt >= 0.7 and rt >= 0.5 * base[name]
                ok = ok and good
                print(f"RF L={L} nc={nc} m={m} a'={ap:.3f} {name}: rate={rt:.3f} prof={[f'{v:.1e}' for v in prof]} {good} rss={rss_gb():.2f}GB", flush=True)
    for L, nc, ms in ((3, 12, (0, 1, 2, 4, 8)), (5, 8, (0, 1, 2, 4))):
        base = None
        first = True
        for m in ms:
            lo, nx, cov, dim = lowest(L, nc, m, rng)
            ap = L**2 * 2 * np.pi * m / (L * nc) ** 2
            v = L**2 * lo
            if m == 0:
                base = v
            else:
                if ap <= 0.2:
                    good = v >= 0.5 * base
                    ok = ok and good
                else:
                    good = None
                if first:
                    g2 = v >= 0.8 * base
                    ok = ok and g2
                    print(f"  F2 L={L}: {v:.4f} against {base:.4f}: {g2}", flush=True)
                    first = False
            c0 = cov <= 1e-10
            ok = ok and c0
            print(f"L={L} nc={nc} m={m} a'={ap:.4f} dim={dim} L^2 lambda={v:.4f} next={L**2*nx:.4f} cov={cov:.1e} F0={c0} rss={rss_gb():.2f}GB", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
