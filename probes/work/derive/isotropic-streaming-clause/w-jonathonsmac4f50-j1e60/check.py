#!/usr/bin/env python3
"""isotropic-streaming-clause, attempt 2 of 3: isotropic rates exist, and the anisotropy was
never about the axes.

No prior attempt existed on this problem at claim time.

Setting (block 51, as the unit states it): a record of content s (a unit vector) steps to
x + sign(s_k) e_k at rate |s_k|/sqrt 3.  The streaming operator to second order is
(1/sqrt 3)[-s.grad + (1/2) sum_k |s_k| d_k^2]; the sphere moments are <|s_k|> = 1/2,
<s_i^2 |s_i|> = 1/4, <s_i^2 |s_k|> = 1/8, and the viscous term carries a cubic piece.
The unit asks for rates a(s,d) on the 26 neighbours, non-negative, with mean displacement
proportional to s, whose fourth-rank moment <s_i s_j (sum_d a(s,d) d_k d_l)> is isotropic.

  S1  the current rule: why its fourth-rank moment is not isotropic          exact
  S2  the reduction: isotropy holds iff M(s) = sum_d a d d^T is m(s) I       proved
  S3  forward hops along axes only: IMPOSSIBLE                               proved
  S4  axes only, allowing a backward hop: a closed form that works           exact
  S5  forward-only on the 26 neighbours: exact rational witnesses            exact
  S6  (b) what stays and what moves: total rate, capture, the shadow
  S7  (c) the cost of the clause
"""
import sys
from itertools import product, permutations
from fractions import Fraction as F
import sympy as sp

NB = [d for d in product((-1, 0, 1), repeat=3) if any(d)]
AXIS = [d for d in NB if sum(x*x for x in d) == 1]

