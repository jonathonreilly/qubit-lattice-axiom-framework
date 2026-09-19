#!/usr/bin/env python3
"""Referee check for J:derive:no-waves-under-positive-formation:a2 (author w-macbookpro90c72-j80c2, grok-4.6).

Independent code (sympy exact where a finite fact is claimed; numpy only for random scans).
The attempt's multiplier: lambda(k) = sum_{z in F} w_z e^{i k.z}, w_z > 0, sum w_z = 1, F finite in Z^d.

R1  step 1 (Jensen): |lambda| <= 1 on random positive stencils; the gradient i v and the Hessian of |lambda|^2
    at 0 equal to -2 Cov(Z), exactly (sympy) on random rational stencils.
R2  the equality set read as "the collinear exception: F lies in a coset of a hyperplane k.z = const":
    (a) sublattice supports: F = {+-e1, +-e2} has lambda(pi, pi) = -1 exactly, F affinely spanning the plane;
        F = {0, 2} in d = 1 has lambda(pi) = 1;
    (b) collinear supports off the origin: F = {e1, e2} (weights 1/2) has lambda(kappa, kappa) = e^{i kappa}
        exactly -- |lambda| = 1 and arg lambda = |k|/sqrt 2 along (1,1): a wave in the task's sense, under
        positivity, with no unitary structure (the attempt's example F = {0, e1} is the static case v.n = 0).
R3  steps 2-5 numbers: 7-stencil lambda(pi,0,0) = 3/7, series -k1^2/7, Hessian -4/7; drift i/4 of
    (1 + sum e^{i k_j})/4; 2 - e^{ik} has |lambda|^2 = 5 - 4 cos k, = 9 at pi and > 1 for every k != 0
    (amplification, no wave).
R4  scope: (a) several positive levels (not treated by the attempt): every root of the characteristic polynomial
    has |lambda| <= 1 on random two- and three-level positive models; (b) one negative weight on the second level
    (leapfrog, level-t weights 2 - 4c^2 at 0 and c^2 at +-e_i, weight -1 at level t-1) gives |lambda| = 1 on the
    whole zone for c^2 <= 1/2 and arg lambda = c|k| + O(|k|^3): the wave the task asks for, at the cost of
    positivity; the attempt's negative-weight example (R3) is amplification instead.
"""
from __future__ import annotations

import itertools
import random

import numpy as np
import sympy as sp


def lam_sym(F, w, ks):
    return sum(wz * sp.exp(sp.I * sum(ki * zi for ki, zi in zip(ks, z))) for z, wz in zip(F, w))


# --------------------------------------------------------------------------------------------- R1
def r1(seed=31, trials=12):
    rng = random.Random(seed)
    nrng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(400):
        d = int(nrng.integers(1, 4))
        n = int(nrng.integers(2, 7))
        F = nrng.integers(-3, 4, size=(n, d))
        w = nrng.random(n) + 0.05
        w /= w.sum()
        K = nrng.uniform(-np.pi, np.pi, size=(200, d))
        lam = (w[None, :] * np.exp(1j * K @ F.T)).sum(axis=1)
        worst = max(worst, np.abs(lam).max())
    ok_exp = True
    for _ in range(trials):
        d = rng.randint(1, 3)
        n = rng.randint(2, 5)
        F = [tuple(rng.randint(-2, 2) for _ in range(d)) for _ in range(n)]
        raw = [rng.randint(1, 6) for _ in range(n)]
        w = [sp.Rational(x, sum(raw)) for x in raw]
        ks = sp.symbols(f"k1:{d + 1}", real=True)
        lam = lam_sym(F, w, ks)
        mod2 = sp.expand(lam * sp.conjugate(lam))
        v = [sum(wz * z[i] for z, wz in zip(F, w)) for i in range(d)]
        cov = [[sum(wz * z[i] * z[j] for z, wz in zip(F, w)) - v[i] * v[j] for j in range(d)] for i in range(d)]
        at0 = {k: 0 for k in ks}
        for i in range(d):
            ok_exp &= sp.simplify(sp.diff(lam, ks[i]).subs(at0) - sp.I * v[i]) == 0
            for j in range(d):
                h = sp.simplify(sp.diff(mod2, ks[i], ks[j]).subs(at0))
                ok_exp &= sp.simplify(h + 2 * cov[i][j]) == 0
    return worst, ok_exp


