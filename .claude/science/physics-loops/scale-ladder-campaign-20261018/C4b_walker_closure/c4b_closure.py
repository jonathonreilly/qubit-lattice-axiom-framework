#!/usr/bin/env python3
"""C4b: closure of the curvature member with the repo's walker (frame-coupled Weyl half-density) as the matter sector.

Continuum, flat background, leading orders.  Engine: ../B21_check/kb.py (Fourier kernels) + c4b_core spinor extension.
Usage: python3 c4b_closure.py [sections]   sections from T0 A B C D E F (default: all)
"""
from __future__ import annotations
import sys, random
from c4b_core import *

SEC = sys.argv[1:] or ["T0", "A", "B", "C", "D", "E", "F"]
lam1, nu, K1, K2, al, lf, v = sp.symbols("lam1 nu K1 K2 alpha lam_f v", positive=True)
s1, s2, b, c0, beta, betap, aS = sp.symbols("s1 s2 b c0 beta betap a_s", real=True)
R1, R2 = sqrtgR_12()
L = lb(XI, ETA)

# =====================================================================================================================
if "T0" in SEC:
    F1, F2 = functional(Sv[1]), functional(Sv[2])
    ok = is_zero(fadd(pb(F1, F2), functional(Sv[3]), coeffs=[1, -2]))
    # x-dependent: {int N n, int M J_{0,0}} = -i chibar [N, M p_0 sym] chi ... = int (M d_0 N) n ... checked against hand value
    lhs = pb(functional(N * Sv[0]), functional(M * Jv[0][0]))
    ok2 = is_zero(fadd(lhs, functional(M * Dk(N, 0) * Sv[0]), coeffs=[1, 1]))
    check("T0a", ok and ok2, "spinor bracket controls: {int s_1, int s_2} = 2 int s_3 (= -i chibar[sigma1,sigma2]chi); "
          "{int N n, int M J_(0,0)} = -int M d_0N n (hand value: J_(0,0) generates -translation of density weight 1/2)")
    # flat walker algebra: {C_f[N], C_f[M]} = v^2 G_K[z0], with the Kosmann spin coefficient determined, both signs tested
    E0 = sp.eye(3)
    CN, CM = functional(walker(N, E0, v)), functional(walker(M, E0, v))
    br = pb(CN, CM)
    res = {sg: is_zero(fadd(br, functional(kosmann(z0, v ** 2, sg * sp.Rational(1, 4))), coeffs=[1, -1])) for sg in (1, -1)}
    check("T0b", res == {1: False, -1: True}, f"flat walker: {{C_f[N],C_f[M]}} = v^2 G_K[N dM - M dN] with G_K[xi] = int chibar "
          f"i(xi.d + div xi/2 + (i/4) curl xi.sigma) chi (spin term -1/4 curl xi.s; +1/4 fails): {res}  (B15 C2 analogue)")
    # gravity control
    GX, GY = functional(G1d(XI) + G2Lie(XI)), functional(G1d(ETA) + G2Lie(ETA))
    okg = is_zero(fadd(pb(GX, GY), functional(G1d(L) + G2Lie(L)), coeffs=[1, -1]))
    check("T0c", okg, "gravity control: {G_GR[xi], G_GR[eta]} = G_GR[[xi,eta]], G_GR = int Pt L_xi(delta + h)")

# =====================================================================================================================
# A. {C[N], G[xi]} at order chi chi (h^0): fully general constant-coefficient G_f^(0) and h-linear coupling C_f^(1)
def gen_Gf0(xi, tag):
    unk, dens = [], 0
    for k in R3:
        for mu in range(4):
            for j in R3:
                u = sp.Symbol(f"{tag}A_{k}{j}{mu}", real=True); unk.append(u); dens += u * xi[k] * Jv[j][mu]
                w = sp.Symbol(f"{tag}B_{k}{j}{mu}", real=True); unk.append(w); dens += w * Dk(xi[j], k) * Sv[mu]
            z = sp.Symbol(f"{tag}C_{k}{mu}", real=True); unk.append(z); dens += z * xi[k] * Sv[mu]
    return sp.expand(dens), unk


