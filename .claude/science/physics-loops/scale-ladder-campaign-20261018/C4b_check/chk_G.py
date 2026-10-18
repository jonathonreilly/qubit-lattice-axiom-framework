#!/usr/bin/env python3
"""C4b_check part G: the walker against the covariant Weyl operator DERIVED FROM THE LEVI-CIVITA SPIN CONNECTION
(own construction: frame -> coframe -> metric -> Christoffels -> spin connection -> -i sigma^a E_a^j nabla_j on
sqrt(g)-scalar spinors -> half-density conjugation -> lapse-symmetrised functional).  Checks C4b G1-G3.

Usage: python3 chk_G.py [1] [2]   (1: first order general frame; 2: second order symmetric frame)
"""
import sys
from vc_core import *

ORD = sys.argv[1:] or ["1", "2"]
t = sp.Symbol("t")
cax = sp.Symbol("c_ax", real=True)


def trunc(e, order):
    e = sp.expand(e)
    return sum(e.coeff(t, k) * t ** k for k in range(order + 1))


def trM(Mx, order):
    return Mx.applyfunc(lambda z: trunc(z, order))


def sqrt_series(x, order):
    """(1 + x)^(1/2), x = O(t)."""
    out, term = 1, 1
    for n in range(1, order + 1):
        term = trunc(term * x, order)
        out += sp.binomial(sp.Rational(1, 2), n) * term
    return trunc(out, order)


def pow_series(x, p, order):
    out, term = 1, 1
    for n in range(1, order + 1):
        term = trunc(term * x, order)
        out += sp.binomial(p, n) * term
    return trunc(out, order)


def covariant_functional(E, order, sgn):
    """C_cov[N] = int sqrt(g) psibar 1/2 (N H psi + H (N psi)),  H = -i sigma_a E_a^j (d_j + Omega_j),
    Omega_j = sgn (i/4) eps_abc omega_jab sigma_c,  omega_jab = e^a_k (d_j E_b^k + Gamma^k_jl E_b^l),
    psi = g^(-1/4) chi, psibar = g^(-1/4) chibar.  E = 1 + O(t); everything truncated at t^order."""
    Ei = trM(inv_series(E, order), order)      # E^{-1}[j, a]
    e_ = Ei.T                                  # e_[a, j] = e^a_j
    g = trM(e_.T * e_, order)                  # g_ij
    gi = trM(E.T * E, order)                   # g^ij
    dete = trunc(e_.det(), order)              # sqrt(g)
    g14m = pow_series(dete - 1, -sp.Rational(1, 2), order)   # g^(-1/4) = (sqrt g)^(-1/2)
    Gam = [[[trunc(sum(gi[k, l] * (D(g[l, j], i) + D(g[l, i], j) - D(g[i, j], l)) for l in R3) / 2, order)
             for j in R3] for i in R3] for k in R3]
    om = [[[trunc(sum(e_[a, k] * (D(E[b, k], j) + sum(Gam[k][j][l] * E[b, l] for l in R3)) for k in R3), order)
            for b in R3] for a in R3] for j in R3]       # om[j][a][b]
    Om = [sgn * I / 4 * sum(((EPS(a, b, cc) * om[j][a][b]) * SIG[cc] for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0), sp.zeros(2, 2))
          for j in R3]

    def Hop(ps):
        out = sp.zeros(2, 1)
        for j in R3:
            dps = ps.applyfunc(lambda z: D(z, j)) + Om[j] * ps
            for a in R3:
                out += -I * E[a, j] * SIG[a] * dps
        return out.applyfunc(lambda z: trunc(z, order))
    psi = sp.Matrix([g14m * c[0], g14m * c[1]]).applyfunc(lambda z: trunc(z, order))
    psib = [trunc(g14m * d[0], order), trunc(g14m * d[1], order)]
    A1 = Hop(psi)
    A2 = Hop(psi.applyfunc(lambda z: N * z))
    dens = sum(psib[al] * dete * (N * A1[al] + A2[al]) / 2 for al in range(2))
    return trunc(dens, order), (e_, om)


def Tax(E, e_):
    return sp.expand(sum(EPS(a, b, cc) * E[a, j] * E[b, k] * D(e_[cc, k], j)
                         for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0 for j in R3 for k in R3))


nt = lambda e: sp.expand(sp.expand(e).subs(t, 1))

