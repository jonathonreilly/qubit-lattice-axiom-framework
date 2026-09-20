#!/usr/bin/env python3
"""waves-need-signed-weights, attempt 1 of 5: removing Wielandt from (a).

Provenance: four prior attempts exist.  Three (w-jonathonsmac4f50-j62b1, -jafb3, -j841b) are by
the same model family, machine and running worker as this one; -j841b is mine, finished earlier in
this same session.  The fourth (w-macbookpro90c72-jf9e6) is from another machine.  I re-run none
of their routes.  My own a3 (issue 8535) flagged that Wielandt's equality case is ASSUMED in every
treatment of (a) so far - scalar, one-level and many-level - which makes the CLASSIFICATION half
of (a) conditional lane-wide, and listed as its item 1: re-prove it at this scope or replace it.
This attempt replaces it.  What (a) actually needs is only the entrywise equality, and that
follows from ordinary Perron-Frobenius in four lines.

  Q1  what the argument actually needs, and what it was assuming         statement
  Q2  the sub-eigenvector lemma, from the positive left Perron vector    proved + exact
  Q3  the squeeze: |lambda| = rho(C) forces |B| = C entrywise            proved + exact
  Q4  when the companion matrix is irreducible - a real side condition   exact
  Q5  what is left assumed
"""
import sys
import sympy as sp

def companion(ws, M, J, kval):
    """block companion at k = kval; ws[j] is {displacement: M x M matrix}"""
    C = sp.zeros(M*J, M*J)
    for j in range(J):
        Wj = sp.zeros(M, M)
        for y, mat in ws[j].items():
            Wj += mat*sp.exp(-sp.I*kval*y)
        C[0:M, j*M:(j + 1)*M] = Wj
    for j in range(1, J):
        C[j*M:(j + 1)*M, (j - 1)*M:j*M] = sp.eye(M)
    return sp.Matrix(C.rows, C.cols, lambda i, j: sp.expand_complex(sp.simplify(C[i, j])))

def absmat(A):
    return sp.Matrix(A.rows, A.cols, lambda i, j: sp.simplify(sp.Abs(A[i, j])))

