#!/usr/bin/env python3
"""Exact CKM composite positive-volume alignment source-action checks."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CKM_COMPOSITE_POSITIVE_VOLUME_ALIGNMENT_SOURCE_ACTION_BOUNDARY_NOTE_2026-07-12.md"
EXACT_PASS = 0
BOUNDARY_PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "", *, boundary: bool = False) -> None:
    global EXACT_PASS, BOUNDARY_PASS, FAIL
    ok = bool(condition)
    if ok:
        if boundary:
            BOUNDARY_PASS += 1
            tag = "BOUNDARY_PASS"
        else:
            EXACT_PASS += 1
            tag = "EXACT_PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"             {detail}")


def z2_fixed_spectrum_orbit() -> None:
    print("\n1. FIXED-SPECTRUM RESIDUAL-Z2 ORBIT")
    sqrt2 = sp.sqrt(2)
    theta = sp.symbols("theta", real=True)
    e0 = sp.Matrix([1, 0, 0])
    ep = sp.Matrix([0, 1 / sqrt2, 1 / sqrt2])
    em = sp.Matrix([0, 1 / sqrt2, -1 / sqrt2])
    swap = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    p_s = em * em.T
    p_b = e0 * e0.T
    p_plus = ep * ep.T

    h_d = p_s + 9 * p_b + 4 * p_plus
    v_c = sp.cos(theta) * e0 + sp.sin(theta) * ep
    v_t = -sp.sin(theta) * e0 + sp.cos(theta) * ep
    p_c = sp.simplify(v_c * v_c.T)
    p_t = sp.simplify(v_t * v_t.T)
    h_u = sp.simplify(p_s + 4 * p_c + 16 * p_t)
    overlap = sp.trigsimp(sp.trace(p_c * p_b))

    check("H_d commutes with the selected Z2", sp.simplify(h_d * swap - swap * h_d) == sp.zeros(3))
    check("H_u(theta) commutes with the same Z2", sp.simplify(h_u * swap - swap * h_u) == sp.zeros(3))
    x = sp.symbols("x")
    check("H_d has fixed spectrum {1,4,9}", sp.factor(h_d.charpoly(x).as_expr()) == (x - 9) * (x - 4) * (x - 1))
    check("H_u(theta) has fixed spectrum {1,4,16}", sp.trigsimp(sp.factor(h_u.charpoly(x).as_expr()) - (x - 16) * (x - 4) * (x - 1)) == 0)
    check("projector overlap is cos(theta)^2", sp.trigsimp(overlap - sp.cos(theta) ** 2) == 0)
    check("fixed spectra admit overlap one", overlap.subs(theta, 0) == 1, boundary=True)
    check("fixed spectra admit overlap zero", sp.trigsimp(overlap.subs(theta, sp.pi / 2)) == 0, boundary=True)

    h_u_zero = sp.simplify(h_u.subs(theta, 0))
    h_u_one = sp.simplify(h_u.subs(theta, sp.pi / 2))
    expected_d = sp.Matrix([[9, 0, 0], [0, sp.Rational(5, 2), sp.Rational(3, 2)], [0, sp.Rational(3, 2), sp.Rational(5, 2)]])
    expected_u0 = sp.Matrix([[4, 0, 0], [0, sp.Rational(17, 2), sp.Rational(15, 2)], [0, sp.Rational(15, 2), sp.Rational(17, 2)]])
    expected_u1 = sp.Matrix([[16, 0, 0], [0, sp.Rational(5, 2), sp.Rational(3, 2)], [0, sp.Rational(3, 2), sp.Rational(5, 2)]])
    check("exact H_d endpoint matrix matches the note", h_d == expected_d)
    check("exact aligned H_u endpoint matches the note", h_u_zero == expected_u0)
    check("exact orthogonal H_u endpoint matches the note", h_u_one == expected_u1)


def determinant_balance() -> None:
    print("\n2. EIGHTEEN-DIMENSIONAL DETERMINANT BALANCE")
    t, r = sp.symbols("t r", positive=True)
    q = sp.diag(1, 0, 0, 0, 0, 0)
    p = sp.eye(6) - q
    b = sp.diag(1, 0, 0)
    c_proj = sp.kronecker_product(q, sp.eye(3))
    d_proj = sp.kronecker_product(p, b)
    e_proj = sp.eye(18) - c_proj - d_proj
    z_op = t * c_proj + d_proj / r + e_proj

    check("C,D,E are pairwise orthogonal", c_proj * d_proj == sp.zeros(18) and c_proj * e_proj == sp.zeros(18) and d_proj * e_proj == sp.zeros(18))
    check("C,D,E resolve the identity", c_proj + d_proj + e_proj == sp.eye(18))
    check("projector ranks are (3,5,10)", (c_proj.rank(), d_proj.rank(), e_proj.rank()) == (3, 5, 10))
    check("det Z=t^3 R^-5", sp.factor(z_op.det() - t**3 / r**5) == 0)
    check("Z becomes singular of rank 15 at t=0", z_op.subs(t, 0).rank() == 15, boundary=True)

    alpha, beta = sp.symbols("alpha beta", positive=True)
    z_powered = t**alpha * c_proj + r ** (-beta) * d_proj + e_proj
    check(
        "general block powers give det Z=t^(3 alpha)R^(-5 beta)",
        sp.factor(z_powered.det() - t ** (3 * alpha) * r ** (-5 * beta)) == 0,
        boundary=True,
    )

    c_rank1 = sp.kronecker_product(q, b).rank()
    c_rank2 = sp.kronecker_product(q, sp.eye(3) - b).rank()
    d_rank10 = sp.kronecker_product(p, sp.eye(3) - b).rank()
    alternative_exponents = [
        sp.Rational(d_proj.rank(), c_rank1),
        sp.Rational(d_proj.rank(), c_rank2),
        sp.Rational(d_rank10, c_proj.rank()),
    ]
    check(
        "equally covariant atomic lifts give exponents 5,5/2,10/3",
        alternative_exponents == [sp.Integer(5), sp.Rational(5, 2), sp.Rational(10, 3)],
        boundary=True,
    )

    q0 = sp.symbols("q0", positive=True)
    witness = sp.simplify((q0**5) ** 3 / (q0**3) ** 5)
    check("determinant-neutral witness R=q^3,t=q^5 is exact", witness == 1)
    check("neutrality gives t=R^(5/3)", (q0**5) ** 3 == (q0**3) ** 5)


def conditional_actions() -> None:
    print("\n3. CONDITIONAL POSITIVE-VOLUME ACTIONS")
    t, r, z = sp.symbols("t r z", positive=True)
    gamma_det = z - sp.log(z) - 1
    check("Gamma_det has stationary point at z=1", sp.diff(gamma_det, z).subs(z, 1) == 0)
    check("Gamma_det is strictly convex at z=1", sp.diff(gamma_det, z, 2).subs(z, 1) == 1)

    gamma_vol = (3 * sp.log(t) - 5 * sp.log(r)) ** 2 / 18
    derivative = sp.simplify(sp.diff(gamma_vol, t))
    q0 = sp.symbols("q0", positive=True)
    check("volume action derivative vanishes at R=q^3,t=q^5", sp.simplify(derivative.subs({r: q0**3, t: q0**5})) == 0)
    check("volume action vanishes at the five-thirds law", sp.simplify(gamma_vol.subs({r: q0**3, t: q0**5})) == 0)
    second = sp.simplify(sp.diff(gamma_vol, t, 2).subs({r: q0**3, t: q0**5}))
    check("volume action has positive curvature at the target", sp.simplify(second - 1 / (q0**10)) == 0)

    det_control = sp.Integer(2)
    scale = det_control ** sp.Rational(1, 18)
    projected_det = sp.simplify(det_control / scale**18)
    ai_distance_control = sp.expand_log(18 * sp.log(1 / scale) ** 2, force=True)
    check("closest scalar projection has determinant one", projected_det == 1)
    check(
        "independent affine-distance control gives (log det)^2/18",
        sp.simplify(ai_distance_control - sp.log(det_control) ** 2 / 18) == 0,
    )

    a, b_rank = sp.symbols("a b", positive=True)
    check("general rank law has determinant t^a R^-b", sp.simplify((r ** (b_rank / a)) ** a / r**b_rank) == 1)


def natural_action_boundaries() -> None:
    print("\n4. NATURAL-ACTION BOUNDARIES")
    t, r = sp.symbols("t r", positive=True)
    gamma_full = 3 * (t - sp.log(t) - 1) + 5 * (1 / r + sp.log(r) - 1)
    derivative = sp.simplify(sp.diff(gamma_full, t))
    check("full trace-logdet stationarity is R-independent", r not in derivative.free_symbols, boundary=True)
    check("full trace-logdet action selects t=1", derivative.subs(t, 1) == 0, boundary=True)
    check("full trace-logdet minimum is strict at t=1", sp.diff(gamma_full, t, 2).subs(t, 1) == 3, boundary=True)
    check("bare logdet has no interior stationary point", sp.diff(3 * sp.log(t) - 5 * sp.log(r), t) == 3 / t, boundary=True)

    uc, ut, ds, db, theta = sp.symbols("u_c u_t d_s d_b theta", real=True)
    rotation = sp.Matrix([[sp.cos(theta), sp.sin(theta)], [-sp.sin(theta), sp.cos(theta)]])
    h_u = sp.diag(uc, ut)
    h_d = sp.simplify(rotation * sp.diag(ds, db) * rotation.T)
    mixed = sp.trigsimp(sp.trace(h_u * h_d))
    check("linear mixed trace is affine in the projector overlap", sp.trigsimp(mixed - (uc * ds + ut * db + (uc - ut) * (db - ds) * sp.sin(theta) ** 2)) == 0, boundary=True)
    mixed_derivative = sp.trigsimp(sp.diff(mixed, theta))
    check("linear mixed trace has only commuting endpoint extrema", sp.trigsimp(mixed_derivative / ((uc - ut) * (db - ds)) - sp.sin(2 * theta)) == 0, boundary=True)


def jacobi_boundary() -> None:
    print("\n5. STRICT-JACOBI FIXED-SPECTRUM COUNTERFAMILY")
    center, scale, theta, phi = sp.symbols("C S theta phi", real=True)
    core = sp.Matrix(
        [
            [0, sp.cos(theta), 0],
            [sp.cos(theta), 0, sp.sin(theta)],
            [0, sp.sin(theta), 0],
        ]
    )
    jacobi = center * sp.eye(3) + scale * core
    charpoly = jacobi.charpoly()
    x = charpoly.gen
    expected_poly = (x - center + scale) * (x - center) * (x - center - scale)
    check("strict Jacobi family has fixed spectrum C-S,C,C+S", sp.trigsimp(sp.expand(charpoly.as_expr() - expected_poly)) == 0)

    middle = sp.Matrix([-sp.sin(theta), 0, sp.cos(theta)])
    upper_phi = sp.Matrix([sp.cos(phi), 1, sp.sin(phi)]) / sp.sqrt(2)
    check("displayed middle vector is the C eigenvector", sp.trigsimp(jacobi * middle - center * middle) == sp.zeros(3, 1))

    core_phi = core.subs(theta, phi)
    jacobi_phi = center * sp.eye(3) + scale * core_phi
    check("displayed upper vector is the C+S eigenvector", sp.trigsimp(jacobi_phi * upper_phi - (center + scale) * upper_phi) == sp.zeros(3, 1))
    overlap = sp.trigsimp((middle.T * upper_phi)[0] ** 2)
    check("relative Jacobi overlap is sin(phi-theta)^2/2", sp.trigsimp(overlap - sp.sin(phi - theta) ** 2 / 2) == 0, boundary=True)
    check("strict positive-link controls give distinct overlaps", overlap.subs({theta: sp.pi / 6, phi: sp.pi / 3}) == sp.Rational(1, 8), boundary=True)


def nni_boundary() -> None:
    print("\n6. NNI COEFFICIENT SOURCE-LAW BOUNDARY")
    q = sp.symbols("q", positive=True)
    r = q**6
    target = q**10
    c_required = (1 - r) * q**2 * sp.sqrt(1 - target) / (1 - 2 * target)
    tan_two_theta = sp.simplify(2 * c_required * sp.sqrt(r) / (1 - r))
    target_tangent = sp.simplify(2 * sp.sqrt(target * (1 - target)) / (1 - 2 * target))
    check("required NNI coefficient reproduces target mixing tangent", sp.simplify(tan_two_theta - target_tangent) == 0)

    q_control = sp.Rational(1, 2)
    r_control = q_control**6
    target_control = q_control**10
    c_control = sp.simplify(c_required.subs(q, q_control))
    cos_two_theta = sp.simplify(
        (1 - r_control)
        / sp.sqrt((1 - r_control) ** 2 + 4 * c_control**2 * r_control)
    )
    direct_sin_sq = sp.simplify((1 - cos_two_theta) / 2)
    check("direct NNI block diagonalization reaches the target on-branch", direct_sin_sq == target_control)
    check("small-angle branch denominator is positive in the exact control", 1 - 2 * target_control > 0, boundary=True)
    limit_ratio = sp.limit(c_required / q**2, q, 0, dir="+")
    check("required coefficient scales as R^(1/3)", limit_ratio == 1, boundary=True)

    c0 = sp.symbols("c0", positive=True)
    generic_tangent = 2 * c0 * sp.sqrt(r) / (1 - r)
    check("constant NNI coefficient instead starts at R^(1/2)", sp.limit(generic_tangent / (2 * c0 * q**3), q, 0, dir="+") == 1, boundary=True)


def textual_firewalls() -> None:
    print("\n7. CLAIM-BOUNDARY FIREWALLS")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.split())
    check("source note declares bounded_theorem", "**Claim type:** bounded_theorem" in note, boundary=True)
    check("source note declares exact support/boundary theorem", "**Actual current-surface status:** exact support/boundary theorem" in note, boundary=True)
    check("source note declares negative route pruning", "**Trace class:** negative_route_pruning" in note, boundary=True)
    check("conditional action is not presented as framework-derived", "sharp conditional representation, not a current framework derivation" in normalized, boundary=True)
    check("physical source action remains open", "physical statement that the quark composite uses (4.1)-(4.2)" in normalized, boundary=True)
    check("full mass pair remains open", "framework derivation and physical typing of the full quark mass pair" in normalized, boundary=True)
    check("retained-grade proposal language is forbidden", "does not permit retained-grade proposal language" in normalized, boundary=True)
    forbidden_targets = ["0.0422", "93.4", "4.180", "0.022", "0.041"]
    check("note contains no observed target values", not any(value in note for value in forbidden_targets), boundary=True)


def main() -> int:
    print("CKM COMPOSITE POSITIVE-VOLUME ALIGNMENT SOURCE-ACTION BOUNDARY")
    z2_fixed_spectrum_orbit()
    determinant_balance()
    conditional_actions()
    natural_action_boundaries()
    jacobi_boundary()
    nni_boundary()
    textual_firewalls()
    print(f"\nSUMMARY: EXACT_PASS={EXACT_PASS} BOUNDARY_PASS={BOUNDARY_PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
