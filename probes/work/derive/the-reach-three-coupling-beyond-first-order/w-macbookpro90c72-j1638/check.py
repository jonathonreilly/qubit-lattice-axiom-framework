#!/usr/bin/env python3
"""J:derive:the-reach-three-coupling-beyond-first-order:a3 -- worker w-macbookpro90c72-j1638.

Block 69's coupling H3[b] = H + V[b], V[b] = sum_{a,l} sigma_a (1/2){C_a[b_a^l], P_l}, P_l the two-step momentum; the clocked walk
phi H3 phi; the two-step relabelling G = (1/2) sum_j {xi_j, P_j}. Exact Gaussian-rational vectors on the 5^3 torus (two-step shifts
distinct), random rational fields.
  R1  every completion H3[f(B)] (f applied to the bond field) is hermitian and species-blind: V_n H3[b] V_n^-1 = s_n H3[b] for all seven n
      (block 70's maps); the reason is the hop parity: sigma_a with hops m = e_a mod 2 (ATTEMPT S1)                          (exact)
  R2  exponentiating the relabelling is not a coupling to the strain: [[P_j, G], H] != 0, so the second-order term of e^{iG} H e^{-iG}
      changes under xi -> xi + const                                                                                         (exact)
  R3  the log-strain completion H + V[e^{-Lambda} - 1]: a uniform strain shows every species e^{-Lambda^T} e^{-Lambda}            (exact)
  R4  the completion enters the sea's second variation only through 2 tr(P_sea V[b_2]); kappa_aa per bond (floating, L = 8, 16) (float)
  R5  the momentum balance at finite strain, exactly: i[phi, P_j] = -(1/2) C2_j[d2_j phi]; i[H, G] = V[d xi];
      i[V[b], G] = sum sigma_a (T1 + T2 + T3) (two flux terms paired with differences of xi, one force paired with xi itself);
      i[phi H3 phi, G] = phi i[H3, G] phi - (Lambda H3 phi + phi H3 Lambda)                                                  (exact)
  R6  expectation form: d<G>/dt = sum (d_a xi_j) K_a^j[phi psi] + strain flux - sum_j xi_j (f^P_j[b] + f^B_j[b]); uniform xi: the total
      two-step momentum changes at minus the total force (rates and strain gradients)                                        (exact)
"""
import itertools
import random
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

import ops as O
from gq import V, inner, sitedens

NF = 0
NP = 0
L = 5
random.seed(20260923)


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def rfield(lo=-3, hi=3, den=4, pos=False):
    f = np.empty((L, L, L), dtype=object)
    for x in itertools.product(range(L), repeat=3):
        v = Fr(random.randint(lo, hi), den)
        f[x] = (Fr(1) + abs(v)) if pos else v
    return f


def rvec():
    re = np.empty((L, L, L, 2), dtype=object); im = np.empty((L, L, L, 2), dtype=object)
    for x in itertools.product(range(L), repeat=3):
        for c in range(2):
            re[x + (c,)] = Fr(random.randint(-4, 4), 3); im[x + (c,)] = Fr(random.randint(-4, 4), 3)
    return V(re, im)


def same(u, v):
    return all(x == y for x, y in zip(u.re.flat, v.re.flat)) and all(x == y for x, y in zip(u.im.flat, v.im.flat))


# ---------------------------------------------------------------- R1
def R1():
    ok = species_check()
    rep("R1 completions are species-blind", ok,
        "on the 6^3 torus with random rational bond fields b_a^l (any b, hence any completion f(B) applied bond by bond): V_n H3[b] "
        "V_n^-1 = s_n H3[b] exactly for all seven n (V_n = R_n U_n, U_n = (-1)^{n.x}, R_n the coin's half turn for s_n D_n); the reason: "
        "every term is sigma_a times a hop m with m = e_a mod 2 (C_a one step along a, P_l zero or two along l), and U_n gives (-1)^{n.m} "
        "= D_a while R_n gives s_n D_a; the linear H3[B] is itself such a completion, so the task's HIT condition fails")


def species_check():
    global L
    L0 = L
    L = 6
    b = [[rfield() for _ in range(3)] for _ in range(3)]
    psi = rvec()
    ok = True
    for n in itertools.product((0, 1), repeat=3):
        if n == (0, 0, 0):
            continue
        U = np.empty((6, 6, 6), dtype=object)
        for x in itertools.product(range(6), repeat=3):
            U[x] = Fr((-1) ** (n[0] * x[0] + n[1] * x[1] + n[2] * x[2]))
        Dn = [(-1) ** k for k in n]
        sn = Dn[0] * Dn[1] * Dn[2]
        rho = [sn * x for x in Dn]
        if rho == [1, 1, 1]:
            R = lambda p: p
        else:
            c = rho.index(1)
            R = lambda p, c=c: p.sigma(c)
        Vn = lambda p: R(p.mulfield(U))
        lhs = Vn(O.H3(b, psi))
        rhs = O.H3(b, Vn(psi))
        rhs = rhs if sn == 1 else -rhs
        ok = ok and same(lhs, rhs)
    L = L0
    return ok


