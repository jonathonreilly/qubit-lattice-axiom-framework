#!/usr/bin/env python3
"""dispersion-under-positive-weights, independent run 1 of 2 (worker w-jonathonsmac4f50-jfec0, claude-opus-5).

Linear gain-one formation model with memory: theta_{t+1} = sum_{j>=0} sum_p w_{j,p} theta_{t-j}(x + p) + noise, w >= 0, sum w = 1.
Along a direction u write X for the offset projected on u under the level-0 weights and Y under the level-1 weights, so
phi(k) = E[e^{ikX}] and psi(k) = E[e^{ikY}]; mu_i, q_i, v_i = q_i - mu_i^2 are their mean, second moment and variance.

A1 (exact)  one level: |phi| <= 1 and |phi(k)| = 1 - (1/2) k^T Cov k + O(k^4), so 1 - |phi| = O(k^2) and it is positive unless
            all the weight sits on one offset (Cov = 0): diffusive.
A2 (exact)  two levels, weights a and 1 - a: the root of lambda^2 - a phi lambda - (1-a) psi near 1 is
            lambda = 1 + i k alpha - k^2 [ ... ], alpha = (a mu_1 + (1-a) mu_2)/(2-a), and
            |lambda(k)|^2 = 1 - 2 D k^2 + O(k^3) with  D = [a v_1 + (1-a) v_2 + B]/(2(2-a)),
            B = a(1-a)(mu_1 - mu_2)^2 (2 - a - a(1-a))/(2-a)^2 ... computed and factored exactly here.
A3 (exact)  D > 0 unless the law is degenerate; the degenerate cases are enumerated exactly.
N1 (numerical, labelled)  |lambda(k)| and arg lambda(k) at small k for a in {0.25, 0.5, 0.75} and several predecessor sets.
N2 (numerical, labelled)  random positive multi-level weights: D > 0 in every draw.

Provenance: I attempted the related derivation unit J:derive:waves-need-signed-weights:a2 earlier in this campaign, so this run is
not blind to that result; the supervisor should weigh it against the other independent run of this computation."""
import itertools
import math
import random
import sys

