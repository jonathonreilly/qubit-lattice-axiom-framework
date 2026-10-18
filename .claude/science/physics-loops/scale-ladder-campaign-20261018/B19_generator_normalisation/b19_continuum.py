#!/usr/bin/env python3
"""B19 continuum: is the relabelling-generator normalisation (and hence the 'common cone') fixed by the algebra?

Exact sympy jet calculus in 3D (b19_jets.py, written fresh).  Conventions:
  delta_xi F := {F, G[xi]};  Lie bracket [xi,eta]^k = xi.d eta^k - eta.d xi^k.
  gravity: g = delta + h, six independent h_a (a = 00,11,22,01,02,12) with momenta P_a,
     G_g[xi] = sum_a P_a (L_xi g)_a = lam1 * G1[xi] + lam2 * G2[xi],
     G1 = sum P_a (d_i xi_j + d_j xi_i)  (linear, abelian),  G2 = sum P_a (xi.d h_ij + h_kj d_i xi^k + h_ik d_j xi^k);
     kin = (sum Pd^2 - (sum Pd)^2/2)/(4 alpha) + sum Poff^2/(8 alpha)  (GR form, B14 normalisation);
     C_g(N) = N [kin - K1 R1(h) - K2 [sqrt g R]^(2)(h)]   (GR sign; K1 = K2 is GR).
  scalar: H_m = ak pi^2/2 + c |d phi|^2/2 + mu phi^2/2;  G_m[xi] = int pi xi.d phi  (pi a weight-1 density).
  Maxwell: H_A = (g2/2) E^2 + (cB/(4 g2)) F_ij F_ij;  G_c[xi] = int E^i xi^k F_ki (gauge covariant),
     G_L[xi] = int E^i L_xi A_i (Lie);  Gauss[theta] = int theta d_i E^i.
  Sector normalisations lam_m, lam_A multiply G_m, G_c in the total generator.

Families (PASS/FAIL):
  C1  {G_m,G_m}: closes with unit structure constant and the stated sign; lam G_m needs lam in {0, nu}.
  C2  {G_g,G_g} with (lam1, lam2): closes iff lam2 = nu; lam1 is NOT fixed (abelian linear part).
  C3  Maxwell: G_L closes exactly; G_c closes up to Gauss[b xi^i eta^j F_ij]; sign/coefficient b.
  C4  total {G,G}: lam_m = lam_A = lam2 = nu forced; lam1 free.
  C5  {C,C} at O(eps): the cone relation of each species in terms of (lam_s, lam1, K1, alpha).
  C6  {G,C} at O(phi^2) per species with free coupling strength a_s, trace t_s, lapse rule (s1, s2), Gauss:
      s1 = -lam_s, a_s lam1 = lam_s.  Joint scalar+Maxwell: one lapse rule forces lam_m = lam_A (no {G,G} used).
  C7  gravity {G,C} at degree 1 (needs G2 and the h^2 potential): s1 = -lam2 and lam1 K2 = lam2 K1.
  C8  TT graviton speed^2 from C_g^(2): K2/(4 alpha).
  C9  chain C5+C6+C7: every matter cone = K2/(4 alpha) = graviton cone; all lam's cancel.
  C10 canonical rescalings (phi->phi/sqrt r, pi->sqrt r pi; h->rho h, P->P/rho) map the families to themselves
      with lam_s invariant (matter) / lam1 -> lam1/rho (gravity), and leave every derived cone relation invariant.
"""
from __future__ import annotations

import sympy as sp

from b19_jets import J, D, e_, bracket, degree_part, functional_zero_eqs, is_zero_functional, euler, DIM

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


COMP = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
HN = {ab: f"h{ab[0]}{ab[1]}" for ab in COMP}
PN = {ab: f"P{ab[0]}{ab[1]}" for ab in COMP}
GRAV = set(HN.values()) | set(PN.values())
MATS = {"phi", "pi"}
MATA = {f"A{i}" for i in range(DIM)} | {f"E{i}" for i in range(DIM)}
CONJ = {"phi": "pi", **{HN[ab]: PN[ab] for ab in COMP}, **{f"A{i}": f"E{i}" for i in range(DIM)}}
PHASE = list(CONJ.keys()) + list(CONJ.values())


