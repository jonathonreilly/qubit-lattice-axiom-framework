#!/usr/bin/env python3
"""Monte Carlo check of the tree coefficient of the odd test, Wilson SU(2) on T^4.

T_cl(x; m,n,r) = (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2), W_1 = U_mn(x), W_2 = U_nr(x),
W_3 = U_rm(x), plaquettes based at x. For W = a + i v.sigma, T_cl = 2 v_1 . (v_2 x v_3).

Formula under test (checks/witness_tree_coeff.py): beta^2 <T_cl> -> K_total = 0.6157 at
T = infinity; K_comp = 0.3969 is the value with no vertex (Gaussian potential in Feynman
gauge). The finite-T trivial-holonomy value is computed in the same script family.

PRE-REGISTERED CRITERIA (written before the first run).
 M1 ZERO: a fit beta^2 <T> = K + K2 / beta over the listed beta has K different from 0 by more
    than 10 sigma. FAIL: the odd test has no leading term, and the plan changes.
 M2 VERTEX: K differs from K_comp = 0.3969 by more than 3 sigma. FAIL: the vertex is not seen.
 M3 VALUE: |K - K_total| < max(3 sigma, 0.03). FAIL: the formula is wrong, or T = 8 is too small
    for the formula; then a run at T = 10 decides between those.
 Control: <s_p> beta at large beta is close to 3/4, and the odd part under the reversed
 ordering T(W1,W3,W2) = -T(W1,W2,W3) holds exactly by construction (not a test).

Errors by binning in configurations. RSS checked against 2 GB.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import json
import resource
import sys
import time

import numpy as np

RSS_LIMIT_GB = 2.0


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss /= 1024.0
    g = rss / 1024.0 / 1024.0
    if g > RSS_LIMIT_GB:
        raise SystemExit(f"RSS {g:.2f} GB above limit")
    return g


def qmul(p, q):
    a, v = p[..., 0], p[..., 1:]
    b, w = q[..., 0], q[..., 1:]
    out = np.empty(np.broadcast_shapes(p.shape, q.shape))
    out[..., 0] = a * b - np.sum(v * w, axis=-1)
    out[..., 1:] = a[..., None] * w + b[..., None] * v - np.cross(v, w)
    return out


def qconj(p):
    out = p.copy()
    out[..., 1:] *= -1
    return out


class Field:
    def __init__(self, T, rng):
        self.T = T
        self.rng = rng
        self.U = np.zeros((4, T, T, T, T, 4))
        self.U[..., 0] = 1.0
        idx = np.indices((T, T, T, T))
        self.even = (idx.sum(axis=0) % 2) == 0

    def staple_sum(self, mu):
        U = self.U
        S = np.zeros(U.shape[1:])
        for nu in range(4):
            if nu == mu:
                continue
            # plaquette U_mu(x) U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1 = U_mu(x) * staple
            up = qmul(qmul(np.roll(U[nu], -1, axis=mu), qconj(np.roll(U[mu], -1, axis=nu))), qconj(U[nu]))
            # U_mu(x) U_nu(x+mu-nu)^-1 U_mu(x-nu)^-1 U_nu(x-nu)
            a = np.roll(np.roll(U[nu], -1, axis=mu), 1, axis=nu)
            dn = qmul(qmul(qconj(a), qconj(np.roll(U[mu], 1, axis=nu))), np.roll(U[nu], 1, axis=nu))
            S += up + dn
        return S

    def heatbath_half(self, mu, mask, beta):
        S = self.staple_sum(mu)[mask]
        k = np.sqrt(np.sum(S * S, axis=-1))
        Ubar = S / k[..., None]
        a = beta * k
        n = a.size
        x0 = np.empty(n)
        todo = np.arange(n)
        rng = self.rng
        while todo.size:
            r1 = 1.0 - rng.random(todo.size)
            r2 = rng.random(todo.size)
            r3 = 1.0 - rng.random(todo.size)
            r4 = rng.random(todo.size)
            delta = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / a[todo]
            ok = r4 * r4 <= 1.0 - 0.5 * delta
            x0[todo[ok]] = 1.0 - delta[ok]
            todo = todo[~ok]
        cth = 2 * rng.random(n) - 1
        phi = 2 * np.pi * rng.random(n)
        sth = np.sqrt(1 - cth * cth)
        r = np.sqrt(np.maximum(1 - x0 * x0, 0.0))
        X = np.stack([x0, r * sth * np.cos(phi), r * sth * np.sin(phi), r * cth], axis=-1)
        self.U[mu][mask] = qmul(X, qconj(Ubar))

    def sweep(self, beta):
        for mu in range(4):
            self.heatbath_half(mu, self.even, beta)
            self.heatbath_half(mu, ~self.even, beta)
        self.U /= np.sqrt(np.sum(self.U * self.U, axis=-1, keepdims=True))

    def plaq(self, mu, nu):
        U = self.U
        return qmul(
            qmul(qmul(U[mu], np.roll(U[nu], -1, axis=mu)), qconj(np.roll(U[mu], -1, axis=nu))),
            qconj(U[nu]),
        )

    def measure(self):
        P = {}
        for mu in range(4):
            for nu in range(mu + 1, 4):
                p = self.plaq(mu, nu)
                P[(mu, nu)] = p
                P[(nu, mu)] = qconj(p)
        s = np.mean([1 - np.mean(P[(m, n)][..., 0]) for m in range(4) for n in range(m + 1, 4)])
        vals = []
        for (m, n, r) in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
            v1, v2, v3 = P[(m, n)][..., 1:], P[(n, r)][..., 1:], P[(r, m)][..., 1:]
            vals.append(2 * np.mean(np.sum(v1 * np.cross(v2, v3), axis=-1)))
        return s, float(np.mean(vals))


def run(T, beta, ntherm, nmeas, every, seed):
    rng = np.random.default_rng(seed)
    f = Field(T, rng)
    for _ in range(ntherm):
        f.sweep(beta)
    ss, tt = [], []
    for i in range(nmeas):
        for _ in range(every):
            f.sweep(beta)
        s, t = f.measure()
        ss.append(s)
        tt.append(t)
    check_rss()
    return np.array(ss), np.array(tt)


def binned_err(x, nbins=20):
    n = len(x) // nbins
    b = x[: n * nbins].reshape(nbins, n).mean(axis=1)
    return float(b.mean()), float(b.std(ddof=1) / np.sqrt(nbins))


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    budget = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {"6": 600, "8": 800, "12": 1000, "16": 1400, "24": 2000, "32": 2600}
    rows = []
    for key, nmeas in budget.items():
        beta = float(key)
        t0 = time.time()
        ntherm = 200 if beta < 20 else 400
        ss, tt = run(T, beta, ntherm, nmeas, 1, seed=int(1000 * beta) + T)
        sm, se = binned_err(ss)
        tm, te = binned_err(tt)
        rows.append((beta, beta * beta * tm, beta * beta * te))
        print(f"T={T} beta={beta:g} nmeas={nmeas}: beta<s>={beta*sm:.4f}+-{beta*se:.4f} beta^2<T>={beta*beta*tm:.4f}+-{beta*beta*te:.4f} time={time.time()-t0:.0f}s rss={check_rss():.2f}GB", flush=True)
    b = np.array(rows)
    A = np.stack([np.ones(len(b)), 1.0 / b[:, 0]], axis=1)
    w = 1.0 / b[:, 2]
    cov = np.linalg.inv((A * w[:, None]).T @ (A * w[:, None]))
    par = cov @ ((A * w[:, None]).T @ (b[:, 1] * w))
    chi2 = float(np.sum(((A @ par - b[:, 1]) * w) ** 2))
    K, dK = par[0], np.sqrt(cov[0, 0])
    print(f"fit K={K:.4f}+-{dK:.4f} K2={par[1]:.3f}+-{np.sqrt(cov[1,1]):.3f} chi2/dof={chi2/(len(b)-2):.2f}")
    Ktot, Kcomp = 0.6157, 0.3969
    print(f"M1 {'PASS' if abs(K) > 10*dK else 'FAIL'} M2 {'PASS' if abs(K-Kcomp) > 3*dK else 'FAIL'} M3 {'PASS' if abs(K-Ktot) < max(3*dK, 0.03) else 'FAIL'}")


if __name__ == "__main__":
    main()