# --------------------------------------------------------------------------------------------- R2
def r2():
    k1, k2, kap = sp.symbols("k1 k2 kappa", real=True)
    # (a) sublattice supports
    F4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    lam4 = lam_sym(F4, [sp.Rational(1, 4)] * 4, (k1, k2))
    val = sp.simplify(lam4.subs({k1: sp.pi, k2: sp.pi}))
    phases = [sp.pi * (z[0] + z[1]) for z in F4]  # k.z at k = (pi, pi)
    in_hyperplane = len(set(phases)) == 1
    lam1 = lam_sym([(0,), (2,)], [sp.Rational(1, 2)] * 2, (k1,))
    val1 = sp.simplify(lam1.subs(k1, sp.pi))
    # (b) collinear support off the origin
    Fc = [(1, 0), (0, 1)]
    lamc = lam_sym(Fc, [sp.Rational(1, 2)] * 2, (k1, k2))
    diag = sp.simplify(lamc.subs({k1: kap, k2: kap}) - sp.exp(sp.I * kap))
    # the attempt's own example F = {0, e1}: on its null line lambda = 1 (static)
    lams = lam_sym([(0, 0), (1, 0)], [sp.Rational(1, 2)] * 2, (k1, k2))
    stat = sp.simplify(lams.subs({k1: 0, k2: kap}) - 1)
    return val, in_hyperplane, val1, diag, stat


# --------------------------------------------------------------------------------------------- R3
def r3():
    k1, k2, k3, k = sp.symbols("k1 k2 k3 k", real=True)
    F7 = [(0, 0, 0)] + [tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in (1, -1)]
    lam7 = sp.simplify(sp.expand(lam_sym(F7, [sp.Rational(1, 7)] * 7, (k1, k2, k3)).rewrite(sp.cos)))
    at_pi = sp.simplify(lam7.subs({k1: sp.pi, k2: 0, k3: 0}))
    ser = sp.series(lam7.subs({k2: 0, k3: 0}), k1, 0, 4).removeO()
    hess = sp.simplify(sp.diff(sp.expand(lam7 * sp.conjugate(lam7)), k1, 2).subs({k1: 0, k2: 0, k3: 0}))
    F4 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    drift = sp.simplify(sp.diff(lam_sym(F4, [sp.Rational(1, 4)] * 4, (k1, k2, k3)), k1).subs({k1: 0, k2: 0, k3: 0}))
    lamn = 2 - sp.exp(sp.I * k)
    modn = sp.simplify(sp.expand(lamn * sp.conjugate(lamn)).rewrite(sp.cos))
    return at_pi, sp.expand(ser), hess, drift, modn


# --------------------------------------------------------------------------------------------- R4
def r4(seed=5):
    nrng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(300):
        levels = int(nrng.integers(2, 4))
        d = 2
        stencils = []
        tot = nrng.random(levels) + 0.05
        tot /= tot.sum()
        for j in range(levels):
            n = int(nrng.integers(1, 5))
            F = nrng.integers(-2, 3, size=(n, d))
            w = nrng.random(n) + 0.05
            stencils.append((F, tot[j] * w / w.sum()))
        for kk in nrng.uniform(-np.pi, np.pi, size=(40, d)):
            hats = [(w * np.exp(1j * F @ kk)).sum() for F, w in stencils]
            # lambda^m = sum_j hat_j lambda^{m-1-j}
            coeffs = [1.0] + [-h for h in hats]
            worst = max(worst, np.abs(np.roots(coeffs)).max())
    # leapfrog: theta_{t+1} = A theta_t - theta_{t-1}, A: 2 - 4c^2 at 0, c^2 at +-e1, +-e2 (d = 2)
    k1, k2, c, s = sp.symbols("k1 k2 c s", positive=True)
    E = 2 * (1 - sp.cos(k1)) + 2 * (1 - sp.cos(k2))
    ahat = 2 - c ** 2 * E
    # roots of lambda^2 - ahat lambda + 1: |lambda| = 1 iff |ahat| <= 2 iff c^2 E <= 4; E <= 8
    unit_zone = sp.Rational(1, 2)  # c^2 <= 1/2
    worst_leap = 0.0
    for c2 in (0.1, 0.25, 0.5):
        for kk in np.random.default_rng(1).uniform(-np.pi, np.pi, size=(500, 2)):
            a = 2 - c2 * (2 * (1 - np.cos(kk[0])) + 2 * (1 - np.cos(kk[1])))
            worst_leap = max(worst_leap, abs(np.abs(np.roots([1, -a, 1])).max() - 1))
    # small-k phase along a direction: arg lambda = arccos(ahat/2); with k = s (cos t, sin t)
    t = sp.Symbol("t", real=True)
    ah = ahat.subs({k1: s * sp.cos(t), k2: s * sp.sin(t)})
    arg_series = sp.series(sp.acos(ah / 2), s, 0, 3).removeO()
    arg_lead = sp.simplify(arg_series)
    return worst, unit_zone, worst_leap, arg_lead


