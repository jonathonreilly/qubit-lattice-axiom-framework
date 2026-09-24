#!/usr/bin/env python3
"""Waves of possibility's lean with precession: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-jb8c1 (claude-opus-5-5).

Model (task): d pi_x/dt = -Gamma (pi_x - Phi(pi)_x) + Omega L_(h_x) pi_x, Phi(pi)_x = prod_y (K1 pi_y)/<prod_y (K1 pi_y)> (block 42/103),
K1 f(s) = int e^{beta s.b} f(b) dsigma(b)/Z (block 103), h_x the unit lean of Phi(pi)_x, L_h f(s) = (h x s).grad f(s).
Exact (sympy): fixed points, the turn algebra and its dispersion, the staggered sea's turn, the sublattice flip.
Floating point, labelled executed: the full m = 1 linearization on 60 associated-Legendre profiles, uniform (beta = 1) and staggered (beta = -1).
"""
from __future__ import annotations

import json
import math
import subprocess
import sys

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources, verbatim
B103 = ("ff6da653b1", "docs/ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_CARRY_CONTENT_NOT_RECORD_COUNT_AT_LONG_RANGE_A_MASSLESS_TURN_CHANNEL_IN_THE_"
        "ORDERED_SEA_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B103_Q = ["The one-neighbour operator is `K₁f(s) = ∫e^{βs·b}f(b)dσ(b)/Z`, with `Z = sinh β/β`.",
          "It is a uniform solution `F(s·n)` of `F = (K₁F)⁶/⟨(K₁F)⁶⟩`, with lean `M = ⟨s·n⟩_F` along a unit vector `n`.",
          "The lean (`ℓ = 1`) loses its mass term at exactly one `β₀`, strictly between `5085/10000` and `5086/10000` (`β₀ = 0.508558…`).",
          "the turn `δ(s) = √(1 − t²)F′(t)cos φ` is an eigenvector of the per-neighbour linearization with eigenvalue exactly `1/6`."]
TASK_Q = ["d pi_x/dt = -Gamma (pi_x - Phi(pi)_x) + Omega L_(h_x) pi_x, with Phi block 42's self-consistent map, h_x the unit direction of "
          "the lean of Phi(pi)_x and L_h the generator of rotations of contents about h.",
          "the expectation to test is omega = (+-Omega - i Gamma) E(k)/6, waves with omega ~ k^2",
          "is the dispersion linear at small k, omega ~ c|k|, and what is c in units of Omega?"]


def family_q() -> None:
    txt = subprocess.run(["git", "show", f"{B103[0]}:{B103[1]}"], capture_output=True, text=True).stdout
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:odds-turn-with-precession:a2"), "")
    miss = [f"b103[{i}]" for i, q in enumerate(B103_Q) if q not in txt] + [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 103 (head ff6da653, PR #8919) and the task quoted verbatim ({len(B103_Q) + len(TASK_Q)} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ A: fixed points and the turn algebra
def cross(a, b):
    return sp.Matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])


def family_a() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    s = sp.Matrix([x, y, z])
    Ff = sp.Lambda(sp.Symbol('q'), sp.exp(2 * sp.Symbol('q')) + sp.Symbol('q') ** 3)   # a concrete non-trivial profile
    n = sp.Matrix([0, 0, 1])
    grad = lambda f: sp.Matrix([sp.diff(f, v) for v in (x, y, z)])
    Lh = lambda h, f: (cross(h, s).T * grad(f))[0]
    ok = sp.simplify(Lh(n, Ff(s.dot(n)))) == 0                                     # (a) an axially symmetric sea does not precess
    ok &= sp.simplify(Lh(-n, Ff(-s.dot(n)))) == 0                                  # nor does the staggered sublattice leaning -n
    # linear order: pi = F(s.m), m = n + tau, h = n + taubar (tau, taubar transverse, first order)
    e = sp.Symbol("e")
    t1, t2, u1, u2 = sp.symbols("tau1 tau2 taubar1 taubar2", real=True)
    tau = sp.Matrix([t1, t2, 0]); tb = sp.Matrix([u1, u2, 0])
    m = n + e * tau; h = n + e * tb
    val = Lh(h, Ff(s.dot(m)))
    first = sp.diff(val, e).subs(e, 0)
    want = (2 * sp.exp(2 * z) + 3 * z ** 2) * (s.T * cross(n, tb - tau))[0]
    ok &= sp.simplify(first - want) == 0                                            # L_h pi = F'(t) s.(n x (taubar - tau)): a tilt
    # the tilt dynamics tau' = -(Gamma + Omega n x)(tau - taubar); per wave k: taubar = (1 - E/6) tau
    G, W, E = sp.symbols("Gamma Omega E", positive=True)
    nx = sp.Matrix([[0, -1], [1, 0]])                                                # n x on the transverse plane
    Mk = -(G * sp.eye(2) + W * nx) * (E / 6)
    ev = list(Mk.eigenvals().keys())
    ok &= all(any(sp.simplify(v - w) == 0 for v in ev) for w in (-(G + sp.I * W) * E / 6, -(G - sp.I * W) * E / 6))
    check("A", ok, "(a) the ordered sea F(s.n) and the staggered sea (F on one sublattice, F(-s.n) on the other) are fixed points for every "
          "Omega: L_n F(s.n) = 0 (symbolic); (b) at first order a tilted site precesses about its target's lean by L_h F(s.m) = "
          "F'(t) s.(n x (taubar - tau)), again a tilt; so tau' = -(Gamma + Omega n x)(tau - taubar), and per wave k (taubar = (1 - E/6) tau) "
          "the eigenvalues are -(Gamma -+ i Omega) E/6: omega = (+-Omega - i Gamma) E(k)/6")