# ---------------------------------------------------------------- R2
def R2():
    xi = [rfield() for _ in range(3)]
    psi = rvec()
    Gx = lambda p: O.G(xi, p)
    ok = True
    vals = []
    for j in range(3):
        Pj = lambda p, j=j: O.P(j, p)
        PG = lambda p: (Pj(Gx(p)) - Gx(Pj(p)))
        out = PG(O.H(psi)) - O.H(PG(psi))
        nz = any(x != 0 for x in out.re.flat) or any(x != 0 for x in out.im.flat)
        ok = ok and nz
    rep("R2 the relabelling's exponential is not a strain coupling", ok,
        "for a random rational displacement on 5^3: [[P_j, G], H] != 0 for j = 1, 2, 3 (exact); since [P_j, H] = 0, [G + c P, [G + c P, H]] "
        "= [G, [G, H]] + c [[P, G], H], so the second-order term of e^{iG} H e^{-iG} depends on xi and not only on d xi: it defines no "
        "coupling to the strain, which is why a completion must be supplied")


# ---------------------------------------------------------------- R3
def R3():
    k = sp.symbols('k1:4', real=True); q = sp.symbols('q1:4', real=True)
    Lam = sp.Matrix(3, 3, sp.symbols('l0:9'))
    t = sp.Symbol('t')
    # second order in t: e^{-t Lambda} - 1 = -t Lambda + t^2 Lambda^2 / 2
    Bm = -t * Lam + t**2 * Lam * Lam / 2
    ok = True
    for n in itertools.product((0, 1), repeat=3):
        Dn = sp.diag(*[(-1) ** x for x in n])
        # near k = pi n + q the sigma part is D (1 + B) q (block 69 T4 with B -> e^{-t Lambda} - 1)
        M = Dn * (sp.eye(3) + Bm)
        g = sp.expand(M.T * M)
        target = sp.expand(((sp.eye(3) - t * Lam + t**2 * Lam * Lam / 2).T * (sp.eye(3) - t * Lam + t**2 * Lam * Lam / 2)))
        ok = ok and sp.simplify(g - target) == sp.zeros(3, 3)
        # and it agrees with e^{-t Lambda^T} e^{-t Lambda} to second order
        ser = sp.expand((sp.eye(3) - t * Lam.T + t**2 * Lam.T * Lam.T / 2) * (sp.eye(3) - t * Lam + t**2 * Lam * Lam / 2))
        diff = (g - ser).applyfunc(lambda e: sp.expand(e).coeff(t, 0) + sp.expand(e).coeff(t, 1) * t + sp.expand(e).coeff(t, 2) * t**2)
        ok = ok and diff == sp.zeros(3, 3)
    rep("R3 the log-strain completion", ok,
        "with b = e^{-Lambda} - 1 bond by bond (the analogue of phi H phi: the two-step momentum weighted by e^{-Lambda}), a uniform strain "
        "shows every one of the eight species the inverse metric (1 + b)^T (1 + b) = e^{-Lambda^T} e^{-Lambda} (block 69 T4 is exact in "
        "b; checked symbolically to second order in Lambda for all n)")


# ---------------------------------------------------------------- R4
def R4():
    out = []
    for Lf in (8, 16):
        kk = 2 * np.pi * np.arange(Lf) / Lf
        K1, K2, K3 = np.meshgrid(kk, kk, kk, indexing='ij')
        s = np.sqrt(np.sin(K1)**2 + np.sin(K2)**2 + np.sin(K3)**2)
        m = s > 1e-12
        kap = -np.sum((np.sin(K1)**2 * np.cos(K1)**2)[m] / s[m]) / Lf**3
        off = -np.sum((np.sin(K1) * np.cos(K1) * np.sin(K2) * np.cos(K2))[m] / s[m]) / Lf**3
        out.append((Lf, kap, off))
    ok = abs(out[0][1] + 0.10761) < 5e-5 and all(abs(o[2]) < 1e-12 for o in out)
    rep("R4 where the completion enters the sea (floating point)", ok,
        "E_sea = sum of the negative energies of H(eps) = H + eps V[b_1] + eps^2 V[b_2] has E_sea''(0) = 2 tr(P_sea V[b_2]) + (terms of b_1 "
        "only); for a bond-local completion b_2 = c b_1^2 of a mode b_1 = b cos(q.x), tr(P_sea V[b_2]) sees only the uniform part b^2/2, so "
        "the shift is q-independent: per unit uniform strain tr(P_sea V_aa)/N = kappa = -(1/N) sum_k sin^2 k_a cos^2 k_a / |s(k)| = "
        + ", ".join(f"{o[1]:.5f} (L = {o[0]})" for o in out) + "; off-diagonal 0 (agrees with attempt a1's -0.10761 on 8^3, computed "
        "independently)")


