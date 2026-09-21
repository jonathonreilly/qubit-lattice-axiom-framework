#!/usr/bin/env python3
"""bodies-that-slow-records-without-keeping-them, attempt 2 of 4: the slowing strength cancels
out of the condition for the attraction to be usable.

No prior attempt existed on this problem at claim time.  Blocks 48/49/51/52 are taken as the unit
states them (same model family).

Setting: inertial record gas, contents v = m s with s a unit direction and m in (0,1]; a record
hops to x + sign(s_k) e_k at rate m |s_k|/sqrt 3.  A SLOWING site lets the record pass and
multiplies its content by kappa in (0,1), taking the momentum (1-kappa) v and keeping no record.

  B1  block 48's hitting probability, and which simplex measure its constant uses
  B2  (a) the shadow: densities, and what is and is not conserved        exact
  B3  (b) the pull between two slowing sites; action and reaction        exact
  B4  (c) the price, and the inequality - in which kappa CANCELS         exact
"""
import sys
import sympy as sp

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    f1, f2 = sp.symbols('f1 f2', positive=True)
    kap, kap1, kap2, rho, h, m2, m1 = sp.symbols(
        'kappa kappa_1 kappa_2 rho h m2 m1', positive=True)

    print("B1  block 48's hitting probability and its shell constant")
    print("     For the directed walk with step frequencies f, the probability of hitting the")
    print("     origin from x is the multinomial h(x,f) = (n!/prod x_k!) prod f_k^{x_k}, n = |x|_1.")
    print("     Integrating it over the simplex of step frequencies:")
    def shell_int(x, measure):
        n = sum(x); f3 = 1 - f1 - f2
        hh = sp.factorial(n)/sp.prod([sp.factorial(k) for k in x])*f1**x[0]*f2**x[1]*f3**x[2]
        return sp.simplify(sp.integrate(sp.integrate(measure*hh, (f2, 0, 1 - f1)), (f1, 0, 1)))
    for n, xs in ((2, [(2,0,0), (1,1,0)]), (3, [(3,0,0), (2,1,0), (1,1,1)]),
                  (4, [(2,1,1), (2,2,0)])):
        vals = {shell_int(x, 2) for x in xs}
        want(len(vals) == 1 and vals.pop() == sp.Rational(2, (n+1)*(n+2)),
             f"     shell n = {n}: the integral is the SAME at every site listed, and equals "
             f"2/(({n}+1)({n}+2)) = {sp.Rational(2,(n+1)*(n+2))}")
    print("     The shell-constancy is block 48's substantive claim and it holds exactly.  On the")
    print("     VALUE, a note on convention: with the uniform PROBABILITY measure on the simplex")
    print("     (density 2 on a triangle of area 1/2) the constant is 2/((n+1)(n+2)); with plain")
    print("     Lebesgue measure it is 1/((n+1)(n+2)), which is the form the unit quotes.  Both")
    print("     are correct; the statement needs the measure named, and this script uses the")
    print("     probability measure throughout.")

    print("\nB2  (a) the shadow of one slowing site")
    print("     A record that has passed the slowing site carries kappa v and therefore HOPS at")
    print("     kappa times its old rate.  The number flux through every site is unchanged, so to")
    print("     carry the same flux at a lower speed the slowed population must be denser by")
    print("     exactly 1/kappa.  Writing h = h(x,s) for the fraction of the flux at x that came")
    print("     through the origin:")
    n_un, n_sl = rho*(1 - h), rho*h/kap
    dens = sp.simplify(n_un + n_sl)
    want(sp.simplify(dens - rho*(1 + h*(1/kap - 1))) == 0,
         f"       density   = {sp.simplify(dens)} = rho (1 + h(1/kappa - 1)) - the shadow is DENSER")
    v = sp.Symbol('v', positive=True)
    flux = sp.simplify(n_un*v + n_sl*(kap*v))
    want(sp.simplify(flux - rho*v) == 0,
         f"       number flux = {flux} = rho v - UNCHANGED, as it must be")
    print("       momentum density = the SAME expression, because in this model the velocity is")
    print("         proportional to the content: sum(density x velocity) and sum(density x content)")
    print("         are literally the same sum.  That is not a second check, it is one fact read")
    print("         twice, and it is why the extra records exactly make up for their smaller")
    print("         contents.")
    cur = sp.simplify(n_un*v*v + n_sl*(kap*v)*(kap*v))
    want(sp.simplify(cur - rho*v**2*(1 - h*(1 - kap))) == 0,
         f"       momentum CURRENT = {sp.factor(cur)} = rho v^2 (1 - h(1-kappa))")
    print("     - and THAT is the shadow: the number current and the momentum density are both")
    print("     untouched, while the momentum current is short by exactly rho v^2 h (1 - kappa).")
    print("     A slowing body casts a shadow in momentum flux and in nothing else, which is why")
    print("     it can pull without growing.")

    print("\nB3  (b) two slowing sites")
    print("     A second slowing site takes (1 - kappa_2) of the momentum current reaching it.")
    print("     The isotropic part of that current is the same from every direction and cancels;")
    print("     what survives is the deficit B2 computed, which is (1 - kappa_1) h times the")
    print("     current, so the net push on site 2 is")
    F = (1 - kap1)*(1 - kap2)*rho*m2*h
    print(f"       F_2 = {F}   (times block 48's geometric factor; m2 = <m^2>)")
    want(sp.simplify(F.subs({kap1: kap2, kap2: kap1}, simultaneous=True) - F) == 0,
         "     This is SYMMETRIC under exchanging the two bodies (checked by a simultaneous swap),")
    print("       and block 48's geometric factor")
    print("       depends only on the separation, so ACTION AND REACTION ARE EQUAL AND OPPOSITE.")
    print("     (Contrast the halo of a producing lump, where the response depends on one body's")
    print("      production and the other's size and the pair law is not symmetric.)")
    print("     Neither body grows: a slowing site keeps no record, by the definition of the")
    print("     clause, so the capture rate is identically zero and block 49's tie between")
    print("     attraction and growth is evaded - the momentum is taken from the gas, not the")
    print("     records.")
    print("     The magnitude carries the weight <m^2>, not <m>: the momentum current is")
    print("     quadratic in the content, so a gas of slow records pulls much more weakly than")
    print("     its number density suggests.")

    print("\nB4  (c) the price, and the inequality")
    nb, sig, M, rr = sp.symbols('n_b sigma M r', positive=True)
    u = sp.Symbol('u', positive=True)        # u = 1 - kappa, positive since 0 < kappa < 1
    print("     Each passage multiplies m by kappa, so along a path a record meets n_b sigma per")
    print("     unit length and its speed decays at the rate n_b sigma <m> (1 - kappa):")
    tau_e = 1/(nb*sig*m1*u)
    print(f"       run-down time      tau = {tau_e}   with u = 1 - kappa   (LINEAR in u)")
    Fpair = u**2*rho*m2/rr**2
    print(f"       pull between a pair F  = {Fpair}   (QUADRATIC in u)")
    t_app = sp.sqrt(rr*M/Fpair)
    t_app = sp.simplify(t_app)
    want(sp.simplify(t_app - sp.sqrt(M*rr**3/(rho*m2))/u) == 0,
         f"       approach time      t = sqrt(r M / F) = {t_app}")
    print("     The attraction is usable only if the pair closes before the gas runs down, t < tau:")
    cond = sp.simplify((t_app/tau_e)**2)
    want(sp.simplify(cond - M*rr**3*nb**2*sig**2*m1**2/(rho*m2)) == 0,
         f"       (t/tau)^2 = {sp.factor(cond)}")
    want(sp.simplify(sp.diff(cond, u)) == 0,
         "     and KAPPA HAS CANCELLED: the condition does not depend on the slowing strength at")
    print("       all.  The pull is quadratic in 1 - kappa and the run-down linear, and the")
    print("       approach time goes as the inverse first power, so the two cancel exactly.")
    print("     The inequality is therefore")
    print("       M r^3 n_b^2 sigma^2 <m>^2  <  rho <m^2>,")
    print("     i.e. a gas can sustain attraction out to")
    print("       r^3 < rho <m^2> / (M n_b^2 sigma^2 <m>^2),")
    print("     which is set by the DENSITY of slowing sites and the gas's <m^2>/<m>^2, and not")
    print("     by how hard any one of them slows.  Making the slowers gentler buys exactly as")
    print("     much life for the gas as it costs in pull.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on attraction without growth: a slowing site leaves the number "
              "current and the momentum DENSITY exactly unchanged - the slowed population is "
              "denser by 1/kappa and carries kappa times the content, and the two compensate - "
              "while the momentum CURRENT is short by exactly rho v^2 h (1 - kappa), so a slowing "
              "body casts a shadow in momentum flux and in nothing else, which is how it pulls "
              "without capturing anything; the push on a second slowing site is (1 - kappa_1)"
              "(1 - kappa_2) rho <m^2> h times block 48's geometric factor, symmetric under "
              "exchange so action and reaction are equal and opposite, and weighted by <m^2> "
              "rather than <m>; and for the price, the run-down of the gas is LINEAR in 1 - kappa "
              "while the pull is QUADRATIC, but the approach time goes as the inverse first power, "
              "so kappa cancels exactly from the usability condition, leaving "
              "M r^3 n_b^2 sigma^2 <m>^2 < rho <m^2> - a bound set by the density of slowing "
              "sites and the gas's <m^2>/<m>^2, not by how hard any one site slows.  Block 48's "
              "shell constant is confirmed to be the same at every site of a shell, with the "
              "value 2/((n+1)(n+2)) under the uniform probability measure on the simplex and "
              "1/((n+1)(n+2)) under Lebesgue - the form the unit quotes")
        print("HIT: the strength of a slowing body cancels out of the condition for its "
              "attraction to be usable - the pull between two slowing sites is quadratic in "
              "1 - kappa while the gas's run-down is linear in it, and since the approach time "
              "scales as the inverse first power the two cancel exactly, leaving the "
              "kappa-independent inequality M r^3 n_b^2 sigma^2 <m>^2 < rho <m^2>; the mechanism "
              "is that a slowing site leaves the number current and the momentum density exactly "
              "unchanged (the slowed records are denser by 1/kappa and carry kappa times the "
              "content) and shortens only the momentum CURRENT, by exactly rho v^2 h (1 - kappa), "
              "so it pulls without capturing and its pair force, weighted by <m^2>, is symmetric "
              "under exchange and therefore obeys action and reaction")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