def family_c() -> None:
    G, W = sp.symbols("Gamma Omega", positive=True); g, lam = sp.symbols("gamma lambda")
    a = -(G - sp.I * W); b = -(G + sp.I * W)                                        # circular component: n x -> -i
    M = sp.Matrix([[a, a * g], [b * g, b]])                                         # tau_A' = a(tau_A + gamma tau_B), tau_B' = b(tau_B + gamma tau_A)
    cp = sp.expand((M - lam * sp.eye(2)).det())
    ok = sp.simplify(cp - (lam ** 2 + 2 * G * lam + (G ** 2 + W ** 2) * (1 - g ** 2))) == 0
    k = sp.Symbol("k", positive=True)
    gam = (2 + sp.cos(k)) / 3                                                        # gamma along an axis
    s = sp.series(sp.sqrt(1 - gam ** 2), k, 0, 3).removeO()
    ok &= sp.simplify(s - k / sp.sqrt(3)) == 0                                       # sqrt(1 - gamma^2) = |k|/sqrt(3) + O(k^3)
    roots = sp.solve(cp.subs(G, 0), lam)
    ok &= len(roots) == 2 and all(sp.simplify(r ** 2 + W ** 2 * (1 - g ** 2)) == 0 for r in roots) and sp.simplify(roots[0] + roots[1]) == 0
    slow = sp.series(-G + sp.sqrt(G ** 2 - (G ** 2 + W ** 2) * sp.Symbol("x")), sp.Symbol("x"), 0, 2).removeO()
    ok &= sp.simplify(slow + (G ** 2 + W ** 2) * sp.Symbol("x") / (2 * G)) == 0
    check("C", ok, "(c) staggered turn: tau_A' = -(Gamma + Omega n x)(tau_A + taubar_B), tau_B' = -(Gamma - Omega n x)(tau_B + taubar_A) give "
          "lambda^2 + 2 Gamma lambda + (Gamma^2 + Omega^2)(1 - gamma^2) = 0, gamma = (1/3) sum cos k_j: omega = -i Gamma +- "
          "sqrt((Gamma^2 + Omega^2)(1 - gamma^2) - Gamma^2); at Gamma = 0 omega = +-Omega sqrt(1 - gamma^2) = +-Omega |k|/sqrt(3) + O(k^3); "
          "for Gamma > 0 the small-k branch is overdamped, lambda = -(Gamma^2 + Omega^2)(1 - gamma^2)/(2 Gamma) + ...")


def family_d() -> None:
    t, beta = sp.symbols("t beta", real=True)
    ok = True
    for l in range(0, 6):
        lam = lambda bb: sp.integrate(sp.exp(bb * t) * sp.legendre(l, t), (t, -1, 1)) / 2 / (sp.sinh(bb) / bb)
        ok &= sp.simplify(lam(-beta) - (-1) ** l * lam(beta)) == 0
        ok &= sp.expand(sp.legendre(l, -t) - (-1) ** l * sp.legendre(l, t)) == 0
    check("D", ok, "(c) the flip: lambda_l(-beta) = (-1)^l lambda_l(beta) (l <= 5, symbolic) and P_l(-t) = (-1)^l P_l(t), so K1 at -|beta| "
          "on f(-s) is K1 at |beta| on f, evaluated at -s: the staggered equations at beta < 0 are the uniform ones at |beta|; the staggered "
          "sea exists iff -beta > beta0 (block 103 T1, 0.5085 < beta0 < 0.5086), with the same F")