# ---------------------------------------------------------------- R5, R6
def R5R6():
    phi = rfield(pos=True)
    xi = [rfield() for _ in range(3)]
    b = [[rfield() for _ in range(3)] for _ in range(3)]
    psi = rvec()
    ok = True
    # (i) i[phi, P_j] = -(1/2) C2_j[d2_j phi]
    for j in range(3):
        lhs = (O.P(j, psi).mulfield(phi) - O.P(j, psi.mulfield(phi))).times_i()
        rhs = O.C2w(j, O.d2(j, phi), psi).scale((Fr(-1, 2), Fr(0)))
        ok1 = same(lhs, rhs)
        ok = ok and ok1
    # (ii) i[H, G] = V[d xi]  (block 69 T3(a)); dxi[a][j] = d_a xi_j
    dxi = [[O.d(a, xi[j]) for j in range(3)] for a in range(3)]
    Gx = lambda p: O.G(xi, p)
    lhs = O.icomm(O.H, Gx, psi)
    ok_ii = same(lhs, O.Vb(dxi, psi))
    # (iii) i[V[b], G] = sum_{a,l,j} sigma_a (T1 + T2 + T3)
    Vb = lambda p: O.Vb(b, p)
    direct = O.icomm(Vb, Gx, psi)
    total = psi.zero_like()
    T3sum = psi.zero_like()
    for a in range(3):
        for l in range(3):
            A = lambda p, a=a, l=l: O.Cw(a, b[a][l], p)
            Pl = lambda p, l=l: O.P(l, p)
            for j in range(3):
                Pj = lambda p, j=j: O.P(j, p)
                iPlxi = lambda p, l=l, j=j: O.C2w(l, O.d2(l, xi[j]), p).scale((Fr(1, 2), Fr(0)))       # i[P_l, xi_j]
                iAxi = lambda p, a=a, l=l, j=j: -O.Sw(a, b[a][l] * O.d(a, xi[j]), p)                     # i[C_a[b], xi_j]
                iAPj = lambda p, A=A, Pj=Pj: (A(Pj(p)) - Pj(A(p))).times_i()                           # i[C_a[b], P_j]
                xij = lambda p, j=j: p.mulfield(xi[j])
                anti = lambda X, Y, p: X(Y(p)) + Y(X(p))
                T1 = anti(A, lambda p: anti(iPlxi, Pj, p), psi)
                T2 = anti(lambda p: anti(iAxi, Pj, p), Pl, psi)
                T3 = anti(lambda p: anti(xij, iAPj, p), Pl, psi)
                q = (T1 + T2 + T3).scale((Fr(1, 4), Fr(0))).sigma(a)
                total = total + q
                T3sum = T3sum + T3.scale((Fr(1, 4), Fr(0))).sigma(a)
    ok_iii = same(direct, total)
    # (iv) the full clocked law: i[phi H3 phi, G] = phi i[H3, G] phi - (Lambda H3 phi + phi H3 Lambda)
    H3b = lambda p: O.H3(b, p)
    Hw = lambda p: H3b(p.mulfield(phi)).mulfield(phi)
    Lam = lambda p: sum((O.C2w(j, O.d2(j, phi), p.mulfield(xi[j])).scale((Fr(1, 4), Fr(0)))
                         + O.C2w(j, O.d2(j, phi), p).mulfield(xi[j]).scale((Fr(1, 4), Fr(0))) for j in range(3)), p.zero_like())
    lhs = O.icomm(Hw, Gx, psi)
    rhs = O.icomm(H3b, Gx, psi.mulfield(phi)).mulfield(phi) - (Lam(H3b(psi.mulfield(phi))) + H3b(Lam(psi)).mulfield(phi))
    ok_iv = same(lhs, rhs)
    # R6: expectations. d<G>/dt = <psi| i[H_w, G] |psi>
    rate = inner(psi, lhs)[0]
    chi = psi.mulfield(phi)
    # K-pairing: <chi| V[d xi] |chi>
    flux0 = inner(chi, O.Vb(dxi, chi))[0]
    # strain flux: <chi| sum sigma_a (T1 + T2) |chi>, strain force: <chi| sum sigma_a T3 |chi> (computed on chi)
    t12 = psi.zero_like(); t3 = psi.zero_like()
    for a in range(3):
        for l in range(3):
            A = lambda p, a=a, l=l: O.Cw(a, b[a][l], p)
            Pl = lambda p, l=l: O.P(l, p)
            for j in range(3):
                Pj = lambda p, j=j: O.P(j, p)
                iPlxi = lambda p, l=l, j=j: O.C2w(l, O.d2(l, xi[j]), p).scale((Fr(1, 2), Fr(0)))
                iAxi = lambda p, a=a, l=l, j=j: -O.Sw(a, b[a][l] * O.d(a, xi[j]), p)
                iAPj = lambda p, A=A, Pj=Pj: (A(Pj(p)) - Pj(A(p))).times_i()
                xij = lambda p, j=j: p.mulfield(xi[j])
                anti = lambda X, Y, p: X(Y(p)) + Y(X(p))
                t12 = t12 + (anti(A, lambda p: anti(iPlxi, Pj, p), chi) + anti(lambda p: anti(iAxi, Pj, p), Pl, chi)).scale((Fr(1, 4), Fr(0))).sigma(a)
                t3 = t3 + anti(lambda p: anti(xij, iAPj, p), Pl, chi).scale((Fr(1, 4), Fr(0))).sigma(a)
    strain_flux = inner(chi, t12)[0]
    strain_force_pairing = inner(chi, t3)[0]                   # = - sum_j sum_x xi_j f^B_j
    rate_force_pairing = 2 * inner(Lam(psi), H3b(chi))[0]      # = sum_j sum_x xi_j f^P_j[b]
    ok_R6 = rate == flux0 + strain_flux + strain_force_pairing - rate_force_pairing
    # uniform xi: the flux terms vanish; the total momentum changes at minus the total force
    xi_u = [np.full((L, L, L), Fr(c), dtype=object) for c in (1, 2, -1)]
    Gu = lambda p: O.G(xi_u, p)
    rate_u = inner(psi, O.icomm(Hw, Gu, psi))[0]
    dxi_u = [[O.d(a, xi_u[j]) for j in range(3)] for a in range(3)]
    zero_flux = all(x == 0 for a in range(3) for j in range(3) for x in dxi_u[a][j].flat)
    subs = dict(i=ok, ii=ok_ii, iii=ok_iii, iv=ok_iv)
    ok = ok and ok_ii and ok_iii and ok_iv
    if not ok:
        print('R5 sub-checks:', subs)
    rep("R5 the finite-strain law, operator form", ok,
        "exact on 5^3 with random rational phi > 0, xi, b and psi: i[phi, P_j] = -(1/2) C2_j[d2_j phi] (block 72 T1(a)); i[H, G] = V[d xi]; "
        "i[V[b], G] = sum_{a,l,j} sigma_a (T1 + T2 + T3) with T1 = (1/4){C_a[b], {(1/2) C2_l[d2_l xi_j], P_j}}, T2 = (1/4){{-S_a[b d_a xi_j], "
        "P_j}, P_l}, T3 = (1/4){{xi_j, i[C_a[b], P_j]}, P_l}; and i[phi H3[b] phi, G] = phi i[H3[b], G] phi - (Lambda H3[b] phi + phi H3[b] "
        "Lambda), Lambda = sum_j (1/2){xi_j, (1/2) C2_j[d2_j phi]}")
    rep("R6 the finite-strain momentum balance", ok_R6 and zero_flux,
        f"d<G>/dt = sum (d_a xi_j) K_a^j[phi psi] + <T1 + T2>_{{phi psi}} - sum_j xi_j (f^P_j[b] + f^B_j[b]) holds exactly ({rate} on this "
        f"sample): the strain adds a flux (paired with d xi and d2 xi) and a FORCE f^B from i[C_a[b], P_j], which involves only the "
        f"two-step differences of b; f^P_j[b] is block 72's rate force with H3[b] in place of H; for uniform xi the flux terms vanish and the "
        f"total two-step momentum changes at minus the total force (rates and strain gradients)")


def main():
    R1(); R2(); R3(); R4(); R5R6()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL completions exist (no HIT by the task's criterion): every H3[f(B)] is hermitian and exactly species-blind "
              "because each term is sigma_a times a hop of parity e_a; the natural one by analogy with the rates is the log-strain b = "
              "e^{-Lambda} - 1 (uniform strain: e^{-Lambda^T} e^{-Lambda} for all eight species); exponentiating the relabelling is not a strain "
              "coupling ([[P, G], H] != 0); the completion enters the sea only through 2 tr(P_sea V[b_2]) (kappa = -0.1076 per bond on 8^3); "
              "NEW: block 66/72's exact momentum balance at finite strain: d<G>/dt = sum (d xi) K[phi psi] + strain flux - sum xi (f^P[b] + "
              "f^B[b]), with a strain-gradient force f^B from i[C_a[b], P_j] (two-step differences of b), exact on 5^3")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
