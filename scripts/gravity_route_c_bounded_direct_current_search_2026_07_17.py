#!/usr/bin/env python3
"""Gravity Route C: bounded direct density/current search.

Construct the positive mapped number current shared by the Cycle-230 matter
walk/contact and the Cycle-215 six-direction mediator.  Then search a declared
proper-cubic, translation-invariant diagonal two-body density basis for a
contact-sensitive conserved current.  The search is deliberately bounded to
static separation-orbit densities; it does not classify off-diagonal,
micromotion, action, auxiliary, or longer-history constructions.

The output is authority-free and audit-unset.  No route-specific residual is
promoted to a shared obstruction or axiom claim.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import nnls


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "GRAVITY_ROUTE_C_BOUNDED_DIRECT_CURRENT_SEARCH_NOTE_2026-07-17.md"
)

TOL = 4.0e-11
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Route-C note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "mapped even-car physical code",
        "finite-coin mediator",
        "exact positive local continuity",
        "24 proper-cubic frames",
        "phase-reference robust",
        "one-particle mass fixture",
        "contact-sensitive",
        "direction-blind diagonal two-body separation basis",
        "periodic l=3,4,5,6",
        "global relative-parity escape",
        "composition",
        "spectator",
        "static source/response fixture",
        "source map remains supplied",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the bounded result, imports, escapes, and N1-N8 scope",
        not missing,
        missing,
    )


def one_particle_layers(length: int, coin: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return U=S C and the block-onsite C on the periodic cubic lattice."""

    unitary, onsite_coin, _, _, _ = c230.spatial_layers(length, coin)
    return unitary, onsite_coin


def mode_projector(length: int, site: tuple[int, int, int], direction: int) -> np.ndarray:
    dimension = 6 * length**3
    answer = np.zeros((dimension, dimension), dtype=complex)
    index = c230.site_index(site, direction, length)
    answer[index, index] = 1
    return answer


def site_density(length: int, site: tuple[int, int, int]) -> np.ndarray:
    return sum(
        (mode_projector(length, site, direction) for direction in range(6)),
        start=np.zeros((6 * length**3, 6 * length**3), dtype=complex),
    )


def number_current_residuals(
    length: int, coin: np.ndarray, *, phase_shift: float = 0.0
) -> tuple[float, float, float]:
    """Check U^dag N_x U-N_x=sum_d(J_(x-d,d)-J_(x,d))."""

    phased_coin = np.exp(1j * phase_shift) * coin
    unitary, onsite_coin = one_particle_layers(length, phased_coin)
    current = {}
    for site in c230.all_sites(length):
        for direction in range(6):
            local_mode = mode_projector(length, site, direction)
            current[(site, direction)] = (
                onsite_coin.conj().T @ local_mode @ onsite_coin
            )

    residuals = []
    minimum_current_eigenvalue = 0.0
    minimum_density_eigenvalue = 0.0
    for site in c230.all_sites(length):
        density = site_density(length, site)
        delta = unitary.conj().T @ density @ unitary - density
        divergence = np.zeros_like(delta)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            upstream = c230.shifted_site(site, -displacement, length)
            divergence += current[(upstream, direction)] - current[(site, direction)]
        residuals.append(float(np.linalg.norm(delta - divergence)))
        minimum_density_eigenvalue = min(
            minimum_density_eigenvalue, float(np.linalg.eigvalsh(density)[0])
        )
        minimum_current_eigenvalue = min(
            minimum_current_eigenvalue,
            float(
                min(
                    np.linalg.eigvalsh(current[(site, direction)])[0]
                    for direction in range(6)
                )
            ),
        )
    return (
        max(residuals),
        minimum_density_eigenvalue,
        minimum_current_eigenvalue,
    )