def hs(i, j, a=(0, 0, 0)):
    return J(HN[(min(i, j), max(i, j))], a)


def dJ(f, k):
    return J(f, e_(k))


lam1, lam2, lamm, lamA, nu = sp.symbols("lam1 lam2 lam_m lam_A nu")
al, K1, K2, ak, c, mu, g2, cB = sp.symbols("alpha K1 K2 a_k c mu g2 c_B", positive=True)
eps = sp.Symbol("e")
XI = [J(f"xi{k}") for k in range(DIM)]
ETA = [J(f"eta{k}") for k in range(DIM)]
N, M = J("N"), J("M")
phi, pi = J("phi"), J("pi")
A = [J(f"A{i}") for i in range(DIM)]
E = [J(f"E{i}") for i in range(DIM)]


def lie(x, y):
    return [sp.expand(sum(x[l] * D(y[k], l) - y[l] * D(x[k], l) for l in range(DIM))) for k in range(DIM)]


# ------------------------------------------------------------------ generators
def G1(x):
    return sp.expand(sum(J(PN[(i, j)]) * (D(x[j], i) + D(x[i], j)) for (i, j) in COMP))


def G2(x):
    out = 0
    for (i, j) in COMP:
        v = sum(x[k] * D(hs(i, j), k) for k in range(DIM))
        v += sum(hs(k, j) * D(x[k], i) + hs(i, k) * D(x[k], j) for k in range(DIM))
        out += J(PN[(i, j)]) * v
    return sp.expand(out)


def Gm(x):
    return sp.expand(pi * sum(x[k] * dJ("phi", k) for k in range(DIM)))


def Fk(k, i):
    return D(A[i], k) - D(A[k], i)


def Gc(x):
    return sp.expand(sum(E[i] * sum(x[k] * Fk(k, i) for k in range(DIM)) for i in range(DIM)))


def GL(x):
    return sp.expand(sum(E[i] * sum(x[k] * D(A[i], k) + A[k] * D(x[k], i) for k in range(DIM)) for i in range(DIM)))


def gauss(theta):
    return sp.expand(theta * sum(D(E[i], i) for i in range(DIM)))


# ------------------------------------------------------------------ metric expansions
def trunc(x, n=2):
    x = sp.expand(x)
    return sp.Add(*[x.coeff(eps, k) * eps ** k for k in range(n + 1)])


H = [[hs(i, j) for j in range(DIM)] for i in range(DIM)]
TRH = sum(H[i][i] for i in range(DIM))
TRH2 = sp.expand(sum(H[i][j] * H[j][i] for i in range(DIM) for j in range(DIM)))
GINV = [[sp.expand((1 if i == j else 0) - eps * H[i][j] + eps ** 2 * sum(H[i][k] * H[k][j] for k in range(DIM)))
         for j in range(DIM)] for i in range(DIM)]
SQRTG = 1 + eps * TRH / 2 + eps ** 2 * (TRH ** 2 / 8 - TRH2 / 4)
ISQRTG = 1 - eps * TRH / 2 + eps ** 2 * (TRH ** 2 / 8 + TRH2 / 4)
GMET = [[(1 if i == j else 0) + eps * H[i][j] for j in range(DIM)] for i in range(DIM)]


def sqrtg_R():
    dg = [[[eps * hs(i, j, e_(k)) for j in range(DIM)] for i in range(DIM)] for k in range(DIM)]
    Gam = [[[trunc(sp.Rational(1, 2) * sum(GINV[k][l] * (dg[i][l][j] + dg[j][l][i] - dg[l][i][j]) for l in range(DIM)))
             for j in range(DIM)] for i in range(DIM)] for k in range(DIM)]
    Ric = [[0] * DIM for _ in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            r = sum(D(Gam[k][i][j], k) - D(Gam[k][i][k], j) for k in range(DIM))
            r += sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in range(DIM) for l in range(DIM))
            Ric[i][j] = trunc(r)
    R = trunc(sum(GINV[i][j] * Ric[i][j] for i in range(DIM) for j in range(DIM)))
    return trunc(SQRTG * R)


def kin():
    pd = [J(PN[(j, j)]) for j in range(DIM)]
    tr = sum(pd)
    return (sum(p ** 2 for p in pd) - tr ** 2 / 2) / (4 * al) + sum(J(PN[ab]) ** 2 for ab in COMP[3:]) / (8 * al)


