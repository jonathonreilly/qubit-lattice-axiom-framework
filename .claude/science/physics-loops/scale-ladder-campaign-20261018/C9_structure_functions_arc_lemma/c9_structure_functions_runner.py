#!/usr/bin/env python3
"""C9: do field-dependent structure functions (or enlarged generator sets) evade the arc lemma?

Campaign block C9 (scale-ladder-campaign-20261018). Same-family worker, unchecked. Pure lattice mathematics:
supplied vector fields / generators, no dynamics adopted, no physical identification.

Lane note: docs/NO_TRANSLATION_COVARIANT_LATTICE_RELABELLING_ALGEBRA_OF_ANY_RANGE_..._2026-10-18.md (Theorem B,
arc lemma). Its premise (P2) demands field-independent structure constants; this runner tests what happens when the
bracket closes only with field-dependent structure functions C_ab^e(Phi), [V_a, V_b] = sum_e C_ab^e V_e, and when
the closure may land in a larger generator set.

Every gating test is exact (sympy over QQ, QQ(lambda) symbolic, QQ[w]/Phi_L(w) cyclotomic, Fraction) except the
single "F_" line (mpmath, 40 digits; a sign statement about cos(2 pi/L)).

Parts
  R  Ruler-background scalar relabelling, position space, central difference (real, nearest-neighbour):
     dV: delta u_x = xi_x (1 + (Delta u)_x). Exact closure with rational structure functions, field-dependent;
     zeroth-order constants = naive lattice bracket (not Lie); Jacobiator = background-velocity term;
     ad_D = -Delta; Lam_2/Lam_1 = w + 1/w = 2 cos(2 pi/L) > 0 for L >= 5, (S) holds.
  M  Same model in momentum coordinates with an arbitrary symbol lambda_k (symbolic) and with SLAC lambda_k = kbar:
     cbar(a,b) = lambda_a - lambda_b; Jac(cbar) identity; SLAC gives Lam_n = nbar Lam_1 on the whole zone.
     Full structure-function Jacobi (with the derivative term) at random rational points.
  X  Realisation lemma: every graded antisymmetric cbar is C(0) of a T-covariant frame.
  P  Poisson (cotangent-lift) form: the lowest-order generators are abelian; cbar appears one order up.
  H  Fixed-point / homogeneity: the linear scalar relabelling at phi = const does not close with constants, its
     structure functions are homogeneous of degree 0 and discontinuous at the common zero; the gap version of the
     arc lemma (support S strictly inside Z_L) by Groebner.
  E  Enlarged generator sets: sl2 |x V_(L-1) (3 extra generators at momenta 0, +-1) has Lam_n = nbar Lam_1 for all n
     with [X_1, X_-1] = H ~ D; D |x Heisenberg (1 extra central generator) does it with [X_1, X_-1] = Z; Groebner:
     under (S') any profile lacking a second generator at one of 0, +-1 cannot have Lam_2 = 2 Lam_1.
"""
from __future__ import annotations

import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import mpmath
import sympy as sp

PASS = FAIL = 0
T0 = time.time()
random.seed(20261018)


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def nbar(n, L):
    r = n % L
    return r - L if r > L // 2 else r


# -------------------------------------------------------------------------------------------------------------
# vector-field engine (components are sympy expressions in the coordinate symbols)
# -------------------------------------------------------------------------------------------------------------
def vf_bracket(V, W, xs):
    """[V, W]^i = V(W^i) - W(V^i)."""
    n = len(xs)
    return [sp.expand(sum(V[c] * sp.diff(W[i], xs[c]) - W[c] * sp.diff(V[i], xs[c]) for c in range(n)))
            for i in range(n)]


def vf_apply(V, f, xs):
    return sum(V[c] * sp.diff(f, xs[c]) for c in range(len(xs)))


# =============================================================================================================
# Part R: ruler-background scalar relabelling, position space, central difference
# =============================================================================================================
def central_delta(L):
    """(Delta u)_x = (u_{x+1} - u_{x-1})/2 as an L x L rational matrix (L >= 3)."""
    D = [[Fr(0)] * L for _ in range(L)]
    for x in range(L):
        D[x][(x + 1) % L] += Fr(1, 2)
        D[x][(x - 1) % L] -= Fr(1, 2)
    return D


