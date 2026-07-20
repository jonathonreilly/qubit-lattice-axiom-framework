#!/usr/bin/env python3
"""Checks the one-horizon Haar--Berezin Hoeffding lineage cluster lift."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_"
    "LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


def expectation(function: dict[tuple[int, ...], float], axes: set[int]) -> dict[tuple[int, ...], float]:
    dimension = len(next(iter(function)))
    out = {}
    for point in function:
        total = 0.0
        for values in itertools.product((-1, 1), repeat=len(axes)):
            source = list(point)
            for axis, value in zip(sorted(axes), values):
                source[axis] = value
            total += function[tuple(source)]
        out[point] = total / (2 ** len(axes))
    assert all(len(point) == dimension for point in out)
    return out


def subtract(left: dict[tuple[int, ...], float], right: dict[tuple[int, ...], float]) -> dict[tuple[int, ...], float]:
    return {point: left[point] - right[point] for point in left}


def hoeffding_component(
    function: dict[tuple[int, ...], float], tagged: set[int]
) -> dict[tuple[int, ...], float]:
    dimension = len(next(iter(function)))
    component = expectation(function, set(range(dimension)) - tagged)
    for axis in sorted(tagged):
        component = subtract(component, expectation(component, {axis}))
    return component


def add_functions(functions: list[dict[tuple[int, ...], float]]) -> dict[tuple[int, ...], float]:
    points = functions[0]
    return {point: sum(function[point] for function in functions) for point in points}


def multiply(*functions: dict[tuple[int, ...], float]) -> dict[tuple[int, ...], float]:
    return {point: math.prod(function[point] for function in functions) for point in functions[0]}


def sup_norm(function: dict[tuple[int, ...], float]) -> float:
    return max(abs(value) for value in function.values())


def mean(function: dict[tuple[int, ...], float]) -> float:
    return sum(function.values()) / len(function)


def atomize(function: dict[tuple[int, ...], float]) -> dict[tuple[int, ...], dict[tuple[int, ...], float]]:
    dimension = len(next(iter(function)))
    out = {}
    for size in range(dimension + 1):
        for tagged in itertools.combinations(range(dimension), size):
            out[tagged] = hoeffding_component(function, set(tagged))
    return out


def atom_norm(function: dict[tuple[int, ...], float], weight: float) -> float:
    return sum(weight ** len(tagged) * sup_norm(component) for tagged, component in atomize(function).items())


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(((int(n), n * math.exp(-slack * n)) for n in candidates), key=lambda row: row[1])


def integer_sup_attachment(k_value: float, c: float) -> tuple[int, float]:
    critical = -math.log1p(-k_value / c) / k_value
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), math.exp(-c * n) * math.expm1(k_value * n)) for n in candidates),
        key=lambda row: row[1],
    )


def attachment_constants(k_value: float, c: float) -> dict[str, float]:
    n_d, d_slack = integer_sup_n_exp(c - k_value)
    n_a, a_zero = integer_sup_attachment(k_value, c)
    tau = k_value * d_slack
    anchored = (a_zero + tau / (1.0 - tau)) / (1.0 - tau)
    return {
        "n_d": float(n_d),
        "d_slack": d_slack,
        "n_a": float(n_a),
        "a_zero": a_zero,
        "tau": tau,
        "A_att": anchored,
    }


def tagged_rows(
    mass: float, beta: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    r_star = 1.0 + math.sqrt(2.0)
    coordinate_cost = r_star**2
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    wilson = (
        12.0
        * math.expm1((3.0 * beta / 4.0) * coordinate_cost**4)
        * math.exp(4.0 * total_weight)
    )
    determinant = 0.0
    schur = 0.0
    for length in range(4, 10000, 2):
        det_term = (
            1.5
            * coordinate_cost**length
            * h**length
            * g(3.0 * coordinate_cost**length * h**length / length)
            * math.exp(length * total_weight)
        )
        determinant += det_term
        x_length = 9.0 * eta**2 * 2.0 ** (-length) * mass ** (-(length - 1))
        schur_term = (
            18.0
            * eta**2
            * coordinate_cost ** (length + 2)
            * length
            * h ** (length - 1)
            * g(coordinate_cost ** (length + 2) * x_length)
            * math.exp(length * total_weight)
        )
        schur += schur_term
        if max(det_term, schur_term) < 1.0e-22:
            break
    return {
        "C": coordinate_cost,
        "q_hop": h * coordinate_cost * math.exp(total_weight),
        "K_W": wilson,
        "K_I": determinant,
        "K_S": schur,
        "K": wilson + determinant + schur,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []
    r_star = 1.0 + math.sqrt(2.0)
    coordinate_cost = r_star**2
    checks.append(
        (
            "hoeffding_weight_identity",
            math.isclose(coordinate_cost, 1.0 + 2.0 * r_star, abs_tol=1.0e-14)
            and math.isclose(coordinate_cost, 3.0 + 2.0 * math.sqrt(2.0), abs_tol=1.0e-14),
            f"r*={r_star:.15f}, C*=r*^2=1+2r*={coordinate_cost:.15f}",
        )
    )

    points = tuple(itertools.product((-1, 1), repeat=3))
    function = {
        point: 0.7 + 0.2 * point[0] - 0.3 * point[1] + 0.11 * point[0] * point[2]
        for point in points
    }
    atoms = atomize(function)
    reconstructed = add_functions(list(atoms.values()))
    max_error = max(abs(function[point] - reconstructed[point]) for point in points)
    black_box = coordinate_cost**3 * sup_norm(function)
    checks.append(
        (
            "canonical_atom_reconstruction_and_bound",
            max_error < 1.0e-14 and atom_norm(function, r_star) <= black_box + 1.0e-14,
            f"atoms={len(atoms)}, reconstruction_error={max_error:.3e}, atom_norm={atom_norm(function,r_star):.12f}<=black_box={black_box:.12f}",
        )
    )

    dummy_function = {point: 1.0 + 0.25 * point[0] for point in points}
    dummy_atoms = atomize(dummy_function)
    dummy_nonzero = [tagged for tagged, component in dummy_atoms.items() if sup_norm(component) > 1.0e-14]
    checks.append(
        (
            "dummy_coordinate_has_no_tag",
            dummy_nonzero == [(), (0,)],
            f"nonzero_tag_sets={dummy_nonzero}",
        )
    )

    fully_dummy = {point: 0.375 for point in points}
    fully_dummy_nonzero = [
        tagged for tagged, component in atomize(fully_dummy).items() if sup_norm(component) > 1.0e-14
    ]
    checks.append(
        (
            "skeleton_cancellation_has_empty_current_atom",
            fully_dummy_nonzero == [()],
            f"V-only transporter with syntactic A,H carrier has nonzero_tag_sets={fully_dummy_nonzero}",
        )
    )

    centered_x = {point: float(point[0]) for point in points}
    checks.append(
        (
            "centered_tags_do_not_survive_expectation",
            abs(mean(centered_x)) < 1.0e-15 and math.isclose(mean(multiply(centered_x, centered_x)), 1.0),
            f"E[x]={mean(centered_x):.1f}, E[x*x]={mean(multiply(centered_x,centered_x)):.1f}",
        )
    )

    omega = complex(-0.5, math.sqrt(3.0) / 2.0)
    center_moments = [sum(omega ** (power * moment) for power in range(3)) / 3.0 for moment in range(1, 4)]

    # Build the normalized SU(3) alternating tensor rather than stipulating
    # its Haar-projector coefficient.  On the six permutation basis states,
    # P = |epsilon><epsilon| / <epsilon,epsilon>; checking P^2=P makes the
    # selected 1/6 coefficient mutation-sensitive.
    permutations = list(itertools.permutations(range(3)))

    def permutation_sign(permutation):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(3) for right in range(left + 1, 3)
        )
        return -1.0 if inversions % 2 else 1.0

    epsilon = {permutation: permutation_sign(permutation) for permutation in permutations}
    epsilon_norm_sq = sum(value * value for value in epsilon.values())
    projector = {
        (left, right): epsilon[left] * epsilon[right] / epsilon_norm_sq
        for left in permutations for right in permutations
    }
    projector_residual = max(
        abs(
            sum(projector[(left, middle)] * projector[(middle, right)] for middle in permutations)
            - projector[(left, right)]
        )
        for left in permutations for right in permutations
    )
    epsilon_component = projector[((0, 1, 2), (0, 1, 2))]
    center_residual = max(
        abs(center_moments[0]),
        abs(center_moments[1]),
        abs(center_moments[2] - 1.0),
    )
    checks.append(
        (
            "center_charge_allows_cubic_haar_singlet",
            center_residual < 1.0e-15
            and math.isclose(epsilon_norm_sq, 6.0)
            and projector_residual < 1.0e-15
            and math.isclose(epsilon_component, 1.0 / 6.0),
            f"SU3-center max residual={center_residual:.3e}; "
            f"epsilon norm^2={epsilon_norm_sq:.0f}, projector-idempotence residual={projector_residual:.3e}, "
            f"Haar U11 U22 U33 epsilon coefficient={epsilon_component:.12f}",
        )
    )

    factor_one = {point: 0.1 + 0.2 * point[0] - 0.05 * point[1] for point in points}
    factor_two = {
        point: -0.03 + 0.15 * point[0] + 0.07 * point[1] + 0.04 * point[2]
        for point in points
    }
    decorated_sum = 0.0
    decorated_weights = []
    for atom_one, atom_two in itertools.product(atomize(factor_one).values(), atomize(factor_two).values()):
        weight = mean(multiply(atom_one, atom_two))
        decorated_sum += weight
        if abs(weight) > 1.0e-15:
            decorated_weights.append(weight)
    direct_weight = mean(multiply(factor_one, factor_two))
    checks.append(
        (
            "decorated_factor_collection_evaluation",
            math.isclose(decorated_sum, direct_weight, abs_tol=1.0e-14),
            f"decorated_sum={decorated_sum:.15f}, direct_weight={direct_weight:.15f}",
        )
    )

    direct_log_partial = 0.0
    decorated_log_partial = 0.0
    power_errors = []
    for order in range(1, 5):
        direct_power = direct_weight**order
        decorated_power = sum(
            math.prod(choice) for choice in itertools.product(decorated_weights, repeat=order)
        )
        power_errors.append(abs(direct_power - decorated_power))
        coefficient = ((-1) ** (order + 1)) / order
        direct_log_partial += coefficient * direct_power
        decorated_log_partial += coefficient * decorated_power
    checks.append(
        (
            "decorated_hard_core_log_evaluation",
            max(power_errors) < 1.0e-14
            and math.isclose(decorated_log_partial, direct_log_partial, abs_tol=1.0e-14),
            f"nonzero_decorations={len(decorated_weights)}, power_errors={power_errors}, log_partial={decorated_log_partial:.15f}",
        )
    )

    mass, beta, c, theta, lam = 1.0e4, 0.0, 0.001, 1.0e-6, 1.0
    eta = mass**-0.5
    rows = tagged_rows(mass, beta, c, theta, lam, eta)
    checks.append(
        (
            "tagged_residual_activity_point",
            rows["q_hop"] < 0.00636
            and rows["K_I"] < 2.44e-9
            and rows["K_S"] < 9.95e-7
            and rows["K"] < c,
            "q_hop={:.15e}, K_I={:.15e}, K_S={:.15e}, K={:.15e}, margin={:.15e}".format(
                rows["q_hop"], rows["K_I"], rows["K_S"], rows["K"], c - rows["K"]
            ),
        )
    )

    beta_ceiling = (4.0 / 3.0) * math.log1p(
        (c - rows["K_I"] - rows["K_S"])
        / (12.0 * math.exp(4.0 * (theta + 2.0 * c + lam)))
    )
    beta_ceiling /= coordinate_cost**4
    beta_probe = 0.99 * beta_ceiling
    probe_rows = tagged_rows(mass, beta_probe, c, theta, lam, eta)
    checks.append(
        (
            "strict_nonzero_beta_interval",
            1.7e-9 < beta_ceiling < 1.8e-9 and probe_rows["K"] < c,
            f"beta_ceiling={beta_ceiling:.15e}, beta_probe={beta_probe:.15e}, K_probe={probe_rows['K']:.15e}<c",
        )
    )

    attachment = attachment_constants(rows["K"], c)
    conversion = 68.0 * math.exp(lam / 2.0)
    q_centered = conversion * attachment["A_att"]
    q_split = max(math.exp(-lam / 2.0), q_centered)
    base_defect = conversion * rows["K"]
    checks.append(
        (
            "tagged_marked_constants",
            q_centered < 0.083 and q_split < 1.0 and base_defect < 1.12e-4,
            "tau={:.15e}, A_att={:.15e}, q_centered={:.15e}, q_split={:.12f}, B_tag={:.15e}".format(
                attachment["tau"], attachment["A_att"], q_centered, q_split, base_defect
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "ev(Gamma_hat_res)=Gamma_res",
        "one RG horizon only",
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
    forbidden = ["proves an autonomous RG", "tags survive integration", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