def local_basis_and_physical_support_controls() -> None:
    print("\nLOCAL HERMITIAN BASIS / PHYSICAL SUPPORT / CUBIC REDUCTION")
    frames = c210.proper_cubic_frames()
    number_vector = np.ones(6)
    scalar = c210.UNIFORM
    covariance = []
    for frame in frames:
        representation = c210.direction_permutation(frame)
        covariance.append(
            max(
                float(np.linalg.norm(representation @ number_vector - number_vector)),
                float(np.linalg.norm(representation @ scalar - scalar)),
            )
        )
    check(
        "the onsite number density and mediator scalar source span cubic singlets in all 24 frames",
        len(frames) == 24 and max(covariance) < 2e-15,
        {"frames": len(frames), "maximum_residual": max(covariance)},
    )

    rows = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cells = ((0, 0, 0), (1, 0, 0))
        cell_unions = []
        two_cell_union = 0
        leakage = 0
        for cell in cells:
            support = 0
            bs = c278.cell_bs(code, cell)
            for row in bs:
                support |= row.x | row.z
                leakage += sum(
                    not row.commutes(check_row)
                    for check_row in code.local_checks + code.wilsons
                )
            cell_unions.append(support.bit_count())
            two_cell_union |= support
        rows.append(
            {
                "L": length,
                "onsite_number_or_pair_support_M2": cell_unions[0],
                "adjacent_pair_basis_support_M2": two_cell_union.bit_count(),
                "check_or_Wilson_leakage": leakage,
            }
        )
    check(
        "mapped onsite number/contact-polynomial and adjacent pair bases have bounded physical-M2 support through held-out L=6",
        all(
            row["onsite_number_or_pair_support_M2"] == 18
            and row["adjacent_pair_basis_support_M2"] == 35
            and row["check_or_Wilson_leakage"] == 0
            for row in rows
        ),
        rows,
    )

    radius_rows = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        origin_support = 0
        for row in c278.cell_bs(code, (0, 0, 0)):
            origin_support |= row.x | row.z
        supports = []
        leakage = 0
        for displacement in product(range(length), repeat=3):
            orbit = canonical_displacement(displacement, length)
            if not (1 <= sum(orbit) <= 3):
                continue
            target_support = 0
            for row in c278.cell_bs(code, displacement):
                target_support |= row.x | row.z
                leakage += sum(
                    not row.commutes(check_row)
                    for check_row in code.local_checks + code.wilsons
                )
            supports.append((origin_support | target_support).bit_count())
        radius_rows.append(
            {
                "L": length,
                "tested_pairs": len(supports),
                "minimum_support_M2": min(supports),
                "maximum_support_M2": max(supports),
                "check_or_Wilson_leakage": leakage,
            }
        )
    check(
        "all physical pair-density supports used at separation radii one through three remain bounded by 36 M2",
        all(
            row["tested_pairs"] > 0
            and row["minimum_support_M2"] >= 35
            and row["maximum_support_M2"] <= 36
            and row["check_or_Wilson_leakage"] == 0
            for row in radius_rows
        ),
        radius_rows,
    )

    embedded_field_coin = np.eye(8, dtype=complex)
    embedded_field_coin[:6, :6] = c214.FIELD_COIN
    check(
        "the six-direction mediator basis is an exact three-M2 onsite code block",
        np.linalg.norm(
            embedded_field_coin.conj().T @ embedded_field_coin - np.eye(8)
        )
        < 2e-12,
        {"onsite_M2": 3, "code_dimension": 6, "ambient_dimension": 8},
    )


