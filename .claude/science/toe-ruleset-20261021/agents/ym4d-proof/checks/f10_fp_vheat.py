"""f10: Lemma FP-exact and Theorem V-heat (lane C, session 7).

Criteria: checks/f10_criteria.md (written before this script). Tests FLOW.md §50 (P2), (P3); proofs in §52, §53.
Part A: Lemma FP-exact on a charge-1 2D torus (9, 9), L = 3, NA-FP's axial-path slice at flux.
Part V: V1 the operator structure (i) against f9's SU(2) builder (imported read-only); V2, V3 the closed form (ii) against a
direct heat-trace computation with the formula operator; V4 against checks/f9_out.txt; V5 reported asymptotics.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys
sys.dont_write_bytecode = True
import re
import time
import resource
import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import ive

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f9_root_sector as f9  # read-only import: build_su2, theta_landau, adinv, links_of, all_sites, site_index

T0 = time.time()
RESULTS = []
H_FD = 1e-3


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    RESULTS.append((name, ok))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def j(nu, t):
    return ive(nu, 2.0 * np.asarray(t, dtype=float))


def realify_map(M):
    """complex-linear map w -> M w, with w = x1 - i x2 per complex dof, as a real matrix on interleaved (x1, x2)."""
    M = np.asarray(M)
    E = np.array([1.0, -1j])
    m, n = M.shape
    R = np.zeros((2 * m, 2 * n))
    for b in range(2):
        col = M * E[b]
        R[0::2, b::2] = np.real(col)
        R[1::2, b::2] = -np.imag(col)
    return R


def logdet_pos(A):
    s, v = np.linalg.slogdet(A)
    return v, s


def null_basis(A, tol=1e-10):
    u, s, vh = np.linalg.svd(A)
    r = int(np.sum(s > tol * max(1.0, s.max())))
    return vh[r:].conj().T


# ======================================================================== Part A: Lemma FP-exact
def fp_objects(dims, f, Lb=3):
    links, lidx = f9.links_of(dims, [True, True])
    X = f9.all_sites(dims)
    nS, nL = len(X), len(links)
    th = np.array([f9.theta_landau(X[a], mu, f, dims, True) for (a, mu, b) in links])
    Ub = np.exp(1j * th)
    # D_U lambda_b = U_b lambda(y) - lambda(x), b = (x -> y)
    D = np.zeros((nL, nS), complex)
    for k, (a, mu, b) in enumerate(links):
        D[k, b] += Ub[k]
        D[k, a] -= 1.0
    sidx = {tuple(x): i for i, x in enumerate(X)}
    cen = [i for i, x in enumerate(X) if x[0] % Lb == 1 and x[1] % Lb == 1]
    nc = len(cen)
    hmat = np.zeros((nc, nL), complex)
    Mmat = np.zeros((nc, nS), complex)
    for ic, c in enumerate(cen):
        cx = X[c]
        terms = 0
        for order in ((0, 1), (1, 0)):
            for d0 in (-1, 0, 1):
                for d1 in (-1, 0, 1):
                    delta = {0: d0, 1: d1}
                    cur = cx.copy()
                    T = 1.0 + 0j
                    row = np.zeros(nL, complex)
                    for mu in order:
                        st = int(np.sign(delta[mu]))
                        for _ in range(abs(delta[mu])):
                            nxt = cur.copy(); nxt[mu] += st
                            if st > 0:
                                k = lidx[(sidx[tuple(np.mod(cur, dims))], mu)]
                                row[k] += T
                                T = T * Ub[k]
                            else:
                                k = lidx[(sidx[tuple(np.mod(nxt, dims))], mu)]
                                row[k] += -T * np.conj(Ub[k])
                                T = T * np.conj(Ub[k])
                            cur = nxt
                    y = sidx[tuple(np.mod(cur, dims))]
                    hmat[ic] += row
                    Mmat[ic, y] += T
                    terms += 1
        hmat[ic] /= terms
        Mmat[ic] /= terms
    # covariant plaquette sum c_U (rows = plaquettes), for B
    rows = []
    for a in range(nS):
        x = X[a]
        k1 = lidx[(a, 0)]
        xp = x.copy(); xp[0] += 1
        k2 = lidx[(sidx[tuple(np.mod(xp, dims))], 1)]
        xq = x.copy(); xq[1] += 1
        k3 = lidx[(sidx[tuple(np.mod(xq, dims))], 0)]
        k4 = lidx[(a, 1)]
        r = np.zeros(nL, complex)
        r[k1] += 1.0
        r[k2] += Ub[k1]
        r[k3] += -Ub[k1] * Ub[k2] * np.conj(Ub[k3])
        r[k4] += -Ub[k1] * Ub[k2] * np.conj(Ub[k3]) * np.conj(Ub[k4])
        rows.append(r)
    cU = np.array(rows)
    return dict(D=D, h=hmat, M=Mmat, cen=cen, cU=cU, nS=nS, nL=nL)


def part_a():
    say("Part A (Lemma FP-exact; charge-1 torus (9, 9), L = 3, axial-path slice of NA-FP)")
    dims = (9, 9)
    rng = np.random.default_rng(7)
    for kq in (1, 3):
        f = 2 * np.pi * kq / 81.0
        O = fp_objects(dims, f)
        O0 = fp_objects(dims, 0.0)
        D, h, M, cen = O["D"], O["h"], O["M"], O["cen"]
        nS = O["nS"]
        non = np.array([i for i in range(nS) if i not in set(cen)])
        # A0
        a0 = 0.0
        for _ in range(3):
            lam = rng.normal(size=nS) + 1j * rng.normal(size=nS)
            a0 = max(a0, np.abs(h @ (D @ lam) - (M @ lam - lam[cen])).max())
        verdict(f"A0 (k = {kq})", a0 <= 1e-12, f"max |h(D lam) - (M lam - lam(c))| = {a0:.1e}")

        def build(Oo):
            Dd, hh, MM = Oo["D"], Oo["h"], Oo["M"]
            G = Dd[:, non]                       # Gamma = D|_{Lambda'}
            Mp = MM[:, non]
            Nres = null_basis(Mp)               # Lambda_res (complex, orthonormal)
            Nperp = sla.orth(Mp.conj().T)       # Lambda' minus Lambda_res
            chiG = np.vstack([hh @ G, Nres.conj().T @ (G.conj().T @ G)])
            return G, Mp, Nres, Nperp, chiG, hh
        G, Mp, Nres, Nperp, chiG, hh = build(O)
        G0, _, _, _, chiG0, hh0 = build(O0)
        GR = realify_map(G)
        S0 = null_basis(GR.T)                   # real orthonormal basis of S_0 = (Gamma Lambda')^perp
        cR = realify_map(O["cU"])
        Bm = cR.T @ cR + 0.3 * np.eye(cR.shape[1])
        P0 = S0 @ S0.T
        Q = P0 @ Bm @ P0
        NresR = realify_map(Nres)
        Ofull = Q + GR @ NresR @ NresR.T @ GR.T
        hR = realify_map(hh)
        H0 = null_basis(hR)
        chiR = realify_map(chiG)
        sv = np.linalg.svd(chiR, compute_uv=False)
        verdict(f"A1 (k = {kq})", sv.min() >= 1e-6, f"sigma_min(chi Gamma) = {sv.min():.3e}")
        lo, _ = logdet_pos(H0.T @ Ofull @ H0)
        lhh, _ = logdet_pos(hR @ hR.T)
        lchi = np.linalg.slogdet(chiR)[1]
        LHS = 0.5 * lo + 0.5 * lhh - lchi
        lq, _ = logdet_pos(S0.T @ Q @ S0)
        ld, _ = logdet_pos(GR.T @ GR)
        RHS = 0.5 * lq - 0.5 * ld
        verdict(f"A2 (k = {kq})", abs(LHS - RHS) <= 1e-8 * (1 + abs(RHS)),
                f"LHS = {LHS:.12f}, RHS = {RHS:.12f}, |diff| = {abs(LHS - RHS):.1e}")
        fM = np.linalg.slogdet(realify_map(Mp @ Nperp))[1]
        fP = np.linalg.slogdet(realify_map(Nres.conj().T @ (G.conj().T @ G) @ Nres))[1]
        verdict(f"A3 (k = {kq})", abs(lchi - fM - fP) <= 1e-8, f"|log|det chiG| - log det M_perp - log det P_res Delta' P_res| = {abs(lchi - fM - fP):.1e}")
        lam_min = np.linalg.eigvalsh(H0.T @ Ofull @ H0).min()
        verdict(f"A4 (k = {kq})", lam_min > 0, f"lambda_min(Pi O Pi | ker h) = {lam_min:.3e}")
        hR0 = realify_map(hh0)
        LHSc = 0.5 * lo + 0.5 * logdet_pos(hR0 @ hR0.T)[0] - np.linalg.slogdet(realify_map(chiG0))[1]
        verdict(f"A-ctl (k = {kq}) (must FAIL A2)", abs(LHSc - RHS) >= 1e-4, f"|LHS_ctl - RHS| = {abs(LHSc - RHS):.3e}")
        say(f"    A5 (reported): log det(hh*) = {lhh:.6f} (f = 0: {logdet_pos(hR0 @ hR0.T)[0]:.6f}); "
            f"log|det chiG| = {lchi:.6f} (f = 0: {np.linalg.slogdet(realify_map(chiG0))[1]:.6f})")


# ======================================================================== Part V: the vector operator
def plaquettes(dims, periodic, lidx):
    X = f9.all_sites(dims)
    out = []
    for a in range(len(X)):
        x = X[a]
        if (a, 0) not in lidx or (a, 1) not in lidx:
            continue
        xm = x.copy(); xm[0] += 1
        xn = x.copy(); xn[1] += 1
        if (not periodic[0] and xm[0] >= dims[0]) or (not periodic[1] and xn[1] >= dims[1]):
            continue
        am = int(f9.site_index(xm[None], dims)[0]); an = int(f9.site_index(xn[None], dims)[0])
        if (am, 1) not in lidx or (an, 0) not in lidx:
            continue
        out.append((lidx[(a, 0)], lidx[(am, 1)], lidx[(an, 0)], lidx[(a, 1)]))
    return np.array(out)


def formula_ops(dims, periodic, f, seam, q, Cfun, Sfun, spin=True):
    """H_C = sum_p [C_p c_p^* c_p + S_p Spin_p], D_C (left chart, complex root coordinate), from the plaquette transports."""
    links, lidx = f9.links_of(dims, periodic)
    X = f9.all_sites(dims)
    nL, nS = len(links), len(X)
    th = np.array([f9.theta_landau(X[a], mu, f, dims, seam) for (a, mu, b) in links])
    P = plaquettes(dims, periodic, lidx)
    t1, t2, t3, t4 = (th[P[:, i]] for i in range(4))
    Phi = t1 + t2 - t3 - t4
    kap = np.stack([np.ones(len(P)), np.exp(1j * q * t1), -np.exp(1j * q * (t1 + t2 - t3)), -np.exp(1j * q * Phi)], axis=1)
    Cp, Sp = Cfun(Phi), (Sfun(Phi) if spin else 0.0 * Phi)
    rows, cols, vals = [], [], []
    for i in range(4):
        for k in range(4):
            sgn = 0.0 if i == k else (1.0 if i < k else -1.0)
            v = np.conj(kap[:, i]) * kap[:, k] * (Cp + Sp * sgn / 2j)
            rows.append(P[:, i]); cols.append(P[:, k]); vals.append(v)
    H = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(nL, nL))
    dr, dc, dv = [], [], []
    for k, (a, mu, b) in enumerate(links):
        dr += [k, k]; dc += [a, b]; dv += [1.0, -np.exp(1j * q * th[k])]
    D = sp.csr_matrix((dv, (dr, dc)), shape=(nL, nS))
    return H, D, links, lidx, X, th


def part_v1():
    say("Part V1 (structure (i), SU(2): f9's Wilson Hessian vs the formula, left chart, w = x1 - i x2)")
    cases = [("torus (9, 9), one quantum", (9, 9), [True, True], 2 * np.pi / 81, True),
             ("open box 11^2, f = 0.07", (11, 11), [False, False], 0.07, False)]
    for label, dims, per, f, seam in cases:
        S = f9.build_su2(dims, per, f, seam=seam)
        nL, nS = S["nL"], S["nS"]
        th = np.array([f9.theta_landau(S["X"][a], mu, f, dims, seam) for (a, mu, b) in S["links"]])
        Rl = f9.adinv(th)                   # Ad(U^{-1}) per link: X_right = R X_left
        Rs = f9.adinv(np.array([0.0] * nS))  # identity for sites
        Rbig = sp.block_diag([Rl[k] for k in range(nL)]).tocsr()
        Hl = (Rbig.T @ S["H"] @ Rbig).toarray()
        Dl = (Rbig.T @ S["D0"]).toarray()
        rootL = np.sort(np.concatenate([3 * np.arange(nL), 3 * np.arange(nL) + 1]))
        rootS = np.sort(np.concatenate([3 * np.arange(nS), 3 * np.arange(nS) + 1]))
        Hroot = Hl[np.ix_(rootL, rootL)]
        Droot = Dl[np.ix_(rootL, rootS)]
        for spin, nm in ((True, ""), (False, "-ctl (S_p := 0; must FAIL)")):
            Hc, Dc, *_ = formula_ops(dims, per, f, seam, 2.0, np.cos, lambda x: 2 * np.sin(x), spin=spin)
            dH = np.abs(Hroot - realify_map(Hc.toarray())).max()
            dD = np.abs(Droot - realify_map(Dc.toarray())).max()
            if spin:
                verdict(f"V1 {label}", dH <= 1e-12 and dD <= 1e-12, f"max |H diff| = {dH:.1e}, max |D diff| = {dD:.1e} (max |H| = {np.abs(Hroot).max():.2f})")
                hd = np.abs((Hc @ Dc).toarray()).max()
                say(f"    (reported) max |H_C D_C| (formula) = {hd:.1e}")
            else:
                verdict(f"V1{nm} {label}", dH >= 1e-3, f"max |H diff| = {dH:.3e}")


def closed_form(t, gam):
    t = np.asarray(t, float)
    rho = j(1, t) / j(0, t)
    return (1 + rho) ** 2 - rho ** 2 / 3 + rho / (2 * t) + 4 * gam * (1 - rho) / t


def direct_R12(q, Cfun, Sfun, B, ts):
    tmax = ts.max()
    num = int(round(tmax / 0.5)) + 1
    grid = np.linspace(0, tmax, num)
    pick = [int(np.argmin(abs(grid - t))) for t in ts]
    c = B // 2
    Y = []
    for fv in (0.0, H_FD, 2 * H_FD):
        Hc, Dc, links, lidx, X, th = formula_ops((B, B), [False, False], fv, False, q, Cfun, Sfun)
        K = (Hc + Dc @ Dc.conj().T).tocsr()
        sc = int(f9.site_index(np.array([[c, c]]), (B, B))[0])
        acc = 0.0
        for mu in range(2):
            e = np.zeros(K.shape[0], complex); e[lidx[(sc, mu)]] = 1.0
            V = spla.expm_multiply(-K, e, start=0.0, stop=tmax, num=num, endpoint=True)
            acc = acc + np.real(V @ e.conj())[pick]
        Y.append(acc)
    cv = f9.richardson(*Y, H_FD)
    return cv / (q ** 2 * ts ** 2 * j(0, ts) ** 2), np.abs(Y[0] / (2 * j(0, ts) ** 2) - 1).max()


def part_v2_v5():
    ts = np.array([2, 3, 4, 6, 8, 12, 16, 24], float)
    B = 101
    say("Part V2 (closed form, SU(2), direct heat trace of the formula operator, open box 101^2, q = 2)")
    R2, nrm = direct_R12(2.0, np.cos, lambda x: 2 * np.sin(x), B, ts)
    cf = closed_form(ts, 1 / 8)
    for t, a, b in zip(ts, R2, cf):
        say(f"    t = {t:4.0f}: R_12 direct = {a:.7f}, closed form = {b:.7f}")
    rel = np.abs(R2 / cf - 1).max()
    verdict("V2", rel <= 1e-5, f"max rel deviation = {rel:.1e} (normalisation |Y(0)/(2 j0^2) - 1| = {nrm:.1e})")
    say("Part V3 (closed form, gamma = 1/4: SU(3) root (1, 2) of i sqrt(3/2) diag(1, 0, -1), q = sqrt(3/2))")
    q3 = np.sqrt(1.5)
    C3 = lambda x: 0.5 * (np.cos(q3 * x) + 1.0)
    S3 = lambda x: np.sin(q3 * x)
    R3, _ = direct_R12(q3, C3, S3, B, ts)
    cf3 = closed_form(ts, 1 / 4)
    for t, a, b in zip(ts, R3, cf3):
        say(f"    t = {t:4.0f}: R_12 direct = {a:.7f}, closed form = {b:.7f}")
    rel3 = np.abs(R3 / cf3 - 1).max()
    verdict("V3", rel3 <= 1e-5, f"max rel deviation = {rel3:.1e}")
    say("Part V4 (closed form vs checks/f9_out.txt printed values)")
    txt = open(os.path.join(HERE, "f9_out.txt")).read()
    pat = re.compile(r"t =\s+(\d+): R_12 = ([\d.]+), R_S = (-?[\d.]+)")
    rows = [(float(a), float(b), float(c)) for a, b, c in pat.findall(txt)]
    tt = np.array([r[0] for r in rows])
    d12 = np.abs(np.array([r[1] for r in rows]) - closed_form(tt, 1 / 8)).max()
    rho = j(1, tt) / j(0, tt)
    dS = np.abs(np.array([r[2] for r in rows]) + rho ** 2 / 6).max()
    verdict("V4", len(rows) == 8 and max(d12, dS) <= 3e-6, f"{len(rows)} rows; max |R_12 diff| = {d12:.1e}, max |R_S diff| = {dS:.1e}")
    say("Part V5 (reported: closed-form asymptotics, SU(2))")
    for t in (1e2, 1e3, 1e4):
        r12 = closed_form(t, 1 / 8)
        rs = -(j(1, t) / j(0, t)) ** 2 / 6
        say(f"    t = {t:.0e}: R_12 = {r12:.8f}, R_12 + R_S = {r12 + rs:.8f}, R_V4D = {r12 + 2 * rs:.8f}, t(R_12 - 11/3) = {t * (r12 - 11 / 3):.6f}")


if __name__ == "__main__":
    say(f"f10_fp_vheat.py  start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC")
    for part in (part_a, part_v1, part_v2_v5):
        t1 = time.time()
        part()
        say(f"  ({part.__name__}: {time.time() - t1:.1f} s)")
    npass = sum(ok for _, ok in RESULTS)
    say(f"SUMMARY: {npass}/{len(RESULTS)} verdict lines PASS (controls are counted as PASS when they fail as required)")
    say("  " + "; ".join(f"{n}: {'PASS' if ok else 'FAIL'}" for n, ok in RESULTS))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
    say(f"end {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC  wall {time.time() - T0:.1f} s  peak RSS {rss:.0f} MB")
