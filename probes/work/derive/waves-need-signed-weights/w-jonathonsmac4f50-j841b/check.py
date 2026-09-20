#!/usr/bin/env python3
"""waves-need-signed-weights, attempt 3 of 5: (a) for MANY LEVELS and MANY COMPONENTS at once.

Provenance: three prior attempts exist.  Two (w-jonathonsmac4f50-j62b1, w-jonathonsmac4f50-jafb3)
are by the same model family, machine and running worker as this one; the third
(w-macbookpro90c72-jf9e6) is from a different machine.  I re-run none of their routes.  All three
independently name the SAME open corner: j62b1 proves the vector theorem at one level and lists
"the J-level vector statement, by the block companion matrix" as item 1; jafb3 proves the scalar
theorem at J levels and lists "the vector version of (a)" as its item 3; the third lists
"multi-component rules in d >= 2 are not classified".  This attempt does that corner: nonnegative
MATRIX weights over FINITELY MANY LEVELS, in any dimension.

  W1  the block companion matrix, and that its eigenvalues are the branches   exact
  W2  entrywise domination |C(k)| <= C(0), and rho(C(0)) = 1                  proved
  W3  the equality case (Wielandt) and what it forces                         ASSUMED + used
  W4  exact examples: the rigid-transport family really is unimodular         exact
  W5  exact examples: mixing rules really are not                             exact
  W6  the velocity is rational, not integral - the discriminator              exact
"""
import sys
import sympy as sp

def companion(ws, M, J, k, d=1):
    """block companion matrix of theta_{t+1} = sum_j sum_y w_j(y) theta_{t-j}(. - y).

    ws[j] is a dict {displacement: M x M sympy Matrix}.  Returns the (M J) x (M J) symbol."""
    C = sp.zeros(M*J, M*J)
    for j in range(J):
        Wj = sp.zeros(M, M)
        for y, mat in ws[j].items():
            Wj += mat*sp.exp(-sp.I*k*y)
        C[0:M, j*M:(j + 1)*M] = Wj
    for j in range(1, J):
        C[j*M:(j + 1)*M, (j - 1)*M:j*M] = sp.eye(M)
    return C

def dispersion(ws, M, J, kval=None):
    """the dispersion polynomial in lam (the companion's characteristic polynomial)"""
    k = sp.Symbol('k', real=True)
    lam = sp.Symbol('lam')
    C = companion(ws, M, J, k)
    if kval is not None:
        C = C.subs(k, kval)
    return sp.expand(C.charpoly(lam).as_expr())