# ------------------------------------------------------------------------------------------------ N: executed, the full distribution
def family_n() -> None:
    from numpy.polynomial import legendre as Lg
    Nq, Lmax = 120, 60
    tq, wq = Lg.leggauss(Nq)
    def Pl(l, t):
        c = np.zeros(l + 1); c[l] = 1
        return Lg.legval(t, c)
    def dPl(l, t):
        c = np.zeros(l + 1); c[l] = 1
        return Lg.legval(t, Lg.legder(c))
    def lams(beta):
        tt, ww = Lg.leggauss(400)
        Z = math.sinh(beta) / beta
        return np.array([0.5 * np.sum(ww * np.exp(beta * tt) * Pl(l, tt)) / Z for l in range(Lmax + 2)])
    B0 = np.array([Pl(l, tq) for l in range(Lmax + 1)])                            # Legendre on nodes
    B0n = B0 * np.sqrt((2 * np.arange(Lmax + 1) + 1) / 2)[:, None]
    B1 = np.array([np.sqrt(1 - tq ** 2) * dPl(l, tq) for l in range(1, Lmax + 1)])  # order-one functions (sign irrelevant)
    B1n = B1 / np.sqrt(np.sum(wq * B1 ** 2, axis=1))[:, None]
    def K0(f, lm):   # K1 on axially symmetric f
        return B0n.T @ (lm[:Lmax + 1] * (B0n @ (wq * f)))
    def K1m1(f, lm):  # K1 on m = 1 profiles f(t) e^{i phi}
        return B1n.T @ (lm[1:Lmax + 1] * (B1n @ (wq * f)))
    beta = 1.0
    lm = lams(beta)
    F = 1 + 0.9 * tq
    for _ in range(3000):
        g0 = K0(F, lm)
        Fn = g0 ** 6 / (0.5 * np.sum(wq * g0 ** 6))
        if np.max(np.abs(Fn - F)) < 1e-15:
            break
        F = Fn
    g0 = K0(F, lm)
    M0 = 0.5 * np.sum(wq * tq * F)
    # F'(t) from its Legendre series
    cF = np.linalg.lstsq(np.array([Pl(l, tq) for l in range(Lmax + 1)]).T, F, rcond=None)[0]
    Fp = Lg.legval(tq, Lg.legder(cF))
    tilt = Fp * np.sqrt(1 - tq ** 2)
    lean = lambda G_: np.sum(wq * np.sqrt(1 - tq ** 2) * G_) / (4 * M0)             # circular lean change of a profile G e^{i phi}
    # per-neighbour linearization on the tilt: F K1(tilt)/g0 = tilt/6
    one6 = np.max(np.abs(F * K1m1(tilt, lm) / g0 - tilt / 6))
    # full m = 1 operator at wave vector k (uniform sea): g -> -Gamma(g - DPhi g) + Omega(i g - i eps[DPhi g] tilt)
    Bm = B1n.T                                                                       # nodal values of the basis
    proj = lambda f: B1n @ (wq * f)                                                  # coefficients
    rows, ok = [], one6 < 1e-10
    for Gm, Om in ((1.0, 2.0), (1.0, 0.5)):
        for kvec in ((0.7, 0.0, 0.0), (0.4, 1.1, -0.3)):
            gam = sum(math.cos(c) for c in kvec) / 3; Ek = 6 * (1 - gam)
            A = np.zeros((Lmax, Lmax), complex)
            for j in range(Lmax):
                gj = Bm[:, j]
                DG = 6 * gam * F * K1m1(gj, lm) / g0
                out = -Gm * (gj - DG) + Om * (1j * gj - 1j * lean(DG) * tilt)
                A[:, j] = proj(out)
            ev = np.linalg.eigvals(A)
            want = -(Gm - 1j * Om) * Ek / 6
            dmin = np.min(np.abs(ev - want))
            others = [v for v in ev if abs(v - want) > 1e-6]
            slowest = max(v.real for v in others)
            ok &= dmin < 1e-9 and slowest < want.real - 1e-3
            rows.append(f"G={Gm:g},O={Om:g},k={kvec}: |lambda - (-(G - iO)E/6)| = {dmin:.0e}, next Re {slowest:.3f} vs {want.real:.4f}")
    # staggered sea, beta = -1: A leans n (F), B leans -n (F(-t)); K1 at beta = -1 has (-1)^l lambda_l(1)
    lmn = np.array([(-1) ** l * lm[l] for l in range(Lmax + 2)])
    FB = Lg.legval(-tq, cF)
    FBp = Lg.legval(-tq, Lg.legder(cF))                                              # F'(-t)
    gA0 = K0(FB, lmn)                                                                # K1 of the B sea, seen by A: equals g0(t)
    gB0 = K0(F, lmn)                                                                 # K1 of the A sea, seen by B: equals g0(-t)
    same = max(np.max(np.abs(gA0 - g0)), np.max(np.abs(gB0 - Lg.legval(-tq, np.linalg.lstsq(np.array([Pl(l, tq) for l in range(Lmax + 1)]).T, g0, rcond=None)[0]))))
    tiltB = FBp * np.sqrt(1 - tq ** 2)
    for Gm, Om in ((1.0, 2.0), (0.05, 1.0)):
        for kvec in ((0.3, 0.0, 0.0), (0.9, 0.4, 0.2)):
            gam = sum(math.cos(c) for c in kvec) / 3
            A = np.zeros((2 * Lmax, 2 * Lmax), complex)
            for j in range(2 * Lmax):
                gA = Bm[:, j] if j < Lmax else np.zeros(Nq); gB = Bm[:, j - Lmax] if j >= Lmax else np.zeros(Nq)
                DA = 6 * gam * F * K1m1(gB, lmn) / gA0
                DB = 6 * gam * FB * K1m1(gA, lmn) / gB0
                oA = -Gm * (gA - DA) + Om * (1j * gA - 1j * lean(DA) * tilt)
                oB = -Gm * (gB - DB) + Om * (-1j * gB + 1j * lean(DB) * tiltB)
                A[:, j] = np.concatenate([proj(oA), proj(oB)])
            ev = np.linalg.eigvals(A)
            disc = complex((Gm ** 2 + Om ** 2) * (1 - gam ** 2) - Gm ** 2)
            wants = [-Gm + 1j * np.sqrt(disc), -Gm - 1j * np.sqrt(disc)]
            dmin = max(np.min(np.abs(ev - w)) for w in wants)
            others = [v for v in ev if min(abs(v - w) for w in wants) > 1e-6]
            slowest = max(v.real for v in others)
            ok &= dmin < 1e-9
            rows.append(f"stag G={Gm:g},O={Om:g},k={kvec}: max |lambda - root| = {dmin:.0e}, roots Re {max(w.real for w in wants):.3f}, others Re <= {slowest:.3f}")
    ok &= same < 1e-10
    OUT.append("     [executed, float] beta = 1 sea (M = %.6f), per-neighbour tilt eigenvalue 1/6 to %.0e; " % (M0, one6) + "; ".join(rows))
    check("N", ok, "the full m = 1 linearization (60 order-one profiles, 120 Gauss nodes) has the predicted turn eigenvalues to 1e-9 as exact "
          "eigenvalues for the uniform sea at beta = 1 (every other eigenvalue more damped: the turn is the slow, massless branch) and the "
          "staggered sea at beta = -1 (its K1 of the other sublattice equals the uniform g0, as the flip says; there the other modes also "
          "decay at about Gamma, so the turn is set apart by its dispersion, not its damping)")


