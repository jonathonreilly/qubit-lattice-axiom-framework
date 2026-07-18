#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the narrow theorem note
`DM_LEPTOGENESIS_PMNS_CONSTRAINED_OPTIMIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the standalone
calculus-identity implication: GIVEN

  (H1)  J : Omega -> R is C^2, strictly convex on open convex Omega;
  (H1') F = { z in Omega : C(z) = 0 } is segment-feasible
        (supplied convex-feasibility, not discharged);
  (H2)  grad C(z) =/= 0 on F;
  (H3)  F is non-empty and bounded;
  (H4)  the constrained minimum of J on F is attained at an interior
        point z_* in F (z_* in Omega);

THEN the constrained problem  min { J(z) : z in F }  satisfies

  (T1)  uniqueness of the global minimizer z_*;
  (T2)  Lagrange stationarity:  grad J(z_*) = lambda_* grad C(z_*);
  (T3)  multiplier formula:
        lambda_* = <grad J(z_*), grad C(z_*)> / || grad C(z_*) ||^2.

This narrow-theorem companion runner gives a sympy-based exact-symbolic
verification of the abstract implication:

  (a) realizes a generic strictly convex C^2 J(z) (a symbolic SPD
      quadratic on R^n with n=2 for tractability of symbolic gradients);
  (b) realizes a generic smooth equality constraint C(z) (a symbolic
      affine constraint c^T z - d, regular by construction);
  (c) computes the closed-form constrained minimizer z_* via the
      Lagrange system and verifies (T1)-(T3) symbolically;
  (d) verifies (C1)-(C2) parametrically and illustrates (C3) at an exact
      rational sample;
  (e) free-symbol bookkeeping for the multiplier substitution;
  (f) numerical FP cross-check at one independent random SPD/affine
      sample;
  (g) counterfactual probe: necessity of (H1) (strict convexity) via
      a degenerate J = c^T z linear case admitting an affine subspace
      of minimizers;
  (h) counterfactual probe: necessity of (H2) (constraint regularity)
      via a constraint with vanishing gradient, breaking (L-formula);
  (i) sanity probe: the convex-uniqueness (T1) argument via strict
      midpoint inequality on a sample strictly convex J at the
      midpoint of a hypothetical pair of minimizers.

Companion role: not a new claim row, not a new source note, no status
promotion. It verifies the standalone calculus content at exact symbolic
precision under the four explicit supplied hypotheses plus (H1'). The
supplied hypotheses themselves are not re-derived. Any downstream mapping to
`I_seed` or `eta_{i_*}/eta_obs - 1` is informative and does not supply or
discharge those hypotheses.
"""

import sys

try:
    import sympy
    from sympy import (
        Matrix,
        Rational,
        Symbol,
        diff,
        simplify,
        solve,
        symbols,
        expand,
        zeros,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("DM_LEPTOGENESIS_PMNS_CONSTRAINED_OPTIMIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of (T1) uniqueness, (T2) Lagrange")
    print("stationarity, (T3) multiplier formula under supplied (H1)-(H4) + (H1')")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # ---------------------------------------------------------------------
    # We instantiate the abstract narrow theorem at n=2 (the smallest
    # case that allows nontrivial gradient/constraint geometry). The
    # narrow theorem holds at arbitrary finite n; the n=2 instantiation
    # is a faithful symbolic test of the algebraic identities (T1)-(T3)
    # and corollaries (C1)-(C3) because the proofs are linear in n.

    # Free coordinates z = (z1, z2)
    z1, z2 = symbols("z1 z2", real=True)
    z = Matrix([z1, z2])

    # Generic strictly-convex C^2 J(z) := (1/2) (z - a)^T A (z - a)
    # with A SPD symbolic (we parametrize A = [[A11, A12], [A12, A22]]
    # with A11 > 0, A22 > 0, det(A) = A11 A22 - A12^2 > 0).
    A11 = Symbol("A11", positive=True, real=True)
    A22 = Symbol("A22", positive=True, real=True)
    A12 = Symbol("A12", real=True)
    A = Matrix([[A11, A12], [A12, A22]])
    a1 = Symbol("a1", real=True)
    a2 = Symbol("a2", real=True)
    a = Matrix([a1, a2])

    # Strict convexity of J <=> A SPD <=> A11 > 0 AND det(A) > 0.
    # We track det_A separately for the SPD discriminant.
    det_A = A11 * A22 - A12**2

    diff_vec = z - a
    J_expr = (Rational(1, 2) * (diff_vec.T @ A @ diff_vec))[0, 0]
    J_expr = expand(J_expr)

    # Generic smooth equality constraint C(z) := c1 z1 + c2 z2 - d
    # (affine, regular: grad C = (c1, c2) =/= 0).
    c1 = Symbol("c1", real=True)
    c2 = Symbol("c2", real=True)
    d = Symbol("d", real=True)
    C_expr = c1 * z1 + c2 * z2 - d

    grad_J = Matrix([diff(J_expr, v) for v in (z1, z2)])
    grad_C = Matrix([diff(C_expr, v) for v in (z1, z2)])

    print(f"  J(z) = (1/2) (z - a)^T A (z - a)")
    print(f"  A = {A.tolist()}")
    print(f"  a = {a.tolist()}")
    print(f"  C(z) = c1 z1 + c2 z2 - d")
    print(f"  grad J(z) = {grad_J.tolist()}")
    print(f"  grad C(z) = {grad_C.tolist()}")

    # Exact discriminant identity. Positivity is the separate supplied (H1)
    # premise and is not self-certified by this expression.
    check(
        "det(A) equals the displayed discriminant A11 A22 - A12^2 exactly",
        simplify(A.det() - det_A) == 0,
        detail=f"det_A = {det_A}",
    )

    # Constraint regularity (supplied (H2): grad C =/= 0 on F)
    grad_C_norm_sq = (grad_C.T @ grad_C)[0, 0]
    check(
        "grad C has explicit nonvanishing-norm form c1^2 + c2^2 (supplied (H2))",
        simplify(grad_C_norm_sq - (c1**2 + c2**2)) == 0,
        detail=f"|| grad C ||^2 = {grad_C_norm_sq}",
    )

    # ---------------------------------------------------------------------
    section("Part 1: closed-form constrained minimizer via Lagrange system")
    # ---------------------------------------------------------------------
    # Solve grad J(z_*) = lambda * grad C(z_*) jointly with C(z_*) = 0.
    # I.e., A (z_* - a) = lambda c, c^T z_* = d.
    lam = Symbol("lam", real=True)
    eqs = [
        grad_J[0] - lam * grad_C[0],
        grad_J[1] - lam * grad_C[1],
        C_expr,
    ]
    sol = solve(eqs, (z1, z2, lam), dict=True)
    check(
        "Lagrange system has a unique symbolic solution (z1, z2, lam)",
        isinstance(sol, list) and len(sol) == 1,
        detail=f"|solutions| = {len(sol) if isinstance(sol, list) else 'n/a'}",
    )

    sol0 = sol[0]
    z1_star = simplify(sol0[z1])
    z2_star = simplify(sol0[z2])
    lam_star = simplify(sol0[lam])
    print(f"  z_*[0] = {z1_star}")
    print(f"  z_*[1] = {z2_star}")
    print(f"  lambda_* = {lam_star}")

    # ---------------------------------------------------------------------
    section("Part 2: (T2) Lagrange stationarity at z_*")
    # ---------------------------------------------------------------------
    grad_J_star = grad_J.subs({z1: z1_star, z2: z2_star})
    grad_C_star = grad_C.subs({z1: z1_star, z2: z2_star})
    L_diff = grad_J_star - lam_star * grad_C_star
    L_diff_simpl = Matrix([simplify(L_diff[i]) for i in range(2)])
    check(
        "(T2) grad J(z_*) - lambda_* grad C(z_*) = 0 parametrically (component 0)",
        L_diff_simpl[0] == 0,
        detail=f"diff[0] = {L_diff_simpl[0]}",
    )
    check(
        "(T2) grad J(z_*) - lambda_* grad C(z_*) = 0 parametrically (component 1)",
        L_diff_simpl[1] == 0,
        detail=f"diff[1] = {L_diff_simpl[1]}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (T3) multiplier formula lambda_* = <gJ, gC>/||gC||^2")
    # ---------------------------------------------------------------------
    inner_J_C_star = simplify((grad_J_star.T @ grad_C_star)[0, 0])
    norm_C_sq_star = simplify((grad_C_star.T @ grad_C_star)[0, 0])
    lam_formula = simplify(inner_J_C_star / norm_C_sq_star)
    check(
        "(T3) lambda_* = <grad J(z_*), grad C(z_*)> / || grad C(z_*) ||^2",
        simplify(lam_formula - lam_star) == 0,
        detail=f"formula = {lam_formula}, lam_star = {lam_star}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: derivable corollaries (C1)-(C3)")
    # ---------------------------------------------------------------------
    # (C1) grad J - lambda grad C = 0 at z_*  (same as T2)
    check(
        "(C1) grad J(z_*) - lambda_* grad C(z_*) = 0  (rearranged Lagrange)",
        L_diff_simpl[0] == 0 and L_diff_simpl[1] == 0,
        detail=f"diff = {L_diff_simpl.T.tolist()}",
    )

    # (C2) projection of grad J onto T_{z_*} F is zero.
    # T_{z_*} F = { v : <grad C(z_*), v> = 0 }.
    # The projection of g onto T_{z_*} F is
    #   P(g) = g - <g, grad C(z_*)>/||grad C(z_*)||^2 * grad C(z_*).
    proj = grad_J_star - inner_J_C_star / norm_C_sq_star * grad_C_star
    proj_simpl = Matrix([simplify(proj[i]) for i in range(2)])
    check(
        "(C2) projection of grad J(z_*) onto T_{z_*}F is zero (component 0)",
        proj_simpl[0] == 0,
        detail=f"proj[0] = {proj_simpl[0]}",
    )
    check(
        "(C2) projection of grad J(z_*) onto T_{z_*}F is zero (component 1)",
        proj_simpl[1] == 0,
        detail=f"proj[1] = {proj_simpl[1]}",
    )

    # (C3) If grad J(z_*) =/= 0 and grad C(z_*) =/= 0, then lambda_* =/= 0.
    # Equivalently: lambda_* = 0 forces grad J(z_*) = 0.
    # We verify the contrapositive symbolically: substituting lambda = 0
    # into (L) yields grad J(z_*) = 0, which we exhibit as the constraint
    # of vanishing.
    L_at_zero = (grad_J_star - 0 * grad_C_star)
    L_at_zero_simpl = Matrix([simplify(L_at_zero[i]) for i in range(2)])
    # The implication is: if lambda were 0, then grad_J_star must be 0.
    # The exact parametric implication is already the identity (L). We also
    # exhibit it at one rational sample with nonzero grad J and lambda.
    sample_c3 = {A11: 1, A22: 1, A12: 0, a1: 1, a2: 0, c1: 1, c2: 1, d: 0}
    lam_star_c3 = lam_star.subs(sample_c3)
    grad_J_star_c3 = Matrix([grad_J_star[i].subs(sample_c3) for i in range(2)])
    grad_J_nonzero = any(simplify(grad_J_star_c3[i]) != 0 for i in range(2))
    check(
        "(C3) at a=(1,0), A=I, c=(1,1), d=0: grad J(z_*) =/= 0 forces lambda_* =/= 0",
        grad_J_nonzero and simplify(lam_star_c3) != 0,
        detail=f"grad J(z_*) = {grad_J_star_c3.T.tolist()}, lambda_* = {lam_star_c3}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: free-symbol bookkeeping after multiplier substitution")
    # ---------------------------------------------------------------------
    # When lambda is substituted by the (L-formula) value, the Lagrange
    # difference grad J(z_*) - lambda * grad C(z_*) has empty free
    # symbols modulo the substitution z = z_*.
    L_diff_after_lam_sub = (grad_J_star - lam_formula * grad_C_star)
    L_diff_after_simpl = Matrix([simplify(L_diff_after_lam_sub[i]) for i in range(2)])
    check(
        "Lagrange diff with lambda substituted by (L-formula) is zero (component 0)",
        L_diff_after_simpl[0] == 0,
        detail=f"diff[0] = {L_diff_after_simpl[0]}",
    )
    check(
        "Lagrange diff with lambda substituted by (L-formula) is zero (component 1)",
        L_diff_after_simpl[1] == 0,
        detail=f"diff[1] = {L_diff_after_simpl[1]}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: numerical FP cross-check at one independent random sample")
    # ---------------------------------------------------------------------
    # SPD A: diagonal positive entries plus small off-diagonal staying SPD.
    sample = {
        A11: Rational(7, 4),
        A22: Rational(5, 2),
        A12: Rational(1, 2),
        a1: Rational(3, 10),
        a2: Rational("-2", 10),
        c1: 1,
        c2: -2,
        d: Rational(1, 5),
    }
    z1_star_num = float(z1_star.subs(sample))
    z2_star_num = float(z2_star.subs(sample))
    lam_star_num = float(lam_star.subs(sample))
    # Constraint satisfaction
    C_at_star_num = float(C_expr.subs({z1: z1_star_num, z2: z2_star_num, **sample}))
    check(
        "(numerical) C(z_*) = 0 at random SPD/affine sample",
        abs(C_at_star_num) < 1e-12,
        detail=f"|C(z_*)| = {abs(C_at_star_num):.3e}",
    )
    # Lagrange stationarity component-wise
    grad_J_num = [float(grad_J_star[i].subs(sample)) for i in range(2)]
    grad_C_num = [float(grad_C_star[i].subs(sample)) for i in range(2)]
    diff_num = [grad_J_num[i] - lam_star_num * grad_C_num[i] for i in range(2)]
    check(
        "(numerical) Lagrange (L) holds at z_* component-wise (random sample)",
        all(abs(diff_num[i]) < 1e-12 for i in range(2)),
        detail=f"|diff| = ({abs(diff_num[0]):.3e}, {abs(diff_num[1]):.3e})",
    )

    # ---------------------------------------------------------------------
    section("Part 7: counterfactual probe -- necessity of (H1) (strict convexity)")
    # ---------------------------------------------------------------------
    # Replace J by a linear function J_lin(z) = c1' z1 + c2' z2.
    # Then grad J_lin = (c1', c2') is CONSTANT and the Lagrange system
    # becomes (c1', c2') = lambda (c1, c2), C(z) = 0. This is
    # OVER-determined in lambda but UNDER-determined in z: any z on the
    # constraint affine line gives the same value of J_lin (only if
    # (c1', c2') parallel to (c1, c2)) or no minimum at all otherwise.
    # In either case, (T1) (unique global minimum) fails.
    c1p, c2p = symbols("c1p c2p", real=True)
    J_lin = c1p * z1 + c2p * z2
    grad_J_lin = Matrix([diff(J_lin, v) for v in (z1, z2)])
    # Try to solve grad J_lin = lambda grad C, C(z) = 0:
    eqs_lin = [grad_J_lin[0] - lam * grad_C[0], grad_J_lin[1] - lam * grad_C[1], C_expr]
    sol_lin = solve(eqs_lin, (z1, z2, lam), dict=True)
    # If (c1', c2') parallel to (c1, c2), z is free along the constraint.
    # If not parallel, no solution (J_lin unbounded below on F).
    # Either way, no unique minimizer -- (T1) fails.
    # For the parallel case c1p = c1, c2p = c2: any z on C(z)=0 is a
    # stationary candidate, so the constrained problem has infinitely
    # many minimizers in J = constant along F.
    sample_parallel = {c1p: c1, c2p: c2}
    eqs_par = [
        grad_J_lin[0].subs(sample_parallel) - lam * grad_C[0],
        grad_J_lin[1].subs(sample_parallel) - lam * grad_C[1],
        C_expr,
    ]
    sol_par = solve(eqs_par, (z1, z2, lam), dict=True)
    # sympy returns an infinite-family solution (lambda = 1) with z free
    # along the constraint. We detect this by checking that z1 or z2 is
    # a free symbol in the resulting solution dict (or sol_par contains
    # multiple distinct symbolic candidates).
    cf_h1_no_unique = (
        not sol_par
        or len(sol_par) == 0
        or any(
            (z1 in s and z2 not in s) or (z2 in s and z1 not in s)
            for s in sol_par
        )
    )
    # More robust: at c1p = c1, c2p = c2, J_lin = c1 z1 + c2 z2 = d
    # everywhere on C(z) = 0 by direct substitution. Hence J is
    # CONSTANT on F, no unique minimizer.
    J_lin_par_on_F = simplify(
        J_lin.subs(sample_parallel).subs({z2: (d - c1 * z1) / c2}) - d
    )
    check(
        "(H1) counterfactual: linear J on affine constraint is constant on F (no unique min)",
        J_lin_par_on_F == 0,
        detail=f"J_lin - d on F = {J_lin_par_on_F} (zero means J constant)",
    )

    # ---------------------------------------------------------------------
    section("Part 8: counterfactual probe -- necessity of (H2) (constraint regularity)")
    # ---------------------------------------------------------------------
    # Replace C by C_cf(z) = z1^2 + z2^2. Its feasible set is the singleton
    # {(0,0)}, where grad C_cf vanishes. Choose the strictly convex objective
    # J_cf = (z1 - 1)^2 + z2^2, whose gradient is nonzero at the feasible
    # minimizer. No lambda can satisfy grad J_cf = lambda grad C_cf there,
    # and the projection formula has zero denominator.
    C_cf = z1**2 + z2**2
    J_cf = (z1 - 1) ** 2 + z2**2
    grad_C_cf = Matrix([diff(C_cf, v) for v in (z1, z2)])
    grad_J_cf = Matrix([diff(J_cf, v) for v in (z1, z2)])
    C_cf_at0 = C_cf.subs({z1: 0, z2: 0})
    grad_C_cf_at0 = grad_C_cf.subs({z1: 0, z2: 0})
    grad_J_cf_at0 = grad_J_cf.subs({z1: 0, z2: 0})
    norm_grad_C_cf_at0_sq = (grad_C_cf_at0.T @ grad_C_cf_at0)[0, 0]
    check(
        "(H2) counterfactual point (0,0) is feasible for C_cf = z1^2 + z2^2",
        simplify(C_cf_at0) == 0,
        detail=f"C_cf(0,0) = {C_cf_at0}",
    )
    check(
        "(H2) counterfactual has grad C_cf(0,0) = 0 but grad J_cf(0,0) nonzero",
        grad_C_cf_at0 == zeros(2, 1) and grad_J_cf_at0 != zeros(2, 1),
        detail=f"grad C_cf = {grad_C_cf_at0.T.tolist()}, grad J_cf = {grad_J_cf_at0.T.tolist()}",
    )
    check(
        "(H2) counterfactual cannot satisfy Lagrange stationarity for any lambda",
        simplify(grad_J_cf_at0 - lam * grad_C_cf_at0) != zeros(2, 1),
        detail=f"grad J_cf - lambda grad C_cf = {(grad_J_cf_at0 - lam * grad_C_cf_at0).T.tolist()}",
    )
    check(
        "(H2) counterfactual makes the multiplier-formula denominator zero",
        simplify(norm_grad_C_cf_at0_sq) == 0,
        detail=f"|| grad C_cf(0,0) ||^2 = {norm_grad_C_cf_at0_sq}",
    )

    # ---------------------------------------------------------------------
    section("Part 9: (T1) midpoint strict-convexity probe")
    # ---------------------------------------------------------------------
    # At a sample SPD J, two hypothetical minimizers z_a, z_b on F yield
    # J(z_m) < (1/2)(J(z_a) + J(z_b)) at the midpoint z_m. We exhibit
    # this numerically at one sample.
    sample_t1 = {A11: 1, A22: 1, A12: 0, a1: 0, a2: 0}
    z_a_val = Matrix([1, 0])
    z_b_val = Matrix([0, 1])
    z_m_val = Matrix([Rational(1, 2), Rational(1, 2)])
    J_a = (
        Rational(1, 2)
        * ((z_a_val - a.subs(sample_t1)).T @ A.subs(sample_t1) @ (z_a_val - a.subs(sample_t1)))[0, 0]
    )
    J_b = (
        Rational(1, 2)
        * ((z_b_val - a.subs(sample_t1)).T @ A.subs(sample_t1) @ (z_b_val - a.subs(sample_t1)))[0, 0]
    )
    J_m = (
        Rational(1, 2)
        * ((z_m_val - a.subs(sample_t1)).T @ A.subs(sample_t1) @ (z_m_val - a.subs(sample_t1)))[0, 0]
    )
    avg = (J_a + J_b) / 2
    strict_ineq = simplify(avg - J_m) > 0
    check(
        "(T1) midpoint strict-convexity inequality at sample (z_a=(1,0), z_b=(0,1))",
        bool(strict_ineq),
        detail=f"J((z_a+z_b)/2) = {J_m}, (J(z_a)+J(z_b))/2 = {avg}, diff = {simplify(avg - J_m)}",
    )

    # ---------------------------------------------------------------------
    section("Part 10: A SPD reality check (sanity)")
    # ---------------------------------------------------------------------
    # Verify that the symbolic A with A11, A22 positive and det(A) > 0
    # admits a strictly-convex J via the parametric Hessian test.
    H_J = sympy.Matrix([
        [diff(J_expr, vi, vj) for vj in (z1, z2)] for vi in (z1, z2)
    ])
    check(
        "Hessian of J equals A symbolically (strict convexity ↔ A SPD)",
        simplify(H_J - A) == zeros(2, 2),
        detail=f"H_J - A = {(H_J - A).tolist()}",
    )

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (T2) Lagrange stationarity grad J(z_*) = lambda_* grad C(z_*)")
    print("    (T3) multiplier formula lambda_* = <gJ, gC>/||gC||^2")
    print("    (C1)-(C2) reduce to 0 parametrically; (C3) follows from (L) and has an exact sample")
    print("    Numerical FP cross-check at random SPD/affine sample (constraint and (L))")
    print("    (H1) counterfactual: linear J on affine F is constant -> no unique min")
    print("    (H2) counterfactual: vanishing-grad C breaks (L-formula) denominator")
    print("    (T1) midpoint strict-convexity inequality at one sample")
    print("    Hessian of J equals A (strict convexity <=> A SPD)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
