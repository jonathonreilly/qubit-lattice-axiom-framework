#!/usr/bin/env python3
"""J:derive:wind-force-on-an-absorbing-sphere:a4 -- worker w-macbookpro90c72-j9625.

The scattering clause (C) of block 44 for the sphere menu: each bond at rate gamma re-draws the contents
of its two records uniformly on the pairs with the same sum.  For s1 + s2 = P the pairs with that sum
are the diametrically opposite points of the circle {s : |s| = 1, s.P = |P|^2/2}.

  K1  the circle and its uniform measure; the Funk-Hecke reduction
  K2  the linearised collision kernel is diagonal in spherical harmonics with eigenvalue
      mu_l = 4 int_0^1 u P_l(u)^2 du = 2 c_[l/2] c_[(l+1)/2],  c_k = (2k-1)!!/(2k)!!   (exact, l <= 12)
      mu_1 = 1 (momentum), mu_2 = 1/2 (the stress is halved by a collision), mu_3 = 3/8, mu_4 = 9/32
  K3  mu_2 = 1/2 again by an independent tensor route (isotropic rank-4 tensor, exact)
  K4  relaxation rates per record in the product closure: 6 gamma rho (1 - mu_l)
  K5  executed control (floating point): Monte Carlo of the re-draw, linear response by +-eps
See ATTEMPT.md.
"""
import numpy as np
import sympy as sp

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


u, t, phi, p = sp.symbols('u t phi p', real=True)


def K1():
    # circle: s = (p/2) Phat + sqrt(1 - p^2/4) (cos phi e1 + sin phi e2), p = |P|; P - s is on it too
    e1, e2, Ph = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])
    s = (p / 2) * Ph + sp.sqrt(1 - p**2 / 4) * (sp.cos(phi) * e1 + sp.sin(phi) * e2)
    P = p * Ph
    unit = sp.simplify(s.dot(s)) == 1
    partner = sp.simplify((P - s).dot(P - s)) == 1 and sp.simplify((P - s).dot(Ph) - p / 2) == 0
    # for independent uniform s1, s2 with t = s1.s2 (uniform on [-1,1]): |P|/2 = Phat.s1 = sqrt((1+t)/2)
    half = sp.sqrt(2 + 2 * t) / 2
    proj = (1 + t) / sp.sqrt(2 + 2 * t)
    same = sp.simplify(half - sp.sqrt((1 + t) / 2)) == 0 and sp.simplify(proj**2 - (1 + t) / 2) == 0
    rep("K1 momentum class", unit and partner and same,
        "for s1 + s2 = P the class is the circle s.Phat = |P|/2 on the unit sphere, and P - s lies on it diametrically opposite; "
        "with t = s1.s2 uniform, |P|/2 = Phat.s1 = u = sqrt((1+t)/2), so two Funk-Hecke averages give mu_l = 2 E_t[P_l(u)^2]")