def part_R():
    print("\n=== Part R: ruler-background scalar relabelling (position space, central difference, exact) ===")
    for L in range(3, 8):
        t = time.time()
        u = sp.symbols(f"u0:{L}")
        Dl = central_delta(L)
        g = [1 + sum(sp.Rational(Dl[x][y].numerator, Dl[x][y].denominator) * u[y] for y in range(L)) for x in range(L)]
        # generator of the site relabelling xi = delta_i:  V_i = g_i d/du_i
        V = [[g[i] if m == i else sp.Integer(0) for m in range(L)] for i in range(L)]
        # predicted structure functions C_ij^j = Delta_ji g_i/g_j, C_ij^i = -Delta_ij g_j/g_i (others 0)
        closure_ok, fielddep = True, False
        C = {}
        for i in range(L):
            for j in range(L):
                if i == j:
                    continue
                W = vf_bracket(V[i], V[j], u)
                Cij = [sp.Integer(0)] * L
                Cij[j] += sp.Rational(Dl[j][i].numerator, Dl[j][i].denominator) * g[i] / g[j]
                Cij[i] -= sp.Rational(Dl[i][j].numerator, Dl[i][j].denominator) * g[j] / g[i]
                rhs = [sum(Cij[e] * V[e][m] for e in range(L)) for m in range(L)]
                closure_ok &= all(sp.cancel(W[m] - rhs[m]) == 0 for m in range(L))
                fielddep |= any(sp.diff(Cij[e], uu) != 0 for e in range(L) for uu in u)
                C[(i, j)] = Cij
        check(f"R1_closure_L{L}", closure_ok,
              "[V_i, V_j] = C_ij^e V_e exactly, C_ij^j = Delta_ji g_i/g_j, C_ij^i = -Delta_ij g_j/g_i, g = 1 + Delta u "
              "(rational structure functions on the T-invariant open set g_x != 0)")
        check(f"R2_fielddep_L{L}", fielddep, "some C_ij^e has a non-zero u-derivative: (P2) fails, structure functions")
        zero = {uu: 0 for uu in u}
        cbar = {k: [sp.nsimplify(c.subs(zero)) for c in v] for k, v in C.items()}
        for i in range(L):
            cbar[(i, i)] = [sp.Integer(0)] * L
        # zeroth order = naive lattice bracket  zeta = eta Delta xi - xi Delta eta  (xi = delta_i, eta = delta_j)
        naive_ok = True
        for i in range(L):
            for j in range(L):
                zeta = [(1 if m == j else 0) * Dl[m][i] - (1 if m == i else 0) * Dl[m][j] for m in range(L)]
                naive_ok &= all(cbar[(i, j)][m] == zeta[m] for m in range(L))
        check(f"R3_cbar_naive_L{L}", naive_ok, "C(0) = naive bracket eta Delta xi - xi Delta eta (field-independent)")
        # Jacobiator of cbar vs background-velocity term  sum_cyc V_c(C_ab^e)(0) = sum_cyc d_c C_ab^e(0)
        dC = {k: [[sp.nsimplify(sp.diff(v[e], u[c]).subs(zero)) for c in range(L)] for e in range(L)]
              for k, v in C.items()}
        for i in range(L):
            dC[(i, i)] = [[0] * L for _ in range(L)]
        ident_ok, jac_nonzero = True, False
        for a, b, c in itertools.product(range(L), repeat=3):
            for e in range(L):
                jac = sum(cbar[(a, b)][d] * cbar[(d, c)][e] + cbar[(b, c)][d] * cbar[(d, a)][e]
                          + cbar[(c, a)][d] * cbar[(d, b)][e] for d in range(L))
                der = dC[(a, b)][e][c] + dC[(b, c)][e][a] + dC[(c, a)][e][b]
                ident_ok &= (sp.nsimplify(jac - der) == 0)
                jac_nonzero |= (jac != 0)
        if L == 3:
            check(f"R4_jacobiator_L{L}", ident_ok and not jac_nonzero,
                  "Jac(cbar)_abc^e = sum_cyc d_c C_ab^e(0) for all triples, and Jac(cbar) = 0 at L = 3: the zeroth-"
                  "order bracket is sl2 (the arc lemma's L = 3 exception), first-order terms cancel cyclically")
        else:
            check(f"R4_jacobiator_L{L}", ident_ok and jac_nonzero,
                  "Jac(cbar)_abc^e = sum_cyc d_c C_ab^e(0) for all triples (background velocity V_c(0) = d_c), and "
                  "Jac(cbar) != 0: the zeroth-order bracket is not a Lie algebra")
        # ad_D at the background, D = sum_i V_i (xi = 1):  zeta = -Delta eta
        adD = [[sum(cbar[(i, j)][m] for i in range(L)) for j in range(L)] for m in range(L)]
        check(f"R5_adD_L{L}", all(adD[m][j] == -Dl[m][j] for m in range(L) for j in range(L)),
              f"[D, V_eta](0) = V_(-Delta eta)(0): ad_D at the background is -Delta ({time.time()-t:.1f}s)")
    # spectrum in QQ[w]/Phi_L(w): Fourier modes, Lam_n, (S), ratio
    w = sp.Symbol("w")
    for L in range(3, 13):
        Phi = sp.Poly(sp.cyclotomic_poly(L, w), w, domain="QQ")
        red = lambda e: sp.Poly(sp.expand(e), w, domain="QQ").rem(Phi)
        Dl = central_delta(L)
        def mode(n):
            return [w ** ((n * x) % L) for x in range(L)]
        lam = {n: (w ** (n % L) - w ** ((-n) % L)) / 2 for n in range(L)}     # symbol of Delta on mode n
        eig_ok = True
        for n in range(L):
            v = mode(n)
            for x in range(L):
                lhs = sum(sp.Rational(Dl[x][y].numerator, Dl[x][y].denominator) * v[y] for y in range(L))
                eig_ok &= red(lhs - lam[n] * v[x]).is_zero
        Lam = {n: -lam[n] for n in range(L)}          # Lam_n = cbar(0, n) = -lambda_n
        S_ok = (not red(Lam[1]).is_zero) and (not red(lam[1] - lam[L - 1]).is_zero)
        ratio_ok = red(Lam[2] - (w + w ** (L - 1)) * Lam[1]).is_zero
        check(f"R6_spectrum_L{L}", eig_ok and S_ok and ratio_ok,
              "Delta e_n = lambda_n e_n, Lam_n = -lambda_n; (S): Lam_1 != 0 and cbar(1,-1) = lambda_1 - lambda_-1 != 0; "
              "Lam_2 = (w + 1/w) Lam_1 in QQ[w]/Phi_L")
    mpmath.mp.dps = 40
    ratios = {L: 2 * mpmath.cos(2 * mpmath.pi / L) for L in range(5, 41)}
    check("F_R7_ratio_positive", all(r > 0 for r in ratios.values()) and abs(ratios[40] - 2) < mpmath.mpf("0.025")
          and abs(2 * mpmath.cos(2 * mpmath.pi / 4)) < mpmath.mpf(10) ** -35,
          f"Lam_2/Lam_1 = 2cos(2pi/L) > 0 for L = 5..40 (arc lemma would force <= 0), "
          f"L=6: {mpmath.nstr(ratios[6], 6)}, L=40: {mpmath.nstr(ratios[40], 8)}; L = 4 gives 0 (inside the arc set)")