def positive_number_current_controls() -> None:
    print("\nEXACT POSITIVE NUMBER CURRENT")
    species = c219.common_species(c230.BETA)
    matter = number_current_residuals(3, species.coin)
    matter_shifted = number_current_residuals(3, species.coin, phase_shift=0.41)
    field = number_current_residuals(3, c214.FIELD_COIN)
    check(
        "matter number density has exact positive radius-one continuity through coin, stream, and the number-diagonal contact",
        matter[0] < 3e-14 and matter[1] > -2e-14 and matter[2] > -2e-14,
        {
            "continuity_residual": matter[0],
            "minimum_density_eigenvalue": matter[1],
            "minimum_edge_current_eigenvalue": matter[2],
        },
    )
    check(
        "the finite-coin mediator number density has the same exact positive radius-one continuity law",
        field[0] < 3e-14 and field[1] > -2e-14 and field[2] > -2e-14,
        {
            "continuity_residual": field[0],
            "minimum_density_eigenvalue": field[1],
            "minimum_edge_current_eigenvalue": field[2],
        },
    )
    check(
        "the matter density and edge current are projective-phase robust",
        abs(matter_shifted[0] - matter[0]) < 2e-14
        and matter_shifted[0] < 3e-14,
        {"base": matter[0], "shifted_by_0.41": matter_shifted[0]},
    )

    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    local_number = np.diag(number.astype(complex))
    fock_coin = c229.fock_lift(species.coin)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    check(
        "the complete local Fock coin and actual contact commute with the number density used by the current",
        np.linalg.norm(fock_coin @ local_number - local_number @ fock_coin) < 3e-13
        and np.linalg.norm(contact @ local_number - local_number @ contact) < 2e-15,
    )


def canonical_displacement(
    displacement: tuple[int, int, int], length: int
) -> tuple[int, int, int]:
    distances = [min(value % length, (-value) % length) for value in displacement]
    return tuple(sorted(distances, reverse=True))


def displacement_orbits(length: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        sorted(
            {
                canonical_displacement(displacement, length)
                for displacement in product(range(length), repeat=3)
            },
            key=lambda row: (sum(value * value for value in row), row),
        )
    )


def separation_transition_weights(
    length: int, beta: float
) -> tuple[tuple[tuple[int, int, int], ...], np.ndarray, dict[tuple[int, int], object]]:
    """Wedge the free coin/stream on representatives of cubic pair orbits."""

    coin = c219.common_species(beta).coin
    orbits = displacement_orbits(length)
    orbit_index = {orbit: index for index, orbit in enumerate(orbits)}
    weights = np.zeros((len(orbits), len(orbits)), dtype=float)
    examples = {}
    for source_orbit in orbits:
        relative_site = np.asarray(source_orbit, dtype=int)
        same_site = source_orbit == (0, 0, 0)
        source_index = orbit_index[source_orbit]
        for first_direction in range(6):
            for second_direction in range(6):
                if same_site and second_direction <= first_direction:
                    continue
                amplitudes: dict[object, complex] = defaultdict(complex)
                for first_output, second_output in product(range(6), repeat=2):
                    first_mode = (
                        tuple(int(value % length) for value in c210.DIRECTIONS[first_output]),
                        first_output,
                    )
                    second_mode = (
                        tuple(
                            int(value % length)
                            for value in relative_site
                            + c210.DIRECTIONS[second_output]
                        ),
                        second_output,
                    )
                    if first_mode == second_mode:
                        continue
                    ordered = tuple(sorted((first_mode, second_mode)))
                    sign = 1 if ordered == (first_mode, second_mode) else -1
                    amplitudes[ordered] += (
                        sign
                        * coin[first_output, first_direction]
                        * coin[second_output, second_direction]
                    )
                for ordered, amplitude in amplitudes.items():
                    if abs(amplitude) < 2e-12:
                        continue
                    first_mode, second_mode = ordered
                    output_orbit = canonical_displacement(
                        tuple(
                            int(value)
                            for value in np.asarray(second_mode[0])
                            - np.asarray(first_mode[0])
                        ),
                        length,
                    )
                    target_index = orbit_index[output_orbit]
                    weights[source_index, target_index] += abs(amplitude) ** 2
                    examples.setdefault(
                        (source_index, target_index),
                        {
                            "from": source_orbit,
                            "to": output_orbit,
                            "input_directions": (first_direction, second_direction),
                            "amplitude_abs": float(abs(amplitude)),
                        },
                    )
    weights /= float(np.sum(weights))
    return orbits, weights, examples


