#!/usr/bin/env python3
"""Checks the external shortest-center, Schur-tail, and Weyl-reference ledger."""

from __future__ import annotations

from collections import deque
from decimal import Decimal, getcontext
import importlib.util
import itertools
import math
from pathlib import Path
import re

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_"
    "PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE_BOUNDED_"
    "THEOREM_NOTE_2026-07-12.md"
)
BLOCK42 = ROOT / "scripts" / (
    "wilson_staggered_enhanced_moment_generated_base_decorated_factor_"
    "return_2026_07_12.py"
)
BLOCK44 = ROOT / "scripts" / (
    "wilson_staggered_site_block_syntactic_support_tree_span_marked_"
    "response_return_2026_07_12.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def center_parameters(mass: float) -> dict[str, float]:
    onsite = mass + 2.0 / mass
    hop = 1.0 / (4.0 * mass)
    shortest_hop = hop * hop / onsite
    shortest_onsite = onsite - 8.0 * hop * hop / onsite
    return {
        "mu": onsite,
        "k": hop,
        "h": 8.0 * hop / onsite,
        "mu_prime": shortest_onsite,
        "k_prime": shortest_hop,
    }


def build_periodic_fixture(side: int, mass: float):
    sites = list(itertools.product(range(side), repeat=4))
    index = {site: position for position, site in enumerate(sites)}
    retained = [
        position
        for position, site in enumerate(sites)
        if all(coordinate % 2 == 0 for coordinate in site)
    ]
    eliminated = [position for position in range(len(sites)) if position not in retained]
    hop = 1.0 / (4.0 * mass)
    hopping = np.zeros((len(sites), len(sites)), dtype=np.float64)
    for site in sites:
        source = index[site]
        for direction in range(4):
            for sign in (-1, 1):
                target_site = list(site)
                target_site[direction] = (target_site[direction] + sign) % side
                hopping[source, index[tuple(target_site)]] = -hop
    return (
        hopping[np.ix_(retained, eliminated)],
        hopping[np.ix_(eliminated, eliminated)],
        hopping[np.ix_(eliminated, retained)],
    )


def graph_distances(adjacency: np.ndarray, source: int) -> list[int | None]:
    distances: list[int | None] = [None] * adjacency.shape[0]
    distances[source] = 0
    queue = deque([source])
    while queue:
        left = queue.popleft()
        for right in np.flatnonzero(adjacency[left]):
            right_int = int(right)
            if distances[right_int] is None:
                distances[right_int] = int(distances[left]) + 1
                queue.append(right_int)
    return distances


def decimal_tail_rows(mass_power: int, theta: str, lam: str) -> dict[str, Decimal]:
    getcontext().prec = 100
    mass = Decimal(10) ** mass_power
    mu = mass + Decimal(2) / mass
    theta_d = Decimal(theta)
    lam_d = Decimal(lam)
    h = Decimal(2) / (mass * mass + Decimal(2))
    b = h * (theta_d + lam_d).exp()
    path_row = (
        Decimal(4)
        / (mass * mass * mu)
        * (Decimal(3) * theta_d + Decimal(2) * lam_d).exp()
        * b
        * b
        / (Decimal(1) - b * b)
    )
    coefficient_row = Decimal(6) * Decimal(3).sqrt() / mass * path_row
    operator_tail = Decimal(4) / (
        mass**3 * (mass * mass + Decimal(2)) * (mass * mass + Decimal(4))
    )
    return {
        "h": h,
        "b": b,
        "path_row": path_row,
        "coefficient_row": coefficient_row,
        "operator_tail": operator_tail,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    # Independent finite-lattice reconstruction.  This does not share the
    # scalar formulas used below and catches parity, sign, and factor errors.
    matrix_mass = 7.0
    params_matrix = center_parameters(matrix_mass)
    r_ki, r_ii, r_ik = build_periodic_fixture(4, matrix_mass)
    boundary_norm_squared = np.linalg.norm(r_ki, 2) ** 2
    odd_sandwich = r_ki @ (r_ii / params_matrix["mu"]) @ r_ik
    a_ii = params_matrix["mu"] * np.eye(r_ii.shape[0]) + r_ii
    inverse = np.linalg.inv(a_ii)
    full_center = (
        params_matrix["mu"] * np.eye(r_ki.shape[0]) - r_ki @ inverse @ r_ik
    )
    shortest_center = (
        params_matrix["mu"] * np.eye(r_ki.shape[0])
        - (r_ki @ r_ik) / params_matrix["mu"]
    )
    tail_matrix = shortest_center - full_center
    tail_norm = np.linalg.norm(tail_matrix, 2)
    tail_bound = (
        4.0
        / matrix_mass**3
        / (matrix_mass**2 + 2.0)
        / (matrix_mass**2 + 4.0)
    )
    full_gap = float(np.linalg.eigvalsh(full_center)[0])
    shortest_gap = float(np.linalg.eigvalsh(shortest_center)[0])
    full_gap_bound = params_matrix["mu"] - 1.0 / matrix_mass**3
    shortest_gap_exact = (
        params_matrix["mu"]
        - 1.0 / (matrix_mass**2 * params_matrix["mu"])
    )
    checks.append(
        (
            "finite_lattice_boundary_norm_and_bipartite_parity",
            math.isclose(boundary_norm_squared, 1.0 / matrix_mass**2, rel_tol=1e-12)
            and np.linalg.norm(odd_sandwich, 2) < 1e-14,
            "||R_KI||^2={:.15e}=1/m^2; ||R_KI(R_II/mu)R_IK||={:.3e}".format(
                boundary_norm_squared, np.linalg.norm(odd_sandwich, 2)
            ),
        )
    )
    checks.append(
        (
            "finite_lattice_length_four_tail_bound",
            tail_norm <= tail_bound * (1.0 + 1e-12)
            and np.linalg.eigvalsh(tail_matrix)[0] >= -1e-14,
            "E_>=4 PSD lower={:.3e}; ||E_>=4||={:.15e} <= {:.15e}".format(
                np.linalg.eigvalsh(tail_matrix)[0], tail_norm, tail_bound
            ),
        )
    )
    checks.append(
        (
            "finite_lattice_full_and_shortest_gap_checks",
            full_gap >= full_gap_bound - 1e-12
            and math.isclose(shortest_gap, shortest_gap_exact, rel_tol=1e-12),
            "gap full={:.15f}>={:.15f}; gap shortest={:.15f}={:.15f}".format(
                full_gap, full_gap_bound, shortest_gap, shortest_gap_exact
            ),
        )
    )

    distances = graph_distances(r_ii, 0)
    pointwise_ratios = []
    h_matrix = params_matrix["h"]
    for target, distance in enumerate(distances):
        if distance is None or distance > 4:
            continue
        bound = (
            params_matrix["mu"] ** -1
            * h_matrix**distance
            / (1.0 - h_matrix**2)
        )
        pointwise_ratios.append(abs(inverse[0, target]) / bound)
    checks.append(
        (
            "pointwise_internal_resolvent_locality",
            pointwise_ratios and max(pointwise_ratios) <= 1.0 + 1e-10,
            "max_(d_I<=4) |A_2^-1(u,v)|/[mu^-1 h^d/(1-h^2)]={:.15f}".format(
                max(pointwise_ratios)
            ),
        )
    )

    # The projective coefficient l1 norm gives incidence constant one.
    trial = np.array(
        [
            [0.07 + 0.03j, -0.04 + 0.08j, 0.02 - 0.01j],
            [0.05 - 0.02j, -0.09 + 0.01j, 0.03 + 0.06j],
            [-0.01 + 0.04j, 0.02 + 0.03j, 0.11 - 0.02j],
        ],
        dtype=np.complex128,
    )
    hermitian = 0.5 * (trial + trial.conjugate().T)
    coefficient_l1 = float(np.sum(np.abs(trial)))
    hermitian_l1 = float(np.sum(np.abs(hermitian)))
    checks.append(
        (
            "quadratic_projector_coefficient_to_operator_incidence_one",
            np.linalg.norm(hermitian, 2) <= hermitian_l1 + 1e-14
            and hermitian_l1 <= coefficient_l1 + 1e-14,
            "||Herm Q||op={:.15e} <= |Herm Q|_1={:.15e} <= |Q|_1={:.15e}".format(
                np.linalg.norm(hermitian, 2), hermitian_l1, coefficient_l1
            ),
        )
    )

    tail_fixture = {-1: 1.7, 1: 2.3}
    tail_empty = 0.5 * (tail_fixture[-1] + tail_fixture[1])
    tail_centered = {
        hidden: value - tail_empty for hidden, value in tail_fixture.items()
    }
    checks.append(
        (
            "tail_hidden_empty_and_centered_ownership_split",
            tail_empty != 0.0
            and max(abs(value) for value in tail_centered.values()) > 0.0
            and all(
                math.isclose(tail_empty + tail_centered[hidden], value)
                for hidden, value in tail_fixture.items()
            )
            and abs(tail_empty) <= max(abs(value) for value in tail_fixture.values())
            and max(abs(value) for value in tail_centered.values())
            <= 2.0 * max(abs(value) for value in tail_fixture.values()),
            "E_hid E={:.15f}, Q_hid E={}, exact reconstruction; empty<=B and centered<=2B".format(
                tail_empty, tail_centered
            ),
        )
    )

    block42 = load_module("block42", BLOCK42)
    block44 = load_module("block44", BLOCK44)
    mass = 1.0e46
    atom_cost = 3.0 + 2.0 * math.sqrt(2.0)
    theta_decorated = 0.400001
    theta_ordinary = theta_decorated + 5.0 * math.log(atom_cost)
    rows42 = block42.enhanced_rows(
        mass=mass,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=theta_decorated,
        decorated_lambda=1.0,
    )
    activity44 = math.exp(-0.2) * rows42["K_decorated_bound"]
    rows44 = block44.attachment_rows(activity44, 0.1, 0.2)

    # The preintegration local jet and the later ordinary output are distinct
    # accounts.  Spatial size weights convert their anchored rows to onsite
    # coefficient rows before the Weyl estimate.
    epsilon_pre = math.exp(-theta_ordinary) * rows42["B_star"]
    theta_weak = 0.0000005
    epsilon_output = math.exp(-theta_weak) * rows44["B_weak"]
    tail_rows = decimal_tail_rows(46, "0.200001", "0.2")
    epsilon_total = epsilon_pre + epsilon_output
    checks.append(
        (
            "actual_local_jet_and_conditional_trial_rows_are_separate",
            epsilon_pre < 1e-9
            and 0.07 < epsilon_output < 0.071
            and rows44["K_weak"] < 0.1,
            "actual epsilon_P0={:.15e}, conditional epsilon_44={:.15e}, K_weak44={:.15e}".format(
                epsilon_pre, epsilon_output, rows44["K_weak"]
            ),
        )
    )

    deep_params = center_parameters(mass)
    shortest_gap_ratio = (
        deep_params["mu"]
        - 16.0 * deep_params["k"] ** 2 / deep_params["mu"]
    ) / mass
    updated_gap_ratio = shortest_gap_ratio - epsilon_total
    chart_transition = 3.0 * math.log(1.0 / updated_gap_ratio)
    actual_base_gap_ratio = shortest_gap_ratio - epsilon_pre
    checks.append(
        (
            "actual_p0_base_center_gap",
            actual_base_gap_ratio > 0.999999999
            and tail_rows["operator_tail"] / (Decimal(10) ** 46)
            < Decimal("1e-367"),
            "gap(S_base)/m>={:.15f}; hidden-empty tail/m has log10={:.12f}".format(
                actual_base_gap_ratio,
                (tail_rows["operator_tail"] / (Decimal(10) ** 46)).log10(),
            ),
        )
    )
    checks.append(
        (
            "conditional_projected_quadratic_weyl_reserve",
            0.929 < updated_gap_ratio < 0.930
            and theta_weak < chart_transition < theta_decorated,
            "conditional epsilon_Q={:.15e}; gap_trial/m={:.15f}; theta_w={:.7f}<three-pair chart charge={:.15f}<theta_d={:.6f}".format(
                epsilon_total,
                updated_gap_ratio,
                theta_weak,
                chart_transition,
                theta_decorated,
            ),
        )
    )

    checks.append(
        (
            "bipartite_weighted_haar_tail_is_residual_owned_and_tiny",
            tail_rows["b"] < Decimal(1)
            and tail_rows["operator_tail"] > Decimal(0)
            and tail_rows["coefficient_row"] > Decimal(0)
            and tail_rows["operator_tail"].log10() < Decimal(-321)
            and tail_rows["coefficient_row"].log10() < Decimal(-364),
            "b={:.6E}, log10 operator-tail={:.12f}, log10 weighted-coefficient-tail={:.12f}".format(
                tail_rows["b"],
                tail_rows["operator_tail"].log10(),
                tail_rows["coefficient_row"].log10(),
            ),
        )
    )

    # Fresh fixed-external-background third-horizon reference.  The onsite
    # quadratic is absorbed into positive site blocks, so only the shortest
    # nearest-neighbor bond is paid here.
    gap = mass * updated_gap_ratio
    eta_squared = 1.0 / gap
    k_prime = deep_params["k_prime"]
    h3 = 8.0 * k_prime / gap
    theta_reference = 0.200001
    lambda_reference = 0.2
    nu3 = 18.0 * atom_cost**3 * eta_squared * k_prime
    boundary_activity = (
        8.0
        * math.exp(2.0 * theta_reference + lambda_reference)
        * math.expm1(nu3)
    )
    checks.append(
        (
            "fresh_shortest_center_bond_reference_activity",
            h3 < 1e-184
            and 0.0 < boundary_activity < 1e-179,
            "h3={:.15e}, nu3={:.15e}, K_B3={:.15e}".format(
                h3, nu3, boundary_activity
            ),
        )
    )

    getcontext().prec = 100
    h3_decimal = Decimal(str(h3))
    atom_decimal = Decimal(str(atom_cost))
    total_weight = Decimal(str(theta_reference + lambda_reference))
    determinant_ratio = atom_decimal * h3_decimal * total_weight.exp()
    # g(x)=(exp(x)-1)/x is at most 2 here (indeed x << 1).  The extra
    # factor two makes this an outward upper bound rather than replacing
    # g(x) by its limiting value one.
    determinant_bound = (
        Decimal(3)
        * determinant_ratio**2
        / (Decimal(1) - determinant_ratio**2)
    )
    checks.append(
        (
            "fresh_reference_determinant_loop_convergence",
            determinant_ratio < Decimal(1)
            and determinant_bound > Decimal(0)
            and determinant_bound.log10() < Decimal(-366),
            "C_*h3 exp(L3)={:.6E}, log10 K_D3^bd={:.12f}".format(
                determinant_ratio, determinant_bound.log10()
            ),
        )
    )

    # A finite positive block fixture checks the exact normalized product
    # reference and determinant phase order without sharing the path bound.
    onsite_left = np.diag([2.3, 2.6, 2.9]).astype(np.complex128)
    onsite_right = np.diag([2.1, 2.5, 3.0]).astype(np.complex128)
    link = np.diag(
        [
            np.exp(0.2j),
            np.exp(-0.35j),
            np.exp(0.15j),
        ]
    )
    fixture_hop = 0.04
    off_diagonal = -fixture_hop * link
    full = np.block(
        [
            [onsite_left, off_diagonal],
            [off_diagonal.conjugate().T, onsite_right],
        ]
    )
    product = np.block(
        [
            [onsite_left, np.zeros((3, 3), dtype=np.complex128)],
            [np.zeros((3, 3), dtype=np.complex128), onsite_right],
        ]
    )
    relative = np.linalg.solve(product, full - product)
    determinant_product = np.linalg.det(product)
    determinant_full = np.linalg.det(full)
    determinant_ratio_direct = determinant_full / determinant_product
    determinant_ratio_log = np.exp(np.linalg.slogdet(np.eye(6) + relative)[1])
    checks.append(
        (
            "finite_positive_correlated_reference_normalization",
            np.linalg.eigvalsh(full)[0] > 2.0
            and determinant_product.real > 0.0
            and determinant_ratio_direct.real > 0.0
            and abs(determinant_ratio_direct.imag) < 1e-14
            and math.isclose(
                determinant_ratio_direct.real,
                determinant_ratio_log,
                rel_tol=1e-13,
            ),
            "gap={:.15f}, det(A3)/det(M3)={:.15f}>0, exp(logdet)={:.15f}".format(
                np.linalg.eigvalsh(full)[0],
                determinant_ratio_direct.real,
                determinant_ratio_log,
            )
            + "; det(M3)={:.15f}, det(M3)*Z3={:.15f}=det(A3)={:.15f}".format(
                determinant_product.real,
                (determinant_product * determinant_ratio_direct).real,
                determinant_full.real,
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "S_base=S_next^(2)+delta Q_P0^sa",
        "S_trial=S_base+delta Q_trial^sa",
        "E_(>=4)",
        "P_(0,2)^sa",
        "V_3(W):=det M_3(W)>0",
        "C_3D_3(1)=1",
        "old `C_2,D_2,J_2` ledger is consumed",
        "fixed external gauge background",
        "NG45:",
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
            "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