if "1" in ORD:
    eps = sp.Matrix(3, 3, lambda a, j: F_(f"e{a}{j}"))
    E = (sp.eye(3) + t * eps)
    res = {}
    for sgn in (1, -1):
        cov, (e_, om) = covariant_functional(E, 1, sgn)
        cov1 = sp.expand(cov).coeff(t, 1)
        T1 = sp.expand(trunc(Tax(E, e_), 1)).coeff(t, 1)
        wk1 = sp.expand(walker(N, E)).coeff(t, 1)
        cov0 = sp.expand(cov).coeff(t, 0)
        ok0 = div_eqs(sp.expand(cov0 - walker(N, sp.eye(3))), N) == []
        r = sp.expand(cov1 - wk1 - cax * N * T1 * (d[0] * c[0] + d[1] * c[1]))
        res[sgn] = (ok0, vsolve(div_eqs(r, N), [cax]))
        print(f"   sign {sgn}: flat part = walker: {ok0}; c_ax solutions {res[sgn][1]}", flush=True)
        if sgn == 1:
            # totally antisymmetric spin connection vs T (Hehl-Datta type scalar)
            omabc = sp.expand(sum(EPS(a, b, cc) * sum(E[a, j] * om[j][b][cc] for j in R3)
                                  for a in R3 for b in R3 for cc in R3 if EPS(a, b, cc) != 0)).coeff(t, 1)
            rr = sp.Symbol("rr")
            rel = vsolve(coeff_eqs(sp.expand(omabc - rr * T1)), [rr])
            print(f"   eps_abc omega_abc (first order) = rr * T^(1): {rel}", flush=True)
    okG = res[1][0] and res[1][1] == [{cax: sp.Rational(1, 4)}] and res[-1][1] == []
    check("G2a", okG, f"general first-order frame 1 + t eps (9 free functions): covariant Weyl functional (LC spin "
          f"connection, the sign that makes it Hermitian/covariant) = walker + c_ax int N T n with c_ax = 1/4 uniquely; "
          f"other sign: no c_ax. {res}")
    check("G2b", len(rel) == 1 and rel[0][rr] != 0, f"eps_abc omega_abc = {rel[0][rr] if rel else None} x T at first order: "
          f"T is (proportional to) the totally antisymmetric part of the LC spin connection, so the 1/4 N T n term is the "
          f"Hehl-Datta-type 'axial' coupling eps^abc omega_abc to chi^dag chi (= the Weyl field's axial density)")
    # rotation defect of the bare walker (C4b G1) by direct substitution, own convention
    A = sp.Matrix(3, 3, lambda a, j: sum(EPS(a, j, k) * th[k] for k in R3))
    kap, cc_ = sp.symbols("kap cc", real=True)
    divth = sum(D(th[k], k) for k in R3)
    W1 = walker(N, A)
    rot = pb(walker(N, sp.eye(3)), spinrot(th, kap), grav=False)
    nb = d[0] * c[0] + d[1] * c[1]
    s_no = vsolve(div_eqs(sp.expand(W1 - rot), N), [kap])
    s_w = vsolve(div_eqs(sp.expand(W1 - rot - cc_ * N * divth * nb), N), [kap, cc_])
    check("G1", s_no == [] and s_w == [{kap: sp.Rational(1, 2), cc_: sp.Rational(1, 2)}],
          f"walker on E = 1 + A (A_aj = eps_ajk th_k): = {{C[1], kap int th.s}} + cc int N div(th) n with kap = cc = 1/2 "
          f"({s_w}); no pure spin rotation ({s_no})")

if "2" in ORD:
    # symmetric section to second order: covariant functional vs walker + 1/4 N T n (C4b G3 and the operator used in F2)
    Es = (sp.eye(3) - t * Hm / 2 + sp.Rational(3, 8) * t ** 2 * Hm * Hm).applyfunc(sp.expand)
    cov, (e_, om) = covariant_functional(Es, 2, 1)
    T = trunc(Tax(Es, e_), 2)
    nb = d[0] * c[0] + d[1] * c[1]
    wk = sp.expand(walker(N, Es))
    T1c, T2c = sp.expand(T).coeff(t, 1), sp.expand(T).coeff(t, 2)
    check("G3a", T1c == 0 or coeff_eqs(T1c) == [], "symmetric section: T^(1) = 0 identically")
    r1 = sp.expand(sp.expand(cov).coeff(t, 1) - wk.coeff(t, 1))
    check("G3b", div_eqs(r1, N) == [], "symmetric section, O(h): covariant functional = bare walker")
    r2b = sp.expand(sp.expand(cov).coeff(t, 2) - wk.coeff(t, 2))
    r2c = sp.expand(r2b - sp.Rational(1, 4) * N * T2c * nb)
    nzb, nzc = div_eqs(r2b, N) != [], div_eqs(r2c, N) == []
    check("G3c", nzb and nzc, f"symmetric section, O(h^2): covariant functional != bare walker ({nzb}) and == walker + "
          f"1/4 int N T^(2) n ({nzc}): c4b's walker_cov IS the covariant Weyl operator to second order")
total()
