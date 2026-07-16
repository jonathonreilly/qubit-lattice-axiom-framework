#!/usr/bin/env python3
"""Checks the completed-joint two-mark bound and one nonlinear bundle tube."""

from __future__ import annotations

import importlib.util
import itertools
import math
from pathlib import Path
import re
from decimal import Decimal, localcontext


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_COMPLETED_JOINT_TWO_MARK_COVARIANCE_NONLINEAR_"
    "SOURCE_OUTPUT_TUBE_BOUNDED_THEOREM_NOTE_2026-07-13.md"
)
BLOCK46 = ROOT / "scripts" / (
    "wilson_staggered_scalar_product_reference_completed_joint_atom_"
    "return_2026_07_13.py"
)
C_STAR = 3.0 + 2.0 * math.sqrt(2.0)
SAFE_ROOTS = 68


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    if slack <= 0.0:
        raise ValueError("slack must be positive")
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), n * math.exp(-slack * n)) for n in candidates),
        key=lambda row: row[1],
    )


def normalized_average(
    values: dict[tuple[int, int], float], weights: dict[tuple[int, int], float]
) -> float:
    denominator = sum(weights.values())
    return sum(values[point] * weights[point] for point in values) / denominator


def tube_rows(delta: float = 0.001) -> dict[str, float]:
    block46 = load_module("block46", BLOCK46)
    base = block46.first_joint_rows()
    allowance = base["allowance"]
    perturbation_activity = math.expm1(delta)
    k_ball = base["K_T"] + perturbation_activity
    slack = allowance - k_ball
    n_d, d_value = integer_sup_n_exp(slack)
    tau = k_ball * d_value
    conversion = SAFE_ROOTS * math.exp(base["lambda"] / 2.0)
    # One complete rooted marked side costs 1+H=(1-tau)^-2.  Multiplying
    # the two ordered sides overcounts disconnected and shared structures,
    # so (1-tau)^-4 is a conservative two-mark envelope.
    pair_envelope = 1.0 / (1.0 - tau) ** 4
    hessian = conversion * pair_envelope
    base_output = base["B_out_total"]
    linear = base["q"]
    tube_left = base_output + linear * delta + 0.5 * hessian * delta**2
    source_radius = math.log1p(allowance - base["K_T"])

    # T_res excludes the declared Hermitian onsite quadratic center.  For the
    # complete quadratic gap, separately charge its raw shift by delta and
    # every generated residual output by the full residual-tube envelope.
    complete_output_charge = delta + tube_left + base_output
    epsilon_quadratic = (
        base["B_star"]
        + math.exp(-base["theta_weak"]) * complete_output_charge
        + base["K_tail_empty"]
    )
    gap_ratio = 1.0 - epsilon_quadratic
    sigma_eta = 3.0 * math.log(1.0 / gap_ratio)
    theta_atom = base["theta_weak"] - math.log(C_STAR) - sigma_eta
    output_factor = math.expm1(delta)
    return {
        **{f"base_{key}": value for key, value in base.items()},
        "delta": delta,
        "K_perturb": perturbation_activity,
        "K_ball": k_ball,
        "slack": slack,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "conversion": conversion,
        "pair_envelope": pair_envelope,
        "M_pair": hessian,
        "B": base_output,
        "q": linear,
        "tube_left": tube_left,
        "tube_margin": delta - tube_left,
        "complete_output_charge": complete_output_charge,
        "source_radius": source_radius,
        "epsilon_quadratic": epsilon_quadratic,
        "gap_ratio": gap_ratio,
        "sigma_eta": sigma_eta,
        "theta_atom": theta_atom,
        "K_output_factor": output_factor,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    # An exact finite product fixture checks the full Hessian split at a
    # nontrivially tilted base.  Fiber-constant lifts have zero covariance
    # with every mark; two product-centered marks have a nonzero covariance.
    points = list(itertools.product((-1, 1), repeat=2))
    product_weights = {point: 0.25 for point in points}
    base_potential = {
        (u, v): 0.17 * u * v + 0.06 * u - 0.04 * v for u, v in points
    }
    physical_weights = {
        point: product_weights[point] * math.exp(-base_potential[point])
        for point in points
    }
    raw = {point: 0.73 for point in points}
    mark_f = {(u, v): float(u) for u, v in points}
    mark_g = {(u, v): 0.6 * u + 0.8 * v for u, v in points}

    def covariance(
        left: dict[tuple[int, int], float],
        right: dict[tuple[int, int], float],
        weights: dict[tuple[int, int], float],
    ) -> float:
        product = {point: left[point] * right[point] for point in points}
        return normalized_average(product, weights) - normalized_average(
            left, weights
        ) * normalized_average(right, weights)

    cov_raw_raw = covariance(raw, raw, physical_weights)
    cov_raw_mark = covariance(raw, mark_f, physical_weights)
    cov_marks = covariance(mark_f, mark_g, physical_weights)
    direct_product_covariance = covariance(mark_f, mark_g, product_weights)
    checks.append(
        (
            "fiber_constant_raw_hessian_blocks_vanish",
            abs(cov_raw_raw) < 1.0e-14
            and abs(cov_raw_mark) < 1.0e-14
            and abs(cov_marks) > 0.1
            and abs(direct_product_covariance) > 0.1,
            "Cov(raw,raw)={:.3e}, Cov(raw,Fo)={:.3e}, Cov_Phi(Fo,Go)={:.12f}, direct E0 pair={:.12f}".format(
                cov_raw_raw, cov_raw_mark, cov_marks, direct_product_covariance
            ),
        )
    )

    # A fiber-constant raw perturbation factors from numerator and denominator;
    # only the centered arm needs to enter the joint activity row.
    raw_shift = 0.31
    raw_tilted_weights = {
        point: physical_weights[point] * math.exp(-raw_shift) for point in points
    }
    checks.append(
        (
            "fiber_constant_raw_factor_cancels_from_normalized_response",
            math.isclose(
                normalized_average(mark_f, raw_tilted_weights),
                normalized_average(mark_f, physical_weights),
                rel_tol=1.0e-14,
                abs_tol=1.0e-14,
            ),
            "E_(Phi+Lf)[Fo]={:.15f}=E_Phi[Fo]={:.15f}; only Ho enters K_delta".format(
                normalized_average(mark_f, raw_tilted_weights),
                normalized_average(mark_f, physical_weights),
            ),
        )
    )

    def response(source_s: float, source_t: float) -> float:
        partition = sum(
            physical_weights[point]
            * math.exp(-source_s * mark_f[point] - source_t * mark_g[point])
            for point in points
        )
        return -math.log(partition)

    step = 1.0e-4
    mixed_difference = (
        response(step, step)
        - response(step, -step)
        - response(-step, step)
        + response(-step, -step)
    ) / (4.0 * step**2)
    checks.append(
        (
            "mixed_second_derivative_has_no_extra_factor_two",
            math.isclose(mixed_difference, -cov_marks, rel_tol=2.0e-8),
            "d_s d_t[-log Z]={:.12f}, -Cov(Fo,Go)={:.12f}; Taylor diagonal alone carries 1/2".format(
                mixed_difference, -cov_marks
            ),
        )
    )

    # Two combinatorial layers distribute n path steps in n+1 ways on one
    # rooted marked side.  Multiply two full side envelopes for a safe pair
    # bound rather than asserting a sharp two-root enumeration.
    test_tau = 0.23
    cutoff = 30
    distributed_sum = sum(
        test_tau ** (first + second)
        for first in range(cutoff + 1)
        for second in range(cutoff + 1 - first)
    )
    coefficient_sum = sum(
        (order + 1) * test_tau**order for order in range(cutoff + 1)
    )
    closed_pair = 1.0 / (1.0 - test_tau) ** 2
    h_function = test_tau * (2.0 - test_tau) / (1.0 - test_tau) ** 2
    conservative_two_mark = closed_pair**2
    checks.append(
        (
            "conservative_two_mark_two_side_envelope",
            math.isclose(distributed_sum, coefficient_sum, rel_tol=1.0e-14)
            and coefficient_sum <= closed_pair
            and math.isclose(1.0 + h_function, closed_pair, rel_tol=1.0e-14)
            and math.isclose(conservative_two_mark, (1.0 - test_tau) ** -4),
            "one-side truncated={:.15f}, layer distribution={:.15f}, 1+H=(1-t)^-2={:.15f}, two-side safe product=(1-t)^-4={:.15f}".format(
                coefficient_sum, distributed_sum, closed_pair, conservative_two_mark
            ),
        )
    )

    rows = tube_rows()
    with localcontext() as context:
        context.prec = 80
        decimal_delta = Decimal("0.001")
        decimal_c = Decimal("0.01")
        decimal_k_base = Decimal(str(rows["base_K_T"]))
        decimal_k_ball = decimal_k_base + decimal_delta.exp() - Decimal(1)
        decimal_slack = decimal_c - decimal_k_ball
        decimal_candidates = [
            (
                n,
                Decimal(n) * (-decimal_slack * Decimal(n)).exp(),
            )
            for n in (110, 111, 112)
        ]
        decimal_n, decimal_d = max(decimal_candidates, key=lambda row: row[1])
        decimal_tau = decimal_k_ball * decimal_d
        decimal_conversion = Decimal(68) * Decimal("0.1").exp()
        decimal_m = decimal_conversion / (Decimal(1) - decimal_tau) ** 4
        decimal_b = Decimal(str(rows["B"]))
        decimal_q = Decimal("-0.1").exp()
        decimal_lhs = (
            decimal_b
            + decimal_q * decimal_delta
            + decimal_m * decimal_delta**2 / Decimal(2)
        )
    checks.append(
        (
            "independent_high_precision_tube_recomputation",
            decimal_n == 111
            and math.isclose(float(decimal_k_ball), rows["K_ball"], rel_tol=1.0e-15)
            and math.isclose(float(decimal_tau), rows["tau"], rel_tol=1.0e-15)
            and math.isclose(float(decimal_m), rows["M_pair"], rel_tol=1.0e-15)
            and math.isclose(float(decimal_lhs), rows["tube_left"], rel_tol=1.0e-15)
            and decimal_lhs < decimal_delta,
            "Decimal n={}, K_delta={}, tau={}, M={}, lhs={}, margin={}".format(
                decimal_n,
                decimal_k_ball,
                decimal_tau,
                decimal_m,
                decimal_lhs,
                decimal_delta - decimal_lhs,
            ),
        )
    )
    checks.append(
        (
            "uniform_strong_ball_pair_hessian_bound",
            rows["delta"] < rows["source_radius"]
            and rows["K_ball"] < rows["base_allowance"]
            and rows["tau"] < 1.0
            and 88.0 < rows["M_pair"] < 89.0,
            "delta={:.6f}<r_src={:.15f}, K_delta={:.15e}<c, D={:.15f}@n={}, tau_delta={:.15f}, M_delta={:.15f}".format(
                rows["delta"],
                rows["source_radius"],
                rows["K_ball"],
                rows["D"],
                int(rows["n_D"]),
                rows["tau"],
                rows["M_pair"],
            ),
        )
    )
    checks.append(
        (
            "one_horizon_nonlinear_residual_source_output_tube",
            rows["tube_left"] < rows["delta"]
            and rows["tube_margin"] > 1.4e-5,
            "B={:.15e}, q={:.15f}, delta={:.6f}, B+qdelta+(M/2)delta^2={:.15e}<delta, margin={:.15e}".format(
                rows["B"],
                rows["q"],
                rows["delta"],
                rows["tube_left"],
                rows["tube_margin"],
            ),
        )
    )
    checks.append(
        (
            "separate_center_ledger_gap_eta_and_residual_atom_membership",
            rows["gap_ratio"] > 0.9997
            and rows["theta_atom"] > 0.400001
            and rows["K_output_factor"] < rows["base_allowance"],
            "complete center/output charge=delta+tube+B={:.15e}, epsilon_Q={:.15e}, gap/m={:.15f}, sigma_eta={:.15e}, theta_atom={:.15f}, expm1(delta)={:.15e}<c".format(
                rows["complete_output_charge"],
                rows["epsilon_quadratic"],
                rows["gap_ratio"],
                rows["sigma_eta"],
                rows["theta_atom"],
                rows["K_output_factor"],
            ),
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
            phrase_counts == {phrase: int(phrase == "background") for phrase in hidden_phrases},
            f"pre-N3 note plus pre-scan runner counts={phrase_counts}; sole background hit is the declared finite-sector import",
        )
    )
    required = [
        "**Type:** bounded_theorem",
        "D^2R_Phi[F,G]=-Cov_Phi(F,G)",
        "T_res=(1-P_quad)D_(2,1)R",
        "[1+H]^2=(1-tau)^(-4)",
        "K_delta=K_T+expm1(delta)",
        "B+q delta+(M_delta/2)delta^2",
        "source/output Banach-bundle tube",
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
        "proves an autonomous RG ball",
        "proves a physical fixed point",
        "proves a continuum limit",
        "requires a new axiom",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_SCALAR_PRODUCT_REFERENCE_COMPLETED_JOINT_OUTER_HAAR_ACTUAL_OUTPUT_ATOM_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md",
            "WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
