#!/usr/bin/env python3
"""Kill test of the flat commuting response formula, by exact quadrature.

Registered before the first run (2026-11-01, mac-mini-worker, item joint-induction).

Model. Plaquette space R^m, split orthogonally as span(H) + span(K) + span(N).
Field theta = tau + K eta + N zeta, tau in span(H) fixed (the parent W).
Action A(theta) = sum_p s(theta_p), s(t) = 1 - cos t, so s''' = -t + ...
Level-j density of eta: rho(eta) = integral d zeta exp(-x A). a^w(eta) is the
weighted energy of the classical lift (zeta at its minimum given eta), which is
what (CF_j) defines, NOT the conditional mean of the fine energy.
Response: f(tau) := [E_tau x a^w - x a^w(crit)] at tau, minus the same at tau = 0.

Claim (F1). With P := K K^T + N N^T, Nn := N N^T, theta := critical field,
    f = Phi[P] - Phi[Nn] + (smaller),
    Phi[P] := (1/2) <w theta, P (theta diag P)> + (1/4) sum_pr w_p P_pr^2 theta_r^2
              - (1/4) sum_p w_p theta_p^2 P_pp.

Criteria, fixed now.
 T1 PASS if for every seed |f - formula| <= 0.05 |formula| at x = 1e7, |theta| about 0.05.
 T2 PASS if f(w = 1) is below 1e-3 |formula(w random)| (total response vanishes).
 T3 PASS if the residual falls by at least a factor 2 from |theta| = 0.1 to 0.05.
 C1, C2, C3 are controls and must FAIL T1 on at least half the seeds:
   C1 drops the N diagonal in the first term (the R_j term);
   C2 drops the mixed N K term of the second term (the lift's response);
   C3 sets Nn = 0 in the whole formula.
A failed criterion is kept. The run can refute (F1); it cannot prove it.
"""
import math
import resource
import sys

import numpy as np
from numpy.polynomial.hermite_e import hermegauss

RSS_LIMIT = 2 * 1024 ** 3


def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT:
        sys.exit("RSS guard: above 2 GB, stopping")


def s(t):
    return 1.0 - np.cos(t)


def sp(t):
    return np.sin(t)


def spp(t):
    return np.cos(t)


class Toy:
    def __init__(self, seed, m=7, dk=2, dn=1):
        rng = np.random.default_rng(seed)
        q, _ = np.linalg.qr(rng.normal(size=(m, m)))
        self.N = q[:, :dn]
        self.K = q[:, dn:dn + dk]
        self.H = q[:, dn + dk:]
        self.w = rng.uniform(0, 1, size=m)
        self.dir = rng.normal(size=m - dn - dk)
        self.dir /= np.linalg.norm(self.H @ self.dir, ord=np.inf)
        self.m, self.dk, self.dn = m, dk, dn

    def lift(self, tau, eta):
        """Minimise A over zeta at fixed tau + K eta, vectorised over eta (n, dk)."""
        base = tau[None, :] + eta @ self.K.T
        z = np.zeros((eta.shape[0], self.dn))
        for _ in range(60):
            th = base + z @ self.N.T
            g = sp(th) @ self.N
            hdiag = spp(th)
            Hm = np.einsum("ij,ki,kj->...", np.eye(1), np.zeros((1, 1)), np.zeros((1, 1))) if False else None
            Hmat = np.einsum("pi,np,pj->nij", self.N, hdiag, self.N)
            dz = np.linalg.solve(Hmat, g[..., None])[..., 0]
            z = z - dz
            if np.max(np.abs(dz)) < 1e-15:
                break
        return z

    def crit(self, tau):
        """Critical eta, zeta for the classical problem at tau."""
        eta = np.zeros((1, self.dk))
        z = np.zeros((1, self.dn))
        B = np.hstack([self.K, self.N])
        y = np.zeros(self.dk + self.dn)
        for _ in range(80):
            th = tau + B @ y
            g = B.T @ sp(th)
            Hm = B.T @ (spp(th)[:, None] * B)
            dy = np.linalg.solve(Hm, g)
            y = y - dy
            if np.max(np.abs(dy)) < 1e-15:
                break
        return y[: self.dk], y[self.dk:]

    def expectation(self, tau, x, nq=30, w=None):
        """E_tau[x (a^w(eta) - a^w(crit))] under rho, by nested Gauss-Hermite."""
        w = self.w if w is None else w
        g = 1.0 / math.sqrt(x)
        ec, zc = self.crit(tau)
        ye, we = hermegauss(nq)
        grids = np.meshgrid(*([ye] * self.dk), indexing="ij")
        Y = np.stack([a.ravel() for a in grids], axis=1)
        W = np.ones(Y.shape[0])
        for d in range(self.dk):
            W *= we[np.unravel_index(np.arange(Y.shape[0]), (nq,) * self.dk)[d]]
        eta = ec[None, :] + g * Y
        z = self.lift(tau, eta)
        th_lift = tau[None, :] + eta @ self.K.T + z @ self.N.T
        th_crit = tau + self.K @ ec + self.N @ zc
        # classical action relative to the critical point, and energy
        dA = np.sum(s(th_lift) - s(th_crit), axis=1)
        da = (s(th_lift) - s(th_crit)) @ w
        # inner integral over zeta around the lift (dn = 1 here)
        yi, wi = hermegauss(nq)
        inner = np.zeros(eta.shape[0])
        for k in range(eta.shape[0]):
            zeta = z[k, 0] + g * yi
            th = th_lift[k][None, :] + (zeta - z[k, 0])[:, None] * self.N[:, 0][None, :]
            ex = -x * (np.sum(s(th) - s(th_lift[k]), axis=1)) + 0.5 * yi ** 2
            inner[k] = np.sum(wi * np.exp(ex))
        logw = -x * dA + 0.5 * np.sum(Y ** 2, axis=1) + np.log(inner)
        logw -= logw.max()
        dens = W * np.exp(logw)
        guard()
        return float(np.sum(dens * (x * da)) / np.sum(dens)), self.K @ ec + self.N @ zc + tau


