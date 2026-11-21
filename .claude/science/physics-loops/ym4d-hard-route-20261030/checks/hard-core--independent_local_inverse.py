#!/usr/bin/env python3
"""A strictly local right inverse for the chart, (LOC-INV) of Text 4.6, on a 2D abelian toy.

Answers gate independent-core-16ca92dd7, D1: is xi_eff,c, read at fixed (b on Z, n), strictly local in the background?
The toy has the exact block map Q_str of Text 5.1 in d = 2 and H_1 = d^T d + D D^T + m^2 + diag(u), with u a local potential that
stands for the W dependence of the operators. V V^T is dropped from H_m, so H_m = H_1: that removes one polynomial and nothing else
tested here. It cannot test the 4D chart, and it establishes no bound.

PRE-STATED CRITERIA, written before the first run.
  With P_0 := U U_tilde Gamma, P_0^# := P_0^T H_m, U := 1 - l Q with l(c) = 1 on the crossing links of c, E' := P_0 P_0^# U - U,
  P := (P_0, -E'), R := (P_0^#, 1):
  EXACT.    PASS-EXACT if |P R u - u| <= 1e-10 |u| and |Q P| <= 1e-10 in sup norm, on random u in X = ker Q. FAIL-EXACT otherwise.
  RANGE.    PASS-RANGE if P and R have no entry beyond the link distance computed from the degrees. FAIL-RANGE otherwise.
  TAIL-R.   Z is a long thin line of links in one row, containing at most one crossing link per bond. Ext_Z puts the compensation on the
            crossing links off Z. x := R Ext_Z u + K n, K := 1 - R Ext_Z Res_Z P, at fixed real (u, n). Complex step on u_j at a far link j.
            PASS-TAIL-R if |d x_c / d u_j| < 1e-13 for all sampled j beyond the computed range. FAIL-TAIL-R otherwise.
  CONTROL.  The same derivative with the orthogonal right inverse, x := P_Z^+ u + n. CONTROL-OK if it is above 1e-13 at some sampled j
            beyond that range, which is the gate's FAIL-TAIL-LOCAL. CONTROL-VOID otherwise, and then TAIL-R has tested nothing.
  FORMULA.  Dense, small torus, high degree, no locality: E = P_0 P_0^# - 1 on X equals C_1^{1/2} Delta C_1^{-1/2}, with
            C_1 := (A + m^2)^{-1}, P_0 P_0^T = C_1^{1/2} (1 + Delta) C_1^{1/2}. PASS-FORMULA if the relative error is <= 1e-8.
  SMALL.    Same run. Delta' from P P^T = C_1^{1/2} (1 + Delta') C_1^{1/2}. PASS-SMALL if ||Delta|| < 0.1 and ||Delta'|| <= 2 ||Delta||.
            NOT-REACHED if ||Delta|| >= 0.1 at the largest degree tried. FAIL-SMALL otherwise.

  RESULT OF THE FIRST RUN, kept as registered. PASS-EXACT, PASS-RANGE, PASS-TAIL-R with exact zeros, and CONTROL-VOID: the bound of the script is 78 against an observed
  range of 23, so "far" was beyond distance 157, where the orthogonal inverse has decayed to 1e-29, below the registered threshold. So that run tested nothing, by its own criterion.
  The dense stage diverged, from a bug of mine: in d = 2, ||Q|| = 1, not 1 / L, so B = Q Gamma^2 Q^T goes up to L^2 and the scale 1.2 of the Neumann polynomial was wrong.
  ADDED BEFORE THE SECOND RUN. PROFILE: sample j along Z at every sixth distance from 0 to 150, at the same (u, n). r_obs := the largest sampled distance at which the
  derivative with R is nonzero. PASS-PROFILE if r_obs <= 78, the derivative with R is exactly zero beyond r_obs, and the orthogonal one exceeds 1e-13 at some sampled distance
  beyond r_obs. FAIL-PROFILE if the derivative with R is nonzero beyond 78. PROFILE-VOID if R passes and the orthogonal one never exceeds 1e-13 beyond r_obs.
  The Neumann scale becomes 1.05 times the largest eigenvalue of B, by power iteration. FORMULA and SMALL are unchanged, with larger degrees if needed.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import json, resource, sys
import numpy as np
import scipy.sparse as sp


def check_rss():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3
    if gb > 2.0:
        sys.exit(f"RSS {gb:.2f} GB above limit")


class Toy:
    def __init__(self, L, Nx, Ny=None):
        Ny = Nx if Ny is None else Ny
        self.L, self.Nx, self.Ny, self.Sx, self.Sy = L, Nx, Ny, L * Nx, L * Ny
        Sx, Sy = self.Sx, self.Sy
        self.nl = 2 * Sx * Sy
        self.m2 = 1.0 / L ** 2
        rows, cols, vals = [], [], []
        # plaquettes: d[p, l]
        for x in range(Sx):
            for y in range(Sy):
                p = self.site(x, y)
                for l, v in ((self.link(x, y, 0), 1.0), (self.link((x + 1) % Sx, y, 1), 1.0),
                             (self.link(x, (y + 1) % Sy, 0), -1.0), (self.link(x, y, 1), -1.0)):
                    rows.append(p); cols.append(l); vals.append(v)
        self.d = sp.csr_matrix((vals, (rows, cols)), shape=(Sx * Sy, self.nl))
        rows, cols, vals = [], [], []
        # gradient: D[l, site]
        for x in range(Sx):
            for y in range(Sy):
                for mu, (xx, yy) in enumerate((((x + 1) % Sx, y), (x, (y + 1) % Sy))):
                    l = self.link(x, y, mu)
                    rows += [l, l]; cols += [self.site(xx, yy), self.site(x, y)]; vals += [1.0, -1.0]
        self.D = sp.csr_matrix((vals, (rows, cols)), shape=(self.nl, Sx * Sy))
        self.H0 = (self.d.T @ self.d + self.D @ self.D.T + self.m2 * sp.identity(self.nl)).tocsr()
        self.build_q()

    def site(self, x, y):
        return (x % self.Sx) * self.Sy + (y % self.Sy)

    def link(self, x, y, mu):
        return 2 * self.site(x, y) + mu

    def build_q(self):
        L, Nx, Ny = self.L, self.Nx, self.Ny
        nb = 2 * Nx * Ny
        rows, cols, vals = [], [], []
        lr, lc, lv = [], [], []
        self.crossing = {}
        self.tube = {}
        for bx in range(Nx):
            for by in range(Ny):
                for mu in range(2):
                    c = 2 * (bx * Ny + by) + mu
                    cr, tb = [], []
                    x0, y0 = bx * L, by * L
                    for t in range(L):
                        for i in range(2 * L - 1):
                            w = (i + 1) / L if i < L - 1 else (1.0 if i == L - 1 else (2 * L - 1 - i) / L)
                            if mu == 0:
                                l = self.link(x0 + i, y0 + t, 0)
                            else:
                                l = self.link(x0 + t, y0 + i, 1)
                            rows.append(c); cols.append(l); vals.append(w / L)
                            tb.append(l)
                            if i == L - 1:
                                cr.append(l)
                                lr.append(l); lc.append(c); lv.append(1.0)
                    self.crossing[c] = cr
                    self.tube[c] = tb
        self.Q = sp.csr_matrix((vals, (rows, cols)), shape=(nb, self.nl))
        self.l = sp.csr_matrix((lv, (lr, lc)), shape=(self.nl, nb))
        self.U = (sp.identity(self.nl) - self.l @ self.Q).tocsr()
        self.nb = nb

    def cheb_sqrt_inv(self, H, deg, lo, hi):
        nodes = np.cos(np.pi * (np.arange(deg + 1) + 0.5) / (deg + 1))
        vals = (0.5 * (hi - lo) * nodes + 0.5 * (hi + lo)) ** (-0.5)
        c = np.array([(2.0 / (deg + 1)) * np.sum(vals * np.cos(k * np.arccos(nodes))) for k in range(deg + 1)])
        c[0] *= 0.5
        I = sp.identity(H.shape[0], format="csr", dtype=H.dtype)
        X = (2.0 * H - (lo + hi) * I) / (hi - lo)
        t0, t1 = I, X.copy()
        out = c[0] * t0 + c[1] * t1
        for k in range(2, deg + 1):
            t0, t1 = t1, (2.0 * X @ t1 - t0).tocsr()
            out = out + c[k] * t1
        out = out.tocsr()
        out.eliminate_zeros()
        return out

    def poly_inv(self, B, deg, sc):
        # Neumann polynomial for B^{-1}, scaled: (1/sc) sum_{j<=deg} (1 - B/sc)^j
        I = sp.identity(B.shape[0], format="csr", dtype=B.dtype)
        Y = (I - B / sc).tocsr()
        term, out = I, I
        for _ in range(deg):
            term = (term @ Y).tocsr()
            out = (out + term).tocsr()
        return (out / sc).tocsr()

    def chart(self, u, deg, tdeg):
        H = (self.H0 + sp.diags(u)).tocsr()
        lo, hi = self.m2 * 0.9, 9.0
        Gam = self.cheb_sqrt_inv(H, deg, lo, hi)
        G2 = (Gam @ Gam).tocsr()
        B = (self.Q @ G2 @ self.Q.T).tocsr()
        v = np.ones(B.shape[0], dtype=complex)
        for _ in range(60):
            v = B @ v
            v /= np.linalg.norm(v)
        sc = 1.05 * abs(np.vdot(v, B @ v))
        T = self.poly_inv(B, tdeg, sc=sc)
        Ut = (sp.identity(self.nl) - G2 @ self.Q.T @ T @ self.Q).tocsr()
        P0 = (self.U @ Ut @ Gam).tocsr()
        P0s = (P0.T @ H).tocsr()
        Ep = (P0 @ P0s @ self.U - self.U).tocsr()
        P = sp.hstack([P0, -Ep], format="csr")
        R = sp.vstack([P0s, sp.identity(self.nl, format="csr")], format="csr")
        return H, P0, P0s, Ep, P, R

    def link_dist(self, a, b):
        Sx, Sy = self.Sx, self.Sy
        xa, ya, xb, yb = (a // 2) // Sy, (a // 2) % Sy, (b // 2) // Sy, (b // 2) % Sy
        dx = min((xa - xb) % Sx, (xb - xa) % Sx)
        dy = min((ya - yb) % Sy, (yb - ya) % Sy)
        return dx + dy

    def ext_z(self, zlinks):
        """Ext_Z on vectors of Z: Q(c) u_0 goes on the crossing links of c off Z, uniformly."""
        zset = set(zlinks)
        rows, cols, vals = [], [], []
        Qcsr = self.Q
        for j, l in enumerate(zlinks):
            rows.append(l); cols.append(j); vals.append(1.0)
        Qz = Qcsr[:, zlinks].tocsc()
        for c in range(self.nb):
            free = [u for u in self.crossing[c] if u not in zset]
            col = Qz[c, :].tocoo()
            if col.nnz == 0:
                continue
            if not free:
                raise RuntimeError("a whole crossing set in Z")
            # weight of each free crossing link in Q(c) is 1 / L
            amp = self.L / len(free)
            for j, v in zip(col.col, col.data):
                for u in free:
                    rows.append(u); cols.append(j); vals.append(-v * amp)
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.nl, len(zlinks)))


def support_range(toy, M, row_links, col_map):
    """largest link distance of a nonzero entry of M, in the rows row_links."""
    worst = 0
    Mcsr = M.tocsr()
    for r in row_links:
        for idx in range(Mcsr.indptr[r], Mcsr.indptr[r + 1]):
            if abs(Mcsr.data[idx]) > 0:
                worst = max(worst, toy.link_dist(r, col_map(Mcsr.indices[idx])))
    return worst


def test_local(L, Nx, Ny, deg, tdeg, seed=20261031):
    # a long thin torus: long along Z, so far links exist; short across, to keep the sparse matrices small
    toy = Toy(L, Nx, Ny)
    S = toy.Sx
    rng = np.random.default_rng(seed)
    u0 = np.zeros(toy.nl)
    H, P0, P0s, Ep, P, R = toy.chart(u0, deg, tdeg)
    print(f"L={L} Nx={Nx} Ny={Ny} Sx={S} Sy={toy.Sy} links={toy.nl} deg={deg} tdeg={tdeg} nnz P={P.nnz} nnz R={R.nnz}", flush=True)
    check_rss()
    # EXACT
    v = rng.normal(size=toy.nl)
    ux = toy.U @ v
    res = P @ (R @ ux) - ux
    qp = abs(toy.Q @ P).max() if (toy.Q @ P).nnz else 0.0
    exact = np.linalg.norm(res) <= 1e-10 * np.linalg.norm(ux) and qp <= 1e-10
    print(f"EXACT |P R u - u| / |u| = {np.linalg.norm(res) / np.linalg.norm(ux):.2e}, |Q P|_max = {qp:.2e}: {'PASS-EXACT' if exact else 'FAIL-EXACT'}", flush=True)
    # RANGE on sampled rows
    rows_sample = list(rng.integers(0, toy.nl, size=40))
    rp = support_range(toy, P, rows_sample, lambda j: j % toy.nl)
    rr = support_range(toy, R, rows_sample, lambda j: j % toy.nl)
    bound = 2 * (2 * deg + 2 * (2 * L + 2) * 1 + (tdeg + 1) * (2 * deg + 4 * L + 4)) + 2 * deg + 4
    print(f"RANGE of P on sampled rows {rp}, of R {rr}, computed bound {bound}, long side {S}: "
          f"{'PASS-RANGE' if rp <= bound and rr <= bound else 'FAIL-RANGE'}{'' if 2 * bound < S else ' (twice the bound exceeds the long side)'}", flush=True)
    obs_range = bound
    # Z: a row of x-links, away from wrapping, and no whole crossing set
    y0 = 1
    nz = S - 3 * (2 * L)  # no wrap: leave free bonds at both ends
    if nz < 4 * obs_range:
        sys.exit(f"long side too short: nz = {nz}, range {obs_range}")
    x_a = 0
    zlinks = [toy.link((x_a + i) % S, y0, 0) for i in range(nz)]
    n_noise = 2 * toy.nl
    # a real (u, n)
    Ext = toy.ext_z(zlinks)
    u_real = rng.normal(size=len(zlinks))
    n_raw = rng.normal(size=n_noise)

    Res = sp.csr_matrix((np.ones(len(zlinks)), (np.arange(len(zlinks)), zlinks)), shape=(len(zlinks), toy.nl))

    def x_both(pot):
        H, P0, P0s, Ep, Pc, Rc = toy.chart(pot, deg, tdeg)
        y = Pc @ n_raw
        xr = Rc @ (Ext @ u_real) + (n_raw - Rc @ (Ext @ (Res @ y)))
        Pz = Pc[zlinks, :]
        Pzd = Pz[:, np.unique(Pz.nonzero()[1])]
        idx = np.unique(Pz.nonzero()[1])
        Pzd = Pzd.toarray()
        g = Pzd @ Pzd.T
        ncut = n_raw[idx]
        xo_c = Pzd.T @ np.linalg.solve(g, u_real) + (ncut - Pzd.T @ np.linalg.solve(g, Pzd @ ncut))
        pos = np.searchsorted(idx, c_link)
        return xr[c_link], xo_c[pos] if pos < len(idx) and idx[pos] == c_link else 0.0

    c_link = zlinks[nz // 2]  # the xi_0 coordinate at this link, for both coordinate systems
    step = 1e-30
    far = []
    for i in range(nz):
        j = zlinks[i]
        if toy.link_dist(j, c_link) > 2 * obs_range + 1:
            far.append(j)
    far = [zlinks[nz // 2 + i] for i in range(0, 151, 6) if nz // 2 + i < nz]
    rows = []
    for j in far:
        pot = np.zeros(toy.nl, dtype=complex)
        pot[j] = 1j * step
        xr_c, xo_c = x_both(pot)
        dr = abs(xr_c.imag) / step
        do = abs(np.imag(xo_c)) / step
        rows.append((toy.link_dist(j, c_link), dr, do))
        print(f"  j at distance {rows[-1][0]:3d}: |d x_c / d u_j|, strictly local R {dr:.2e}, orthogonal P_Z^+ {do:.2e}", flush=True)
        check_rss()
    r_obs = max([r[0] for r in rows if r[1] != 0.0], default=0)
    tail_r = max([r[1] for r in rows if r[0] > r_obs], default=0.0)
    tail_o = max([r[2] for r in rows if r[0] > r_obs], default=0.0)
    if r_obs > 78:
        v_tail = "FAIL-PROFILE"
    else:
        v_tail = "PASS-PROFILE" if tail_o > 1e-13 else "PROFILE-VOID"
    v_ctrl = f"r_obs={r_obs}"
    print(f"PROFILE r_obs = {r_obs}, beyond it R {tail_r:.2e}, orthogonal {tail_o:.2e}: {v_tail}", flush=True)
    return {"L": L, "Nx": Nx, "Ny": Ny, "deg": deg, "tdeg": tdeg, "exact": bool(exact), "range_P": int(rp), "range_R": int(rr), "bound": int(bound),
            "tail_r": float(tail_r), "tail_orth": float(tail_o), "v_tail": v_tail, "v_ctrl": v_ctrl}


def test_dense(L, Nb, deg, tdeg):
    toy = Toy(L, Nb)
    H, P0, P0s, Ep, P, R = toy.chart(np.zeros(toy.nl), deg, tdeg)
    P0d, Hd, Qd = P0.toarray(), H.toarray(), toy.Q.toarray()
    # X basis
    w, v = np.linalg.eigh(Qd.T @ Qd)
    Xb = v[:, w < 1e-10]
    AmX = Xb.T @ Hd @ Xb  # A + m^2 on X
    wa, va = np.linalg.eigh(AmX)
    C1h = va @ np.diag(wa ** -0.5) @ va.T
    C1hi = va @ np.diag(wa ** 0.5) @ va.T
    PX = Xb.T @ P0d
    Dl = C1hi @ (PX @ PX.T) @ C1hi - np.eye(Xb.shape[1])
    Eform = C1h @ Dl @ C1hi
    # E on X: P0 P0^T H - 1, in the basis of X
    Edir = PX @ (P0d.T @ Hd @ Xb) - np.eye(Xb.shape[1])
    relerr = np.linalg.norm(Edir - Eform) / max(np.linalg.norm(Eform), 1e-300)
    PpX = Xb.T @ P.toarray()
    Dl2 = C1hi @ (PpX @ PpX.T) @ C1hi - np.eye(Xb.shape[1])
    if not (np.isfinite(Dl).all() and np.isfinite(Dl2).all()):
        print(f"DENSE L={L} deg={deg} tdeg={tdeg}: not finite", flush=True)
        return {"L": L, "Nb": Nb, "deg": deg, "tdeg": tdeg, "relerr": float("inf"), "Delta": float("inf"), "Delta_prime": float("inf")}
    nd, nd2 = np.linalg.norm(Dl, 2), np.linalg.norm(Dl2, 2)
    print(f"DENSE L={L} Nb={Nb} deg={deg} tdeg={tdeg}: dim X = {Xb.shape[1]}, |E - formula| / |formula| = {relerr:.2e}, "
          f"||Delta|| = {nd:.3e}, ||Delta'|| = {nd2:.3e}, ||E||_2 = {np.linalg.norm(Edir, 2):.3e}", flush=True)
    check_rss()
    return {"L": L, "Nb": Nb, "deg": deg, "tdeg": tdeg, "relerr": float(relerr), "Delta": float(nd), "Delta_prime": float(nd2)}


def main():
    print("blas threads", os.environ.get("VECLIB_MAXIMUM_THREADS"), flush=True)
    out = {"local": [], "dense": []}
    out["local"].append(test_local(3, 160, 2, 1, 0))
    for deg, tdeg in ((8, 4), (16, 40), (30, 150), (45, 400)):
        out["dense"].append(test_dense(3, 4, deg, tdeg))
    best = min(out["dense"], key=lambda r: r["Delta"])
    v_formula = "PASS-FORMULA" if all(r["relerr"] <= 1e-8 for r in out["dense"] if np.isfinite(r["relerr"])) else "FAIL-FORMULA"
    if best["Delta"] >= 0.1:
        v_small = "NOT-REACHED"
    else:
        v_small = "PASS-SMALL" if best["Delta_prime"] <= 2 * best["Delta"] else "FAIL-SMALL"
    print(v_formula, v_small, f"best ||Delta|| = {best['Delta']:.3e}, ||Delta'|| = {best['Delta_prime']:.3e}", flush=True)
    out["v_formula"], out["v_small"] = v_formula, v_small
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hard-core--independent_local_inverse_results.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path, "rss GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3, flush=True)


if __name__ == "__main__":
    main()