def Hm0():
    return ak * pi ** 2 / 2 + c * sum(dJ("phi", k) ** 2 for k in range(DIM)) / 2 + mu * phi ** 2 / 2


def Hm_g1():
    """O(h) part of ak pi^2/(2 sqrt g) + sqrt g (c g^ij d phi d phi + mu phi^2)/2 (metric-variational stress)."""
    full = ak * pi ** 2 / 2 * ISQRTG + SQRTG * (c * sum(GINV[i][j] * dJ("phi", i) * dJ("phi", j)
                                                       for i in range(DIM) for j in range(DIM)) + mu * phi ** 2) / 2
    return sp.expand(trunc(full, 1)).coeff(eps, 1)


def HA0():
    return g2 / 2 * sum(e ** 2 for e in E) + cB / (4 * g2) * sum(Fk(i, j) ** 2 for i in range(DIM) for j in range(DIM))


def HA_g1():
    el = g2 / 2 * ISQRTG * sum(GMET[i][j] * E[i] * E[j] for i in range(DIM) for j in range(DIM))
    mg = cB / (4 * g2) * SQRTG * sum(GINV[i][k] * GINV[j][l] * Fk(i, j) * Fk(k, l)
                                     for i in range(DIM) for j in range(DIM) for k in range(DIM) for l in range(DIM))
    return sp.expand(trunc(el + mg, 1)).coeff(eps, 1)


def eqs_of(expr):
    return functional_zero_eqs(expr, PHASE)


def solve(eqs, unk):
    return sp.solve(eqs, unk, dict=True)


# ================================================================== C1
def c1():
    br = bracket(Gm(XI), Gm(ETA), CONJ)
    LB = lie(XI, ETA)
    ok = is_zero_functional(br - Gm(LB), PHASE)
    wrong = is_zero_functional(br + Gm(LB), PHASE)
    check("C1a", ok and not wrong, "{G_m[xi],G_m[eta]} = +G_m[[xi,eta]] exactly (pi weight-1 density, delta_xi F = {F,G[xi]} = L_xi F); the opposite sign fails")
    lam = sp.Symbol("lam")
    sol = solve(eqs_of(lam ** 2 * br - nu * lam * Gm(LB)), [lam])
    check("C1b", sol == [{lam: 0}, {lam: nu}] or sol == [{lam: nu}, {lam: 0}],
          f"lam G_m closes with structure constant nu iff lam in {{0, nu}}: {sol} -- already at the matter field's LEADING (quadratic) order")


# ================================================================== C2
def c2():
    G = lambda x: lam1 * G1(x) + lam2 * G2(x)
    br = bracket(G(XI), G(ETA), CONJ)
    LB = lie(XI, ETA)
    ok1 = is_zero_functional(bracket(G1(XI), G1(ETA), CONJ), PHASE)
    exact = is_zero_functional((br - G(LB)).subs({lam1: 1, lam2: 1}), PHASE)
    check("C2a", ok1 and exact, "{G1,G1} = 0 (linear generator abelian); full G_g = int P L_xi(delta+h) closes: {G_g[xi],G_g[eta]} = G_g[[xi,eta]] to all orders (G_g is degree 1+2)")
    d1 = degree_part(br - nu * G(LB), GRAV, 1)
    d2 = degree_part(br - nu * G(LB), GRAV, 2)
    s1 = solve(eqs_of(d1), [lam2])
    s2 = solve(eqs_of(d2), [lam2])
    sol = solve(eqs_of(br - nu * G(LB)), [lam1, lam2])
    print("   degree-1 condition ->", s1, "; degree-2 condition ->", s2, "; joint ->", sol)
    check("C2b", {lam2: nu} in s1 and {lam2: nu} in sol and all(lam1 not in s for s in sol if s.get(lam2) == nu),
          "with G = lam1 G1 + lam2 G2: closure (structure constant nu) forces lam2 = nu but leaves lam1 FREE -- the normalisation of the linear (abelian) gauge shift delta h = 2 lam1 d xi is not fixed by {G,G}; lam1/lam2 is the scale r of the background in g = r delta + h")