def gen_coup1(Lp, tag):
    unk, dens = [], 0
    for ab in COMP:
        hab = h(*ab)
        for mu in range(4):
            for k in R3:
                e = sp.Symbol(f"{tag}e_{ab[0]}{ab[1]}{k}{mu}", real=True); unk.append(e); dens += e * hab * Jv[k][mu]
                f = sp.Symbol(f"{tag}f_{ab[0]}{ab[1]}{k}{mu}", real=True); unk.append(f); dens += f * Dk(hab, k) * Sv[mu]
            g = sp.Symbol(f"{tag}g_{ab[0]}{ab[1]}{mu}", real=True); unk.append(g); dens += g * hab * Sv[mu]
    return sp.expand(Lp * dens), unk


if "A" in SEC:
    kA = pat(N=1, x=1, f=2)
    Gf0, uG = gen_Gf0(XI, "")
    C1d, uC = gen_coup1(N, "")
    E0 = sp.eye(3)
    Cf0N = functional(walker(N, E0))
    # lam1 = 1 here: the coupling unknowns represent lam1 x (coupling coefficients)
    lhs = fadd(pb(Cf0N, functional(Gf0), keep=kA), pb(functional(C1d), functional(G1d(XI)), keep=kA))
    rhs = functional(walker(lapse(XI, s1, s2), E0), keep=kA)
    eqs = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
    unk = uG + uC + [s1, s2]
    print(f"   A: {len(eqs)} real equations, {len(unk)} unknowns (G_f^(0): {len(uG)}, lam1 x coupling: {len(uC)}, s1, s2)")
    sol = sp.solve(eqs, unk, dict=True)
    assert len(sol) == 1
    sol = sol[0]
    free = [x for x in unk if x not in sol]
    print(f"   free parameters: {free}")
    G_sol = sp.expand(Gf0.subs(sol))
    C_sol = sp.expand(C1d.subs(sol))
    # expected: one free scale lam_f (G_f = lam_f x Kosmann), s1 = -lam_f, s2 = 0, lam1 x coupling = lam_f x walker's
    # h-linear coupling about E = (delta + h)^(-1/2), i.e. a_s lam1 = lam_f
    Ewalk1 = (frame_sym(1, 1) - sp.eye(3)).applyfunc(sp.expand)
    walk1 = walker(N, Ewalk1)
    ok = len(free) == 1
    if ok:
        p = free[0]
        lamf_val = sp.expand(-sol[s1])
        okK = is_zero(fadd(functional(G_sol), functional(kosmann(XI, lamf_val))))  # may differ by sign; test both
        okK = is_zero(fadd(functional(G_sol), functional(kosmann(XI, lamf_val)), coeffs=[1, -1]))
        okC = is_zero(fadd(functional(C_sol), functional(walk1), coeffs=[1, -lamf_val]))
        ok = okK and okC and sol[s2] == 0 and lamf_val != 0
        print(f"   lam_f = -s1 = {lamf_val}; G_f^(0) = lam_f Kosmann: {okK}; lam1 x coupling = lam_f x walker(E=(1+h)^(-1/2)) h-linear: {okC}; s2 = {sol[s2]}")
    check("A1", ok, "{C[N],G[xi]} at order chi chi with a FULLY GENERAL constant-coefficient G_f^(0) (84 real coefficients: "
          "xi J, dxi S, xi S for all 4 sigma's) and a fully general h-linear coupling (168: h J, dh S, h S): unique up to one scale "
          "lam_f: G_f^(0) = lam_f x Kosmann, s1 = -lam_f, s2 = 0, and lam1 x coupling = lam_f x [walker on E = (delta + h)^(-1/2)]"
          "^(1) = lam_f x [-1/2 h] frame coupling.  So the walker's coupling strength satisfies a_s = lam_f / lam1")
    # A2: the walker's own coupling plugged in with symbolic a_s, lam1, lam_f: residual vanishes iff a_s lam1 = lam_f
    Ea = (frame_sym(aS, 1) - sp.eye(3)).applyfunc(sp.expand)
    lhs = fadd(pb(Cf0N, functional(kosmann(XI, lf)), keep=kA), pb(functional(walker(N, Ea)), functional(lam1 * G1d(XI)), keep=kA))
    rhs = functional(walker(lapse(XI, -lf, 0), E0), keep=kA)
    e2 = eqs_ri(fadd(lhs, rhs, coeffs=[1, -1]))
    s2_ = sp.solve(e2, [aS], dict=True)
    check("A2", s2_ == [{aS: lf / lam1}], f"walker coupling with free strength a_s (E = (delta + a_s h)^(-1/2)): closure at order "
          f"chi chi iff a_s = lam_f/lam1: {s2_}")