def main() -> int:
    family_q(); family_a(); family_c(); family_d(); family_n()
    print("Waves of possibility's lean with precession - checks; worker w-macbookpro9927a-jb8c1 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED (a) both seas are fixed points for every Omega; (b) the turns form an invariant subspace of the full linearized "
          "dynamics (rotation covariance gives the per-neighbour 1/6 exactly), so the turn frequencies are exactly omega = (+-Omega - "
          "i Gamma) E(k)/6: precessing, diffusing waves with omega ~ k^2 and a fixed quality Omega/Gamma; (c) the staggered sea exists iff "
          "-beta > beta0 and its turns obey lambda^2 + 2 Gamma lambda + (Gamma^2 + Omega^2)(1 - gamma^2) = 0: linear with c = Omega/sqrt(3) "
          "only at Gamma = 0, overdamped and diffusive at small k for Gamma > 0; (d) no condition on Omega/Gamma")
    print("HIT: with precession about the target's lean the ordered sea's turns are exact eigenmodes with omega = (+-Omega - i Gamma) E(k)/6; "
          "the staggered sea's turns obey lambda^2 + 2 Gamma lambda + (Gamma^2 + Omega^2)(1 - gamma(k)^2) = 0, linear (c = Omega/sqrt(3)) "
          "only without relaxation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