# =============================================================================================================
# Part M: momentum coordinates, symbolic symbol lambda_k, and SLAC
# =============================================================================================================
def mom_frame(L, alpha):
    """V_a = d_a + sum_k alpha(a,k) u_k d_(a+k) on C^L with momentum coordinates u_k (k in Z_L)."""
    u = sp.symbols(f"z0:{L}")
    V = []
    for a in range(L):
        comp = [sp.Integer(1) if i == a else sp.Integer(0) for i in range(L)]
        for k in range(L):
            comp[(a + k) % L] += alpha(a, k) * u[k]
        V.append([sp.expand(x) for x in comp])
    return u, V


def frame_C0_dC0(L, u, V):
    """structure functions at u = 0 and their first derivatives, from C = M^{-1} W, M(0) = 1:
       C(0) = W(0),  d_c C(0) = d_c W(0) - (d_c M) W(0)."""
    zero = {x: 0 for x in u}
    C0, dC0 = {}, {}
    for a in range(L):
        for b in range(L):
            W = vf_bracket(V[a], V[b], u)
            W0 = [sp.expand(x.subs(zero)) for x in W]
            C0[(a, b)] = W0
            dC0[(a, b)] = [[sp.expand(sp.diff(W[e], u[c]).subs(zero)
                                      - sum(sp.diff(V[d][e], u[c]).subs(zero) * W0[d] for d in range(L)))
                            for c in range(L)] for e in range(L)]
    return C0, dC0


def jac_identity(L, C0, dC0):
    ok, nonzero = True, False
    for a, b, c in itertools.product(range(L), repeat=3):
        for e in range(L):
            jac = sum(C0[(a, b)][d] * C0[(d, c)][e] + C0[(b, c)][d] * C0[(d, a)][e] + C0[(c, a)][d] * C0[(d, b)][e]
                      for d in range(L))
            der = dC0[(a, b)][e][c] + dC0[(b, c)][e][a] + dC0[(c, a)][e][b]
            ok &= sp.expand(jac - der) == 0
            nonzero |= sp.expand(jac) != 0
    return ok, nonzero


def graded_ok(L, C0):
    return all(C0[(a, b)][e] == 0 for a in range(L) for b in range(L) for e in range(L) if e != (a + b) % L)


def full_jacobi_at_point(L, u, V, pt):
    """exact structure functions C(pt) = M^{-1} W and the full Jacobi sum_cyc (C C - V_c(C)) at a rational point."""
    sub = dict(zip(u, pt))
    M = sp.Matrix(L, L, lambda i, a: V[a][i])
    Mi_sym = None
    Mp = M.subs(sub)
    Mpi = Mp.inv()
    Wsym = {(a, b): sp.Matrix(vf_bracket(V[a], V[b], u)) for a in range(L) for b in range(L)}
    C = {k: Mpi * W.subs(sub) for k, W in Wsym.items()}
    # derivative of C = M^{-1} W along V_c at pt:  d(M^{-1}W)[v] = M^{-1}(dW[v] - dM[v] M^{-1} W)
    def dir_der(expr_mat, vvec):
        return sp.Matrix(expr_mat.shape[0], expr_mat.shape[1],
                         lambda i, j: sum(vvec[c] * sp.diff(expr_mat[i, j], u[c]) for c in range(L)).subs(sub))
    Vp = [[V[c][i].subs(sub) for i in range(L)] for c in range(L)]
    dC = {}
    for k, W in Wsym.items():
        for c in range(L):
            dW = dir_der(W, Vp[c])
            dM = dir_der(M, Vp[c])
            dC[(k, c)] = Mpi * (dW - dM * C[k])
    worst = 0
    for a, b, c in itertools.product(range(L), repeat=3):
        tot = sp.zeros(L, 1)
        for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
            for d in range(L):
                tot += C[(x, y)][d] * C[(d, z)]
            tot -= dC[((x, y), z)]
        if any(sp.nsimplify(t) != 0 for t in tot):
            worst += 1
    return worst == 0, Mp.det()