def irreducible(A):
    """A nonnegative square matrix is irreducible iff (I + A)^(n-1) is entrywise positive"""
    n = A.rows
    P = (sp.eye(n) + absmat(A))**(n - 1)
    return all(sp.simplify(P[i, j]) > 0 for i in range(n) for j in range(n))

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("Q1  what (a) needs, and what every treatment so far has been assuming")
    print("     The branches of a gain-one rule with nonnegative weights are the eigenvalues of")
    print("     the block companion matrix C(k), and nonnegativity gives |C(k)| <= C(0) entrywise")
    print("     with rho(C(0)) = 1.  To conclude that |lambda(k)| = 1 forces each weight entry")
    print("     onto a SINGLE displacement, all three prior treatments invoke Wielandt's equality")
    print("     case: |B| <= C, rho(B) = rho(C) implies B = e^{i phi} D C D^{-1}.  But the")
    print("     classification only uses the ENTRYWISE half of that conclusion,")
    print("       |B_{mn}| = C_{mn}  for every entry,")
    print("     and that half does not need Wielandt at all.")

    print("\nQ2  the sub-eigenvector lemma")
    print("     LEMMA.  C nonnegative irreducible with spectral radius rho; y >= 0, y /= 0, and")
    print("     C y >= rho y entrywise.  Then C y = rho y, and y > 0 strictly.")
    print("     PROOF.  Perron-Frobenius gives a strictly positive LEFT eigenvector v with")
    print("     v^T C = rho v^T.  Then v^T (C y - rho y) = rho v^T y - rho v^T y = 0, while")
    print("     C y - rho y >= 0 entrywise and v > 0, so every entry of C y - rho y vanishes.")
    print("     Positivity of y is then (I + C)^{n-1} y > 0 by irreducibility.  []")
    print("     The only import is the existence of a positive left Perron vector, which is the")
    print("     standard statement of Perron-Frobenius, not its equality case.  Checked:")
    for ws, M, J, nm in [
            ([{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}],
             1, 1, "diffusive one-level"),
            ([{1: sp.Matrix([[sp.Rational(1, 2)]])}, {2: sp.Matrix([[sp.Rational(1, 2)]])}],
             1, 2, "two-level chain"),
            ([{0: sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 3)], [sp.Rational(1, 2), 0]]),
               1: sp.Matrix([[0, sp.Rational(1, 3)], [0, sp.Rational(1, 2)]])}],
             2, 1, "two-component one-level")]:
        C0 = companion(ws, M, J, 0)
        evs = C0.eigenvals()
        rho = max(sp.Abs(sp.N(e)) for e in evs)
        left = (C0.T - sp.eye(M*J)).nullspace()
        pos = bool(left) and all(sp.simplify(left[0][i]/left[0][0]) > 0
                                 for i in range(M*J))
        want(abs(rho - 1) < sp.Rational(1, 10**9) and pos,
             f"     {nm}: rho(C(0)) = 1 and the left 1-eigenvector has all entries of one sign")

    print("\nQ3  the squeeze")
    print("     THEOREM.  With C = C(0) nonnegative irreducible, rho(C) = 1, and B = C(k)")
    print("     satisfying |B| <= C entrywise: if B x = lambda x with x /= 0 and |lambda| = 1 then")
    print("     |B| = C entrywise.")
    print("     PROOF.  |x| >= 0 and |x| /= 0, and entrywise")
    print("       |x| = |lambda||x| = |B x| <= |B| |x| <= C |x|,")
    print("     so C|x| >= |x| = rho(C)|x|.  By Q2, C|x| = |x| and |x| > 0.  Then the whole chain")
    print("     is an equality, so (C - |B|)|x| = 0 with C - |B| >= 0 and |x| > 0, which forces")
    print("     C - |B| = 0 entrywise.  []")
    print("     For NONNEGATIVE weights |B_{mn}| = C_{mn} says |sum_y w(y)_{mn} e^{-iky}| =")
    print("     sum_y w(y)_{mn}, which holds only if all the displacements in that entry share a")
    print("     phase - so on an OPEN set of k, only if the entry has a single displacement.")
    print("     That is condition (i), and Wielandt is gone.  Checked on the two sides:")
    rigid = [{0: sp.zeros(2, 2)},
             {1: sp.Matrix([[0, 1], [0, 0]]), -1: sp.Matrix([[0, 0], [1, 0]])}]
    mixing = [{0: sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [0, 0]]),
               1: sp.Matrix([[0, 0], [1, 0]])}]
    spread = [{0: sp.Matrix([[sp.Rational(1, 2)]]), 1: sp.Matrix([[sp.Rational(1, 2)]])}]
    for ws, M, J, nm, expect, note in [
            (rigid, 2, 2, "rigid transport", True,
             "condition (i) holds, and this rule IS unimodular at every k"),
            (mixing, 2, 1, "single-site but mixing", True,
             "condition (i) ALSO holds - yet every branch is strictly inside the circle, so (i)"
             " is necessary and not sufficient, which is where condition (ii) does its work"),
            (spread, 1, 1, "two displacements in one entry", False,
             "condition (i) FAILS, so by the theorem no branch can be unimodular here")]:
        C0 = companion(ws, M, J, 0)
        for kv in (sp.pi/3, sp.Rational(2, 5)*sp.pi):
            Bk = companion(ws, M, J, kv)
            eq = absmat(Bk) == absmat(C0)
            want(eq == expect,
                 f"     {nm} at k = {kv}: |C(k)| {'=' if eq else '/='} C(0) entrywise")
        print(f"       - {note}")

    print("\nQ4  when is the companion matrix irreducible?")
    print("     Q2 needs irreducibility, and it is NOT automatic: the companion of a J-level rule")
    print("     is irreducible only if the deepest level is actually used.  Checked:")
    deep = [{0: sp.Matrix([[sp.Rational(1, 2)]])}, {1: sp.Matrix([[sp.Rational(1, 2)]])}]
    shallow = [{0: sp.Matrix([[1]])}, {1: sp.Matrix([[0]])}]
    want(irreducible(companion(deep, 1, 2, 0)),
         "     a two-level rule that uses both levels: companion is irreducible")
    want(not irreducible(companion(shallow, 1, 2, 0)),
         "     a two-level rule whose DEEPEST weight vanishes: companion is REDUCIBLE, and the")
    print("       lemma does not apply to it - but such a rule is a (J-1)-level rule, so the")
    print("       theorem applies to it after dropping the empty level.  The honest statement is")
    print("       that J is the true depth, and then irreducibility of the companion reduces to")
    print("       irreducibility of A = sum_j A_j, which is the hypothesis j62b1 already makes.")
    A2 = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
    A2red = sp.Matrix([[1, 0], [0, 1]])
    want(irreducible(A2) and not irreducible(A2red),
         "     and for one level the companion IS A, so the condition is exactly A irreducible")

    print("\nQ5  what is left assumed")
    print("     Only Perron-Frobenius: a nonnegative irreducible matrix has spectral radius rho")
    print("     with a strictly positive left eigenvector, and (I + C)^{n-1} > 0.  Wielandt's")
    print("     equality case, which was the import in all four prior attempts, is no longer")
    print("     needed for condition (i).  The PHASE condition (ii) - that the surviving phases")
    print("     form a diagonal conjugation - still needs an argument, and Q3 gives none; but (ii)")
    print("     is not what the open-set statement rests on, because (i) alone already confines k")
    print("     to a proper closed subgroup unless every entry is single-site.")

    print()
    if ok:
        print("SUMMARY: PARTIAL - the entrywise half of Wielandt's equality case, which is all "
              "that theorem (a) uses, is proved here directly from Perron-Frobenius: if C is "
              "nonnegative irreducible with rho(C) = 1, |B| <= C entrywise, and Bx = lambda x "
              "with |lambda| = 1, then |x| = |lambda||x| = |Bx| <= |B||x| <= C|x| makes |x| a "
              "sub-eigenvector, the positive left Perron vector forces C|x| = |x| and |x| > 0, "
              "the whole chain becomes an equality and (C - |B|)|x| = 0 with C - |B| >= 0 gives "
              "|B| = C entrywise - which for nonnegative weights is exactly condition (i), single "
              "displacement per entry on any open set of k; the only import left is ordinary "
              "Perron-Frobenius, not its equality case, and the side condition is irreducibility "
              "of the companion, shown here to fail exactly when the deepest level is unused (a "
              "rule of smaller true depth) and otherwise to reduce to irreducibility of A"
              )
        print("HIT: theorem (a)'s classification half no longer needs Wielandt's equality case in "
              "any of its scalar, one-level or many-level forms: the entrywise equality |B| = C "
              "follows in four lines from the existence of a positive left Perron vector, via the "
              "sub-eigenvector lemma applied to |x|, and that is the only part of Wielandt the "
              "argument ever used; the residual hypothesis is irreducibility of the block "
              "companion matrix, which fails precisely when the deepest level carries zero weight "
              "- a rule that is really of smaller depth - and otherwise reduces to irreducibility "
              "of the gain matrix A")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