def moments(a):
    """mean displacement and second moment of a rate dict {d: rate}"""
    mean = sp.zeros(3, 1); M = sp.zeros(3, 3)
    for d, v in a.items():
        dv = sp.Matrix(d); q = sp.Rational(v.numerator, v.denominator) if isinstance(v, F) else v
        mean += q*dv; M += q*(dv*dv.T)
    return sp.simplify(mean), sp.simplify(M)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    s1, s2, s3, lam, kap = sp.symbols('s1 s2 s3 lambda kappa', real=True)
    s = sp.Matrix([s1, s2, s3])

    print("S1  the current rule's fourth-rank moment")
    print("     Axis hops only, one way, rate |s_k|/sqrt3, so sum_d a d_k d_l = delta_kl |s_k|/sqrt3")
    print("     and T_ijkl = <s_i s_j |s_k|> delta_kl / sqrt3.  With the unit's sphere moments:")
    T1111 = sp.Rational(1, 4)/sp.sqrt(3)
    T1122 = sp.Rational(1, 8)/sp.sqrt(3)
    print(f"       T_1111 = <s_1^2|s_1|>/sqrt3 = {T1111}")
    print(f"       T_1122 = <s_1^2|s_2|>/sqrt3 = {T1122}")
    print("       T_1212 = 0                      (delta_kl kills k=1, l=2)")
    print("     An isotropic fourth-rank tensor symmetric in (ij) and (kl) is")
    print("       T = A delta_ij delta_kl + B(delta_ik delta_jl + delta_il delta_jk),")
    print("     so T_1212 = B = 0, forcing T_1111 = A = T_1122.  But")
    want(sp.simplify(T1111 - T1122) != 0,
         f"       T_1111 - T_1122 = {sp.simplify(T1111 - T1122)} != 0: NOT isotropic, as block 51 says")

    print("\nS2  the reduction")
    print("     Write M_kl(s) = sum_d a(s,d) d_k d_l.  If M(s) = m(s) I with m invariant under the")
    print("     cubic group, then T_ijkl = <s_i s_j m(s)> delta_kl, and cubic symmetry alone gives")
    print("     <s_1^2 m> = <s_2^2 m> = <s_3^2 m> and <s_1 s_2 m> = 0, so <s_i s_j m> = (<m>/3)")
    print("     delta_ij and T = (<m>/3) delta_ij delta_kl - isotropic (the B = 0 branch).")
    print("     So it is ENOUGH to make the hop second moment a multiple of the identity at each")
    print("     content.  That is the condition the rest of this script works with.")
    ta, pa = sp.symbols('vartheta varphi', positive=True)
    sv = [sp.sin(ta)*sp.cos(pa), sp.sin(ta)*sp.sin(pa), sp.cos(ta)]
    def avg(e):
        return sp.simplify(sp.integrate(sp.integrate(e*sp.sin(ta), (ta, 0, sp.pi)),
                                        (pa, 0, 2*sp.pi))/(4*sp.pi))
    print("     First, the unit's sphere moments, recomputed here rather than taken on trust:")
    want(avg(sp.Abs(sv[2])) == sp.Rational(1, 2), "       <|s_k|>       = 1/2")
    want(avg(sv[2]**2*sp.Abs(sv[2])) == sp.Rational(1, 4), "       <s_i^2 |s_i|> = 1/4")
    want(avg(sv[0]**2*sp.Abs(sv[2])) == sp.Rational(1, 8), "       <s_i^2 |s_k|> = 1/8  (i /= k)")
    print("     - all three agree with block 51, so S1's arithmetic rests on checked numbers.")
    print("     Now the reduction itself, on a non-constant cubic invariant m = s_1^4+s_2^4+s_3^4:")
    minv = sv[0]**4 + sv[1]**4 + sv[2]**4
    want(avg(sv[0]*sv[1]*minv) == 0, "       <s_1 s_2 m> = 0")
    want(avg(sv[0]**2*minv) == avg(sv[2]**2*minv) == sp.Rational(1, 5),
         "       <s_1^2 m> = <s_3^2 m> = 1/5")
    print("     so <s_i s_j m> = (<m>/3) delta_ij for a cubic-invariant m, as claimed, and the")
    print("     fourth-rank moment is isotropic whenever M(s) = m(s) I.")

    print("\nS3  forward hops along the axes only: impossible")
    print("     Take s = e_1.  The only axis neighbour with s.d > 0 is d = (1,0,0), so")
    print("       M = a (1,0,0)(1,0,0)^T = diag(a, 0, 0),")
    a = sp.Symbol('a', positive=True)
    Mx = sp.diag(a, 0, 0)
    want(sp.simplify(Mx - Mx[0, 0]*sp.eye(3)) != sp.zeros(3, 3),
         "     which is a multiple of the identity only if a = 0, i.e. the record never moves.")
    print("     So NO forward-only rule on the axis neighbours alone can be isotropic.  This is")
    print("     the sense in which the unit's 'the cubic term comes from hops along lattice axes")
    print("     only' is right - but S4 shows it is the FORWARD-ONLY part that is doing the work.")

    print("\nS4  axes only, if a record may also step backwards")
    print("     Take a(s, +-e_k) = lambda (1 +- kappa s_k), non-negative for every unit s when")
    print("     kappa <= 1 since |s_k| <= 1.  Then")
    mean4 = sp.zeros(3, 1); M4 = sp.zeros(3, 3)
    for k in range(3):
        for sg in (1, -1):
            d = sp.zeros(3, 1); d[k] = sg
            rate = lam*(1 + kap*sg*s[k])
            mean4 += rate*d; M4 += rate*(d*d.T)
    want(sp.simplify(mean4 - 2*lam*kap*s) == sp.zeros(3, 1),
         "       mean displacement = 2 lambda kappa s   (proportional to s, as required)")
    want(sp.simplify(M4 - 2*lam*sp.eye(3)) == sp.zeros(3, 3),
         "       second moment      = 2 lambda I        (a multiple of I, INDEPENDENT of s)")
    print("     The total rate is 6 lambda, also independent of s.  By S2 the fourth-rank moment")
    print("     is isotropic, with no diagonal neighbours used at all.")
    print("     So the anisotropy of the current clause is NOT caused by restricting hops to the")
    print("     axes.  It is caused by the rate |s_k| being ONE-WAY: the second moment then")
    print("     inherits the content's direction.  A two-way linear rate on the same six")
    print("     neighbours removes it exactly.")

    print("\nS5  forward-only on the full 26-neighbour set: exact witnesses")
    print("     If backward steps are refused (a(s,d) = 0 whenever s.d <= 0), diagonals become")
    print("     necessary by S3.  They are also sufficient.  Exact rational rates, symmetrised")
    print("     over the stabiliser of s in the cubic group, normalised to m = 1:")
    W = {
        (1, 0, 0): {(1, 1, 1): F(1,4), (1, 1, -1): F(1,4), (1, -1, 1): F(1,4), (1, -1, -1): F(1,4)},
        (1, 1, 0): {(0, 1, 0): F(1,2), (1, 0, 0): F(1,2), (0, 1, 1): F(1,4), (0, 1, -1): F(1,4),
                    (1, 0, 1): F(1,4), (1, 0, -1): F(1,4)},
        (1, 1, 1): {(1, 1, 0): F(1,5), (1, 0, 1): F(1,5), (0, 1, 1): F(1,5),
                    (1, -1, 1): F(1,5), (-1, 1, 1): F(1,5), (1, 1, -1): F(1,5)},
    }
    for sv, a in W.items():
        sm = sp.Matrix(sv)
        mean, M = moments(a)
        par = sp.simplify(mean.cross(sm)) == sp.zeros(3, 1)
        iso = sp.simplify(M - M[0, 0]*sp.eye(3)) == sp.zeros(3, 3)
        nn = all(v >= 0 for v in a.values())
        fw = all((sm.T*sp.Matrix(d))[0] > 0 for d in a)
        want(par and iso and nn and fw,
             f"     s = {sv}: {len(a)} neighbours, mean = {tuple(mean)} parallel to s, "
             f"M = {M[0,0]} I, all rates >= 0, every hop forward")
    print("     The s = (1,0,0) witness is the clean one: rate 1/4 on each of the four body")
    print("     diagonals (1,+-1,+-1).  Their mean is (1,0,0) and their second moment is exactly")
    print("     I, because each has d_k^2 = 1 in every coordinate and the signs cancel pairwise.")
    print("     Generic directions work too (checked separately by exact rational programming at")
    print("     (3,2,1) and (5,1,1); those rates are not symmetric and are not reproduced here).")

    print("\nS6  (b) what stays and what moves")
    tot = {sv: sum(a.values()) for sv, a in W.items()}
    for sv, t in tot.items():
        print(f"     total hop rate at s = {sv}: {t}")
    want(len(set(tot.values())) > 1,
         "     the total rate is NOT the same at every content for these witnesses, so 'one event")
    print("       per record' does not come for free: a rule with a content-dependent total rate")
    print("       changes the event clock, and the uniform product measure's stationarity has to")
    print("       be re-argued rather than inherited from block 44.  By contrast S4's rule has")
    print("       total rate 6 lambda at every content, so it keeps a single event clock.")
    print("     Capture: block 48's law |s|_1 counts records stepping onto a site, which for axis")
    print("     hops is sum_k |s_k|.  Under S4 the analogous count is sum over the six axis")
    print("     neighbours of lambda(1 -+ kappa s_k) = 6 lambda MINUS the flux 2 lambda kappa s.n,")
    print("     so capture becomes affine in s rather than |s|_1 - a different law.  NOT verified")
    print("     here against a simulator.")
    print("     Collisionless shadow: NOT computed.  The shadow is a statement about straight-line")
    print("     transport behind a body, and S4's rule makes every record diffuse as well as")
    print("     stream, so the shadow should soften; I have not measured it.")

    print("\nS7  (c) the cost")
    print("     Three different prices, one per construction:")
    print("       S4 (axes, two-way): records step BACKWARDS against their content at positive")
    print("         rate.  Cheapest in geometry (no new neighbours, six as before, one event")
    print("         clock) and most expensive in reading: a record's content no longer determines")
    print("         the direction it moves, only the direction it moves ON AVERAGE.")
    print("       S5 (forward-only, 26 neighbours): the owner's reading is preserved - a record")
    print("         only ever steps somewhere it is heading - at the cost of diagonal neighbours,")
    print("         so the lattice's adjacency is no longer the nearest-neighbour graph the other")
    print("         clauses use, and the total rate varies with content.")
    print("       Keeping the present clause: the wind stays anisotropic, which is block 51's")
    print("         finding and the reason the unit exists.")
    print("     Nothing here chooses between them; that is the owner's call.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the isotropic streaming clause: non-negative rates with mean "
              "displacement proportional to s and an isotropic fourth-rank moment DO exist, and "
              "the anisotropy of the present clause is not caused by restricting hops to the "
              "lattice axes. The fourth-rank moment is isotropic as soon as the hop second moment "
              "M(s) = sum_d a(s,d) d d^T is a multiple of the identity with a cubic-invariant "
              "coefficient, since cubic symmetry then gives T = (<m>/3) delta_ij delta_kl. "
              "Forward hops on the axes alone cannot do it (at s = e_1 the only forward axis "
              "neighbour gives M = diag(a,0,0)), but the two-way axis rule a(s,+-e_k) = "
              "lambda(1 +- kappa s_k), non-negative for kappa <= 1, has mean displacement exactly "
              "2 lambda kappa s and second moment exactly 2 lambda I independent of s, using no "
              "diagonal neighbours at all; while if backward steps are refused, exact rational "
              "forward-only witnesses on the 26 neighbours exist, the cleanest being rate 1/4 on "
              "each of the four body diagonals (1,+-1,+-1) at s = (1,0,0), whose mean is (1,0,0) "
              "and whose second moment is exactly I. The two constructions differ in cost: the "
              "two-way axis rule keeps one event clock (total rate 6 lambda at every content) but "
              "lets records step backwards, whereas the forward-only rule preserves the owner's "
              "reading but needs diagonal neighbours and has a content-dependent total rate")
        print("HIT: the cubic viscous term of the streaming clause is NOT a consequence of hops "
              "being along lattice axes - it is a consequence of the rate |s_k| being one-way. "
              "The two-way axis rule a(s, +-e_k) = lambda(1 +- kappa s_k) is non-negative for "
              "every unit s when kappa <= 1, has mean displacement exactly 2 lambda kappa s and "
              "hop second moment exactly 2 lambda I independent of s, so by cubic symmetry its "
              "fourth-rank sphere moment is isotropic, and it uses only the six axis neighbours; "
              "forward-only rules cannot be isotropic on the axes alone (at s = e_1 the second "
              "moment is diag(a,0,0)) but do exist on the 26 neighbours, with exact rational "
              "witnesses such as rate 1/4 on each body diagonal (1,+-1,+-1) at s = (1,0,0) giving "
              "mean (1,0,0) and second moment exactly I")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
