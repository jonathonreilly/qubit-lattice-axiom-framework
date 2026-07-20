#!/usr/bin/env python3
"""Checks enhanced-return arithmetic conditional on an open two-root bound."""

from __future__ import annotations

from decimal import Decimal, localcontext
import importlib.util
import math
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_ENHANCED_COMPLETED_JOINT_RUNNING_LOCAL_JET_"
    "TARGET_TO_NEXT_PRODUCT_SOURCE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md"
)
BLOCK42 = ROOT / "scripts" / (
    "wilson_staggered_enhanced_moment_generated_base_decorated_factor_"
    "return_2026_07_12.py"
)
BLOCK45 = ROOT / "scripts" / (
    "wilson_staggered_external_shortest_center_tail_quadratic_weyl_"
    "reference_2026_07_12.py"
)
C_STAR = 3.0 + 2.0 * math.sqrt(2.0)
SAFE_ROOTS = 68
VISIBLE_MICRO_CHARGE = 1.0e-20


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def outward_float(value: Decimal) -> float:
    """Return a binary64 value greater than or equal to a positive Decimal."""

    result = float(value)
    if value > 0 and result == 0.0:
        return math.nextafter(0.0, math.inf)
    if Decimal.from_float(result) < value:
        return math.nextafter(result, math.inf)
    return result


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    if slack <= 0.0:
        raise ValueError("slack must be positive")
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), n * math.exp(-slack * n)) for n in candidates),
        key=lambda row: row[1],
    )


