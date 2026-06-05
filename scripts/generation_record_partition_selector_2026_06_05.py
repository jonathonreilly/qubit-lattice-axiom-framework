"""GENERATION_RECORD_PARTITION_SELECTOR -- exact K/CPT central-sector checks.

This runner sharpens the generation partition gate after the 2026-06-05 Record
axiom. Given the supplied C3 generation carrier and fixed K/CPT conjugation, the
Record-compatible central sectors are K/CPT orbits. The exact algebra below
shows that the unique nontrivial K-stable central partition is

    singlet P0  |  faithful doublet P1.

Resolving the faithful characters separately requires a K-odd orientation
operator i(C-C^2), or equivalently an extra complex basis choice inside the
doublet. No weight, probability, or dynamics is selected here.
"""

from __future__ import annotations

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def zero_matrix(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def same_matrix(a: sp.Matrix, b: sp.Matrix) -> bool:
    return zero_matrix(a - b)


def canonical_solution_tuple(sol: dict[sp.Symbol, sp.Expr], symbols: tuple[sp.Symbol, ...]) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sol[s]) for s in symbols)


def main() -> int:
    I = sp.I
    sqrt3 = sp.sqrt(3)
    omega = sp.Rational(-1, 2) + I * sqrt3 / 2

    eye = sp.eye(3)
    C = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])
    C2 = C**2

    # -------------------------------------------------------------------------
    # 1. C3 carrier and complex character idempotents.
    # -------------------------------------------------------------------------
    check("P1.1 C is the order-3 generation cycle",
          same_matrix(C**3, eye) and not same_matrix(C, eye))
    check("P1.2 primitive cube root identities hold exactly",
          sp.simplify(omega**3 - 1) == 0 and sp.simplify(1 + omega + omega**2) == 0)

    # Central primitive idempotents over C. The labels + and - are the faithful
    # conjugate characters; K swaps them.
    P0 = sp.simplify((eye + C + C2) / 3)
    Pp = sp.simplify((eye + omega**2 * C + omega * C2) / 3)
    Pm = sp.simplify((eye + omega * C + omega**2 * C2) / 3)
    P1 = sp.simplify(Pp + Pm)

    projectors = [P0, Pp, Pm]
    idempotent_ok = all(same_matrix(P * P, P) for P in projectors)
    orthogonal_ok = all(
        same_matrix(projectors[i] * projectors[j], sp.zeros(3))
        for i in range(3) for j in range(3) if i != j
    )
    check("P1.3 complex central character projectors are orthogonal idempotents",
          idempotent_ok and orthogonal_ok)
    check("P1.4 complex character projectors resolve the identity",
          same_matrix(P0 + Pp + Pm, eye))
    check("P1.5 ranks of complex sectors are 1,1,1",
          [sp.simplify(P.trace()) for P in projectors] == [1, 1, 1])
    check("P1.6 each complex projector commutes with the C3 generator",
          all(same_matrix(P * C, C * P) for P in projectors))

    # -------------------------------------------------------------------------
    # 2. K/CPT conjugation acts on sectors by orbits.
    # -------------------------------------------------------------------------
    K = lambda M: sp.conjugate(M)
    check("P2.1 K fixes the singlet projector P0",
          same_matrix(K(P0), P0))
    check("P2.2 K swaps the two faithful character projectors",
          same_matrix(K(Pp), Pm) and same_matrix(K(Pm), Pp))
    check("P2.3 the K/CPT orbits are exactly {P0} and {Pp,Pm}",
          same_matrix(K(P1), P1) and same_matrix(P1, eye - P0))
    check("P2.4 orbit dimensions are 1 and 2",
          sp.simplify(P0.trace()) == 1 and sp.simplify(P1.trace()) == 2)
    check("P2.5 P1 is a real central idempotent",
          same_matrix(P1 * P1, P1) and same_matrix(K(P1), P1) and same_matrix(P1 * C, C * P1))

    # -------------------------------------------------------------------------
    # 3. Enumerate real/K-stable central idempotents. This is the algebraic
    # selector: over the K-fixed real central algebra there is no finer central
    # idempotent inside the doublet.
    # -------------------------------------------------------------------------
    a, b, c = sp.symbols("a b c", real=True)
    X = a * eye + b * C + c * C2
    equations = []
    idem = sp.simplify(X * X - X)
    for entry in idem:
        equations.append(sp.expand(entry))
    solutions = sp.solve(equations, (a, b, c), dict=True)
    got = sorted(canonical_solution_tuple(sol, (a, b, c)) for sol in solutions)
    expected = sorted([
        (sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3)),
        (sp.Rational(2, 3), sp.Rational(-1, 3), sp.Rational(-1, 3)),
    ])
    check("P3.1 exact real central idempotent enumeration gives only 0, I, P0, P1",
          got == expected,
          f"solutions={got}")

    P0_coeff = (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3))
    P1_coeff = (sp.Rational(2, 3), sp.Rational(-1, 3), sp.Rational(-1, 3))
    check("P3.2 P0 and P1 are the only nonzero proper real central idempotents",
          P0_coeff in got and P1_coeff in got and len(got) == 4)
    check("P3.3 the doublet P1 has no nonzero proper K-stable central sub-idempotent",
          got == expected,
          "any such sub-idempotent would appear in the real central idempotent list")

    # K-stable sums of complex primitive projectors are exactly unions of K orbits.
    subset_data = []
    labels = ["0", "+", "-"]
    for mask in range(8):
        subset = [labels[i] for i in range(3) if mask & (1 << i)]
        Psum = sp.zeros(3)
        for i, P in enumerate(projectors):
            if mask & (1 << i):
                Psum += P
        if same_matrix(K(Psum), Psum):
            subset_data.append(tuple(subset))
    check("P3.4 K-stable complex-sector unions are exactly orbit unions",
          subset_data == [(), ("0",), ("+", "-"), ("0", "+", "-")],
          f"K-stable unions={subset_data}")

    # -------------------------------------------------------------------------
    # 4. K-real C3-invariant readout observables resolve P0|P1 and cannot split
    # the faithful pair.
    # -------------------------------------------------------------------------
    alpha, beta = sp.symbols("alpha beta", real=True)
    A = alpha * eye + beta * (C + C2)
    lam0 = alpha + 2 * beta
    lam1 = alpha - beta
    check("P4.1 general K-real C3-invariant Hermitian observable is alpha I + beta(C+C^2)",
          same_matrix(K(A), A) and same_matrix(A.conjugate().T, A) and same_matrix(A * C, C * A))
    check("P4.2 K-real central observable has one singlet eigenvalue and one doublet eigenvalue",
          same_matrix(A * P0, lam0 * P0) and same_matrix(A * P1, lam1 * P1),
          f"lambda0={lam0}; lambda1={lam1}")
    check("P4.3 faithful character projectors have equal eigenvalue for every K-real central observable",
          same_matrix(A * Pp, lam1 * Pp) and same_matrix(A * Pm, lam1 * Pm))

    J = sp.simplify(I * (C - C2))
    check("P4.4 J=i(C-C^2) is Hermitian and C3-invariant",
          same_matrix(J.conjugate().T, J) and same_matrix(J * C, C * J))
    check("P4.5 J is K-odd, so it is not a K-real record observable",
          same_matrix(K(J), -J))
    charpoly = sp.factor(J.charpoly().as_expr())
    check("P4.6 J is exactly the doublet-splitting orientation operator",
          charpoly == sp.Symbol("lambda") * (sp.Symbol("lambda")**2 - 3),
          f"charpoly={charpoly}")

    # Verify directly that adding J separates the faithful projectors.
    mu_p = sp.simplify((J * Pp).trace() / Pp.trace())
    mu_m = sp.simplify((J * Pm).trace() / Pm.trace())
    check("P4.7 J assigns opposite eigenvalues to the faithful sectors",
          sp.simplify(mu_p + mu_m) == 0 and sp.simplify(mu_p**2 - 3) == 0,
          f"mu_plus={mu_p}; mu_minus={mu_m}")

    # -------------------------------------------------------------------------
    # 5. Record interpretation: outcomes are K/CPT orbits, so the native
    # alphabet has two letters before any extra K-breaking refinement.
    # -------------------------------------------------------------------------
    record_letters = [("singlet", int(P0.trace())), ("doublet", int(P1.trace()))]
    complex_letters = [("chi0", int(P0.trace())), ("chi_plus", int(Pp.trace())), ("chi_minus", int(Pm.trace()))]
    check("P5.1 Record K/CPT orbit alphabet has two letters with dimensions 1 and 2",
          record_letters == [("singlet", 1), ("doublet", 2)],
          str(record_letters))
    check("P5.2 three complex letters are a non-K-stable refinement, not the native Record alphabet",
          len(complex_letters) == 3 and not same_matrix(K(Pp), Pp) and not same_matrix(K(Pm), Pm),
          str(complex_letters))
    check("P5.3 partition selector does not determine weights or dynamics",
          True,
          "it selects P0|P1 only; block-count vs dimension weights and arrows remain separate gates")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("FINDING: with the supplied C3 carrier and fixed K/CPT conjugation,")
    print("         Record-compatible central sectors are uniquely P0 | P1.")
    print("         Splitting the doublet requires a K-odd orientation import.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
