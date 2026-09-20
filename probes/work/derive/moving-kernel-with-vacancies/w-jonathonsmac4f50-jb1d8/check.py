#!/usr/bin/env python3
"""moving-kernel-with-vacancies, attempt 4 of 4: removing attempt a3's half-filling floor.

Provenance: the only prior attempt, a3 (w-jonathonsmac4f50-jb416), is BY ME - same model family,
machine and running worker, finished minutes before this one was claimed.  I do not re-run its
route.  a3 proves that the infrared bound with vacancies is <|sigma(k)|^2> <= 1/(beta rho_2 E(k))
with rho_2 the occupied-occupied BOND density, so that long-range order needs beta rho_2 rho >
3G(0); its binding constraint is that the only unconditional tie between the densities is
rho_2 >= 2 rho - 1, which is VACUOUS at rho <= 1/2, and its section 4 names exactly one cheap
executable item: find out how much room there is between rho_2 and that bound.  This attempt runs
that item exactly, and the answer removes the floor.

  V1  the occupation marginal after summing out the contents                 exact
  V2  the FKG lattice condition for that marginal, over ALL pairs of subsets  exact
  V3  rho_2 vs rho^2 vs 2 rho - 1, scanning fugacity and coupling             exact
  V4  what that does to a3's threshold
"""
import sys
from itertools import product, combinations
from fractions import Fraction as F
import sympy as sp

def torus2(L):
    sites = [(i, j) for i in range(L) for j in range(L)]
    bonds = []
    for (i, j) in sites:
        bonds.append(((i, j), ((i + 1) % L, j)))
        bonds.append(((i, j), (i, (j + 1) % L)))
    return sites, bonds

def ring(n):
    sites = [(i,) for i in range(n)]
    bonds = [((i,), ((i + 1) % n,)) for i in range(n)]
    return sites, bonds

def ZA(occ, sites, bonds, w):
    """Ising partition function of the two-valued contents on the induced subgraph `occ`."""
    occ = set(occ)
    inner = [(x, y) for (x, y) in bonds if x in occ and y in occ]
    lst = sorted(occ)
    idx = {x: n for n, x in enumerate(lst)}
    tot = F(0)
    for cfg in product([1, -1], repeat=len(lst)):
        wt = F(1)
        for (x, y) in inner:
            wt *= w if cfg[idx[x]] == cfg[idx[y]] else 1/w
        tot += wt
    return tot

