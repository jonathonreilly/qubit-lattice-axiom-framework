#!/usr/bin/env python3
"""Checks the completed scalar-product joint expansion and one atom return."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import re
from decimal import Decimal

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_SCALAR_PRODUCT_REFERENCE_COMPLETED_JOINT_OUTER_HAAR_"
    "ACTUAL_OUTPUT_ATOM_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md"
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
SAFE_HAAR_ROOTS = 68
SAFE_GAUSSIAN_ROOTS = 16
VISIBLE_TAIL_CHARGE = 1.0e-20


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


def center_parameters(mass: float) -> dict[str, float]:
    mu = mass + 2.0 / mass
    hop = 1.0 / (4.0 * mass)
    shortest_hop = hop * hop / mu
    mu_prime = mu - 8.0 * hop * hop / mu
    return {
        "mu": mu,
        "hop": hop,
        "k_prime": shortest_hop,
        "mu_prime": mu_prime,
        "h_short": 8.0 * shortest_hop / mu_prime,
    }


def first_joint_rows() -> dict[str, float]:
    block42 = load_module("block42", BLOCK42)
    block45 = load_module("block45", BLOCK45)
    mass = 1.0e64
    theta = 4.38
    allowance = 0.01
    lam = 0.2
    total_weight = theta + 2.0 * allowance + lam
    rows42 = block42.enhanced_rows(
        mass=mass,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        # Recompute Block42 at the actual joint source weight.  The later
        # fresh-atom target is 0.400001; it is not the source argument here.
        decorated_theta=4.6,
        decorated_lambda=1.0,
    )
    params = center_parameters(mass)
    b_star = rows42["B_star"]
    k_q = math.expm1(b_star)
    k_p0 = math.expm1(b_star)

    # Q insertions destroy the old even-total-word formula.  The factor three
    # safely pays the color trace in an all-length anchored trace-log row.
    x_q = (mass / params["mu_prime"]) * b_star
    x_r = C_STAR * params["h_short"] * math.exp(total_weight)
    x_full = x_q + x_r
    full_determinant_potential = 3.0 * x_full / (1.0 - x_full)
    # Haar expectation is contractive, while (1-E_hid) costs at most two.
    # Both C_o and D_o own the centered determinant potential.
    determinant_potential = 2.0 * full_determinant_potential
    k_d = math.expm1(determinant_potential)

    eta_squared = 1.0 / mass
    reference_bond = (
        8.0
        * math.exp(2.0 * (theta + 2.0 * allowance) + lam)
        * math.expm1(18.0 * C_STAR**3 * eta_squared * params["k_prime"])
    )
    boundary_bond = reference_bond
    k_decorated = rows42["K_decorated_bound"]

    # The hidden-empty tail is outside the normalized graph.  Its centered
    # arm is positive but below binary64 range.  Verify the analytic Decimal
    # row, then charge a visible binary64 number above one ulp of the aggregate
    # activity.  This is a strict outward bound and is not absorbed by K_red.
    tail_rows = block45.decimal_tail_rows(64, "4.4", "0.2")
    centered_tail_decimal = 2 * tail_rows["coefficient_row"]
    if not 0 < centered_tail_decimal < Decimal("1e-499"):
        raise ValueError(f"unexpected centered tail row {centered_tail_decimal}")
    centered_tail = VISIBLE_TAIL_CHARGE
    k_reference = k_q + reference_bond + k_d
    k_red = k_decorated + k_p0 + boundary_bond + k_d + centered_tail
    k_total = k_reference + k_red
    n_d, d_value = integer_sup_n_exp(allowance - k_total)
    tau = k_total * d_value
    attachment = 2.0 * d_value * k_red / (1.0 - tau) ** 3
    conversion = SAFE_HAAR_ROOTS * math.exp(lam / 2.0)
    output_potential = conversion * k_total
    q_centered = conversion * attachment
    q_raw = math.exp(-lam / 2.0)

    theta_weak = theta / 2.0
    lambda_weak = lam / 2.0
    hidden_empty_tail = VISIBLE_TAIL_CHARGE
    # Charge the carried P0 row again in the actual quadratic gap.  This is
    # deliberately more conservative than applying its strong size weight.
    # The separately reattached hidden-empty quadratic tail is also charged.
    epsilon_output = (
        b_star + math.exp(-theta_weak) * output_potential + hidden_empty_tail
    )
    gap_ratio = 1.0 - epsilon_output
    sigma_eta = 3.0 * math.log(1.0 / gap_ratio)
    theta_atom = theta_weak - math.log(C_STAR) - sigma_eta
    # The hidden-empty tail is separately reattached after the normalized
    # ratio.  Charge it visibly in the final physical factor envelope too.
    output_total_potential = output_potential + hidden_empty_tail
    factor_output = math.expm1(output_total_potential)
    return {
        "mass": mass,
        "theta": theta,
        "allowance": allowance,
        "lambda": lam,
        "total_weight": total_weight,
        "B_star": b_star,
        "K_decorated": k_decorated,
        "mu_prime": params["mu_prime"],
        "k_prime": params["k_prime"],
        "h_short": params["h_short"],
        "x_Q": x_q,
        "x_R": x_r,
        "x_full": x_full,
        "B_D_full": full_determinant_potential,
        "B_D": determinant_potential,
        "K_Q": k_q,
        "K_P0": k_p0,
        "K_G": reference_bond,
        "K_J": boundary_bond,
        "K_D_minus": k_d,
        "K_D_plus": k_d,
        "K_tail_centered": centered_tail,
        "log10_B_tail_centered": float(centered_tail_decimal.log10()),
        "K_ref": k_reference,
        "K_R": k_red,
        "K_T": k_total,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "A_joint": attachment,
        "conversion": conversion,
        "B_out": output_potential,
        "B_out_total": output_total_potential,
        "K_tail_empty": hidden_empty_tail,
        "K_out_factor": factor_output,
        "q_centered": q_centered,
        "q_raw": q_raw,
        "q": max(q_centered, q_raw),
        "theta_weak": theta_weak,
        "lambda_weak": lambda_weak,
        "epsilon_output": epsilon_output,
        "gap_ratio": gap_ratio,
        "sigma_eta": sigma_eta,
        "theta_atom": theta_atom,
    }


def next_boundary_rows(output_potential: float) -> dict[str, float]:
    allowance = 0.01
    theta = 0.280001
    lam = 0.1
    k_q = math.expm1(output_potential)
    k_p = k_q
    determinant_potential = 6.0 * output_potential / (1.0 - output_potential)
    k_d = math.expm1(determinant_potential)
    k_reference = k_q + k_d
    k_red = k_p + k_d
    k_total = k_reference + k_red
    n_d, d_value = integer_sup_n_exp(allowance - k_total)
    tau = k_total * d_value
    attachment = 2.0 * d_value * k_red / (1.0 - tau) ** 3
    conversion = SAFE_HAAR_ROOTS * math.exp(lam / 2.0)
    next_output = conversion * k_total
    return {
        "allowance": allowance,
        "theta": theta,
        "lambda": lam,
        "K_Q": k_q,
        "K_P": k_p,
        "B_D": determinant_potential,
        "K_D": k_d,
        "K_ref": k_reference,
        "K_R": k_red,
        "K_T": k_total,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "A_joint": attachment,
        "conversion": conversion,
        "B_out": next_output,
        "K_out_factor": math.expm1(next_output),
        "q_centered": conversion * attachment,
        "q_raw": math.exp(-lam / 2.0),
        "q": max(conversion * attachment, math.exp(-lam / 2.0)),
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    # A finite Hermitian three-color fixture has onsite hidden dependence and
    # offsite hopping.  It independently checks the scalar product reference,
    # the hidden-empty/centered determinant split, and positivity.
    mu_fixture = 3.5
    determinant_values: dict[int, float] = {}
    matrices: dict[int, np.ndarray] = {}
    for hidden in (-1, 1):
        q_matrix = np.diag(
            [0.12 + 0.03 * hidden, -0.08 + 0.02 * hidden, 0.05 - 0.01 * hidden]
        ).astype(np.complex128)
        phase = np.exp(0.2j * hidden)
        r_matrix = np.array(
            [
                [0.0, 0.06 * phase, -0.025j],
                [0.06 * phase.conjugate(), 0.0, 0.04 * phase],
                [0.025j, 0.04 * phase.conjugate(), 0.0],
            ],
            dtype=np.complex128,
        )
        matrix = mu_fixture * np.eye(3) + q_matrix + r_matrix
        matrices[hidden] = matrix
        determinant_values[hidden] = float(
            (np.linalg.det(matrix) / mu_fixture**3).real
        )
    psi = {hidden: math.log(value) for hidden, value in determinant_values.items()}
    psi_empty = 0.5 * (psi[-1] + psi[1])
    psi_centered = {hidden: value - psi_empty for hidden, value in psi.items()}
    normalized_at_zero = {
        hidden: determinant_values[hidden] * math.exp(-psi_centered[hidden])
        for hidden in (-1, 1)
    }
    restore_at_one = {
        hidden: math.exp(-psi_centered[hidden]) * math.exp(psi_centered[hidden])
        for hidden in (-1, 1)
    }
    checks.append(
        (
            "scalar_product_reference_hidden_centering_identity",
            min(np.linalg.eigvalsh(matrix)[0] for matrix in matrices.values()) > 3.2
            and max(normalized_at_zero.values()) - min(normalized_at_zero.values())
            < 1.0e-14
            and max(abs(value - 1.0) for value in restore_at_one.values()) < 1.0e-14,
            "min gap={:.15f}, Z_A C_o={}, C_oD_o(1)={}".format(
                min(np.linalg.eigvalsh(matrix)[0] for matrix in matrices.values()),
                normalized_at_zero,
                restore_at_one,
            ),
        )
    )

    fixture = matrices[1]
    x_matrix = fixture / mu_fixture - np.eye(3)
    full_series = 0.0j
    even_series = 0.0j
    power = np.eye(3, dtype=np.complex128)
    for order in range(1, 201):
        power = power @ x_matrix
        term = ((-1) ** (order + 1)) * np.trace(power) / order
        full_series += term
        if order % 2 == 0:
            even_series += term
    exact_log = float(np.linalg.slogdet(np.eye(3) + x_matrix)[1])
    checks.append(
        (
            "full_all_length_trace_log_not_even_only",
            np.linalg.norm(x_matrix, 2) < 0.08
            and abs(full_series.imag) < 1.0e-14
            and abs(full_series.real - exact_log) < 1.0e-14
            and abs(even_series.real - exact_log) > 1.0e-3
            and abs(np.trace(x_matrix).real) > 1.0e-3
            and abs(np.trace(np.linalg.matrix_power(x_matrix, 3)).real) > 1.0e-6,
            "||X||={:.6f}, logdet={:.15f}, full-series={:.15f}, even-only={:.15f}, TrX={:.6e}, TrX^3={:.6e}".format(
                np.linalg.norm(x_matrix, 2),
                exact_log,
                full_series.real,
                even_series.real,
                np.trace(x_matrix).real,
                np.trace(np.linalg.matrix_power(x_matrix, 3)).real,
            ),
        )
    )

    h_ki = np.array([[0.03, -0.01j, 0.02]], dtype=np.complex128)
    h_ik = h_ki.conjugate().T
    schur_direct = h_ki @ np.linalg.inv(fixture) @ h_ik
    t_value = 2.1
    block_matrix = np.block([[np.array([[t_value]]), h_ki], [h_ik, fixture]])
    determinant_schur = np.linalg.det(fixture) * np.linalg.det(
        np.array([[t_value]]) - schur_direct
    )
    checks.append(
        (
            "color_one_gaussian_determinant_schur_ownership",
            math.isclose(
                np.linalg.det(block_matrix).real,
                determinant_schur.real,
                rel_tol=1.0e-14,
                abs_tol=1.0e-14,
            )
            and abs(np.linalg.det(block_matrix).imag) < 1.0e-14,
            "det(block)={:.15f}, det(A)det(t-H_KI A^-1 H_IK)={:.15f}".format(
                np.linalg.det(block_matrix).real, determinant_schur.real
            ),
        )
    )

    checks.append(
        (
            "mixed_site_block_and_haar_root_incidence",
            SAFE_GAUSSIAN_ROOTS <= SAFE_HAAR_ROOTS,
            "68 K_Haar+16 K_Gauss <= 68(K_Haar+K_Gauss); Gaussian-only roots use 16 owned hidden site blocks",
        )
    )

    rows = first_joint_rows()
    checks.append(
        (
            "centered_schur_tail_is_positive_outward_charged",
            rows["K_tail_centered"] == VISIBLE_TAIL_CHARGE
            and rows["log10_B_tail_centered"] < -499.0
            and VISIBLE_TAIL_CHARGE > math.ulp(rows["K_R"]),
            "analytic log10 centered-tail potential={:.12f}; visible charged K_tail^o={:.17e}>ulp(K_R)".format(
                rows["log10_B_tail_centered"], rows["K_tail_centered"]
            ),
        )
    )
    checks.append(
        (
            "completed_joint_activity_strictly_closes",
            rows["K_T"] < rows["allowance"]
            and rows["tau"] < 1.0
            and rows["q"] < 1.0
            and rows["x_full"] < 1.0,
            "K_ref={:.15e}, K_R={:.15e}, K_T={:.15e}<c, D={:.15e}, tau={:.15e}, A_joint={:.15e}, q_centered={:.15e}, q_raw={:.15e}".format(
                rows["K_ref"],
                rows["K_R"],
                rows["K_T"],
                rows["D"],
                rows["tau"],
                rows["A_joint"],
                rows["q_centered"],
                rows["q_raw"],
            ),
        )
    )
    checks.append(
        (
            "actual_output_projection_gap_and_fresh_atom_return",
            rows["gap_ratio"] > 0.99999
            and rows["theta_atom"] > 0.400001
            and rows["K_out_factor"] < rows["allowance"]
            and rows["K_out_factor"] > math.expm1(rows["B_out"]),
            "B_out={:.15e}, K_tail^empty={:.1e}, K_out,total^fac={:.15e}<c, epsilon_Q={:.15e}, gap/m={:.15f}, sigma_eta={:.15e}, theta_atom={:.15f}>0.400001".format(
                rows["B_out"],
                rows["K_tail_empty"],
                rows["K_out_factor"],
                rows["epsilon_output"],
                rows["gap_ratio"],
                rows["sigma_eta"],
                rows["theta_atom"],
            ),
        )
    )

    next_rows = next_boundary_rows(rows["B_out_total"])
    checks.append(
        (
            "next_same_certificate_fails_response_and_factor_return",
            next_rows["K_T"] < next_rows["allowance"]
            and next_rows["tau"] < 1.0
            and next_rows["q"] > 1.0
            and next_rows["K_out_factor"] > next_rows["allowance"],
            "K_Tnext={:.15e}<c, tau_next={:.15e}, q_next={:.15f}>1, B_next_out={:.15e}, K_next_out^fac={:.15e}>c".format(
                next_rows["K_T"],
                next_rows["tau"],
                next_rows["q"],
                next_rows["B_out"],
                next_rows["K_out_factor"],
            ),
        )
    )

    # The no-go is about literal reuse of one surcharge/halving certificate.
    # It is not a no-go for an RG action or a continuum trajectory.
    a0 = 10.0
    chi = 0.03
    iterate = a0
    first_negative = None
    for horizon in range(1, 200):
        iterate = iterate / 2.0 - chi
        closed = 2.0 ** (-horizon) * (a0 + 2.0 * chi) - 2.0 * chi
        if not math.isclose(iterate, closed, rel_tol=1.0e-13, abs_tol=1.0e-13):
            raise RuntimeError("recurrence closed form mismatch")
        if iterate < 0.0 and first_negative is None:
            first_negative = horizon
    checks.append(
        (
            "unchanged_positive_surcharge_halving_certificate_no_fixed_point",
            -2.0 * chi < 0.0
            and first_negative is not None
            and iterate < 0.0
            and math.exp(-0.2 / 2.0**100) > 0.999999999999,
            "fixed point=-2chi={:.6f}; a0={} first becomes negative at j={}; Lambda_j->0 gives exp(-Lambda_j/2)->1".format(
                -2.0 * chi, a0, first_negative
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
            f"pre-N3 note plus pre-scan runner counts={phrase_counts}; sole background hit is declared fixed-external scope",
        )
    )
    required = [
        "**Type:** bounded_theorem",
        "A_3=mu'I+Q_I(W)+R_(II)(W)",
        "Z_A=G_(mu')[B_QB_R]",
        "psi_empty=E_hid psi",
        "C_oD_o(1)=1",
        "68K_Haar+16K_Gauss<=68K_T",
        "Phi_44^out is not an input",
        "NG46:",
        "a_(j+1)=a_j/2-chi",
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
        "proves an autonomous RG map",
        "proves a physical mass gap",
        "proves Lorentz invariance",
        "requires a new axiom",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
