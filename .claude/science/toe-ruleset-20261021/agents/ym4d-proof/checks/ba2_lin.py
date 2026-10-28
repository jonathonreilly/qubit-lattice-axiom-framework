"""ba2: BFT lane A, session 2 (criteria: checks/ba2_criteria.md, written before this file).

Part V: the exact identities of Lemma BL-1 and Proposition BL-6 (b), and the sizes of Lemma BL-2, on real-space
        chains (d = 4, L = 3), against an independent direct solve (CG on the normal equations with the explicit
        source gradient).
Part M: the data constants of Proposition BL-4 for k = 1..4 from the exact symbols (code of checks/c26_led.py).
Usage: python3 ba2_lin.py V | M
"""
import itertools
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsmr

import c26_led as c26

L = c26.L
T0 = time.time()


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


# ------------------------------------------------------------------ Part V helpers
def gradmat(lv):
    """level gradient d: 0-forms -> 1-forms, (d lam)(X, mu) = lam(X + e_mu) - lam(X)."""
    X = lv.coords(); rows, cols, vals = [], [], []
    for mu in range(lv.d):
        em = np.zeros(lv.d, dtype=np.int64); em[mu] = 1
        r = lv.link(X, mu)
        rows += [r, r]; cols += [lv.site(X + em), lv.site(X)]
        vals += [np.ones(lv.N), -np.ones(lv.N)]
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(lv.NL, lv.N))


class SChain(c26.Chain):
    def __init__(self, d, T, k, kap):
        super().__init__(d, T, k, kap)
        self.D = [lv.dmat() for lv in self.levels]
        self.MT = self.M.T.tocsr()
        self.ntop = self.levels[k].NL

    def split(self, x):
        return [x[self.off[i]:self.off[i + 1]] for i in range(self.k)]

    def b_of(self, Bk):
        b = np.zeros(self.M.shape[0]); b[-self.ntop:] = np.sqrt(self.kap[-1]) * Bk
        return b

    def grad_src(self, s=None, j=None):
        """explicit gradient g of the linear source functional sum_l <s_l, Q_l x_l - x_{l+1}> + <j_l, x_l>."""
        g = np.zeros(self.M.shape[1]); gs = self.split(g)
        k = self.k
        if s is not None:
            for l in range(k):
                if s[l] is None:
                    continue
                gs[l] += self.Q[l].T @ s[l]
                if l + 1 < k:
                    gs[l + 1] -= s[l]
        if j is not None:
            for l in range(k):
                if j[l] is not None:
                    gs[l] += j[l]
        return g

    def cg(self, Bk, g, tol=1e-12, maxit=400000):
        rhs = self.MT @ self.b_of(Bk) + g
        A = lambda v: self.MT @ (self.M @ v)
        x = np.zeros_like(rhs); r = rhs.copy(); p = r.copy(); rr = float(r @ r); nb = np.sqrt(float(rhs @ rhs))
        it = 0
        for it in range(maxit):
            Ap = A(p); al = rr / float(p @ Ap); x += al * p; r -= al * Ap; rn = float(r @ r)
            if np.sqrt(rn) <= tol * nb:
                break
            p = r + (rn / rr) * p; rr = rn
        res = np.linalg.norm(rhs - A(x)) / nb
        return x, res, it + 1

    def ls(self, Bk):
        b = self.b_of(Bk)
        x = lsmr(self.M, b, atol=1e-15, btol=1e-15, maxiter=400000)[0]
        ne = np.linalg.norm(self.MT @ (self.M @ x - b)) / max(np.linalg.norm(self.MT @ b), 1e-300)
        return x, ne

    def outs(self, x, Bk):
        xs = self.split(x); k = self.k
        r = [self.Q[l] @ xs[l] - (xs[l + 1] if l + 1 < k else Bk) for l in range(k)]
        f = [self.D[l] @ xs[l] for l in range(k)]
        return r, f, xs


def rel(a, b):
    return float(np.max(np.abs(a - b)) / max(np.max(np.abs(a)), 1e-300))