def densities(sites, bonds, w, z):
    """exact rho and rho_2 for the law with vacancies at fugacity z"""
    N, B = len(sites), len(bonds)
    Z = F(0); occ_tot = F(0); oo_tot = F(0)
    for mask in range(1 << N):
        occ = [sites[i] for i in range(N) if mask >> i & 1]
        wt = (z**len(occ))*ZA(occ, sites, bonds, w)
        Z += wt
        occ_tot += wt*len(occ)
        oset = set(occ)
        oo_tot += wt*sum(1 for (x, y) in bonds if x in oset and y in oset)
    return occ_tot/(Z*N), oo_tot/(Z*B)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("V1  the occupation marginal")
    print("     Summing the contents out of the law with vacancies leaves a measure on the")
    print("     OCCUPIED SET alone:   mu(A)  proportional to  z^|A| Z_A,   where Z_A is the")
    print("     content partition function on the subgraph induced by A (for the two-valued menu,")
    print("     an Ising partition function).  Every question about rho and rho_2 is a question")
    print("     about mu.  Checked on a ring of 4 at w = e^beta = 2, z = 1:")
    sites, bonds = ring(4)
    want(ZA([], sites, bonds, F(2)) == 1 and ZA([(0,)], sites, bonds, F(2)) == 2,
         "     Z_empty = 1 and Z_{one site} = 2 (two contents, no bonds)")
    z2 = ZA([(0,), (1,)], sites, bonds, F(2))
    want(z2 == 2*(F(2) + F(1, 2)),
         f"     Z_{{two adjacent}} = {z2} = 2(w + 1/w) - the bond is counted once")

    print("\nV2  the FKG lattice condition for the occupation marginal")
    print("     If mu(A u B) mu(A n B) >= mu(A) mu(B) for all subsets A, B, then the occupation")
    print("     variables are positively associated, and rho_2 >= rho^2 follows at once.  The")
    print("     condition is checked here EXACTLY over every ordered pair of subsets:")
    for (name, (ss, bb)), w, z in [(("ring of 6", ring(6)), F(2), F(1)),
                                   (("ring of 6", ring(6)), F(3), F(1, 2)),
                                   (("ring of 8", ring(8)), F(2), F(2)),
                                   (("3x3 torus", torus2(3)), F(2), F(1))]:
        N = len(ss)
        mu = {}
        for mask in range(1 << N):
            occ = frozenset(ss[i] for i in range(N) if mask >> i & 1)
            mu[mask] = (z**len(occ))*ZA(occ, ss, bb, w)
        bad = 0
        for A in range(1 << N):
            for B in range(A, 1 << N):
                if mu[A | B]*mu[A & B] < mu[A]*mu[B]:
                    bad += 1
        want(bad == 0,
             f"     {name}, w = {w}, z = {z}: all {(1 << N)*((1 << N) + 1)//2} pairs satisfy it "
             f"({bad} violations)")
    print("     So on every instance tested the marginal is log-supermodular, which is the")
    print("     hypothesis of the FKG inequality.  Given FKG (ASSUMED as a theorem, not re-proved")
    print("     here), 1[x occupied] and 1[y occupied] are increasing functions of the occupied")
    print("     set, hence positively correlated, hence")
    print("       rho_2  >=  rho^2    for every bond.")

    print("\nV3  the two bounds against the truth")
    print("     Exact densities on a 3x3 torus, scanning the fugacity and the coupling:")
    ss, bb = torus2(3)
    rows = []
    for w in (F(1), F(2), F(4)):
        for z in (F(1, 8), F(1, 4), F(1, 2), F(1), F(2)):
            rho, rho2 = densities(ss, bb, w, z)
            rows.append((w, z, rho, rho2))
            print(f"       w = {w}, z = {z}:  rho = {float(rho):.6f}   rho_2 = {float(rho2):.6f}"
                  f"   rho^2 = {float(rho*rho):.6f}   2rho-1 = {float(2*rho - 1):+.6f}")
    want(all(r2 >= r*r for (_, _, r, r2) in rows),
         f"     rho_2 >= rho^2 in all {len(rows)} cases, exactly - the FKG prediction holds")
    want(all(r2 >= 2*r - 1 for (_, _, r, r2) in rows),
         "     rho_2 >= 2 rho - 1 also holds, as it must, but:")
    low = [(w, z, r, r2) for (w, z, r, r2) in rows if r < F(1, 2)]
    want(len(low) > 0 and all(2*r - 1 < 0 <= r*r <= r2 for (_, _, r, r2) in low),
         f"     in the {len(low)} cases with rho < 1/2 the bound 2 rho - 1 is NEGATIVE and says")
    print("       nothing, while rho^2 is positive and correct.  That is exactly a3's floor, and")
    print("       it is an artefact of the inequality, not of the law.")
    worst = min(rows, key=lambda t: float(t[3]/(t[2]*t[2])))
    want(worst[3] >= worst[2]*worst[2],
         f"     the tightest case is w = {worst[0]}, z = {worst[1]}, where rho_2/rho^2 = "
         f"{float(worst[3]/(worst[2]*worst[2])):.6f} >= 1")

    print("\nV4  what this does to a3's threshold")
    print("     a3 gives  M^2 >= rho - 3G(0)/(beta rho_2)  and long-range order once")
    print("     beta rho_2 rho > 3G(0).  With rho_2 >= 2 rho - 1 that reads")
    print("       beta > 3G(0)/(rho(2 rho - 1)),   which needs rho > 1/2.")
    print("     With rho_2 >= rho^2 it reads instead")
    print("       beta > 3G(0)/rho^3,   which needs nothing of rho at all.")
    G3 = sp.Rational(76, 100)
    prev, tbl = None, []
    for rv in (sp.Rational(1, 4), sp.Rational(2, 5), sp.Rational(1, 2),
               sp.Rational(3, 5), sp.Rational(9, 10), 1):
        new = sp.nsimplify(G3/rv**3)
        old = sp.nsimplify(G3/(rv*(2*rv - 1))) if rv > sp.Rational(1, 2) else None
        tbl.append((rv, new, old))
        print(f"       rho = {rv}:  beta > {float(new):.4f} (from rho^2)" +
              (f"   vs {float(old):.4f} (from 2rho-1)" if old else
               "   vs NO STATEMENT (from 2rho-1)"))
    want(all(tbl[i][1] > tbl[i + 1][1] for i in range(len(tbl) - 1)),
         "     the new threshold decreases with rho and is finite at every positive density,")
    want(sp.simplify(tbl[-1][1] - G3) == 0,
         "     and at rho = 1 it is 3G(0) = 0.76, still recovering block 19 exactly")
    for rv, new, old in tbl:
        if old is not None:
            strict = rv < 1
            want((new < old) if strict else (new == old),
                 f"     at rho = {rv} the new threshold {float(new):.4f} is "
                 + (f"BELOW the old {float(old):.4f}" if strict else
                    f"EQUAL to the old {float(old):.4f}, as it must be since rho^2 = 2rho-1 "
                    f"at rho = 1"))
    want(sp.Rational(1, 2)**2 > 2*sp.Rational(1, 2) - 1,
         "     the two bounds cross only at rho = 1: rho^2 > 2 rho - 1 for every rho < 1, so the")
    print("       improvement is everywhere, not only below half filling.")

    print()
    if ok:
        print("SUMMARY: PARTIAL - attempt a3's half-filling floor is an artefact of its "
              "inequality, not of the law: summing the contents out leaves an occupation marginal "
              "mu(A) proportional to z^|A| Z_A, and this marginal satisfies the FKG lattice "
              "condition mu(AuB)mu(AnB) >= mu(A)mu(B) on every instance tested - all pairs of "
              "subsets of rings of 6 and 8 and of a 3x3 torus, at several couplings and "
              "fugacities - so by FKG (ASSUMED) the occupation variables are positively "
              "associated and rho_2 >= rho^2, which is positive at every density where 2 rho - 1 "
              "is negative; checked exactly in 15 further cases on the 3x3 torus, including every "
              "case with rho < 1/2; a3's long-range-order criterion beta rho_2 rho > 3G(0) then "
              "reads beta > 3G(0)/rho^3, finite at every positive density, strictly below a3's "
              "3G(0)/(rho(2rho-1)) wherever the latter exists, and still equal to 3G(0) at rho = 1"
              )
        print("HIT: the occupation marginal of the law with vacancies is log-supermodular on every "
              "instance checked, so FKG gives rho_2 >= rho^2 for the occupied-occupied bond "
              "density, and attempt a3's threshold beta > 3G(0)/(rho(2 rho - 1)) - which exists "
              "only above half filling - is replaced by beta > 3G(0)/rho^3, which is finite at "
              "EVERY positive density and strictly smaller wherever both are defined; a3's "
              "rho > 1/2 floor came from inclusion-exclusion being the only tie it had between "
              "the site and bond densities, and it does not survive the correlation input")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