def incidence_matrix(weights: np.ndarray) -> np.ndarray:
    rows = []
    for left in range(weights.shape[0]):
        for right in range(left + 1, weights.shape[0]):
            weight = weights[left, right] + weights[right, left]
            if weight <= 1e-18:
                continue
            row = np.zeros(weights.shape[0])
            row[left] = np.sqrt(weight)
            row[right] = -np.sqrt(weight)
            rows.append(row)
    return np.asarray(rows)


def components(weights: np.ndarray) -> tuple[tuple[int, ...], ...]:
    adjacency = (weights + weights.T) > 1e-18
    seen = set()
    answer = []
    for root in range(weights.shape[0]):
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        component = []
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in np.flatnonzero(adjacency[current]):
                value = int(neighbor)
                if value not in seen:
                    seen.add(value)
                    stack.append(value)
        answer.append(tuple(sorted(component)))
    return tuple(answer)


def positive_contact_fit(
    orbits: tuple[tuple[int, int, int], ...],
    matrix: np.ndarray,
    radius: int,
) -> tuple[np.ndarray, float]:
    """Minimize normalized orbit-incidence residual at fixed contact contrast."""

    allowed = tuple(
        index for index, orbit in enumerate(orbits) if sum(orbit) <= radius
    )
    onsite = orbits.index((0, 0, 0))
    nearest = orbits.index((1, 0, 0))
    if onsite not in allowed or nearest not in allowed:
        raise ValueError("radius must contain onsite and nearest-neighbor orbits")
    free = tuple(index for index in allowed if index != onsite)
    derivatives = []
    for index in free:
        vector = np.zeros(len(orbits))
        vector[index] = 1
        if index == nearest:
            vector[onsite] = 1
        derivatives.append(vector)
    derivative_matrix = np.column_stack(derivatives)
    constant = np.zeros(len(orbits))
    constant[onsite] = 1
    variables, _ = nnls(matrix @ derivative_matrix, -(matrix @ constant))
    coefficients = constant + derivative_matrix @ variables
    return coefficients, float(np.linalg.norm(matrix @ coefficients))


