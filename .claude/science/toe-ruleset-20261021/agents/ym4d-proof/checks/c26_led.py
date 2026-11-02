"""c26: (LED) via the dual reduction and the coarse symbol (criteria: checks/c26_criteria.md, written first).

Part A: exact identities against the real-space LSMR minimiser of c23's chain (S4' root-based Q, L = 3, weights kappa_i).
Part B: d = 4 l1 norms of the response kernels dB_k -> r_{k-1} and dB_k -> f_0 versus k (informational).
Usage: python3 -I c26_led.py A | B
"""
import itertools
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsmr

T0 = time.time()
L = 3
TAU = np.arange(-32.0, 0.0, 0.2)          # t = e^tau; upper end shifted per run


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


# ------------------------------------------------------------------ chain (copied from c23, with weights)
class Level:
    def __init__(self, d, n):
        self.d, self.n = d, n
        self.N = n ** d
        self.NL = d * self.N
        self.planes = list(itertools.combinations(range(d), 2))

    def site(self, X):
        X = np.mod(X, self.n)
        s = np.zeros(X.shape[:-1], dtype=np.int64)
        for i in range(self.d):
            s = s * self.n + X[..., i]
        return s

    def coords(self):
        return np.indices((self.n,) * self.d).reshape(self.d, -1).T

    def link(self, X, mu):
        return mu * self.N + self.site(X)

    def dmat(self):
        X = self.coords(); rows, cols, vals = [], [], []
        for p, (mu, nu) in enumerate(self.planes):
            r = p * self.N + np.arange(self.N)
            em = np.zeros(self.d, dtype=np.int64); em[mu] = 1
            en = np.zeros(self.d, dtype=np.int64); en[nu] = 1
            for (c, v) in ((self.link(X, mu), 1.0), (self.link(X + em, nu), 1.0),
                           (self.link(X + en, mu), -1.0), (self.link(X, nu), -1.0)):
                rows.append(r); cols.append(c); vals.append(np.full(self.N, v))
        return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                             shape=(len(self.planes) * self.N, self.NL))


def axial(a, b, order):
    out = []; z = list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


def template(d, mu):
    h = (L - 1) // 2
    orders = list(itertools.permutations(range(d)))
    tw = {}
    w = 1.0 / (len(orders) * L ** d)
    cY = [0] * d; cY[mu] = L
    for sig in orders:
        for off in itertools.product(range(-h, h + 1), repeat=d):
            y = list(off); yL = list(y); yL[mu] += L
            seq = axial([0] * d, y, sig)
            for j in range(L):
                z = list(y); z[mu] += j; seq.append((tuple(z), mu, 1))
            seq += [(z, c, -s) for (z, c, s) in reversed(axial(cY, yL, sig))]
            for (z, c, s) in seq:
                tw[(z, c)] = tw.get((z, c), 0.0) + s * w
    return {k: v for k, v in tw.items() if abs(v) > 1e-15}


def qmat(fine, coarse, tmpls):
    d = fine.d; h = (L - 1) // 2
    Xc = coarse.coords(); rows, cols, vals = [], [], []
    for mu in range(d):
        r = coarse.link(Xc, mu)
        root = L * Xc + h
        for (z, nu), wv in tmpls[mu].items():
            rows.append(r); cols.append(fine.link(root + np.array(z), nu)); vals.append(np.full(coarse.N, wv))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(coarse.NL, fine.NL))