def part_V():
    d = 4; ok = dict(V0=True, V1=True, V2=True, V3=True, V4=True)
    rng = np.random.default_rng(20261028)
    for (T, k, kap) in ((3, 1, (1.0,)), (2, 2, (1.0, 1.0)), (2, 2, (0.5, 2.0))):
        tt = time.time()
        ch = SChain(d, T, k, kap); lv = ch.levels
        # ---- V1: residual-type sources at every level + data
        Bk = rng.normal(size=ch.ntop)
        s = [rng.normal(size=lv[l + 1].NL) for l in range(k)]
        sig = [s[l] / kap[l] for l in range(k)]
        tau = [np.zeros(lv[0].NL)]
        for l in range(k):
            tau.append(ch.Q[l] @ tau[l] + sig[l])
        x, res, its = ch.cg(Bk, ch.grad_src(s=s))
        y, ne = ch.ls(Bk + tau[k])
        rx, fx, xs = ch.outs(x, Bk); ry, fy, ys = ch.outs(y, Bk + tau[k])
        v1 = max([rel(rx[l], ry[l] + sig[l]) for l in range(k)] + [rel(fx[0], fy[0])]
                 + ([rel(fx[1], fy[1] - ch.D[1] @ tau[1])] if k >= 2 else []))
        ok["V0"] &= (res <= 1e-10) and (ne <= 1e-8); ok["V1"] &= v1 <= 1e-7
        msg = f"T={T} k={k} kap={kap}: V1 rel {v1:.2e} (CG res {res:.1e}, {its} it; LSMR ne {ne:.1e})"
        if k == 2:
            # ---- V2: plain level-1 current = level-0 current + residual source s_0 = -j_1 (then BL-1 (i))
            D1T = ch.D[1].T.tocsr()
            psi = rng.normal(size=ch.D[1].shape[0])
            cst = np.repeat(rng.normal(size=d), lv[1].N)
            j1 = D1T @ psi + cst
            Bk = rng.normal(size=ch.ntop)
            x, res1, it1 = ch.cg(Bk, ch.grad_src(j=[None, j1]))
            sig0 = -j1 / kap[0]
            tau1 = sig0; tau2 = ch.Q[1] @ tau1
            y, res2, it2 = ch.cg(Bk + tau2, ch.grad_src(j=[ch.Q[0].T @ j1, None]))
            rx, fx, _ = ch.outs(x, Bk); ry, fy, _ = ch.outs(y, Bk + tau2)
            v2 = max(rel(rx[0], ry[0] + sig0), rel(rx[1], ry[1]), rel(fx[0], fy[0]),
                     rel(fx[1], fy[1] - ch.D[1] @ tau1))
            ok["V0"] &= max(res1, res2) <= 1e-10; ok["V2"] &= v2 <= 1e-7
            msg += f"; V2 rel {v2:.2e} (CG res {res1:.1e}/{res2:.1e}, {it1}/{it2} it)"
            # ---- V3: constant coarse current pushed down to level 1 (BL-6 (b))
            c = 0.37
            J = np.zeros(ch.ntop); J[:lv[2].N] = c          # component mu = 0 (e_1)
            j1 = ch.Q[1].T @ J
            x, res3, it3 = ch.cg(np.zeros(ch.ntop), ch.grad_src(j=[None, j1]))
            rx, fx, _ = ch.outs(x, np.zeros(ch.ntop))
            e3 = (float(np.max(np.abs(rx[1] - J / kap[1]))), float(np.max(np.abs(rx[0]))), float(np.max(np.abs(fx[0]))))
            ok["V0"] &= res3 <= 1e-10; ok["V3"] &= max(e3) <= 1e-8
            msg += f"; V3 |r_1 - c/kap_1| {e3[0]:.1e} |r_0| {e3[1]:.1e} |dx_0| {e3[2]:.1e} (CG res {res3:.1e}, {it3} it)"
            if kap == (1.0, 1.0):
                # ---- V4: sizes of BL-2
                Q01 = (ch.Q[1] @ ch.Q[0]).tocsr()
                nrm = {}
                for (a, b, Qm) in ((0, 1, ch.Q[0]), (1, 2, ch.Q[1]), (0, 2, Q01)):
                    nrm[(a, b)] = float(abs(Qm).sum(axis=1).max()) * L ** (-(b - a))
                cerr = 0.0
                for l in range(2):
                    for mu in range(d):
                        v = np.zeros(lv[l].NL); v[mu * lv[l].N:(mu + 1) * lv[l].N] = 1.0
                        w = np.zeros(lv[l + 1].NL); w[mu * lv[l + 1].N:(mu + 1) * lv[l + 1].N] = L
                        cerr = max(cerr, float(np.max(np.abs(ch.Q[l] @ v - w))))
                G0T = gradmat(lv[0]).T.tocsr()
                rat, dv = 0.0, 0.0
                for _ in range(20):
                    jj = D1T @ rng.normal(size=ch.D[1].shape[0]) + np.repeat(rng.normal(size=d), lv[1].N)
                    q = ch.Q[0].T @ jj
                    rat = max(rat, L ** 3 * float(np.max(np.abs(q))) / float(np.max(np.abs(jj))))
                    dv = max(dv, float(np.max(np.abs(G0T @ q))) / float(np.max(np.abs(jj))))
                ok["V4"] &= max(nrm.values()) <= 5.0 and cerr <= 1e-13 and rat <= 1 + 1e-12 and dv <= 1e-12
                msg += (f"\n    V4: coarse row norms Q(0,1) {nrm[(0, 1)]:.4f} Q(1,2) {nrm[(1, 2)]:.4f} Q(0,2) {nrm[(0, 2)]:.4f};"
                        f" |Q const - L const| {cerr:.1e}; max L^3|Q^T j|/|j| {rat:.6f}; |d* Q^T j|/|j| {dv:.1e}")
        print(msg + f" ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"ba2 V: time {time.time() - T0:.0f} s, peak RSS {rss():.0f} MB")


# ------------------------------------------------------------------ Part M
D4 = 4
PLANES = list(itertools.combinations(range(D4), 2))


def rhat_units(T, k, kap):
    P = c26.P_symbol(D4, T, k, kap); nu = c26.nu_sym(D4, T)
    out = []
    for v in range(D4):
        bh = [np.ones((T,) * D4, dtype=complex) if m == v else np.zeros((T,) * D4, dtype=complex) for m in range(D4)]
        out.append(c26.r_from_b(P, bh, nu))
    return out


def N_r(rh):
    return max(sum(float(np.abs(np.fft.ifftn(rh[v][mu]).real).sum()) for v in range(D4)) for mu in range(D4))


def fker(T, k, kap, rh, u, a, b):
    n = L ** k
    Pab = c26.Phi_f(D4, T, n, a, b, u); Pba = c26.Phi_f(D4, T, n, b, a, u)
    pref = n ** (5.0 - D4) * (-kap[k - 1])
    return np.array([np.fft.ifftn(pref * (Pab * rh[v][b] - Pba * rh[v][a])).real for v in range(D4)])


def line_stats(T, k, kap, rh, line, alphas):
    n = L ** k; c = (n - 1) // 2
    us = [(t, 0, 0, 0) if line == "A" else (t, c, c, c) for t in range(n + 1)]
    Nf = 0.0; H = {a: 0.0 for a in alphas}; shift_err = 0.0
    for (a, b) in PLANES:
        Ks = [fker(T, k, kap, rh, u, a, b) for u in us]
        for t in range(n):
            Nf = max(Nf, float(np.abs(Ks[t]).sum()))
        sref = np.roll(Ks[0], -1, axis=1)
        shift_err = max(shift_err, float(np.max(np.abs(Ks[n] - sref)) / np.max(np.abs(sref))))
        for t in range(n + 1):
            for t2 in range(t + 1, n + 1):
                dd = float(np.abs(Ks[t] - Ks[t2]).sum())
                for al in alphas:
                    H[al] = max(H[al], dd / ((t2 - t) / n) ** al)
        del Ks
    return Nf, H, shift_err


def part_M():
    alphas = (0.25, 0.5); res = {}
    rng = np.random.default_rng(7)
    T = 16
    for kp in (1.0, 0.25, 4.0):
        for k in range(1, 5):
            tt = time.time(); kap = (kp,) * k; n = L ** k
            rh = rhat_units(T, k, kap)
            nr = N_r(rh)
            if kp == 1.0:
                NfA, HA, eA = line_stats(T, k, kap, rh, "A", alphas)
                NfB, HB, eB = line_stats(T, k, kap, rh, "B", alphas)
                nf = max(NfA, NfB); H = {al: max(HA[al], HB[al]) for al in alphas}
                res[(kp, k)] = (nr, nf, H)
                print(f"T={T} kappa={kp} k={k} (n={n}): N_r={nr:.5f} N_f={nf:.5f} (lines A {NfA:.5f}, B {NfB:.5f}) "
                      f"H_f(0.25)={H[0.25]:.5f} H_f(0.5)={H[0.5]:.5f} [A {HA[0.25]:.4f}/{HA[0.5]:.4f}, "
                      f"B {HB[0.25]:.4f}/{HB[0.5]:.4f}] t=n shift sanity {max(eA, eB):.1e} "
                      f"({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
            else:
                offs = [(0,) * D4, ((n - 1) // 2,) * D4] + [tuple(int(z) for z in rng.integers(0, n, size=D4))
                                                             for _ in range(3)]
                nf = 0.0
                for u in offs:
                    for (a, b) in PLANES:
                        nf = max(nf, float(np.abs(fker(T, k, kap, rh, u, a, b)).sum()))
                res[(kp, k)] = (nr, nf, None)
                print(f"T={T} kappa={kp} k={k} (n={n}): N_r={nr:.5f} N_f={nf:.5f} (offsets {offs}) "
                      f"({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    ok = {}
    for kp in (1.0, 0.25, 4.0):
        nrs = [res[(kp, k)][0] for k in (2, 3, 4)]; nfs = [res[(kp, k)][1] for k in (2, 3, 4)]
        ok[f"Q1 kappa={kp}"] = max(nrs) <= 1.10 * min(nrs)
        ok[f"Q2 kappa={kp}"] = max(nfs) <= 1.25 * min(nfs)
    for al in alphas:
        h = {k: res[(1.0, k)][2][al] for k in (2, 3, 4)}
        ok[f"Q3 alpha={al}"] = h[4] <= 1.25 * max(h[2], h[3])
    # I1: T = 12, k = 3, line A
    tt = time.time(); k = 3; kap = (1.0,) * k
    rh = rhat_units(12, k, kap)
    NfA, HA, eA = line_stats(12, k, kap, rh, "A", alphas)
    print(f"I1: T=12 k=3 line A: N_f={NfA:.5f} H_f(0.25)={HA[0.25]:.5f} H_f(0.5)={HA[0.5]:.5f} "
          f"(T=16, both lines: N_f={res[(1.0, 3)][1]:.5f} H_f={res[(1.0, 3)][2][0.25]:.5f}/{res[(1.0, 3)][2][0.5]:.5f}) "
          f"({time.time() - tt:.0f} s)", flush=True)
    # I2: analytic lower bounds (kappa = 1)
    print("I2 (analytic, kappa = 1): necessity first term 2^(1-a) L^-th L^((a-th)(k-1)); F3 ratios "
          "single l=1: L^((1-a-th)(k-1)); all levels: (k-1) L^(1-a-th) if th <= 1-a")
    for (al, th) in ((0.5, 0.25), (0.25, 0.5), (0.5, 0.5)):
        row = []
        for k in range(1, 9):
            nec = 2 ** (1 - al) * L ** (-th) * L ** ((al - th) * (k - 1))
            f3a = L ** ((1 - al - th) * (k - 1))
            f3b = (k - 1) * L ** (1 - al - th) if th <= 1 - al else float("nan")
            row.append(f"k={k}: {nec:.3g}/{f3a:.3g}/{f3b:.3g}")
        print(f"  (alpha, theta) = ({al}, {th}): " + "; ".join(row))
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"ba2 M: time {time.time() - T0:.0f} s, peak RSS {rss():.0f} MB")


if __name__ == "__main__":
    {"V": part_V, "M": part_M}[sys.argv[1]]()
