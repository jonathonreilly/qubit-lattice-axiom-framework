"""f8b (lane C, session 5; POST-HOC amendment A1 of checks/f8_criteria.md): model 2, the full-box staple map.

Reuses f8_cov_gi.py's code unchanged, replacing only the stencil (model 2), and adds the B1'a, B1'b, B4' tests.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import time
import numpy as np
import scipy.sparse as sp
import f8_cov_gi as base

L = base.L
log = base.log
T0 = time.time()


def fullbox_stencil(d, mu, phi):
    """Model 2: t over the full box {-1,0,1}^d; legs axial in increasing index order (independent of mu)."""
    paths = []
    for tv in itertools.product((-1, 0, 1), repeat=d):
        t = np.array(tv, dtype=np.int64)
        steps = []
        x = np.zeros(d, dtype=np.int64)
        for nu in range(d):
            for _ in range(abs(t[nu])):
                sg = 1 if t[nu] > 0 else -1
                steps.append((x.copy(), nu, sg)); x[nu] += sg
        for _ in range(L):
            steps.append((x.copy(), mu, 1)); x[mu] += 1
        z = np.zeros(d, dtype=np.int64); z[mu] = L
        leg = []
        xx = z.copy()
        for nu in range(d):
            for _ in range(abs(t[nu])):
                sg = 1 if t[nu] > 0 else -1
                leg.append((xx.copy(), nu, sg)); xx[nu] += sg
        for (xs, nu, sg) in reversed(leg):
            xe = xs.copy(); xe[nu] += sg
            steps.append((xe, nu, -sg))
        ph = 0.0
        for (xs, nu, sg) in steps:
            if nu == 1:
                ph += sg * phi * xs[0]
        paths.append((steps, ph))
    w = 1.0 / len(paths)
    m = sum(w * np.exp(1j * ph) for _, ph in paths)
    coef = {}
    for steps, ph in paths:
        om = w * np.real(np.exp(1j * ph) * np.conj(m)) / abs(m) ** 2
        for (xs, nu, sg) in steps:
            if sg > 0:
                key = (tuple(xs), nu); c = 1.0
            else:
                xb = xs.copy(); xb[nu] -= 1
                key = (tuple(xb), nu); c = -1.0
            coef[key] = coef.get(key, 0.0) + om * c
    return coef, abs(m)


base.staple_stencil = fullbox_stencil  # model 2 everywhere in base


def qbox_map(Nk, d):
    """Q_box built directly from its definition: (1/L^d) sum_{t in box} sum_{j<L} xi_mu(y + t + j e_mu)."""
    Nc = Nk // L
    Sc = base.all_sites(Nc, d)
    rows, cols, vals = [], [], []
    for s, yp in enumerate(Sc):
        y = L * yp
        for mu in range(d):
            r = s * d + mu
            for tv in itertools.product((-1, 0, 1), repeat=d):
                for j in range(L):
                    z = y + np.array(tv); z[mu] += j
                    rows.append(r); cols.append(base.site_index(z, Nk, d) * d + mu); vals.append(1.0 / L ** d)
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(Sc) * d, len(base.all_sites(Nk, d)) * d))


def part_B2():
    log("=== Part B' (model 2, d = 4) ===")
    d = 4
    T = 2
    dn, W, Z = base.perp_data(T, d)
    Pp = W @ W.T
    # B1'a and B1'b (operator facts), top torus T = 2
    okA = okB = True
    for m in (1, 2):
        Ns = [T * L ** (m - i) for i in range(m + 1)]  # sides from level n-m (index 0) to level n
        Q2 = sp.identity(dn.shape[0], format="csr")
        Qb = sp.identity(dn.shape[0], format="csr")
        for i in range(m - 1, -1, -1):
            Tm, _ = base.staple_map(Ns[i], d, 0.0)
            Q2 = (Q2 @ Tm).tocsr()
            Qb = (Qb @ qbox_map(Ns[i], d)).tocsr()
        diff = (Q2 - Qb).tocsc()
        emax = 0.0
        ncol = diff.shape[1]
        for c0 in range(0, ncol, 20000):
            blk = Pp @ diff[:, c0:c0 + 20000].toarray()
            emax = max(emax, np.max(np.abs(blk)))
        QQ = (Qb @ Qb.T).toarray()
        nrm = np.max(np.linalg.eigvalsh(Pp @ QQ @ Pp))
        a_ok = emax <= 1e-12
        b_ok = nrm <= L ** (-2 * m) * (1 + 1e-12)
        okA &= a_ok; okB &= b_ok
        log(f"m={m}: max|P_perp(Q2^m - Qbox^m)| = {emax:.2e}; ||P_perp Qbox^m Qbox^mT P_perp|| = {nrm:.12f} "
            f"(bound L^-2m = {L ** (-2 * m):.12f}); max|Q2^m-Qbox^m| (no P_perp, info) = {abs(diff).max():.3e}")
    upper = 1.0 / (1 - L ** (-2))
    specs = {}
    lamG = {}
    for (Tt, n) in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
        t0 = time.time()
        dnn, Wt, Zt = base.perp_data(Tt, d)
        C, _, _ = base.chain(d, Tt, n, 0.0)
        ev = np.linalg.eigvalsh(Wt.T @ C @ Wt)
        sp_ok = ev.min() >= 1 - 1e-12 and ev.max() <= upper * (1 + 1e-12)
        okB &= sp_ok
        specs[(Tt, n)] = C
        if Tt == 2:
            Cb = np.linalg.inv(Zt.T @ np.linalg.inv(C) @ Zt)
            lamG[n] = np.max(np.linalg.eigvalsh(Cb))
        log(f"T={Tt} n={n}: perp spectrum [{ev.min():.12f}, {ev.max():.12f}] (allowed [1, {upper:.12f}]) "
            f"{'ok' if sp_ok else 'VIOLATED'} | {time.time() - t0:.1f} s")
    D32 = Pp @ (specs[(2, 3)] - specs[(2, 2)]) @ Pp
    e32 = np.linalg.eigvalsh(0.5 * (D32 + D32.T))
    inc_ok = e32.min() >= -1e-12 and e32.max() <= L ** (-4) * (1 + 1e-12)
    okB &= inc_ok
    log(f"P_perp(C_3 - C_2)P_perp spectrum [{e32.min():.3e}, {e32.max():.12f}] (bound L^-4 = {L ** -4:.12f}) "
        f"{'ok' if inc_ok else 'VIOLATED'}")
    log(f"(B1'a) {'PASS' if okA else 'FAIL'}")
    log(f"(B1'b) {'PASS' if okB else 'FAIL'}")
    log(f"info: lam_max(C_G^flat), n=1,2,3 (T=2): {lamG[1]:.6f}, {lamG[2]:.6f}, {lamG[3]:.6f}")
    # B4'
    cperp, cfull = [], []
    status = "EVALUATED"
    for n in (1, 2, 3):
        t0 = time.time()
        V0 = (T * L ** n) ** d
        hn = 0.01 * L ** (-2 * (n - 1))
        g = {}
        for f in (0.0, hn / 2, hn, 2 * hn):
            C, _, _ = base.chain(d, T, n, f)
            g[f] = (0.5 * base.logdet_pd(W.T @ C @ W), 0.5 * np.linalg.slogdet(C)[1])

        def rich(h, i):
            return (16 * (g[h][i] - g[0.0][i]) - (g[2 * h][i] - g[0.0][i])) / (12 * h * h) / V0
        c1, c2 = rich(hn, 0), rich(hn / 2, 0)
        cons = abs(c1 - c2) / abs(c1)
        if cons > 1e-4:
            status = "NOT EVALUATED"
        cperp.append(c1); cfull.append(rich(hn, 1))
        Cb, _, _ = base.chain(d, T, n, 0.05 * L ** (-2 * n))
        evb = np.linalg.eigvalsh(W.T @ Cb @ W)
        log(f"n={n}: c_perp={c1:.10e} (half-step {c2:.10e}, rel {cons:.1e}); info: c_full={cfull[-1]:.6e}; "
            f"perp spectrum at f=0.05 L^-2n: [{evb.min():.6f}, {evb.max():.6f}] | {time.time() - t0:.1f} s")
    if status == "NOT EVALUATED":
        log("(B4') NOT EVALUATED (Richardson consistency > 1e-4)")
    else:
        inc = abs(cperp[2] - cperp[1]) / abs(cperp[1] - cperp[0])
        B4 = abs(cperp[2] - cperp[1]) <= 0.5 * abs(cperp[1] - cperp[0]) and abs(cperp[2]) <= 2 * max(abs(cperp[0]), abs(cperp[1]))
        log(f"(B4') c_perp(1,2,3) = {cperp[0]:.6e}, {cperp[1]:.6e}, {cperp[2]:.6e}; increment ratio {inc:.4f}: {'PASS' if B4 else 'FAIL'}")
        log(f"     info: c_full(1,2,3) = {cfull[0]:.6e}, {cfull[1]:.6e}, {cfull[2]:.6e}")


if __name__ == "__main__":
    log(f"f8b start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC (model 2, POST-HOC amendment A1)")
    log("--- (A') Part A of f8 with model 2 ---")
    base.part_A()
    log(f"Part A' done at {time.time() - T0:.1f} s")
    part_B2()
    log(f"total {time.time() - T0:.1f} s")