def part_M():
    print("\n=== Part M: momentum coordinates, symbolic symbol lambda_k, and SLAC (exact) ===")
    for L in range(3, 7):
        t = time.time()
        lam = [sp.Integer(0)] + list(sp.symbols(f"lam1:{L}"))
        u, V = mom_frame(L, lambda a, k: lam[k])
        C0, dC0 = frame_C0_dC0(L, u, V)
        cb_ok = graded_ok(L, C0) and all(sp.expand(C0[(a, b)][(a + b) % L] - (lam[a] - lam[b])) == 0
                                         for a in range(L) for b in range(L))
        check(f"M1_cbar_L{L}", cb_ok, "generic symbol lambda (lambda_0 = 0): C(0) graded, cbar(a,b) = lambda_a - lambda_b, "
              "so Lam_n = cbar(0,n) = -lambda_n for EVERY symbol")
        ok, nz = jac_identity(L, C0, dC0)
        check(f"M2_jacobiator_L{L}", ok and nz, f"Jac(cbar) = sum_cyc d_c C_ab^(a+b+c)(0) as polynomials in lambda, "
              f"Jac(cbar) not identically 0 ({time.time()-t:.1f}s)")
        fo_ok = True
        for a, b, c, e in itertools.product(range(L), repeat=4):
            pred = (lam[c] * (lam[(a + c) % L] - lam[(b + c) % L] - lam[a] + lam[b])) if e == (a + b + c) % L else 0
            fo_ok &= sp.expand(dC0[(a, b)][e][c] - pred) == 0
        check(f"M2b_first_order_L{L}", fo_ok, "first-order structure functions: d_c C_ab^e(0) = 0 unless e = a+b+c, and "
              "d_c C_ab^(a+b+c)(0) = lambda_c (lambda_(a+c) - lambda_(b+c) - lambda_a + lambda_b)")
    # additive symbol: Witt-like cbar is Lie and first-order terms cancel; check the identity's other side
    # SLAC lambda_k = kbar (the factor i 2pi/L of the physical generator rescales every identity uniformly)
    for L in (5, 7):
        t = time.time()
        u, V = mom_frame(L, lambda a, k: sp.Integer(nbar(k, L)))
        C0, dC0 = frame_C0_dC0(L, u, V)
        Lam = {n: C0[(0, n)][n] for n in range(L)}
        spec_ok = graded_ok(L, C0) and all(Lam[n] == nbar(n, L) * Lam[1] for n in range(L)) and Lam[1] != 0
        S_ok = C0[(1, L - 1)][0] != 0
        ok, nz = jac_identity(L, C0, dC0)
        first_order = any(dC0[(a, b)][e][c] != 0 for a in range(L) for b in range(L) for e in range(L) for c in range(L))
        check(f"M3_SLAC_L{L}", spec_ok and S_ok and ok and nz and first_order,
              f"SLAC ruler model: Lam_n = nbar Lam_1 for all n (Lam_1 = {Lam[1]}), cbar(1,-1) = {C0[(1, L-1)][0]} != 0, "
              f"exact closure with structure functions, Jac(cbar) != 0 compensated by first-order terms "
              f"({time.time()-t:.1f}s)")
    # full structure-function Jacobi (derivative term included) at random rational points, away from u = 0
    for L, lamf in ((4, lambda k: sp.Integer(nbar(k, 4))), (5, lambda k: sp.Integer(nbar(k, 5)))):
        t = time.time()
        u, V = mom_frame(L, lambda a, k: lamf(k))
        allok = True
        for trial in range(2):
            pt = [sp.Rational(random.randint(-5, 5), random.randint(7, 13)) for _ in range(L)]
            ok, det = full_jacobi_at_point(L, u, V, pt)
            allok &= ok and det != 0
        check(f"M4_fullJacobi_L{L}", allok, "sum_cyc (C_ab^d C_dc^e - V_c(C_ab^e)) = 0 exactly at 2 random rational "
              f"points (the sign convention of the derivative term) ({time.time()-t:.1f}s)")
    # forward difference: even Lam_-1 = -Lam_1 (step 1 of the arc lemma) fails
    w = sp.Symbol("w")
    allok = True
    for L in range(3, 10):
        Phi = sp.Poly(sp.cyclotomic_poly(L, w), w, domain="QQ")
        red = lambda e: sp.Poly(sp.expand(e), w, domain="QQ").rem(Phi)
        lam1, lamm1 = w - 1, w ** (L - 1) - 1          # forward difference symbol w^k - 1
        allok &= not red(-(lam1 + lamm1)).is_zero       # Lam_1 + Lam_-1 = -(lambda_1 + lambda_-1)
    check("M5_forward_breaks_step1", allok, "forward difference (lambda_k = w^k - 1): Lam_1 + Lam_-1 = 2 - w - 1/w != 0 "
          "in QQ[w]/Phi_L, L = 3..9: with structure functions even the first step of the arc lemma is not forced")


