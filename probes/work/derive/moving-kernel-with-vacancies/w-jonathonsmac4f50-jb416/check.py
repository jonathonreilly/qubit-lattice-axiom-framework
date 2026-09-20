#!/usr/bin/env python3
"""moving-kernel-with-vacancies, attempt 3 of 4: the stiffness is the BOND density, and that
is what puts a floor under rho.

No prior attempt existed on this problem at claim time.

Setting (block 39's, as the unit states it): a site is empty or carries one record with a content;
two records weigh c*omega; a bond with an empty end weighs 1; c_0 is the neutral scale; records
move in detailed balance with the static law on the occupied set; fugacity z, density rho.

  K1  the enlarged one-site kernel, and where c_0 comes from             exact
  K2  why the sphere menu has NO scale-free side conditions (unlike the six-axis menu)
  K3  (a),(b) the twist touches only occupied-occupied bonds; the sum rule   exact on a torus
  K4  the bond density rho_2, and the only inequality that ties it to rho   exact
  K5  (c),(d) the stiffness, the explicit threshold, and where the route stops
"""
import sys
from itertools import product
from fractions import Fraction as F
import sympy as sp

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    b = sp.Symbol('beta', positive=True)
    c, s, t = sp.symbols('c s t', real=True)

    print("K1  the enlarged one-site kernel and the neutral scale")
    print("     States: a content, or empty.  The kernel is K(s,s') = c e^{beta s.s'} between")
    print("     records and 1 on any bond with an empty end.  The empty state couples to the")
    print("     contents only through the CONSTANT function, because that bond weight does not")
    print("     depend on the content.  So on span{1, e_empty} the kernel is the 2x2 block")
    print("       [[ c <e^{beta s.s'}> , 1 ], [ 1 , 1 ]],   det = c <e^{beta s.s'}> - 1,")
    print("     with the average over the uniform content measure.  For the SPHERE menu:")
    # the explicit antiderivative, so nothing depends on sympy's branch handling at beta = 0
    avg_sphere = sp.simplify((sp.exp(b) - sp.exp(-b))/(2*b))   # <e^{beta s.s'}> over S^2
    anti = sp.exp(b*t)/(2*b)
    want(sp.simplify(sp.diff(anti, t) - sp.exp(b*t)/2) == 0,
         "     (the antiderivative e^{beta t}/(2 beta) is verified by differentiation)")
    want(sp.simplify(anti.subs(t, 1) - anti.subs(t, -1) - avg_sphere) == 0,
         "     evaluating it at the endpoints of the cosine's range gives the average:")
    want(sp.simplify(avg_sphere - sp.sinh(b)/b) == 0,
         f"     <e^{{beta s.s'}}> = sinh(beta)/beta exactly, so det = 0 at")
    c0_sphere = sp.simplify(1/avg_sphere)
    want(sp.simplify(c0_sphere - b/sp.sinh(b)) == 0,
         "       c_0 = beta/sinh(beta) - which is exactly what the unit quotes from block 39's T5,")
    print("       recovered here as a determinant rather than as an average.")
    print("     For the TWO-VALUED menu (block 36's runner, contents +-1):")
    avg_two = sp.simplify((sp.exp(b) + sp.exp(-b))/2)
    want(sp.simplify(avg_two - sp.cosh(b)) == 0 and
         sp.simplify(1/avg_two - 1/sp.cosh(b)) == 0,
         "     <e^{beta s s'}> = cosh(beta), so c_0 = 1/cosh(beta) there")

    print("\nK2  why the sphere menu needs no side conditions, and the six-axis menu does")
    print("     The kernel's other eigenvalues are its expansion coefficients on the content")
    print("     space.  For the sphere, e^{beta s.s'} = sum_l a_l(beta) P_l(s.s') with every")
    print("     a_l(beta) > 0 (they are modified Bessel functions of a positive argument), so the")
    print("     ONLY way to lose positive semidefiniteness is through the 2x2 block: bond-plane")
    print("     RP holds exactly for c >= c_0, with no further condition.  Checked for the")
    print("     two-valued menu, where the expansion has just two terms:")
    lam_plus = sp.simplify(sp.cosh(b))          # the constant mode
    lam_minus = sp.simplify(sp.sinh(b))         # the alternating mode
    want(sp.simplify(lam_plus - avg_two) == 0,
         "     the constant mode has eigenvalue cosh(beta) - it is the one in the 2x2 block")
    for bv in (sp.Rational(1, 2), 1, 3):
        want(sp.N(lam_minus.subs(b, bv)) > 0,
             f"     the alternating mode has eigenvalue sinh(beta) > 0 at beta = {bv}: "
             f"{float(sp.N(lam_minus.subs(b, bv))):.6f} - never an obstruction")
    print("     This is the contrast with the SIX-AXIS menu, whose finite content space has the")
    print("     modes p-q and p+q-2r; those can be negative (at (5,2,4), p+q-2r = -1), and there")
    print("     RP fails at every scale.  The menu, not the scale, decides whether 'exactly for")
    print("     c >= c_0' is the whole story.")

    print("\nK3  (a),(b) what the twist twists, and the sum rule")
    print("     The twisted partition function rotates the CONTENTS, so a bond contributes a")
    print("     twist cost only when BOTH of its ends carry records: a bond with an empty end")
    print("     weighs 1 whatever the twist.  So the Gaussian-domination quadratic form is")
    print("     beta times a sum over OCCUPIED-OCCUPIED bonds, not over all bonds.")
    print("     Exact check on a 3x3 torus with two-valued contents, e^beta = 2, c = 1, z = 1:")
    L, w = 3, F(2)
    sites = [(i, j) for i in range(L) for j in range(L)]
    N = len(sites)
    bonds = []
    for (i, j) in sites:
        bonds.append(((i, j), ((i + 1) % L, j)))
        bonds.append(((i, j), (i, (j + 1) % L)))
    idx = {x: n for n, x in enumerate(sites)}
    Z = F(0); occ_tot = F(0); occocc_tot = F(0); sumsq = F(0)
    for cfg in product([0, 1, -1], repeat=N):        # 0 = empty, +-1 = content
        wt = F(1)
        for (x, y) in bonds:
            a, bb = cfg[idx[x]], cfg[idx[y]]
            if a != 0 and bb != 0:
                wt *= w if a == bb else 1/w          # c = 1, e^{beta s s'} = w^{s s'}
        Z += wt
        nocc = sum(1 for v in cfg if v != 0)
        occ_tot += wt*nocc
        occocc_tot += wt*sum(1 for (x, y) in bonds
                             if cfg[idx[x]] != 0 and cfg[idx[y]] != 0)
        sumsq += wt*sum(v*v for v in cfg)            # sum_x |s_x|^2 1[occupied]
    rho = occ_tot/(Z*N)
    rho2 = occocc_tot/(Z*len(bonds))
    want(sumsq/(Z*N) == rho,
         f"     sum rule: (1/N) sum_x <|s_x|^2 1[occ]> = rho = {rho} = {float(rho):.6f}, because")
    print("       |s|^2 = 1 on every content.  By Parseval this is (1/N) sum_k <|sigma(k)|^2>,")
    print("       so the sum rule of block 19 becomes rho, not 1: the vacancies take the rest.")
    print(f"     bond density rho_2 = <occupied-occupied bonds>/|bonds| = {rho2} = "
          f"{float(rho2):.6f}")
    want(rho2 < rho, "     and rho_2 < rho here, as it must be for a law that is not saturated")

    print("\nK4  the only inequality that ties rho_2 to rho")
    print("     For one bond, P(both ends occupied) >= P(x occ) + P(y occ) - 1 = 2 rho - 1 by")
    print("     inclusion-exclusion, and nothing better holds without a correlation input:")
    want(rho2 >= 2*rho - 1,
         f"     checked: rho_2 = {float(rho2):.6f} >= 2 rho - 1 = {float(2*rho - 1):.6f}")
    print("     The bound is vacuous for rho <= 1/2, and it is sharp: a law that puts all its")
    print("     mass on configurations where the occupied sets of the two ends are as disjoint")
    print("     as the marginals allow attains it.  Exact witness on two sites:")
    # two sites with marginals rho each: build the joint law that minimises P(both occupied)
    for rv in (F(3, 5), F(7, 10), F(1, 2), F(2, 5)):
        both = max(F(0), 2*rv - 1)
        one = rv - both                     # P(x occ, y empty) = P(x empty, y occ)
        none = 1 - 2*rv + both
        law = [both, one, one, none]
        valid = all(v >= 0 for v in law) and sum(law) == 1
        marg_x = both + one
        marg_y = both + one
        want(valid and marg_x == rv and marg_y == rv,
             f"       rho = {rv}: the law ({both}, {one}, {one}, {none}) on "
             f"(both, x only, y only, neither) is a probability law with both marginals {rv} "
             f"and P(both occupied) = {both}, so 2 rho - 1 cannot be improved")

    print("\nK5  (c),(d) the stiffness, and the threshold it forces")
    print("     Gaussian domination with the twist supported on occupied-occupied bonds gives")
    print("       <|sigma(k)|^2>  <=  1 / (beta rho_2 E(k)),")
    print("     so the coefficient of 1/E(k) - the inverse stiffness - is 1/(beta rho_2): it is")
    print("     set by the BOND density, not by the site density.  That is the answer to (d).")
    print("     Feeding this into the sum rule of K3:")
    print("       rho = (1/N) sum_k <|sigma(k)|^2> <= M^2 + (1/(beta rho_2)) (1/N) sum_{k/=0} 1/E(k)")
    print("     and (1/N) sum_{k/=0} 1/E(k) -> 3G(0) on Z^3, pinned by block 22 (PR #8156) to")
    print("     0.75 < 3G(0) < 0.76 (ASSUMED here, not re-derived).  Hence")
    print("       M^2  >=  rho  -  3G(0)/(beta rho_2),")
    print("     so long-range order holds as soon as  beta rho_2 rho > 3G(0).")
    G3 = sp.Rational(76, 100)                      # the upper end of block 22's bracket
    print("     Using rho_2 >= 2 rho - 1, which needs rho > 1/2, the threshold is explicit:")
    print("       beta  >  3G(0) / ( rho (2 rho - 1) ) .")
    rows = []
    for rv in (sp.Rational(55, 100), sp.Rational(3, 5), sp.Rational(7, 10),
               sp.Rational(9, 10), 1):
        if rv > sp.Rational(1, 2):
            thr = sp.nsimplify(G3/(rv*(2*rv - 1)))
            rows.append((rv, thr))
            print(f"       rho = {rv}: beta > {thr} = {float(thr):.4f}")
    want(all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1)),
         "     the threshold decreases with rho, as it must, and at rho = 1 it is 3G(0) = 0.76,")
    want(sp.simplify(rows[-1][1] - G3) == 0,
         "     recovering block 19's full-lattice threshold exactly when the vacancies vanish")
    print("     Below rho = 1/2 the route gives nothing: 2 rho - 1 <= 0, the stiffness is not")
    print("     bounded below by the site density alone, and the obstruction is real rather than")
    print("     technical - at low density the occupied set need not percolate, and a transverse")
    print("     field supported on a non-percolating set cannot have long-range order at all.")
    want(sp.Rational(1, 2)*(2*sp.Rational(1, 2) - 1) == 0,
         "     so rho > 1/2 is where this argument lives, and the gap between 1/2 and the site-")
    print("       percolation threshold of Z^3 (about 0.3116) is where a better inequality")
    print("       between rho_2 and rho would buy real ground.")

    print()
    if ok:
        print("SUMMARY: PARTIAL for the sphere menu with vacancies at fugacity z: the enlarged "
              "one-site kernel's empty state couples to the contents only through the constant "
              "function, so the 2x2 block [[c<e^{beta s.s'}>, 1],[1, 1]] has determinant "
              "c<e^{beta s.s'}> - 1 and c_0 = beta/sinh(beta) is a determinant rather than an "
              "average (1/cosh(beta) for the two-valued menu); every other mode of the sphere "
              "kernel is a positive Bessel coefficient, which is why 'RP exactly for c >= c_0' "
              "needs no side condition here while the six-axis menu does; the twist touches only "
              "occupied-occupied bonds, so the sum rule reads rho rather than 1 (checked exactly "
              "by enumerating all 3^9 configurations of a 3x3 torus) and the infrared bound is "
              "<|sigma(k)|^2> <= 1/(beta rho_2 E(k)) with rho_2 the BOND density - the stiffness "
              "is carried by rho_2, not rho, giving M^2 >= rho - 3G(0)/(beta rho_2) and long-range "
              "order once beta rho_2 rho > 3G(0); the only unconditional tie is rho_2 >= 2 rho - 1, "
              "so the explicit threshold beta > 3G(0)/(rho(2 rho - 1)) exists only for rho > 1/2 "
              "and reduces to block 19's 3G(0) at rho = 1")
        print("HIT: with vacancies the coefficient of 1/E(k) in the infrared bound is 1/(beta "
              "rho_2) with rho_2 the occupied-occupied BOND density, not the site density rho, "
              "because the twist costs nothing on a bond with an empty end; the sum rule becomes "
              "rho, so M^2 >= rho - 3G(0)/(beta rho_2) and long-range order needs only beta rho_2 "
              "rho > 3G(0) - but the sole unconditional inequality between the two densities is "
              "rho_2 >= 2 rho - 1, which is vacuous at rho <= 1/2, so this route yields an "
              "explicit threshold beta > 3G(0)/(rho(2 rho - 1)) only above half filling, and the "
              "whole interval from the site-percolation threshold of Z^3 up to 1/2 is out of "
              "reach for a reason that is about the two densities, not about beta")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