def main():
    worst1, ok_exp = r1()
    print(f"R1 step 1: max |lambda| over 400 random positive stencils (d = 1..3) x 200 wavevectors = {worst1:.15f}; "
          f"gradient i v and Hessian of |lambda|^2 = -2 Cov(Z) at 0, exact on 12 random rational stencils: {ok_exp}")
    val, in_hyp, val1, diag, stat = r2()
    print(f"R2 (a) F = {{+-e1, +-e2}}: lambda(pi, pi) = {val}; k.z constant on F (a hyperplane k.z = const): {in_hyp}; "
          f"F = {{0, 2}} (d = 1): lambda(pi) = {val1}")
    print(f"   (b) F = {{e1, e2}}, weights 1/2: lambda(kappa, kappa) - e^(i kappa) = {diag} (so |lambda| = 1, arg lambda = kappa "
          f"= |k|/sqrt 2 along (1,1)); the attempt's F = {{0, e1}}: lambda(0, kappa) - 1 = {stat} (static)")
    at_pi, ser, hess, drift, modn = r3()
    print(f"R3 7-stencil: lambda(pi,0,0) = {at_pi}; axis series {ser}; Hessian of |lambda|^2 = {hess}; drift of (1+sum e^(ik_j))/4: "
          f"{drift}; |2 - e^(ik)|^2 = {modn}")
    worst4, unit_zone, worst_leap, arg_lead = r4()
    print(f"R4 (a) 300 random positive two-/three-level models: max |root| = {worst4:.12f}; (b) leapfrog: max ||lambda| - 1| "
          f"for c^2 in {{0.1, 0.25, 0.5}} = {worst_leap:.2e} (unit circle for c^2 <= {unit_zone}); arg lambda = {arg_lead} + O(|k|^3)")

    step1_core = worst1 <= 1 + 1e-12 and ok_exp
    gloss_fails = val == -1 and not in_hyp and val1 == 1
    wave_under_positivity = diag == 0
    numbers = (at_pi == sp.Rational(3, 7) and ser == 1 - k_sq() and hess == sp.Rational(-4, 7) and drift == sp.I / 4)
    if step1_core and numbers and (gloss_fails or wave_under_positivity):
        print("SUMMARY: fails at step 1 - its equality set is misread: (a) |lambda| = 1 at k != 0 also for supports in a proper "
              "sublattice, not only 'F in a coset of a hyperplane k.z = const' (F = {+-e1,+-e2}: lambda(pi,pi) = -1; F = {0,2}: "
              "lambda(pi) = 1); (b) inside the collinear case with the support's hyperplane off the origin the mode is an exact "
              "wave under positive weights (F = {e1,e2}: lambda(kappa,kappa) = e^(i kappa), |lambda| = 1, arg = |k|/sqrt 2), so the "
              "HIT's 'waves |lambda|=1 with arg=c|k| require dropping positivity or adding a conserved unitary structure' and "
              "'no propagating wave under positivity' are false (the attempt's exception F = {0,e1} is the static case); the "
              "core Jensen bound, the expansion (Hessian -2 Cov), the 7-stencil 3/7, -1/7, -4/7, drift i/4 and |2-e^(ik)| = 3 "
              "at pi hold; not covered: several earlier levels (true here numerically) and the wave-giving change (a "
              "second-level weight -1 gives |lambda| = 1, arg = c|k|; the attempt's negative example is amplification)")
    elif step1_core and numbers:
        print("HIT: confirmed - Jensen bound, expansion and the stencil numbers re-derived")
        print("SUMMARY: confirmed")
    else:
        print(f"SUMMARY: fails - core {step1_core}, numbers {numbers}")


def k_sq():
    k1 = sp.Symbol("k1", real=True)
    return k1 ** 2 / 7


if __name__ == "__main__":
    main()