# =============================================================================================================
# Part X: realisation lemma
# =============================================================================================================
def part_X():
    print("\n=== Part X: every graded antisymmetric cbar is C(0) of a T-covariant frame (exact) ===")
    for L in (4, 5, 6):
        t = time.time()
        cb = {}
        for a in range(L):
            for b in range(a + 1, L):
                cb[(a, b)] = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
                cb[(b, a)] = -cb[(a, b)]
            cb[(a, a)] = sp.Integer(0)
        cb[(0, 1)], cb[(1, 0)] = sp.Integer(1), sp.Integer(-1)
        cb[(0, 2)], cb[(2, 0)] = sp.Integer(2), sp.Integer(-2)           # Lam_2 = 2 Lam_1: forbidden for constants
        u, V = mom_frame(L, lambda a, k: -cb[(a, k % L)] / 2)
        C0, dC0 = frame_C0_dC0(L, u, V)
        ok = graded_ok(L, C0) and all(C0[(a, b)][(a + b) % L] == cb[(a, b)] for a in range(L) for b in range(L))
        okj, nz = jac_identity(L, C0, dC0)
        check(f"X1_L{L}", ok and okj, f"random rational cbar with Lam_1 = 1, Lam_2 = 2 realised: "
              f"V_a = d_a - (1/2) sum_k cbar(a,k) u_k d_(a+k) has C(0) = cbar exactly; Jacobiator identity holds "
              f"(Jac(cbar) != 0: {nz}) ({time.time()-t:.1f}s)")


# =============================================================================================================
# Part P: Poisson (cotangent lift) form
# =============================================================================================================
def part_P():
    print("\n=== Part P: Poisson form X_a = <p, V_a>: lowest order abelian, cbar one order up (exact) ===")
    for L in (5, 7):
        u, V = mom_frame(L, lambda a, k: sp.Integer(nbar(k, L)))
        p = sp.symbols(f"p0:{L}")
        X = [sp.expand(sum(p[m] * V[a][m] for m in range(L))) for a in range(L)]

        def pb(f, g):  # {u_m, p_n} = delta_mn
            return sp.expand(sum(sp.diff(f, u[m]) * sp.diff(g, p[m]) - sp.diff(f, p[m]) * sp.diff(g, u[m])
                                 for m in range(L)))
        X1 = [sp.Integer(0) + p[a] for a in range(L)]
        lin_ok = all(sp.expand(X[a] - X1[a]).subs({x: 0 for x in u}) == 0 for a in range(L))
        ab_ok = all(pb(X1[a], X1[b]) == 0 for a in range(L) for b in range(L))
        C0, _ = frame_C0_dC0(L, u, V)
        deg1_ok = True
        for a in range(L):
            for b in range(L):
                br = pb(X[a], X[b])
                deg1 = sp.expand(br.subs({x: 0 for x in u}))
                deg1_ok &= sp.expand(deg1 + C0[(a, b)][(a + b) % L] * p[(a + b) % L]) == 0
        # exact identity {X_a, X_b} = -sum_e C_ab^e X_e at a rational point
        pt = [sp.Rational(random.randint(-4, 4), 9) for _ in range(L)]
        pp = [sp.Rational(random.randint(-4, 4), 7) for _ in range(L)]
        sub = dict(zip(u, pt)) | dict(zip(p, pp))
        M = sp.Matrix(L, L, lambda i, a: V[a][i]).subs(dict(zip(u, pt)))
        Mi = M.inv()
        full_ok = True
        for a, b in [(1, L - 1), (0, 2), (2, 3)]:
            W = sp.Matrix(vf_bracket(V[a], V[b], u)).subs(dict(zip(u, pt)))
            Cab = Mi * W
            full_ok &= sp.nsimplify(pb(X[a], X[b]).subs(sub) + sum(Cab[e] * X[e].subs(sub) for e in range(L))) == 0
        check(f"P1_L{L}", lin_ok and ab_ok and deg1_ok and full_ok,
              "lowest-order generators X^(1)_a = p_a Poisson-commute (abelian: (S) fails at that order); "
              "degree-1 part of {X_a, X_b} = -cbar(a,b) p_(a+b); {X_a, X_b} = -C_ab^e(u) X_e at a rational point")


# =============================================================================================================
# Part H: fixed-point / homogeneity; gap version of the arc lemma
# =============================================================================================================
def gap_jacobi(L, support, fixed):
    """graded algebra with basis X_n, n in support (0, +-1 in support); cyclic Jacobi; Lam_1 = 1, c(1,-1) = 1."""
    S = set(s % L for s in support)
    var = {}
    for a in range(L):
        for b in range(a + 1, L):
            if a in S and b in S and (a + b) % L in S:
                var[(a, b)] = sp.Symbol(f"c{a}_{b}")
    var[(0, 1)] = sp.Integer(1)
    var[(1, L - 1)] = sp.Integer(1)
    for k, v in fixed.items():
        var[k] = v

    def c(a, b):
        a, b = a % L, b % L
        if a == b or (a, b) not in var and (b, a) not in var:
            return sp.Integer(0)
        return var[(a, b)] if a < b else -var[(b, a)]
    eqs = set()
    for a, b, e in itertools.combinations(sorted(S), 3):
        J = sp.expand(c(a, b) * c(a + b, e) + c(b, e) * c(b + e, a) + c(e, a) * c(e + a, b))
        if J != 0:
            eqs.add(J)
    eqs = list(eqs)
    vs = sorted({s for q in eqs for s in q.free_symbols}, key=str)
    return eqs, vs


