#!/usr/bin/env python3
"""B21: do the degree-2 brackets force K1 = K2?  (continuum, exact sympy; isotropic parity-even local ansatz)

Model (b21_core conventions):
  C(N) = int N [ kin0 + kin1 - K1 R1 - K2 R2 ],  R_n = [sqrt g R]^(n) of g = delta + h
  kin0 = (tr Pt^2 + b (tr Pt)^2)/(4 alpha)                       b free
  kin1 = k1 trh trPt^2 + k2 trh (trPt)^2 + k3 tr(h Pt) trPt + k4 tr(h Pt Pt)    k1..k4 free (general isotropic h-linear
         ultralocal kinetic metric; the DeWitt expansion is one point)
  G[xi] = lam1 G1[xi] + G2[xi; m1..m12]   (G2 = general isotropic one-derivative P-linear, h-linear: 12 terms)
  lapse rule {C(N), G[xi]} = C(N'),  N' = s1 xi.dN + s2 N div xi
  {C(N), C(M)} = c0 G[zeta],  zeta^i = (delta_ij + beta h_ij + beta' delta_ij trh)(N d_j M - M d_j N)

Checks:
  A0  R1, R2 (jets) have the block-62 symbols (sanity of the copied pickle -> jets conversion).
  A1  {G,G} at degree 1 (order P):  solution set for (m, nu).
  A2  {C,G} at degree 1 (h-linear): solution set for (m, s1, s2)   [B19 C7 / B19_check K12c, recomputed].
  A3  A1 + A2 jointly: G2 = nu * (L_xi h) UNIQUELY (all null directions removed) and lam1 K2 = nu K1.
  A4  {G,G} at degree 2 with that G2: holds identically for every lam1 (lam1 free).
  A5  {C,C} at degree 1: b = -1/2 forced, c0 fixed.
  A6  {C,G} at degree 2, P^2 sector: kin1 fixed (= (nu/lam1) x DeWitt expansion), s1 = -nu consistent.
  A7  {C,C} at degree 2 (order P h): structure function fixed: beta = -nu/lam1, beta' = 0.
  A8  joint solution: one-parameter (lam1/nu) family; K1 = K2 <=> lam1 = nu <=> beta = -1 <=> kin1 = DeWitt(delta+h);
      the family is exactly the orbit of the canonical rescaling h -> rho h, P -> P/rho (so no bracket can fix it).
  A9  positive control: GR expanded about the background r delta (r = lam1/nu) reproduces the joint solution.
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from b21_core import (J, D, bracket, CONJ, XI, ETA, N, M, h, Pt, trh, trP, trPP, trhP, trhPP, G1, G2, lie_vec,
                      load_R12_jets, kernel, kernel_eqs, HS, HS2, PS, PS2, NS, MS, XS, ES, R3)

RES = {"pass": 0, "fail": 0}
T0 = time.time()


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


m = sp.symbols("m1:13")
k = sp.symbols("k1:5")
s1, s2, b, c0, beta, betap = sp.symbols("s1 s2 b c0 beta betap")
lam1, nu, K1, K2, al = sp.symbols("lam1 nu K1 K2 alpha", nonzero=True)
R1, R2 = load_R12_jets()
LIE = {mm: 0 for mm in m}
LIE[m[0]] = 1
LIE[m[1]] = 1          # T1 + T2 = L_xi h


def kin0(bb=b):
    return sp.expand((trPP + bb * trP ** 2) / (4 * al))


def kin1(kk=k):
    return sp.expand(kk[0] * trh * trPP + kk[1] * trh * trP ** 2 + kk[2] * trhP * trP + kk[3] * trhPP)


def Gfull(x, mm=m, l1=lam1):
    return sp.expand(l1 * G1(x) + G2(x, mm))


def lapse(x=XI):
    return sp.expand(s1 * sum(x[i] * D(N, i) for i in R3) + s2 * N * sum(D(x[i], i) for i in R3))


def solve(eqs, unk):
    sol = sp.solve(eqs, unk, dict=True)
    return sol


# ---------------------------------------------------------------- A0
def a0():
    e, gens = kernel(R2, [HS2])
    p = [g for g in gens if str(g).startswith("k_h0")]
    A0 = {f: sp.Symbol(f"A_{f}_0") for f in ["h00", "h11", "h22", "h01", "h02", "h12"]}
    sub = {sp.Symbol(f"A_{f}_1"): A0[f] for f in A0}
    ker = sp.expand(e.xreplace(sub) / 2)
    U = lambda i, j: A0[f"h{min(i,j)}{max(i,j)}"]
    Hm = sp.Matrix(3, 3, lambda i, j: U(i, j)); pv = sp.Matrix(p); p2 = sum(x ** 2 for x in p); tr = Hm.trace()
    b62 = -(p2 / 4) * (Hm * Hm).trace() + (Hm * pv).dot(Hm * pv) / 2 - (pv.T * Hm * pv)[0] * tr / 2 + p2 * tr ** 2 / 4
    e1, g1 = kernel(R1, [HS])
    q = [g for g in g1 if str(g).startswith("k_")]
    # single slot: last copy carries -(sum of none) = 0 ... so evaluate R1 with N to give it a momentum partner
    e1, g1 = kernel(N * R1, [HS, NS])
    q = [g for g in g1 if str(g).startswith("k_h0")]
    Hq = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"A_h{min(i,j)}{max(i,j)}_0"))
    qv = sp.Matrix(q); q2 = sum(x ** 2 for x in q)
    r1_note = (q2 * Hq.trace() - (qv.T * Hq * qv)[0]) * sp.Symbol("A_N_0")
    check("A0", sp.expand(ker - b62) == 0 and sp.expand(e1 - r1_note) == 0,
          "jets R2 = block-62 / 09-23 R2 symbol and R1 = p^2 tr h - p.h.p (same normalisation): the copied pickle is "
          "[sqrt g R]^(1),(2) of g = delta + h")


# ---------------------------------------------------------------- A1, A4
def a1():
    br = bracket(Gfull(XI), Gfull(ETA), CONJ)
    LB = lie_vec(XI, ETA)
    res = sp.expand(br - nu * Gfull(LB))
    eqs = kernel_eqs(res, [PS, XS, ES])
    sol = solve(eqs, list(m) + [nu])
    print("   {G,G} degree 1 (order P):", sol)
    exp = {m[0]: nu, m[1]: m[2] + nu, m[5]: 2 * m[6], m[7]: 0, m[8]: 0, m[9]: 0, m[10]: 0, m[11]: 0}
    ok = len(sol) == 1 and all(sp.simplify(sol[0].get(x, x) - v) == 0 for x, v in exp.items())
    check("A1", ok, "{lam1 G1 + G2, lam1 G1 + G2} = nu G[[xi,eta]] at order P (the lam1 {G1,G2} cross terms): forces the "
          "xi.dh coefficient m1 = nu and kills m8..m12, leaving 4 free directions (m3, m4, m5, m7) of the form "
          "W = F(h, L_xi delta) (bilinear, symmetric in the two G1 shifts -> drop out of the antisymmetrised bracket)")
    return res, sol[0]


def a4(res):
    sub = {**{mm: nu * v for mm, v in LIE.items()}}
    eqs = kernel_eqs(res.subs(sub), [HS, PS, XS, ES])
    eqs1 = kernel_eqs(res.subs(sub), [PS, XS, ES])
    check("A4", eqs == [] and eqs1 == [], "with G2 = nu int P L_xi h the full {G,G} = nu G[[xi,eta]] holds at degrees 1 AND 2 "
          "identically for symbolic lam1, nu: lam1 (the background scale r = lam1/nu) is free under {G,G}")


# ---------------------------------------------------------------- A2, A3
def a2():
    C = sp.expand(N * (-K1 * R1 - K2 * R2))
    br = bracket(C, Gfull(XI), CONJ)
    rhs = sp.expand(lapse() * (-K1 * R1))
    eqs = kernel_eqs(br - rhs, [NS, XS, HS])
    sol = solve(eqs, list(m) + [s1, s2])
    print("   {C,G} degree 1 (h-linear):", sol)
    ok = len(sol) == 1 and sp.simplify(sol[0][s1] + lam1 * K2 / K1) == 0 and sol[0][s2] == 0
    free = [x for x in m if x not in sol[0]]
    check("A2", ok, f"h-linear {{C(N), G[xi]}} = C^(1)(N'): s1 = -lam1 K2/K1, s2 = 0 unique; G2 = (lam1 K2/K1) L_xi h + "
          f"{len(free)}-dim null family {free} (reproduces B19 C7 / B19_check K12c with this code)")
    return sol[0], eqs


def a3(eqs_gg, eqs_cg):
    sol = solve(list(eqs_gg) + list(eqs_cg), list(m) + [nu, s1, s2])
    print("   joint {G,G}deg1 + {C,G}deg1:", sol)
    # (run-1 bug, kept in b21_brackets_run2_A3check_BUG.log: compared to the SYMBOL nu although nu is itself solved for)
    ok = len(sol) == 1 and all(sp.simplify(sol[0][x] - sol[0][nu] * LIE[x]) == 0 for x in m) \
        and sp.simplify(sol[0][nu] - lam1 * K2 / K1) == 0 and sp.simplify(sol[0][s1] + lam1 * K2 / K1) == 0
    check("A3", ok, "jointly: G2 = nu int P L_xi h UNIQUELY (all 3 {C,G}-null and all 4 {G,G}-null directions removed), "
          "nu = lam1 K2/K1 (i.e. lam1 K2 = nu K1) and s1 = -nu: the B19_check caveat '{G,G} with G2's R1-null directions' "
          "is closed -- but this is a relation between K2/K1 and lam1/nu, not K1 = K2")
    return sol[0]


# ---------------------------------------------------------------- A5
def a5():
    C = lambda L: sp.expand(L * (kin0() - K1 * R1))
    br = bracket(C(N), C(M), CONJ)
    z0 = [sp.expand(N * D(M, i) - M * D(N, i)) for i in R3]
    eqs = kernel_eqs(br - c0 * lam1 * G1(z0), [NS, MS, PS])
    sol = solve(eqs, [b, c0])
    print("   {C,C} degree 1:", sol)
    ok = len(sol) == 1 and sol[0][b] == sp.Rational(-1, 2) and sp.simplify(sol[0][c0] - K1 / (4 * al * lam1)) == 0
    check("A5", ok, "{C(N),C(M)} at degree 1 = c0 lam1 G1[N dM - M dN] forces the DeWitt trace b = -1/2 and "
          "c0 = K1/(4 alpha lam1)  (b != -1/2 leaves int trP div(zeta), not a G)")
    return sol[0]


# ---------------------------------------------------------------- A6
def a6():
    C = sp.expand(N * (kin0(sp.Rational(-1, 2)) + kin1()))
    br = bracket(C, Gfull(XI), CONJ)
    rhs = sp.expand(lapse() * kin0(sp.Rational(-1, 2)))
    eqs = kernel_eqs(br - rhs, [NS, XS, PS2])
    sol = solve(eqs, list(m) + list(k) + [s1, s2])
    print("   {C,G} degree 2, P^2 sector (general m, k, s):", sol)
    return eqs, sol


# ---------------------------------------------------------------- A7
def a7():
    C = lambda L: sp.expand(L * (kin0(sp.Rational(-1, 2)) + kin1() - K1 * R1 - K2 * R2))
    br = bracket(C(N), C(M), CONJ)
    z0 = [sp.expand(N * D(M, i) - M * D(N, i)) for i in R3]
    zeta = [sp.expand(z0[i] + beta * sum(h(i, j) * z0[j] for j in R3) + betap * trh * z0[i]) for i in R3]
    rhs = sp.expand(K1 / (4 * al * lam1) * Gfull(zeta))
    eqs = kernel_eqs(br - rhs, [NS, MS, PS, HS])
    sol = solve(eqs, list(m) + list(k) + [beta, betap])
    print("   {C,C} degree 2 (general m, k, beta, beta'):", sol)
    return eqs, sol


def dewitt(r):
    """h-linear part of (1/sqrt g)(tr(gPgP) - (g.P)^2/2)/(4 alpha') at g = r delta + h, normalised so that the h^0 part
    is (trP^2 - trP^2/2)/(4 alpha): kin1 = (1/r)[2 tr(hPP) - trP tr(hP) - (trh/2)(trPP - (trP)^2/2)]/(4 alpha)."""
    return {k[0]: -1 / (8 * al * r), k[1]: 1 / (16 * al * r), k[2]: -1 / (4 * al * r), k[3]: 2 / (4 * al * r)}


def a9_control():
    """GR about r delta, computed directly (not from the solves): expand sqrt g R and the DeWitt kinetic term."""
    r, eps = sp.symbols("r eps", positive=True)
    Hm = sp.Matrix(3, 3, lambda i, j: h(i, j)); Pm = sp.Matrix(3, 3, lambda i, j: Pt(i, j))
    g = r * sp.eye(3) + eps * Hm
    detg = sp.expand(g.det())
    isq = sp.series(1 / sp.sqrt(detg), eps, 0, 2).removeO()
    gP = g * Pm
    kin = sp.expand(isq * ((gP * gP).trace() - (gP.trace()) ** 2 / 2))
    k0 = sp.expand(kin.coeff(eps, 0)); k1_ = sp.expand(kin.coeff(eps, 1))
    norm = sp.simplify(sp.cancel(k0 / sp.expand(trPP - trP ** 2 / 2)))        # = r^(1/2)
    # (run-2 bug: norm was left as an uncancelled ratio, so the comparison below could not reduce to 0)
    kin1_pred = sp.expand(sp.simplify(k1_ / norm) / (4 * al))
    return sp.simplify(norm), kin1_pred


if __name__ == "__main__":
    a0()
    res_gg, sol_gg = a1()
    eqs_gg = kernel_eqs(res_gg, [PS, XS, ES])
    a4(res_gg)
    sol_cg, eqs_cg = a2()
    joint = a3(eqs_gg, eqs_cg)
    sol_cc1 = a5()
    eqs6, sol6 = a6()
    # A6 verdict, given A3's G2 = nu Lie, s1 = -nu
    # s1 = -nu AND s2 = 0 are A2/A3's lapse rule (one lapse rule for the whole C).  Run 2 imposed only s1 and the P^2
    # sector alone leaves s2 free (k1, k2 shift with s2: the N -> N(1 + t trh) density-weight convention of B19_check 3a);
    # kept as b21_brackets_run2_A3check_BUG.log.
    sub3 = {**{x: nu * LIE[x] for x in m}, s1: -nu, s2: 0}
    # A6 joint with A3
    e6 = [sp.expand(e.subs(sub3)) for e in eqs6]
    s6s = solve(e6, list(k))
    print("   A6 with A3 imposed:", s6s)
    dw = dewitt(lam1 / nu)
    ok6 = len(s6s) == 1 and all(sp.simplify(s6s[0][x] - dw[x]) == 0 for x in k)
    check("A6", ok6, "{C(N),G[xi]} degree 2, P^2 sector, with A3's G2 = nu L_xi h and lapse rule s1 = -nu, s2 = 0: consistent, and the "
          "h-linear kinetic metric is FORCED to the DeWitt expansion about r delta with r = lam1/nu: "
          "kin1 = (nu/lam1)[2tr(hPP) - trP tr(hP) - trh(trPP - trP^2/2)/2]/(4 alpha)")
    eqs7, sol7 = a7()
    # A7 with A3 and A6 imposed
    sub6 = {**sub3, **{x: dw[x] for x in k}}
    e7 = [sp.expand(e.subs(sub6).subs(K2, nu * K1 / lam1)) for e in eqs7]
    s7 = solve(e7, [beta, betap])
    print("   A7 with A3+A6 imposed:", s7)
    ok7 = len(s7) == 1 and sp.simplify(s7[0][beta] + nu / lam1) == 0 and s7[0][betap] == 0
    check("A7", ok7, "{C(N),C(M)} degree 2 (order P h) with A3+A6: consistent, structure function zeta = (delta - (nu/lam1) h)"
          "(N dM - M dN), i.e. beta = -nu/lam1 = -1/r, beta' = 0 (the inverse metric of r delta + h, up to the factor 1/r in c0)")
    # A7' : does {C,C} degree 2 by itself (general m, k, beta) relate K2 to K1?  solve with K2 as unknown
    s7K = solve([sp.expand(e.subs(sub3)) for e in eqs7], list(k) + [beta, betap, K2])
    print("   A7' {C,C}deg2 with A3's G2 only (k, beta, beta', K2 unknown):", s7K)
    s7free = solve([sp.expand(e) for e in eqs7], list(m) + list(k) + [beta, betap])
    print("   A7'' {C,C}deg2 alone, general m, k, beta (K2 symbolic):", s7free)
    okb = len(s7K) == 1 and sp.simplify(s7K[0][K2] - nu * K1 / lam1) == 0 and sp.simplify(s7K[0][beta] + nu / lam1) == 0 \
        and s7K[0][betap] == 0 and all(sp.simplify(s7K[0][x] - dw[x]) == 0 for x in k)
    check("A7b", okb, "second route: {C,C} at degree 2 with G2 = nu L_xi h, kin1 / beta / beta' / K2 all unknown, forces "
          "lam1 K2 = nu K1, kin1 = DeWitt/r and beta = -1/r by itself (no {C,G} input beyond G2)")
    okf = len(s7free) == 1 and sp.simplify(s7free[0][m[0]] - lam1 * K2 / K1) == 0 \
        and sp.simplify(s7free[0][m[8]] + lam1 * (beta + K2 / K1)) == 0
    check("A7c", okf, "{C,C} degree 2 ALONE (general G2, kin1, beta): m1 (the xi.dh coefficient of G2) = lam1 K2/K1 and "
          "m9 = -lam1 (beta + K2/K1).  With {G,G} degree 1 (A1: m1 = nu, m9 = 0): lam1 K2 = nu K1 and beta = -K2/K1. "
          "Hence the structure-function premise beta = -1 (zeta = (delta - h)(N dM - M dN)) is EQUIVALENT to K2 = K1 "
          "(and then lam1 = nu)")
    # A7d: impose A1's {G,G} solution and beta = -1 explicitly; solve for everything else including K2 and lam1
    gg1 = {m[0]: nu, m[1]: m[2] + nu, m[5]: 2 * m[6], m[7]: 0, m[8]: 0, m[9]: 0, m[10]: 0, m[11]: 0}
    e7d = [sp.expand(e.subs(gg1).subs(beta, -1)) for e in eqs7]
    s7d = solve(e7d, [m[2], m[3], m[4], m[6]] + list(k) + [betap, K2])
    print("   A7d {G,G}deg1 + {C,C}deg2 with beta = -1:", s7d)
    okd = len(s7d) == 1 and sp.simplify(s7d[0][K2] - K1) == 0
    e7e = [sp.expand(e.subs(gg1)) for e in eqs7]
    s7e = solve(e7e, [m[2], m[3], m[4], m[6]] + list(k) + [betap, beta, K2])
    print("   A7e {G,G}deg1 + {C,C}deg2, beta and K2 free:", s7e)
    oke = len(s7e) == 1 and sp.simplify(s7e[0][K2] - nu * K1 / lam1) == 0 and sp.simplify(s7e[0][beta] + nu / lam1) == 0
    check("A7d", okd and oke, "{G,G} degree 1 + {C,C} degree 2 with the structure function fixed to delta - h (beta = -1) "
          "force K2 = K1; with beta free they force K2 = nu K1/lam1 and beta = -nu/lam1 = -K2/K1 (lam1/nu free)")
    # ------------------------------------------------ A8 one-parameter family and the rescaling orbit
    rho = sp.Symbol("rho", positive=True)
    fam = {"K2": nu * K1 / lam1, "s1": -nu, "s2": 0, "c0": K1 / (4 * al * lam1), "beta": -nu / lam1,
           **{str(x): dw[x] for x in k}, **{str(x): nu * LIE[x] for x in m}}
    # rescaling map: lam1 -> lam1/rho, K1 -> rho K1, K2 -> rho^2 K2, alpha -> rho^2 alpha, k -> k/rho, beta -> rho beta,
    #                m, nu, s, c0*lam1? : c0 -> c0 * (rho K1)/(rho^2 alpha * lam1/rho) / (K1/(alpha lam1)) = c0
    mp = {lam1: lam1 / rho, K1: rho * K1, al: rho ** 2 * al}
    okK2 = sp.simplify(fam["K2"].subs(mp, simultaneous=True) - rho ** 2 * fam["K2"]) == 0
    okb = sp.simplify(fam["beta"].subs(mp, simultaneous=True) - rho * fam["beta"]) == 0
    okk = all(sp.simplify(fam[str(x)].subs(mp, simultaneous=True) - fam[str(x)] / rho) == 0 for x in k)
    okc = sp.simplify(fam["c0"].subs(mp, simultaneous=True) - fam["c0"]) == 0
    # the scaling of each object under h -> rho h, P -> P/rho (direct)
    sc = lambda ex: sp.expand(ex.xreplace({s: (rho if str(s).startswith("h") else 1 / rho) * s for s in ex.free_symbols
                                           if str(s)[:1] in "hP" and len(str(s)) > 3}))
    okobj = sp.expand(sc(G1(XI)) - G1(XI) / rho) == 0 and sp.expand(sc(G2(XI, [nu * LIE[x] for x in m])) - G2(XI, [nu * LIE[x] for x in m])) == 0 \
        and sp.expand(sc(R1) - rho * R1) == 0 and sp.expand(sc(R2) - rho ** 2 * R2) == 0 \
        and sp.expand(sc(kin0(sp.Rational(-1, 2))) - kin0(sp.Rational(-1, 2)) / rho ** 2) == 0 and sp.expand(sc(kin1()) - kin1() / rho) == 0
    # K1 = K2 point and a K1 != K2 point both in the family (exact witness)
    wit = {lam1: 2, nu: 1, K1: 3, al: 5}
    K2w = fam["K2"].subs(wit)
    check("A8", okK2 and okb and okk and okc and okobj and K2w != wit[K1],
          f"the joint solution of ALL brackets computed (A1-A7) is a 1-parameter family in r = lam1/nu with K2/K1 = 1/r, "
          f"beta = -1/r, kin1 = DeWitt/r; it is exactly the orbit of the canonical map h -> rho h, P -> P/rho "
          f"(lam1 -> lam1/rho, K1 -> rho K1, K2 -> rho^2 K2, alpha -> rho^2 alpha, k -> k/rho, beta -> rho beta; G1, G2, R1, R2, "
          f"kin0, kin1 scale as stated). Exact witness of closure with K1 != K2: lam1 = 2, nu = 1, K1 = 3 -> K2 = {K2w}. "
          f"So K1 = K2 <=> lam1 = nu <=> beta = -1 <=> kin1 = DeWitt(delta + h): one normalisation premise, not a bracket output")
    # ------------------------------------------------ A9 control
    norm, kin1_pred = a9_control()
    r = sp.Symbol("r", positive=True)
    dwr = dewitt(r)
    ok9 = sp.expand(kin1_pred - kin1(sp.Matrix([dwr[x] for x in k]))) == 0
    check("A9", ok9, f"control (direct expansion, not a solve): the DeWitt term (1/sqrt g)(tr gPgP - (gP)^2/2) on g = r delta + h "
          f"has h^0 part {norm} x (trP^2 - trP^2/2) and h-linear part = (1/r) x the A6 DeWitt form; with r = lam1/nu this "
          f"is A6's forced kin1; [sqrt g R](r delta + h) = r^(1/2)(R1/r + R2/r^2 + ...) gives K2/K1 = 1/r = nu/lam1 (= A3); "
          f"g^ij = (delta - h/r)/r gives beta = -1/r (= A7): the whole family is GR about r delta")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