def phi(w, theta, P):
    d = np.diag(P)
    a = 0.5 * (w * theta) @ (P @ (theta * d))
    b = 0.25 * np.sum(w[:, None] * P ** 2 * (theta ** 2)[None, :])
    c = 0.25 * np.sum(w * theta ** 2 * d)
    return a + b - c


def formula(w, theta, Kp, Np, mode="full"):
    """Kp, Np projectors. mode selects the controls."""
    P = Kp + Np
    if mode == "full":
        return phi(w, theta, P) - phi(w, theta, Np)
    if mode == "C1":
        # first term with diag Kp only, in place of diag P
        d_k, d_n = np.diag(Kp), np.diag(Np)
        t1 = 0.5 * (w * theta) @ (Kp @ (theta * d_k))
        t2 = 0.5 * (w * theta) @ (Np @ (theta * d_k))
        t3 = 0.25 * np.sum(w[:, None] * (Kp ** 2 + 2 * Np * Kp) * (theta ** 2)[None, :])
        t4 = 0.25 * np.sum(w * theta ** 2 * d_k)
        return t1 + t2 + t3 - t4
    if mode == "C2":
        d_k, d_p = np.diag(Kp), np.diag(P)
        t1 = 0.5 * (w * theta) @ (Kp @ (theta * d_p))
        t2 = 0.5 * (w * theta) @ (Np @ (theta * d_k))
        t3 = 0.25 * np.sum(w[:, None] * (Kp ** 2) * (theta ** 2)[None, :])
        t4 = 0.25 * np.sum(w * theta ** 2 * d_k)
        return t1 + t2 + t3 - t4
    if mode == "C3":
        return phi(w, theta, Kp)
    raise ValueError(mode)


def main():
    x = 1e7
    seeds = range(1, 9)
    amp_hi, amp_lo = 0.10, 0.05
    res = {"full": [], "C1": [], "C2": [], "C3": []}
    t2 = []
    t3 = []
    for sd in seeds:
        toy = Toy(sd)
        Kp = toy.K @ toy.K.T
        Np = toy.N @ toy.N.T
        tau0 = np.zeros(toy.m)
        f0, _ = toy.expectation(tau0, x)
        out = {}
        for amp in (amp_hi, amp_lo):
            tau = amp * toy.H @ toy.dir
            f1, th = toy.expectation(tau, x)
            f = f1 - f0
            out[amp] = (f, th)
        f, th = out[amp_lo]
        F = formula(toy.w, th, Kp, Np)
        rel = abs(f - F) / abs(F)
        res["full"].append(rel)
        for mode in ("C1", "C2", "C3"):
            Fc = formula(toy.w, th, Kp, Np, mode)
            res[mode].append(abs(f - Fc) / abs(F))
        # T2: total response
        wone = np.ones(toy.m)
        f0t, _ = toy.expectation(tau0, x, w=wone)
        f1t, _ = toy.expectation(amp_lo * toy.H @ toy.dir, x, w=wone)
        t2.append(abs(f1t - f0t) / abs(F))
        fh, thh = out[amp_hi]
        Fh = formula(toy.w, thh, Kp, Np)
        t3.append((abs(fh - Fh) / abs(Fh), rel))
        print(f"seed {sd}: f={f:+.6e} formula={F:+.6e} rel={rel:.3e} "
              f"C1={res['C1'][-1]:.2e} C2={res['C2'][-1]:.2e} C3={res['C3'][-1]:.2e} "
              f"total={t2[-1]:.2e} rel@0.1={t3[-1][0]:.3e}", flush=True)
        guard()
    T1 = max(res["full"]) <= 0.05
    T2 = max(t2) <= 1e-3
    T3 = all(a >= 2 * b for a, b in t3)
    ctrl = {m: sum(r > 0.05 for r in res[m]) >= len(res[m]) / 2 for m in ("C1", "C2", "C3")}
    print("T1", "PASS" if T1 else "FAIL", "max rel", max(res["full"]))
    print("T2", "PASS" if T2 else "FAIL", "max", max(t2))
    print("T3", "PASS" if T3 else "FAIL", t3)
    print("controls fail T1 as they must:", ctrl)
    print("peak RSS bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == "__main__":
    main()