def gap_consistent(L, support, fixed):
    eqs, vs = gap_jacobi(L, support, fixed)
    if any(q.is_number and q != 0 for q in eqs):
        return False
    if not vs:
        return True
    return list(sp.groebner(eqs, *vs, order="grevlex", domain="QQ").exprs) != [1]


def gap_arc_lam2(L, support):
    """predicted Lam_2/Lam_1 values: 2 is the bottom of an arc [2, 2+m] inside the run of the support starting at 2."""
    S = set(s % L for s in support)
    if 2 not in S:
        return set()
    run = 0
    n = 2
    while n <= L - 2 and n in S:
        run += 1
        n += 1
    return {Fr(-m, 2) for m in range(run)}


def part_H():
    print("\n=== Part H: fixed point / homogeneity, and the gap version of the arc lemma (exact) ===")
    # H1: linear scalar relabelling delta phi = xi Delta phi at phi = const (a common zero)
    for L in range(3, 7):
        Dl = central_delta(L)
        # linear vector field A_i: (A_i phi)_m = delta_mi (Delta phi)_i  -> matrix A_i[m][y] = delta_mi Dl[i][y]
        A = [sp.Matrix(L, L, lambda m, y: Dl[i][y] if m == i else 0) for i in range(L)]
        # vector-field bracket of linear fields x -> A x, x -> B x is x -> (B A - A B) x
        comms = [B * Am - Am * B for Am in A for B in A]
        span = sp.Matrix([list(Am) for Am in A])
        big = sp.Matrix([list(Am) for Am in A] + [list(Cm) for Cm in comms])
        not_closed = big.rank() > span.rank()
        # structure functions C_ij^j = Delta_ji (Delta phi)_i/(Delta phi)_j are degree-0 homogeneous, non-constant
        phi1 = [sp.Rational(x * x + 1, 1) for x in range(L)]
        phi2 = [sp.Rational(3 * x + (x % 2) * 5 + 1, 2) for x in range(L)]
        dphi = lambda ph: [sum(Dl[x][y] * ph[y] for y in range(L)) for x in range(L)]
        d1, d2 = dphi(phi1), dphi(phi2)
        i, j = 1, 0                                                    # Delta_01 = 1/2 != 0
        val = lambda d: Dl[j][i] * d[i] / d[j] if d[j] != 0 else None
        disc = (val(d1) is not None and val(d2) is not None and val(d1) != val(d2))
        check(f"H1_L{L}", not_closed and disc,
              f"linear scalar relabelling at the common zero phi = const: brackets leave the constant span "
              f"(rank {span.rank()} -> {big.rank()}); C_10^0 = Delta_01 (Delta phi)_1/(Delta phi)_0 takes values "
              f"{val(d1)} and {val(d2)} on two rays: degree-0 homogeneous, no continuous value at phi = 0")
    # H2: gap version of the arc lemma (Groebner, own cyclic generator)
    grid = [Fr(2), Fr(1), Fr(1, 2), Fr(0), Fr(-1, 2), Fr(-1), Fr(-3, 2), Fr(1, 3)]
    cases = [(6, [0, 1, 2, 4, 5]), (7, [0, 1, 2, 4, 5, 6]), (7, [0, 1, 2, 3, 5, 6]), (8, [0, 1, 2, 3, 5, 6, 7])]
    for L, sup in cases:
        t = time.time()
        pred = gap_arc_lam2(L, sup)
        cons = {v for v in grid if gap_consistent(L, sup, {(0, 2): sp.Rational(v.numerator, v.denominator)})}
        check(f"H2_gap_L{L}_S{''.join(map(str, sup))}", cons == pred and Fr(2) not in cons,
              f"support {sup}: consistent Lam_2/Lam_1 on an 8-point grid = {sorted(map(str, cons))} = gap-arc "
              f"prediction {sorted(map(str, pred))} ({time.time()-t:.1f}s)")


