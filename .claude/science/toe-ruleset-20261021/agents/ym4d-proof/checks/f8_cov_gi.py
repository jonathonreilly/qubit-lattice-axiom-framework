"""f8 (lane C, session 5): Lemma COV-GI and Proposition COV-perp-C in a small-torus U(1) gauge chain.

Criteria: checks/f8_criteria.md (written before this script). Model: staple averaging map (stated there).
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f8_cov_gi.py > f8_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import time
import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp

L = 3
KAPPA = 1.0
T0 = time.time()


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- lattice helpers
def site_index(x, N, d):
    idx = 0
    for c in range(d):
        idx = idx * N + (x[c] % N)
    return idx


def all_sites(N, d):
    return np.array(list(itertools.product(range(N), repeat=d)), dtype=np.int64)


def ext_d(N, d):
    """0-forms -> 1-forms: (d lam)(x, mu) = lam(x + e_mu) - lam(x). Link index = site*d + mu."""
    S = all_sites(N, d)
    V = len(S)
    rows, cols, vals = [], [], []
    for s, x in enumerate(S):
        for mu in range(d):
            xp = x.copy(); xp[mu] += 1
            r = s * d + mu
            rows += [r, r]; cols += [site_index(xp, N, d), s]; vals += [1.0, -1.0]
    return sp.csr_matrix((vals, (rows, cols)), shape=(V * d, V))


def ext_d2(N, d):
    """1-forms -> plaquettes (mu < nu); also returns a flag array: plaquette in the (0,1) plane."""
    S = all_sites(N, d)
    rows, cols, vals, flag = [], [], [], []
    p = 0
    for s, x in enumerate(S):
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = x.copy(); xm[mu] += 1
                xn = x.copy(); xn[nu] += 1
                rows += [p] * 4
                cols += [s * d + mu, site_index(xm, N, d) * d + nu, site_index(xn, N, d) * d + mu, s * d + nu]
                vals += [1.0, 1.0, -1.0, -1.0]
                flag.append(mu == 0 and nu == 1)
                p += 1
    return sp.csr_matrix((vals, (rows, cols)), shape=(p, len(S) * d)), np.array(flag)


# ---------------------------------------------------------------- staple stencil (model averaging map)
def staple_stencil(d, mu, phi):
    """Stencil of the model map for a coarse link in direction mu (level-k units, relative to y = L y').
    Returns (dict {(offset tuple, nu): coefficient}, |m|)."""
    trans = [nu for nu in range(d) if nu != mu]
    paths = []
    for tv in itertools.product((-1, 0, 1), repeat=d - 1):
        t = np.zeros(d, dtype=np.int64)
        for nu, tn in zip(trans, tv):
            t[nu] = tn
        steps = []  # (start site (relative), direction, sign)
        # leg y -> y + t, increasing index order
        x = np.zeros(d, dtype=np.int64)
        for nu in range(d):
            for _ in range(abs(t[nu])):
                sg = 1 if t[nu] > 0 else -1
                steps.append((x.copy(), nu, sg)); x[nu] += sg
        for _ in range(L):
            steps.append((x.copy(), mu, 1)); x[mu] += 1
        # reverse of the axial leg z -> z + t, z = L e_mu
        z = np.zeros(d, dtype=np.int64); z[mu] = L
        leg = []
        xx = z.copy()
        for nu in range(d):
            for _ in range(abs(t[nu])):
                sg = 1 if t[nu] > 0 else -1
                leg.append((xx.copy(), nu, sg)); xx[nu] += sg
        for (xs, nu, sg) in reversed(leg):
            xe = xs.copy(); xe[nu] += sg  # traverse from xe back to xs: direction nu, sign -sg
            steps.append((xe, nu, -sg))
        # phase: A_1(x) = phi * x_0 (axis 0 = "1", axis 1 = "2"), relative to y
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


def staple_map(Nk, d, phi):
    """Sparse T_k(phi): level-k links (side Nk) -> level-(k+1) links (side Nk/L); and Pi_{k+1} (diag)."""
    Nc = Nk // L
    Sc = all_sites(Nc, d)
    rows, cols, vals = [], [], []
    pis = np.zeros(len(Sc) * d)
    sten = [staple_stencil(d, mu, phi) for mu in range(d)]
    for s, yp in enumerate(Sc):
        y = L * yp
        for mu in range(d):
            coef, mabs = sten[mu]
            r = s * d + mu
            pis[r] = mabs
            for (off, nu), c in coef.items():
                if abs(c) < 1e-300:
                    continue
                rows.append(r); cols.append(site_index(y + np.array(off), Nk, d) * d + nu); vals.append(c)
    Tm = sp.csr_matrix((vals, (rows, cols)), shape=(len(Sc) * d, len(all_sites(Nk, d)) * d))
    return Tm, pis


def chain(d, T, n, f, with_M=False):
    """Returns C_n (dense, level-n links), and optionally M = T_{n-1}...T_0 (sparse)."""
    N = [T * L ** (n - k) for k in range(n + 1)]
    maps, pis = [], []
    for k in range(n):
        if k == 0 and not with_M:
            # only Pi_1 is needed from level 0 (T_0 enters M only): from the stencil, tiled over level-1 links
            pi = np.tile(np.array([staple_stencil(d, mu, f)[1] for mu in range(d)]), N[1] ** d)
            maps.append(None); pis.append(pi)
        else:
            Tm, pi = staple_map(N[k], d, (L ** (2 * k)) * f)
            maps.append(Tm); pis.append(pi)
    En = N[n] ** d * d
    C = np.diag(1.0 / pis[n - 1]) / KAPPA  # j = n term (A_n = 1, Pi_n from level n-1)
    A = sp.identity(En, format="csr")
    for j in range(n - 1, 0, -1):  # A_j = A_{j+1} T_j
        A = (A @ maps[j]).tocsr()
        Pinv = sp.diags(1.0 / pis[j - 1])
        C = C + (A @ Pinv @ A.T).toarray() / KAPPA
    M = None
    if with_M:
        M = sp.identity(En, format="csr")
        for k in range(n - 1, -1, -1):
            M = (M @ maps[k]).tocsr()
    return C, M, N


def mean_zero_basis(V):
    Q, _ = np.linalg.qr(np.hstack([np.ones((V, 1)), np.eye(V)[:, : V - 1]]))
    return Q[:, 1:V]


def logdet_pd(X):
    c = sla.cho_factor(X, lower=True)
    return 2.0 * np.sum(np.log(np.diag(c[0])))


# ---------------------------------------------------------------- Part A
def part_A():
    log("=== Part A: exact identities (dense) ===")
    rng = np.random.default_rng(8)
    cases = [(2, 3, 1), (2, 3, 2), (3, 3, 1), (4, 2, 1)]
    ok = {"A0": True, "A1": True, "A2": True, "A3": True, "A4": True, "ctl": True}
    for (d, T, n) in cases:
        t0 = time.time()
        N0 = T * L ** n
        Nn = T
        S0 = all_sites(N0, d)
        V0, E0 = len(S0), len(S0) * d
        dd = ext_d(N0, d)
        d2, flag = ext_d2(N0, d)
        lvl = np.array([all(c % (L ** n) == 0 for c in x) for x in S0])
        interior = np.where(~lvl)[0]
        bnd = np.where(lvl)[0]
        # level-n site ordering: fine site L^n y' <-> coarse index of y'
        Sn = all_sites(Nn, d)
        bnd_order = np.array([site_index((L ** n) * y, N0, d) for y in Sn])
        # slice basis
        RdT = dd.T.tocsr()[interior, :].toarray()
        B = sla.null_space(RdT)  # E0 x dimS, orthonormal
        del RdT
        dimS = B.shape[1]
        # harmonic extension J
        Lap = (dd.T @ dd).toarray()
        Vn = len(Sn)
        U = mean_zero_basis(Vn)
        lam = np.zeros((V0, Vn - 1))
        lam[bnd_order, :] = U
        rhs = -Lap[np.ix_(interior, bnd_order)] @ U
        lam[interior, :] = np.linalg.solve(Lap[np.ix_(interior, interior)], rhs)
        del Lap
        J = dd @ lam  # E0 x (Vn-1), fine-link vectors (in S)
        dn = ext_d(Nn, d).toarray()
        D = dn @ U
        En = dn.shape[0]
        Wperp = sla.null_space(dn.T)  # ker d_n^T
        Zg = sla.orth(D)
        PG = Zg @ Zg.T
        Pp = np.eye(En) - PG
        Rr = rng.standard_normal((En, En))
        G = PG @ Rr @ Pp
        BJ = B.T @ J
        lnJJ = np.linalg.slogdet(J.T @ J)[1]
        lnDD = np.linalg.slogdet(D.T @ D)[1]
        A4vals = {}
        for f in (0.0, 0.03, 0.07, 0.01, 0.02):
            C, M, _ = chain(d, T, n, f, with_M=True)
            Cp = Pp @ C @ Pp + PG
            Cpp = (np.eye(En) + G) @ C @ (np.eye(En) + G).T
            cosw = np.where(flag, np.cos(f), 1.0)
            Hs = (d2.T @ sp.diags(cosw) @ d2).tocsr()
            HB = Hs @ B
            BHB = B.T @ HB
            MB = (M @ B)
            MJ = M @ J

            def lhs(Cx, Hc=BHB, want_min=False):
                Ci = np.linalg.inv(Cx)
                Aop = Hc + MB.T @ Ci @ MB
                Aop = 0.5 * (Aop + Aop.T)
                amin = sla.eigh(Aop, eigvals_only=True, subset_by_index=[0, 0])[0] if want_min else None
                return 0.5 * logdet_pd(Aop) + 0.5 * np.linalg.slogdet(Cx)[1], amin

            lc = lhs(C)[0]
            A4vals[f] = (lc, lhs(Cp)[0], 0.5 * np.linalg.slogdet(C)[1], lc - 0.5 * np.linalg.slogdet(C)[1])
            if f in (0.01, 0.02):
                continue
            # A0
            e_MJ = np.max(np.abs(MJ - D))
            e_HJ = np.max(np.abs(B.T @ (Hs @ J)))
            l0, amin = lhs(C, want_min=True)
            A0 = e_MJ <= 1e-12 and e_HJ <= 1e-12 and amin > 0
            # A1
            l1 = lhs(Cp)[0]; l2 = lhs(Cpp)[0]
            A1 = abs(l0 - l1) <= 1e-8 and abs(l0 - l2) <= 1e-8
            # A3
            Ci = np.linalg.inv(C)
            Pi2 = Ci - Ci @ D @ np.linalg.solve(D.T @ Ci @ D, D.T @ Ci)
            Pi1 = Wperp @ np.linalg.solve(Wperp.T @ C @ Wperp, Wperp.T)
            e_Pi = np.max(np.abs(Pi1 - Pi2)) / np.max(np.abs(Pi1))
            A3 = e_Pi <= 1e-10
            # A2
            Ar = BHB + MB.T @ Pi1 @ MB
            ev = np.linalg.eigvalsh(0.5 * (Ar + Ar.T))
            k = Vn - 1
            top = ev[-1]
            small_ok = np.all(np.abs(ev[:k]) <= 1e-9 * top) and ev[k] >= 1e-6 * top
            rhs_v = 0.5 * np.sum(np.log(ev[k:])) + 0.5 * logdet_pd(Wperp.T @ C @ Wperp) + 0.5 * lnDD - 0.5 * lnJJ
            A2 = abs(l0 - rhs_v) <= 1e-8 and small_ok
            # control: H + 0.3*1
            ctl_txt = ""
            if f == 0.03:
                Hc = BHB + 0.3 * np.eye(dimS)
                dctl = abs(lhs(C, Hc)[0] - lhs(Cp, Hc)[0])
                ctl_fail = dctl >= 1e-4
                ok["ctl"] &= ctl_fail
                ctl_txt = f" | ctl |dLHS|={dctl:.3e} ({'FAILS as required' if ctl_fail else 'DID NOT FAIL'})"
            ok["A0"] &= A0; ok["A1"] &= A1; ok["A2"] &= A2; ok["A3"] &= A3
            log(f"(d,T,n)=({d},{T},{n}) f={f:.2f} dimS={dimS} k={k}: |MJ-D|={e_MJ:.1e} |HJ|={e_HJ:.1e} minA={amin:.3e} "
                f"| LHS={l0:.10f} LHS-LHS'={l0 - l1:.1e} LHS-LHS''={l0 - l2:.1e} | RHS-LHS={rhs_v - l0:.1e} "
                f"ker(max {np.max(np.abs(ev[:k])) / top:.1e}, next {ev[k] / top:.1e}) | Pi rel {e_Pi:.1e}{ctl_txt}")
        if (d, T, n) in [(2, 3, 2), (4, 2, 1)]:
            # A4: Richardson f^2 coefficient per fine site, h = 0.01, 2h
            g0 = A4vals[0.0]
            h = 0.01
            coef = [(16 * (A4vals[h][i] - g0[i]) - (A4vals[2 * h][i] - g0[i])) / (12 * h * h) / V0 for i in range(4)]
            rel = abs(coef[0] - coef[1]) / abs(coef[0])
            ok["A4"] &= rel <= 1e-6
            log(f"  A4 (d,T,n)=({d},{T},{n}): f^2 coeff per fine site: full C_n {coef[0]:.10e}, C' {coef[1]:.10e} (rel {rel:.1e}); "
                f"info: 1/2 logdet C_n alone {coef[2]:.6e}, 1/2 logdet_S(H+M^T C^-1 M) alone {coef[3]:.6e}")
        log(f"  case time {time.time() - t0:.1f} s")
        del B
    for kk in ("A0", "A1", "A2", "A3", "A4"):
        log(f"({kk}) {'PASS' if ok[kk] else 'FAIL'}")
    log(f"(A-ctl) {'FAILS as required (A1 informative)' if ok['ctl'] else 'DID NOT FAIL: A1 NOT INFORMATIVE'}")


# ---------------------------------------------------------------- Part B
def perp_data(T, d):
    dn = ext_d(T, d).toarray()
    Vn = T ** d
    U = mean_zero_basis(Vn)
    D = dn @ U
    W = sla.null_space(dn.T)
    Z = sla.orth(D)
    return dn, W, Z


def part_B():
    log("=== Part B: chain on level-n links (d = 4) ===")
    d = 4
    res = {}
    okB1 = okB2 = True
    for (T, n) in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
        t0 = time.time()
        dn, W, Z = perp_data(T, d)
        C, _, N = chain(d, T, n, 0.0)
        ev = np.linalg.eigvalsh(W.T @ C @ W)
        pred = (1 - L ** (-2 * n)) / (1 - L ** (-2))
        e1 = np.max(np.abs(ev - pred)) / pred
        B1 = e1 <= 1e-10
        # B2
        v = dn[:, 0].copy()  # d_n delta_x at x = 0 (column of d_n)
        B2 = v @ C @ v >= n * (v @ v) * (1 - 1e-12)
        # B3
        Cb = np.linalg.inv(Z.T @ np.linalg.inv(C) @ Z)
        lamG = np.max(np.linalg.eigvalsh(Cb))
        okB1 &= B1; okB2 &= B2
        res[(T, n)] = {"lamG": lamG}
        log(f"T={T} n={n}: perp eigenvalues in [{ev.min():.15f}, {ev.max():.15f}] pred {pred:.15f} rel {e1:.1e} | "
            f"<v,Cv>/(n|v|^2)={v @ C @ v / (n * (v @ v)):.6f} | lam_max(C_G^flat)={lamG:.6f} "
            f"lam_max(PG C PG)={np.max(np.linalg.eigvalsh(Z.T @ C @ Z)):.6f} | {time.time() - t0:.1f} s")
    log(f"(B1) {'PASS' if okB1 else 'FAIL'}")
    log(f"(B2) {'PASS' if okB2 else 'FAIL'}")
    lg = [res[(2, n)]["lamG"] for n in (1, 2, 3)]
    rG = (lg[2] - lg[1]) / (lg[1] - lg[0])
    B3 = lg[0] < lg[1] < lg[2] and 0.5 <= rG <= 2.0
    log(f"(B3) lam_G(n=1,2,3) = {lg[0]:.6f}, {lg[1]:.6f}, {lg[2]:.6f}; r_G = {rG:.4f}: {'PASS' if B3 else 'FAIL'}")
    # B4
    T = 2
    dn, W, Z = perp_data(T, d)
    cperp, cfull = [], []
    status = "EVALUATED"
    for n in (1, 2, 3):
        t0 = time.time()
        V0 = (T * L ** n) ** d
        hn = 0.01 * L ** (-2 * (n - 1))
        g = {}
        for f in (0.0, hn / 2, hn, 2 * hn):
            C, _, _ = chain(d, T, n, f)
            g[f] = (0.5 * logdet_pd(W.T @ C @ W), 0.5 * np.linalg.slogdet(C)[1])
        def rich(h, i):
            return (16 * (g[h][i] - g[0.0][i]) - (g[2 * h][i] - g[0.0][i])) / (12 * h * h) / V0
        c1, c2 = rich(hn, 0), rich(hn / 2, 0)
        cons = abs(c1 - c2) / abs(c1)
        if cons > 1e-4:
            status = "NOT EVALUATED"
        cperp.append(c1); cfull.append(rich(hn, 1))
        # operator bounds at |f| = 0.05 L^{-2n}
        Cb, _, _ = chain(d, T, n, 0.05 * L ** (-2 * n))
        evb = np.linalg.eigvalsh(W.T @ Cb @ W)
        log(f"n={n}: c_perp={c1:.10e} (half-step {c2:.10e}, rel {cons:.1e}); info: c_full(1/2 logdet C_n)={cfull[-1]:.6e}; "
            f"perp spectrum at f=0.05 L^-2n: [{evb.min():.6f}, {evb.max():.6f}] | {time.time() - t0:.1f} s")
    if status == "NOT EVALUATED":
        log("(B4) NOT EVALUATED (Richardson consistency > 1e-4)")
    else:
        inc = abs(cperp[2] - cperp[1]) / abs(cperp[1] - cperp[0])
        B4 = abs(cperp[2] - cperp[1]) <= 0.5 * abs(cperp[1] - cperp[0]) and abs(cperp[2]) <= 2 * max(abs(cperp[0]), abs(cperp[1]))
        log(f"(B4) c_perp(1,2,3) = {cperp[0]:.6e}, {cperp[1]:.6e}, {cperp[2]:.6e}; increment ratio {inc:.4f}: {'PASS' if B4 else 'FAIL'}")
        log(f"     info: c_full(1,2,3) = {cfull[0]:.6e}, {cfull[1]:.6e}, {cfull[2]:.6e}")


if __name__ == "__main__":
    log(f"f8 start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC, L={L}, kappa={KAPPA}")
    part_A()
    log(f"Part A done at {time.time() - T0:.1f} s")
    part_B()
    log(f"total {time.time() - T0:.1f} s")
