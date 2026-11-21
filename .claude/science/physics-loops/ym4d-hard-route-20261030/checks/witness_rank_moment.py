#!/usr/bin/env python3
"""Rank of the moment map on the kernel of the site densities: the universal statement behind a level-j version of Text 3.13.

Setting: a box in Z^4; A := e_F + d t on it, e_F the linear potential of uniform flux F, t arbitrary. Z := the conserved currents on the box. rho_x(J, A) := (1/2) sum_(l at x) J(l) A(l).
Let PP_h be the polynomial link fields of degree <= 3 with H u = 0 (H = d^T d, in the interior). They carry the source-free part of a second-order response near the box, whose coefficients depend on the far geometry and on the action.
Let P[F', F] be a polynomial of degree <= 3 with H P = J2(e_F', e_F), J2(l) := VV(delta_l, e_F', e_F), the local current of two linear potentials. Its top part is what is universal.
    NN(t) := { J in Z : rho(J, A) = 0, <J, u> = 0 for u in PP_h },    m^(k)(J) := <J, P[e_k, F] - tbar e_k >,  k over the six planes.
On NN(t) the value m does not depend on the choice of P or on the gauge of e_k.

Hand derivation (Text 3.14): m(F) = 0 on NN(t), for every t. In Fock gauge m(*F) = 0 too, since [F, *F] = 0 and J2 = (3/4) [F, F'] x there, so the root directions give rank 4 for generic F.
The potentials e_k of this script are not Fock: a_nu = x_mu. The Fock potential of F is e_F - (1/2) d sum F_k x_mu x_nu.
What the level-j argument needs, with many separated cells (Text 3.14): m is not zero on NN(t), for every t, for F != 0.

On L = 4 the Fock simple case has m = 0 exactly; on L = 5, 6 it has rank 4 with four equal singular values. So L = 4 is a small-box artefact (a function of one coordinate on 4 points is a cubic), and adversaries must run on L >= 5.

An earlier version of this script used compactly supported y with J = H y. On boxes of side 4 and 5 its kernel was empty, because the support of H y is larger than that of y; no result came from it, and it is replaced by this form.

PRE-REGISTERED CRITERIA (written before the first run of this form).
 M0: H P = J2 on the interior of the box, relative 1e-10; and m(F) = 0 on NN(t), relative 1e-9. FAIL means the derivation is wrong.
 M2: at t = 0, generic F: rank m = 4. If not 4, report the value and stop to rethink. (First run: rank 5 in the script's gauge, and rank 2 for F = F_01. Rethought: that t = 0 is not Fock. M2' below is the prediction restated, before its run.)
 M2': in Fock gauge, generic F: rank m = 4.
 M3: t random of several amplitudes: report rank. Expect 5.
 M4: t special: linear, staggered plus small, spike at one site, axial gauge. Report rank.
 M5 ADVERSARY (restated before its first run): minimise over t the sum of squares of ALL singular values of m on an orthonormal basis of NN(t), for F generic and for F simple, from polynomial and random starts. If < 1e-10 of the value at t = 0,
    the statement "m != 0" is false as posed; report the t. If it stays above 1e-4 of it from all starts, numerical evidence (only).
    Changed after a first run at L = 5: unbounded t runs away: m tends to 0 like |F|^2 / |d t| as t grows, because at F = 0 a polynomial pure gauge has m = 0. That is a scaling, not a zero: all singular values stayed non-zero, and the run ended with an SVD failure at |t| ~ 1e4.
    So t is now bounded, |t| <= M with M = 30 on a box of side 5 with |F| = 1, by t := M tanh(s / M). The criterion stands with this bound.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import resource
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_rank_box import Box  # noqa: E402


def check_rss(limit_gb=2.0):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3
    if r > limit_gb:
        raise MemoryError(f"rss {r:.2f} GB")
    return r


PLANES = list(itertools.combinations(range(4), 2))
MONOMIALS = [m for m in itertools.product(range(4), repeat=4) if sum(m) <= 3]


class Poly:
    """Polynomial link fields on a box: coordinates relative to the box centre, evaluated at link midpoints."""

    def __init__(self, box, c):
        self.box = box
        self.c = c
        self.X = box.mid - c
        pw = np.ones((box.W, len(MONOMIALS)))
        for j, m in enumerate(MONOMIALS):
            for a in range(4):
                if m[a]:
                    pw[:, j] *= self.X[:, a] ** m[a]
        self.dirs = np.array([l[1] for l in box.links])
        self.nm = len(MONOMIALS)
        self.M = np.zeros((box.W, 4 * self.nm))
        for r in range(4):
            sel = self.dirs == r
            self.M[sel, r * self.nm : (r + 1) * self.nm] = pw[sel]


class Moment:
    def __init__(self, L, Lp=None):
        self.L = L
        Lp = Lp or max(L, 6)
        # solve the polynomial identities on a box of side Lp, with coordinates relative to its centre
        bp = Box(Lp)
        cp = np.full(4, (Lp - 1) / 2.0)
        pp = Poly(bp, cp)
        curl_p = self.curl_matrix(bp)
        Hp = curl_p.T @ curl_p
        inner = np.array([i for i, (x, r) in enumerate(bp.links) if all(1 <= x[m] <= Lp - 2 for m in range(4) if m != r)])
        Hpoly = Hp[inner] @ pp.M
        U, s, Vt = np.linalg.svd(Hpoly, full_matrices=True)
        rk = int(np.sum(s > 1e-10 * s[0]))
        self.hom = Vt[rk:]  # coefficients of PP_h
        ek_p = self.linear_potentials(bp, cp)
        self.ek_coef = None
        self.Hpoly_pinv = (Vt[:rk].T / s[:rk]) @ U[:, :rk].T
        self.inner_p = inner
        self.bp, self.pp, self.curl_p, self.Hp, self.ek_p = bp, pp, curl_p, Hp, ek_p
        # test box
        self.box = Box(L)
        b = self.box
        self.c = np.full(4, (L - 1) / 2.0)
        self.poly = Poly(b, self.c)
        self.curl = self.curl_matrix(b)
        self.mean_m, self.mean_n = self.mean_matrices(b)
        self.e = self.linear_potentials(b, self.c)
        U, s, Vt = np.linalg.svd(b.D0.T, full_matrices=True)
        rk = int(np.sum(s > 1e-10 * s[0]))
        self.Zb = Vt[rk:]  # basis of conserved currents on the box, n x W
        self.n = self.Zb.shape[0]
        self.ends = np.zeros((b.W, 2), dtype=int)
        for i, (x, r) in enumerate(b.links):
            y = list(x)
            y[r] += 1
            self.ends[i] = (b.sidx[x], b.sidx[tuple(y)])
        self.mom_h = self.Zb @ (self.poly.M @ self.hom.T)  # n x dim PP_h

    @staticmethod
    def curl_matrix(b):
        C = np.zeros((b.P.shape[0], b.W))
        for i in range(b.P.shape[0]):
            a, bb, cc, e = b.P[i]
            C[i, [a, bb, cc, e]] = [1, 1, -1, -1]
        return C

    @staticmethod
    def mean_matrices(b):
        Mm = np.zeros((b.P.shape[0], b.W))
        Mn = np.zeros((b.P.shape[0], b.W))
        for i in range(b.P.shape[0]):
            a, bb, cc, e = b.P[i]
            Mm[i, [a, cc]] = 0.5
            Mn[i, [bb, e]] = 0.5
        return Mm, Mn

    @staticmethod
    def linear_potentials(b, c):
        """a_nu(x) = x_mu - c_mu on nu links: uniform flux +1 on (mu, nu) plaquettes. Linear in the coordinates of the base site; x_mu is the same along a nu link."""
        e = np.zeros((6, b.W))
        for k, (mu, nu) in enumerate(PLANES):
            for i, (x, r) in enumerate(b.links):
                if r == nu:
                    e[k, i] = x[mu] - c[mu]
        return e

    def J2_on(self, b, curl, Mm, Mn, e1, e2):
        """J2(l) = VV(delta_l, e1, e2)."""
        p1, m1, n1 = curl @ e1, Mm @ e1, Mn @ e1
        p2, m2, n2 = curl @ e2, Mm @ e2, Mn @ e2
        return curl.T @ (m1 * n2 - n1 * m2) - Mm.T @ (p1 * n2 - n1 * p2) + Mn.T @ (p1 * m2 - m1 * p2)

    def particular(self, F):
        """Polynomial coefficients of P[e_k, F], k = 0..5, and the relative error of the identity on the interior."""
        bp = self.bp
        Mm, Mn = self.mean_matrices(bp)
        eF = F @ self.ek_p
        coef = np.zeros((6, self.pp.M.shape[1]))
        worst = 0.0
        for k in range(6):
            tgt = self.J2_on(bp, self.curl_p, Mm, Mn, self.ek_p[k], eF)[self.inner_p]
            c = self.Hpoly_pinv @ tgt
            res = self.Hp[self.inner_p] @ (self.pp.M @ c) - tgt
            worst = max(worst, np.abs(res).max() / max(np.abs(tgt).max(), 1e-300))
            coef[k] = c
        return coef, worst

    def kernel(self, A, tol=1e-9):
        b = self.box
        A = A / max(np.abs(A).max(), 1e-300)  # the density rows must be on the scale of the moment rows, or the rank is wrong for small A
        prod = self.Zb * A[None, :]
        R = np.zeros((b.V, self.n))
        for i in range(b.W):
            xa, xb = self.ends[i]
            R[xa] += 0.5 * prod[:, i]
            R[xb] += 0.5 * prod[:, i]
        K = np.vstack([R, self.mom_h.T])
        U, s, Vt = np.linalg.svd(K, full_matrices=True)
        rk = int(np.sum(s > tol * max(s[0], 1e-300)))
        return Vt[rk:], rk

    def m_on_kernel(self, F, coef, t):
        b = self.box
        A = F @ self.e + b.D0 @ t
        Nz, rk = self.kernel(A)
        tbar = 0.5 * (t[self.ends[:, 0]] + t[self.ends[:, 1]])
        g = (self.poly.M @ coef.T).T - self.e * tbar[None, :]  # 6 x W
        mN = g @ self.Zb.T @ Nz.T
        return mN, Nz.shape[0], rk

    def report(self, F, coef, t, label):
        mN, dn, rk = self.m_on_kernel(F, coef, t)
        s = np.linalg.svd(mN, compute_uv=False) if mN.size else np.zeros(6)
        mF = F @ mN
        A = F @ self.e + self.box.D0 @ t
        prod = self.Zb * A[None, :]
        R = np.zeros((self.box.V, self.n))
        for i in range(self.box.W):
            xa, xb = self.ends[i]
            R[xa] += 0.5 * prod[:, i]
            R[xb] += 0.5 * prod[:, i]
        U_, s_, Vt_ = np.linalg.svd(R, full_matrices=True)
        rr = int(np.sum(s_ > 1e-9 * s_[0]))
        dipvals = (self.Zb @ self.e.T).T @ Vt_[rr:].T
        sd = np.linalg.svd(dipvals, compute_uv=False)
        print(f"{label}: rank(rho, moments)={rk} dim NN={dn} sv of m: " + " ".join(f"{v:.2e}" for v in s) + (f" | m(F) rel {np.abs(mF).max()/max(s[0],1e-300):.1e}" if mN.size else "") + " | sv of dip on N: " + " ".join(f"{v:.1e}" for v in sd), flush=True)
        return s


def main():
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    mode = sys.argv[2] if len(sys.argv) > 2 else "basic"
    rng = np.random.default_rng(3)
    t0 = time.time()
    Mo = Moment(L)
    b = Mo.box
    print(f"L={L}: sites {b.V} links {b.W} cycles {Mo.n} dim PP_h (with gradients) {Mo.hom.shape[0]} rank of its moments {np.linalg.matrix_rank(Mo.mom_h, tol=1e-8)} setup {time.time()-t0:.1f}s rss {check_rss():.2f}GB", flush=True)
    F = rng.normal(size=6)
    F = F / np.linalg.norm(F)
    coef, worst = Mo.particular(F)
    print(f"M0 polynomial identity worst rel residual {worst:.1e}", flush=True)
    Mo.report(F, coef, np.zeros(b.V), "M2 t = 0, generic F")
    idx0 = np.array(b.sites, dtype=float) - Mo.c
    def fock_t(Fv):
        return -0.5 * sum(Fv[k] * idx0[:, mu] * idx0[:, nu] for k, (mu, nu) in enumerate(PLANES))
    Mo.report(F, coef, fock_t(F), "M2' Fock gauge, generic F")
    F2 = np.zeros(6)
    F2[0] = 1.0
    coef2, w2 = Mo.particular(F2)
    Mo.report(F2, coef2, np.zeros(b.V), "   t = 0, F = F_01 only")
    Mo.report(F2, coef2, fock_t(F2), "   Fock gauge, F = F_01 only")
    for amp in (0.01, 0.1, 1.0, 10.0):
        Mo.report(F, coef, amp * rng.normal(size=b.V), f"M3 t random amp {amp}")
    idx = np.array(b.sites, dtype=float)
    Mo.report(F, coef, 0.3 * idx @ rng.normal(size=4), "M4 t linear")
    st = (idx.sum(axis=1) % 2) * 2 - 1
    Mo.report(F, coef, 5.0 * st, "M4 t staggered")
    Mo.report(F, coef, 5.0 * st + 0.1 * rng.normal(size=b.V), "M4 t staggered + small random")
    sp = np.zeros(b.V)
    sp[b.sidx[tuple([L // 2] * 4)]] = 100.0
    Mo.report(F, coef, sp, "M4 t spike")
    A0 = F @ Mo.e
    t_ax = np.zeros(b.V)
    for x in sorted(b.sites):
        if x[0] > 0:
            y = list(x)
            y[0] -= 1
            t_ax[b.sidx[x]] = t_ax[b.sidx[tuple(y)]] - A0[b.lidx[(tuple(y), 0)]]
    Mo.report(F, coef, t_ax, "M4 axial gauge, direction 0")
    sg3 = ((idx[:, 0] + idx[:, 1] + idx[:, 2]) % 2) * 2 - 1
    f4 = rng.normal(size=L)
    Mo.report(F, coef, 3.0 * sg3 * f4[idx[:, 3].astype(int)], "M4 t staggered in three directions, arbitrary in the fourth")
    Mo.report(F, coef, fock_t(F) + 3.0 * sg3 * f4[idx[:, 3].astype(int)], "M4 Fock plus the same")
    if mode == "adv":
        steps = int(sys.argv[3]) if len(sys.argv) > 3 else 600
        idc = np.array(b.sites, dtype=int)
        mons = [np.ones(b.V)] + [idx0[:, a] for a in range(4)] + [idx0[:, a] * idx0[:, c] for a in range(4) for c in range(a, 4)]
        mons = np.array(mons).T
        def fam_poly(c):
            return mons @ c
        def fam_one(c):  # a function of x_0 only, added to a quadratic
            return mons @ c[:15] + c[15:15 + L][idc[:, 0]]
        def fam_two(c):  # a function of (x_0, x_1), added to a quadratic
            return mons @ c[:15] + c[15:].reshape(L, L)[idc[:, 0], idc[:, 1]]
        fams = [("poly", fam_poly, 15), ("function of x_0", fam_one, 15 + L), ("function of (x_0, x_1)", fam_two, 15 + L * L), ("rough", lambda c: c, b.V)]
        for label, Fv, cf in (("generic F", F, coef), ("F = F_01", F2, coef2)):
            MB = 30.0
            def bound(tv):
                return MB * np.tanh(tv / MB)
            def total(tv):
                try:
                    mN, dn, rk = Mo.m_on_kernel(Fv, cf, bound(tv))
                except np.linalg.LinAlgError:
                    return 1e6
                return float(np.sum(mN**2))
            def svs(tv):
                mN, dn, rk = Mo.m_on_kernel(Fv, cf, bound(tv))
                return np.linalg.svd(mN, compute_uv=False), dn
            base = total(fock_t(Fv))
            print(f"M5 {label} L={L}: total in Fock gauge: {base:.3e}", flush=True)
            for name, fam, np_ in fams:
                for start in range(2):
                    t1 = time.time()
                    x0 = rng.normal(size=np_) * (10.0 ** rng.uniform(-1.5, 0.3))
                    res = minimize(lambda c: total(fam(c)), x0, method="Powell", options={"maxiter": 3, "maxfev": steps, "xtol": 1e-3, "ftol": 1e-8})
                    s_, dn = svs(fam(res.x))
                    print(f"   {name} start {start}: total / Fock = {res.fun/base:.3e}, sv " + " ".join(f"{u:.2e}" for u in s_) + f", max|t| {np.abs(bound(fam(res.x))).max():.1e}, dim NN {dn}, evals {res.nfev}, time {time.time()-t1:.0f}s rss {check_rss():.2f}GB", flush=True)


if __name__ == "__main__":
    main()