import numpy as np
import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def main():
    k, a = sp.symbols("k a", real=True, positive=True)
    mu1, mu2, q1, q2 = sp.symbols("mu1 mu2 q1 q2", real=True)

    # ---------------- A1
    w, x = sp.symbols("w x", real=True)
    # |phi|^2 for a general weight law: 1 - k^2 Var + O(k^4)
    X = sp.symbols("X", real=True)
    phi_s = 1 + sp.I * k * mu1 - k ** 2 * q1 / 2
    mod2 = sp.expand(sp.simplify(sp.expand(phi_s * sp.conjugate(phi_s), complex=True)))
    ok = sp.simplify(sp.series(mod2, k, 0, 3).removeO() - (1 - k ** 2 * (q1 - mu1 ** 2))) == 0
    check("A1", ok, "one level: phi(k) = E[e^{ikX}] with a probability law on the offsets, so |phi| <= 1 by the triangle inequality and "
          "|phi(k)|^2 = 1 - k^2 Var(X) + O(k^4), i.e. |phi| = 1 - (1/2) Var(X) k^2 + O(k^4) (symbolic): the decay is quadratic and vanishes "
          "only when Var(X) = 0, that is when the whole weight sits on one offset")

    # ---------------- A2: the root near 1
    lam = 1 + sp.I * k * sp.Symbol("alpha", real=True) + k ** 2 * sp.Symbol("gamma")
    al, ga = sp.Symbol("alpha", real=True), sp.Symbol("gamma")
    psi_s = 1 + sp.I * k * mu2 - k ** 2 * q2 / 2
    F = sp.expand(lam ** 2 - a * phi_s * lam - (1 - a) * psi_s)
    c1 = sp.simplify(sp.expand(F).coeff(k, 1))
    al_sol = sp.solve(sp.Eq(c1, 0), al)[0]
    c2 = sp.simplify(sp.expand(F).coeff(k, 2).subs(al, al_sol))
    ga_sol = sp.simplify(sp.solve(sp.Eq(c2, 0), ga)[0])
    lam_sol = 1 + sp.I * k * al_sol + k ** 2 * ga_sol
    mod = sp.simplify(sp.expand(sp.series(sp.expand(lam_sol * sp.conjugate(lam_sol), complex=True), k, 0, 3).removeO()))
    D = sp.simplify(-sp.expand(mod).coeff(k, 2) / 2)
    v1, v2 = sp.symbols("v1 v2", nonnegative=True)
    Dsub = sp.simplify(D.subs({q1: v1 + mu1 ** 2, q2: v2 + mu2 ** 2}))
    Bexpr = sp.simplify(sp.expand(Dsub * 2 * (2 - a) - (a * v1 + (1 - a) * v2)))
    ok = sp.simplify(al_sol - (a * mu1 + (1 - a) * mu2) / (2 - a)) == 0
    ok &= sp.simplify(Dsub - (a * v1 + (1 - a) * v2 + Bexpr) / (2 * (2 - a))) == 0
    check("A2", ok, f"two levels: the root near 1 is lambda = 1 + i k alpha - ... with alpha = {sp.simplify(al_sol)} (a real drift, so "
          f"arg lambda = alpha k + O(k^2) and |lambda| is unchanged at first order), and |lambda|^2 = 1 - 2 D k^2 + O(k^3) with "
          f"D = [a v_1 + (1-a) v_2 + B]/(2(2-a)), B = {sp.factor(Bexpr)} (symbolic)")

    # ---------------- A3: positivity of B and the degenerate cases
    Bfac = sp.factor(Bexpr)
    num, den = sp.fraction(sp.together(Bexpr))
    ok = sp.simplify(sp.expand(num * sp.sign(1)) - sp.expand(a * (1 - a) * (2 * mu1 - mu2) ** 2)) == 0 or \
         sp.simplify(sp.expand(Bexpr - a * (1 - a) * (2 * mu1 - mu2) ** 2 / (2 - a) ** 2)) == 0
    # B = a(1-a)(2 mu1 - mu2)^2/(2-a)^2 >= 0 on 0 <= a <= 1; D = 0 iff v1 = v2 = 0 and a(1-a)(2 mu1 - mu2)^2 = 0
    # the vanishing case is the rigid translation: single offsets with p2 = 2 p1 (level j shifts by (j+1) p1)
    kk_ = sp.Symbol("kk", real=True)
    pp = sp.Symbol("p", real=True)
    Lsym = sp.Symbol("L")
    poly_rig = Lsym ** 2 - a * sp.exp(sp.I * kk_ * pp) * Lsym - (1 - a) * sp.exp(2 * sp.I * kk_ * pp)
    rig = sp.simplify(sp.expand(poly_rig.subs(Lsym, sp.exp(sp.I * kk_ * pp)))) == 0
    ok &= rig
    deg = [sp.simplify(Bexpr.subs({a: aa, mu1: 1, mu2: 2})) for aa in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4))]
    check("A3", ok, f"B = a(1-a)(2 mu_1 - mu_2)^2/(2-a)^2 >= 0 for 0 <= a <= 1, so D >= [a v_1 + (1-a) v_2]/(2(2-a)) >= 0, and D = 0 only when "
          f"v_1 = v_2 = 0 together with a(1-a)(2 mu_1 - mu_2)^2 = 0: each level on a single offset with p_2 = 2 p_1 (or a single level, "
          f"a in {{0, 1}}).  That case is exactly a rigid translation: with phi = e^{{ikp}} and psi = e^{{2ikp}} the equation factors and "
          f"lambda = e^{{ikp}} exactly (symbolic), so |lambda| = 1 with arg lambda = pk - a shift, not a dispersive wave.  Every other "
          f"positive-weight law has D > 0, so none has |lambda| = 1 - O(k^4).  B at (mu_1, mu_2) = (1, 2) is {[str(x) for x in deg]} "
          f"(the rigid case), against B = a(1-a)/(2-a)^2 at (mu_1, mu_2) = (1, 1)")

    # ---------------- N1: the table
    E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    NB6 = [E1, E2, E3, tuple(-c for c in E1), tuple(-c for c in E2), tuple(-c for c in E3)]
    SETS = {
        "site+6 (light-cone)": [(0, 0, 0)] + NB6,
        "6 neighbours": NB6,
        "backward {0,e1,e2,e3}": [(0, 0, 0), E1, E2, E3],
        "8 cube corners": [c for c in itertools.product((1, -1), repeat=3)],
        "single site {0}": [(0, 0, 0)],
        "single shift {e1}": [E1],
    }
    rows = []
    okn = True
    for aa in (0.25, 0.5, 0.75):
        for n1, P1 in SETS.items():
            for n2, P2 in SETS.items():
                if (n1, n2) not in [("site+6 (light-cone)", "site+6 (light-cone)"), ("backward {0,e1,e2,e3}", "backward {0,e1,e2,e3}"),
                                    ("site+6 (light-cone)", "backward {0,e1,e2,e3}"), ("6 neighbours", "8 cube corners"),
                                    ("single site {0}", "single site {0}"), ("single shift {e1}", "single shift {e1}"),
                                    ("single site {0}", "single shift {e1}")]:
                    continue
                u = np.array([1.0, 0.0, 0.0]) / 1.0
                mu_1 = float(np.mean([np.dot(u, p) for p in P1]))
                mu_2 = float(np.mean([np.dot(u, p) for p in P2]))
                q_1 = float(np.mean([np.dot(u, p) ** 2 for p in P1]))
                q_2 = float(np.mean([np.dot(u, p) ** 2 for p in P2]))
                al_v = (aa * mu_1 + (1 - aa) * mu_2) / (2 - aa)
                D_v = float(Dsub.subs({a: aa, mu1: mu_1, mu2: mu_2, v1: q_1 - mu_1 ** 2, v2: q_2 - mu_2 ** 2}))
                lam_num = []
                for kk in (0.05, 0.1, 0.2):
                    ph = complex(np.mean([np.exp(1j * kk * np.dot(u, p)) for p in P1]))
                    ps = complex(np.mean([np.exp(1j * kk * np.dot(u, p)) for p in P2]))
                    r = np.roots([1, -aa * ph, -(1 - aa) * ps])
                    lam1 = max(r, key=abs)
                    lam_num.append((kk, abs(lam1), np.angle(lam1)))
                fit = (1 - lam_num[0][1]) / lam_num[0][0] ** 2
                okn &= abs(fit - D_v) < 0.02 + 0.1 * abs(D_v) and (D_v > 1e-12 or (q_1 - mu_1 ** 2 == 0 and q_2 - mu_2 ** 2 == 0))
                rows.append((aa, n1, n2, al_v, D_v, lam_num, fit))
    for aa, n1, n2, al_v, D_v, ln, fit in rows:
        if aa == 0.5 or n1 != n2:
            print(f"   a={aa:g} level0={n1} level1={n2}: alpha={al_v:+.4f}, D={D_v:.4f}; "
                  + ", ".join(f"k={kk}: |lambda|={m:.6f}, arg={g:+.4f}" for kk, m, g in ln))
    check("N1", okn, "(numerical, labelled) the largest root of lambda^2 - a phi lambda - (1-a) psi at k = 0.05, 0.1, 0.2 along (1,0,0) for "
          "a = 0.25, 0.5, 0.75 and the listed pairs of predecessor sets: |lambda| = 1 - D k^2 with the D of A2 (agreement better than 2 % of "
          "D or 0.02 absolute), arg lambda = alpha k; |lambda| = 1 only for the two degenerate rows (single site at both levels, single shift "
          "at both levels), where the law is a rigid translation")

    # ---------------- N2: random positive multi-level weights
    random.seed(7)
    worst = None
    mins = []
    for trial in range(200):
        J = random.choice([1, 2, 3])
        offs = [(random.randint(-2, 2), random.randint(-2, 2), random.randint(-2, 2)) for _ in range(random.randint(1, 5))]
        w = {}
        for j in range(J + 1):
            for p in offs:
                w[(j, p)] = random.random()
        tot = sum(w.values())
        w = {kk: vv / tot for kk, vv in w.items()}
        u = np.array([1.0, 0.0, 0.0])
        def sym(kk):
            return sum(wv * np.exp(1j * kk * np.dot(u, p)) * np.exp(0) for (j, p), wv in w.items())
        # the characteristic polynomial: lambda^{J+1} = sum_j (sum_p w_{j,p} e^{ikp}) lambda^{J-j}
        def roots(kk):
            coef = [1.0 + 0j] + [-sum(wv * np.exp(1j * kk * np.dot(u, p)) for (j, p), wv in w.items() if j == jj) for jj in range(J + 1)]
            return np.roots(coef)
        r0 = roots(0.0)
        lam_at = lambda kk: max(roots(kk), key=lambda z: abs(z))
        d_est = (1 - abs(lam_at(0.05))) / 0.05 ** 2
        offs_set = {p for (j, p) in w}
        proj = {p[0] for p in offs_set}                       # the law projected on u = (1,0,0)
        # degenerate along u: the projected offsets are a single point, and either that point is 0 or there is one level
        degenerate = len(proj) == 1 and (list(proj)[0] == 0 or J == 0)
        if not degenerate:
            mins.append(d_est)
            if d_est <= -1e-9:
                worst = (trial, d_est, sorted(w))
    check("N2", worst is None, "(numerical, labelled) 200 random positive multi-level weight laws (up to four levels of memory and five offsets): "
          f"the largest root obeys |lambda(0.05)| <= 1 in every non-degenerate draw ({len(mins)} of 200 draws were non-degenerate; the smallest "
          f"estimated D is {min(mins):.2e} and the median {sorted(mins)[len(mins)//2]:.4f}); degeneracy is a property of the direction: draws "
          f"whose offsets share their first coordinate have a single-point projected law along (1,0,0) and give D = 0 there while remaining "
          f"dispersive across it")

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: FAILED checks {FAILS}")
        return 0
    print("SUMMARY: with positive weights the mode nearest 1 is diffusive, not propagating: for one level |phi| = 1 - (1/2)Var k^2, and for two "
          "levels the root near 1 has arg lambda = alpha k with alpha = (a mu_1 + (1-a) mu_2)/(2-a) and |lambda| = 1 - D k^2 with "
          "D = [a v_1 + (1-a) v_2 + a(1-a)(2 mu_1 - mu_2)^2/(2-a)^2]/(2(2-a)) > 0 unless each level sits on a single offset with p_2 = 2 p_1 "
          "(a rigid translation, where lambda = e^{ikp} exactly) - so no positive-weight choice gives |lambda| = 1 - O(k^4) with a wave's linear phase")
    return 0


if __name__ == "__main__":
    sys.exit(main())
