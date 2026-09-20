#!/usr/bin/env python3
"""moving-what-fixes-the-scale, attempt 5 of 5: c_0 has a spectral derivation, and the two
facts block 39 gives are one fact.

Provenance: the one prior attempt, a1 (w-jonathonsmac4f50-j882f), is by the same model family,
machine and running worker.  It settles (a), (c) and the SECOND half of (b) (the identification
with block 24's integrated reading - a no-go).  I do not re-run any of those.  Its section 4
names three open items; this attempt takes the two it calls most valuable:

  D1  the 7-state pair-weight matrix and its spectrum                   exact
  D2  (b) first half: c_0 is exactly where the empty/uniform block is singular
  D3  (b) first half: at c_0 the empty state IS the uniform superposition of contents
  D4  bond-plane reflection positivity: what it really requires         (a correction)
  D5  (d) formation-then-motion against formation-in-place              exact no-go
"""
import sys
import sympy as sp

AX = [0, 1, 2, 3, 4, 5]          # +e1,-e1,+e2,-e2,+e3,-e3
def opp(a):
    return a ^ 1

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r, c, z = sp.symbols('p q r c z', positive=True)
    c0 = 6/(p + q + 4*r)

    print("D1  the pair-weight matrix of the law with vacancies")
    print("     A site is empty or carries one of six contents, so the pair weight is a 7x7")
    print("     matrix T: record a with record b weighs c*omega(a,b) (omega = p, q, r for equal,")
    print("     opposite, orthogonal); any bond with an empty end weighs 1.")
    Om = sp.Matrix(6, 6, lambda i, j: p if i == j else (q if j == opp(i) else r))
    T = sp.zeros(7, 7)
    for i in AX:
        for j in AX:
            T[i, j] = c*Om[i, j]
    for i in AX:
        T[i, 6] = 1
        T[6, i] = 1
    T[6, 6] = 1
    want(T.T == T, "     T is symmetric, and the six-axis block is Omega = (p-r)I + (q-r)J + r 11^T")
    ev = Om.eigenvals()
    want(sp.simplify(sum(k*v for k, v in ev.items()) - 6*p) == 0,
         "     Omega's spectrum is p+q+4r (once), p+q-2r (twice), p-q (three times); trace 6p")
    for val, mult in [(p + q + 4*r, 1), (p + q - 2*r, 2), (p - q, 3)]:
        got = [m for k, m in ev.items() if sp.simplify(k - val) == 0]
        want(got == [mult], f"       eigenvalue {val} has multiplicity {mult}")
    # explicit eigenvectors, so nothing rests on a symbolic root-finder
    v1 = sp.Matrix([1]*6)
    v2 = sp.Matrix([1, 1, -1, -1, 0, 0])          # J-symmetric, orthogonal to 1
    v3 = sp.Matrix([1, -1, 0, 0, 0, 0])           # J-antisymmetric
    for vec, val, tag in [(v1, p + q + 4*r, "uniform"), (v2, p + q - 2*r, "axis-symmetric"),
                          (v3, p - q, "axis-antisymmetric")]:
        want(sp.simplify(Om*vec - val*vec) == sp.zeros(6, 1),
             f"       {tag} vector is an eigenvector with eigenvalue {val}")

    print("\nD2  (b), first half: where the empty state meets the record states")
    print("     The empty state couples to the six contents only through the all-ones direction,")
    print("     because every bond with an empty end weighs the same 1.  So T splits into the")
    print("     3- and 2-dimensional eigenspaces of Omega orthogonal to 1 (untouched by the")
    print("     vacancy) and a 2x2 block on span{u, e_empty} with u = (1,...,1)/sqrt 6:")
    A1 = p + q + 4*r
    B = sp.Matrix([[c*A1, sp.sqrt(6)], [sp.sqrt(6), 1]])
    u = sp.Matrix([sp.Rational(1, 1)]*6 + [0])/sp.sqrt(6)
    e_e = sp.Matrix([0]*6 + [1])
    want(sp.simplify((T*u - (c*A1*u + sp.sqrt(6)*e_e)).norm()) == 0,
         "     T u = c(p+q+4r) u + sqrt(6) e_empty")
    want(sp.simplify((T*e_e - (sp.sqrt(6)*u + e_e)).norm()) == 0,
         "     T e_empty = sqrt(6) u + e_empty, so the 2x2 block is [[c(p+q+4r), sqrt6],[sqrt6, 1]]")
    det = sp.simplify(B.det())
    want(sp.simplify(det - (c*A1 - 6)) == 0,
         f"     its determinant is c(p+q+4r) - 6, which vanishes at exactly one scale:")
    want(sp.simplify(sp.solve(det, c)[0] - c0) == 0,
         "       c = 6/(p+q+4r) = c_0.  The unit's guessed 'zero eigenvalue' is this one.")
    detT = sp.factor(T.det())
    want(sp.simplify(detT - c**5*(p - q)**3*(p + q - 2*r)**2*(c*(p + q + 4*r) - 6)) == 0,
         "     and the whole 7x7 determinant factors as")
    print(f"       det T = {detT}")
    print("     - every factor is one of the eigenvalues above, with its multiplicity, and the")
    print("       ONLY factor that depends on the scale is c(p+q+4r) - 6.  So c_0 is the unique")
    print("       scale at which the law with vacancies has a degenerate transfer operator.")

    print("\nD3  (b), first half: what the null vector says")
    Bc = B.subs(c, c0)
    ns = sp.simplify(Bc).nullspace()
    want(len(ns) == 1, f"     at c_0 the 2x2 block has a one-dimensional kernel")
    v = sp.simplify(ns[0]/ns[0][0])
    want(sp.simplify(v[1] + sp.sqrt(6)) == 0,
         f"     spanned by u - sqrt(6) e_empty, i.e. e_empty = (1/6) * sum over the six contents")
    print("     of the record states, AS A VECTOR IN THE TRANSFER OPERATOR.  This is the exact")
    print("     sense in which 'no state is privileged' holds at c_0: the empty state is not a")
    print("     seventh state at all there, it is the uniform superposition of the six contents.")
    sub312 = {p: 3, q: 1, r: 2}
    T312 = lambda cv: sp.Matrix(7, 7, lambda i, j: sp.cancel(T[i, j].subs(sub312).subs(c, cv)))
    want(T312(sp.Rational(1, 2)).rank() == 4 and T312(1).rank() == 5,
         "     at (3,1,2): rank T = 4 at c_0 = 1/2 and 5 at c = 1 - the drop at c_0 is by one,")
    print("       on top of the two ranks (p+q-2r) = 0 costs at every scale there.")

    print("\nD4  the two facts block 39 gives are ONE fact - with two side conditions")
    print("     Bond-plane reflection positivity through a bond holds iff the pair-weight matrix")
    print("     T is positive semidefinite.  T's eigenvalues are p-q (x3), p+q-2r (x2) and the")
    print("     two roots of the 2x2 block, whose trace c(p+q+4r)+1 > 0 and whose determinant is")
    print("     c(p+q+4r)-6.  So T >= 0 exactly when")
    print("       c >= c_0    AND    p >= q    AND    p + q >= 2r,")
    print("     the last two being independent of the scale.  The averaging statement (an empty")
    print("     neighbour weighs what a uniformly random record weighs: c(p+q+4r)/6 = 1) and the")
    print("     RP threshold are therefore the SAME equation c(p+q+4r) = 6, seen once as a mean")
    print("     and once as a determinant.")
    for (pv, qv, rv) in [(3, 1, 2), (5, 2, 4), (7, 3, 5), (4, 1, 1)]:
        sub = {p: pv, q: qv, r: rv}
        c0v = sp.nsimplify(c0.subs(sub))
        e2 = pv + qv - 2*rv
        e3 = pv - qv
        Tv = sp.Matrix(7, 7, lambda i, j: sp.cancel(T[i, j].subs(sub).subs(c, c0v)))
        evs = Tv.eigenvals()
        negs = [k for k in evs if k.is_real and k < 0]
        print(f"       (p,q,r) = {(pv,qv,rv)}: c_0 = {c0v}, p-q = {e3}, p+q-2r = {e2}; "
              f"at c_0 the spectrum of T has {len(negs)} negative eigenvalue(s)")
        want((len(negs) > 0) == (e2 < 0 or e3 < 0),
             f"         PSD at c_0 iff p >= q and p+q >= 2r: "
             f"{'fails' if (e2 < 0 or e3 < 0) else 'holds'} here")
    print("     So 'reflection positive exactly for c >= c_0' is right only where p >= q and")
    print("     p + q >= 2r.  At (5,2,4) the second fails (7 < 8), and NO scale makes the law")
    print("     with vacancies reflection positive through a bond plane there.")

    print("\nD5  (d) formation-then-motion against formation-in-place")
    print("     Take x and y adjacent and both empty, with x having one occupied neighbour A")
    print("     carrying content a, and y having none.  Two routes end with a record at y:")
    print("       route 1: form at x (rate z Z_x, content s with weight c omega(a,s)), then move")
    print("                x -> y, which by the motion rule happens with probability")
    print("                1/(1 + c omega(a,s)) - the record weighs c omega(a,s) at x and 1 at y;")
    print("       route 2: form at y (rate z Z_y, content s with weight 1 - uniform).")
    s = sp.Symbol('s')
    om = [p, q, r, r, r, r]          # omega(a, s) as s runs over the six contents, a fixed
    w1 = [c*o/(1 + c*o) for o in om]
    tot1 = sum(w1)
    route1 = [sp.simplify(w/tot1) for w in w1]
    route2 = [sp.Rational(1, 6)]*6
    want(sp.simplify(route1[0] - route2[0]) != 0,
         "     route 1 gives content s with probability proportional to c w/(1 + c w), route 2")
    print("       uniformly.  Equality for every content demands c omega/(1 + c omega) constant")
    print("       in omega, and t -> ct/(1+ct) is strictly increasing for every c > 0, so:")
    diff = sp.simplify(route1[0] - route1[2])      # equal-axis vs orthogonal
    sols = sp.solve(sp.numer(sp.together(diff)), c)
    real_pos = [x for x in sols if x.is_real and x > 0] if sols else []
    want(len(real_pos) == 0,
         f"     the two routes agree for NO positive c when p != r (solutions in c: "
         f"{real_pos or 'none'})")
    for (pv, qv, rv) in [(3, 1, 2), (5, 2, 4)]:
        sub = {p: pv, q: qv, r: rv}
        c0v = sp.nsimplify(c0.subs(sub))
        r1 = [sp.cancel(x.subs(sub).subs(c, c0v)) for x in route1]
        tv = sp.cancel(sum(abs(a - b) for a, b in zip(r1, route2))/2)
        want(tv > 0, f"     (p,q,r) = {(pv,qv,rv)} at c_0: total variation between the two routes' "
                     f"content laws is {tv} = {float(tv):.6f} > 0")
    print("     Equality holds iff p = q = r, i.e. iff the six-axis rule is trivial.  So (d)")
    print("     fixes no scale at all: it is not a condition on c, it is a condition on the")
    print("     six-axis weights, and the weights the lane works with never satisfy it.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on what fixes the binding scale: the 7-state pair-weight matrix T "
              "(c omega between records, 1 on any bond with an empty end) has the six-axis "
              "spectrum p+q+4r, p+q-2r (twice), p-q (three times), and the empty state couples "
              "only to the all-ones direction, giving a 2x2 block [[c(p+q+4r), sqrt6],[sqrt6, 1]] "
              "whose determinant c(p+q+4r) - 6 vanishes exactly at c_0; there T has rank 6 and its "
              "kernel is u - sqrt(6) e_empty, so the empty state IS the uniform superposition of "
              "the six contents in the transfer operator - candidate (b)'s first half gives c_0 a "
              "spectral derivation, and block 39's averaging fact and RP threshold are the same "
              "equation seen as a mean and as a determinant; bond-plane RP needs in addition the "
              "scale-free p >= q and p + q >= 2r, and at (5,2,4) the latter fails (7 < 8) so no "
              "scale is reflection positive there; candidate (d) fixes no scale, the two routes' "
              "content laws differing in total variation by 7/132 at (3,1,2) and agreeing only if "
              "p = q = r")
        print("HIT: c_0 = 6/(p+q+4r) is the unique scale at which the 7-state transfer operator "
              "is singular, with kernel u - sqrt(6) e_empty, so at c_0 the empty state is exactly "
              "the uniform superposition of the six record states and the operator has rank 6 - "
              "the averaging sentence and the reflection-positivity threshold of block 39 are one "
              "equation c(p+q+4r) = 6, read once as a mean and once as a determinant; bond-plane "
              "RP additionally requires the scale-free conditions p >= q and p + q >= 2r, so "
              "block 39's 'exactly for c >= c_0' is incomplete and fails at every scale for "
              "(5,2,4); and consistency between formation and motion (candidate d) constrains the "
              "weights, not the scale, holding only at p = q = r")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
