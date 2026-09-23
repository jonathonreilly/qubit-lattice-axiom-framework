#!/usr/bin/env python3
"""J:derive:what-fixes-the-powers-and-the-kinetic-sign:a1 -- worker w-macbookpro90c72-j3daf.

Block 60's member G = K l^p (a Lap lam + b q) (lam = log l), F = sum_x w_x G_x, the kinetic term
sum_x c_k l_x^s (dlam_x/dt)^2 / w_x, content <H> = sum_b c_b <h_b> + sum_x w_x <m_x>, bonds crossed at
sqrt(w_x w_y)/(chi_x chi_y), chi = sqrt(l).  Exact sympy checks of what each principle fixes.

  W1  change of the time label (all rates x L): every term has weight one for all p, s: nothing fixed
  W2  uniform rescaling of all lengths with the hop rates held (l -> C l forces w -> C w):
      <H>_hop x 1, <H>_rest x C, F x C^(1+p), kinetic x C^(s-1)
  W3  the field disturbances' frequency against the walker's: omega^2 x C^(2+p-s): unit-free iff s = p + 2
  W4  the closed-lattice sum rule (block 60 T5): a uniform solution with positive content needs c_k < 0;
      l ~ t^(2/s)
  W5  the geometric count: sqrt(g) R for g = l^2 delta in d dimensions is l^(d-2) x (two derivatives of lam):
      p = d - 2 (= 1), and then s = p + 2 = d (= 3); block 62's speed agreement fixes alpha/K = 1/4
See ATTEMPT.md.
"""
import sympy as sp

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


n = 4
lam = sp.symbols('lam0:%d' % n, real=True)
u = sp.symbols('u0:%d' % n, real=True)
ldot = sp.symbols('ld0:%d' % n, real=True)
K, a, b, p, s, ck, C, Lm = sp.symbols('K a b p s c_k C L', positive=True)
th = sp.symbols('h0:%d' % n, real=True)          # hop energy per tick on bond (x, x+1) of a ring
rm = sp.symbols('r0:%d' % n, real=True)          # on-site energy per tick


def ring_terms(lam_, w_):
    lap = lambda f, z: f[(z + 1) % n] + f[(z - 1) % n] - 2 * f[z]
    q = lambda z: ((lam_[(z + 1) % n] - lam_[z])**2 + (lam_[(z - 1) % n] - lam_[z])**2) / 2
    F = sum(w_[z] * K * sp.exp(p * lam_[z]) * (a * lap(lam_, z) + b * q(z)) for z in range(n))
    kin = sum(ck * sp.exp(s * lam_[z]) * ldot[z]**2 / w_[z] for z in range(n))
    return F, kin


def W1():
    w = [sp.exp(x) for x in u]
    F, kin = ring_terms(lam, w)
    Fl, kinl = ring_terms(lam, [Lm * x for x in w])
    kinl = kinl.subs({ld: Lm * ld for ld in ldot}, simultaneous=True)       # d/dt scales with the label
    okF = sp.simplify(Fl - Lm * F) == 0
    okK = sp.simplify(kinl - Lm * kin) == 0
    rep("W1 time label", okF and okK,
        "rates x L (lengths, weight zero, unchanged; d/dt x L): F and the kinetic term both have weight one for every p and s, like <H>: "
        "the label fixes nothing about p, s or c_k")


def W2():
    w = [sp.exp(x) for x in u]
    F, kin = ring_terms(lam, w)
    lamC = [x + sp.log(C) for x in lam]                  # l -> C l
    wC = [C * x for x in w]                              # hop rates sqrt(w w)/sqrt(l l) held => w -> C w
    FC, kinC = ring_terms(lamC, wC)
    z0 = lambda e: sp.simplify(sp.powsimp(sp.expand_power_exp(sp.expand(e)), force=True)) == 0
    okF = z0(FC - C**(1 + p) * F)
    okK = z0(kinC - C**(s - 1) * kin)
    cb = [sp.sqrt(w[z] * w[(z + 1) % n]) / sp.exp((lam[z] + lam[(z + 1) % n]) / 2) for z in range(n)]
    cbC = [sp.sqrt(wC[z] * wC[(z + 1) % n]) / sp.exp((lamC[z] + lamC[(z + 1) % n]) / 2) for z in range(n)]
    hop_same = all(z0(cbC[z] - cb[z]) for z in range(n))
    H = sum(cb[z] * th[z] for z in range(n)) + sum(w[z] * rm[z] for z in range(n))
    HC = sum(cbC[z] * th[z] for z in range(n)) + sum(wC[z] * rm[z] for z in range(n))
    okH = z0(HC - (sum(cb[z] * th[z] for z in range(n)) + C * sum(w[z] * rm[z] for z in range(n))))
    # a definite weight for the whole ledger: massless content (weight 0) would need 1 + p = 0 and s - 1 = 0
    rep("W2 length rescaling", okF and okK and hop_same and okH,
        "l -> C l with the hop rates held (so w -> C w): the walker's hop energy is unchanged, its rest energy x C, F x C^(1+p), the kinetic "
        "term x C^(s-1): no single weight for the whole ledger (massless content alone would need p = -1, s = 1, i.e. beta = 1/p < 0); "
        "K absorbs the unit: the member is unchanged if K -> C^-(1+p) K, so K has the dimension of length^-(1+p) (length^-2 at p = 1)")