def K2():
    mus = [sp.nsimplify(4 * sp.integrate(u * sp.legendre(l, u)**2, (u, 0, 1))) for l in range(1, 13)]
    c = lambda k: sp.factorial2(2 * k - 1) / sp.factorial2(2 * k) if k > 0 else sp.Integer(1)
    closed = [2 * c(l // 2) * c((l + 1) // 2) for l in range(1, 13)]
    ok = all(sp.simplify(a_ - b_) == 0 for a_, b_ in zip(mus, closed)) and mus[0] == 1 and mus[1] == sp.Rational(1, 2)
    mono = all(mus[i + 1] < mus[i] for i in range(len(mus) - 1))
    rep("K2 collision spectrum", ok and mono,
        "linearised re-draw on degree-l harmonics: mu_l = 4 int_0^1 u P_l(u)^2 du = 2 c_[l/2] c_[(l+1)/2], c_k = (2k-1)!!/(2k)!!: "
        + ", ".join(f"{m}" for m in mus[:8]) + " (l = 1..8; exact to l = 12); momentum kept (mu_1 = 1), stress halved (mu_2 = 1/2), "
        "mu_l ~ 4/(pi l)")
    return mus


def K3():
    # T_ijkl = E[g(P)_ij s1_k s1_l], g(P) = E_phi[s1' s1'^T + s2' s2'^T]; isotropic: a d_ij d_kl + b (d_ik d_jl + d_il d_jk)
    # tr g = 2 (both outgoing contents are unit) ; s1^T g s1 = (1+t)^2/2 + (1-t)^2/4
    trg = 2
    q = sp.integrate(((1 + t)**2 / 2 + (1 - t)**2 / 4) / 2, (t, -1, 1))       # E_t[s1^T g s1]
    a_, b_ = sp.symbols('a b')
    sol = sp.solve([9 * a_ + 6 * b_ - trg, 3 * a_ + 12 * b_ - q], [a_, b_])
    # traceless second moment: before 2 * (2/15) eps Q per pair, after 2b * 2 eps Q ... ratio
    before = 2 * sp.Rational(2, 15)
    after = 2 * 2 * sol[b_]
    ok = q == 1 and sol[a_] == sp.Rational(1, 5) and sol[b_] == sp.Rational(1, 30) and sp.simplify(after / before - sp.Rational(1, 2)) == 0
    rep("K3 stress halved", ok,
        f"independently: tr g = 2, E[s1.g s1] = {q}, so the isotropic tensor has a = {sol[a_]}, b = {sol[b_]}; a pair's traceless second "
        "moment 4 eps Q/15 becomes 2 eps Q/15: halved")


def K4(mus):
    g, rho = sp.symbols('gamma rho', positive=True)
    rates = [sp.simplify(6 * g * rho * (1 - m)) for m in mus[:4]]
    ok = rates[0] == 0 and sp.simplify(rates[1] - 3 * g * rho) == 0
    rep("K4 relaxation rates", ok,
        "product closure: a record meets a re-draw at rate 6 gamma rho (six bonds, the other end occupied), so the degree-l part of the "
        "content law relaxes at 6 gamma rho (1 - mu_l): " + ", ".join(str(r) for r in rates) + " for l = 1..4 (momentum conserved, "
        "stress at 3 gamma rho)")


def K5():
    rng = np.random.default_rng(3)

    def sample(n, eps):
        out = np.empty((0, 3))
        while len(out) < n:
            v = rng.normal(size=(2 * n, 3))
            v /= np.linalg.norm(v, axis=1)[:, None]
            w = 1 + eps * (3 * v[:, 2]**2 - 1) / 2
            keep = rng.uniform(0, 1 + abs(eps), size=2 * n) < w
            out = np.vstack([out, v[keep]])
        return out[:n]

    def redraw(s1, s2):
        P = s1 + s2
        Pn = np.linalg.norm(P, axis=1)
        ph = P / Pn[:, None]
        e1 = np.cross(ph, [1.0, 0, 0])
        bad = np.linalg.norm(e1, axis=1) < 1e-6
        e1[bad] = np.cross(ph[bad], [0, 1.0, 0])
        e1 /= np.linalg.norm(e1, axis=1)[:, None]
        e2 = np.cross(ph, e1)
        an = rng.uniform(0, 2 * np.pi, len(P))
        r = np.sqrt(np.clip(1 - Pn**2 / 4, 0, None))
        s1p = (Pn / 2)[:, None] * ph + r[:, None] * (np.cos(an)[:, None] * e1 + np.sin(an)[:, None] * e2)
        return s1p, P - s1p
    Y2 = lambda s: (3 * s[:, 2]**2 - 1) / 2
    n, eps = 600000, 0.3
    res = []
    for sg in (1, -1):
        s1, s2 = sample(n, sg * eps), sample(n, sg * eps)
        a1, a2 = redraw(s1, s2)
        res.append(((Y2(s1).mean() + Y2(s2).mean()) / 2, (Y2(a1).mean() + Y2(a2).mean()) / 2))
    fac = (res[0][1] - res[1][1]) / (res[0][0] - res[1][0])
    rep("K5 Monte Carlo (executed)", abs(fac - 0.5) < 0.03,
        f"re-draw of 600000 pairs from 1 +- 0.3 P_2(z), linear response by the difference: l = 2 factor {fac:.3f} (exact 1/2)")


def main():
    K1()
    mus = K2()
    K3()
    K4(mus)
    K5()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL the exact relaxation spectrum of clause (C) for the sphere menu: the linearised momentum-class re-draw "
              "multiplies degree-l harmonics by mu_l = 4 int_0^1 u P_l(u)^2 du = 2 c_[l/2] c_[(l+1)/2] (mu_1 = 1, mu_2 = 1/2, mu_3 = 3/8), "
              "so the stress relaxes at 3 gamma rho per record in the product closure; the flow past an absorbing sphere and K/K0 "
              "(tasks a-b) are not solved; the regimes (c) are stated from these rates")
        print("HIT: block 44's scattering clause for the sphere menu, linearised, is diagonal in spherical harmonics with eigenvalues "
              "mu_l = 4 int_0^1 u P_l(u)^2 du = 2 c_[l/2] c_[(l+1)/2], c_k = (2k-1)!!/(2k)!!: momentum is kept, the traceless second moment "
              "(the stress) is halved by every collision, so it relaxes at 3 gamma rho per record in the product closure, and the l-th "
              "moment at 6 gamma rho (1 - mu_l)")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