class Chain:
    def __init__(self, d, T, k, kap):
        self.d, self.T, self.k, self.kap = d, T, k, kap
        self.levels = [Level(d, T * L ** (k - i)) for i in range(k + 1)]
        tm = [template(d, mu) for mu in range(d)]
        self.Q = [qmat(self.levels[i], self.levels[i + 1], tm) for i in range(k)]
        self.D0 = self.levels[0].dmat()
        nv = [lv.NL for lv in self.levels[:k]]
        self.off = np.concatenate([[0], np.cumsum(nv)])
        blocks = [[None] * k for _ in range(k + 1)]
        blocks[0][0] = self.D0
        for i in range(k):
            s = np.sqrt(kap[i])
            blocks[i + 1][i] = s * self.Q[i]
            if i + 1 < k:
                blocks[i + 1][i + 1] = -s * sp.identity(self.levels[i + 1].NL, format="csr")
        self.M = sp.bmat(blocks, format="csr")

    def solve(self, Bk):
        b = np.zeros(self.M.shape[0]); b[-self.levels[self.k].NL:] = np.sqrt(self.kap[-1]) * Bk
        x = lsmr(self.M, b, atol=1e-15, btol=1e-15, maxiter=400000)[0]
        ne = np.linalg.norm(self.M.T @ (self.M @ x - b)) / max(np.linalg.norm(self.M.T @ b), 1e-300)
        Bs = [x[self.off[i]:self.off[i + 1]] for i in range(self.k)]
        f = self.D0 @ Bs[0]
        r = [self.Q[i] @ Bs[i] - (Bs[i + 1] if i + 1 < self.k else Bk) for i in range(self.k)]
        E = 0.5 * float(f @ f) + 0.5 * sum(self.kap[i] * float(r[i] @ r[i]) for i in range(self.k))
        return dict(E=E, f=f, r=r, ne=ne)


# ------------------------------------------------------------------ symbols
def Dn(theta, n):
    """n^-1 sum_{j<n} exp(-i theta j / n) (coarse-unit argument theta)."""
    theta = np.asarray(theta, dtype=float)
    den = n * (1.0 - np.exp(-1j * theta / n))
    num = 1.0 - np.exp(-1j * theta)
    out = np.ones_like(den)
    m = np.abs(den) > 1e-13
    out[m] = num[m] / den[m]
    return out


def outer(fs):
    out = fs[0]
    for f in fs[1:]:
        out = np.multiply.outer(out, f)
    return out


def pgrid(T):
    return 2 * np.pi * np.arange(T) / T


def tau_grid(T):
    phimin = 4 * np.sin(np.pi / T) ** 2 * 0.999
    return np.arange(-32.0, np.log(40.0 / phimin) + 0.2, 0.2)


def S_symbol(d, T, n, mu):
    """coarse symbol of Q^(n) Q^(n)T on component mu (direct straight average, side n)."""
    p = pgrid(T); th = p[:, None] + 2 * np.pi * np.arange(n)[None, :]
    a = np.abs(Dn(th, n)) ** 2
    fac = [a.sum(1) if al != mu else (a * a).sum(1) for al in range(d)]
    return n ** (2.0 - d) * outer(fac).real


def G_laplace(d, T, n, mu):
    p = pgrid(T); th = p[:, None] + 2 * np.pi * np.arange(n)[None, :]
    a = np.abs(Dn(th, n)) ** 2; ph = 4 * n * n * np.sin(th / (2 * n)) ** 2
    out = np.zeros((T,) * d)
    tg = tau_grid(T); h = tg[1] - tg[0]
    for tau in tg:
        t = np.exp(tau); e = np.exp(-t * ph)
        fac = [(a * e).sum(1) if al != mu else (a * a * e).sum(1) for al in range(d)]
        out += h * t * outer(fac).real
    out *= n ** (4.0 - d)
    out[(0,) * d] = np.inf
    return out


def G_direct(d, T, n, mu):
    p = pgrid(T); out = np.zeros((T,) * d)
    grids = np.meshgrid(*([p] * d), indexing="ij")
    for K in itertools.product(range(n), repeat=d):
        th = [grids[a] + 2 * np.pi * K[a] for a in range(d)]
        W2 = np.ones_like(grids[0])
        ph = np.zeros_like(grids[0])
        for a in range(d):
            W2 = W2 * np.abs(Dn(th[a], n)) ** 2
            ph = ph + 4 * n * n * np.sin(th[a] / (2 * n)) ** 2
        W2 = W2 * np.abs(Dn(th[mu], n)) ** 2
        with np.errstate(divide="ignore", invalid="ignore"):
            out += np.where(ph > 0, W2 / ph, 0.0)
    out *= n ** (4.0 - d)
    out[(0,) * d] = np.inf
    return out


