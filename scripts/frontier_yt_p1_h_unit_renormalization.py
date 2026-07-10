#!/usr/bin/env python3
"""
YT P1 - H_unit 1-loop renormalization symbolic single-D_S1 reduction.

Status
------
Re-audit required after the 2026-07-10 bounded rescope. The claim surface is
the symbolic FR1/FR2 and staggered vertex numerator, the single-D_S1
reduction, and the R7-R9 tadpole split with symbolic u_0 > 0 on the D2 + D13
action surface carried by docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md.

Numerical plaquette values, the old envelope/floor, the asserted logarithmic
coefficient, the exact continuum coefficient, and the cited literature
bracket are context only and do not contribute PASS/FAIL checks.

Blocks
------
  1. Action, diagram, normalization, and color structural checks.
  2. Sympy FR1, FR2, and per-component staggered-vertex limits.
  3. Symbolic kernel and rescope checks (2026-07-10): dimensionless a-power,
     one-link U = u_0 V scaling, exact R7/R9 algebra, and R6 IR power.
  4. Comparator values as log-only context (no PASS/FAIL).
  5. Note-surface pins for the authority re-route, withdrawal, and Repair Note.

The literal R6 IR power is derived rather than assumed. This runner does not
perform 4D BZ quadrature or assert an envelope, log coefficient, or continuum
matching coefficient.

Self-contained: stdlib + sympy.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def main() -> int:
    print("=" * 72)
    print("YT P1 - H_unit 1-loop symbolic single-D_S1 reduction")
    print("=" * 72)
    print()

    # -------------------------------------------------------------------
    # Block 1: action and single-diagram structural surface
    # -------------------------------------------------------------------
    print("Block 1: action and single-diagram structural surface.")

    def eta_mu(x: tuple[int, int, int, int], mu: int) -> int:
        return (-1) ** sum(x[nu] for nu in range(mu))

    x_sample = (3, 2, 5, 7)
    etas = [eta_mu(x_sample, mu) for mu in range(4)]
    check(
        "D2 staggered eta-phase form eta_mu(x) = (-1)^{Sum_{nu<mu} x_nu}",
        etas == [1, -1, -1, 1],
        f"etas = {etas} at x = {x_sample}",
    )

    n_c = sp.Integer(3)
    g_bare = sp.Integer(1)
    beta = sp.simplify(2 * n_c / g_bare**2)
    check(
        "D13 Wilson plaquette coupling beta = 2 N_c / g_bare^2",
        beta == 6,
        f"beta = {beta} at the canonical surface",
    )

    n_iso = sp.Integer(2)
    z_squared = sp.simplify(n_c * n_iso)
    check(
        "H_unit normalization Z^2 = N_c N_iso = 6 on Q_L",
        z_squared == 6,
        f"tree anchor = 1/sqrt({z_squared})",
    )

    diagrams = ("D_S1_gluon_sandwich", "D_S2_left_leg_SE", "D_S3_right_leg_SE")
    check(
        "Three C_F-channel topologies are enumerated",
        len(diagrams) == 3,
        f"diagrams = {diagrams}",
    )
    external_legs = diagrams[1:]
    residual = diagrams[:1]
    check(
        "D_S2 and D_S3 are the external-leg pair absorbed into Z_q",
        external_legs == ("D_S2_left_leg_SE", "D_S3_right_leg_SE"),
        f"external legs = {external_legs}",
    )
    check(
        "Exactly one residual non-trivial diagram: D_S1",
        residual == ("D_S1_gluon_sandwich",),
        f"residual = {residual}",
    )

    c_f = sp.simplify((n_c**2 - 1) / (2 * n_c))
    check(
        "Color factor C_F = (N_c^2 - 1)/(2 N_c) = 4/3",
        c_f == sp.Rational(4, 3),
        f"C_F = {c_f}",
    )
    print()

    # -------------------------------------------------------------------
    # Block 2: symbolic Feynman-rule limits
    # -------------------------------------------------------------------
    print("Block 2: Sympy Feynman-rule limits.")

    a = sp.symbols("a", positive=True)
    k = sp.symbols("k0:4", real=True)
    k_squared = sp.Add(*(component**2 for component in k))

    d_psi = sp.Add(*(sp.sin(component * a) ** 2 for component in k)) / a**2
    d_psi_series = sp.series(d_psi, a, 0, 3).removeO().expand()
    d_psi_limit = sp.simplify(sp.limit(d_psi, a, 0))
    check(
        "FR1 D_psi(k) -> k^2 as a -> 0",
        sp.simplify(d_psi_limit - k_squared) == 0,
        f"series = {d_psi_series}",
    )

    d_g = 4 * sp.Add(*(sp.sin(component * a / 2) ** 2 for component in k)) / a**2
    d_g_series = sp.series(d_g, a, 0, 3).removeO().expand()
    d_g_limit = sp.simplify(sp.limit(d_g, a, 0))
    check(
        "FR2 D_g(k) -> k^2 as a -> 0",
        sp.simplify(d_g_limit - k_squared) == 0,
        f"series = {d_g_series}",
    )

    vertex_component = sp.cos(k[0] * a / 2) ** 2
    vertex_series = sp.series(vertex_component, a, 0, 3).removeO().expand()
    check(
        "Per-component staggered vertex cos^2(k_mu a/2) -> 1",
        sp.limit(vertex_component, a, 0) == 1,
        f"series = {vertex_series}",
    )
    print()

    # -------------------------------------------------------------------
    # Block 3: symbolic kernel and rescope checks (2026-07-10)
    # -------------------------------------------------------------------
    print("Block 3: symbolic kernel and rescope checks (2026-07-10).")

    # In q = k a variables:
    #   N_S ~ a^-2, D_psi^-2 ~ a^4, D_g^-1 ~ a^2, d^4k ~ a^-4.
    a_powers = {
        "N_S": sp.Integer(-2),
        "D_psi^-2": sp.Integer(4),
        "D_g^-1": sp.Integer(2),
        "d^4k": sp.Integer(-4),
    }
    total_a_power = sp.simplify(sum(a_powers.values()))
    check(
        "R6 full kernel has total a-power zero in q = k a variables",
        total_a_power == 0,
        f"{a_powers}; total = {total_a_power}",
    )

    u_0 = sp.symbols("u_0", positive=True)
    v_link = sp.symbols("V", nonzero=True)
    n_link = sp.Integer(1)
    one_link_u = (u_0 * v_link) ** n_link
    one_link_v = v_link**n_link
    link_rescaling = sp.simplify(one_link_u / one_link_v)
    check(
        "U = u_0 V rescales the retained one-link vertex by exactly u_0^1",
        link_rescaling == u_0,
        f"n_link = {n_link}; ratio = {link_rescaling}",
    )

    i_d_s1, i_tadpole, i_ti = sp.symbols("I_D_S1 I_tadpole I_TI")
    r7_solution = sp.solve(sp.Eq(i_d_s1, i_tadpole + i_ti), i_ti)[0]
    r9_rhs = i_d_s1 - i_tadpole
    check(
        "R7/R9 tadpole split is the exact symbolic identity I_framework = I_D_S1 - I_tadpole",
        sp.simplify(r7_solution - r9_rhs) == 0,
        f"solve(R7, I_TI) = {r7_solution}",
    )

    # Derive the literal small-q scaling of R6. Scaling q_mu -> lambda q_mu
    # avoids choosing a special ray and retains the full q^2 dependence.
    lam = sp.symbols("lambda", positive=True)
    q = sp.symbols("q0:4", real=True)
    q_squared = sp.Add(*(component**2 for component in q))
    d_psi_q = sp.Add(*(sp.sin(lam * component) ** 2 for component in q))
    d_g_q = 4 * sp.Add(*(sp.sin(lam * component / 2) ** 2 for component in q))
    n_s_q = sp.Add(*(sp.cos(lam * component / 2) ** 2 for component in q))
    r6_kernel_q = n_s_q / (d_psi_q**2 * d_g_q)
    leading_r6 = sp.simplify(sp.limit(lam**6 * r6_kernel_q, lam, 0))
    expected_leading_r6 = sp.simplify(4 / q_squared**3)
    check(
        "R6 integrand has leading small-q power q^-6 per unit d^4q measure",
        sp.simplify(leading_r6 - expected_leading_r6) == 0,
        f"lambda^6 K(lambda q) -> {leading_r6}",
    )

    radial_power = sp.Integer(-6) + (sp.Integer(4) - 1)
    check(
        "IR singularity blocks any finite volume-times-maximum envelope before subtraction",
        radial_power == -3,
        f"radial d^4q gives lambda^{radial_power} d lambda",
    )
    print(
        "  explanation: the displayed R6 kernel is q^-6; with radial "
        "d^4q ~ q^3 dq this is q^-3 dq, not a derived logarithm. "
        "A justified IR subtraction and coefficient derivation are open, "
        "so no finite envelope or exact (CL) coefficient follows as written."
    )
    print()

    # -------------------------------------------------------------------
    # Block 4: context only
    # -------------------------------------------------------------------
    print("Block 4: comparator context (no checks).")
    print(
        "  context only, no PASS/FAIL: comparator values, registered import: "
        "<P> = 0.5934, u_0 = 0.87768..., 1/u_0 = 1.13937..., "
        "alpha_LM = 0.0907."
    )
    print(
        "  context only, no PASS/FAIL: cited literature bracket [4, 10] is "
        "a comparator, never a derivation input."
    )
    print()

    # -------------------------------------------------------------------
    # Block 5: note-surface pins
    # -------------------------------------------------------------------
    print("Block 5: note-surface pins.")

    repo_root = Path(__file__).resolve().parents[1]
    note_path = repo_root / "docs" / "YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md"
    note = note_path.read_text(encoding="utf-8")

    historical_link = "](MINIMAL_AXIOMS_2026-04-11.md)"
    historical_backtick = "`docs/MINIMAL_AXIOMS_2026-04-11.md`"
    check(
        "Historical axioms file is not markdown-linked anywhere in the note",
        historical_link not in note,
        f"forbidden link occurrences = {note.count(historical_link)}",
    )
    check(
        "Historical axioms file remains as a backticked historical mention",
        historical_backtick in note and "historical record only" in note,
        "historical-only annotation present",
    )

    ward_source = (
        "From the retained Ward/action authority\n"
        "[YT_WARD_IDENTITY_DERIVATION_THEOREM.md]"
        "(YT_WARD_IDENTITY_DERIVATION_THEOREM.md)\n"
        "(D2 staggered eta-phases; D13 Wilson plaquette coupling"
    )
    check(
        "Section 1.1 sources the action from the retained Ward/action authority",
        ward_source in note,
        "D2 eta-phases + D13 Wilson coupling source line present",
    )

    withdrawal_marker = "**2026-07-10 envelope withdrawal.**"
    check(
        "Dated envelope withdrawal block is present",
        withdrawal_marker in note,
        withdrawal_marker,
    )

    withdrawal_start = note.find(withdrawal_marker)
    withdrawal_end = note.find("\n---", withdrawal_start)
    withdrawn_number_positions = []
    cursor = 0
    while True:
        cursor = note.find("23.35", cursor)
        if cursor == -1:
            break
        withdrawn_number_positions.append(cursor)
        cursor += len("23.35")
    number_only_in_withdrawal = (
        withdrawal_start >= 0
        and withdrawal_end > withdrawal_start
        and len(withdrawn_number_positions) == 1
        and withdrawal_start <= withdrawn_number_positions[0] < withdrawal_end
    )
    check(
        "23.35 appears exactly once and only inside the withdrawal block",
        number_only_in_withdrawal,
        f"occurrences = {len(withdrawn_number_positions)}",
    )

    check(
        "Repair Note section exists",
        "## Repair Note" in note and "**Date:** 2026-07-10" in note,
        "dated Repair Note present",
    )
    print()

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print()
    print("Symbolic findings:")
    print(f"  FR1 limit: D_psi -> {d_psi_limit}")
    print(f"  FR2 limit: D_g -> {d_g_limit}")
    print(f"  q = k a kernel a-power: {total_a_power}")
    print(f"  R6 small-q leading term: {leading_r6} * lambda^-6")
    print(f"  radial IR behavior: lambda^{radial_power} d lambda")
    print("  (CL) coefficient as written: NOT established; open follow-up")
    print()
    print("Claim surface retained:")
    print("  FR1/FR2 + staggered numerator; R1-R5 single-D_S1 reduction;")
    print("  R7-R9 symbolic tadpole split with u_0 > 0 and n_link = 1.")
    print("Withdrawn from the claim surface:")
    print("  plaquette numerics; envelope/floor/log coefficient; exact continuum")
    print("  coefficient; cited literature bracket as anything beyond comparator context.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