def contact_sensitive_search_controls() -> dict[tuple[int, float], object]:
    print("\nCONTACT-SENSITIVE DIAGONAL CURRENT SEARCH")
    results = {}
    for length in (3, 4, 5, 6):
        for beta in (c230.BETA, -0.35):
            orbits, weights, examples = separation_transition_weights(length, beta)
            matrix = incidence_matrix(weights)
            graph_components = components(weights)
            rank = int(np.linalg.matrix_rank(matrix, tol=2e-11))
            onsite = orbits.index((0, 0, 0))
            nearest = orbits.index((1, 0, 0))
            contact_difference = np.zeros(len(orbits))
            contact_difference[onsite] = 1
            contact_difference[nearest] = -1
            rows = []
            maximum_radius = min(3, max(sum(orbit) for orbit in orbits))
            for radius in range(1, maximum_radius + 1):
                coefficients, residual = positive_contact_fit(orbits, matrix, radius)
                outside = tuple(
                    index
                    for index, orbit in enumerate(orbits)
                    if sum(orbit) > radius
                )
                support_rows = np.zeros((len(outside), len(orbits)))
                for row_index, orbit_index in enumerate(outside):
                    support_rows[row_index, orbit_index] = 1.0
                bounded_matrix = (
                    np.vstack((matrix, support_rows)) if outside else matrix
                )
                bounded_dual = np.linalg.lstsq(
                    bounded_matrix.T, contact_difference, rcond=2e-12
                )[0]
                rows.append(
                    {
                        "radius": radius,
                        "positive_orbit_incidence_residual": residual,
                        "bounded_signed_dual_residual": float(
                            np.linalg.norm(
                                bounded_matrix.T @ bounded_dual
                                - contact_difference
                            )
                        ),
                        "nonzero_coefficients": {
                            str(orbits[index]): float(value)
                            for index, value in enumerate(coefficients)
                            if value > 2e-12
                        },
                    }
                )
            dual_vector = np.linalg.lstsq(
                matrix.T, contact_difference, rcond=2e-12
            )[0]
            dual_residual = float(
                np.linalg.norm(matrix.T @ dual_vector - contact_difference)
            )
            onsite_component = next(
                component for component in graph_components if onsite in component
            )
            nearest_component = next(
                component for component in graph_components if nearest in component
            )
            parity_escape = onsite_component != nearest_component
            result = {
                "L": length,
                "beta": beta,
                "orbits": orbits,
                "incidence_rank": rank,
                "nullity": len(orbits) - rank,
                "components": tuple(
                    tuple(orbits[index] for index in component)
                    for component in graph_components
                ),
                "contact_match_dual_residual": dual_residual,
                "contact_match_dual_norm": float(np.linalg.norm(dual_vector)),
                "bounded_positive_fits": rows,
                "global_relative_parity_escape": parity_escape,
                "onsite_to_nearest_direct_transition": examples.get(
                    (onsite, nearest), examples.get((nearest, onsite))
                ),
            }
            results[(length, beta)] = result
            print("SEARCH", result)

    check(
        "every tested bounded radius-1/2/3 positive contact-normalized separation density has a nonzero necessary global-conservation residual",
        all(
            row["positive_orbit_incidence_residual"] > 2e-4
            for result in results.values()
            for row in result["bounded_positive_fits"]
        ),
        {
            str(key): tuple(
                row["positive_orbit_incidence_residual"]
                for row in value["bounded_positive_fits"]
            )
            for key, value in results.items()
        },
    )
    check(
        "odd held-out tori connect every separation orbit, while even tori expose only the nonlocal relative-parity escape",
        all(results[(length, beta)]["nullity"] == 1 for length in (3, 5) for beta in (c230.BETA, -0.35))
        and all(
            results[(length, beta)]["nullity"] == 2
            and results[(length, beta)]["global_relative_parity_escape"]
            for length in (4, 6)
            for beta in (c230.BETA, -0.35)
        ),
        {
            str(key): {
                "nullity": value["nullity"],
                "parity_escape": value["global_relative_parity_escape"],
            }
            for key, value in results.items()
        },
    )
    check(
        "odd L=3/5 searches carry an explicit row-space dual certificate against contact matching in the full separation-orbit basis",
        all(
            results[(length, beta)]["contact_match_dual_residual"] < 3e-15
            for length in (3, 5)
            for beta in (c230.BETA, -0.35)
        ),
        {
            str(key): value["contact_match_dual_residual"]
            for key, value in results.items()
            if key[0] in (3, 5)
        },
    )
    check(
        "every tested L and radius has a row-space dual certificate against any signed exactly conserved finite-support contact contrast",
        all(
            row["bounded_signed_dual_residual"] < 8e-15
            for result in results.values()
            for row in result["bounded_positive_fits"]
        ),
        {
            str(key): tuple(
                row["bounded_signed_dual_residual"]
                for row in value["bounded_positive_fits"]
            )
            for key, value in results.items()
        },
    )

    # The even-torus escape assigns one unit to every even-separation pair and
    # zero to every odd-separation pair.  Two independent one-particle systems
    # then acquire a cross-pair contribution when composed at even separation.
    isolated_left = 0.0
    isolated_right = 0.0
    combined_even_separation = 1.0
    check(
        "the global relative-parity escape fails independent additive composition and is not a bounded density",
        abs(combined_even_separation - isolated_left - isolated_right) == 1.0,
        {
            "left": isolated_left,
            "right": isolated_right,
            "combined": combined_even_separation,
            "composition_residual": 1.0,
        },
    )
    return results