# ================================================================== C3
def c3():
    LB = lie(XI, ETA)
    okL = is_zero_functional(bracket(GL(XI), GL(ETA), CONJ) - GL(LB), PHASE)
    check("C3a", okL, "Lie generator G_L[xi] = int E^i L_xi A_i (E weight-1 vector density): {G_L[xi],G_L[eta]} = G_L[[xi,eta]] exactly")
    b = sp.Symbol("b")
    th = sum(XI[i] * ETA[j] * Fk(i, j) for i in range(DIM) for j in range(DIM))
    brc = bracket(Gc(XI), Gc(ETA), CONJ)
    no_gauss = is_zero_functional(brc - Gc(LB), PHASE)
    sol = solve(eqs_of(brc - Gc(LB) - gauss(b * th)), [b])
    rel = is_zero_functional(Gc(XI) - GL(XI) - gauss(sum(XI[k] * A[k] for k in range(DIM))), PHASE)
    check("C3b", (not no_gauss) and sol == [{b: -1}] and rel,
          f"covariant G_c = G_L + Gauss[xi.A]; {{G_c[xi],G_c[eta]}} = G_c[[xi,eta]] + Gauss[b xi^i eta^j F_ij] with b = {sol} (closes only mod Gauss, field-dependent multiplier)")
    lam = sp.Symbol("lam")
    bb = sp.Symbol("bb")
    sol2 = solve(eqs_of(lam ** 2 * brc - nu * lam * Gc(LB) - gauss(bb * th)), [lam, bb])
    check("C3c", any(s.get(lam) == nu for s in sol2) and all(s.get(lam) in (0, nu) for s in sol2),
          f"lam G_c closes mod Gauss with structure constant nu iff lam in {{0, nu}} (any Gauss multiplier allowed): {sol2}")


# ================================================================== C4
def c4():
    LB = lie(XI, ETA)
    G = lambda x: lam1 * G1(x) + lam2 * G2(x) + lamm * Gm(x) + lamA * Gc(x)
    cross = [bracket(G1(XI) + G2(XI), Gm(ETA), CONJ), bracket(G1(XI) + G2(XI), Gc(ETA), CONJ), bracket(Gm(XI), Gc(ETA), CONJ)]
    check("C4a", all(is_zero_functional(x, PHASE) for x in cross), "cross brackets {G_g,G_m}, {G_g,G_c}, {G_m,G_c} vanish identically (neither matter generator contains the metric when momenta are densities)")
    bb = sp.Symbol("bb")
    th = sum(XI[i] * ETA[j] * Fk(i, j) for i in range(DIM) for j in range(DIM))
    res = bracket(G(XI), G(ETA), CONJ) - nu * G(LB) - gauss(bb * th)
    sol = solve(eqs_of(res), [lam2, lamm, lamA, bb])
    nontriv = [s for s in sol if s.get(lamm) not in (0, None) and s.get(lamA) not in (0, None) and s.get(lam2) not in (0, None)]
    ok = nontriv == [{lam2: nu, lamm: nu, lamA: nu, bb: -nu}] or (len(nontriv) == 1 and nontriv[0][lam2] == nu and nontriv[0][lamm] == nu and nontriv[0][lamA] == nu)
    print("   all solutions:", sol)
    check("C4b", ok, f"total G = lam1 G1 + lam2 G2 + lam_m G_m + lam_A G_c closes (mod Gauss) with all sectors nonzero iff lam2 = lam_m = lam_A = nu; lam1 free: {nontriv}")