def enhanced_return_rows(delta: float = 0.001) -> dict[str, float]:
    block42 = load_module("block42_return", BLOCK42)
    block45 = load_module("block45_return", BLOCK45)

    mass = 1.0e96
    theta = 12.4
    allowance = 0.01
    lam = 0.4
    total_weight = theta + 2.0 * allowance + lam
    rows42 = block42.enhanced_rows(
        mass=mass,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=total_weight,
        decorated_lambda=1.0,
    )

    with localcontext() as context:
        context.prec = 120
        dm = Decimal("1e96")
        dtheta = Decimal("12.4")
        dc = Decimal("0.01")
        dlam = Decimal("0.4")
        dc_star = Decimal(3) + Decimal(2) * Decimal(2).sqrt()
        dmu = dm + Decimal(2) / dm
        dhop = Decimal(1) / (Decimal(4) * dm)
        dk_prime = dhop * dhop / dmu
        dmu_prime = dmu - Decimal(8) * dhop * dhop / dmu
        dh_short = Decimal(8) * dk_prime / dmu_prime
        db_star = Decimal(str(rows42["B_star"]))
        dx_q = (dm / dmu_prime) * db_star
        dx_r = dc_star * dh_short * (dtheta + Decimal(2) * dc + dlam).exp()
        dx_full = dx_q + dx_r
        ddet_full = Decimal(3) * dx_full / (Decimal(1) - dx_full)
        ddet_centered = Decimal(2) * ddet_full
        dk_det = ddet_centered.exp() - Decimal(1)
        dref_exponent = Decimal(18) * dc_star**3 * (Decimal(1) / dm) * dk_prime
        # exp(z)-1 <= z/(1-z) for this positive z<1.  Using the rational
        # envelope keeps an e-386 row visible to Decimal even though exp(z)
        # rounds to one at any practical significant-digit precision.
        dref_bond = (
            Decimal(8)
            * (Decimal(2) * (dtheta + Decimal(2) * dc) + dlam).exp()
            * dref_exponent
            / (Decimal(1) - dref_exponent)
        )

    tail_rows = block45.decimal_tail_rows(96, "12.42", "0.4")
    centered_tail_decimal = Decimal(2) * tail_rows["coefficient_row"]
    if not 0 < centered_tail_decimal < Decimal("1e-700"):
        raise ValueError(f"unexpected enhanced centered tail {centered_tail_decimal}")

    k_q = math.expm1(rows42["B_star"])
    k_p0 = k_q
    k_determinant = outward_float(dk_det)
    # The actual Gaussian/boundary rows and both tail arms are positive but
    # below aggregate binary64 resolution.  Keep each visible and outward.
    k_gaussian = VISIBLE_MICRO_CHARGE
    k_boundary = VISIBLE_MICRO_CHARGE
    k_tail_centered = VISIBLE_MICRO_CHARGE
    k_tail_empty = VISIBLE_MICRO_CHARGE
    k_decorated = rows42["K_decorated_bound"]
    k_reference = k_q + k_gaussian + k_determinant
    k_red = (
        k_decorated
        + k_p0
        + k_boundary
        + k_determinant
        + k_tail_centered
    )
    k_total = k_reference + k_red
    n_d, d_value = integer_sup_n_exp(allowance - k_total)
    tau = k_total * d_value
    attachment = 2.0 * d_value * k_red / (1.0 - tau) ** 3
    conversion = SAFE_ROOTS * math.exp(lam / 2.0)
    base_output = conversion * k_total + k_tail_empty
    q_raw = math.exp(-lam / 2.0)
    q_centered = conversion * attachment
    q = max(q_raw, q_centered)

    perturbation_activity = math.expm1(delta)
    k_ball = k_total + perturbation_activity
    n_ball, d_ball = integer_sup_n_exp(allowance - k_ball)
    tau_ball = k_ball * d_ball
    pair_envelope = 1.0 / (1.0 - tau_ball) ** 4
    hessian = conversion * pair_envelope
    tube_left = base_output + q * delta + 0.5 * hessian * delta**2
    tube_margin = delta - tube_left
    source_radius = math.log1p(allowance - k_total)

    complete_output_charge = delta + tube_left + base_output
    theta_weak = theta / 2.0
    epsilon_quadratic = (
        rows42["B_star"]
        + math.exp(-theta_weak) * complete_output_charge
        + k_tail_empty
    )
    gap_ratio = 1.0 - epsilon_quadratic
    sigma_eta = 3.0 * math.log(1.0 / gap_ratio)
    theta_atom = theta_weak - math.log(C_STAR) - sigma_eta
    lambda_atom = lam / 2.0

    # A fixed-field comparison of any scalar onsite reference whose mass lies
    # in [gap_ratio*m,(2-gap_ratio)*m] costs at most this per site.  The exact
    # mass-adapted field torsor is an isometry; this deliberately pays the
    # larger identity-chart alternative.
    reference_delta = gap_ratio ** (-3.0) - 1.0
    reference_transition = 1.0 + math.sqrt(2.0) * reference_delta
    reference_log_cost = math.log(reference_transition)
    returned_theta = theta_atom - reference_log_cost
    returned_lambda = lambda_atom
    next_source_theta = 4.4
    next_source_lambda = 0.2
    output_factor = math.expm1(delta)

    return {
        "mass": mass,
        "theta": theta,
        "allowance": allowance,
        "lambda": lam,
        "total_weight": total_weight,
        "delta": delta,
        "B_star": rows42["B_star"],
        "K_decorated": k_decorated,
        "x_Q_decimal": float(dx_q),
        "log10_x_R": float(dx_r.log10()),
        "K_D": k_determinant,
        "log10_K_G_bound": float(dref_bond.log10()),
        "log10_tail_centered": float(centered_tail_decimal.log10()),
        "K_G_visible": k_gaussian,
        "K_J_visible": k_boundary,
        "K_tail_centered": k_tail_centered,
        "K_tail_empty": k_tail_empty,
        "K_ref": k_reference,
        "K_R": k_red,
        "K_T": k_total,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "A_joint": attachment,
        "conversion": conversion,
        "B": base_output,
        "q_raw": q_raw,
        "q_centered": q_centered,
        "q": q,
        "K_perturb": perturbation_activity,
        "K_ball": k_ball,
        "n_ball": float(n_ball),
        "D_ball": d_ball,
        "tau_ball": tau_ball,
        "pair_envelope": pair_envelope,
        "M": hessian,
        "tube_left": tube_left,
        "tube_margin": tube_margin,
        "source_radius": source_radius,
        "complete_output_charge": complete_output_charge,
        "epsilon_quadratic": epsilon_quadratic,
        "gap_ratio": gap_ratio,
        "sigma_eta": sigma_eta,
        "theta_atom": theta_atom,
        "lambda_atom": lambda_atom,
        "reference_delta": reference_delta,
        "reference_transition": reference_transition,
        "reference_log_cost": reference_log_cost,
        "returned_theta": returned_theta,
        "returned_lambda": returned_lambda,
        "next_source_theta": next_source_theta,
        "next_source_lambda": next_source_lambda,
        "K_output_factor": output_factor,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []
    rows = enhanced_return_rows()

    checks.append(
        (
            "enhanced_completed_joint_activity",
            rows["K_T"] < rows["allowance"]
            and rows["tau"] < 1.0
            and rows["K_G_visible"] > math.ulp(rows["K_T"])
            and rows["K_tail_centered"] > math.ulp(rows["K_T"]),
            "K_dec={:.15e}, K_T={:.15e}<c, D={:.15f}@n={}, tau={:.15e}, visible micro rows={:.1e}>ulp(K_T), log10 G upper bound={:.3f}, log10 centered tail={:.3f}".format(
                rows["K_decorated"],
                rows["K_T"],
                rows["D"],
                int(rows["n_D"]),
                rows["tau"],
                rows["K_G_visible"],
                rows["log10_K_G_bound"],
                rows["log10_tail_centered"],
            ),
        )
    )

    checks.append(
        (
            "conditional_uniform_enhanced_two_mark_tube_arithmetic",
            rows["delta"] < rows["source_radius"]
            and rows["K_ball"] < rows["allowance"]
            and rows["tau_ball"] < 1.0
            and rows["tube_left"] < rows["delta"],
            "K_delta={:.15e}<c, D_delta={:.15f}@n={}, tau_delta={:.15f}, M_delta={:.15f}, tube={:.15e}<delta, margin={:.15e}".format(
                rows["K_ball"],
                rows["D_ball"],
                int(rows["n_ball"]),
                rows["tau_ball"],
                rows["M"],
                rows["tube_left"],
                rows["tube_margin"],
            ),
        )
    )

    # Independent high-precision reconstruction of the ball optimizer,
    # Hessian, and Taylor row from the outward base rows.
    with localcontext() as context:
        context.prec = 80
        dd = Decimal("0.001")
        dc = Decimal("0.01")
        dkt = Decimal(str(rows["K_T"]))
        dkb = dkt + dd.exp() - Decimal(1)
        dslack = dc - dkb
        candidates = [
            (n, Decimal(n) * (-dslack * Decimal(n)).exp())
            for n in (110, 111, 112)
        ]
        dn, dD = max(candidates, key=lambda row: row[1])
        dtau = dkb * dD
        dconv = Decimal(68) * Decimal("0.2").exp()
        dM = dconv / (Decimal(1) - dtau) ** 4
        dB = Decimal(str(rows["B"]))
        dq = Decimal("-0.2").exp()
        dlhs = dB + dq * dd + dM * dd**2 / Decimal(2)
    checks.append(
        (
            "independent_decimal_tube_reconstruction",
            dn == 111
            and math.isclose(float(dtau), rows["tau_ball"], rel_tol=1.0e-15)
            and math.isclose(float(dM), rows["M"], rel_tol=1.0e-15)
            and math.isclose(float(dlhs), rows["tube_left"], rel_tol=1.0e-15)
            and dlhs < dd,
            f"Decimal n={dn}, tau={dtau}, M={dM}, lhs={dlhs}, margin={dd-dlhs}",
        )
    )

    # Retained coefficient lifts are hidden-fiber constant.  The fixture keeps
    # distinct local, raw non-onsite, and centered perturbation coordinates.
    hidden = (-1.0, 1.0)
    reference = {h: 0.5 for h in hidden}
    external = (-0.7, 0.4)

    def response(
        x: float,
        local_scale: float,
        raw_scale: float,
        centered_scale: float,
    ) -> float:
        local_jet = local_scale * (0.13 * x + 0.21 * x**2)
        raw_nonlocal = raw_scale * (0.07 * x - 0.04 * x**3)
        potential = {
            h: (
                0.17 * h
                + 0.09 * x * h
                + local_jet
                + raw_nonlocal
                + centered_scale * (0.11 + 0.03 * x) * h
            )
            for h in hidden
        }
        partition = sum(reference[h] * math.exp(-potential[h]) for h in hidden)
        return -math.log(partition)

    factor_errors = []
    local_mixed_errors = []
    raw_mixed_errors = []
    centered_expectations = []
    nonzero_coordinates = []
    step = 1.0e-4
    for x in external:
        local = 0.13 * x + 0.21 * x**2
        raw_nonlocal = 0.07 * x - 0.04 * x**3
        factor_errors.append(
            abs(
                (
                    response(x, 1.0, 1.0, 0.37)
                    - response(x, 0.0, 0.0, 0.37)
                )
                - local
                - raw_nonlocal
            )
        )
        local_mixed = (
            response(x, step, 0.0, step)
            - response(x, step, 0.0, -step)
            - response(x, -step, 0.0, step)
            + response(x, -step, 0.0, -step)
        ) / (4.0 * step**2)
        raw_mixed = (
            response(x, 0.0, step, step)
            - response(x, 0.0, step, -step)
            - response(x, 0.0, -step, step)
            + response(x, 0.0, -step, -step)
        ) / (4.0 * step**2)
        local_mixed_errors.append(abs(local_mixed))
        raw_mixed_errors.append(abs(raw_mixed))
        centered_expectations.append(
            abs(
                sum(
                    reference[h] * (0.11 + 0.03 * x) * h
                    for h in hidden
                )
            )
        )
        nonzero_coordinates.extend([abs(local), abs(raw_nonlocal)])
    checks.append(
        (
            "three_way_source_split_and_factorization",
            max(factor_errors) < 1.0e-14
            and max(local_mixed_errors) < 2.0e-8
            and max(raw_mixed_errors) < 2.0e-8
            and max(centered_expectations) == 0.0
            and min(nonzero_coordinates) > 0.0,
            "max factorization error={:.3e}, mixed local/centered={:.3e}, "
            "mixed raw/centered={:.3e}, centered expectation={:.1e}".format(
                max(factor_errors),
                max(local_mixed_errors),
                max(raw_mixed_errors),
                max(centered_expectations),
            ),
        )
    )

    # E_1 returns retained coefficients.  P_rel acts there before L_1 lifts
    # the local and raw complement coordinates back to interactions.
    supports = ("local", "nonlocal")
    coarse = {"local": 0.031, "nonlocal": -0.047}
    centered = {"local": 0.013, "nonlocal": -0.019}
    gamma_out = {
        support: {h: coarse[support] + centered[support] * h for h in hidden}
        for support in supports
    }
    expectation = {
        support: sum(reference[h] * gamma_out[support][h] for h in hidden)
        for support in supports
    }
    j_1 = {"local": expectation["local"], "nonlocal": 0.0}
    g_1 = {"local": 0.0, "nonlocal": expectation["nonlocal"]}
    gamma_1_centered = {
        support: {
            h: gamma_out[support][h] - expectation[support] for h in hidden
        }
        for support in supports
    }
    gamma_1_residual = {
        support: {
            h: gamma_out[support][h] - j_1[support] for h in hidden
        }
        for support in supports
    }
    reconstruction_error = max(
        abs(
            gamma_out[support][h]
            - j_1[support]
            - g_1[support]
            - gamma_1_centered[support][h]
        )
        for support in supports
        for h in hidden
    )
    residual_local_expectation = abs(
        sum(
            reference[h] * gamma_1_residual["local"][h] for h in hidden
        )
    )
    centered_expectation_error = max(
        abs(
            sum(
                reference[h] * gamma_1_centered[support][h] for h in hidden
            )
        )
        for support in supports
    )
    residual_nonlocal_expectation = sum(
        reference[h] * gamma_1_residual["nonlocal"][h] for h in hidden
    )
    checks.append(
        (
            "coefficient_valued_next_product_output_split",
            reconstruction_error < 1.0e-16
            and residual_local_expectation < 1.0e-16
            and centered_expectation_error < 1.0e-16
            and math.isclose(
                residual_nonlocal_expectation,
                g_1["nonlocal"],
                rel_tol=0.0,
                abs_tol=1.0e-16,
            )
            and abs(g_1["nonlocal"]) > 0.0,
            "reconstruction error={:.1e}, P_rel E_1 residual={:.1e}, "
            "E_1 centered={:.1e}, retained raw complement={:.3f}".format(
                reconstruction_error,
                residual_local_expectation,
                centered_expectation_error,
                residual_nonlocal_expectation,
            ),
        )
    )

    # A non-scalar Hermitian diagonal fixture separates the scalar trace from
    # the traceless running coefficient without weakening the operator bound.
    epsilon_q = rows["epsilon_quadratic"]
    q_diagonal = [0.6 * epsilon_q, -0.2 * epsilon_q, 0.1 * epsilon_q]
    scalar_trace = sum(q_diagonal) / 3.0
    traceless_diagonal = [entry - scalar_trace for entry in q_diagonal]
    scalar_reconstruction_error = max(
        abs(entry - scalar_trace - traceless)
        for entry, traceless in zip(q_diagonal, traceless_diagonal)
    )
    trace_error = abs(sum(traceless_diagonal))
    operator_norm = max(abs(entry) for entry in q_diagonal)
    mass_ratio = 1.0 + scalar_trace
    checks.append(
        (
            "scalar_trace_reference_and_traceless_ledger",
            scalar_reconstruction_error < 1.0e-20
            and trace_error < 1.0e-20
            and abs(scalar_trace) <= operator_norm <= epsilon_q
            and max(abs(entry) for entry in traceless_diagonal) > 0.0
            and 1.0 - epsilon_q <= mass_ratio <= 1.0 + epsilon_q,
            "reconstruction error={:.1e}, traceless trace={:.1e}, "
            "|scalar|={:.3e}<=op={:.3e}<=epsilon_Q={:.3e}, m_1/m={:.15f}".format(
                scalar_reconstruction_error,
                trace_error,
                abs(scalar_trace),
                operator_norm,
                epsilon_q,
                mass_ratio,
            ),
        )
    )

    mass_ratio_fixture = 1.0 - 0.5 * rows["epsilon_quadratic"]
    rho_fixture = math.sqrt(1.0 / mass_ratio_fixture)
    eta_old_fixture = rows["mass"] ** (-0.5)
    eta_new_fixture = (rows["mass"] * mass_ratio_fixture) ** (-0.5)
    torsor_isometry = math.isclose(
        eta_new_fixture / rho_fixture,
        eta_old_fixture,
        rel_tol=2.0e-15,
    ) and math.isclose(
        rows["mass"] / rho_fixture**2,
        rows["mass"] * mass_ratio_fixture,
        rel_tol=2.0e-15,
    )
    checks.append(
        (
            "gap_atom_and_reference_transition_return",
            rows["gap_ratio"] > 0.99999
            and rows["returned_theta"] > rows["next_source_theta"]
            and rows["returned_lambda"] >= rows["next_source_lambda"]
            and rows["K_output_factor"] < rows["allowance"]
            and torsor_isometry,
            "complete charge={:.15e}, eps_Q={:.15e}, gap/m={:.15f}, theta_atom={:.15f}, logT_ref={:.15e}, returned=({:.15f},{:.1f})>(4.4,0.2), torsor isometry={}, expm1(delta)={:.15e}<c".format(
                rows["complete_output_charge"],
                rows["epsilon_quadratic"],
                rows["gap_ratio"],
                rows["theta_atom"],
                rows["reference_log_cost"],
                rows["returned_theta"],
                rows["returned_lambda"],
                torsor_isometry,
                rows["K_output_factor"],
            ),
        )
    )

    block42 = load_module("block42_failure", BLOCK42)
    low_mass_failed = False
    low_mass_message = ""
    try:
        block42.enhanced_rows(
            mass=1.0e64,
            block40_cluster_reserve=0.2,
            block41_reserve=0.2,
            decorated_theta=rows["total_weight"],
            decorated_lambda=1.0,
        )
    except ValueError as exc:
        low_mass_failed = True
        low_mass_message = str(exc)
    next_fixed_theta = 4.38 / 2.0 - math.log(C_STAR)
    checks.append(
        (
            "finite_horizon_not_autonomous_boundary",
            low_mass_failed
            and next_fixed_theta < 4.4
            and rows["theta"] > rows["next_source_theta"],
            f"m=1e64 enhanced rerun fails ({low_mass_message}); unchanged next atom theta before eta charge={next_fixed_theta:.15f}<4.4; enhanced source theta={rows['theta']:.1f}",
        )
    )

    text = NOTE.read_text()
    runner_prefix = Path(__file__).read_text().split("hidden_phrases =", 1)[0].lower()
    pre_n3 = text.split("### N3", 1)[0].lower()
    hidden_phrases = [
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard qft",
        "registered",
        "canonical",
    ]
    phrase_counts = {
        phrase: pre_n3.count(phrase) + runner_prefix.count(phrase)
        for phrase in hidden_phrases
    }
    checks.append(
        (
            "hidden_condition_phrase_scan",
            phrase_counts == {phrase: 0 for phrase in hidden_phrases},
            f"pre-N3 note plus pre-scan runner counts={phrase_counts}",
        )
    )

    required = [
        "**Type:** open_gate",
        "conditional on the open Block47 two-root proof obligation",
        "P_rel=P_0",
        "j=P_rel E_ref H",
        "g=(1-P_rel)E_ref H",
        "h^o=(1-L E_ref)H",
        "R(Phi+L(j+g)+h^o)=L(j+g)+R(Phi+h^o)",
        "j_1=P_rel E_1 Gamma_out",
        "Gamma_1^res=Gamma_out-L_1j_1=L_1g_1+gamma_1^o",
        "P_sc Q=(tr_color Q/3)I",
        "widehat Q_1=m^(-1)P_quad j_1",
        "theta_return=theta_atom-log T_ref",
        "target-to-next-product-source return section",
        "No axiom-update stop",
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
    ]
    missing = [item for item in required if item not in text]
    forbidden = [
        "proves an autonomous invariant ball",
        "proves all-horizon control",
        "proves a continuum limit",
        "requires a new axiom",
        "NOT_TESTED",
        "f=P_rel E_ref H",
        "J_1=P_rel C_1 Gamma_out",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_COMPLETED_JOINT_TWO_MARK_COVARIANCE_NONLINEAR_SOURCE_OUTPUT_TUBE_BOUNDED_THEOREM_NOTE_2026-07-13.md",
            "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_SCALAR_PRODUCT_REFERENCE_COMPLETED_JOINT_OUTER_HAAR_ACTUAL_OUTPUT_ATOM_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md",
        ]
    )
    dependencies = sorted(set(re.findall(r"\]\(([^)#?]+\.md)\)", text)))
    checks.append(
        (
            "repository_dependency_set",
            dependencies == expected_dependencies,
            f"markdown_dependency_set={dependencies}",
        )
    )

    passed = sum(ok for _, ok, _ in checks)
    failed = len(checks) - passed
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