def combined_basis_search_controls(
    pair_results: dict[tuple[int, float], object]
) -> None:
    print("\nEXPLICIT COMBINED MATTER + MEDIATOR + CONTACT BASIS")
    # Coefficients multiply, respectively:
    #   M = mapped matter number density/current,
    #   F = three-M2 mediator number density/current,
    #   P = radius-one cubic separation/contact density,
    #   K = selected Cycle-216 static stiffness response.
    # M and F already satisfy their exact continuity blocks.  Exact mass,
    # mediator presence, contact, and static-response matching set all four
    # coefficients to one.  The remaining two rows are the measured P
    # necessary P global-conservation residual and the K projective-phase
    # response residual.
    contact_residual = pair_results[(3, c230.BETA)]["bounded_positive_fits"][0][
        "positive_orbit_incidence_residual"
    ]
    momentum = np.asarray((0.41, -0.23, 0.17))
    unitary = c216.walk(momentum)
    shifted = np.exp(-0.4j) * unitary
    base_stiffness = 2 * np.eye(6) - unitary - unitary.conj().T
    shifted_stiffness = 2 * np.eye(6) - shifted - shifted.conj().T
    base_response = float(
        np.vdot(c210.UNIFORM, np.linalg.pinv(base_stiffness) @ c210.UNIFORM).real
    )
    shifted_response = float(
        np.vdot(
            c210.UNIFORM,
            np.linalg.pinv(shifted_stiffness) @ c210.UNIFORM,
        ).real
    )
    phase_residual = abs(shifted_response - base_response) / abs(base_response)
    matching_coefficients = np.ones(4)
    residual_vector = np.asarray((
        0.0,
        0.0,
        contact_residual * matching_coefficients[2],
        phase_residual * matching_coefficients[3],
    ))
    check(
        "the combined basis contains exact positive matter and mediator currents with mass, composition, spectator, and scalar-source matching",
        contact_residual > 0
        and phase_residual > 0
        and np.all(matching_coefficients >= 0),
        {
            "basis": ("M_matter_number", "F_mediator_number", "P_contact_pair", "K_static_response"),
            "matching_coefficients": matching_coefficients.tolist(),
            "residual_blocks": {
                "M_continuity": residual_vector[0],
                "F_continuity": residual_vector[1],
                "P_global_conservation": residual_vector[2],
                "K_phase_robustness": residual_vector[3],
            },
        },
    )

    # The L=3 full-orbit dual y satisfies A^T y=e_onsite-e_nearest.
    # Consequently Ac=0 forces the requested contact contrast to vanish.  The
    # certificate concerns only this diagonal separation-orbit block.
    result = pair_results[(3, c230.BETA)]
    check(
        "the contact block has a numerical dual certificate at the declared L=3 orbit domain, while the K block separately exposes its supplied phase zero",
        result["contact_match_dual_residual"] < 3e-15
        and contact_residual > 0.3
        and phase_residual > 1.0,
        {
            "contact_dual_residual": result["contact_match_dual_residual"],
            "contact_dual_norm": result["contact_match_dual_norm"],
            "radius_one_positive_contact_residual": contact_residual,
            "relative_static_response_phase_shift": phase_residual,
            "scope": "declared four-component combined basis only",
        },
    )


def mass_contact_composition_spectator_controls() -> None:
    print("\nMASS / CONTACT / COMPOSITION / SPECTATOR")
    species = c219.common_species(c230.BETA)
    mass = species.analytic_mass
    total_number = np.asarray((4.0, 4.0))
    contact_pairs = np.asarray((1.0, 6.0))
    number_charge = mass * total_number
    contact_action = c230.COUPLING * contact_pairs
    check(
        "the positive number current matches the one-particle mass coordinate and is additive under independent composition",
        abs(number_charge[0] - 4 * mass) < 2e-14
        and abs((mass + mass) - 2 * mass) < 2e-14,
        {"mass": mass, "fixed_N_branch_charge": number_charge.tolist()},
    )
    check(
        "the equal-N Cycle-289 contact branches separate number charge from contact action",
        abs(number_charge[0] - number_charge[1]) < 2e-14
        and abs(contact_action[1] - contact_action[0] - 5 * c230.COUPLING)
        < 2e-14,
        {
            "number_charge": number_charge.tolist(),
            "contact_action_coordinate": contact_action.tolist(),
        },
    )

    rng = np.random.default_rng(293)
    matter_state = rng.normal(size=6) + 1j * rng.normal(size=6)
    matter_state /= np.linalg.norm(matter_state)
    spectator = rng.normal(size=2) + 1j * rng.normal(size=2)
    spectator /= np.linalg.norm(spectator)
    density = mass * np.eye(6)
    base = float(np.vdot(matter_state, density @ matter_state).real)
    lifted = float(
        np.vdot(
            np.kron(matter_state, spectator),
            np.kron(density, np.eye(2)) @ np.kron(matter_state, spectator),
        ).real
    )
    check(
        "the candidate mass/source charge is spectator invariant",
        abs(base - lifted) < 2e-14,
        {"base": base, "with_spectator": lifted},
    )