# ================================================================== C5
def c5():
    chi, d = sp.symbols("chi d")
    R1 = sp.expand(sqrtg_R()).coeff(eps, 1)
    R1_std = sp.expand(sum(D(D(hs(i, j), i), j) for i in range(DIM) for j in range(DIM)) - sum(D(D(TRH, k), k) for k in range(DIM)))
    check("C5r", sp.expand(R1 - R1_std) == 0, "[sqrt g R]^(1) = d_i d_j h_ij - lap tr h (the B14/09-24 R1)")
    dens = kin() - K1 * R1 + Hm0() + HA0()
    br = bracket(N * dens, M * dens, CONJ)
    grav = degree_part(degree_part(br, GRAV, 1), MATS | MATA, 0)
    mat = degree_part(degree_part(br, GRAV, 0), MATS | MATA, 2)
    x0 = [N * D(M, k) - M * D(N, k) for k in range(DIM)]
    rhs = lam1 * G1([chi * v for v in x0]) + lamm * Gm([chi * v for v in x0]) + lamA * Gc([chi * v for v in x0]) \
        + gauss(d * sum(x0[k] * A[k] for k in range(DIM)))
    sol = solve(eqs_of(grav + mat - rhs), [chi, c, cB, d])
    print("   {C,C} O(eps) solution:", sol)
    ok = len(sol) == 1 and sp.simplify(sol[0][chi] - K1 / (4 * al * lam1)) == 0 \
        and sp.simplify(ak * sol[0][c] - lamm * K1 / (4 * al * lam1)) == 0 \
        and sp.simplify(sol[0][cB] - lamA * K1 / (4 * al * lam1)) == 0
    check("C5", ok, "{C(N),C(M)} at O(eps) [C = kin - K1 R1 + H_m + H_A, GR sign] closes into ONE lam1 G1 + lam_m G_m + lam_A G_c [chi xi0], xi0 = N dM - M dN, iff chi = K1/(4 alpha lam1) and each species' speed^2 v_s^2 (= ak c, cB) = lam_s K1/(4 alpha lam1) [analytic expectation: {H_s(N),H_s(M)} = v_s^2 G_s[xi0], {C_g(N),C_g(M)} = (K1/4alpha) G1[xi0]]: v_s^2 is proportional to lam_s/lam1, so doubling one generator doubles that species' cone (B16 T3c)")
    return sol[0]


# ================================================================== C6
def c6():
    s1, s2 = sp.symbols("s1 s2")
    Np = [s1 * sum(XI[k] * D(N, k) for k in range(DIM)) + s2 * N * sum(D(XI[k], k) for k in range(DIM))][0]
    out = {}
    # scalar
    am, tm, bm = sp.symbols("a_m t_m beta_m")
    Cs = N * (Hm0() + am * Hm_g1() + tm * TRH * Hm0())
    G = lam1 * G1(XI) + lamm * Gm(XI)
    lhs = degree_part(bracket(Cs, G, CONJ), GRAV, 0)
    rhs = Np * Hm0() + bm * N * Gm(XI)
    sol = solve(eqs_of(lhs - rhs), [am, tm, s1, s2, bm])
    print("   scalar {G,C} phi^2:", sol)
    oks = len(sol) == 1 and sp.simplify(sol[0][s1] + lamm) == 0 and sp.simplify(sol[0][am] - lamm / lam1) == 0
    check("C6a", oks, "scalar {C_s(N), lam1 G1 + lam_m G_m} at O(phi^2) = H_m(s1 xi.dN + s2 N div xi) iff s1 = -lam_m and coupling strength a_m = lam_m/lam1 (times the metric stress), trace t_m tied to s2: the lapse transforms with the matter normalisation")
    out["m"] = sol[0]
    # Maxwell
    aA, tA, b1, b2, bA = sp.symbols("a_A t_A b1 b2 beta_A")
    CA = N * (HA0() + aA * HA_g1() + tA * TRH * HA0())
    G = lam1 * G1(XI) + lamA * Gc(XI)
    lhs = degree_part(bracket(CA, G, CONJ), GRAV, 0)
    rhs = Np * HA0() + gauss(b1 * N * sum(XI[k] * E[k] for k in range(DIM)) + b2 * N * sum(XI[k] * A[k] for k in range(DIM))) + bA * N * Gc(XI)
    solA = solve(eqs_of(lhs - rhs), [aA, tA, s1, s2, b1, b2, bA])
    print("   Maxwell {G,C} A^2:", solA)
    okA = len(solA) == 1 and sp.simplify(solA[0][s1] + lamA) == 0 and sp.simplify(solA[0][aA] - lamA / lam1) == 0
    check("C6b", okA, "Maxwell {C_A(N), lam1 G1 + lam_A G_c} at O(A^2) = H_A(s1 xi.dN + s2 N div xi) + Gauss[b1 N xi.E + b2 N xi.A] iff s1 = -lam_A, a_A = lam_A/lam1 (Maxwell metric stress)")
    out["A"] = solA[0]
    # joint: one constraint C = C_s + C_A, one lapse rule
    Cj = N * (Hm0() + am * Hm_g1() + tm * TRH * Hm0() + HA0() + aA * HA_g1() + tA * TRH * HA0())
    G = lam1 * G1(XI) + lamm * Gm(XI) + lamA * Gc(XI)
    lhs = degree_part(bracket(Cj, G, CONJ), GRAV, 0)
    rhs = Np * (Hm0() + HA0()) + gauss(b1 * N * sum(XI[k] * E[k] for k in range(DIM)) + b2 * N * sum(XI[k] * A[k] for k in range(DIM))) \
        + bm * N * Gm(XI) + bA * N * Gc(XI)
    solj = solve(eqs_of(lhs - rhs), [am, tm, aA, tA, s1, s2, b1, b2, bm, bA, lamA])
    print("   joint scalar+Maxwell:", solj)
    okj = len(solj) == 1 and sp.simplify(solj[0][lamA] - lamm) == 0
    check("C6c", okj, "scalar + Maxwell with ONE constraint and ONE lapse rule: closure at O(matter^2) forces lam_A = lam_m (no {G,G} input, no nonlinear gravity): doubling G_A alone is excluded at the leading order of the {G,C} bracket")
    return out