def W3():
    w0, l0, al, P2, om = sp.symbols('wbar lbar alpha P2 omega', positive=True)
    # second order about the uniform state: kinetic (alpha lbar^s / wbar) omega^2 = static K wbar lbar^p P2
    omega2 = sp.solve(sp.Eq(al * l0**s / w0 * om**2, K * w0 * l0**p * P2), om**2)[0]
    scaled = omega2.subs({l0: C * l0, w0: C * w0}, simultaneous=True)
    ratio = sp.simplify(scaled / omega2)
    ok = sp.simplify(ratio - C**(2 + p - s)) == 0 and sp.simplify(ratio.subs(s, p + 2)) == 1 and ratio.subs({p: 1, s: 3}) == 1
    # the walker's frequency at fixed hop rates is unchanged, so the ratio of speeds is unit-free iff s = p + 2
    rep("W3 unit-free speed", ok,
        "the field's second-order mode equation (alpha lbar^s/wbar) omega^2 = K wbar lbar^p P^2 gives omega^2 x C^(2+p-s) under the rescaling, "
        "while the walker's frequency (hop rates held) is unchanged: the disturbances' speed relative to the walker's top speed does not "
        "depend on the unit of length iff s = p + 2; block 60's (p, s) = (1, 3) satisfies it")


def W4():
    m, w, l, ld, t, t0 = sp.symbols('m w l ld t t0', positive=True)
    L = ck * l**s * ld**2 / w - m * w                      # block 60 T5, uniform, content at rest m per site
    ckw = sp.solve(sp.diff(L, w).subs(ck, sp.Symbol('kk')), sp.Symbol('kk'))[0]
    neg = sp.simplify(ckw + m * w**2 / (l**s * ld**2)) == 0     # c_k = -m w^2/(l^s ld^2) < 0
    ell = (1 + t / t0)**(2 / s)
    lamt = sp.log(ell)
    eq = sp.simplify(2 * sp.diff(lamt, t, 2) + s * sp.diff(lamt, t)**2) == 0
    rep("W4 kinetic sign", neg and eq,
        "on a closed lattice (every rate varied, ledger zero) a uniform solution with content at rest needs m w^2 + c_k l^s lamdot^2 = 0, "
        "so c_k < 0 whenever m > 0; then 2 lamddot + s lamdot^2 = 0 and l = (1 + t/t0)^(2/s): at s = 3 the comparator's t^(2/3)")


def W5():
    # conformally flat g = exp(2 lam) delta in d = 3: sqrt(g) R computed from Christoffel symbols
    x = sp.symbols('x1:4', real=True)
    lf = sp.Function('lam')(*x)
    d = 3
    g = sp.exp(2 * lf) * sp.eye(d)
    gi = sp.exp(-2 * lf) * sp.eye(d)
    Gam = [[[sum(gi[i, l_] * (sp.diff(g[l_, j], x[k]) + sp.diff(g[l_, k], x[j]) - sp.diff(g[j, k], x[l_])) for l_ in range(d)) / 2
             for k in range(d)] for j in range(d)] for i in range(d)]
    Ric = sp.zeros(d, d)
    for j in range(d):
        for k in range(d):
            Ric[j, k] = sum(sp.diff(Gam[i][j][k], x[i]) - sp.diff(Gam[i][j][i], x[k])
                            + sum(Gam[i][i][l_] * Gam[l_][j][k] - Gam[i][k][l_] * Gam[l_][j][i] for l_ in range(d)) for i in range(d))
    R = sp.simplify(sum(gi[j, k] * Ric[j, k] for j in range(d) for k in range(d)))
    sqrtgR = sp.simplify(sp.exp(d * lf) * R)
    lapl = sum(sp.diff(lf, xi, 2) for xi in x)
    grad2 = sum(sp.diff(lf, xi)**2 for xi in x)
    ok_R = sp.simplify(sqrtgR - (-sp.exp(lf) * (4 * lapl + 2 * grad2))) == 0     # l^(d-2) with d = 3: p = 1; block 60 T3(d)
    al = sp.symbols('alpha', positive=True)
    speed = sp.solve(sp.Eq(K / (4 * al), 1), al)[0]                              # block 62: X = K wbar^2 P^2/(4 alpha) vs walker P^2
    rep("W5 geometric count", ok_R and speed == K / 4,
        "for g = l^2 delta in three dimensions sqrt(g) R = -l (4 Lap lam + 2 |grad lam|^2): the volume l^3 times a curvature of weight l^-2 "
        "gives p = d - 2 = 1 (block 60 T3(d)), and W3 then gives s = p + 2 = d = 3 (the volume power of the kinetic term); block 62's "
        "speed agreement fixes alpha = K/4")


def main():
    W1(); W2(); W3(); W4(); W5()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL what the principles fix: the change of label fixes nothing; the uniform rescaling of all lengths at held hop "
              "rates multiplies F by C^(1+p) and the kinetic term by C^(s-1) and leaves the walker's hop energy alone, so it is a change of "
              "the unit of length absorbed by K ~ length^-(1+p); unit-free wave speeds force s = p + 2 (block 60's 3 = 1 + 2); the "
              "closed-lattice sum rule forces c_k < 0; p = 1 (beta = 1) is fixed only by declaring the field energy the volume integral of "
              "the curvature (p = d - 2); alpha/K = 1/4 only by declaring speed agreement")
        print("HIT: in block 60's member a uniform rescaling of all lengths at held hop rates multiplies F by C^(1+p), the kinetic term by "
              "C^(s-1) and the field waves' frequency^2 by C^(2+p-s) while the walker's hop energy is unchanged, so the waves' speed "
              "relative to the walker's top speed is free of the unit of length exactly when s = p + 2 (p = 1 gives the declared s = 3), "
              "a uniform closed-lattice solution with content needs c_k < 0, and p itself is fixed only by the curvature reading p = d - 2")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