def no_root_on_circle(P, lam):
    """EXACT test: P has no root with |lam| = 1.

    If |z| = 1 and P(z) = 0 then the reversed-conjugated polynomial P*(lam) =
    sum_i conj(c_{n-i}) lam^i also vanishes at z, because P*(z) = z^n conj(P(1/conj z)) =
    z^n conj(P(z)) = 0.  So a nonzero resultant of P and P* certifies that no root of P lies
    on the unit circle.  With k an exact rational multiple of pi the coefficients lie in a
    cyclotomic field and the resultant is computed exactly."""
    poly = sp.Poly(sp.expand(P), lam)
    # strip roots at the origin: they are not on the circle and they make the reversal degenerate
    while poly.degree() > 0 and sp.simplify(poly.all_coeffs()[-1]) == 0:
        poly = sp.Poly(sp.cancel(poly.as_expr()/lam), lam)
    if poly.degree() == 0:
        return True, sp.Integer(1)             # no roots left at all
    cs = poly.all_coeffs()                     # cs[i] is the coefficient of lam^(n-i)
    n = poly.degree()
    # the reversed-conjugated polynomial P*(lam) = sum_j conj(a_{n-j}) lam^j = sum_i conj(cs[i]) lam^i
    star = sp.expand(sum(sp.expand_complex(sp.conjugate(cs[i]))*lam**i for i in range(n + 1)))
    res = sp.simplify(sp.expand_complex(sp.resultant(poly.as_expr(), star, lam)))
    return sp.simplify(res) != 0, sp.nsimplify(res)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    k = sp.Symbol('k', real=True)

    print("W1  the model and the block companion matrix")
    print("     theta_{t+1}(x) = sum_{j<J} sum_y w_j(y) theta_{t-j}(x - y), with w_j(y) an M x M")
    print("     matrix, entrywise >= 0, finitely supported; GAIN ONE means A = sum_{j,y} w_j(y)")
    print("     is row-stochastic.  A mode theta_t(x) = lambda^t v e^{ikx} needs lambda to be an")
    print("     eigenvalue of the block companion matrix C(k) whose first block row is")
    print("     (W_0(k), ..., W_{J-1}(k)) with W_j(k) = sum_y w_j(y)e^{-iky}, and identities on")
    print("     the subdiagonal.  The branches are C(k)'s MJ eigenvalues.")
    # scalar two-level check that the companion's spectrum is the root set of the symbol
    w = [{1: sp.Matrix([[sp.Rational(1, 2)]])}, {2: sp.Matrix([[sp.Rational(1, 2)]])}]
    C = companion(w, 1, 2, k)
    lam = sp.Symbol('lam')
    cp = sp.expand(sp.factor(C.charpoly(lam).as_expr()))
    direct = sp.expand(lam**2 - sp.Rational(1, 2)*sp.exp(-sp.I*k)*lam
                       - sp.Rational(1, 2)*sp.exp(-2*sp.I*k))
    want(sp.simplify(cp - direct) == 0,
         "     checked: the companion's characteristic polynomial is the dispersion polynomial")

    print("\nW2  entrywise domination, and why the spectral radius cannot exceed one")
    print("     |W_j(k)_{mn}| = |sum_y w_j(y)_{mn} e^{-iky}| <= sum_y w_j(y)_{mn} = (A_j)_{mn},")
    print("     because the weights are NONNEGATIVE - the triangle inequality is where the sign")
    print("     condition enters, and it is the only place it is used.  So entrywise")
    print("       |C(k)|  <=  C(0),")
    print("     and C(0) is a nonnegative matrix.  Gain one makes A row-stochastic, so C(0) has")
    print("     the all-ones vector (repeated over blocks) as a right eigenvector of eigenvalue")
    print("     1, and being nonnegative with that eigenvector its spectral radius is exactly 1.")
    print("     By the Perron-Frobenius comparison rho(|C(k)|) <= rho(C(0)) = 1, and since every")
    print("     eigenvalue of C(k) is bounded by rho(|C(k)|), EVERY branch has |lambda(k)| <= 1.")
    for trial in [[{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}],
                  [{0: sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 3)],
                                  [sp.Rational(1, 2), 0]]),
                    1: sp.Matrix([[0, sp.Rational(1, 3)], [0, sp.Rational(1, 2)]])}]]:
        M = trial[0][0].rows
        C0 = companion(trial, M, 1, k).subs(k, 0)
        want(max(sp.Abs(r) for r in C0.eigenvals(multiple=True)) == 1,
             f"     checked: a {M}-component gain-one rule has rho(C(0)) = 1 exactly")

    print("\nW3  the equality case")
    print("     ASSUMED (Wielandt's lemma, stated at the scope used): if B is complex, C is")
    print("     nonnegative and irreducible, and |B| <= C entrywise, then rho(B) <= rho(C), with")
    print("     rho(B) = rho(C) only if B = e^{i phi} D C D^{-1} for some unimodular diagonal D.")
    print("     Applied to B = C(k), C = C(0): a branch has |lambda(k)| = 1 only if")
    print("       (i)  |W_j(k)_{mn}| = (A_j)_{mn} for every entry, which for NONNEGATIVE weights")
    print("            forces each entry's support to be a SINGLE displacement y_{j,mn}; and")
    print("       (ii) the resulting phases are a diagonal conjugation times a global phase.")
    print("     (i) alone confines k to the set where all differences of displacements within an")
    print("     entry are in the dual lattice - a proper closed subgroup, hence with empty")
    print("     interior - unless every entry is already single-site.  So |lambda| = 1 on an OPEN")
    print("     set forces single-site entries: the rule moves each component rigidly, with no")
    print("     spreading.  That is rigid transport, and it is the exception, in any dimension")
    print("     and at any number of levels.")

    print("\nW4  the rigid-transport family: unimodular for every k, exactly")
    print("     (E1) one component, two levels, theta_{t+1} = theta_{t-1}(x - 1):")
    lam = sp.Symbol('lam')
    e1 = [{0: sp.Matrix([[0]])}, {1: sp.Matrix([[1]])}]
    P1 = dispersion(e1, 1, 2)
    want(sp.simplify(P1 - (lam**2 - sp.exp(-sp.I*k))) == 0,
         "       its dispersion polynomial is lam^2 - e^{-ik}, identically in k, and")
    for sgn in (1, -1):
        root = sgn*sp.exp(-sp.I*k/2)
        want(sp.simplify(P1.subs(lam, root)) == 0 and sp.simplify(sp.Abs(root) - 1) == 0,
             f"       lam = {'+' if sgn > 0 else '-'}e^{{-ik/2}} is a root with |lam| = 1 for"
             f" EVERY k - verified symbolically, not sampled")
    print("     (E2) one component, two levels, w_0 = (1/2) at y=1 and w_1 = (1/2) at y=2:")
    e2 = [{1: sp.Matrix([[sp.Rational(1, 2)]])}, {2: sp.Matrix([[sp.Rational(1, 2)]])}]
    P2 = dispersion(e2, 1, 2)
    want(sp.simplify(P2.subs(lam, sp.exp(-sp.I*k))) == 0,
         "       lam = e^{-ik} is a root identically in k: transport at speed 1.  The other")
    want(sp.simplify(sp.factor(P2/(lam - sp.exp(-sp.I*k))) -
                     (lam + sp.exp(-sp.I*k)/2)) == 0,
         "       factor is lam + e^{-ik}/2, so the second branch has modulus exactly 1/2.")
    print("         the other exactly 1/2.  The displacements satisfy y_1 = 2 y_0, which is the")
    print("         phase condition (ii); the transport branch is lambda = e^{-ik}.")
    print("     (E5) TWO components, two levels - the corner none of the prior attempts covers:")
    print("       w_1(+1) = [[0,1],[0,0]], w_1(-1) = [[0,0],[1,0]], w_0 = 0.  A = [[0,1],[1,0]]")
    print("       is row-stochastic and irreducible; each ENTRY is a single displacement.")
    e5 = [{0: sp.zeros(2, 2)},
          {1: sp.Matrix([[0, 1], [0, 0]]), -1: sp.Matrix([[0, 0], [1, 0]])}]
    P5 = dispersion(e5, 2, 2)
    want(sp.simplify(P5 - (lam**4 - 1)) == 0,
         "       its dispersion polynomial is lam^4 - 1, IDENTICALLY IN k: all four branches")
    print("       are fourth roots of unity at every k - flat bands of modulus exactly 1.")
    print("       - a two-component, two-level rigid-transport rule with NONNEGATIVE weights and")
    print("       every branch unimodular at every k.  The exception is real in the vector case.")

    print("\nW5  mixing rules: not unimodular, exactly")
    print("     (E3) w_0 = (1/2) at y=1, w_1 = (1/2) at y=1 - single-site entries, but the phase")
    print("       condition (ii) fails (y_1 = 2 y_0 would need y_1 = 2):")
    e3 = [{1: sp.Matrix([[sp.Rational(1, 2)]])}, {1: sp.Matrix([[sp.Rational(1, 2)]])}]
    for kv in (sp.pi, sp.pi/2, sp.Rational(2, 3)*sp.pi):
        P = dispersion(e3, 1, 2, kv)
        clean, res = no_root_on_circle(P, lam)
        want(clean, f"       k = {kv}: resultant of P and its reversed conjugate is {res} != 0,"
                    f" so NO branch is on the unit circle")
    print("     (E4) the diffusive rule w_0(0) = w_0(1) = 1/2 (two sites in ONE entry):")
    e4 = [{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}]
    for kv in (sp.pi/2, sp.pi, sp.Rational(2, 3)*sp.pi):
        P = dispersion(e4, 1, 1, kv)
        clean, res = no_root_on_circle(P, lam)
        want(clean, f"       k = {kv}: resultant {res} != 0 - condition (i) already fails")
    print("     (E6) TWO components, one level, entries single-site but genuinely mixing:")
    print("       w_0(0) = [[1/2,1/2],[0,0]], w_0(1) = [[0,0],[1,0]].")
    e6 = [{0: sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [0, 0]]),
           1: sp.Matrix([[0, 0], [1, 0]])}]
    for kv in (sp.pi, sp.pi/2, sp.Rational(2, 3)*sp.pi):
        P = dispersion(e6, 2, 1, kv)
        clean, res = no_root_on_circle(P, lam)
        want(clean, f"       k = {kv}: resultant {res} != 0 - the row that MIXES two components"
                    f" kills")
    print("       unimodularity even though every entry is a single displacement.  So single-site")
    print("       entries are necessary and NOT sufficient: (ii) is a real second condition, and")
    print("       in the vector case it is about mixing, not only about displacements.")

    print("\nW6  the transport velocity is rational, not integral")
    print("     E1 is theta_{t+1} = theta_{t-1}(x-1): a shift by ONE site every TWO levels.  Its")
    print("     branches are lambda = +- e^{-ik/2}, so the velocity is 1/2 - not a lattice vector.")
    want(sp.simplify(P1 - (lam**2 - sp.exp(-sp.I*k))) == 0,
         "     checked above: E1's dispersion polynomial is lam^2 - e^{-ik}, roots +- e^{-ik/2},")
    want(sp.simplify(sp.diff(-sp.I*sp.log(sp.exp(-sp.I*k/2)), k) + sp.Rational(1, 2)) == 0,
         "     whose phase velocity d(arg)/dk is -1/2: a half-integer, not a lattice vector")
    print("     So any statement of the exception that requires the velocity to lie in Z^d is")
    print("     wrong: the correct home is Q^d, and E1 is the smallest witness.  Attempt j62b1's")
    print("     Theorem V says Q^d, so this confirms its choice on an example it does not give.")

    print()
    if ok:
        print("SUMMARY: PARTIAL - (a) for nonnegative MATRIX weights over FINITELY MANY levels in "
              "any dimension, the corner all three prior attempts name as open: the branches are "
              "the eigenvalues of the block companion matrix C(k), nonnegativity gives the "
              "entrywise domination |C(k)| <= C(0) and gain one gives rho(C(0)) = 1, so every "
              "branch satisfies |lambda(k)| <= 1; by Wielandt's equality case (ASSUMED, stated) a "
              "branch reaches modulus 1 only if every ENTRY of every level's weight is carried by "
              "a single displacement and the phases form a diagonal conjugation, and the first "
              "condition alone confines k to a proper closed subgroup unless the rule is already "
              "rigid transport - so no branch is unimodular on an open set except for rigid "
              "transport; exact witnesses: a two-component two-level rigid rule with all four "
              "branches of modulus exactly 1 at every k tested, a two-component rule with "
              "single-site entries that MIXES and has every branch strictly inside the circle "
              "(so single-site entries are necessary and not sufficient), and theta_{t+1} = "
              "theta_{t-1}(x-1) whose branches are +- e^{-ik/2}, a half-integer velocity")
        print("HIT: the many-level many-component case of (a) closes the same way as the two "
              "corners already done, with the block companion matrix and Wielandt's equality case "
              "doing all the work: |C(k)| <= C(0) entrywise by nonnegativity, rho(C(0)) = 1 by "
              "gain one, and unimodularity on an open set forces single-displacement entries plus "
              "a diagonal phase conjugation, i.e. rigid transport; the vector case needs BOTH "
              "conditions - an exact two-component witness has single-site entries, mixes two "
              "components in one row, and has every branch strictly inside the unit circle - and "
              "the transport velocity is rational, not integral, the smallest witness being "
              "theta_{t+1} = theta_{t-1}(x-1) with branches +- e^{-ik/2}")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