# =============================================================================================================
# Part E: enlarged generator sets
# =============================================================================================================
def lie_check(basis_mom, br, L):
    """br: dict (i, j) -> {k: coef} for i < j (antisymmetry implied). Exact Jacobi + momentum grading."""
    n = len(basis_mom)

    def bracket(x, y):
        out = {}
        for i, a in x.items():
            for j, b in y.items():
                if i == j:
                    continue
                d = br.get((i, j)) if i < j else {k: -v for k, v in br.get((j, i), {}).items()}
                for k, v in (d or {}).items():
                    out[k] = out.get(k, 0) + a * b * v
        return {k: v for k, v in out.items() if v != 0}
    grading = all((basis_mom[k] - basis_mom[i] - basis_mom[j]) % L == 0 for (i, j), d in br.items() for k in d)
    jac = True
    for i, j, k in itertools.combinations(range(n), 3):
        e = lambda q: {q: Fr(1)}
        t1 = bracket(bracket(e(i), e(j)), e(k))
        t2 = bracket(bracket(e(j), e(k)), e(i))
        t3 = bracket(bracket(e(k), e(i)), e(j))
        tot = {}
        for t in (t1, t2, t3):
            for q, v in t.items():
                tot[q] = tot.get(q, 0) + v
        jac &= all(v == 0 for v in tot.values())
    return grading, jac, bracket


