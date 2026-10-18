#!/usr/bin/env python3
"""B19 continuum, part 2: is the quadratic gravity generator G2 (and with it the lapse rule) FORCED?

C11  [sqrt g R]^(2) (g = delta + h) has the Fourier symbol of block 62's R_2 =
     -(p^2/4) tr(h^T h) + (1/2)|h p|^2 - (1/2)(p^T h p) tr h + (p^2/4) tr(h)^2  (so block 62/101 has K1 = K2 = K).
C12  General rotation-covariant quadratic gravity generator G2 = sum_a P_a W_a(mu), W_ij a combination of the 12
     symmetric bilinears in (h, d xi) and (xi, d h).  Demand {C_g(N), lam1 G1 + G2} at degree 1 (same order eps as
     the matter phi^2 bracket in B14's power counting h ~ eps, phi ~ eps^(1/2)) = C^(1)(s1 xi.dN + s2 N div xi),
     with C_g = N[kin - K (R1 + [sqrt g R]^(2))].  Report the solution space for (mu, s1, s2).
C13  same with K2 != K1: the lapse coefficient becomes s1 = -lam1 K2/K1 (cone = K2/(4 alpha) after the chain).
"""
from __future__ import annotations

import sympy as sp

import b19_continuum as bc
from b19_jets import J, D, KEY, bracket, degree_part, functional_zero_eqs, DIM

check, RES = bc.check, bc.RES
hs, COMP, PN, GRAV, CONJ, PHASE = bc.hs, bc.COMP, bc.PN, bc.GRAV, bc.CONJ, bc.PHASE
XI, N, eps, lam1, K1, K2 = bc.XI, bc.N, bc.eps, bc.lam1, bc.K1, bc.K2


def symbol_of_quadratic(dens, hnames):
    """Fourier symbol: int d^a h_A d^b h_B -> Re[(-i)^|a| i^|b|] p^(a+b) h_A h_B (real amplitudes, symmetrised)."""
    p = sp.symbols("p0:3")
    hm = {}
    for (i, j) in COMP:
        hm[bc.HN[(i, j)]] = sp.Symbol(f"H{i}{j}")
    out = 0
    for t in sp.Add.make_args(sp.expand(dens)):
        coef, jets = sp.Integer(1), []
        for b, e in t.as_powers_dict().items():
            if b in KEY and KEY[b][0] in hnames:
                jets += [KEY[b]] * int(e)
            else:
                coef *= b ** e
        assert len(jets) == 2, t
        (f1, a1), (f2, a2) = jets
        ph = sp.re(sp.expand((-sp.I) ** sum(a1) * sp.I ** sum(a2)))
        mon = sp.Mul(*[p[k] ** (a1[k] + a2[k]) for k in range(3)])
        out += coef * ph * mon * hm[f1] * hm[f2]
    return sp.expand(out), p, hm


def c11(R2):
    s, p, hm = symbol_of_quadratic(R2, set(bc.HN.values()))
    Hm = sp.Matrix(3, 3, lambda i, j: hm[bc.HN[(min(i, j), max(i, j))]])
    pv = sp.Matrix(p)
    p2 = sum(x ** 2 for x in p)
    tr = Hm.trace()
    b62 = -(p2 / 4) * (Hm.T * Hm).trace() + sp.Rational(1, 2) * (Hm * pv).dot(Hm * pv) - sp.Rational(1, 2) * (pv.T * Hm * pv)[0] * tr + (p2 / 4) * tr ** 2
    check("C11", sp.expand(s - b62) == 0, "[sqrt g R]^(2) of g = delta + h has exactly block 62's Fierz-Pauli symbol R_2: the 09-24/block-101 member carries the SAME K on R1 and R2 (K1 = K2) -- the GR relation, supplied by block 62, not by closure")


def W_basis(x):
    h = lambda i, j: hs(i, j)
    trh = sum(h(k, k) for k in range(DIM))
    dx = lambda i, j: D(x[j], i)          # d_i xi_j
    div = sum(dx(k, k) for k in range(DIM))
    dh = lambda k, i, j: D(h(i, j), k)
    dtr = lambda k: D(trh, k)
    dl = lambda i, j: 1 if i == j else 0
    B = []
    B.append(lambda i, j: sum(x[k] * dh(k, i, j) for k in range(DIM)))                                   # T1 xi.d h_ij
    B.append(lambda i, j: sum(h(i, k) * dx(j, k) + h(j, k) * dx(i, k) for k in range(DIM)))               # T2 h_ik d_j xi_k + (ij)
    B.append(lambda i, j: sum(h(k, i) * dx(k, j) + h(k, j) * dx(k, i) for k in range(DIM)))               # T3 h_ki d_k xi_j + (ij)
    B.append(lambda i, j: dl(i, j) * sum(h(k, l) * dx(k, l) for k in range(DIM) for l in range(DIM)))     # T4
    B.append(lambda i, j: dl(i, j) * trh * div)                                                            # T5
    B.append(lambda i, j: h(i, j) * div)                                                                    # T6
    B.append(lambda i, j: trh * (dx(i, j) + dx(j, i)))                                                      # T7
    B.append(lambda i, j: dl(i, j) * sum(x[k] * dtr(k) for k in range(DIM)))                                # T8
    B.append(lambda i, j: sum(x[k] * (dh(i, j, k) + dh(j, i, k)) for k in range(DIM)))                     # T9
    B.append(lambda i, j: dl(i, j) * sum(x[k] * dh(l, k, l) for k in range(DIM) for l in range(DIM)))     # T10
    B.append(lambda i, j: x[i] * dtr(j) + x[j] * dtr(i))                                                    # T11
    B.append(lambda i, j: sum(x[i] * dh(k, k, j) + x[j] * dh(k, k, i) for k in range(DIM)))               # T12
    return B