def P_symbol(d, T, k, kap, direct=False):
    P = []
    for mu in range(d):
        s = np.zeros((T,) * d)
        for m in range(k):
            s += (kap[k - 1] / kap[k - 1 - m]) * S_symbol(d, T, L ** m, mu)
        g = (G_direct if direct else G_laplace)(d, T, L ** k, mu)
        P.append(s + kap[k - 1] * g)
    return P


def nu_sym(d, T):
    p = pgrid(T); g = np.meshgrid(*([p] * d), indexing="ij")
    return [np.exp(1j * g[a]) - 1.0 for a in range(d)]


def r_from_b(P, bhat, nu):
    Pi = [1.0 / x for x in P]
    num = sum(np.conj(nu[m]) * Pi[m] * bhat[m] for m in range(len(P)))
    den = sum(np.abs(nu[m]) ** 2 * Pi[m] for m in range(len(P)))
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(den > 0, num / den, 0.0)
    return [-Pi[m] * (bhat[m] - nu[m] * t) for m in range(len(P))]


def R_symbol(P, nu, planes):
    """R[mu][plane]: r_hat_mu = sum_planes R * F_hat_plane, F_plane = (dB)_{a b}, a < b."""
    d = len(P); Pi = [1.0 / x for x in P]
    den = sum(np.abs(nu[m]) ** 2 * Pi[m] for m in range(d))
    R = [[None] * len(planes) for _ in range(d)]
    for mu in range(d):
        for j, (a, b) in enumerate(planes):
            # F_{nu mu} with nu = a, mu = b gives +F_plane; nu = b, mu = a gives -F_plane
            if mu == b:
                c = Pi[a] * np.conj(nu[a])
            elif mu == a:
                c = -Pi[b] * np.conj(nu[b])
            else:
                c = 0.0 * den
            with np.errstate(divide="ignore", invalid="ignore"):
                R[mu][j] = np.where(den > 0, -Pi[mu] * c / den, 0.0)
    return R


def Phi_f(d, T, n, rho, sig, u, direct=False):
    """alias sum Phi_{rho sig u}(p) = int dt sum_K prod_alpha factor (Laplace) for the f_0 Bloch formula."""
    p = pgrid(T); th = p[:, None] + 2 * np.pi * np.arange(n)[None, :]
    D = Dn(th, n); ph = 4 * n * n * np.sin(th / (2 * n)) ** 2
    base = []
    for al in range(d):
        f = np.exp(1j * th * u[al] / n) * D
        if al == sig:
            f = f * D
        if al == rho:
            f = f * (np.exp(1j * th / n) - 1.0)
        base.append(f)
    if direct:
        out = np.zeros((T,) * d, dtype=complex)
        grids = np.meshgrid(*([np.arange(T)] * d), indexing="ij")
        for K in itertools.product(range(n), repeat=d):
            num = np.ones((T,) * d, dtype=complex); den = np.zeros((T,) * d)
            for al in range(d):
                num = num * base[al][grids[al], K[al]]
                den = den + ph[grids[al], K[al]]
            with np.errstate(divide="ignore", invalid="ignore"):
                out += np.where(den > 0, num / den, 0.0)
    else:
        out = np.zeros((T,) * d, dtype=complex)
        tg = tau_grid(T); h = tg[1] - tg[0]
        for tau in tg:
            t = np.exp(tau); e = np.exp(-t * ph)
            out += h * t * outer([(base[al] * e).sum(1) for al in range(d)])
    out[(0,) * d] = 0.0
    return out


def f_bloch(d, T, k, kap, rhat, u, direct=False):
    """coarse-unit fine curvature at fine sites nX + u, all planes, from r_hat (Bloch formula)."""
    n = L ** k; pl = list(itertools.combinations(range(d), 2)); out = []
    for (a, b) in pl:
        fa = Phi_f(d, T, n, a, b, u, direct) * rhat[b] - Phi_f(d, T, n, b, a, u, direct) * rhat[a]
        out.append(np.fft.ifftn(n ** (5.0 - d) * (-kap[k - 1]) * fa).real)
    return out


