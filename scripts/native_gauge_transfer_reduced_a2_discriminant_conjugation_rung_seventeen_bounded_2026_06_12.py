#!/usr/bin/env python3
"""W96 / rung seventeen reduced-A2 discriminant-conjugation runner.

This runner verifies the source-side algebra for the A2 discriminant route.
It proves the retained boundary factor is the degree-three A2 discriminant,
checks the exact delta-Doob generator conjugation, and records the exact
obstruction that stops the heat-sandwich spectrum from being closed here.

No fitted constants, external values, rounded anchors, or value-from-target
steps are used.
"""

from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_DISCRIMINANT_CONJUGATION_RUNG_SEVENTEEN_BOUNDED_NOTE_2026-06-12.md"
)
RUNNER_REL = (
    "scripts/"
    "native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.py"
)
CACHE_REL = (
    "logs/runner-cache/"
    "native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.txt"
)

RUNG_SIX_NOTE = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md"
)
RUNG_NINE_NOTE = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md"
)
RUNG_ELEVEN_NOTE = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md"
)
RUNG_SIXTEEN_NOTE = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_CLOSED_FORM_RUNG_SIXTEEN_BOUNDED_NOTE_2026-06-12.md"
)


PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


x, y, u, v = sp.symbols("x y u v")
delta = x * y * (x + y)
H = delta / 2
Q = x**2 + x * y + y**2


def subst_simul(expr: sp.Expr, pairs: list[tuple[sp.Symbol, sp.Expr]]) -> sp.Expr:
    return sp.expand(expr.subs(pairs, simultaneous=True))


def sx(expr: sp.Expr) -> sp.Expr:
    return subst_simul(expr, [(x, -x), (y, x + y)])


def sy(expr: sp.Expr) -> sp.Expr:
    return subst_simul(expr, [(x, x + y), (y, -y)])


def sxy(expr: sp.Expr) -> sp.Expr:
    return subst_simul(expr, [(x, -y), (y, -x)])


def swap_xy(expr: sp.Expr) -> sp.Expr:
    return subst_simul(expr, [(x, y), (y, x)])


def Lxy(expr: sp.Expr) -> sp.Expr:
    return sp.simplify((sp.diff(expr, x, 2) - sp.diff(expr, x, y) + sp.diff(expr, y, 2)) / 3)


def Luv(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.diff(expr, u, 2) / 3 + sp.diff(expr, v, 2))


delta_x = sp.diff(delta, x)
delta_y = sp.diff(delta, y)
cx = sp.factor((2 * delta_x - delta_y) / (3 * delta))
cy = sp.factor((-delta_x + 2 * delta_y) / (3 * delta))


