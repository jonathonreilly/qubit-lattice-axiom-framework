#!/usr/bin/env python3
"""Cycle 385: exact finite physical menu-overlap grade identifiability.

The runner deduplicates the Cycle-381 installed fine/coarse effects and, only
under an explicitly supplied effect-functionality premise, assigns one grade
variable to each equal-effect class.  Menu normalization then becomes a
finite incidence system A g = 1.  Cycle-383 effect/coarse-CP quotients are used
only at their declared levels; same-effect process differences remain visible.

Rank, nullity, positivity bounds, trace-labelled and nontrace finite-table
solutions, exact refinements, bounded Cycle-317 host menus, held/frame
invariance, deletions, malformed domains, and concrete candidate augmenting
menus are tested.  Underdetermination is a bounded diagnostic of this finite
graph, not a no-go, global Born failure, minimum-content claim, or axiom
pressure.  No grade is promoted to probability, actuality, sampling, or
frequency.  Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from itertools import combinations_with_replacement
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MENU_OVERLAP_GRADE_IDENTIFIABILITY_TOURNAMENT_"
    "CYCLE385_NOTE_2026-07-18.md"
)

import physical_born_menu_grade_interface_census_cycle381_2026_07_18 as c381
import physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18 as c383


TOL = 1.2e-10
RANK_TOL = 1.2e-10
I2 = c381.I2
PAULIS = (c381.c317.X, c381.c317.Y, c381.c317.Z)
AUTHORITY = "none"
AUDIT = "unset"
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


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-385 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "explicitly supplied effect-functionality premise",
        "36 menu presentations",
        "55 equal-effect classes",
        "rank 20",
        "nullity 35",
        "14 connected components",
        "strictly positive nontrace finite-table witness",
        "perturbation stability",
        "not representable by any single qubit density matrix",
        "fine-only rank is 15",
        "host merge reduces the original-class freedom by one",
        "13 exact candidate augmenting menus",
        "7 independent constraints",
        "not physically registered by this cycle",
        "not in the pinned main base at construction",
        "future landing",
        "bounded diagnostic only",
        "no no-go, global born failure, minimum-content claim, or axiom pressure",
        "no probability, actuality, sampler, or frequency promotion",
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate disposition: fail for any negative claim",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the finite system, premise boundary, witnesses, augmentations, provenance, and semantic firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


@dataclass(frozen=True)
class MenuPresentation:
    name: str
    carrier: str
    program_index: int
    surface: str
    provenance: str
    effects: tuple[np.ndarray, ...]


@dataclass(frozen=True)
class EffectSystem:
    menus: tuple[MenuPresentation, ...]
    effects: tuple[np.ndarray, ...]
    menu_classes: tuple[tuple[int, ...], ...]
    occurrences: tuple[tuple[str, ...], ...]
    incidence: np.ndarray
    maximum_class_residual: float


def validate_menu(menu: MenuPresentation) -> None:
    if not isinstance(menu, MenuPresentation) or not menu.effects:
        raise ValueError("menu must contain at least one declared effect")
    total = np.zeros((2, 2), dtype=complex)
    for effect in menu.effects:
        array = np.asarray(effect, dtype=complex)
        if array.shape != (2, 2) or not np.all(np.isfinite(array)):
            raise ValueError("effect is outside the finite qubit matrix domain")
        if np.linalg.norm(array - array.conj().T) >= TOL:
            raise ValueError("effect is not Hermitian")
        eigenvalues = np.linalg.eigvalsh(array)
        if eigenvalues[0] < -TOL or eigenvalues[-1] > 1 + TOL:
            raise ValueError("effect is outside the positive unit interval")
        total += array
    if np.linalg.norm(total - I2) >= TOL:
        raise ValueError("menu effects do not sum to identity")


def build_effect_system(
    menus: tuple[MenuPresentation, ...],
    *,
    effect_functionality_premise: bool,
) -> EffectSystem:
    if not effect_functionality_premise:
        raise ValueError("equal-effect deduplication requires the supplied effect-functionality premise")
    if not menus:
        raise ValueError("the finite menu family is empty")
    key_to_class: dict[c383.MatrixKey, int] = {}
    effects: list[np.ndarray] = []
    members: list[list[np.ndarray]] = []
    occurrences: list[list[str]] = []
    menu_classes = []
    for menu in menus:
        validate_menu(menu)
        classes = []
        for outcome, effect in enumerate(menu.effects):
            key = c383.matrix_key(effect)
            if key not in key_to_class:
                key_to_class[key] = len(effects)
                effects.append(np.asarray(effect, dtype=complex))
                members.append([])
                occurrences.append([])
            index = key_to_class[key]
            if np.linalg.norm(effect - effects[index]) >= TOL:
                raise ValueError("matrix-key collision exceeds the equality tolerance")
            members[index].append(np.asarray(effect, dtype=complex))
            occurrences[index].append(f"{menu.name}/outcome={outcome}")
            classes.append(index)
        menu_classes.append(tuple(classes))
    incidence = np.zeros((len(menus), len(effects)), dtype=float)
    for row, classes in enumerate(menu_classes):
        for index in classes:
            incidence[row, index] += 1
    maximum_residual = max(
        float(np.linalg.norm(member - effects[index]))
        for index, group in enumerate(members)
        for member in group
    )
    return EffectSystem(
        menus,
        tuple(effects),
        tuple(menu_classes),
        tuple(tuple(items) for items in occurrences),
        incidence,
        maximum_residual,
    )


def installed_menus(
    fixtures: dict[int, c381.c317.PhysicalFixture],
) -> tuple[
    tuple[MenuPresentation, ...],
    dict[str, c381.c323.FixedProgramCarrier],
    dict[str, tuple[c381.c349.MenuSchema, ...]],
]:
    carriers, tables = c381.installed_carriers(fixtures[3].contact)
    rows = []
    for carrier_name, carrier in carriers.items():
        provenance = (
            "landed-in-pinned-main-base Cycle321/323 carrier"
            if carrier_name == "cycle321-canonical"
            else "campaign Cycle349 carrier unlanded at census construction"
        )
        for program_index, program in enumerate(carrier.programs):
            for surface, effects in (
                ("fine", program.fine_effects),
                ("coarse", program.coarse_effects),
            ):
                rows.append(MenuPresentation(
                    name=(
                        f"{carrier_name}/{program_index}/{program.name}/{surface}"
                    ),
                    carrier=carrier_name,
                    program_index=program_index,
                    surface=surface,
                    provenance=provenance,
                    effects=tuple(effects),
                ))
    return tuple(rows), carriers, tables


def matrix_rank(matrix: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=RANK_TOL))


def connected_component_sizes(system: EffectSystem) -> tuple[int, ...]:
    adjacency = [set() for _ in system.effects]
    for classes in system.menu_classes:
        for index in classes:
            adjacency[index].update(classes)
    seen: set[int] = set()
    sizes = []
    for start in range(len(adjacency)):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        size = 0
        while stack:
            current = stack.pop()
            size += 1
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def positive_bounds(
    incidence: np.ndarray,
    variable_indices: tuple[int, ...] | None = None,
) -> tuple[tuple[float, float], ...]:
    count = incidence.shape[1]
    indices = variable_indices or tuple(range(count))
    bounds = []
    for index in indices:
        objective = np.zeros(count)
        objective[index] = 1
        lower = linprog(
            objective,
            A_eq=incidence,
            b_eq=np.ones(incidence.shape[0]),
            bounds=(0, None),
            method="highs",
        )
        upper = linprog(
            -objective,
            A_eq=incidence,
            b_eq=np.ones(incidence.shape[0]),
            bounds=(0, None),
            method="highs",
        )
        if not lower.success or not upper.success:
            raise RuntimeError("positive grade polytope linear program failed")
        bounds.append((float(lower.fun), float(-upper.fun)))
    return tuple(bounds)


def identifiability_controls(system: EffectSystem) -> dict[str, object]:
    incidence = system.incidence
    rank = matrix_rank(incidence)
    nullity = incidence.shape[1] - rank
    singular_values = np.linalg.svd(incidence, compute_uv=False)
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in system.effects
    ])
    trace_residual = float(np.linalg.norm(incidence @ trace_grade - 1))

    perturbation_pair = next(
        (left, right)
        for left in range(len(system.effects))
        for right in range(left + 1, len(system.effects))
        if np.array_equal(incidence[:, left], incidence[:, right])
        and trace_grade[left] > 0
        and trace_grade[right] > 0
    )
    left, right = perturbation_pair
    epsilon = min(trace_grade[left], trace_grade[right]) / 2
    nontrace = trace_grade.copy()
    nontrace[left] += epsilon
    nontrace[right] -= epsilon
    nontrace_residual = float(np.linalg.norm(incidence @ nontrace - 1))
    stability_radius = min(trace_grade[left], trace_grade[right])
    stability_rows = []
    for fraction in (-0.9, -0.5, -0.1, 0.1, 0.5, 0.9):
        candidate = trace_grade.copy()
        delta = fraction * stability_radius
        candidate[left] += delta
        candidate[right] -= delta
        stability_rows.append({
            "fraction": fraction,
            "minimum": float(np.min(candidate)),
            "normalization_residual": float(np.linalg.norm(
                incidence @ candidate - 1
            )),
        })

    bloch_matrix = np.asarray([
        [float(np.trace(effect @ sigma).real / 2) for sigma in PAULIS]
        for effect in system.effects
    ])
    fitted_bloch, *_ = np.linalg.lstsq(
        bloch_matrix, nontrace - trace_grade, rcond=None
    )
    density_fit_residual = float(np.linalg.norm(
        bloch_matrix @ fitted_bloch - (nontrace - trace_grade)
    ))

    bounds = positive_bounds(incidence)
    fixed = tuple(
        index for index, (lower, upper) in enumerate(bounds)
        if abs(upper - lower) < TOL
    )
    zero_reachable = sum(abs(lower) < TOL for lower, _ in bounds)
    width_one = sum(abs((upper - lower) - 1) < TOL for lower, upper in bounds)
    components = connected_component_sizes(system)
    detail = {
        "menu_presentations": incidence.shape[0],
        "effect_occurrences": sum(len(menu.effects) for menu in system.menus),
        "equal_effect_classes": incidence.shape[1],
        "effect_functionality_identifications": (
            sum(len(menu.effects) for menu in system.menus) - incidence.shape[1]
        ),
        "matrix_rank": rank,
        "nullity": nullity,
        "unique_incidence_rows": len(np.unique(incidence, axis=0)),
        "connected_components": len(components),
        "component_sizes": components,
        "minimum_nonzero_singular_value": float(singular_values[rank - 1]),
        "maximum_null_singular_value": float(singular_values[rank]),
        "maximum_equal_effect_class_residual": system.maximum_class_residual,
        "trace_label_minimum": float(np.min(trace_grade)),
        "trace_label_maximum": float(np.max(trace_grade)),
        "trace_normalization_residual": trace_residual,
        "nontrace_perturbation_classes": perturbation_pair,
        "nontrace_perturbation_epsilon": float(epsilon),
        "nontrace_minimum": float(np.min(nontrace)),
        "nontrace_normalization_residual": nontrace_residual,
        "nontrace_distance_from_trace": float(np.linalg.norm(nontrace - trace_grade)),
        "positive_perturbation_open_radius": float(stability_radius),
        "signed_perturbation_stability_rows": tuple(stability_rows),
        "minimum_stability_grid_grade": min(row["minimum"] for row in stability_rows),
        "maximum_stability_grid_residual": max(
            row["normalization_residual"] for row in stability_rows
        ),
        "best_single_density_matrix_fit_residual": density_fit_residual,
        "positive_bound_fixed_classes": fixed,
        "positive_bound_zero_reachable_classes": zero_reachable,
        "positive_bound_width_one_classes": width_one,
        "positive_bound_maximum_width": max(upper - lower for lower, upper in bounds),
        "effect_functionality_premise_supplied": True,
        "finite_table_solution_selected_by_framework": False,
    }
    check(
        "the exact finite overlap system has 55 effect classes, rank 20, nullity 35, and a strictly positive nontrace normalized witness",
        incidence.shape == (36, 55)
        and detail["effect_occurrences"] == 117
        and rank == 20
        and nullity == 35
        and detail["unique_incidence_rows"] == 20
        and detail["connected_components"] == 14
        and components == (8, 6, 5, 5, 5, 4, 4, 4, 4, 3, 2, 2, 2, 1)
        and detail["minimum_nonzero_singular_value"] > 1.19
        and detail["maximum_null_singular_value"] < TOL
        and system.maximum_class_residual < TOL
        and trace_residual < TOL
        and detail["trace_label_minimum"] > 0.05
        and detail["nontrace_minimum"] > 0.05
        and nontrace_residual < TOL
        and detail["nontrace_distance_from_trace"] > 0.13
        and detail["positive_perturbation_open_radius"] > 0.19
        and len(stability_rows) == 6
        and detail["minimum_stability_grid_grade"] > 0.019
        and detail["maximum_stability_grid_residual"] < TOL
        and density_fit_residual > 0.13
        and len(fixed) == 3
        and zero_reachable == 52
        and width_one == 50
        and detail["positive_bound_maximum_width"] > 0.99
        and detail["effect_functionality_premise_supplied"]
        and not detail["finite_table_solution_selected_by_framework"],
        detail,
    )
    return {**detail, "trace_grade": trace_grade, "nontrace_grade": nontrace, "bounds": bounds}


def quotient_and_refinement_controls(system: EffectSystem) -> dict[str, object]:
    with redirect_stdout(StringIO()):
        ray = c383.ray_quotient_section_controls()
        axis = c383.effect_functionality_and_axis_separator_controls()
    fine_rows = tuple(
        index for index, menu in enumerate(system.menus) if menu.surface == "fine"
    )
    coarse_rows = tuple(
        index for index, menu in enumerate(system.menus) if menu.surface == "coarse"
    )
    fine_rank = matrix_rank(system.incidence[np.asarray(fine_rows)])
    coarse_rank = matrix_rank(system.incidence[np.asarray(coarse_rows)])
    difference_rows = []
    for program in range(18):
        difference = system.incidence[2 * program] - system.incidence[2 * program + 1]
        if np.linalg.norm(difference) >= TOL:
            difference_rows.append(difference)
    difference_rank = matrix_rank(np.asarray(difference_rows))
    full_rank = matrix_rank(system.incidence)
    detail = {
        "ray_coarse_CP_quotient_equal": ray["coarse_common_states_equal"],
        "ray_coarse_effect_residual": ray["coarse_effect_residual"],
        "ray_coarse_CP_residual": ray["coarse_CP_Choi_residual"],
        "axis_effect_quotient_equal": axis["axis_effect_quotient_equal"],
        "axis_coarse_CP_quotient_equal": axis["axis_coarse_CP_quotient_equal"],
        "axis_coarse_CP_residual": axis["axis_coarse_CP_Choi_residual"],
        "fine_only_rank": fine_rank,
        "coarse_only_rank": coarse_rank,
        "fine_plus_coarse_rank": full_rank,
        "coarse_presentation_rank_gain_over_fine_only": full_rank - fine_rank,
        "nonzero_fine_minus_coarse_rows": len(difference_rows),
        "fine_minus_coarse_difference_rank": difference_rank,
        "effect_functionality_and_quotient_level_are_supplied": True,
        "same_effect_means_same_process": False,
        "refinement_identity_is_probability_or_actuality": False,
    }
    check(
        "lawful Cycle-383 effect/coarse-CP quotients and exact refinements add five finite constraints without erasing process separators",
        detail["ray_coarse_CP_quotient_equal"]
        and detail["ray_coarse_effect_residual"] < TOL
        and detail["ray_coarse_CP_residual"] < TOL
        and detail["axis_effect_quotient_equal"]
        and not detail["axis_coarse_CP_quotient_equal"]
        and detail["axis_coarse_CP_residual"] > 0.4
        and fine_rank == 15
        and coarse_rank == 12
        and full_rank == 20
        and detail["coarse_presentation_rank_gain_over_fine_only"] == 5
        and len(difference_rows) == 9
        and difference_rank == 8
        and detail["effect_functionality_and_quotient_level_are_supplied"]
        and not detail["same_effect_means_same_process"]
        and not detail["refinement_identity_is_probability_or_actuality"],
        detail,
    )
    return detail


def host_instantiated_menus(
    fixture: c381.c317.PhysicalFixture,
) -> tuple[MenuPresentation, ...]:
    rows = []
    for index, (eigenvalues, direction) in enumerate((
        ((0.83, 0.21), (2, 1, -3)),
        ((0.91, 0.64), (-1, 4, 2)),
        ((0.47, 0.02), (3, -2, 5)),
    )):
        vector = np.asarray(direction, dtype=float)
        vector /= np.linalg.norm(vector)
        high, low = eigenvalues
        projector = c381.c317.projector_bloch(vector)
        kraus = (
            sqrt(low) * fixture.contact,
            sqrt(high - low) * projector @ fixture.contact,
            sqrt(high - low) * (I2 - projector) @ fixture.contact,
            sqrt(1 - high) * fixture.contact,
        )
        program = c381.c321.Program(
            f"Cycle317 host mixed binary {index}", kraus, ((0, 1), (2, 3))
        )
        rows.append(MenuPresentation(
            program.name,
            "Cycle317-host-compiler",
            index,
            "coarse",
            "landed bounded compiler; coefficients/direction host supplied",
            tuple(program.coarse_effects),
        ))

    direction = np.asarray((1, 2, 3), dtype=float)
    direction /= np.linalg.norm(direction)
    coefficient = 2 / (1 + float(np.sum(abs(direction))))
    components = [(coefficient / 2, c381.c317.projector_bloch(direction))]
    for axis in range(3):
        unit = np.zeros(3)
        unit[axis] = -np.sign(direction[axis])
        components.append((
            coefficient * abs(direction[axis]) / 2,
            c381.c317.projector_bloch(unit),
        ))
    isometry, groups = c381.c317.merge_isometry(tuple(components), fixture.contact)
    effects = c381.c317.derived_effects(isometry, groups)
    rows.append(MenuPresentation(
        "Cycle317 host four-component axis merge",
        "Cycle317-host-compiler",
        3,
        "coarse",
        "landed bounded compiler; components/grouping host supplied",
        tuple(effects),
    ))
    return tuple(rows)


def host_augmentation_controls(
    base: EffectSystem,
    fixture: c381.c317.PhysicalFixture,
    base_bounds: tuple[tuple[float, float], ...],
) -> dict[str, object]:
    host = host_instantiated_menus(fixture)
    augmented = build_effect_system(
        base.menus + host, effect_functionality_premise=True
    )
    merge_only = build_effect_system(
        base.menus + (host[-1],), effect_functionality_premise=True
    )
    augmented_rank = matrix_rank(augmented.incidence)
    singular_values = np.linalg.svd(augmented.incidence, full_matrices=True)
    rank = int(np.sum(singular_values[1] > RANK_TOL))
    kernel = singular_values[2][rank:].conj().T
    projected_old_freedom = matrix_rank(kernel[:len(base.effects)])
    augmented_bounds = positive_bounds(
        augmented.incidence, tuple(range(len(base.effects)))
    )
    tightened = sum(
        new_upper < old_upper - TOL or new_lower > old_lower + TOL
        for (old_lower, old_upper), (new_lower, new_upper)
        in zip(base_bounds, augmented_bounds)
    )
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in augmented.effects
    ])
    detail = {
        "host_menus": len(host),
        "host_binary_menus": 3,
        "host_merge_menus": 1,
        "augmented_menu_presentations": len(augmented.menus),
        "augmented_effect_classes": len(augmented.effects),
        "new_effect_classes": len(augmented.effects) - len(base.effects),
        "augmented_rank": augmented_rank,
        "augmented_nullity": len(augmented.effects) - augmented_rank,
        "rank_gain": augmented_rank - matrix_rank(base.incidence),
        "merge_only_rank_gain": matrix_rank(merge_only.incidence) - matrix_rank(base.incidence),
        "base_old_class_freedom": len(base.effects) - matrix_rank(base.incidence),
        "projected_old_class_freedom_after_all_host_menus": projected_old_freedom,
        "tightened_old_class_positive_bounds": tightened,
        "trace_normalization_residual": float(np.linalg.norm(
            augmented.incidence @ trace_grade - 1
        )),
        "host_coefficients_directions_and_invocation_supplied": True,
        "host_menu_is_autonomously_registered": False,
    }
    check(
        "bounded Cycle-317 host menus add four equations and six classes; the exact host merge reduces original-class freedom by one",
        len(host) == 4
        and augmented.incidence.shape == (40, 61)
        and augmented_rank == 24
        and detail["augmented_nullity"] == 37
        and detail["rank_gain"] == 4
        and detail["merge_only_rank_gain"] == 1
        and detail["base_old_class_freedom"] == 35
        and projected_old_freedom == 34
        and tightened == 8
        and detail["trace_normalization_residual"] < TOL
        and detail["host_coefficients_directions_and_invocation_supplied"]
        and not detail["host_menu_is_autonomously_registered"],
        detail,
    )
    return detail


def candidate_augmenting_menu_controls(system: EffectSystem) -> dict[str, object]:
    base_rank = matrix_rank(system.incidence)
    existing_rows = {tuple(row) for row in system.incidence}
    candidates = []
    for outcomes in (2, 3, 4):
        for classes in combinations_with_replacement(range(len(system.effects)), outcomes):
            total = sum(
                (system.effects[index] for index in classes),
                start=np.zeros((2, 2), dtype=complex),
            )
            residual = float(np.linalg.norm(total - I2))
            if residual >= TOL:
                continue
            row = np.zeros(len(system.effects))
            for index in classes:
                row[index] += 1
            if tuple(row) in existing_rows:
                continue
            if matrix_rank(np.vstack((system.incidence, row))) == base_rank:
                continue
            candidates.append((classes, row, residual))

    running = system.incidence.copy()
    running_rank = base_rank
    selected = []
    for classes, row, residual in candidates:
        new_rank = matrix_rank(np.vstack((running, row)))
        if new_rank > running_rank:
            selected.append((classes, row, residual))
            running = np.vstack((running, row))
            running_rank = new_rank

    rows = tuple({
        "classes": classes,
        "sources": tuple(system.occurrences[index][0] for index in classes),
        "sum_to_I_residual": residual,
    } for classes, _row, residual in selected)
    all_rank = matrix_rank(np.vstack((
        system.incidence,
        *(row for _classes, row, _residual in candidates),
    )))
    detail = {
        "searched_outcome_range": (2, 3, 4),
        "exact_candidate_augmenting_menus": len(candidates),
        "greedy_independent_candidate_menus": len(selected),
        "rank_after_all_candidates": all_rank,
        "nullity_after_all_candidates": len(system.effects) - all_rank,
        "maximum_candidate_sum_to_I_residual": max(
            residual for _classes, _row, residual in candidates
        ),
        "independent_candidate_rows": rows,
        "candidate_effects_already_enumerated": True,
        "candidate_menus_physically_registered_by_this_cycle": False,
        "candidate_menu_eligibility_law": None,
    }
    check(
        "thirteen exact unregistered candidate menus made from enumerated effects would add seven independent overlap constraints",
        len(candidates) == 13
        and len(selected) == 7
        and all_rank == 27
        and detail["nullity_after_all_candidates"] == 28
        and detail["maximum_candidate_sum_to_I_residual"] < TOL
        and detail["candidate_effects_already_enumerated"]
        and not detail["candidate_menus_physically_registered_by_this_cycle"]
        and detail["candidate_menu_eligibility_law"] is None,
        detail,
    )
    return detail


def rotate_effect(effect: np.ndarray, frame: np.ndarray) -> np.ndarray:
    scalar = float(np.trace(effect).real / 2)
    bloch = np.asarray([
        float(np.trace(effect @ sigma).real / 2) for sigma in PAULIS
    ])
    rotated = frame @ bloch
    return scalar * I2 + sum(
        (rotated[index] * sigma for index, sigma in enumerate(PAULIS)),
        start=np.zeros((2, 2), dtype=complex),
    )


def frame_and_held_controls(
    system: EffectSystem,
    fixtures: dict[int, c381.c317.PhysicalFixture],
    carriers: dict[str, c381.c323.FixedProgramCarrier],
    tables: dict[str, tuple[c381.c349.MenuSchema, ...]],
) -> dict[str, object]:
    frames = c381.c317.c311.c235.proper_cubic_frames()
    failures = 0
    maximum_completeness_residual = 0.0
    maximum_trace_delta = 0.0
    base_trace = np.asarray([
        float(np.trace(effect).real / 2) for effect in system.effects
    ])
    for frame in frames:
        rotated_menus = tuple(MenuPresentation(
            menu.name,
            menu.carrier,
            menu.program_index,
            menu.surface,
            menu.provenance,
            tuple(rotate_effect(effect, frame) for effect in menu.effects),
        ) for menu in system.menus)
        rotated = build_effect_system(
            rotated_menus, effect_functionality_premise=True
        )
        rotated_trace = np.asarray([
            float(np.trace(effect).real / 2) for effect in rotated.effects
        ])
        failures += int(
            rotated.incidence.shape != system.incidence.shape
            or not np.array_equal(rotated.incidence, system.incidence)
            or matrix_rank(rotated.incidence) != matrix_rank(system.incidence)
        )
        maximum_trace_delta = max(
            maximum_trace_delta,
            float(np.max(abs(rotated_trace - base_trace))),
        )
        maximum_completeness_residual = max(
            maximum_completeness_residual,
            max(float(np.linalg.norm(sum(
                menu.effects, start=np.zeros((2, 2), dtype=complex)
            ) - I2)) for menu in rotated_menus),
        )
    with redirect_stdout(StringIO()):
        inherited = c381.carrier_frame_and_held_controls(fixtures, carriers, tables)
        quotient_carrier = c383.fixed_carrier_controls()
    held_leakage = max(
        row["held_L6_support"]["one_and_two_use_leakage"]
        for row in inherited["carrier_rows"]
    )
    detail = {
        "proper_cubic_frames": len(frames),
        "incidence_or_rank_frame_failures": failures,
        "maximum_rotated_completeness_residual": maximum_completeness_residual,
        "maximum_trace_label_frame_delta": maximum_trace_delta,
        "inherited_carrier_frame_failures": sum(
            row["frame_branch_failures"] for row in inherited["carrier_rows"]
        ),
        "maximum_held_L6_leakage": held_leakage,
        "canonical_held_N": inherited["canonical_Cycle350_held_N"],
        "scaled_held_N": inherited["scaled_Cycle349_held_N"],
        "Cycle383_fixed_carrier_frames": quotient_carrier["proper_cubic_frames"],
        "Cycle383_fixed_carrier_frame_failures": quotient_carrier[
            "carrier_branch_failures"
        ],
        "Cycle383_ray_two_use_coarse_CP_residual": quotient_carrier[
            "ray_two_use_coarse_CP_residual"
        ],
        "grade_system_depends_on_corpus_multiplicity": False,
    }
    check(
        "the finite overlap incidence and lawful quotient are invariant in all 24 frames and retained held L6 N12 controls",
        len(frames) == 24
        and failures == 0
        and maximum_completeness_residual < TOL
        and maximum_trace_delta < TOL
        and detail["inherited_carrier_frame_failures"] == 0
        and held_leakage < TOL
        and detail["canonical_held_N"] == 12
        and detail["scaled_held_N"] == 12
        and detail["Cycle383_fixed_carrier_frames"] == 24
        and detail["Cycle383_fixed_carrier_frame_failures"] == 0
        and detail["Cycle383_ray_two_use_coarse_CP_residual"] < TOL
        and not detail["grade_system_depends_on_corpus_multiplicity"],
        detail,
    )
    return detail


def deletion_and_domain_controls(system: EffectSystem) -> dict[str, object]:
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in system.effects
    ])
    branch_defects = []
    for menu, classes in zip(system.menus, system.menu_classes):
        deleted = classes[:-1]
        branch_defects.append(abs(sum(trace_grade[index] for index in deleted) - 1))
    full_rank = matrix_rank(system.incidence)
    deletion_ranks = tuple(
        matrix_rank(np.delete(system.incidence, row, axis=0))
        for row in range(system.incidence.shape[0])
    )

    template = system.menus[0]
    invalid = (
        lambda: build_effect_system((), effect_functionality_premise=True),
        lambda: build_effect_system(system.menus, effect_functionality_premise=False),
        lambda: validate_menu(MenuPresentation(
            "empty", "invalid", 0, "fine", "invalid", ()
        )),
        lambda: validate_menu(MenuPresentation(
            "non-Hermitian", "invalid", 0, "fine", "invalid",
            (np.asarray([[1, 1], [0, 0]], dtype=complex),),
        )),
        lambda: validate_menu(MenuPresentation(
            "negative", "invalid", 0, "fine", "invalid",
            (-0.1 * I2, 1.1 * I2),
        )),
        lambda: validate_menu(MenuPresentation(
            "wrong shape", "invalid", 0, "fine", "invalid",
            (np.eye(3),),
        )),
        lambda: validate_menu(MenuPresentation(
            "nan", "invalid", 0, "fine", "invalid",
            (np.asarray([[np.nan, 0], [0, 1]], dtype=complex),),
        )),
        lambda: validate_menu(MenuPresentation(
            "incomplete", template.carrier, template.program_index,
            template.surface, template.provenance, template.effects[:-1],
        )),
    )
    rejections = 0
    for attack in invalid:
        try:
            attack()
        except (TypeError, ValueError):
            rejections += 1
    detail = {
        "fine_branch_deletions": len(branch_defects),
        "minimum_deleted_branch_grade_defect": min(branch_defects),
        "rank_essential_menu_equations": sum(rank < full_rank for rank in deletion_ranks),
        "redundant_menu_equations": sum(rank == full_rank for rank in deletion_ranks),
        "minimum_rank_after_single_equation_deletion": min(deletion_ranks),
        "domain_rejections": rejections,
        "domain_attempts": len(invalid),
        "effect_functionality_premise_deletion_rejects": True,
    }
    check(
        "branch/equation deletions remain visible and malformed effect, menu, and functionality domains reject",
        len(branch_defects) == 36
        and min(branch_defects) > 0.05
        and detail["rank_essential_menu_equations"] == 9
        and detail["redundant_menu_equations"] == 27
        and detail["minimum_rank_after_single_equation_deletion"] == 19
        and rejections == len(invalid) == 8
        and detail["effect_functionality_premise_deletion_rejects"],
        detail,
    )
    return detail


def provenance_and_semantic_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        lineage = c381.campaign_lineage_status_controls()
    cycle381_path = ROOT / "scripts/physical_born_menu_grade_interface_census_cycle381_2026_07_18.py"
    cycle383_path = ROOT / "scripts/physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18.py"
    detail = {
        "landed_in_pinned_main_base": (
            "Cycle317 bounded physical menu compiler",
            "Cycle321 effect/coarse-CP programs",
            "Cycle323 fixed physical carrier",
        ),
        "campaign_commit_unlanded_at_census_construction": lineage["campaign_corpus_commit"],
        "pinned_main_base_commit": lineage["pinned_main_base_commit"],
        "campaign_commit_is_pinned_main_base_ancestor": lineage[
            "campaign_commit_is_pinned_main_base_ancestor"
        ],
        "Cycle381_and_Cycle383_are_campaign_inputs_at_Cycle385_construction": True,
        "Cycle381_source_exists": cycle381_path.exists(),
        "Cycle383_source_exists": cycle383_path.exists(),
        "future_landing_allowed": lineage["future_landing_allowed"],
        "effect_functionality_premise": "supplied finite-table identification",
        "menu_normalization_equations": "supplied for enumerated physical presentations",
        "global_effect_domain_registered": False,
        "universal_menu_eligibility": False,
        "selected_numerical_grade": None,
        "probability_interpretation": None,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "frequency_theorem": None,
        "bounded_diagnostic_only": True,
        "N1_N8_negative_claim_gate": "FAIL; live constructive routes remain",
        "negative_claim_shipped": False,
        "no_go": None,
        "global_Born_failure": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "status-split provenance and every supplied grade/menu premise are explicit without semantic or constitutional promotion",
        not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["Cycle381_and_Cycle383_are_campaign_inputs_at_Cycle385_construction"]
        and detail["Cycle381_source_exists"]
        and detail["Cycle383_source_exists"]
        and detail["future_landing_allowed"]
        and not detail["global_effect_domain_registered"]
        and not detail["universal_menu_eligibility"]
        and detail["selected_numerical_grade"] is None
        and detail["probability_interpretation"] is None
        and detail["actual_history_sampler"] is None
        and detail["actual_member_selector"] is None
        and detail["frequency_theorem"] is None
        and detail["bounded_diagnostic_only"]
        and detail["N1_N8_negative_claim_gate"].startswith("FAIL")
        and not detail["negative_claim_shipped"]
        and detail["no_go"] is detail["global_Born_failure"] is None
        and detail["minimum_content_claim"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 385: PHYSICAL MENU-OVERLAP GRADE IDENTIFIABILITY TOURNAMENT")
    print("authority=none; audit=unset; finite conditional diagnostic; no Born promotion")
    note = note_contract()
    with redirect_stdout(StringIO()):
        fixtures = c381.c323.physical_fixture_controls()
    menus, carriers, tables = installed_menus(fixtures)
    system = build_effect_system(menus, effect_functionality_premise=True)
    grades = identifiability_controls(system)
    quotient = quotient_and_refinement_controls(system)
    host = host_augmentation_controls(system, fixtures[3], grades["bounds"])
    candidates = candidate_augmenting_menu_controls(system)
    frame = frame_and_held_controls(system, fixtures, carriers, tables)
    attacks = deletion_and_domain_controls(system)
    provenance = provenance_and_semantic_controls()
    check(
        "Cycle 385 gives an exact bounded underdetermination diagnostic and constructive overlap-menu retask without a no-go or Born-law claim",
        not note["missing"]
        and grades["matrix_rank"] == 20
        and grades["nullity"] == 35
        and grades["nontrace_minimum"] > 0
        and quotient["coarse_presentation_rank_gain_over_fine_only"] == 5
        and host["projected_old_class_freedom_after_all_host_menus"] == 34
        and candidates["greedy_independent_candidate_menus"] == 7
        and frame["incidence_or_rank_frame_failures"] == 0
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and provenance["bounded_diagnostic_only"]
        and provenance["selected_numerical_grade"] is None
        and provenance["no_go"] is provenance["axiom_pressure"] is None,
        {
            "disposition": "exact finite conditional menu-overlap identifiability diagnostic",
            "rank_nullity": (grades["matrix_rank"], grades["nullity"]),
            "strongest_positive": "strictly positive trace and nontrace normalized finite-table witnesses plus seven explicit independent candidate overlap menus",
            "bounded_residual": "the enumerated 55-class graph retains 35 affine directions; host merge lowers original-class freedom by one",
            "next_constructive_test": "physically register and compile the seven candidate hybrid menus, then recompute rank without assuming eligibility",
            "no_go_or_axiom_pressure": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MENU_OVERLAP_GRADE_IDENTIFIABILITY_TOURNAMENT_OPEN")
        return 1
    print("RESULT PHYSICAL_MENU_OVERLAP_GRADE_IDENTIFIABILITY_EXACT_FINITE_DIAGNOSTIC")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