# ------------------------------------------------------------------ Part A
def part_A():
    rng = np.random.default_rng(20261027)
    ok = dict(V1=True, V2=True, Q1=True, Q2=True, Q3=True, Q4=True)
    cases = [(2, 5, 1, (1.0,)), (2, 5, 2, (1.0, 1.0)), (2, 5, 3, (1.0, 1.0, 1.0)),
             (2, 5, 2, (0.5, 2.0)), (2, 5, 3, (0.5, 2.0, 1.0)),
             (3, 3, 1, (1.0,)), (4, 3, 1, (1.0,)), (4, 3, 1, (2.5,)), (4, 2, 2, (1.0, 1.0))]
    for (d, T, k, kap) in cases:
        tt = time.time()
        ch = Chain(d, T, k, kap); top = ch.levels[k]; n = L ** k
        Bk = rng.normal(size=top.NL)
        sol = ch.solve(Bk)
        r = sol["r"][k - 1].reshape(d, *(T,) * d)
        bhat = [np.fft.fftn(Bk.reshape(d, *(T,) * d)[m]) for m in range(d)]
        nu = nu_sym(d, T)
        P = P_symbol(d, T, k, kap)
        v2 = None
        if n ** d <= 6561:
            Pd = P_symbol(d, T, k, kap, direct=True)
            fin = np.isfinite(P[0])
            v2 = max(float(np.max(np.abs(P[m][fin] - Pd[m][fin]) / np.abs(Pd[m][fin]))) for m in range(d))
            ok["V2"] &= v2 <= 1e-9
        rh = r_from_b(P, bhat, nu)
        rs = np.array([np.fft.ifftn(x).real for x in rh])
        # same r from F through the R-symbol
        F = (top.dmat() @ Bk).reshape(len(top.planes), *(T,) * d)
        Fh = [np.fft.fftn(F[j]) for j in range(len(top.planes))]
        R = R_symbol(P, nu, top.planes)
        rF = np.array([np.fft.ifftn(sum(R[m][j] * Fh[j] for j in range(len(top.planes)))).real for m in range(d)])
        q1 = max(np.max(np.abs(r - rs)), np.max(np.abs(r - rF))) / np.max(np.abs(r))
        Pfin = [np.where(np.isfinite(x), x, 0.0) for x in P]
        Es = 0.5 * kap[k - 1] * sum(float(np.sum(Pfin[m] * np.abs(rh[m]) ** 2)) for m in range(d)) / T ** d
        q2 = abs(sol["E"] - Es) / sol["E"]
        div = sum(r[m] - np.roll(r[m], 1, axis=m) for m in range(d))
        q3 = max(np.max(np.abs(div)), abs(r.mean()) * d) / np.max(np.abs(r))
        ok["V1"] &= sol["ne"] <= 1e-8; ok["Q1"] &= q1 <= 1e-6; ok["Q2"] &= q2 <= 1e-6; ok["Q3"] &= q3 <= 1e-6
        msg = (f"d={d} T={T} k={k} kap={kap}: ne={sol['ne']:.1e} Q1 {q1:.2e} Q2 {q2:.2e} Q3 {q3:.2e}"
               + (f" V2 {v2:.1e}" if v2 is not None else ""))
        if (d, T, k) in ((4, 3, 1), (2, 5, 2)) and kap[0] == 1.0:
            lv0 = ch.levels[0]
            fL = (n ** 2 * sol["f"]).reshape(len(lv0.planes), *(T * n,) * d)
            worst = 0.0; worst_d = 0.0
            for u in itertools.product(range(n), repeat=d):
                sl = tuple(slice(u[a], None, n) for a in range(d))
                fb = f_bloch(d, T, k, kap, rh, u)
                for j in range(len(lv0.planes)):
                    worst = max(worst, float(np.max(np.abs(fL[j][sl] - fb[j]))))
                if u == (0,) * d or u == ((n - 1) // 2,) * d:
                    fd = f_bloch(d, T, k, kap, rh, u, direct=True)
                    worst_d = max(worst_d, max(float(np.max(np.abs(fd[j] - fb[j]) / np.max(np.abs(fd[j]))))
                                               for j in range(len(lv0.planes))))
            q4 = worst / np.max(np.abs(fL))
            ok["Q4"] &= q4 <= 1e-6; ok["V2"] &= worst_d <= 1e-9
            msg += f" Q4 {q4:.2e} (Laplace vs direct f {worst_d:.1e})"
        print(msg + f" ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"c26 A: {'VALID' if ok['V1'] and ok['V2'] else 'INVALID'}; time {time.time() - T0:.0f} s, "
          f"peak RSS {rss():.0f} MB")


# ------------------------------------------------------------------ Part B
def norms(d, T, k, kap, offsets):
    n = L ** k; planes = list(itertools.combinations(range(d), 2))
    P = P_symbol(d, T, k, kap); nu = nu_sym(d, T)
    R = R_symbol(P, nu, planes)
    Kr = [[np.fft.ifftn(R[m][j]).real for j in range(len(planes))] for m in range(d)]
    Nr = max(sum(float(np.abs(Kr[m][j]).sum()) for j in range(len(planes))) for m in range(d))
    ax = np.array([max(abs(Kr[m][j][(x,) + (0,) * (d - 1)]) for m in range(d) for j in range(len(planes)))
                   for x in range(T // 2 + 1)])
    Nf = 0.0
    for u in offsets:
        for (a, b) in planes:
            Pab = Phi_f(d, T, n, a, b, u); Pba = Phi_f(d, T, n, b, a, u)
            tot = 0.0
            for j in range(len(planes)):
                sym = n ** (5.0 - d) * (-kap[k - 1]) * (Pab * R[b][j] - Pba * R[a][j])
                tot += float(np.abs(np.fft.ifftn(sym).real).sum())
            Nf = max(Nf, tot)
    return Nr, Nf, ax


def part_B():
    d = 4; rng = np.random.default_rng(7)
    res = {}
    runs = [(16, 1.0, range(1, 7))] + [(16, kp, range(1, 6)) for kp in (0.25, 4.0)] + \
           [(T, 1.0, range(1, 6)) for T in (12, 20)]
    for (T, kp, ks) in runs:
        for k in ks:
            tt = time.time(); n = L ** k
            offs = [(0,) * d, ((n - 1) // 2,) * d] + [tuple(int(x) for x in rng.integers(0, n, size=d)) for _ in range(3)]
            Nr, Nf, ax = norms(d, T, k, (kp,) * k, offs)
            res[(T, kp, k)] = (Nr, Nf)
            sl = np.log(ax[7] / ax[3]) / np.log(7 / 3) if T >= 16 else float("nan")
            print(f"T={T} kappa={kp} k={k} (n={n}): N_r={Nr:.5f} N_f={Nf:.5f} axis slope(3..7)={sl:.2f} "
                  f"({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    Q5 = res[(16, 1.0, 6)][0] <= 1.25 * max(res[(16, 1.0, k)][0] for k in (1, 2, 3))
    Q6 = res[(16, 1.0, 6)][1] <= 1.25 * max(res[(16, 1.0, k)][1] for k in (1, 2, 3))
    print(f"Q5: {'PASS' if Q5 else 'FAIL'}"); print(f"Q6: {'PASS' if Q6 else 'FAIL'}")
    print(f"c26 B: time {time.time() - T0:.0f} s, peak RSS {rss():.0f} MB")


# ------------------------------------------------------------------ Part C (appended after the A and B runs; see criteria addendum)
def pi_coex(d, T, planes):
    nu = nu_sym(d, T); psi = sum(np.abs(x) ** 2 for x in nu)
    idx = {pl: j for j, pl in enumerate(planes)}
    C = []
    for (a, b, c) in itertools.combinations(range(d), 3):
        row = [0.0 * psi for _ in planes]
        row[idx[(b, c)]] = row[idx[(b, c)]] + nu[a]
        row[idx[(a, c)]] = row[idx[(a, c)]] - nu[b]
        row[idx[(a, b)]] = row[idx[(a, b)]] + nu[c]
        C.append(row)
    Pi = [[None] * len(planes) for _ in planes]
    for j in range(len(planes)):
        for jj in range(len(planes)):
            num = sum(np.conj(C[t][j]) * C[t][jj] for t in range(len(C)))
            with np.errstate(divide="ignore", invalid="ignore"):
                Pi[j][jj] = np.where(psi > 0, num / psi, 0.0)
    return Pi


def rep_symbols(d, T, k, kap, u, R, Pc, planes):
    n = L ** k; out = []
    for ja, (a, b) in enumerate(planes):
        Pab = Phi_f(d, T, n, a, b, u); Pba = Phi_f(d, T, n, b, a, u)
        out.append([n ** (5.0 - d) * (-kap[k - 1]) * (Pab * R[b][j] - Pba * R[a][j]) + Pc[ja][j]
                    for j in range(len(planes))])
    return out


def part_C():
    d = 4; planes = list(itertools.combinations(range(d), 2)); ok = dict(V3=True, Q7=True)
    rng = np.random.default_rng(20261027)
    for (T, k) in ((3, 1), (2, 2)):
        tt = time.time(); kap = (1.0,) * k; n = L ** k
        ch = Chain(d, T, k, kap); top = ch.levels[k]
        Bk = rng.normal(size=top.NL); sol = ch.solve(Bk)
        lv0 = ch.levels[0]; fL = (n ** 2 * sol["f"]).reshape(len(planes), *(T * n,) * d)
        F = (top.dmat() @ Bk).reshape(len(planes), *(T,) * d); Fh = [np.fft.fftn(x) for x in F]
        P = P_symbol(d, T, k, kap); R = R_symbol(P, nu_sym(d, T), planes); Pc = pi_coex(d, T, planes)
        offs = [(0,) * d, ((n - 1) // 2,) * d, (1, 0, 2, 1), (n - 1, 1, 0, n - 2)]
        worst = 0.0
        for u in offs:
            S = rep_symbols(d, T, k, kap, u, R, Pc, planes)
            sl = tuple(slice(u[a], None, n) for a in range(d))
            for ja in range(len(planes)):
                fr = np.fft.ifftn(sum(S[ja][j] * Fh[j] for j in range(len(planes)))).real
                worst = max(worst, float(np.max(np.abs(fr - fL[ja][sl]))))
        v3 = worst / np.max(np.abs(fL)); ok["V3"] &= v3 <= 1e-10
        print(f"V3 d=4 T={T} k={k}: max rel error of the representative on closed F = {v3:.2e} "
              f"({time.time() - tt:.0f} s)", flush=True)
    res = {}
    rng = np.random.default_rng(7)
    for T in (12, 16, 20, 24):
        for k in range(1, 7 if T == 16 else 6):
            tt = time.time(); n = L ** k; kap = (1.0,) * k
            offs = [(0,) * d, ((n - 1) // 2,) * d] + [tuple(int(x) for x in rng.integers(0, n, size=d)) for _ in range(3)]
            P = P_symbol(d, T, k, kap); R = R_symbol(P, nu_sym(d, T), planes); Pc = pi_coex(d, T, planes)
            Nf = 0.0
            for u in offs:
                S = rep_symbols(d, T, k, kap, u, R, Pc, planes)
                for ja in range(len(planes)):
                    Nf = max(Nf, sum(float(np.abs(np.fft.ifftn(S[ja][j]).real).sum()) for j in range(len(planes))))
            res[(T, k)] = Nf
            print(f"T={T} k={k}: N_f^rep = {Nf:.5f} ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    for k in range(1, 6):
        ok["Q7"] &= res[(24, k)] <= 1.1 * res[(12, k)]
    ok["Q7"] &= res[(16, 6)] <= 1.25 * max(res[(16, k)] for k in (1, 2, 3))
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"c26 C: time {time.time() - T0:.0f} s, peak RSS {rss():.0f} MB")


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C}[sys.argv[1]]()
