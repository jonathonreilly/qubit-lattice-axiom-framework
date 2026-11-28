#!/usr/bin/env python3
"""Tree-level coefficient of the odd test on the Wilson lattice.

Setting (parts/witness.md, Text 2). Weight exp(-beta sum_p s_p), s_p = 1 - (1/2) Tr U_p,
U_b = exp(i A_b . sigma / 2). Three closed paths Gamma_1,2,3 with a common base point,
W_i their holonomies, T = (1/2) Tr(W_1 W_2 W_3) - (1/2) Tr(W_1 W_3 W_2).

Formal expansion, with G = (-Delta)^{-1} on links (Feynman gauge), J_i the link current of
Gamma_i, E_i = G J_i, P_i(p) = (d E_i)_p:

  <T> = K_total / beta^2 + O(beta^-3),
  K_total = K_comp + K_vert,
  K_comp = -12 [ A_1(E_2, E_3) + A_2(E_3, E_1) + A_3(E_1, E_2) ],
  K_vert = +12 sum_p V_p(E_1, E_2, E_3),
  A_k(E, F) = sum_{s<t on Gamma_k} eps_s eps_t [ E(s) F(t) - E(t) F(s) ],
  V_p = sum_{i<j on p} eps_i eps_j det[ (P_k(p), E_k(b_i), E_k(b_j)) ]_{k=1,2,3}.

K_comp alone is what the Gaussian potential with covariance (4/beta) G gives.

PRE-REGISTERED CRITERIA (written before the first run).
 C1 GAUGE: replacing E_3 by E_3 + d theta, with random theta on sites, leaves K_total
    unchanged to relative 1e-9, and changes K_comp by more than 1e-3 relative to itself or
    to K_total. FAIL means an algebra error in the formula.
 C2 D2: in d = 2 with three disjoint plaquette lassos K_total -> 0 as T -> infinity like
    the -1/V tail of P (|K_total| < 20 * (9/V) for the tested T). FAIL means the formula
    does not see that plaquettes on the plane are independent.
 C3 NONZERO: in d = 4, K_total for the corner cluster at T = 32 differs from 0 by more
    than 10 times its change between T = 24 and T = 32. If not, the plan changes.
 C4 FAR: in d = 4, with Gamma_1, Gamma_2 near the origin and Gamma_3 far at distance R along
    a direction, |K_comp| scales with exponent near -3 and |K_total| with exponent near -4,
    in the range R where the torus is not felt. Only a report: exponents fitted between R
    and 2 R. FAIL (exponent of K_total within 0.25 of -3) would refute the Ward cancellation.

Memory: one source field is 4 T^4 doubles; three sources at T = 32 are 32 MB times 3.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import resource
import sys

import numpy as np

RSS_LIMIT_GB = 2.0


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss /= 1024.0
    rss_gb = rss / 1024.0 / 1024.0
    if rss_gb > RSS_LIMIT_GB:
        raise SystemExit(f"RSS {rss_gb:.2f} GB above limit")
    return rss_gb


class Lat:
    def __init__(self, d, T):
        self.d, self.T = d, T
        self.shape = (T,) * d
        k = 2 * np.pi * np.fft.fftfreq(T)
        khat2 = 2 - 2 * np.cos(k)
        grids = np.meshgrid(*([khat2] * d), indexing="ij", sparse=True)
        lap = sum(grids)
        with np.errstate(divide="ignore"):
            inv = 1.0 / lap
        inv[(0,) * d] = 0.0
        self.inv = inv

    def G(self, f):
        """(-Delta)^{-1} on zero-mean scalar field."""
        return np.fft.ifftn(np.fft.fftn(f) * self.inv).real


def path_links(lat, start, steps):
    """steps: list of signed directions (+1..+d, -1..-d). Returns [(site, mu, eps)]."""
    x = np.array(start) % lat.T
    out = []
    for s in steps:
        mu = abs(s) - 1
        if s > 0:
            out.append((tuple(x), mu, +1))
            x = x.copy()
            x[mu] = (x[mu] + 1) % lat.T
        else:
            x = x.copy()
            x[mu] = (x[mu] - 1) % lat.T
            out.append((tuple(x), mu, -1))
    if tuple(x) != tuple(np.array(start) % lat.T):
        raise ValueError("path not closed")
    return out


def current(lat, links):
    J = np.zeros((lat.d,) + lat.shape)
    for site, mu, eps in links:
        J[(mu,) + site] += eps
    return J


def field_E(lat, J):
    return np.stack([lat.G(J[mu]) for mu in range(lat.d)])


def curl(lat, E, mu, nu):
    """P(x; mu, nu) = E_mu(x) + E_nu(x+mu) - E_mu(x+nu) - E_nu(x), path order +mu +nu -mu -nu."""
    return E[mu] + np.roll(E[nu], -1, axis=mu) - np.roll(E[mu], -1, axis=nu) - E[nu]


def lievy(links, E, F):
    """A(E, F) = sum_{s<t} eps_s eps_t [ E(s) F(t) - E(t) F(s) ] along the path."""
    e = np.array([eps * E[(mu,) + site] for site, mu, eps in links])
    f = np.array([eps * F[(mu,) + site] for site, mu, eps in links])
    ce = np.cumsum(e)
    cf = np.cumsum(f)
    # sum_{s<t} e_s f_t = sum_t ce_{t-1} f_t
    return float(np.sum(ce[:-1] * f[1:]) - np.sum(cf[:-1] * e[1:]))


def K_comp(lat, L1, L2, L3, E1, E2, E3):
    return -12.0 * (lievy(L1, E2, E3) + lievy(L2, E3, E1) + lievy(L3, E1, E2))


def K_vert(lat, E1, E2, E3):
    total = 0.0
    Es = (E1, E2, E3)
    for mu in range(lat.d):
        for nu in range(mu + 1, lat.d):
            P = [curl(lat, E, mu, nu) for E in Es]
            # increments of the 4 links, path order +mu +nu -mu -nu, signs included
            inc = []
            for E in Es:
                inc.append(
                    [
                        E[mu],
                        np.roll(E[nu], -1, axis=mu),
                        -np.roll(E[mu], -1, axis=nu),
                        -E[nu],
                    ]
                )
            for i in range(4):
                for j in range(i + 1, 4):
                    a = [P[k] for k in range(3)]
                    b = [inc[k][i] for k in range(3)]
                    c = [inc[k][j] for k in range(3)]
                    det = (
                        a[0] * (b[1] * c[2] - b[2] * c[1])
                        - a[1] * (b[0] * c[2] - b[2] * c[0])
                        + a[2] * (b[0] * c[1] - b[1] * c[0])
                    )
                    total += float(np.sum(det))
    return 12.0 * total


def plaq(mu, nu):
    return [mu, nu, -mu, -nu]


def lasso(tail, loop):
    return list(tail) + list(loop) + [-s for s in reversed(tail)]


def straight_tail(x):
    tail = []
    for mu, n in enumerate(x):
        tail += [(mu + 1) if n > 0 else -(mu + 1)] * abs(n)
    return tail


def evaluate(lat, base, steps1, steps2, steps3, gauge_test=False, seed=1):
    L1 = path_links(lat, base, steps1)
    L2 = path_links(lat, base, steps2)
    L3 = path_links(lat, base, steps3)
    E1 = field_E(lat, current(lat, L1))
    E2 = field_E(lat, current(lat, L2))
    E3 = field_E(lat, current(lat, L3))
    kc = K_comp(lat, L1, L2, L3, E1, E2, E3)
    kv = K_vert(lat, E1, E2, E3)
    out = {"K_comp": kc, "K_vert": kv, "K_total": kc + kv}
    if gauge_test:
        rng = np.random.default_rng(seed)
        theta = rng.normal(size=lat.shape)
        dth = np.stack([np.roll(theta, -1, axis=mu) - theta for mu in range(lat.d)])
        E3g = E3 + dth
        kc2 = K_comp(lat, L1, L2, L3, E1, E2, E3g)
        kv2 = K_vert(lat, E1, E2, E3g)
        out.update({"K_comp_g": kc2, "K_vert_g": kv2, "K_total_g": kc2 + kv2})
    check_rss()
    return out


def main():
    print("# C1 GAUGE and corner cluster, d = 4")
    results = {}
    for T in (16, 24, 32):
        lat = Lat(4, T)
        r = evaluate(lat, (0, 0, 0, 0), plaq(1, 2), plaq(2, 3), plaq(3, 1), gauge_test=(T == 16))
        results[T] = r
        print(f"T={T} corner (12,23,31): K_comp={r['K_comp']:.9f} K_vert={r['K_vert']:.9f} K_total={r['K_total']:.9f} rss={check_rss():.2f}GB", flush=True)
        if T == 16:
            rel = abs(r["K_total_g"] - r["K_total"]) / max(abs(r["K_total"]), 1e-30)
            shift = abs(r["K_comp_g"] - r["K_comp"])
            ok = rel < 1e-9 and shift > 1e-3 * max(abs(r["K_comp"]), abs(r["K_total"]))
            print(f"C1 {'PASS' if ok else 'FAIL'}: rel change of K_total {rel:.2e}, shift of K_comp {shift:.3e}")
    drift = abs(results[32]["K_total"] - results[24]["K_total"])
    print(f"C3 {'PASS' if abs(results[32]['K_total']) > 10 * drift else 'FAIL'}: K_total(32)={results[32]['K_total']:.8f}, drift={drift:.2e}")

    print("# C2 D2: three disjoint plaquette lassos in d = 2")
    for T in (16, 32, 64):
        lat = Lat(2, T)
        s1 = plaq(1, 2)
        s2 = lasso(straight_tail((3, 0)), plaq(1, 2))
        s3 = lasso(straight_tail((0, 3)), plaq(1, 2))
        r = evaluate(lat, (0, 0), s1, s2, s3)
        bound = 20 * 9 / T**2
        print(f"T={T}: K_comp={r['K_comp']:.6e} K_vert={r['K_vert']:.6e} K_total={r['K_total']:.6e} bound={bound:.2e} {'PASS' if abs(r['K_total']) < bound else 'FAIL'}")

    print("# C4 FAR: Gamma_1 = p_12(0), Gamma_2 = lasso to (0,0,2,0) p_34, Gamma_3 far along (R,R,R,R)")
    T = 40
    lat = Lat(4, T)
    rows = []
    for R in (2, 3, 4, 6):
        s1 = plaq(1, 2)
        s2 = lasso(straight_tail((0, 0, 2, 0)), plaq(1, 3))
        s3 = lasso(straight_tail((R, R, R, 2 * R)), plaq(2, 3))
        r = evaluate(lat, (0, 0, 0, 0), s1, s2, s3)
        rows.append((R, r["K_comp"], r["K_total"]))
        print(f"R={R}: K_comp={r['K_comp']:.6e} K_vert={r['K_vert']:.6e} K_total={r['K_total']:.6e} rss={check_rss():.2f}GB", flush=True)
    for (R0, c0, t0), (R1, c1, t1) in zip(rows, rows[1:]):
        print(f"R {R0}->{R1}: slope K_comp {np.log(abs(c1/c0))/np.log(R1/R0):.2f}, slope K_total {np.log(abs(t1/t0))/np.log(R1/R0):.2f}")


if __name__ == "__main__":
    main()