# ================================================================== C7, C8
def c7():
    s1, s2 = sp.symbols("s1 s2")
    SR = sqrtg_R()
    R1 = sp.expand(SR).coeff(eps, 1)
    R2 = sp.expand(SR).coeff(eps, 2)
    C = N * (-K1 * R1 - K2 * R2)
    G = lam1 * G1(XI) + lam2 * G2(XI)
    lhs = degree_part(bracket(C, G, CONJ), GRAV, 1)
    Np = s1 * sum(XI[k] * D(N, k) for k in range(DIM)) + s2 * N * sum(D(XI[k], k) for k in range(DIM))
    sol = solve(eqs_of(lhs - Np * (-K1 * R1)), [s1, s2, K2])
    print("   gravity {C,G} degree 1:", sol)
    ok = len(sol) == 1 and sp.simplify(sol[0][s1] + lam2) == 0 and sol[0][s2] == 0 and sp.simplify(sol[0][K2] - K1 * lam2 / lam1) == 0
    check("C7", ok, "gravity {C_g(N), lam1 G1 + lam2 G2} at degree 1 (h-linear; needs the nonlinear G2 and the h^2 potential) = C^(1)(s1 xi.dN + s2 N div xi) iff s1 = -lam2, s2 = 0 and K2 = K1 lam2/lam1 (GR: lam1 = lam2 <=> K1 = K2)")
    # C8 TT graviton: only h01(z)
    sub = {}
    for s in R2.free_symbols:
        from b19_jets import KEY
        if s in KEY:
            f, a = KEY[s]
            if f != "h01" or a[0] or a[1]:
                sub[s] = 0
    pot = sp.expand(-K2 * R2.xreplace(sub))
    h = J("h01")
    eul = euler(pot, "h01")
    Bc = sp.simplify(-eul / (2 * J("h01", (0, 0, 2))))
    Akin = 1 / (8 * al)
    w2 = sp.simplify(4 * Akin * Bc)
    check("C8", sp.simplify(w2 - K2 / (4 * al)) == 0 and sp.simplify(eul + 2 * Bc * J("h01", (0, 0, 2))) == 0,
          f"TT graviton h_01(z): potential -K2[sqrt g R]^(2) = B (d_z h01)^2 + t.d. with B = {Bc}; kinetic P01^2/(8 alpha); omega^2/k^2 = {w2}")
    return sol[0], w2


# ================================================================== C9, C10
def c9(cc, gg, w2):
    # C6/C7: the lapse rule s1 multiplies the WHOLE constraint, so s1 = -lam_m = -lam_A = -lam2 (one C, one N')
    sub = {lamm: lam2, lamA: lam2}
    K1_of = sp.solve(sp.Eq(K2, gg[K2]), K1)[0]
    vm = sp.simplify((ak * cc[c]).subs(sub).subs(K1, K1_of))
    vA = sp.simplify(cc[cB].subs(sub).subs(K1, K1_of))
    print(f"   chain: v_m^2 = {vm}, v_A^2 = {vA}, graviton v^2 = {w2}")
    ok = sp.simplify(vm - w2) == 0 and sp.simplify(vA - w2) == 0
    check("C9", ok, "chain C5+C6+C7: one lapse rule s1 for the whole C => lam_m = lam_A = lam2; with K2 lam1 = K1 lam2 (C7) every species' cone v_s^2 = lam2 K1/(4 alpha lam1) = K2/(4 alpha) = TT graviton speed^2 (C8): all generator normalisations cancel -- but only once the gravity sector is taken to degree 1 (G2 and the h^2 potential)")
    return vm


