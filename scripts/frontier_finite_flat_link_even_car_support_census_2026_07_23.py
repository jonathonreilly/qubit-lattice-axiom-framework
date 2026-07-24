#!/usr/bin/env python3
"""Finite certificate for a flat-link even-CAR support census.

Paired note:
    docs/FINITE_FLAT_LINK_EVEN_CAR_SUPPORT_CENSUS_BOUNDED_THEOREM_NOTE_2026-07-23.md

The complete computation is partitioned across this primary and two ordinary
helper modules so every source remains byte-complete in the restricted audit
packet.  It is a bounded support/census certificate, not a representation
theorem, autonomous update law, or physical-site compiler.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.linalg import schur

from frontier_finite_flat_link_even_car_support_census_graph_2026_07_23 import (
    DIRECTIONS,
    FRAMES,
    REVERSE_MODE,
    graph_link_code,
)
from frontier_finite_flat_link_even_car_support_census_factors_2026_07_23 import (
    BETA,
    CONTACT_COUPLING,
    TOL,
    common_coin,
    covariance_controls,
    factor_presentation,
    local_factor_controls,
    onsite_even_car_controls,
    polynomial_controls,
    three_mode_gate_controls,
)


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    "scripts/frontier_finite_flat_link_even_car_support_census_graph_2026_07_23.py",
    "scripts/frontier_finite_flat_link_even_car_support_census_factors_2026_07_23.py",
)
LENGTHS = (3, 6, 7)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def walk_symbol(momentum: np.ndarray) -> np.ndarray:
    coin, _mass = common_coin()
    stream = np.diag(np.exp(-1j * (DIRECTIONS @ np.asarray(momentum, dtype=float))))
    return stream @ coin


def circular_distance(phases: np.ndarray, target: float) -> np.ndarray:
    return np.abs(np.angle(np.exp(1j * (phases - target))))


def band_subspace(
    momentum: np.ndarray,
    target_phase: float | None = None,
    target_value: complex | None = None,
    dimension: int | None = None,
    tolerance: float = 1e-7,
):
    triangular, vectors = schur(walk_symbol(momentum), output="complex")
    values = np.diag(triangular)
    phases = np.angle(values)
    if target_phase is not None:
        indices = np.where(circular_distance(phases, target_phase) < tolerance)[0]
    elif target_value is not None and dimension is not None:
        indices = np.argsort(np.abs(values - target_value))[:dimension]
    else:
        raise ValueError("supply target_phase or target_value and dimension")
    return phases[indices], vectors[:, indices]


def internal_wedge(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    amplitude = np.outer(first, second) - np.outer(second, first)
    return amplitude[np.triu_indices(6, 1)]


def contact_form_factor(particle_first, particle_second, hole_first, hole_second):
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for first_hole in range(hole_first.shape[1]):
        for second_hole in range(hole_second.shape[1]):
            hole_wedge = internal_wedge(hole_first[:, first_hole], hole_second[:, second_hole])
            source = first_hole * hole_second.shape[1] + second_hole
            for first_particle in range(particle_first.shape[1]):
                for second_particle in range(particle_second.shape[1]):
                    particle_wedge = internal_wedge(
                        particle_first[:, first_particle], particle_second[:, second_particle]
                    )
                    target = first_particle * particle_second.shape[1] + second_particle
                    result[target, source] = np.vdot(particle_wedge, hole_wedge)
    return result


def bloch_subspace(momentum: np.ndarray, internal: np.ndarray, length: int) -> np.ndarray:
    coordinates = np.asarray(tuple(product(range(length), repeat=3)), dtype=float)
    envelope = np.exp(1j * (coordinates @ momentum)) / np.sqrt(length**3)
    return np.vstack(
        tuple((envelope[:, None] * internal[:, band][None, :]).reshape(-1) for band in range(internal.shape[1]))
    ).T


def direct_spatial_contact_block(particle_first, particle_second, hole_first, hole_second, length: int):
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for site_number in range(length**3):
        local = slice(6 * site_number, 6 * (site_number + 1))
        result += contact_form_factor(
            particle_first[local], particle_second[local], hole_first[local], hole_second[local]
        )
    return result


def l3_modular_resonance_controls() -> tuple[dict, np.ndarray]:
    length = 3
    unit = 2 * np.pi / length
    momenta = {
        "h1": unit * np.asarray((0, 1, 0), dtype=float),
        "h2": unit * np.asarray((0, -1, 0), dtype=float),
        "p1": unit * np.asarray((1, 1, 1), dtype=float),
        "p2": unit * np.asarray((-1, -1, -1), dtype=float),
    }
    targets = {
        "h1": -0.148864781941705,
        "h2": -2.9904574355314986,
        "p1": 0.0759239848775555,
        "p2": 3.067939104828828,
    }
    subspaces = {name: band_subspace(momentum, targets[name]) for name, momentum in momenta.items()}
    phases = {name: subspaces[name][0] for name in subspaces}
    vectors = {name: subspaces[name][1] for name in subspaces}
    form = contact_form_factor(vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"])
    singulars = np.linalg.svd(form, compute_uv=False)
    phase_costs = (
        phases["p1"][:, None, None, None]
        + phases["p2"][None, :, None, None]
        - phases["h1"][None, None, :, None]
        - phases["h2"][None, None, None, :]
    )
    phase_residual = float(np.max(np.abs(phase_costs - 2 * np.pi)))

    spatial = {name: bloch_subspace(momenta[name], vectors[name], length) for name in vectors}
    direct = direct_spatial_contact_block(
        spatial["p1"], spatial["p2"], spatial["h1"], spatial["h2"], length
    )
    spatial_reduction_residual = float(np.linalg.norm(direct - form / length**3))

    unbalanced_momentum = momenta["p2"] + unit * np.asarray((1, 0, 0))
    triangular, unbalanced_vectors = schur(walk_symbol(unbalanced_momentum), output="complex")
    unbalanced_phases = np.angle(np.diag(triangular))
    unbalanced_vectors = unbalanced_vectors[:, unbalanced_phases > 1e-9]
    unbalanced_internal = contact_form_factor(
        vectors["p1"], unbalanced_vectors, vectors["h1"], vectors["h2"]
    )
    unbalanced_spatial = bloch_subspace(unbalanced_momentum, unbalanced_vectors, length)
    unbalanced_direct = direct_spatial_contact_block(
        spatial["p1"], unbalanced_spatial, spatial["h1"], spatial["h2"], length
    )

    rng = np.random.default_rng(2302)
    gauge_residuals = []
    for _ in range(12):
        rotated = {}
        for name, subspace in vectors.items():
            trial = rng.normal(size=(subspace.shape[1], subspace.shape[1]))
            trial = trial + 1j * rng.normal(size=trial.shape)
            gauge, _r = np.linalg.qr(trial)
            rotated[name] = subspace @ gauge
        rotated_form = contact_form_factor(
            rotated["p1"], rotated["p2"], rotated["h1"], rotated["h2"]
        )
        gauge_residuals.append(
            float(np.linalg.norm(np.linalg.svd(rotated_form, compute_uv=False) - singulars))
        )

    frame_residuals = []
    for frame in FRAMES:
        transformed = {
            name: band_subspace(frame @ momenta[name], targets[name])[1]
            for name in momenta
        }
        transformed_form = contact_form_factor(
            transformed["p1"], transformed["p2"], transformed["h1"], transformed["h2"]
        )
        frame_residuals.append(
            float(np.linalg.norm(np.linalg.svd(transformed_form, compute_uv=False) - singulars))
        )

    rows = {
        "phase_residual_to_2pi": phase_residual,
        "singular_values": tuple(float(value) for value in singulars),
        "form_Frobenius_norm": float(np.linalg.norm(form)),
        "direct_spatial_reduction_residual": spatial_reduction_residual,
        "momentum_balance_residual": float(
            max(
                np.linalg.norm(momenta["h1"] + momenta["h2"]),
                np.linalg.norm(momenta["p1"] + momenta["p2"]),
            )
        ),
        "unbalanced_internal_norm": float(np.linalg.norm(unbalanced_internal)),
        "unbalanced_spatial_norm": float(np.linalg.norm(unbalanced_direct)),
        "maximum_degenerate_basis_residual": max(gauge_residuals),
        "maximum_proper_cubic_singular_value_residual": max(frame_residuals),
        "proper_cubic_frames": len(frame_residuals),
    }
    rows["pass"] = bool(
        phase_residual < 3e-14
        and len(singulars) == 2
        and singulars[-1] > 0.45
        and singulars[0] > 0.49
        and np.linalg.norm(form) > 0.67
        and spatial_reduction_residual < 2e-15
        and rows["momentum_balance_residual"] < 2e-15
        and rows["unbalanced_internal_norm"] > 0.1
        and rows["unbalanced_spatial_norm"] < 2e-15
        and max(gauge_residuals) < 3e-15
        and max(frame_residuals) < 2e-13
    )
    return rows, form


def seam_block(lower: float, upper: float, target: complex):
    hole_phase_plus, hole_plus = band_subspace(
        np.full(3, lower), target_value=target, dimension=2
    )
    hole_phase_minus, hole_minus = band_subspace(
        np.full(3, -lower), target_value=target, dimension=2
    )
    particle_phase_plus, particle_plus = band_subspace(
        np.full(3, upper), target_value=target, dimension=2
    )
    particle_phase_minus, particle_minus = band_subspace(
        np.full(3, -upper), target_value=target, dimension=2
    )
    form = contact_form_factor(particle_plus, particle_minus, hole_plus, hole_minus)
    phase_cost = float(
        np.mean(particle_phase_plus)
        + np.mean(particle_phase_minus)
        - np.mean(hole_phase_plus)
        - np.mean(hole_phase_minus)
    )
    return form, phase_cost, {
        "hole_plus": hole_phase_plus,
        "hole_minus": hole_phase_minus,
        "particle_plus": particle_phase_plus,
        "particle_minus": particle_phase_minus,
    }


def finite_volume_seam_controls(form_l3: np.ndarray) -> dict:
    """Reexecute the shrinking-seam fixture retained from historical Cycle 230."""

    minus_root = 1.5783929737448452
    lengths = (18, 34, 78, 416)
    rows = []
    for length in lengths:
        lower_index = int(np.floor(minus_root * length / (2 * np.pi)))
        lower = 2 * np.pi * lower_index / length
        upper = 2 * np.pi * (lower_index + 1) / length
        form, phase_cost, phase_data = seam_block(lower, upper, -1)
        singulars = np.linalg.svd(form, compute_uv=False)
        rows.append(
            {
                "L": length,
                "lower_gap": minus_root - lower,
                "upper_gap": upper - minus_root,
                "phase_cost": phase_cost,
                "wrapped_phase": abs(float(np.angle(np.exp(1j * phase_cost)))),
                "singular_min": float(np.min(singulars)),
                "singular_max": float(np.max(singulars)),
                "frobenius": float(np.linalg.norm(form)),
                "raw_operator_over_g": float(np.max(singulars) / length**3),
                "hole_phase_max": float(
                    max(np.max(phase_data[name]) for name in ("hole_plus", "hole_minus"))
                ),
                "particle_phase_min": float(
                    min(np.min(phase_data[name]) for name in ("particle_plus", "particle_minus"))
                ),
                "maximum_degenerate_spread": float(
                    max(np.ptp(values) for values in phase_data.values())
                ),
            }
        )

    shrinking_pass = bool(
        rows[-1]["wrapped_phase"] < 0.0046
        and rows[-1]["wrapped_phase"] < rows[0]["wrapped_phase"] / 20
        and max(rows[-1]["lower_gap"], rows[-1]["upper_gap"]) < 0.0077
        and all(row["hole_phase_max"] < 0 for row in rows)
        and all(row["particle_phase_min"] > 0 for row in rows)
        and max(row["maximum_degenerate_spread"] for row in rows) < 3e-14
    )
    strength_pass = bool(
        min(row["singular_min"] for row in rows) > 0.97
        and rows[-1]["singular_min"] > 0.9998
        and abs(rows[-1]["singular_max"] - 1) < 2e-4
        and rows[-1]["raw_operator_over_g"] < rows[0]["raw_operator_over_g"] / 1000
    )

    plus_root = 1.563199679844947
    delta = 1e-3
    minus_singulars = np.linalg.svd(
        seam_block(minus_root - delta, minus_root + delta, -1)[0], compute_uv=False
    )
    plus_form, plus_cost, _ = seam_block(plus_root - delta, plus_root + delta, 1)
    plus_singulars = np.linalg.svd(plus_form, compute_uv=False)
    ordinary_crossing_residual = float(np.linalg.norm(minus_singulars - plus_singulars))

    last_length = lengths[-1]
    lower_index = int(np.floor(minus_root * last_length / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / last_length
    upper = 2 * np.pi * (lower_index + 1) / last_length
    reference_singulars = np.linalg.svd(seam_block(lower, upper, -1)[0], compute_uv=False)
    frame_residuals = []
    for frame in FRAMES:
        subspaces = []
        for momentum in (
            np.full(3, upper),
            np.full(3, -upper),
            np.full(3, lower),
            np.full(3, -lower),
        ):
            subspaces.append(
                band_subspace(frame @ momentum, target_value=-1, dimension=2)[1]
            )
        transformed = contact_form_factor(*subspaces)
        frame_residuals.append(
            float(np.linalg.norm(np.linalg.svd(transformed, compute_uv=False) - reference_singulars))
        )

    rng = np.random.default_rng(230)
    source = rng.normal(size=form_l3.shape[1]) + 1j * rng.normal(size=form_l3.shape[1])
    target = rng.normal(size=form_l3.shape[0]) + 1j * rng.normal(size=form_l3.shape[0])
    source /= np.linalg.norm(source)
    target /= np.linalg.norm(target)
    spectator = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    extra = np.asarray((np.sqrt(0.3), np.sqrt(0.7)), dtype=complex)
    base = np.vdot(target, form_l3 @ source)
    one_spectator = np.vdot(
        np.kron(target, spectator),
        np.kron(form_l3, np.eye(2)) @ np.kron(source, spectator),
    )
    two_spectators = np.vdot(
        np.kron(np.kron(target, spectator), extra),
        np.kron(form_l3, np.eye(4)) @ np.kron(np.kron(source, spectator), extra),
    )
    spectator_residual = float(max(abs(base - one_spectator), abs(base - two_spectators)))

    result = {
        "minus_root_selector": minus_root,
        "plus_root_selector": plus_root,
        "sampled_lengths": lengths,
        "rows": rows,
        "shrinking_phase_control_pass": shrinking_pass,
        "reduced_strength_control_pass": strength_pass,
        "ordinary_crossing_singular_residual": ordinary_crossing_residual,
        "ordinary_crossing_phase_cost": plus_cost,
        "maximum_proper_cubic_singular_residual": max(frame_residuals),
        "passive_spectator_residual": spectator_residual,
    }
    result["pass"] = bool(
        shrinking_pass
        and strength_pass
        and ordinary_crossing_residual < 3e-13
        and abs(plus_cost) < 7e-4
        and max(frame_residuals) < 3e-13
        and spectator_residual < 2e-15
    )
    return result


def source_dependency_closure() -> dict:
    module_paths = (
        "scripts/frontier_finite_flat_link_even_car_support_census_2026_07_23.py",
        "scripts/frontier_finite_flat_link_even_car_support_census_graph_2026_07_23.py",
        "scripts/frontier_finite_flat_link_even_car_support_census_factors_2026_07_23.py",
    )
    sources = {
        path: (ROOT / path).read_text(encoding="utf-8") for path in module_paths
    }
    forbidden = (
        "git" + " show",
        "merge" + "-base",
        "sub" + "process",
        "sys" + ".path",
        "docs/work_" + "history",
        "outputs/" + "physical_",
        "cycle" + "653",
        "cycle" + "656",
    )
    observed = {
        fragment: sum(
            source.lower().count(fragment.lower()) for source in sources.values()
        )
        for fragment in forbidden
    }
    imports = {
        path: tuple(
            line.strip()
            for line in source.splitlines()
            if line.startswith("import ") or line.startswith("from ")
        )
        for path, source in sources.items()
    }
    allowed = {
        "from __future__ import annotations",
        "from collections import Counter, defaultdict",
        "from dataclasses import dataclass",
        "from hashlib import sha256",
        "from itertools import combinations, product",
        "from itertools import combinations, permutations, product",
        "from itertools import product",
        "import json",
        "import math",
        "from pathlib import Path",
        "import numpy as np",
        "from scipy.linalg import schur",
        "from frontier_finite_flat_link_even_car_support_census_graph_2026_07_23 import (",
        "from frontier_finite_flat_link_even_car_support_census_factors_2026_07_23 import (",
    }
    unexpected = tuple(
        sorted({line for rows in imports.values() for line in rows} - allowed)
    )
    return {
        "imports": imports,
        "unexpected_imports": unexpected,
        "source_modules": module_paths,
        "source_module_bytes": {
            path: len(source.encode("utf-8")) for path, source in sources.items()
        },
        "source_module_sha256": {
            path: sha256(source.encode("utf-8")).hexdigest()
            for path, source in sources.items()
        },
        "ordinary_helper_imports": AUDIT_INPUT_PATHS,
        "forbidden_reference_counts": observed,
        "pass": not unexpected
        and not any(observed.values())
        and set(AUDIT_INPUT_PATHS) == set(module_paths[1:])
        and all(len(source) < 40_000 for source in sources.values()),
    }


def main() -> int:
    print("finite flat-link even-CAR support-census runner")
    print(f"sizes={LENGTHS} beta={BETA} contact_coupling={CONTACT_COUPLING}")
    result = {}
    try:
        closure = source_dependency_closure()
        check("fresh dependency closure has no campaign modules, receipts, Git objects, or ancestry gates", closure["pass"], closure)

        local, schedule = local_factor_controls()
        check(
            "six-mode coin/reverse/contact factors reconstruct the canonical M64 ordered word with inverse, leakage, deletion, and mass controls",
            local["pass"],
            {
                "word": local["full_M64_ordered_word_reconstruction_residual"],
                "inverse": local["full_M64_explicit_inverse_residual"],
                "mass": local["mass_fixture_residual"],
                "contact_deletion": local["contact_deletion_residual"],
            },
        )
        polynomials = polynomial_controls(schedule)
        check("coin/contact/FSWAP even-CAR polynomials reconstruct with exact sign controls", polynomials["pass"], polynomials)
        three_mode = three_mode_gate_controls(schedule)
        check(
            "three-mode endpoint controls retain helper parity and distinguish the extra-B expression",
            three_mode["pass"],
            three_mode,
        )
        l3_resonance, form_l3 = l3_modular_resonance_controls()
        check(
            "L3 modular resonance fixture is balanced, nonzero, basis-stable, spatially reduced, and all-24 covariant",
            l3_resonance["pass"],
            l3_resonance,
        )
        finite_seam = finite_volume_seam_controls(form_l3)
        check(
            "shrinking finite-volume seam fixture is reexecuted at L18/L34/L78/L416 "
            "(historical Cycle 230 provenance)",
            finite_seam["pass"],
            finite_seam,
        )

        rows = []
        internals = []
        presentations = []
        for length in LENGTHS:
            row, internal = graph_link_code(length)
            rows.append(row)
            internals.append(internal)
            check(
                f"L{length} 25-M2/cell graph/link quotient, local constraints, sectors, deletion, and malformed-domain controls",
                row["pass"],
                {
                    "rank": row["combined_rank"],
                    "quotient": row["matter_quotient_dimension"],
                    "gram": row["matter_quotient_symplectic_rank"],
                    "sector_failures": row["topological_sector_controls"]["all_eight_sector_failures"],
                },
            )
            presentation = factor_presentation(length, internal, schedule)
            presentations.append(presentation)
            check(
                f"L{length} displayed 32N factor census has bounded support and support-disjoint finite coloring",
                presentation["pass"],
                {
                    "factors": presentation["complete_factor_count"],
                    "palette": presentation["finite_color_palette"],
                    "layers": presentation["sequential_color_layers"],
                    "max_weight": presentation["maximum_factor_M2_weight"],
                },
            )

        finite_palette_bound = all(row["finite_color_palette"] <= 7 for row in presentations)
        check(
            "all three finite census sizes use at most seven support colors",
            finite_palette_bound,
            {f"L{row['length']}": row["finite_color_palette"] for row in presentations},
        )
        covariance = covariance_controls(rows, internals)
        check(
            "all 24 proper-cubic frames and all 576 products preserve signed modes, graph generators, links, constraints, and homology",
            covariance["pass"],
            covariance,
        )
        onsite_algebra = onsite_even_car_controls(internals)
        check(
            "all 15 onsite bilinears satisfy the even-CAR incidence algebra and derived all-24 covariance on code",
            onsite_algebra["pass"],
            onsite_algebra,
        )
        fixed_chart_boundary = {
            "executed_sizes": (3,),
            "L3_local_constraint_failures": covariance["size_rows"][0]["combined_local_constraint_span_failures"],
            "L3_correlation_section_failures": covariance["size_rows"][0]["fixed_chart_correlation_span_failures"],
            "fixed_chart_invariant_claimed": False,
            "transported_chart_supplied": True,
        }
        fixed_chart_boundary["pass"] = bool(
            fixed_chart_boundary["L3_local_constraint_failures"] == 0
            and fixed_chart_boundary["L3_correlation_section_failures"] > 0
        )
        check(
            "combined code-space covariance boundary is explicit: local constraints transport, fixed Wilson section does not",
            fixed_chart_boundary["pass"],
            fixed_chart_boundary,
        )

        support_census = {
            "scope": "finite L3, L6, and L7 census fixtures",
            "result": "rank, support, algebra, coloring, and fixture census for the displayed graph/link Pauli data",
            "physical_encoding_E_constructed": False,
            "E_G_intertwiner_test_executed": False,
            "all_displayed_32N_factor_supports_reexecuted": all(row["pass"] for row in presentations),
            "active_algebra_M2_per_cell": 25,
            "runtime_global_Jordan_Wigner_order": False,
            "runtime_nonlocal_parity_service": False,
            "runtime_Wilson_table": False,
            "compile_time_nonlocal_Wilson_section": True,
            "topological_input_chart_supplied": True,
            "autonomous_update_law_claimed": False,
            "physical_site_compiler_claimed": False,
            "pass": all(row["pass"] for row in rows + presentations)
            and local["pass"]
            and polynomials["pass"]
            and three_mode["pass"]
            and l3_resonance["pass"]
            and finite_seam["pass"]
            and covariance["pass"]
            and onsite_algebra["pass"]
            and fixed_chart_boundary["pass"],
        }
        check("bounded finite flat-link even-CAR support census", support_census["pass"], support_census)
        result = {
            "authority": "none",
            "audit": "unset",
            "claim_type": "bounded_theorem",
            "strict_autonomous_physical_law": False,
            "physical_site_compiler_claimed": False,
            "physical_encoding_E_constructed": False,
            "E_G_intertwiner_test_executed": False,
            "dependency_closure": closure,
            "canonical_M64_word": local,
            "even_CAR_polynomials": polynomials,
            "three_mode_helper_parity": three_mode,
            "L3_modular_resonance_fixture": l3_resonance,
            "shrinking_finite_volume_seam_fixture": finite_seam,
            "graph_link_rows": rows,
            "factor_presentations": presentations,
            "covariance": covariance,
            "onsite_even_CAR_algebra": onsite_algebra,
            "combined_code_space_covariance_boundary": fixed_chart_boundary,
            "support_census": support_census,
            "supplied_structure": {
                "runtime_dependencies": (
                    "Python standard library",
                    "NumPy",
                    "SciPy scipy.linalg.schur",
                ),
                "beta_minus_0p3_coin_family": True,
                "contact_coupling_0p37": True,
                "six_mode_direction_order": tuple(
                    tuple(int(value) for value in direction) for direction in DIRECTIONS
                ),
                "reverse_mode_map": REVERSE_MODE,
                "coin_formula": (
                    "C=exp(i*m/3)*(P_scalar-P_even+exp(i*beta)*P_vector), "
                    "m=3*tan(-beta/2)"
                ),
                "coin_projectors": {
                    "uniform_vector": "s=(1,1,1,1,1,1)/sqrt(6)",
                    "P_scalar": "|s><s|",
                    "P_even": "(I+R)/2-P_scalar",
                    "P_vector": "(I-R)/2",
                    "R": "reverse-mode permutation (0 1)(2 3)(4 5)",
                },
                "pauli_convention": (
                    "i^phase X^x Z^z; product phase adds "
                    "2*popcount(z_left & x_right) modulo 4"
                ),
                "periodic_L3_L6_L7_domains": True,
                "rough_puncture_graph_and_one_terminal_per_cell": True,
                "local_incident_edge_order": "ascending construction index",
                "missing_reverse_pair_helper": "first admissible third mode in ascending mode order",
                "flat_link_logical_section_and_three_topological_inputs": True,
                "compile_time_nonlocal_Wilson_correlation_section": True,
                "K129_sparse_placement_scale": True,
                "fine_support_embedding": {
                    "periodic_modulus": "2*K*L",
                    "cell_center": "2*K*cell",
                    "rough_terminal_offset": "0",
                    "puncture_spoke_offset": "8*direction[mode]",
                    "internal_edge_offset": "4*(direction[left]+direction[right])",
                    "outer_edge_offset": "32*direction[source_mode]",
                    "flat_link_midpoint": "cell_center+K*axis_unit_vector",
                },
                "Wilson_chart_convention": {
                    "origin": (0, 0, 0),
                    "axis_loop_steps": "0 through L-1",
                    "transverse_mode_axis": "(axis+1) mod 3",
                },
                "flat_link_chart_convention": {
                    "logical_Z": "axis loop through the coordinate origin",
                    "logical_X": "axis-oriented links on the coordinate-zero plane",
                    "sector_gradient_root": (0, 0, 0),
                    "topological_bit_insertion": "positive-axis periodic wrap link",
                },
                "thirty_stage_group_factor_order": True,
                "color_labels_supplied": False,
                "coloring_convention": (
                    "deterministic greedy first-fit within lexicographically sorted stages; "
                    "factors retain construction and lexicographic cell order"
                ),
                "compile_time_frame_and_chart_transport": True,
                "L3_target_momentum_indices": {
                    "h1": (0, 1, 0),
                    "h2": (0, -1, 0),
                    "p1": (1, 1, 1),
                    "p2": (-1, -1, -1),
                },
                "L3_target_phases": {
                    "h1": -0.148864781941705,
                    "h2": -2.9904574355314986,
                    "p1": 0.0759239848775555,
                    "p2": 3.067939104828828,
                },
                "seam_root_locations": {
                    "minus_one": 1.5783929737448452,
                    "plus_one": 1.563199679844947,
                },
                "finite_seam_lengths": (18, 34, 78, 416),
                "selection_and_numerical_conventions": {
                    "global_residual_tolerance": TOL,
                    "QR_drop_and_phase_cutoff": 1e-13,
                    "polynomial_coefficient_sign_tolerance": 1e-14,
                    "L3_band_phase_tolerance": 1e-7,
                    "unbalanced_positive_phase_cutoff": 1e-9,
                    "seam_eigenvalue_selector": "two nearest eigenvalues to supplied target",
                    "seam_selected_dimension": 2,
                    "seam_root_neighborhood_delta": 1e-3,
                },
                "acceptance_thresholds": {
                    "L3_phase_residual": 3e-14,
                    "L3_singular_minima": (0.49, 0.45),
                    "L3_form_Frobenius_minimum": 0.67,
                    "L3_spatial_and_momentum_residual": 2e-15,
                    "L3_unbalanced_internal_minimum": 0.1,
                    "L3_degenerate_basis_residual": 3e-15,
                    "L3_proper_cubic_residual": 2e-13,
                    "seam_terminal_wrapped_phase": 0.0046,
                    "seam_terminal_gap": 0.0077,
                    "seam_degenerate_spread": 3e-14,
                    "seam_singular_minimum_all_sizes": 0.97,
                    "seam_terminal_singular_minimum": 0.9998,
                    "seam_terminal_singular_maximum_residual": 2e-4,
                    "seam_crossing_and_frame_residual": 3e-13,
                    "seam_plus_phase_cost": 7e-4,
                    "passive_spectator_residual": 2e-15,
                    "extra_helper_B_operator_residual_minimum": 1e-2,
                    "deleted_coin_factor_residual_minimum": 1e-3,
                    "color_palette_maximum": 7,
                    "sequential_layers_maximum": 58,
                    "factor_weight_maximum": 14,
                },
                "deterministic_RNG_seeds": {
                    "degenerate_band_basis": 2302,
                    "passive_spectator": 230,
                },
                "topological_input_bits_supplied": True,
                "physical_M64_to_M2_encoding_E": False,
                "blank_M2_reference_preparation": False,
                "autonomous_controller_clock_work_return": False,
                "reference_or_topological_sector_genesis": False,
            },
            "scope_boundaries": {
                "controller": "the 30-stage-group, at-most-58-layer factor order is supplied",
                "physical_encoding": "no M64-to-graph/link code isometry E is constructed or tested",
                "reference_genesis": "the correlated graph/link section is supplied; no blank preparation is constructed",
                "topological_sector": "three input qubits are lawful and all eight basis sectors are checked, but no local genesis/selection mechanism is supplied",
                "fixed_chart_covariance": "the local constraints transport, but the supplied fixed Wilson correlation section has measured span failures",
                "static_local_alignment": "the logical graph/link alignment is supplied rather than enforced by one commuting all-local static constraint family",
            },
        }
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")
    result["tests_passed"] = PASS
    result["tests_failed"] = FAIL
    result["pass"] = FAIL == 0
    print("RESULT_JSON=" + json.dumps(result, sort_keys=True, default=float))
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