def G2gen(x, mu):
    B = W_basis(x)
    return sp.expand(sum(J(PN[(i, j)]) * sum(mu[n] * B[n](i, j) for n in range(len(B))) for (i, j) in COMP))


def c12(R1, R2):
    mu = sp.symbols("mu1:13")
    s1, s2 = sp.symbols("s1 s2")
    # sanity: the Lie form is T1 + T2
    lie_ok = sp.expand(G2gen(XI, [1, 1] + [0] * 10) - bc.G2(XI)) == 0
    for (K2v, tag) in ((K1, "C12"), (K2, "C13")):
        C = N * (-K1 * R1 - K2v * R2)
        lhs = degree_part(bracket(C, lam1 * bc.G1(XI) + G2gen(XI, mu), CONJ), GRAV, 1)
        Np = s1 * sum(XI[k] * D(N, k) for k in range(DIM)) + s2 * N * sum(D(XI[k], k) for k in range(DIM))
        eqs = functional_zero_eqs(lhs - Np * (-K1 * R1), PHASE)
        sol = sp.solve(eqs, list(mu) + [s1, s2], dict=True)
        print(f"   {tag} solution:", sol)
        if len(sol) != 1:
            check(tag, False, f"unexpected solution structure {sol}")
            continue
        S = sol[0]
        free = sorted({str(s) for v in S.values() for s in sp.sympify(v).free_symbols if str(s).startswith("mu")} |
                      {str(m) for m in mu if m not in S})
        # field-dependent reparametrisations xi -> xi + v(h, xi): G1[v] with v_j = h_jk xi_k (T9+T2) or tr h xi_j (T11+T7)
        if tag == "C12":
            ok = lie_ok and sp.simplify(S[s1] + lam1) == 0 and S[s2] == 0
            # check: generic solution minus lam1*(T1+T2) lies in span{T9+T2, T11+T7}
            gen = [S.get(m, m) for m in mu]
            a, b = sp.symbols("a_ b_")
            target = [lam1, lam1] + [0] * 10
            span = [0] * 12
            span[8] += a; span[1] += a; span[10] += b; span[6] += b
            diff = [sp.expand(gen[n] - target[n] - span[n]) for n in range(12)]
            sol_ab = sp.solve(diff, [a, b] + [sp.Symbol(f) for f in free], dict=True)
            ok = ok and len(sol_ab) >= 1
            # the three free directions: W with R1(W) == 0 identically (invisible to this bracket)
            nulls = []
            for m in [sp.Symbol(f) for f in free]:
                v = [sp.diff(gen[n], m) for n in range(12)]
                Bs = W_basis(XI)
                W = {(i, j): sum(v[n] * Bs[n](i, j) for n in range(12)) for i in range(DIM) for j in range(DIM)}
                r1W = sp.expand(sum(D(D(W[(i, j)], i), j) for i in range(DIM) for j in range(DIM))
                                - sum(D(D(sum(W[(k, k)] for k in range(DIM)), l), l) for l in range(DIM)))
                nulls.append(r1W == 0)
            ok = ok and all(nulls)
            check(tag, ok, f"with block 62's R2 (K2 = K1): degree-1 {{C_g, lam1 G1 + G2(mu)}} closes iff the lapse rule is s1 = -lam1, s2 = 0 (UNIQUE) and G2 = lam1 * int P L_xi h (Lie completion T1+T2) + a 3-parameter family {free} of pieces W with R1(W) == 0 identically ({nulls}; two are the reparametrisations G1[v], v = h.xi, tr h xi) that this bracket cannot see: the lapse rule, hence the matter normalisation via C6, is FORCED at order eps relative to the linear gauge shift")
        else:
            ok = sp.simplify(S[s1] + lam1 * K2 / K1) == 0 and S[s2] == 0
            check(tag, ok, f"K2 != K1: closure forces s1 = -lam1 K2/K1 (and G2 scaled by K2/K1): the lapse rule tracks the graviton potential, so (C6) lam_s = lam1 K2/K1 and (C5) v_s^2 = K2/(4 alpha) = graviton speed^2 (C8)")


if __name__ == "__main__":
    SR = bc.sqrtg_R()
    R1 = sp.expand(SR).coeff(eps, 1)
    R2 = sp.expand(SR).coeff(eps, 2)
    c11(R2)
    c12(R1, R2)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