def c10(cc, cm, gg):
    r, rho = sp.symbols("r rho", positive=True)
    # matter point rescaling phi -> phi/sqrt r, pi -> sqrt r pi
    from b19_jets import KEY
    def resc(expr, names, fac):
        expr = sp.expand(expr)
        return sp.expand(expr.xreplace({s: fac[KEY[s][0]] * s for s in expr.free_symbols if s in KEY and KEY[s][0] in names}))
    fm = {"phi": 1 / sp.sqrt(r), "pi": sp.sqrt(r)}
    okG = sp.expand(resc(Gm(XI), MATS, fm) - Gm(XI)) == 0
    okH = sp.expand(resc(Hm0(), MATS, fm) - Hm0().subs({ak: r * ak, c: c / r, mu: mu / r}, simultaneous=True)) == 0
    v2 = ak * c
    okv = sp.simplify(v2.subs({ak: r * ak, c: c / r}, simultaneous=True) - v2) == 0
    check("C10a", okG and okH and okv, "canonical point rescaling phi->phi/sqrt r, pi->sqrt r pi: G_m is INVARIANT (so lam_m cannot be moved by it), H_m maps to (ak, c, mu) -> (r ak, c/r, mu/r), and the cone v^2 = ak c is invariant")
    # gravity rescaling h -> rho h, P -> P/rho
    fg = {**{n: rho for n in HN.values()}, **{n: 1 / rho for n in PN.values()}}
    SR = sqrtg_R()
    R1 = sp.expand(SR).coeff(eps, 1)
    R2 = sp.expand(SR).coeff(eps, 2)
    okG1 = sp.expand(resc(G1(XI), GRAV, fg) - G1(XI) / rho) == 0
    okG2 = sp.expand(resc(G2(XI), GRAV, fg) - G2(XI)) == 0
    okk = sp.expand(resc(kin(), GRAV, fg) - kin().subs(al, rho ** 2 * al)) == 0
    okR = sp.expand(resc(R1, GRAV, fg) - rho * R1) == 0 and sp.expand(resc(R2, GRAV, fg) - rho ** 2 * R2) == 0
    okc = sp.expand(resc(Hm_g1(), GRAV, fg) - rho * Hm_g1()) == 0
    mp = {lam1: lam1 / rho, al: rho ** 2 * al, K1: rho * K1, K2: rho ** 2 * K2}
    inv_cone = sp.simplify((ak * cc[c]).subs(mp, simultaneous=True) - ak * cc[c]) == 0
    inv_gg = sp.simplify((K2 - gg[K2]).subs(mp, simultaneous=True) - (K2 - gg[K2]) * rho ** 2) == 0
    inv_a = sp.simplify((sp.Symbol("a_m") * rho - lamm / (lam1 / rho)) - rho * (sp.Symbol("a_m") - lamm / lam1)) == 0
    inv_w = sp.simplify((K2 / (4 * al)).subs(mp, simultaneous=True) - K2 / (4 * al)) == 0
    check("C10b", okG1 and okG2 and okk and okR and okc and inv_cone and inv_gg and inv_a and inv_w,
          "canonical rescaling h->rho h, P->P/rho maps the family to itself with lam1->lam1/rho, lam2 invariant, alpha->rho^2 alpha, K1->rho K1, K2->rho^2 K2, a_s->rho a_s; the relations of C5 (v_s^2 ~ lam_s K1/(alpha lam1)), C6 (a_s lam1 = lam_s), C7 (K2 lam1 = K1 lam2) and the graviton cone K2/(4 alpha) are all invariant: 'c = kappa' in B14's units is the invariant statement v_s^2 = a_s K1/(4 alpha)")


if __name__ == "__main__":
    c1()
    c2()
    c3()
    c4()
    cc = c5()
    cm = c6()
    gg, w2 = c7()
    c9(cc, gg, w2)
    c10(cc, cm, gg)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