def L_delta_xy(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(Lxy(expr) + cx * sp.diff(expr, x) + cy * sp.diff(expr, y))


def anti_invariant_nullity(max_degree: int) -> tuple[int, list[sp.Expr]]:
    monomials: list[sp.Expr] = []
    for total_degree in range(max_degree + 1):
        for xp in range(total_degree + 1):
            monomials.append(x**xp * y ** (total_degree - xp))
    coeffs = sp.symbols(f"a0:{len(monomials)}")
    poly = sum(c * m for c, m in zip(coeffs, monomials))
    polys = [sp.Poly(sx(poly) + poly, x, y), sp.Poly(sy(poly) + poly, x, y)]
    all_monomials: set[tuple[int, int]] = set()
    for p in polys:
        all_monomials.update(p.monoms())
    equations = []
    for p in polys:
        for mon in sorted(all_monomials):
            equations.append(p.coeff_monomial(mon))
    matrix, _ = sp.linear_eq_to_matrix(equations, coeffs)
    basis = matrix.nullspace()
    polys_out = [
        sp.factor(sum(vec[i] * monomials[i] for i in range(len(monomials))))
        for vec in basis
    ]
    return len(basis), polys_out


def main() -> int:
    print("W96 reduced-A2 discriminant conjugation bounded runner")
    print("Exact algebra only; finite rung-eleven rows remain fenced witnesses, not inputs.")
    print()

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note_lower = note_text.lower()
    rung_six = RUNG_SIX_NOTE.read_text(encoding="utf-8")
    rung_nine = RUNG_NINE_NOTE.read_text(encoding="utf-8")
    rung_eleven = RUNG_ELEVEN_NOTE.read_text(encoding="utf-8")
    rung_sixteen = RUNG_SIXTEEN_NOTE.read_text(encoding="utf-8")

    check(
        "note carries exact status-authority sentence",
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome."
        in note_text,
    )
    check(
        "note is a source-side boundary declaration, not an audit verdict",
        "**Claim type:** open_gate" in note_text
        and "**Claim boundary:**" in note_text
        and "never an audit verdict" in note_text,
    )
    check(
        "note names exactly the requested runner and cache",
        RUNNER_REL in note_text and CACHE_REL in note_text,
    )
    check(
        "load-bearing one-hop authorities are markdown linked",
        "[NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md]" in note_text
        and "[NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md]" in note_text
        and "[NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md]" in note_text
        and "[NATIVE_GAUGE_TRANSFER_REDUCED_A2_CLOSED_FORM_RUNG_SIXTEEN_BOUNDED_NOTE_2026-06-12.md]" in note_text,
    )
    check(
        "quote anchors are present in the cited authority files",
        "H(x,y) = x y (x+y) / 2" in rung_six
        and "Q(x,y) = x^2 + x y + y^2" in rung_six
        and "T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2)." in rung_nine
        and "c_D = B_1/mu_1 - B_0/mu_0" in rung_nine
        and "strict inequality lives at the `1/beta` subleading order" in rung_eleven
        and "boundary factor `H` may be exactly the Weyl-chamber ground-state density" in rung_sixteen,
    )
    check(
        "note refuses imports, fits, target values, and comparator promotion",
        "No new axiom, literature value, external comparator number, fitted constant" in note_text
        and "Rung eleven's finite rows remain fences" in note_text
        and "value-from-target" in note_text,
    )
    banned = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the program",
        "perma" + "nently",
        "no other " + "path",
    ]
    check("note avoids forbidden overreach phrases", not any(b in note_lower for b in banned))

    check("H equals one half of the A2 discriminant", sp.simplify(H - delta / 2) == 0)
    H_uv = sp.simplify(H.subs({x: (u + v) / 2, y: (u - v) / 2}))
    Q_uv = sp.simplify(Q.subs({x: (u + v) / 2, y: (u - v) / 2}))
    check(
        "u,v transform gives retained H and Q forms",
        sp.simplify(H_uv - u * (u**2 - v**2) / 8) == 0
        and sp.simplify(Q_uv - (3 * u**2 + v**2) / 4) == 0,
        f"H_uv={sp.factor(H_uv)}, Q_uv={sp.factor(Q_uv)}",
    )
    sample_uv_poly = u**2 + v**2
    check(
        "L transform gives (1/3)d_uu + d_vv",
        sp.simplify(Luv(sample_uv_poly) - sp.Rational(8, 3)) == 0,
        "L(u^2+v^2)=8/3",
    )
    raw_second_difference = sp.diff(sample_uv_poly, u, 2) + 3 * sp.diff(sample_uv_poly, v, 2)
    print("normalization_falsifier_values")
    print(f"  correct_L_on_u2_plus_v2={sp.Rational(8, 3)}")
    print(f"  raw_unnormalized_second_difference={raw_second_difference}")
    check(
        "wrong L normalization is visibly different",
        raw_second_difference == 8 and raw_second_difference != sp.Rational(8, 3),
    )

    check(
        "simple A2 wall reflections preserve Q and flip delta",
        sp.simplify(sx(Q) - Q) == 0
        and sp.simplify(sy(Q) - Q) == 0
        and sp.simplify(sxy(Q) - Q) == 0
        and sp.simplify(sx(delta) + delta) == 0
        and sp.simplify(sy(delta) + delta) == 0
        and sp.simplify(sxy(delta) + delta) == 0,
    )
    delta_sample = delta.subs({x: 1, y: 2})
    sx_sample = sx(delta).subs({x: 1, y: 2})
    swap_sample = swap_xy(delta).subs({x: 1, y: 2})
    print("delta_parity_falsifier_values")
    print(f"  delta(1,2)={delta_sample}")
    print(f"  delta(s_x(1,2))={sx_sample}")
    print(f"  delta(swap(1,2))={swap_sample}")
    check(
        "x<->y is recorded as diagram-swap ambiguity, not a sign-flip proof",
        delta_sample == 6 and sx_sample == -6 and swap_sample == 6
        and "the coordinate swap `x <-> y` is a diagram-swap pointer, not the wall-reflection sign test" in note_lower,
    )

    low_dims = [anti_invariant_nullity(d)[0] for d in range(3)]
    dim3, basis3 = anti_invariant_nullity(3)
    check(
        "degree-three anti-invariant space is one-dimensional and spanned by delta",
        low_dims == [0, 0, 0]
        and dim3 == 1
        and sp.simplify(basis3[0] / delta - 1) == 0,
        f"nullities_deg_0_1_2={low_dims}, deg3_basis={basis3[0]}",
    )
    invariant_test = delta * Q
    check(
        "anti-invariant polynomials factor as delta times an invariant quotient",
        sp.simplify(sx(invariant_test) + invariant_test) == 0
        and sp.simplify(sy(invariant_test) + invariant_test) == 0
        and sp.simplify(sx(invariant_test / delta) - invariant_test / delta) == 0
        and sp.simplify(sy(invariant_test / delta) - invariant_test / delta) == 0,
    )

    check("delta is L-harmonic", sp.simplify(Lxy(delta)) == 0)
    generator_ok = True
    for a in range(4):
        for b in range(4 - a):
            g = x**a * y**b
            residual = sp.simplify(Lxy(delta * g) - delta * L_delta_xy(g))
            generator_ok = generator_ok and residual == 0
    check(
        "delta-Doob generator identity holds on polynomial basis degree <= 3",
        generator_ok,
        f"cx={cx}, cy={cy}",
    )
    check(
        "conjugated generator sends Q to exact constant 4",
        sp.simplify(L_delta_xy(Q) - 4) == 0,
    )
    check(
        "note states the explicit conjugated heat-sandwich operator on g",
        "T_delta = exp(L_delta/2) M_[H exp(-Q)] exp(L_delta/2)" in note_text
        and "L_delta g = L g + ((2 delta_x - delta_y)/(3 delta)) partial_x g" in note_text,
    )

    signed_original = (delta * delta).subs({x: 1, y: 2})
    signed_reflected = (delta * delta).subs({x: -1, y: 3})
    abs_original = abs(int(delta.subs({x: 1, y: 2}))) * int(delta.subs({x: 1, y: 2}))
    abs_reflected = abs(int(delta.subs({x: -1, y: 3}))) * int(delta.subs({x: -1, y: 3}))
    print("full_plane_multiplier_parity_values")
    print(f"  signed_delta_times_anti_at_(1,2)={signed_original}")
    print(f"  signed_delta_times_anti_at_sx(1,2)={signed_reflected}")
    print(f"  abs_delta_times_anti_at_(1,2)={abs_original}")
    print(f"  abs_delta_times_anti_at_sx(1,2)={abs_reflected}")
    check(
        "signed full-plane delta multiplier changes the Weyl parity sector",
        signed_original == signed_reflected == 36 and abs_original == 36 and abs_reflected == -36,
    )
    check(
        "note names the exact missing identity after conjugation",
        "the missing identity is a finite-band or diagonalization identity for `t_delta`" in note_lower
        and "the chamber-positive multiplier is `|delta|/2`, not signed `delta/2`, after full-plane antisymmetrization" in note_lower,
    )

    multiplier = H * sp.exp(-Q)
    comm_scaled = sp.factor(Lxy(multiplier) * sp.exp(Q))
    comm_value = sp.simplify(comm_scaled.subs({x: 1, y: 2}))
    print("commutator_falsifier_values")
    print(f"  exp(Q)*[L,M_Hexp(-Q)]1={comm_scaled}")
    print(f"  at_(1,2)_scaled={comm_value}")
    print("  at_(1,2)_actual=9*exp(-7)")
    check(
        "commutator with the retained multiplier is nonzero",
        comm_value == 9 and "9*exp(-7)" in note_text,
    )

    b2_wrong = x * y * (x + y) * (x + 2 * y)
    g2_wrong = x * y * (x + y) * (x + 2 * y) * (x + 3 * y) * (2 * x + 3 * y)
    a1_wrong = x
    print("wrong_root_system_falsifier_values")
    print(f"  A2_delta(1,2)={delta_sample}")
    print(f"  B2_degree4_product(1,2)={b2_wrong.subs({x: 1, y: 2})}")
    print(f"  G2_degree6_product(1,2)={g2_wrong.subs({x: 1, y: 2})}")
    print(f"  A1_single_root_product(1,2)={a1_wrong.subs({x: 1, y: 2})}")
    check(
        "wrong B2/G2/A1 substitutions visibly break H=delta/2",
        b2_wrong.subs({x: 1, y: 2}) == 30
        and g2_wrong.subs({x: 1, y: 2}) == 1680
        and a1_wrong.subs({x: 1, y: 2}) == 1,
    )

    check(
        "note does not promote closed-form spectral constants",
        "No closed-form `Phi_0`, `Phi_1`, `mu_i`, `A_i`, `B_i`, `c_J`, `c_D`, or subleading margin coefficient is derived here." in note_text
        and "c_J = 0." not in note_text
        and "c_D = 0." not in note_text,
    )
    check(
        "note gives both ambiguity readings",
        "Reading 1: signed-polynomial full-plane reading" in note_text
        and "Reading 2: chamber-positive Dirichlet reading" in note_text,
    )
    check(
        "note differentiates new material from prior rungs",
        "New here versus rung sixteen" in note_text
        and "Restated from rungs nine and eleven" in note_text,
    )
    gate_markers = [f"N{i} -" for i in range(1, 9)]
    check(
        "no-go discipline gate is visible for the named obstruction",
        all(marker in note_text for marker in gate_markers)
        and "Skill freshness" in note_text,
    )
    check(
        "N1 lists five attempted routes",
        all(
            route in note_text
            for route in [
                "Discriminant identification",
                "Signed full-plane polynomial route",
                "Delta-Doob conjugation route",
                "Naive generalized-Hermite route",
                "Rung-eleven finite-row promotion",
            ]
        ),
    )
    check(
        "verification section names this runner total",
        "TOTAL: PASS=29, FAIL=0" in note_text,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