def sl2_semi_V(L):
    """sl2 |x V_m, m = L-1 (L odd), abelian radical.
    basis: 0 = H, 1 = E, 2 = F, 3 + j = v_j (j = 0..m), weight m - 2j, momentum m/2 - j."""
    m = L - 1
    mom = [0, 1, -1] + [m // 2 - j for j in range(m + 1)]
    br = {(0, 1): {1: Fr(2)}, (0, 2): {2: Fr(-2)}, (1, 2): {0: Fr(1)}}
    for j in range(m + 1):
        br[(0, 3 + j)] = {3 + j: Fr(m - 2 * j)}
        if j >= 1:
            br[(1, 3 + j)] = {3 + j - 1: Fr(j * (m - j + 1))}
        if j <= m - 1:
            br[(2, 3 + j)] = {3 + j + 1: Fr(1)}
    return mom, br


def part_E():
    print("\n=== Part E: enlarged generator sets (exact) ===")
    for L in (5, 7, 9):
        mom, br = sl2_semi_V(L)
        grading, jac, bracket = lie_check(mom, br, L)
        # D = H/2 has [D, E] = E: Lam_1 = 1; eigenvalue of ad_D on the radical vector at momentum n is nbar
        m = L - 1
        lam_ok = all(Fr(m - 2 * j, 2) == nbar(m // 2 - j, L) for j in range(m + 1))
        Sp = br[(1, 2)] == {0: Fr(1)}                       # [E, F] = H = 2D
        # relabelling map G[e_n]: n = 0, +-1 -> H, E, F; |nbar| >= 2 -> v at momentum n.  span G not a subalgebra:
        j2 = m // 2 - 2                                      # v at momentum 2
        out = bracket({2: Fr(1)}, {3 + j2: Fr(1)})           # [F, v_(mom 2)] lands at momentum 1, on v (not on E)
        leaves = set(out) == {3 + j2 + 1}
        dims = {r: sum(1 for x in mom if x % L == r % L) for r in (0, 1, -1, 2)}
        check(f"E1_L{L}", grading and jac and lam_ok and Sp and leaves and dims == {0: 2, 1: 2, -1: 2, 2: 1},
              f"sl2 |x V_{m}: exact Jacobi over all triples, momentum-graded, dims g_0 = g_+-1 = 2, others 1; "
              f"(S'): [E, F] = 2D; Lam_n = nbar Lam_1 for EVERY n; span G is not closed ([F, X_2] in the extra "
              f"generator at momentum 1)")
    for L in (5, 7, 9):
        # D |x Heisenberg: 0 = D, 1 = Z, 2 + r = X_n with n = nbar range
        ns = [n for n in range(-(L // 2), L // 2 + 1) if n != 0]
        mom = [0, 0] + ns
        br = {}
        for r, n in enumerate(ns):
            br[(0, 2 + r)] = {2 + r: Fr(n)}
        for r, n in enumerate(ns):
            for s, q in enumerate(ns):
                if r < s and (n + q) % L == 0:
                    br[(2 + r, 2 + s)] = {1: Fr(n)}
        grading, jac, bracket = lie_check(mom, br, L)
        i1, im1 = 2 + ns.index(1), 2 + ns.index(-1)
        x = bracket({i1: Fr(1)}, {im1: Fr(1)})
        check(f"E2_L{L}", grading and jac and set(x) == {1},
              "D |x Heisenberg (one extra central generator Z): exact Jacobi; Lam_n = nbar for all n; "
              "[X_1, X_-1] = Z != 0 (literal (S)) but not proportional to D (fails (S'))")
    # E3: Groebner necessity at L = 5 for multiplicity profiles missing one of the three extras
    L = 5

    def profile_eqs(extra_moms, fixed_lam2):
        names = [("D", 0), ("X1", 1), ("X4", 4), ("X2", 2), ("X3", 3)] + [(f"Y{r}", r) for r in extra_moms]
        idx = {nm: i for i, (nm, _) in enumerate(names)}
        n = len(names)
        mom = [r for _, r in names]
        var = {}
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(n):
                    if (mom[k] - mom[i] - mom[j]) % L == 0:
                        var[(i, j, k)] = sp.Symbol(f"s{i}_{j}_{k}")
        fix = {}
        D, X1, X4, X2 = idx["D"], idx["X1"], idx["X4"], idx["X2"]
        lam_m1 = sp.Symbol("lam_m1")
        for k in range(n):
            if (mom[k] - 1) % L == 0:
                fix[(D, X1, k)] = sp.Integer(1 if k == X1 else 0)          # [D, X1] = X1
            if (mom[k] - 4) % L == 0:
                fix[(D, X4, k)] = lam_m1 if k == X4 else sp.Integer(0)    # X_-1 an ad_D eigenvector
            if mom[k] == 0:
                fix[(X1, X4, k)] = sp.Integer(1 if k == D else 0)          # (S'): [X1, X_-1] = D
            if mom[k] == 2:
                fix[(D, X2, k)] = fixed_lam2 if k == X2 else sp.Integer(0)  # [D, X2] = Lam_2 X2 (g_2 one-dim)
        var.update(fix)

        def brk(i, j):
            if i == j:
                return {}
            if i < j:
                return {k: var[(i, j, k)] for k in range(n) if (i, j, k) in var}
            return {k: -v for k, v in brk(j, i).items()}
        eqs = set()
        for i, j, k in itertools.combinations(range(n), 3):
            tot = {}
            for (a, b, c) in ((i, j, k), (j, k, i), (k, i, j)):
                for d, v in brk(a, b).items():
                    for e, w2 in brk(d, c).items():
                        tot[e] = tot.get(e, 0) + v * w2
            for v in tot.values():
                v = sp.expand(v)
                if v != 0:
                    eqs.add(v)
        return list(eqs), names, var
    for extras, lam2, expect_incons, label in (([0], sp.Integer(2), True, "extra at 0 only"),
                                               ([0, 1], sp.Integer(2), True, "extras at 0, 1"),
                                               ([1, 4], sp.Integer(2), True, "extras at +-1"),
                                               ([0], sp.Rational(1, 3), True, "extra at 0, Lam_2 = 1/3 (cor. (i))"),
                                               ([0], sp.Integer(0), False, "control: extra at 0, Lam_2 = 0 (consistent)"),
                                               ([0], sp.Rational(-1, 2), False,
                                                "control: extra at 0, Lam_2 = -1/2 (consistent)")):
        t = time.time()
        eqs, names, var = profile_eqs(extras, lam2)
        vs = sorted({s for q in eqs for s in q.free_symbols}, key=str)
        G = sp.groebner(eqs, *vs, order="grevlex", domain="QQ")
        incons = list(G.exprs) == [1]
        check(f"E3_L5_{'_'.join(map(str, extras))}_lam2_{lam2}", incons == expect_incons,
              f"{label}: (S') + Lam_2 = {lam2} + Jacobi -> Groebner basis {'[1]' if incons else 'not [1]'} "
              f"({len(vs)} vars, {time.time()-t:.1f}s)")
    # E3 control: the generator accepts the sl2 |x V_4 realisation (extras at 0, +-1), after a basis change
    eqs, names, var = profile_eqs([0, 1, 4], sp.Integer(2))
    # map: D = H/2, X1 = E, X4 = F/2 so that [X1, X4] = H/2 = D; Y0 = v at mom 0, Y1 = v at mom 1, Y4 = v at mom -1,
    # X2 = v at mom 2, X3 = v at mom -2.  Compute all structure constants in this basis exactly.
    mom, br = sl2_semi_V(5)
    _, _, bracket = lie_check(mom, br, 5)
    # sl2|xV_4 basis indices: 0 H, 1 E, 2 F, 3 v0 (mom 2), 4 v1 (mom 1), 5 v2 (mom 0), 6 v3 (mom -1), 7 v4 (mom -2)
    newb = {"D": {0: Fr(1, 2)}, "X1": {1: Fr(1)}, "X4": {2: Fr(1, 2)}, "X2": {3: Fr(1)}, "X3": {7: Fr(1)},
            "Y0": {5: Fr(1)}, "Y1": {4: Fr(1)}, "Y4": {6: Fr(1)}}
    order = [nm for nm, _ in names]
    Bmat = sp.Matrix([[newb[nm].get(q, 0) for q in range(8)] for nm in order])   # rows: new basis in old coords
    Binv = Bmat.inv()
    sub = {}
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            res = {}
            for p, a in newb[order[i]].items():
                for q, b in newb[order[j]].items():
                    for k, v in bracket({p: a}, {q: b}).items():
                        res[k] = res.get(k, 0) + v
            vec = sp.Matrix([[res.get(q, 0) for q in range(8)]])
            coords = vec * Binv
            for k in range(len(order)):
                key = (i, j, k)
                if key in var and isinstance(var[key], sp.Symbol):
                    sub[var[key]] = coords[k]
    sub[sp.Symbol("lam_m1")] = sp.Integer(-1)
    ok = all(sp.nsimplify(q.subs(sub)) == 0 for q in eqs)
    check("E3_control_L5", ok, "the same equation generator is satisfied exactly by sl2 |x V_4 with extras at 0, +-1 "
          "and Lam_2 = 2 (so the [1] results are not generator artefacts)")


if __name__ == "__main__":
    part_R()
    part_M()
    part_X()
    part_P()
    part_H()
    part_E()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time()-T0:.1f}s)")
    sys.exit(0 if FAIL == 0 else 1)
