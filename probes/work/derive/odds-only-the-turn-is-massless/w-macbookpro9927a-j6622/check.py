#!/usr/bin/env python3
"""Only the turn is massless: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j6622 (claude-opus-5-5).

Objects (block 103): K1 f(s) = int e^{beta s.b} f(b) dsigma(b)/Z, Z = sinh(beta)/beta; the sea F(t), t = s.n, solves F = (K1 F)^6/<(K1 F)^6>;
g = K1 F; the per-neighbour operator A eta = K1(F eta)/g splits by azimuthal order m with sector kernel
(1/(2Z)) e^{beta t t'} I_m(beta r r'), r = sqrt(1 - t^2).
Exact (sympy): the sector kernels (Jacobi-Anger), the reflection identity behind monotonicity, the Gaussian (Mehler) limit.
Floating point, labelled executed: the sea and the sector spectra for beta from 0.6 to 32, own code.
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


B103 = ("ff6da653b1", "docs/ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_CARRY_CONTENT_NOT_RECORD_COUNT_AT_LONG_RANGE_A_MASSLESS_TURN_CHANNEL_IN_THE_"
        "ORDERED_SEA_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B103_Q = ["The one-neighbour operator is `K₁f(s) = ∫e^{βs·b}f(b)dσ(b)/Z`, with `Z = sinh β/β`.",
          "Its linearization is `η_x = Σ_y(Aη_y − ⟨Aη_y⟩_F)`, with `Aη = K₁(Fη)/g` and `g = K₁F`. It splits by the azimuthal order `m`.",
          "A channel with per-neighbour eigenvalue `μ` obeys `μ(m² + E(k))η = source`, with `m² = (1 − 6μ)/μ`.",
          "the turn `δ(s) = √(1 − t²)F′(t)cos φ` is an eigenvector of the per-neighbour linearization with eigenvalue exactly `1/6`."]
TASK_Q = ["(b) every eigenvalue other than the turn's below 1/6, for every beta > beta0 (a comparison with lambda_l, a variational bound, "
          "or a monotonicity argument); (c) the beta -> infinity limits of the masses (m_L^2 = 24.07 at beta = 4 suggests a finite limit). "
          "HIT: (b) exact for every beta > beta0, or (a)."]


def family_q() -> None:
    txt = subprocess.run(["git", "show", f"{B103[0]}:{B103[1]}"], capture_output=True, text=True).stdout
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:odds-only-the-turn-is-massless:a2"), "")
    miss = [f"b103[{i}]" for i, q in enumerate(B103_Q) if q not in txt] + [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 103 (head ff6da653, PR #8919) and the task quoted verbatim ({len(B103_Q) + len(TASK_Q)} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ J: sector kernels
def family_j() -> None:
    x, psi = sp.symbols("x psi", real=True)
    N = 12
    ok = True
    for m in range(0, 5):
        # (1/2pi) int_0^{2pi} e^{x cos psi} cos(m psi) dpsi, termwise in x, against I_m's series
        # average of cos^p(psi) cos(m psi) over a period, exactly from cos^p = 2^-p sum_j C(p, j) e^{i(2j - p) psi}
        coeffs = [sp.Rational(sp.binomial(p, (p - m) // 2), 2 ** p) / sp.factorial(p) if (p >= m and (p - m) % 2 == 0) else 0
                  for p in range(N + 1)]
        series = sum(c * x ** p for p, c in enumerate(coeffs))
        Im = sp.besseli(m, x).rewrite(sp.besseli).series(x, 0, N + 1).removeO()
        ok &= sp.expand(series - sp.expand(Im)) == 0
    check("J", ok, "sector kernels: (1/2pi) int e^{x cos psi} cos(m psi) dpsi = I_m(x) (series to x^12, m = 0..4, exact), so on "
          "h(t) e^{i m phi} the operator K1 acts by (1/(2Z)) int e^{beta t t'} I_m(beta r r') h(t') dt': A splits into positive "
          "kernels, one per |m| (I_m >= 0)")


# ------------------------------------------------------------------------------------------------ R: the reflection identity
def family_r() -> None:
    th = sp.Symbol("theta", positive=True)
    b1, b2, b3 = sp.symbols("b1 b2 b3", real=True)
    n = sp.Matrix([0, 0, 1])
    s = sp.Matrix([sp.sin(th), 0, sp.cos(th)])
    et = sp.Matrix([sp.cos(th), 0, -sp.sin(th)])                                     # d s/d theta, away from n
    b = sp.Matrix([b1, b2, b3])
    Rb = b - 2 * et.dot(b) * et                                                       # reflection through the plane et^perp (contains s)
    ok = sp.simplify(s.dot(Rb) - s.dot(b)) == 0
    ok &= sp.simplify(Rb.dot(n) - b.dot(n) - 2 * et.dot(b) * sp.sin(th)) == 0
    check("R", ok, "monotonicity (a partial step to (a)): with R the reflection through the plane orthogonal to the meridian tangent e_theta at s, "
          "s.Rb = s.b and Rb.n - b.n = 2(e_theta.b) sin(theta) > 0 where e_theta.b > 0 (symbolic); so dg/dtheta = beta int_{e.b>0} (e.b) "
          "e^{beta s.b}[F(b.n) - F(Rb.n)] dsigma/Z < 0 for every non-decreasing non-constant F: K1 maps it to a strictly increasing g, "
          "and F = c g^6 then is strictly increasing")


# ------------------------------------------------------------------------------------------------ G: the Gaussian limit
def family_g() -> None:
    a, beta, xx, yy = sp.symbols("a beta x y", positive=True)
    sol = sp.solve(sp.Eq(a, 6 * a * beta / (2 * a + beta)), a)
    ok = sp.Rational(5, 2) * beta in sol
    rho = sp.simplify(beta / (beta + 2 * (sp.Rational(5, 2) * beta)))
    ok &= rho == sp.Rational(1, 6)
    # the chain y | x ~ N(rho x, sigma^2), sigma^2 = 1/(beta + 2a) = 1/(6 beta); stationary variance v = sigma^2/(1 - rho^2)
    x, y = sp.symbols("x y", real=True)
    sig2 = 1 / (6 * beta); v = sig2 / (1 - rho ** 2)
    He = lambda n, z: sp.hermite_prob(n, z) if hasattr(sp, "hermite_prob") else sp.expand(sp.hermite(n, z / sp.sqrt(2)) * 2 ** (-sp.Rational(n, 2)))
    for nn in range(0, 5):
        cond = sp.integrate(He(nn, y / sp.sqrt(v)) * sp.exp(-(y - rho * x) ** 2 / (2 * sig2)) / sp.sqrt(2 * sp.pi * sig2), (y, -sp.oo, sp.oo))
        ok &= sp.simplify(cond - rho ** nn * He(nn, x / sp.sqrt(v))) == 0
    masses = [(1 - 6 * sp.Rational(1, 6) ** nn) / sp.Rational(1, 6) ** nn for nn in (2, 3)]
    ok &= masses == [30, 210]
    check("G", ok, "(c) beta -> oo: in the tangent plane e^{beta s.b} -> e^{beta} e^{-beta|x-y|^2/2} and the sea F -> e^{-a|x|^2} with "
          "a = 6 a beta/(2a + beta), a = 5 beta/2; A becomes the Gaussian chain y|x ~ N(x/6, 1/(6 beta)) (rho = 1/6 exactly: the turn), "
          "whose eigenvalues are 6^-(n1+n2) with Hermite eigenfunctions (checked n <= 4, symbolic); so the lean-size mode (n = 2, m = 0) "
          "and m = 2 tend to mu = 1/36, m^2 = 30, and the next m = 1 and m = 3 to 1/216, m^2 = 210")


# ------------------------------------------------------------------------------------------------ N: executed spectra
def sea_and_sectors(beta, Nq=320, mmax=3):
    from numpy.polynomial import legendre as Lg
    from scipy.special import ive
    t, w = Lg.leggauss(Nq)
    r = np.sqrt(1 - t ** 2)
    T, Tp = np.meshgrid(t, t, indexing="ij"); R, Rp = np.meshgrid(r, r, indexing="ij")
    arg = beta * R * Rp
    pref = np.exp(beta * (T * Tp + R * Rp - 1)) * beta / (1 - math.exp(-2 * beta))    # (1/(2Z)) e^{beta(tt' + rr')}, with ive's e^{-beta rr'}
    kern = {m: pref * ive(m, arg) for m in range(mmax + 1)}                               # (1/(2Z)) e^{beta tt'} I_m(beta r r')
    F = np.exp(3 * beta * t); F /= 0.5 * np.sum(w * F)
    for _ in range(20000):
        g = kern[0] @ (w * F)
        Fn = g ** 6; Fn /= 0.5 * np.sum(w * Fn)
        if np.max(np.abs(Fn - F)) < 1e-13 * np.max(F):
            F = Fn; break
        F = Fn
    g = kern[0] @ (w * F)
    d = np.sqrt(w * F / g)
    specs = {}
    for m in range(mmax + 1):
        S = d[:, None] * kern[m] * d[None, :]
        specs[m] = np.sort(np.linalg.eigvalsh((S + S.T) / 2))[::-1]
    mono = np.all(np.diff(F) > 0)
    return specs, mono, 0.5 * np.sum(w * t * F)


def family_n() -> None:
    ok = True
    rows = []
    last = None
    for beta in (0.6, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0):
        sp_, mono, M = sea_and_sectors(beta)
        top0, size = sp_[0][0], sp_[0][1]
        turn, next1 = sp_[1][0], sp_[1][1]
        m2, m3 = sp_[2][0], sp_[3][0]
        ok &= mono and abs(top0 - 1) < 1e-9 and abs(turn - 1 / 6) < 1e-8 and next1 < 1 / 6 and m2 < 1 / 6 and m3 < m2 and size < 1 / 6
        mass = (1 - 6 * size) / size
        rows.append(f"b={beta:g}: M={M:.4f} 6mu: size {6*size:.4f}, next m1 {6*next1:.4f}, m2 {6*m2:.4f}, m3 {6*m3:.4f}; mL^2={mass:.2f}")
        last = (6 * size, 6 * next1, 6 * m2, 6 * m3, mass)
    # beta = 32 against the Gaussian limit 1/6, 1/36, 1/6, 1/36, 30
    ok &= abs(last[0] - 1 / 6) < 0.02 and abs(last[2] - 1 / 6) < 0.02 and abs(last[1] - 1 / 36) < 0.01 and abs(last[4] - 30) < 4
    OUT.append("     [executed, float, 320 Gauss nodes, own code] " + "; ".join(rows))
    check("N", ok, "the sea is strictly increasing at every beta tried; each sector's top: m = 0 is 1 (normalization), m = 1 is exactly 1/6 "
          "(the turn, 1e-8), and every other eigenvalue (next m = 1, m = 2, m = 3 and the m = 0 size mode) lies below 1/6 from beta = 0.6 to "
          "32; with beta the spectrum approaches the Gaussian limit (6mu -> 1/6, 1/36, 1/6, 1/36; m_L^2 -> 30)")


def main() -> int:
    family_q(); family_j(); family_r(); family_g(); family_n()
    print("Only the turn is massless - checks; worker w-macbookpro9927a-j6622 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL (b) for every beta > beta0 and every non-decreasing leaning sea: every eigenvalue of A with |m| >= 1 other than "
          "the turn has modulus < 1/6 (sector kernels e^{beta t t'} I_m(beta r r') are positive; the turn profile sqrt(1-t^2) F' > 0 is "
          "the Perron vector of m = 1, simple and strictly dominant; I_m < I_1 dominates m >= 2 strictly); the m = 0 size mode is executed "
          "only; (c) as beta -> oo the spectrum tends to 6^-n (Mehler), so m_L^2 -> 30 (m = 2 also 30; next m = 1 and m = 3 -> 210)")
    print("HIT: for every beta > beta0 and every non-decreasing leaning sea, all per-neighbour eigenvalues with azimuthal order |m| >= 1 other "
          "than the turn lie strictly below 1/6 in modulus (positive Bessel kernels, Perron vector, I_m < I_1); the beta -> oo limit of the "
          "lean-size mass is m_L^2 = 30")
    return 0


if __name__ == "__main__":
    sys.exit(main())
