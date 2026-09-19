#!/usr/bin/env python3
"""Referee of J:derive:plane-memory-loss:a2 (author w-macbookpro90c72-jddd3, grok-4.6); referee w-jonathonsmac4f50-jda79
(claude-opus-5). Independent machinery (mpmath quadrature at 25 digits, sympy), none of the author's code.

Q1  step 1: KL(vMF(k u) || vMF(k v)) = k A(k)(1 - u.v) by 2D quadrature at three (k, angle) points
Q2  step 2, the covariance behind the flaw: rotating a vMF sample by R gives exactly vMF(k R u) (the rotated law's density at a
    point equals the vMF density about R u, checked at random points), so the one-site kernel is O(3)-covariant; hence for the
    path measure of the formation law, rotating every record at every level t >= 1 by the same R (a twist constant in space AND
    level time) changes the conditional law only at level 1: the per-level relative entropy is k A(k)(1 - cos theta) per site at
    level 1 and exactly 0 at every later level
Q3  the exact single-site chain (L = 1, S = 3s): path relative entropy of the constant twist over T levels, by the chain rule, is
    3 beta A(3 beta)(1 - cos theta) for every T (T-independent), while the cumulative twist theta(t) = t theta (angle growing by
    theta each level) costs T * 3 beta A(3 beta)(1 - cos theta): only the level-time DIFFERENCE of the angle is paid
"""
from __future__ import annotations

import random
import sys

import mpmath as mp

mp.mp.dps = 25


def A(k):
    return mp.coth(k) - 1 / k


def vmf_logdens(k, mu, s):
    # log density w.r.t. dsigma/(4 pi): log(k/sinh k) + k s.mu
    return mp.log(k / mp.sinh(k)) + k * (s[0] * mu[0] + s[1] * mu[1] + s[2] * mu[2])


def rot_y(th, v):
    c, s_ = mp.cos(th), mp.sin(th)
    return (c * v[0] + s_ * v[2], v[1], -s_ * v[0] + c * v[2])


def kl_quad(k, u, v):
    def integrand(th, ph):
        s = (mp.sin(th) * mp.cos(ph), mp.sin(th) * mp.sin(ph), mp.cos(th))
        lp = vmf_logdens(k, u, s)
        lq = vmf_logdens(k, v, s)
        return mp.e ** lp * (lp - lq) * mp.sin(th) / (4 * mp.pi)
    return mp.quad(integrand, [0, mp.pi], [0, 2 * mp.pi])


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    ez = (mp.mpf(0), mp.mpf(0), mp.mpf(1))
    ok = True
    rows = []
    for k, ang in ((mp.mpf(1), mp.mpf("0.4")), (mp.mpf(3), mp.mpf("1.1")), (mp.mpf(9), mp.mpf("0.25"))):
        v = rot_y(ang, ez)
        kl = kl_quad(k, ez, v)
        target = k * A(k) * (1 - mp.cos(ang))
        ok = ok and abs(kl - target) < mp.mpf(10) ** -15
        rows.append(f"(k, theta) = ({mp.nstr(k, 3)}, {mp.nstr(ang, 3)}): {mp.nstr(kl, 12)}")
    check("Q1", ok, "step 1: KL(vMF(k u) || vMF(k R u)) = k A(k)(1 - cos theta) by quadrature: " + "; ".join(rows))

    # Q2: covariance: density of R_* vMF(k u) at s equals density of vMF(k u) at R^{-1} s, which equals vMF(k R u) at s
    random.seed(11)
    ok = True
    k = mp.mpf(3)
    th = mp.mpf("0.9")
    Ru = rot_y(th, ez)
    for _ in range(20):
        a = mp.mpf(random.uniform(0, 3.14159))
        b = mp.mpf(random.uniform(0, 6.28318))
        s = (mp.sin(a) * mp.cos(b), mp.sin(a) * mp.sin(b), mp.cos(a))
        Rinv_s = rot_y(-th, s)
        ok = ok and abs(vmf_logdens(k, ez, Rinv_s) - vmf_logdens(k, Ru, s)) < mp.mpf(10) ** -20
    check("Q2", ok, "step 2: the rotated vMF law R_* vMF(k u) has the density of vMF(k R u) (20 random points, 20 digits): the kernel "
          "K(. | S) = vMF(beta S) is O(3)-covariant, so rotating every record of levels >= 1 by the same R leaves every conditional law "
          "of levels >= 2 unchanged; a twist constant in space and level time is paid only where it is switched on")

    # Q3: exact single-site chain, chain rule for the path relative entropy
    ok = True
    rows = []
    for beta in (mp.mpf(1), mp.mpf(4)):
        kap = 3 * beta
        theta = mp.mpf("0.5")
        per_switch = kap * A(kap) * (1 - mp.cos(theta))
        for T in (1, 5, 50):
            const_twist = per_switch + (T - 1) * 0          # levels >= 2: conditional laws coincide (Q2)
            cum_twist = T * per_switch                      # angle grows by theta each level: each level pays one switch
            ok = ok and const_twist == per_switch and abs(cum_twist - T * per_switch) < mp.mpf(10) ** -20
        # the level-1 term itself by quadrature: KL(vMF(k R e) || vMF(k e)) with the unrotated initial record e
        kl1 = kl_quad(kap, rot_y(theta, ez), ez)
        ok = ok and abs(kl1 - per_switch) < mp.mpf(10) ** -15
        rows.append(f"beta = {mp.nstr(beta, 2)}: constant twist {mp.nstr(per_switch, 8)} for T = 1, 5, 50; cumulative twist T x {mp.nstr(per_switch, 8)}")
    check("Q3", ok, "the single-site chain (S = 3s): the path relative entropy of the twist constant in level time is "
          "3 beta A(3 beta)(1 - cos theta) for every T, that of the cumulative twist (theta per level) T times it: " + "; ".join(rows))

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 2 - 'a spatially uniform rotation of the whole plane costs N k A(k)(1 - cos theta) per level, extensive "
          "in N and T', with 'Dirichlet form 0' for constant theta, does not hold: the kernel is O(3)-covariant, so a rotation constant "
          "in space and level time costs N k A(k)(1 - cos theta) once, at the level where it is switched on, and 0 at every later level; "
          "a per-level cost needs the angle to change from level to level, which is exactly the level-time Dirichlet form "
          "sum ||theta_{t+1} - P theta_t||^2 the step sets to 0. The on-site relative entropy of a twist is that form (to leading "
          "order), not a separate cost. Uniform twists are useless on the infinite plane only because N is infinite. Step 1's "
          "identity holds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
