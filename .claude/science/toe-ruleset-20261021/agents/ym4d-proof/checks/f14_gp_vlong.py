"""f14 (lane C, session 11): FLOW.md §84 check f14.

Criteria: checks/f14_criteria.md (written before this script).
Part A: the explicit b_n, w_n of FLOW §75 (implemented from the text) against f12's T_n - I_n (finite-torus identity),
        Ward identities at P = 0, and a sign-flip control.
Part B: Proposition G2-log (the log l slope of the regular part of iota^* Delta^{-2} iota) and the straight-path map
        (U2 inequality, transverse growth SP-div).
Part C: the scalar model P_n = -log det Delta_U - 1/2 log det G2_U: brute-force test at n = 1 and the n-dependence of the
        level polarisation y_n(P).
f12 functions are executed UNCHANGED from checks/f12_proxy_2pt.py (md5 printed).
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f14_gp_vlong.py > f14_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import hashlib
import time
import numpy as np
from scipy.special import gammainc, gamma as Gam
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.dont_write_bytecode = True
L = 3
CG = 1.0 / (96 * np.pi ** 2)
SLOPE = np.log(L) / (8 * np.pi ** 2)
SMOKE = os.environ.get("F14_SMOKE") == "1"
T0 = time.time()
VERD = []
HERE = os.path.dirname(os.path.abspath(__file__))


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    VERD.append((name, bool(ok)))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def load_f12():
    path = os.path.join(HERE, "f12_proxy_2pt.py")
    src = open(path, "rb").read()
    ns = {"__name__": "f12mod", "__file__": path}
    exec(compile(src, path, "exec"), ns)
    return ns, hashlib.md5(src).hexdigest()


F12, MD5 = load_f12()
lam1 = F12["lam1"]; D1 = F12["D1"]; G1 = F12["G1"]; H2 = F12["H2"]; F1sq = F12["F1sq"]; F1pair = F12["F1pair"]
F2cos = F12["F2cos"]; c_level = F12["c_level"]; c2_vertex = F12["c2_vertex"]; Fibre = F12["Fibre"]
times = F12["times"]; shifted = F12["shifted"]; integrand = F12["integrand"]; gkind = F12["gkind"]


def sc(t, c):
    return [(c * a, g) for a, g in t]


# =============================================================== Part A: b_n, w_n from the text of §75
def level_data(n, Ks, P, h_u=0.3, flip=False):
    """gamma_n(K), gamma_n(K+P), b_n(K;P), w_n(K;P) in level units, from FLOW §75 (fibre sums via f12's Fibre)."""
    l = L ** n
    p = P / l
    Fp = Fibre(n, Ks, p, h_u=h_u)
    Fm = Fibre(n, Ks, -p, h_u=h_u)
    q1, q2, q3, q4 = Fp.q
    one = [np.ones_like(x) for x in Fp.q]
    d = [(1.0, [D1(q1, n), D1(q2, n), D1(q3, n), D1(q4, n)])]
    dp = [(1.0, [D1(q1, n), D1(q2 + p, n), D1(q3, n), D1(q4, n)])]
    sig = [(float(l), [2 * np.sin(q1), one[1], one[2], one[3]])]           # sigma = l * 2 sin(x_1/l)
    what = [(1.0, [2 * np.cos(q1), one[1], one[2], one[3]])]               # w-hat = 2 cos(x_1/l)
    d3, d4 = D1(q3, n), D1(q4, n)
    ut = [(1.0 / l, [G1(q1, n, k), H2(q2, p, n, k), d3, d4]) for k in range(n)]            # u~ = u(k_m; p)/l
    utm = [(1.0 / l, [G1(q1, n, k), H2(q2 + p, -p, n, k), d3, d4]) for k in range(n)]     # u~^- = u(k_m + p e2; -p)/l
    utmm = [(1.0 / l, [G1(q1, n, k), H2(q2 - p, p, n, k), d3, d4]) for k in range(n)]     # u~^(-) = u(k_m - p e2; p)/l
    m2 = [(-1.0, [F1sq(q1, n, k), D1(q2, n), d3, d4]) for k in range(n)]
    for k in range(n):
        for k2 in range(k + 1, n):
            f2 = sum(F2cos(q2, p, n, i, i2) for i in (k, k + 1) for i2 in (k2, k2 + 1))
            m2.append((-0.5, [F1pair(q1, n, k, k2), f2, d3, d4]))
    mt = sc(m2, 1.0 / l ** 2)                                                              # m~ = m_2/l^2
    cn = l ** 2 * c_level(n)
    c2 = c2_vertex(n, p)
    # level sums: sum_m X / (lt^a lt'^b) = l^{-2(a+b)} fsum(X, "ab")
    S = lambda F, X, kind: F.fsum(X, kind) * float(l) ** (-2 * (int(kind[0]) + int(kind[1])))
    gam = S(Fp, times(d, d), "10") + cn
    gamp = S(Fp, times(dp, dp), "01") + cn
    sgn = -1.0 if flip else 1.0
    b = sgn * S(Fp, times(dp, utm), "01") + S(Fp, times(ut, d), "10") - S(Fp, times(times(dp, sig), d), "11")
    w = (2 * S(Fp, times(d, mt), "10") - S(Fp, times(times(d, d), what), "20") + c2
         + S(Fp, times(times(sig, sig), times(d, d)), "21") - 2 * S(Fp, times(times(sig, d), utm), "11")
         + S(Fp, times(utm, utm), "01")
         + S(Fm, times(times(sig, sig), times(d, d)), "21") - 2 * S(Fm, times(times(sig, d), utmm), "11")
         + S(Fm, times(utmm, utmm), "01"))
    return gam, gamp, b, w, Fp


def part_a():
    say("Part A (b_n, w_n of FLOW §75 against f12's T_n - I_n; Ward identities; control)")
    N = 6 if SMOKE else 8
    ns = (1, 2) if SMOKE else (1, 2, 3, 4)
    Ks = [shifted(N)] * 4
    for n in ns:
        l = L ** n
        for j in (1, 2):
            P = 2 * np.pi * j / N
            p = P / l
            t0 = time.time()
            LHS = integrand(n, Ks, p).mean()
            gam, gamp, b, w, Fp = level_data(n, Ks, P)
            q1 = Fp.q[0]; one = [np.ones_like(x) for x in Fp.q]
            sigf = [(1.0, [2 * np.sin(q1), one[1], one[2], one[3]])]
            Wf = [(1.0, [2 * np.cos(q1), one[1], one[2], one[3]])]
            R1 = (float(l) ** -4 * (Fp.fsum(Wf, "10") - Fp.fsum(times(sigf, sigf), "11"))).mean()
            R2 = (w / gam - b ** 2 / (gam * gamp)).mean() / l ** 2
            rel = abs(LHS - R1 - R2) / (abs(LHS) + abs(R1) + abs(R2))
            say(f"    n = {n}, P = 2pi*{j}/{N}: LHS = {LHS:.15e}, R1 = {R1:.15e}, R2 = {R2:.15e} ({time.time() - t0:.1f} s)")
            verdict(f"A1 finite-torus identity n = {n}, j = {j}", rel <= 1e-10, f"rel = {rel:.2e} (threshold 1e-10)")
    # A2: Ward identities at P = 0
    Kpts = [(0.7, 0.4, 0.3, 0.2), (1.9, -0.8, 0.5, 1.1), (-2.6, 1.3, -0.4, 0.9), (0.35, 2.2, 1.7, -1.2)]
    for n in ((1, 2) if SMOKE else (1, 2, 3)):
        eb, ew, chg = 0.0, 0.0, 0.0
        for K in Kpts:
            res = {}
            for h in (2e-3, 1e-3):
                K1 = K[0] + h * np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
                Ks = [K1, np.array([K[1]]), np.array([K[2]]), np.array([K[3]])]
                gam, gamp, b, w, _ = level_data(n, Ks, 0.0)
                g = gam[:, 0, 0, 0]
                d1 = (-g[4] + 8 * g[3] - 8 * g[1] + g[0]) / (12 * h)
                d2 = (-g[4] + 16 * g[3] - 30 * g[2] + 16 * g[1] - g[0]) / (12 * h * h)
                res[h] = (d1, d2, b[2, 0, 0, 0], w[2, 0, 0, 0])
            d1, d2, bb, ww = res[2e-3]
            eb = max(eb, abs(bb - d1) / max(abs(d1), 1e-3))
            ew = max(ew, abs(ww - d2) / max(abs(d2), 1e-3))
            chg = max(chg, abs(res[1e-3][0] - d1) / max(abs(d1), 1e-3), abs(res[1e-3][1] - d2) / max(abs(d2), 1e-3))
            say(f"    n = {n}, K = {K}: b(K;0) = {bb:.12e}, d1 gamma = {d1:.12e}; w(K;0) = {ww:.12e}, d1^2 gamma = {d2:.12e}")
        say(f"    [reported] n = {n}: step-halving change of the difference quotients (rel) = {chg:.1e}")
        verdict(f"A2 Ward b_n(K;0) = d_1 gamma_n, n = {n}", eb <= 1e-7, f"max rel = {eb:.2e} (threshold 1e-7)")
        verdict(f"A2 Ward w_n(K;0) = d_1^2 gamma_n, n = {n}", ew <= 1e-7, f"max rel = {ew:.2e} (threshold 1e-7)")
    # A3: control
    n, j = 2, 1
    l = L ** n
    Ks = [shifted(N)] * 4
    P = 2 * np.pi * j / N
    LHS = integrand(n, Ks, P / l).mean()
    gam, gamp, b, w, Fp = level_data(n, Ks, P, flip=True)
    q1 = Fp.q[0]; one = [np.ones_like(x) for x in Fp.q]
    sigf = [(1.0, [2 * np.sin(q1), one[1], one[2], one[3]])]
    Wf = [(1.0, [2 * np.cos(q1), one[1], one[2], one[3]])]
    R1 = (float(l) ** -4 * (Fp.fsum(Wf, "10") - Fp.fsum(times(sigf, sigf), "11"))).mean()
    R2 = (w / gam - b ** 2 / (gam * gamp)).mean() / l ** 2
    rel = abs(LHS - R1 - R2) / (abs(LHS) + abs(R1) + abs(R2))
    verdict("A3 control (sign of the d'u~^-/lt' term flipped) fails A1 by >= 1e4", rel >= 1e-6,
            f"rel = {rel:.2e} (must be >= 1e-6)")


# =============================================================== extended direction-2 kernels (a + b <= 4)
def _comb(a, b):
    from math import comb
    return comb(a, b)


def Phi2(al, be, z):
    z = np.asarray(z, float)
    out = np.empty_like(z)
    sm = z < 2.0
    zs = z[sm]
    t = np.full_like(zs, Gam(al) * Gam(be) / Gam(al + be))
    acc = t.copy()
    for k in range(60):
        t = t * (-zs) / (k + 1) * (al + k) / (al + be + k)
        acc = acc + t
    out[sm] = acc
    zb = z[~sm]
    acc = np.zeros_like(zb)
    for jj in range(be):
        s = al + jj
        acc = acc + _comb(be - 1, jj) * (-1.0) ** jj * Gam(s) * gammainc(s, zb) / zb ** s
    out[~sm] = acc
    return out


def gext(kind, T, A, B):
    a, b = int(kind[0]), int(kind[1])
    if b == 0:
        return T ** (a - 1) * np.exp(-T * A) / Gam(a)
    if a == 0:
        return T ** (b - 1) * np.exp(-T * B) / Gam(b)
    mn = np.minimum(A, B)
    z = T * np.abs(A - B)
    AleB = A <= B
    shape = np.broadcast(T, A, B).shape
    zf = np.broadcast_to(z, shape).ravel()
    m = np.broadcast_to(AleB, shape).ravel()
    ph = np.empty_like(zf)
    ph[m] = Phi2(b, a, zf[m])
    ph[~m] = Phi2(a, b, zf[~m])
    return T ** (a + b - 1) * np.exp(-T * mn) * ph.reshape(shape) / (Gam(a) * Gam(b))


class LeanFibre:
    """f12's fibre factorisation with direction-2 kernels computed on demand (a + b <= 4); shift +p in direction 2."""

    def __init__(self, n, Ks, p, h_u=0.3, u_min=-36.0):
        self.n = n; self.l = L ** n; self.p = p
        l = self.l
        m = np.arange(l)
        self.q = [((K[:, None] + 2 * np.pi * m[None, :]) / l) for K in Ks]
        lams = [lam1(q) for q in self.q]
        self.A = lams[1]; self.B = lam1(self.q[1] + p)
        lmin = sum(x.min() for x in lams)
        lmin = min(lmin, lmin - lams[1].min() + self.B.min())
        u_max = np.log(80.0 / max(lmin, 1e-300))
        u = np.arange(u_min, u_max + h_u, h_u)
        self.T = np.exp(u); self.w = h_u * self.T
        T = self.T[None, :, None]
        self.E = [np.exp(-T * lams[mu][:, None, :]) if mu != 1 else None for mu in range(4)]

    def fsum(self, terms, kind):
        T = self.T[None, :, None]
        tab2 = gext(kind, T, self.A[:, None, :], self.B[:, None, :])
        tot = 0.0
        for coef, g in terms:
            Y = []
            for mu in range(4):
                tab = tab2 if mu == 1 else self.E[mu]
                Y.append(np.einsum("km,ktm->kt", g[mu], tab))
            X12 = (Y[0][:, None, :] * Y[1][None, :, :] * self.w).reshape(-1, len(self.T))
            X34 = (Y[2][:, None, :] * Y[3][None, :, :]).reshape(-1, len(self.T))
            R = (X12 @ X34.T).reshape(Y[0].shape[0], Y[1].shape[0], Y[2].shape[0], Y[3].shape[0])
            tot = tot + coef * R
        del tab2
        return tot


# =============================================================== Part B: G2-log and the straight-path map
def part_b():
    say("Part B (Proposition G2-log; straight-path map at U = 1)")
    Ka = (0.7, 0.4, 0.3, 0.2); Kb = (2.1, -1.3, 0.9, 2.8)
    nmax = 5 if SMOKE else 7
    gb = {}
    stepchg = 0.0
    for K in (Ka, Kb):
        Ks = [np.array([x]) for x in K]
        for n in range(1, nmax + 1):
            l = L ** n
            vals = []
            for h_u in (0.3, 0.15):
                F = LeanFibre(n, Ks, 0.0, h_u=h_u)
                one = [np.ones_like(x) for x in F.q]
                g2 = float(l) ** -4 * F.fsum([(1.0, one)], "20")[0, 0, 0, 0]
                lt = sum(float(l) ** 2 * lam1(x / l) for x in K)
                vals.append(g2 - lt ** -2)
                del F
            gb[(K, n)] = vals[0]
            stepchg = max(stepchg, abs(vals[0] - vals[1]) / abs(vals[1]))
        say(f"    K = {K}: gbar_n = " + ", ".join(f"{gb[(K, n)]:.10e}" for n in range(1, nmax + 1)))
        for n in range(2, nmax + 1):
            d = gb[(K, n)] - gb[(K, n - 1)]
            say(f"      n = {n}: gbar_n - gbar_(n-1) = {d:.8e}, / (log L / 8 pi^2) = {d / SLOPE:.6f}")
            if n >= 4:
                verdict(f"B1 log slope n = {n}, K = {K}", abs(d / SLOPE - 1) <= 0.05,
                        f"ratio to log L/(8 pi^2) = {d / SLOPE:.5f} (threshold |. - 1| <= 0.05)")
    verdict("B1 step control h_u 0.3 vs 0.15", stepchg <= 1e-9, f"max rel change of gbar_n = {stepchg:.1e} (threshold 1e-9)")
    # B2, B3: straight-path map
    worst = np.inf
    x11 = {}
    for K in (Ka, Kb):
        Ks = [np.array([x]) for x in K]
        Dl2 = np.array([4 * np.sin(x / 2) ** 2 for x in K])
        for n in range(1, (5 if SMOKE else 7)):
            l = L ** n
            F = LeanFibre(n, Ks, 0.0)
            one = [np.ones_like(x) for x in F.q]
            xmm = []
            for mu in range(4):
                g = list(one)
                g[mu] = np.sin(l * F.q[mu] / 2) ** 2 / np.sin(F.q[mu] / 2) ** 2      # |S_mu(k)|^2
                xmm.append(float(l) ** -4 * F.fsum([(1.0, g)], "10")[0, 0, 0, 0])
            g2 = float(l) ** -4 * F.fsum([(1.0, one)], "20")[0, 0, 0, 0]
            lhs = float(np.dot(Dl2, xmm))
            rhs = Dl2.sum() ** 2 * g2
            if n <= 4:
                worst = min(worst, (lhs - rhs) / lhs)
            x11[(K, n)] = xmm[0]
            say(f"    K = {K}, n = {n}: <D, x D> = {lhs:.10e}, |D|^4 g2 = {rhs:.10e}, x_11 = {xmm[0]:.8e}")
            del F
    verdict("B2 U2 inequality (straight-path map, n <= 4)", worst >= -1e-10, f"min (lhs - rhs)/lhs = {worst:.3e} (>= -1e-10)")
    for n in range(2, (5 if SMOKE else 7)):
        rho = x11[(Ka, n)] / x11[(Ka, n - 1)]
        rhob = x11[(Kb, n)] / x11[(Kb, n - 1)]
        say(f"    rho_{n} = x_11(n)/x_11(n-1) at K_a = {rho:.6f}; at K_b = {rhob:.6f}")
        if n >= 3:
            verdict(f"B3 SP-div growth ratio n = {n} (K_a)", abs(rho / L - 1) <= 0.10, f"rho/L = {rho / L:.4f} (threshold |. - 1| <= 0.10)")
    return gb


# =============================================================== Part C: scalar model of the mechanism
def g2_data(n, Ks, p, h_u=0.3):
    """fine-unit g2, g2(K+P), b2_fine, g2s_fine on the K grid."""
    l = L ** n
    Fp = LeanFibre(n, Ks, p, h_u=h_u)
    Fm = LeanFibre(n, Ks, -p, h_u=h_u)
    q1 = Fp.q[0]
    one = [np.ones_like(x) for x in Fp.q]
    s1 = [np.sin(q1) * 2, one[1], one[2], one[3]]
    s2 = [4 * np.sin(q1) ** 2, one[1], one[2], one[3]]
    wv = [2 * np.cos(q1), one[1], one[2], one[3]]
    l4 = float(l) ** -4
    g2 = l4 * Fp.fsum([(1.0, one)], "20")
    g2p = l4 * Fp.fsum([(1.0, one)], "02")
    b2 = -l4 * (Fp.fsum([(1.0, s1)], "21") + Fp.fsum([(1.0, s1)], "12"))
    g2s = l4 * (0.25 * (2 * Fp.fsum([(1.0, s2)], "31") + Fp.fsum([(1.0, s2)], "22")
                        + 2 * Fm.fsum([(1.0, s2)], "31") + Fm.fsum([(1.0, s2)], "22"))
                - 0.5 * Fp.fsum([(1.0, wv)], "30"))
    # X0 data: extended kernels against f12's on these arguments
    T = Fp.T[None, :, None]; A = Fp.A[:, None, :]; B = Fp.B[:, None, :]
    x0 = 0.0
    for k in ("11", "21", "12"):
        e = gext(k, T, A, B); f = gkind(k, T, A, B)
        x0 = max(x0, float(np.max(np.abs(e - f) / np.maximum(np.abs(f), 1e-300))))
    del Fp, Fm
    return g2, g2p, b2, g2s, x0


def brute_g2(p, theta, eps, dims=(12, 24, 3, 3)):
    """[log det iota^* Delta_U^{-2} iota] on the antiperiodic torus (fine units), U_{x,1} = exp(i eps cos(p x_2 + theta))."""
    N1, N2, N3, N4 = dims
    Nt = N1 * N2 * N3 * N4
    idx = np.arange(Nt).reshape(dims)
    rows, cols, vals = [], [], []
    coords = np.indices(dims).reshape(4, -1).T
    for mu in range(4):
        for x in coords:
            y = x.copy(); y[mu] += 1
            sgn = 1.0
            if y[mu] == dims[mu]:
                y[mu] = 0; sgn = -1.0
            a = eps * np.cos(p * x[1] + theta) if mu == 0 else 0.0
            U = np.exp(1j * a) * sgn
            i, j = idx[tuple(x)], idx[tuple(y)]
            rows += [i, j]; cols += [j, i]; vals += [-U, -np.conj(U)]
    rows += list(range(Nt)); cols += list(range(Nt)); vals += [8.0] * Nt
    Dl = sp.csc_matrix((vals, (rows, cols)), shape=(Nt, Nt), dtype=complex)
    lev = [idx[x1, x2, 0, 0] for x1 in range(0, N1, 3) for x2 in range(0, N2, 3)]
    Iota = np.zeros((Nt, len(lev)), complex)
    for c, s in enumerate(lev):
        Iota[s, c] = 1.0
    Y = spla.splu(Dl).solve(Iota)
    G = Y.conj().T @ Y
    sgn, ld = np.linalg.slogdet(G)
    return ld.real, len(lev)


def part_c():
    say("Part C (scalar model P_n: brute force at n = 1; level polarisation y_n(P))")
    # C1
    theta = 0.3
    for j in (1, 2):
        p = 2 * np.pi * j / 24
        f = {}
        for e in (0.0, 0.02, -0.02, 0.01, -0.01):
            f[e], nlev = brute_g2(p, theta, e)
        c1 = (f[0.02] + f[-0.02] - 2 * f[0.0]) / (2 * 0.02 ** 2)
        c2 = (f[0.01] + f[-0.01] - 2 * f[0.0]) / (2 * 0.01 ** 2)
        brute = (4 * c2 - c1) / 3 / nlev
        Ks = [shifted(4), shifted(8), shifted(1), shifted(1)]
        g2, g2p, b2, g2s, _ = g2_data(1, Ks, p)
        form = (g2s / g2 - 0.25 * b2 ** 2 / (g2 * g2p)).mean()
        rel = abs(brute - form) / abs(form)
        say(f"    P = pi*{j}/4: brute [eps^2] per level site = {brute:.12e} (eps 0.02: {c1 / nlev:.12e}), formula = {form:.12e}")
        verdict(f"C1 brute-force test of the y_n formula, n = 1, P = pi*{j}/4", rel <= 1e-6, f"rel = {rel:.2e} (threshold 1e-6)")
    # C2
    nmax = 4 if SMOKE else 6
    Ns = (8,) if SMOKE else (16, 24)
    y = {}
    x0max = 0.0
    for N in Ns:
        Ks = [shifted(N)] * 4
        for n in range(1, nmax + 1):
            l = L ** n
            for jj in (N // 8, N // 4):
                P = 2 * np.pi * jj / N
                t0 = time.time()
                g2, g2p, b2, g2s, x0 = g2_data(n, Ks, P / l)
                x0max = max(x0max, x0)
                y[(N, n, round(P, 12))] = (2 / P ** 2) * (g2s / (l ** 2 * g2) - 0.25 * b2 ** 2 / (l ** 2 * g2 * g2p)).mean()
                say(f"    N = {N}, n = {n}, P = {P:.6f}: y_n = {y[(N, n, round(P, 12))]:.12e}, "
                    f"y_n + 4 c_g log(1/P) = {y[(N, n, round(P, 12))] + 4 * CG * np.log(1 / P):.12e} ({time.time() - t0:.1f} s)")
    verdict("X0 extended kernels reproduce f12's g_11, g_21, g_12", x0max <= 1e-12, f"max rel = {x0max:.1e} (threshold 1e-12)")
    Nr = Ns[0]
    D = {}
    for P in (np.pi / 4, np.pi / 2):
        for N in Ns:
            for n in range(2, nmax + 1):
                D[(N, n, round(P, 12))] = y[(N, n, round(P, 12))] - y[(N, n - 1, round(P, 12))]
        say(f"    P = {P:.6f}, N = {Nr}: D_n = " + ", ".join(f"{D[(Nr, n, round(P, 12))]:.6e}" for n in range(2, nmax + 1)))
        say(f"    P = {P:.6f}, N = {Nr}: r_n = " + ", ".join(
            f"{abs(D[(Nr, n, round(P, 12))] / D[(Nr, n - 1, round(P, 12))]):.4f}" for n in range(3, nmax + 1)))
    if not SMOKE:
        for P in (np.pi / 4, np.pi / 2):
            for n in (5, 6):
                a, b = D[(16, n, round(P, 12))], D[(24, n, round(P, 12))]
                verdict(f"C2 step control N = 16 vs 24, n = {n}, P = {P:.4f}", abs(a - b) <= 0.1 * abs(b),
                        f"D_n(16) = {a:.6e}, D_n(24) = {b:.6e}, rel = {abs(a - b) / abs(b):.2e} (threshold 0.1)")
        r6 = [abs(D[(16, 6, round(P, 12))] / D[(16, 5, round(P, 12))]) for P in (np.pi / 4, np.pi / 2)]
        r5 = [abs(D[(16, 5, round(P, 12))] / D[(16, 4, round(P, 12))]) for P in (np.pi / 4, np.pi / 2)]
        geo = all(r <= 0.2 for r in r5 + r6)
        verdict("C2 classification 'slow' (r_6 >= 0.5 at both P)", all(r >= 0.5 for r in r6),
                f"r_6 = {r6[0]:.4f}, {r6[1]:.4f}; r_5 = {r5[0]:.4f}, {r5[1]:.4f}; geometric (r_5, r_6 <= 0.2 at both P): {geo}")


if __name__ == "__main__":
    say(f"f14 (lane C, session 11) start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC; SMOKE = {SMOKE}")
    say(f"    f12 functions from checks/f12_proxy_2pt.py, md5 {MD5} (executed unchanged)")
    part_a()
    say(f"    (t = {time.time() - T0:.0f} s)")
    part_b()
    say(f"    (t = {time.time() - T0:.0f} s)")
    part_c()
    npass = sum(1 for _, ok in VERD if ok)
    say(f"Summary: {npass}/{len(VERD)} verdict lines PASS; total {time.time() - T0:.0f} s")