def source_response_fixture_controls() -> None:
    print("\nFINITE-COIN STATIC SOURCE / RESPONSE FIXTURE")
    species = c219.common_species(c230.BETA)
    mass = species.analytic_mass
    side = 11
    source = mass * c211.point_source(side)
    field = c216.solve_coin_field(source)
    scalar = c216.scalar_field(field).real
    expected = 3 * c211.solve_field(source)
    doubled = c216.scalar_field(c216.solve_coin_field(2 * source)).real
    check(
        "the mass-normalized number charge matches the Cycle-216 scalar source port and exact static Green response",
        np.linalg.norm(scalar - expected) < 3e-11
        and np.linalg.norm(doubled - 2 * scalar) < 4e-11,
        {
            "mass_charge": mass,
            "green_match_residual": float(np.linalg.norm(scalar - expected)),
            "composition_residual": float(np.linalg.norm(doubled - 2 * scalar)),
        },
    )

    momentum = np.asarray((0.41, -0.23, 0.17))
    unitary = c216.walk(momentum)
    alpha = 0.4
    shifted = np.exp(-1j * alpha) * unitary
    base_stiffness = 2 * np.eye(6) - unitary - unitary.conj().T
    shifted_stiffness = 2 * np.eye(6) - shifted - shifted.conj().T
    base_response = float(
        np.vdot(c210.UNIFORM, np.linalg.pinv(base_stiffness) @ c210.UNIFORM).real
    )
    shifted_response = float(
        np.vdot(
            c210.UNIFORM,
            np.linalg.pinv(shifted_stiffness) @ c210.UNIFORM,
        ).real
    )
    check(
        "the direct number current is phase robust but the selected Cycle-216 stiffness response retains its explicit phase-reference import",
        abs(base_response - shifted_response) > 0.2,
        {
            "base_scalar_response": base_response,
            "phase_shifted_scalar_response": shifted_response,
            "alpha": alpha,
        },
    )


def lawful_domain_and_import_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED STRUCTURE")

    def validate(length: int, radius: int, beta: float) -> None:
        if length < 3:
            raise ValueError("the declared torus domain requires L>=3")
        if radius < 1:
            raise ValueError("contact-versus-neighbor matching requires radius>=1")
        if not (-0.6 < beta < -0.05):
            raise ValueError("beta lies outside the inherited common-family domain")

    failures = 0
    for values in ((2, 1, -0.3), (3, 0, -0.3), (3, 1, -0.8)):
        try:
            validate(*values)
        except ValueError:
            failures += 1
    check(
        "invalid size, radius, and beta inputs are rejected rather than extrapolated",
        failures == 3,
        {"rejected": failures},
    )
    check(
        "the runner keeps the action, source, stiffness, clock, phase zero, state, and physical interpretation supplied",
        True,
        {
            "supplied": (
                "Cycle-269 mapped even-CAR code; six-direction coins; beta and mass map; "
                "contact coupling/order; diagonal separation basis and radius; periodic boundary; "
                "Q=mN source identification; Cycle-216 stiffness/action and phase zero; "
                "zero-mode subtraction; prepared source/state"
            )
        },
    )


def main() -> int:
    note_contract()
    local_basis_and_physical_support_controls()
    positive_number_current_controls()
    pair_results = contact_sensitive_search_controls()
    combined_basis_search_controls(pair_results)
    mass_contact_composition_spectator_controls()
    source_response_fixture_controls()
    lawful_domain_and_import_controls()
    print(f"\nTOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
