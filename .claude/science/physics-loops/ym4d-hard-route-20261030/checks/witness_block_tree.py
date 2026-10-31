#!/usr/bin/env python3
"""Tree coefficient of the odd test on blocked links: test of Lemma 5.4 at level 1, for one simple map.

Blocking map (not the hard core's, only gauge covariant, strictly local and symmetric): a coarse link from x to
x + L e_mu is normalise( w_0 U_straight + w_1 sum_(nu != mu, sign) U_staple ), with a staple of height 1. To second order
in A, log V = sum_pi w_pi ( Phi_pi + Q_pi ) (the normalisation removes the real part), so for a coarse closed path

  A~_Gamma(E, F) = sum_s eps_s sum_pi w_pi A_pi(E, F) + sum_(s<t) eps_s eps_t ( Ebar_s Fbar_t - Ebar_t Fbar_s ),
  Ebar_s := sum_pi w_pi E(pi), with E(pi) the line integral along the fine path pi, and A_pi the Levy area of the open path pi.

K^(1) = 12 sum_p V_p(E_1, E_2, E_3) - 12 [ A~_1(E_2, E_3) + A~_2(E_3, E_1) + A~_3(E_1, E_2) ], with p over FINE plaquettes,
and E_i = G J_i^(1), where J_i^(1) is the conserved fine current of the coarse closed path.

PRE-REGISTERED CRITERIA (written before the first run).
 B1 WARD: K^(1) is unchanged by E_3 -> E_3 + d_0 theta, with theta random on fine sites: relative 1e-9. FAIL means the second-order form
    A~ is wrong or the claim of Lemma 5.4 about gauge covariance does not hold in this form.
 B2 DECOUPLE: for a coarse (1,2) plaquette and a coarse (3,4) plaquette, E lives on directions (1,2) and (3,4) respectively, and P = 0, to 1e-12.
 B3 RECTANGLE: Stk^(1) := sum_k K^(1)(T^(k)) / P_k^(1) satisfies |Stk^(1)| < 0.6 * 24 |Flux^(1)| at the largest coarse R tried, and the ratio decreases with R.
    FAIL means the Wilson side reads the flux at level 1, and Lemma 5.4 does not hold for this map.
 B4 UNIVERSAL: the level-1 rectangle sum and the level-0 rectangle sum at the same physical geometry (D, R) x L agree within a factor 2.
    Only a report at these small sizes. RESULT: failed as written, ratio 34. The criterion was badly posed: level-0 unit plaquettes against 3 x 3 blocked loops
    differ by the area, a factor 9 in this normalisation, and D = 1 is not separated from the loop size. Replaced by B4'.
 B4' (added after B4, before running it): at coarse D = 3, compare the map at w0 = 0.4 with straight fine loops of the same size, w0 = 1 in this same script. In the mode
    "compare", the ratios of Stk_total and of Flux between the two are within 1 +- 0.5 at the largest R. FAIL means the rectangle sum at this size still depends
    strongly on the blocking, and uniformity in the map needs larger D than I can reach here.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_stokes import run as level0_run  # noqa: E402
from witness_tree_coeff import K_vert, Lat, check_rss, curl, field_E, lievy, plaq  # noqa: E402


def fine_path(lat, start, steps):
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
    return out


class Block:
    def __init__(self, lat, L, w0, d=4):
        self.lat, self.L, self.d = lat, L, d
        self.w0 = w0
        self.w1 = (1.0 - w0) / (2 * (d - 1))

    def paths(self, x, mu):
        """Fine paths with weights for the coarse link from fine site x along mu (mu 1-based, positive)."""
        L = self.L
        straight = [mu] * L
        out = [(self.w0, fine_path(self.lat, x, straight))]
        for nu in range(1, self.d + 1):
            if nu == mu:
                continue
            for sgn in (+1, -1):
                out.append((self.w1, fine_path(self.lat, x, [sgn * nu] + straight + [-sgn * nu])))
        return out


def link_value(E, plink):
    return sum(eps * E[(mu,) + site] for site, mu, eps in plink)


class CoarsePath:
    """A closed coarse path, given by a fine start and signed coarse steps."""

    def __init__(self, block, start, steps):
        self.block = block
        self.lat = block.lat
        L = block.L
        x = np.array(start)
        self.links = []  # (paths, eps)
        for s in steps:
            mu = abs(s)
            if s > 0:
                self.links.append((block.paths(tuple(x % self.lat.T), mu), +1))
                x = x + L * np.eye(4, dtype=int)[mu - 1]
            else:
                x = x - L * np.eye(4, dtype=int)[mu - 1]
                self.links.append((block.paths(tuple(x % self.lat.T), mu), -1))
        if tuple(x % self.lat.T) != tuple(np.array(start) % self.lat.T):
            raise ValueError("coarse path not closed")

    def current(self):
        J = np.zeros((4,) + self.lat.shape)
        for paths, eps in self.links:
            for w, pl in paths:
                for site, mu, e in pl:
                    J[(mu,) + site] += eps * w * e
        return J

    def form_coarse(self, E, F):
        """The Levy area on the coarse path of the blocked values only: what a Gaussian potential on the level-1 lattice sees."""
        ebar, fbar = [], []
        for paths, eps in self.links:
            eb = sum(w * link_value(E, pl) for w, pl in paths)
            fb = sum(w * link_value(F, pl) for w, pl in paths)
            ebar.append(eps * eb)
            fbar.append(eps * fb)
        ce, cf = np.cumsum(ebar), np.cumsum(fbar)
        ebar, fbar = np.array(ebar), np.array(fbar)
        return float(np.sum(ce[:-1] * fbar[1:]) - np.sum(cf[:-1] * ebar[1:]))

    def form(self, E, F):
        """A~(E, F) as in the module docstring."""
        tot = 0.0
        ebar, fbar = [], []
        for paths, eps in self.links:
            eb, fb = 0.0, 0.0
            local = 0.0
            for w, pl in paths:
                eb += w * link_value(E, pl)
                fb += w * link_value(F, pl)
                local += w * lievy(pl, E, F)
            # reversing an open path: its Levy area changes sign, and increments change sign
            tot += eps * local
            ebar.append(eps * eb)
            fbar.append(eps * fb)
        ce = np.cumsum(ebar)
        cf = np.cumsum(fbar)
        ebar = np.array(ebar)
        fbar = np.array(fbar)
        tot += float(np.sum(ce[:-1] * fbar[1:]) - np.sum(cf[:-1] * ebar[1:]))
        return tot


def coarse_steps_between(a, b):
    out = []
    for mu in range(len(a)):
        n = b[mu] - a[mu]
        out += [(mu + 1) if n > 0 else -(mu + 1)] * abs(n)
    return out


def lasso(tail, loop):
    return list(tail) + list(loop) + [-s for s in reversed(tail)]


def K1(block, base, s1, s2, s3, E1, E2, E3):
    lat = block.lat
    G1 = CoarsePath(block, base, s1)
    G2 = CoarsePath(block, base, s2)
    G3 = CoarsePath(block, base, s3)
    kc = -12.0 * (G1.form(E2, E3) + G2.form(E3, E1) + G3.form(E1, E2))
    kv = K_vert(lat, E1, E2, E3)
    return kc, kv


def run_rect(block, D, R):
    """Coarse rectangle: D, R in coarse units."""
    lat, L = block.lat, block.L
    c = (D - 1) // 2
    far_c = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    fine = lambda y: tuple(L * v for v in y)
    Es = {y: field_E(lat, CoarsePath(block, fine(y), plaq(1, 2)).current()) for y in corners}
    Jfar = CoarsePath(block, fine(far_c), plaq(3, 4)).current()
    E3 = field_E(lat, Jfar)
    stk_c, stk_t = 0.0, 0.0
    Pk = None
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        s1 = plaq(1, 2)
        s2 = lasso(coarse_steps_between(y, z), plaq(1, 2))
        s3 = lasso(coarse_steps_between(y, far_c), plaq(3, 4))
        E1, E2 = Es[y], Es[z]
        kc, kv = K1(block, fine(y), s1, s2, s3, E1, E2, E3)
        J2 = CoarsePath(block, fine(z), plaq(1, 2)).current()
        Pk = float(np.sum(J2 * E1))
        stk_c += kc / Pk
        stk_t += (kc + kv) / Pk
    # level-1 flux of the far loop through the coarse square: the blocked covariance of the far loop with the boundary of the square,
    # which is what -24 Flux means for a Gaussian potential on the level-1 lattice with the matched covariance
    Jsq = CoarsePath(block, fine((0, 0, 0, 0)), [3] * D + [4] * D + [-3] * D + [-4] * D).current()
    flux = float(np.sum(Jsq * E3))
    return stk_c, stk_t, flux, Pk


def compare(Tc):
    L = 3
    lat = Lat(4, L * Tc)
    b_a = Block(lat, L, 0.4)
    b_b = Block(lat, L, 1.0)
    for (D, R) in ((3, 4), (3, 5)):
        sca, sta, fa, Pa = run_rect(b_a, D, R)
        scb, stb, fb, Pb = run_rect(b_b, D, R)
        print(f"D={D} R={R}: w0=0.4 Stk_total={sta:.5e} -24Flux={-24*fa:.5e} ratio={abs(sta)/(24*abs(fa)):.4f} P_k={Pa:.4e} | w0=1 Stk_total={stb:.5e} -24Flux={-24*fb:.5e} ratio={abs(stb)/(24*abs(fb)):.4f} P_k={Pb:.4e} | Stk {sta/stb:.3f} Flux {fa/fb:.3f} rss={check_rss():.2f}GB", flush=True)


def main():
    L = 3
    if len(sys.argv) > 2 and sys.argv[2] == "compare":
        compare(int(sys.argv[1]))
        return
    Tc = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    w0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.4
    lat = Lat(4, L * Tc)
    block = Block(lat, L, w0)
    print(f"L={L} T_c={Tc} T_f={lat.T} w0={w0} w1={block.w1:.4f}", flush=True)

    # B1, B2 on one triple
    y0 = (0, 0, 0, 0)
    s1 = plaq(1, 2)
    s2 = lasso(coarse_steps_between((0, 0, 0, 0), (0, 0, 2, 0)), plaq(1, 2))
    s3 = lasso(coarse_steps_between((0, 0, 0, 0), (2, 0, 0, 0)), plaq(1, 3))
    G1, G2, G3 = CoarsePath(block, y0, s1), CoarsePath(block, y0, s2), CoarsePath(block, y0, s3)
    E1, E2, E3 = field_E(lat, G1.current()), field_E(lat, G2.current()), field_E(lat, G3.current())
    kc, kv = K1(block, y0, s1, s2, s3, E1, E2, E3)
    rng = np.random.default_rng(2)
    theta = rng.normal(size=lat.shape)
    dth = np.stack([np.roll(theta, -1, axis=m) - theta for m in range(4)])
    kc2, kv2 = K1(block, y0, s1, s2, s3, E1, E2, E3 + dth)
    print(f"B1 {'PASS' if abs((kc2+kv2)-(kc+kv))/abs(kc+kv) < 1e-9 else 'FAIL'}: K_total={kc+kv:.8e} after gauge {kc2+kv2:.8e} K_comp shift {kc2-kc:.3e} rss={check_rss():.2f}GB", flush=True)

    Jp = CoarsePath(block, y0, plaq(1, 2)).current()
    Jq = CoarsePath(block, tuple(L * v for v in (2, 0, 0, 0)), plaq(3, 4)).current()
    off = max(np.max(np.abs(Jp[2])), np.max(np.abs(Jp[3])), np.max(np.abs(Jq[0])), np.max(np.abs(Jq[1])))
    Ep = field_E(lat, Jp)
    print(f"B2 {'PASS' if off < 1e-12 and abs(np.sum(Jq * Ep)) < 1e-12 else 'FAIL'}: off-plane current {off:.1e}, P = {np.sum(Jq * Ep):.1e}", flush=True)

    rows = []
    for (D, R) in ((1, 2), (1, 3), (1, 4), (1, 5)):
        sc, st, flux, Pk = run_rect(block, D, R)
        rows.append((D, R, sc, st, flux))
        print(f"D={D} R={R}: Stk_comp={sc:.5e} -24Flux={-24*flux:.5e} Stk_total={st:.5e} ratio={abs(st)/(24*abs(flux)):.4f} P_k={Pk:.4e} rss={check_rss():.2f}GB", flush=True)
    for (D, R, sc, st, flux) in rows[:2]:
        rows0, sc0, st0, salt0, flux0 = level0_run(lat.T, D * L, R * L)
        print(f"level 0 at (D, R) = ({D*L}, {R*L}): Stk_total={st0:.5e} -24Flux={-24*flux0:.5e}; level 1 / level 0 of Stk_total = {st/st0:.3f}, of Flux = {flux/flux0:.3f}", flush=True)


if __name__ == "__main__":
    main()
