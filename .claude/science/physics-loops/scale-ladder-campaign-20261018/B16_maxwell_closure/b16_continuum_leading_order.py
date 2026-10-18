#!/usr/bin/env python3
"""B16 leading order (continuum / long-wavelength form of the lattice model): exact sympy jet calculus in 3D.

Reuses B14's continuum machinery (b14_continuum_leading_order.py: jets, total derivative, Euler operator,
density bracket, gravity densities kin / R1 / G_g, scalar H_m / G_m / coupling ansatz / l3()).

SUPPLIED (premises): a U(1) one-form A_i with conjugate vector density E^i,
   H_EM(N) = int N [ (g^2/2) E.E + (cB/(2 g^2)) sum_{i<j} F_ij^2 ],   F_ij = d_i A_j - d_j A_i,
   gauge-covariant relabelling ("Poynting") P_A[xi] = int xi^i E^j F_ij,
   pure Lie-derivative relabelling G_Lie[xi] = int E^j (xi^i d_i A_j + A_i d_j xi^i),
   Gauss[theta] = int theta d_j E^j;  gravity and scalar exactly as in B14.
   Coupling ansatz (Maxwell): int N sum_{6 strain components h_c} h_c Q_c(E,F), with Q_c a GENERAL quadratic
   form in the six variables (E1,E2,E3,F12,F13,F23): 6 x 21 = 126 free coefficients (no isotropy, no parity,
   no derivative terms).
"mod Gauss" = identity required on div E = 0 (jets of E3 with a d_3 eliminated): equivalent to allowing
Gauss terms with arbitrary local multipliers.

Checks:
 M0  comparator: O(h) part of the metric-covariant H_EM(g) (E a vector density, A a one-form).
 M1  {C(N),C(M)} at O(eps), C = kin - K R1 + H_EM: = G_g[xi0] + P_A[xi0] (exactly, no Gauss needed)
     iff cB = K/(4 alpha), for every g.
 M1b with G_Lie instead of P_A: fails without Gauss; = G_g + G_Lie[xi0] + Gauss[r xi0.A] with r forced.
 M2  {G[xi], C(N)} at O(E^2, F^2) with the 126-parameter coupling, RHS H_EM(s1 xi.grad N + s2 N div xi), mod Gauss.
 M3  {C,C} at O(h E F): structure function xi' = kappa (r1 h + r2 tr h) xi0, mod Gauss; M3b T = 0 also solves.
 M4  scalar-lapse rule s2 = 0: coupling unique = Maxwell metric stress; r1 = -1, r2 = 0.
 M5  s2 = 2 lam: r2 = -2 lam (same function as the scalar in B14 L5).
 M6  scalar + Maxwell together, shared N' (s1,s2) and shared structure function (r1,r2): O(eps) closes iff
     c = cB = kappa; the coupled solution is both metric stresses with ONE common lam.
 M7  Gauss in the algebra: {Gauss, C(N)} = 0 = {Gauss, P_A}; {P_A[xi],P_A[eta]} = a P_A[[xi,eta]] + b Gauss[F_ij xi^i eta^j]
     with b != 0; {G_Lie[xi],G_Lie[eta]} = a' G_Lie[[xi,eta]] with no Gauss term; {Gauss[theta], G_Lie[xi]} = Gauss[d xi.grad theta].
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "B14_gravity_noether_source", "b14_continuum_leading_order.py")
_spec = importlib.util.spec_from_file_location("b14c", P)
b = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b)

J, D, euler, bracket, grad, refresh = b.J, b.D, b.euler, b.bracket, b.grad, b.refresh
coeff_equations, zero_in_lapse = b.coeff_equations, b.zero_in_lapse
DIM, PAIRS, HD, HF, CONJ = b.DIM, b.PAIRS, b.HD, b.HF, b.CONJ
al, K, c, mu = b.al, b.K, b.c, b.mu
N, M = b.N, b.M
XI = b.XI
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


AN = [f"A{k}" for k in range(DIM)]
EN = [f"E{k}" for k in range(DIM)]
for k in range(DIM):
    CONJ[AN[k]] = EN[k]
g2, cB = sp.symbols("g2 cB", positive=True)
kappa = K / (4 * al)


def e1(k):
    return tuple(1 if l == k else 0 for l in range(DIM))


def Fij(i, j):
    return J(AN[j], e1(i)) - J(AN[i], e1(j))


EV = [J(n) for n in EN]
FV = {ij: Fij(*ij) for ij in PAIRS}


def hem_density(cb=None):
    cb = cB if cb is None else cb
    return g2 / 2 * sum(e ** 2 for e in EV) + cb / (2 * g2) * sum(f ** 2 for f in FV.values())


def poynting(xi):
    return sum(xi[i] * J(EN[j]) * Fij(i, j) for i in range(DIM) for j in range(DIM) if i != j)


def lie_gen(xi_names):
    out = 0
    for j in range(DIM):
        out += J(EN[j]) * sum(J(xi_names[i]) * J(AN[j], e1(i)) + J(AN[i]) * J(xi_names[i], e1(j)) for i in range(DIM))
    return out


def lie_gen_vec(xi):
    """Lie generator for a composite vector xi given as expressions."""
    out = 0
    for j in range(DIM):
        out += J(EN[j]) * sum(xi[i] * J(AN[j], e1(i)) + J(AN[i]) * D(xi[i], j) for i in range(DIM))
    return out


def divE():
    return sum(J(EN[k], e1(k)) for k in range(DIM))


def on_gauss(expr):
    """restrict to d_k E^k = 0: eliminate every jet of E2 carrying a d_2."""
    expr = sp.expand(expr)
    while True:
        refresh()
        subs = {}
        for s in expr.free_symbols:
            key = b.SYM2KEY.get(s)
            if key and key[0] == EN[2] and key[1][2] >= 1:
                a = list(key[1])
                a0, a1 = list(a), list(a)
                a0[2] -= 1
                a0[0] += 1
                a1[2] -= 1
                a1[1] += 1
                subs[s] = -J(EN[0], a0) - J(EN[1], a1)
        if not subs:
            return expr
        expr = sp.expand(expr.xreplace(subs))


def eqs_of(expr):
    if sp.expand(expr) == 0:
        return []
    return [e for e in coeff_equations(expr, []) if e != 0]


def gg_composite(xi):
    out = 0
    for j in range(DIM):
        out += J(b.PD[j]) * 2 * D(xi[j], j)
    for (i, j) in PAIRS:
        out += J(b.PF[(i, j)]) * (D(xi[j], i) + D(xi[i], j))
    return out


XI0 = [N * gm - M * gn for gn, gm in zip(grad("N"), grad("M"))]
HV = [J(HD[j]) for j in range(DIM)] + [J(HF[ij]) for ij in PAIRS]
FPH = {ij: sp.Symbol(f"Fph{ij[0]}{ij[1]}") for ij in PAIRS}  # placeholders for F_ij (F is not a jet symbol)
TOFV = {FPH[ij]: FV[ij] for ij in PAIRS}
VARS6 = EV + [FPH[ij] for ij in PAIRS]
MONOS = [VARS6[a] * VARS6[bb] for a in range(6) for bb in range(a, 6)]
QC = [[sp.Symbol(f"q{cmp}_{k}") for k in range(len(MONOS))] for cmp in range(6)]
QALL = [s for row in QC for s in row]


def em_coupling():
    return sp.expand(sum(HV[cmp] * sum(QC[cmp][k] * MONOS[k] for k in range(len(MONOS))) for cmp in range(6)).xreplace(TOFV))


def expected_stress():
    eps = sp.Symbol("eps")
    hs = sp.symbols("h00 h11 h22 h01 h02 h12")
    g = sp.Matrix([[1 + eps * hs[0], eps * hs[3], eps * hs[4]], [eps * hs[3], 1 + eps * hs[1], eps * hs[5]], [eps * hs[4], eps * hs[5], 1 + eps * hs[2]]])
    Ev = sp.Matrix(EV)
    Fm = sp.zeros(3, 3)
    for (i, j), f in FPH.items():
        Fm[i, j] = f
        Fm[j, i] = -f
    gi = g.inv()
    sq = sp.sqrt(g.det())
    hem = g2 / 2 * (Ev.T * g * Ev)[0, 0] / sq + cB / (4 * g2) * sq * (gi * Fm * gi * Fm.T).trace()
    lin = sp.expand(sp.series(hem, eps, 0, 2).removeO().coeff(eps, 1))
    zeroth = sp.expand(sp.series(hem, eps, 0, 1).removeO())
    return sp.expand(lin.subs(dict(zip(hs, HV)))), sp.expand(zeroth)  # in placeholders FPH


def coupling_values(dens):
    """coefficients q of a coupling density in the ansatz basis"""
    vals = {}
    poly = sp.Poly(sp.expand(dens), *(HV + VARS6))
    for cmp in range(6):
        for k, mono in enumerate(MONOS):
            vals[QC[cmp][k]] = sp.expand(poly.coeff_monomial(HV[cmp] * mono)) if True else 0
    return vals


s1, s2, r1, r2 = b.s1, b.s2, b.r1, b.r2
lam = sp.Symbol("lam")


def m0():
    lin, zeroth = expected_stress()
    ok = sp.simplify(zeroth.xreplace(TOFV) - hem_density()) == 0
    trh = sum(J(HD[j]) for j in range(DIM))
    # the familiar form: (g^2/2)(h_ij E^i E^j - trh E^2/2) + (cB/g^2)(trh B^2/4 - (1/2) h_ij F_ik F_jk)
    Hm = [[None] * 3 for _ in range(3)]
    for j in range(3):
        Hm[j][j] = J(HD[j])
    for (i, j) in PAIRS:
        Hm[i][j] = Hm[j][i] = J(HF[(i, j)])
    Fm = [[0] * 3 for _ in range(3)]
    for (i, j), f in FPH.items():
        Fm[i][j], Fm[j][i] = f, -f
    form = g2 / 2 * (sum(Hm[i][j] * EV[i] * EV[j] for i in range(3) for j in range(3)) - trh * sum(e ** 2 for e in EV) / 2) \
        + cB / g2 * (trh * sum(f ** 2 for f in FPH.values()) / 4 - sp.Rational(1, 2) * sum(Hm[i][j] * Fm[i][k] * Fm[j][k] for i in range(3) for j in range(3) for k in range(3)))
    ok2 = sp.expand(lin - form) == 0
    check("M0", ok and ok2, "comparator: H_EM(g) = (g^2/2) g_ij E^i E^j/sqrt(g) + (cB/4g^2) sqrt(g) g^ik g^jl F_ij F_kl reduces to H_EM at h=0; O(h) part = (g^2/2)(h_ij E^iE^j - trh E^2/2) + (cB/g^2)(trh sum_{i<j}F^2/4 - h_ij F_ik F_jk/2)")
    return lin


def m1():
    CN = N * (b.kin_density() - K * b.r1_density() + hem_density())
    CM = M * (b.kin_density() - K * b.r1_density() + hem_density())
    br = bracket(CN, CM)
    xi = [kappa * x for x in XI0]
    res = zero_in_lapse(br - gg_composite(xi) - poynting(xi), "N")
    eqs = eqs_of(res)
    sol = sp.solve(eqs, cB, dict=True)
    check("M1", sol == [{cB: K / (4 * al)}], f"{{C(N),C(M)}} = G_g[xi0] + P_A[xi0], xi0 = kappa (N grad M - M grad N), exactly (no Gauss term) iff cB = K/(4 alpha); g drops out (photon speed^2 = g^2 * cB/g^2); solve -> {sol}")
    # with the Lie generator
    rr = sp.Symbol("rr")
    xa = sum(xi[k] * J(AN[k]) for k in range(DIM))
    base = br.subs(cB, kappa) - gg_composite(xi) - lie_gen_vec(xi)
    res0 = zero_in_lapse(base, "N")
    fails = bool(eqs_of(res0))
    on_g = not eqs_of(on_gauss(sp.expand(res0)))
    resr = zero_in_lapse(base - rr * xa * divE(), "N")
    solr = sp.solve(eqs_of(resr), rr, dict=True)
    check("M1b", fails and on_g and len(solr) == 1 and abs(solr[0][rr]) == 1,
          f"with G_Lie: {{C,C}} - G_g[xi0] - G_Lie[xi0] != 0 exactly ({fails}) but vanishes on div E = 0 ({on_g}); exactly = Gauss[r xi0.A] with r solved: {solr} (the Gauss constraint enters with an A-dependent structure function)")
    return solr


def l2_maxwell_eqs():
    xi = [J(n) for n in XI]
    br = bracket(poynting(xi), N * hem_density()) + bracket(b.g_grav_density(XI), N * em_coupling())
    nprime = s1 * sum(xi[k] * grad("N")[k] for k in range(DIM)) + s2 * N * sum(J(XI[k], e1(k)) for k in range(DIM))
    res = zero_in_lapse(br - nprime * hem_density(), "N")
    return eqs_of(on_gauss(res)), eqs_of(res)


def l3_maxwell_eqs():
    hm = hem_density(kappa)
    coup = em_coupling()
    br = bracket(N * coup, M * hm) + bracket(N * hm, M * coup)
    H = [[None] * DIM for _ in range(DIM)]
    for j in range(DIM):
        H[j][j] = J(HD[j])
    for (i, j) in PAIRS:
        H[i][j] = H[j][i] = J(HF[(i, j)])
    trh = sum(H[j][j] for j in range(DIM))
    xip = [kappa * sum((r1 * H[i][j] + (r2 * trh if i == j else 0)) * XI0[j] for j in range(DIM)) for i in range(DIM)]
    res = zero_in_lapse(br - poynting(xip), "N")
    return eqs_of(on_gauss(res))


def m7():
    th = J("theta")
    xi = [J(n) for n in XI]
    ETA = [f"eta{k}" for k in range(DIM)]
    eta = [J(n) for n in ETA]
    gth = th * divE()
    ok1 = sp.expand(euler(bracket(gth, N * hem_density()), "theta")) == 0
    lin, _ = expected_stress()
    ok2 = sp.expand(euler(bracket(gth, N * lin.xreplace(TOFV)), "theta")) == 0
    ok3 = sp.expand(euler(bracket(gth, poynting(xi)), "theta")) == 0
    check("M7a", ok1 and ok2 and ok3, "Gauss first class: {Gauss[theta], N H_EM} = {Gauss[theta], N h.T_stress} = {Gauss[theta], P_A[xi]} = 0 identically")
    comm = [sum(xi[j] * J(ETA[i], e1(j)) - eta[j] * J(XI[i], e1(j)) for j in range(DIM)) for i in range(DIM)]
    a_, b_ = sp.symbols("a_ b_")
    fxe = sum(xi[i] * eta[j] * Fij(i, j) for i in range(DIM) for j in range(DIM) if i != j)
    res = bracket(poynting(xi), poynting(eta)) - a_ * poynting(comm) - b_ * fxe * divE()
    eqs = []
    for n in ETA:
        eqs += eqs_of(euler(res, n))
    sol = sp.solve(eqs, [a_, b_], dict=True)
    okP = len(sol) == 1 and sol[0][b_] != 0 and abs(sol[0][a_]) == 1
    check("M7b", okP, f"{{P_A[xi], P_A[eta]}} = a P_A[[xi,eta]] + b Gauss[F_ij xi^i eta^j] with (a, b) = {sol}: the gauge-covariant generators close only up to the Gauss constraint with an F-dependent structure function")
    res2 = bracket(lie_gen(XI), lie_gen(ETA)) - a_ * lie_gen_vec(comm)
    eqs2 = []
    for n in ETA:
        eqs2 += eqs_of(euler(res2, n))
    sol2 = sp.solve(eqs2, [a_], dict=True)
    res3 = bracket(gth, lie_gen(XI)) - b_ * sum(xi[k] * J("theta", e1(k)) for k in range(DIM)) * divE()
    sol3 = sp.solve(eqs_of(euler(res3, "theta")), [b_], dict=True)
    check("M7c", len(sol2) == 1 and abs(sol2[0][a_]) == 1 and len(sol3) == 1 and abs(sol3[0][b_]) == 1,
          f"{{G_Lie[xi], G_Lie[eta]}} = a' G_Lie[[xi,eta]] with no Gauss term, a' = {sol2}; {{Gauss[theta], G_Lie[xi]}} = b' Gauss[xi.grad theta], b' = {sol3} (Gauss is an ideal; the Lie generators are a subalgebra)")


if __name__ == "__main__":
    lin = m0()
    m1()
    eqs2g, eqs2x = l2_maxwell_eqs()
    sol2 = sp.solve(eqs2g, QALL + [s1, s2], dict=True)
    print("M2: number of solutions", len(sol2))
    exp_vals = coupling_values(lin)
    trh = sum(J(HD[j]) for j in range(DIM))
    hem_ph = g2 / 2 * sum(e ** 2 for e in EV) + cB / (2 * g2) * sum(f ** 2 for f in FPH.values())
    lam_vals = coupling_values(sp.expand(lam * trh * hem_ph))
    ok2 = False
    if len(sol2) == 1:
        s = sol2[0]
        free = sorted(set(QALL + [s1, s2]) - set(s.keys()), key=str)
        print("   free parameters:", free)
        if len(free) == 1:
            # express in lam via s2 = -2 lam
            sub = {free[0]: sp.solve(sp.Eq(sp.sympify(s.get(s2, s2)), -2 * lam), free[0])[0]}
            full = {k: sp.simplify(sp.sympify(s.get(k, k)).subs(sub)) for k in QALL + [s1, s2]}
            ok2 = all(sp.simplify(full[k] - exp_vals[k] - lam_vals[k]) == 0 for k in QALL) and full[s1] == 1
    check("M2", ok2, "{G[xi], C(N)} at O(E^2,F^2) = H_EM(s1 xi.grad N + s2 N div xi) mod Gauss, over the 126-parameter coupling: ONE-parameter family = Maxwell metric stress (M0) + lam tr h H_EM, with s1 = 1, s2 = -2 lam")
    # where Gauss enters {G,C}: with the metric stress (lam = 0, s1 = 1, s2 = 0)
    xiv = [J(n) for n in XI]
    coup_exp = lin.xreplace(TOFV)
    rr = sp.Symbol("rr")
    xE = sum(xiv[k] * J(EN[k]) for k in range(DIM))
    npr = sum(xiv[k] * grad("N")[k] for k in range(DIM))
    out = {}
    for name, gen in (("P_A", poynting(xiv)), ("G_Lie", lie_gen(XI))):
        brx = bracket(gen, N * hem_density()) + bracket(b.g_grav_density(XI), N * coup_exp)
        exact = not eqs_of(zero_in_lapse(brx - npr * hem_density(), "N"))
        rsol = sp.solve(eqs_of(zero_in_lapse(brx - npr * hem_density() - rr * g2 * N * xE * divE(), "N")), rr, dict=True)
        out[name] = (exact, rsol)
    print("M2b {generator: (closes exactly without Gauss, Gauss multiplier r in Gauss[r g^2 N xi.E])}:", out)
    check("M2b", out["P_A"][0] is False and out["P_A"][1] == [{rr: 1}] and out["G_Lie"][0] is True and out["G_Lie"][1] == [{rr: 0}],
          "where Gauss enters {G,C}: with the metric stress, {P_A[xi], C(N)} = H_EM(xi.grad N) + Gauss[g^2 N xi.E] exactly (an E-dependent Gauss multiplier), while {G_Lie[xi], C(N)} = H_EM(xi.grad N) with no Gauss term; for {C,C} it is the reverse (M1, M1b). Either way the algebra closes only with Gauss first class")
    eqs3 = l3_maxwell_eqs()
    zero = {v: 0 for v in QALL + [r1, r2]}
    check("M3b", all(sp.simplify(e.subs(zero)) == 0 for e in eqs3), "{C,C} alone does not force a coupling: T = 0, xi' = 0 solves the h E F order (as for the scalar: the source is fixed by {G,C})")
    eqs2k = [sp.expand(e.subs(cB, kappa)) for e in eqs2g]
    sol4 = sp.solve([e.subs(s2, 0) for e in eqs2k] + eqs3, QALL + [s1, r1, r2], dict=True)
    expk = {k: sp.expand(v.subs(cB, kappa)) for k, v in exp_vals.items()}
    ok4 = len(sol4) == 1 and all(sp.simplify(sp.sympify(sol4[0].get(k, k)) - expk[k]) == 0 for k in QALL) and sol4[0].get(r1) == -1 and sol4[0].get(r2) == 0 and sol4[0].get(s1) == 1
    check("M4", ok4, f"scalar-lapse rule s2 = 0: coupling UNIQUE = Maxwell metric stress at cB = kappa, structure function forced r1 = -1, r2 = 0 (g^ij = delta - h, as for the scalar); (r1, r2) = ({sol4[0].get(r1) if sol4 else None}, {sol4[0].get(r2) if sol4 else None})")
    sol5 = sp.solve([e.subs(s2, 2 * lam) for e in eqs2k] + eqs3, QALL + [s1, r1, r2], dict=True)
    r2l = sp.simplify(sol5[0].get(r2, r2)) if len(sol5) == 1 else None
    check("M5", len(sol5) == 1 and r2l == -2 * lam and sol5[0].get(r1) == -1, f"s2 = 2 lam: r2 = {r2l} = -s2, r1 = -1 (B14 L5 gives r2 = -2 lam for the scalar at the same s2: identical function, so a common structure function needs a common lam)")
    # M6 combined scalar + Maxwell
    CN = N * (b.kin_density() - K * b.r1_density() + b.hm_density() + hem_density())
    CM = M * (b.kin_density() - K * b.r1_density() + b.hm_density() + hem_density())
    br = bracket(CN, CM)
    xi = [kappa * x for x in XI0]
    res = zero_in_lapse(br - gg_composite(xi) - poynting(xi) - b.g_matter_density(xi), "N")
    solc = sp.solve(eqs_of(res), [c, cB], dict=True)
    xiv = [J(n) for n in XI]
    brs = bracket(b.g_matter_density(xiv), N * b.hm_density()) + bracket(b.g_grav_density(XI), N * b.coupling_density())
    nprime = s1 * sum(xiv[k] * grad("N")[k] for k in range(DIM)) + s2 * N * sum(J(XI[k], e1(k)) for k in range(DIM))
    eqs_s2 = [sp.expand(e.subs(c, kappa)) for e in eqs_of(zero_in_lapse(brs - nprime * b.hm_density(), "N"))]
    eqs_s3 = b.l3()
    unk = list(b.A) + list(b.B) + QALL + [s1, s2, r1, r2]
    solall = sp.solve(eqs_s2 + eqs_s3 + eqs2k + eqs3, unk, dict=True)
    ok6 = len(solc) == 1 and solc[0] == {c: kappa, cB: kappa} and len(solall) == 1
    if ok6:
        s = solall[0]
        free = sorted(set(unk) - set(s.keys()), key=str)
        print("M6 combined free parameters:", free)
        ok6 = len(free) == 1 and sp.simplify(sp.sympify(s.get(r1, r1)) + 1) == 0
        if ok6:
            sub = {free[0]: sp.solve(sp.Eq(sp.sympify(s.get(s2, s2)), -2 * lam), free[0])[0]}
            full = {k: sp.simplify(sp.sympify(s.get(k, k)).subs(sub)) for k in unk}
            ok6 = all(sp.simplify(full[k] - expk[k] - lam_vals[k].subs(cB, kappa)) == 0 for k in QALL) and sp.simplify(full[b.A[0]] - (-sp.Rational(1, 4) + lam / 2)) == 0 and sp.simplify(full[r2] - 2 * lam) == 0
    check("M6", ok6, f"scalar + Maxwell with shared N' and shared structure function: O(eps) {{C,C}} closes iff (c, cB) = (kappa, kappa) [{solc}]; the coupled solution space is ONE parameter: both species get their metric stress plus the SAME lam tr h H (s2 = -2 lam, r1 = -1, r2 = 2 lam = -s2, matching M5's r2 = -s2)")
    m7()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
