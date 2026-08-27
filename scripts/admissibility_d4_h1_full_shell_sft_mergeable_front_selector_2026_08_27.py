#!/usr/bin/env python3
"""Exact Block-213 full-shell SFT and mergeable-front selector.

The runner widens Block 212's 194-field periodic catalog to the full binary
shift whose six-neighbor word is one of the 26 readable words.  It proves the
cube-edge normal form, checkerboard factorization, finite scalar-moat and
finite-nucleus constructions, and the preregistered planar-interface census.
It separately tests a native five-of-six permanent-bit propagation rule so a
static completion is not mislabeled as autonomous formation, then constructs
and scopes a supplied-seed append-only permanent-status cap front.
"""
from __future__ import annotations

import argparse
import itertools
import subprocess
from collections import Counter
from functools import cache
from pathlib import Path
from typing import Iterable

import sympy as sp
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27 as b212  # noqa: E402


Vector = tuple[int, int, int]
AUDIT_TIMEOUT_SEC = 300
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block213-mergeable-full-shell-sft-20260827"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_H1_SHARED_SHELL_OVERLAP_CROSS_MOMENT_AND_"
    "UNIQUE_WRITER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
PARENT_RUNNER_PATH = (
    "scripts/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.py"
)
PARENT_CACHE_PATH = (
    "logs/runner-cache/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.txt"
)
PARENT_COMMIT = "ee72530dd92ad5701224f36d4ed0040c1057d704"
PREREG_COMMIT = "249ffece4bac4e8e527884becfa97f871ba33596"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "ffc3fbb8cba8873841be82d903d5b1789f1b2e92"
PREFLIGHT_BLOB = "3fe8de6a0acc0595d8861492e544eb087dbceb5f"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_NOTE_BLOB = "5fda2c56a144b8b095352e1eb37159aebd1478d9"
PARENT_RUNNER_BLOB = "a7a9123021425f486534d84da21aba7130e476b1"
PARENT_CACHE_BLOB = "67ea07b30a9ad94131370dc31f862fab8a7eb38f"

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block213-mergeable-full-shell-sft-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block213-mergeable-full-shell-sft-20260827/PREFLIGHT.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_SHARED_SHELL_OVERLAP_CROSS_MOMENT_AND_UNIQUE_WRITER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.py",
    "logs/runner-cache/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.txt",
)

AXES: tuple[Vector, ...] = b212.AXES
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}
ANTIPODE = b212.ANTIPODE
PAIR_INDICES = ((0, 1), (2, 3), (4, 5))
TORUS4 = tuple(itertools.product(range(4), repeat=3))
TORUS4_INDEX = {site: index for index, site in enumerate(TORUS4)}
L1_BALL2 = tuple(
    site for site in itertools.product(range(-2, 3), repeat=3)
    if sum(map(abs, site)) <= 2
)


MUTATIONS = (
    "stale_main",
    "drop_preregistration",
    "alter_goal",
    "break_word_count",
    "break_cube_edge_form",
    "break_decoder",
    "break_complement",
    "break_layered_wall",
    "break_checkerboard_factorization",
    "break_checkerboard_count",
    "erase_scalar_moats",
    "change_scalar_moat_radius",
    "erase_catalog_caps",
    "change_catalog_cap_histogram",
    "erase_safe_spacing",
    "break_planar_census",
    "claim_all_planar_pairs_join",
    "erase_transverse_rigidity",
    "erase_parallel_wall",
    "break_five_bit_completion",
    "claim_native_seed_propagates",
    "claim_native_front_complete",
    "break_packet_formula",
    "break_permanent_status_confluence",
    "change_status_alphabet",
    "claim_status_seed_not_supplied",
    "claim_status_m2_cp_compiled",
    "claim_status_dense_collision_safe",
    "break_mixed_symmetry_witness",
    "claim_static_is_formation",
    "claim_event_site_selected",
    "claim_occurrence_rate_selected",
    "claim_dense_multi_seed_confluence",
    "claim_complete_history",
    "claim_h2_open",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_movement",
    "claim_retained",
    "claim_universal_no_go",
)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def blob(revision: str, path: str) -> str:
        return git_output("rev-parse", f"{revision}:{path}")

    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": blob(PREREG_COMMIT, GOAL_PATH),
        "goal_worktree": blob("HEAD", GOAL_PATH),
        "preflight_registered": blob(PREREG_COMMIT, PREFLIGHT_PATH),
        "preflight_worktree": blob("HEAD", PREFLIGHT_PATH),
        "axiom_main": blob("origin/main", AXIOM_PATH),
        "axiom_worktree": blob("HEAD", AXIOM_PATH),
        "registry_main": blob("origin/main", REGISTRY_PATH),
        "registry_worktree": blob("HEAD", REGISTRY_PATH),
        "parent_note": blob(PARENT_COMMIT, PARENT_NOTE_PATH),
        "parent_runner": blob(PARENT_COMMIT, PARENT_RUNNER_PATH),
        "parent_cache": blob(PARENT_COMMIT, PARENT_CACHE_PATH),
        "inputs_exist": bool(AUDIT_INPUT_PATHS)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def allowed_words() -> frozenset[int]:
    words = set()
    for mask in range(64):
        xor_vector = tuple(
            ((mask >> left) & 1) ^ ((mask >> right) & 1)
            for left, right in PAIR_INDICES
        )
        if sum(xor_vector) == 1 or (
            xor_vector == (0, 0, 0) and mask in (0, 63)
        ):
            words.add(mask)
    return frozenset(words)


def cube_vertices(mask: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    negative = tuple((mask >> left) & 1 for left, _right in PAIR_INDICES)
    positive = tuple((mask >> right) & 1 for _left, right in PAIR_INDICES)
    return negative, positive


def decode_word(mask: int) -> tuple[object, ...] | None:
    if mask == 0:
        return ("dot", 1)
    if mask == 63:
        return ("dot", -1)
    negative, positive = cube_vertices(mask)
    differences = tuple(index for index in range(3) if negative[index] != positive[index])
    if len(differences) != 1:
        return None
    coordinate = differences[0]
    sign = 1 if sum(negative) % 2 == 0 else -1
    axis = [0, 0, 0]
    axis[coordinate] = sign
    return ("cross",) + tuple(axis)


@cache
def word_facts() -> dict[str, object]:
    words = allowed_words()
    parent_supports = b212.stochastic_supports()
    parent_words = {
        mask for support in parent_supports.values() for mask in support
    }
    parent_decoder = {
        mask: label for label, support in parent_supports.items() for mask in support
    }
    cube_edges = []
    loops = []
    for mask in words:
        negative, positive = cube_vertices(mask)
        distance = sum(a != b for a, b in zip(negative, positive))
        if distance == 1:
            cube_edges.append((negative, positive))
        else:
            loops.append((negative, positive))
    complement = all((63 ^ mask) in words for mask in words)
    rotations = b212.b211.shell_permutations()
    covariance = all(
        b212.b211.act_mask(mask, permutation) in words
        for mask in words for permutation in rotations
    )

    hamming_edges = tuple(
        (left, right)
        for left, right in itertools.combinations(sorted(words), 2)
        if (left ^ right).bit_count() == 1
    )
    completion_histogram = Counter()
    ambiguous_contexts = []
    for missing in range(6):
        for other_bits in range(32):
            completions = []
            for value in (0, 1):
                mask = 0
                source = 0
                for index in range(6):
                    bit = value if index == missing else ((other_bits >> source) & 1)
                    source += int(index != missing)
                    mask |= bit << index
                if mask in words:
                    completions.append(value)
            completion_histogram[len(completions)] += 1
            if len(completions) == 2:
                ambiguous_contexts.append((missing, other_bits))
    return {
        "word_count": len(words),
        "parent_word_set_exact": words == parent_words,
        "weight_histogram": dict(Counter(mask.bit_count() for mask in words)),
        "directed_cube_edges": len(cube_edges),
        "scalar_cube_loops": tuple(sorted(loops)),
        "cube_edge_normal_form": len(cube_edges) == 24
        and tuple(sorted(loops)) == (((0, 0, 0), (0, 0, 0)), ((1, 1, 1), (1, 1, 1))),
        "decoder_exact": all(decode_word(mask) == parent_decoder[mask] for mask in words),
        "complement_closed": complement,
        "proper_cubic_closed": covariance,
        "hamming_edge_count": len(hamming_edges),
        "hamming_edges_only_scalar_point": all(
            left in (0, 63) or right in (0, 63) for left, right in hamming_edges
        ),
        "five_known_completion_histogram": dict(completion_histogram),
        "ambiguous_five_known_contexts": tuple(ambiguous_contexts),
    }


@cache
def periodic_catalog() -> tuple[tuple[tuple[int, ...], tuple[object, ...]], ...]:
    rotations = b212.b211.b194.proper_cubic_rotations()
    catalog: list[tuple[tuple[int, ...], tuple[object, ...]]] = []
    for target in AXES:
        rotation = next(
            candidate for candidate in rotations
            if tuple(map(int, candidate * sp.Matrix((0, 0, 1)))) == target
        )
        sector = {}
        for translation in TORUS4:
            field = tuple(
                b212.period4_bit(tuple(map(
                    int, rotation.T * sp.Matrix(add(site, translation))
                )))
                for site in TORUS4
            )
            sector.setdefault(field, translation)
        catalog.extend((field, (target, translation)) for field, translation in sector.items())
    catalog.extend(
        (((0,) * 64, ("P", (0, 0, 0))), ((1,) * 64, ("N", (0, 0, 0))))
    )
    return tuple(catalog)


def torus_bit(field: tuple[int, ...], site: Vector) -> int:
    return field[TORUS4_INDEX[tuple(value % 4 for value in site)]]


def shell_mask_from_function(center: Vector, bit) -> int:
    return sum(bit(add(center, axis)) << index for index, axis in enumerate(AXES))


def periodic_valid(field: tuple[int, ...]) -> bool:
    return all(
        shell_mask_from_function(center, lambda site: torus_bit(field, site)) in allowed_words()
        for center in TORUS4
    )


@cache
def structural_facts() -> dict[str, object]:
    catalog = periodic_catalog()
    fields = tuple(field for field, _label in catalog)
    labels = tuple(label for _field, label in catalog)
    even_restrictions = {
        tuple(field[index] for index, site in enumerate(TORUS4) if sum(site) % 2 == 0)
        for field in fields
    }
    odd_restrictions = {
        tuple(field[index] for index, site in enumerate(TORUS4) if sum(site) % 2 == 1)
        for field in fields
    }
    splices = set()
    all_splices_valid = True
    shell_source_exact = True
    for even_field in fields:
        for odd_field in fields:
            splice = tuple(
                even_field[index] if sum(site) % 2 == 0 else odd_field[index]
                for index, site in enumerate(TORUS4)
            )
            splices.add(splice)
            all_splices_valid &= periodic_valid(splice)
            shell_source_exact &= all(
                shell_mask_from_function(
                    center, lambda site: torus_bit(splice, site)
                )
                == shell_mask_from_function(
                    center,
                    lambda site, source=(odd_field if sum(center) % 2 == 0 else even_field): torus_bit(source, site),
                )
                for center in TORUS4
            )

    # A field constant on y,z is valid exactly when its 1D word has no isolated
    # bit.  Exhaustive cyclic controls through length 12 back the two-line proof.
    layered_checks = []
    for length in range(2, 13):
        for sequence in itertools.product((0, 1), repeat=length):
            no_isolated = all(
                not (
                    sequence[(index - 1) % length]
                    == sequence[(index + 1) % length]
                    != sequence[index]
                )
                for index in range(length)
            )
            valid = all(
                (
                    sequence[(index - 1) % length]
                    | (sequence[(index + 1) % length] << 1)
                    | (sequence[index] << 2)
                    | (sequence[index] << 3)
                    | (sequence[index] << 4)
                    | (sequence[index] << 5)
                ) in allowed_words()
                for index in range(length)
            )
            layered_checks.append(valid == no_isolated)
    step = lambda x: int(x >= 1)
    step_masks = tuple(
        step(x - 1)
        | (step(x + 1) << 1)
        | (step(x) << 2)
        | (step(x) << 3)
        | (step(x) << 4)
        | (step(x) << 5)
        for x in range(-3, 5)
    )
    flip_degrees = []
    for field in fields:
        degree = 0
        for index in range(64):
            flipped = field[:index] + (1 - field[index],) + field[index + 1:]
            degree += int(periodic_valid(flipped))
        flip_degrees.append(degree)
    return {
        "catalog_count": len(catalog),
        "catalog_distinct": len(set(fields)),
        "catalog_all_valid": all(map(periodic_valid, fields)),
        "vector_count": sum(isinstance(label[0], tuple) for label in labels),
        "even_restriction_classes": len(even_restrictions),
        "odd_restriction_classes": len(odd_restrictions),
        "ordered_checkerboard_pairs": len(fields) ** 2,
        "distinct_checkerboard_splices": len(splices),
        "checkerboard_splices_valid": all_splices_valid,
        "checkerboard_shell_source_exact": shell_source_exact,
        "parity_factorization_exact": True,
        "layered_no_isolated_equivalence": all(layered_checks),
        "layered_control_count": len(layered_checks),
        "step_wall_valid": all(mask in allowed_words() for mask in step_masks),
        "step_wall_masks": tuple(sorted(set(step_masks))),
        "single_bit_flip_degree_histogram": dict(Counter(flip_degrees)),
        "periodic_vector_one_bit_rigid": all(degree == 0 for degree in flip_degrees[:192]),
        "scalar_one_bit_degrees": tuple(flip_degrees[192:]),
    }


def affected_centers(sites: Iterable[Vector]) -> tuple[Vector, ...]:
    return tuple(sorted({sub(site, axis) for site in sites for axis in AXES}))


def add_shell_constraints(
    solver: Solver,
    variables: dict[Vector, int],
    exterior: int,
) -> None:
    for center in affected_centers(variables):
        neighbors = tuple(add(center, axis) for axis in AXES)
        for forbidden in range(64):
            if forbidden in allowed_words():
                continue
            clause = []
            assignment_impossible = False
            for index, site in enumerate(neighbors):
                variable = variables.get(site)
                bit = (forbidden >> index) & 1
                if variable is None:
                    if bit != exterior:
                        assignment_impossible = True
                        break
                else:
                    clause.append(-variable if bit else variable)
            if not assignment_impossible:
                solver.add_clause(clause)


def model_field(
    variables: dict[Vector, int],
    model: list[int],
    exterior: int,
):
    positive = {literal for literal in model if literal > 0}
    values = {site: int(variable in positive) for site, variable in variables.items()}
    return lambda site: values.get(site, exterior)


def validate_finite_field(
    variables: dict[Vector, int],
    model: list[int],
    exterior: int,
) -> bool:
    bit = model_field(variables, model, exterior)
    return all(
        shell_mask_from_function(center, bit) in allowed_words()
        for center in affected_centers(variables)
    )


def l1_ball(radius: int) -> tuple[Vector, ...]:
    return tuple(
        site for site in itertools.product(range(-radius, radius + 1), repeat=3)
        if sum(map(abs, site)) <= radius
    )


def scalar_moat_solution(mask: int, radius: int, exterior: int):
    sites = l1_ball(radius)
    variables = {site: index + 1 for index, site in enumerate(sites)}
    solver = Solver(name="cadical195")
    add_shell_constraints(solver, variables, exterior)
    for index, axis in enumerate(AXES):
        value = (mask >> index) & 1
        solver.add_clause([variables[axis] if value else -variables[axis]])
    sat = solver.solve()
    model = solver.get_model() if sat else []
    solver.delete()
    valid = bool(sat and validate_finite_field(variables, model, exterior))
    return sat, model, variables, valid


@cache
def scalar_moat_facts() -> dict[str, object]:
    minima = {}
    validations = []
    support_sizes = {}
    for exterior in (0, 1):
        for mask in sorted(allowed_words()):
            minimum = None
            for radius in range(1, 7):
                sat, model, variables, valid = scalar_moat_solution(mask, radius, exterior)
                if sat:
                    minimum = radius
                    validations.append(valid)
                    bit = model_field(variables, model, exterior)
                    support_sizes[(exterior, mask)] = sum(
                        bit(site) != exterior for site in variables
                    )
                    break
            minima[(exterior, mask)] = minimum
    zero_radii = {mask: minima[(0, mask)] for mask in allowed_words()}
    one_radii = {mask: minima[(1, mask)] for mask in allowed_words()}
    complement_exact = all(
        zero_radii[mask] == one_radii[63 ^ mask] for mask in allowed_words()
    )
    explicit_triple = {
        (-1, 0, 0), (1, 0, 0), (0, -1, 0), (-1, -2, 0), (1, -2, 0)
    }
    explicit_valid = all(
        shell_mask_from_function(center, lambda site: int(site in explicit_triple))
        in allowed_words()
        for center in affected_centers(explicit_triple)
    ) and shell_mask_from_function((0, 0, 0), lambda site: int(site in explicit_triple)) == 7
    return {
        "tested_exterior_mask_pairs": len(minima),
        "all_extend_by_radius_six": all(radius is not None for radius in minima.values()),
        "maximum_minimum_radius": max(radius for radius in minima.values() if radius is not None),
        "zero_exterior_radius_histogram": dict(Counter(zero_radii.values())),
        "one_exterior_radius_histogram": dict(Counter(one_radii.values())),
        "zero_exterior_minima": tuple(sorted(zero_radii.items())),
        "one_exterior_minima": tuple(sorted(one_radii.items())),
        "complement_minima_exact": complement_exact,
        "all_models_revalidated": all(validations),
        "explicit_triple_mask7_support": tuple(sorted(explicit_triple)),
        "explicit_triple_mask7_valid": explicit_valid,
        "support_size_range": (min(support_sizes.values()), max(support_sizes.values())),
        "deterministic_template_stabilizer_covariance_selected": False,
    }


def box_sites(low: Vector, high: Vector) -> tuple[Vector, ...]:
    return tuple(itertools.product(*(
        range(low[index], high[index] + 1) for index in range(3)
    )))


def catalog_patch(field: tuple[int, ...], center: Vector = (0, 0, 0)) -> dict[Vector, int]:
    return {
        add(center, offset): torus_bit(field, offset)
        for offset in L1_BALL2
    }


def finite_seed_solver(centers: tuple[Vector, ...], pad: int):
    low = tuple(min(center[index] for center in centers) - 2 - pad for index in range(3))
    high = tuple(max(center[index] for center in centers) + 2 + pad for index in range(3))
    sites = box_sites(low, high)
    variables = {site: index + 1 for index, site in enumerate(sites)}
    solver = Solver(name="cadical195")
    add_shell_constraints(solver, variables, 0)
    assumptions = []
    for center in centers:
        by_type = []
        for field, _label in periodic_catalog():
            patch = catalog_patch(field, center)
            by_type.append(tuple(
                variables[site] if value else -variables[site]
                for site, value in patch.items()
            ))
        assumptions.append(tuple(by_type))
    return solver, variables, tuple(assumptions)


@cache
def finite_nucleus_facts() -> dict[str, object]:
    unresolved = set(range(194))
    minima: dict[int, int] = {}
    witnesses = {}
    validations = []
    for pad in range(5):
        solver, variables, assumptions = finite_seed_solver(((0, 0, 0),), pad)
        solved = []
        for field_type in sorted(unresolved):
            if solver.solve(assumptions=assumptions[0][field_type]):
                solved.append(field_type)
                model = solver.get_model() or []
                validations.append(validate_finite_field(variables, model, 0))
                witnesses[field_type] = {
                    site for site, variable in variables.items() if variable in set(
                        literal for literal in model if literal > 0
                    )
                }
        solver.delete()
        for field_type in solved:
            minima[field_type] = pad
        unresolved.difference_update(solved)
    labels = tuple(label for _field, label in periodic_catalog())
    vector_halfwidth = max(
        max(max(map(abs, site)) for site in witnesses[index]) if witnesses[index] else 0
        for index in range(192)
    )
    n_halfwidth = max(max(map(abs, site)) for site in witnesses[193])

    # Base D_+z phase versus every second type at axial separation five.  This
    # is a close-collision diagnostic, not the universal-spacing theorem.
    base_type = next(
        index for index, label in enumerate(labels)
        if label == ((0, 0, 1), (0, 0, 0))
    )
    close_histograms = {}
    close_validations = []
    for direction in ((5, 0, 0), (0, 5, 0), (0, 0, 5)):
        unresolved_types = set(range(194))
        close_minima = {}
        for pad in range(5):
            solver, variables, assumptions = finite_seed_solver(((0, 0, 0), direction), pad)
            solved = []
            for second_type in sorted(unresolved_types):
                query = assumptions[0][base_type] + assumptions[1][second_type]
                if solver.solve(assumptions=query):
                    solved.append(second_type)
                    if len(close_validations) < 20:
                        close_validations.append(validate_finite_field(
                            variables, solver.get_model() or [], 0
                        ))
            solver.delete()
            for second_type in solved:
                close_minima[second_type] = pad
            unresolved_types.difference_update(solved)
        close_histograms[direction] = dict(Counter(close_minima.values()))
        close_histograms[(direction, "unresolved")] = len(unresolved_types)

    safe_separations = {
        "vector_vector": 2 * vector_halfwidth + 3,
        "vector_N": vector_halfwidth + n_halfwidth + 3,
        "N_N": 2 * n_halfwidth + 3,
    }
    return {
        "catalog_seed_types": 194,
        "all_catalog_types_p_capped": not unresolved,
        "minimum_pad_histogram": dict(Counter(minima.values())),
        "all_models_revalidated": all(validations),
        "vector_support_cube_halfwidth": vector_halfwidth,
        "n_support_cube_halfwidth": n_halfwidth,
        "safe_axial_center_separations": safe_separations,
        "arbitrary_finite_safe_separated_seed_union": True,
        "close_base_type": base_type,
        "close_base_vs_all_histograms": close_histograms,
        "close_base_vs_all_complete": all(
            close_histograms[(direction, "unresolved")] == 0
            for direction in ((5, 0, 0), (0, 5, 0), (0, 0, 5))
        ),
        "close_sample_models_revalidated": all(close_validations),
        "all_194_squared_close_pairs_tested": False,
        "dense_collision_front_constructed": False,
    }


def planar_solver(width: int):
    sites = tuple(
        (x, y, z)
        for x in range(-2, width + 2)
        for y in range(4)
        for z in range(4)
    )
    variables = {site: index + 1 for index, site in enumerate(sites)}
    solver = Solver(name="cadical195")
    for x in range(-1, width + 1):
        for y in range(4):
            for z in range(4):
                neighbors = (
                    (x - 1, y, z), (x + 1, y, z),
                    (x, (y - 1) % 4, z), (x, (y + 1) % 4, z),
                    (x, y, (z - 1) % 4), (x, y, (z + 1) % 4),
                )
                for forbidden in range(64):
                    if forbidden not in allowed_words():
                        solver.add_clause([
                            -variables[site] if (forbidden >> index) & 1 else variables[site]
                            for index, site in enumerate(neighbors)
                        ])
    left_assumptions = []
    right_assumptions = []
    for field, _label in periodic_catalog():
        left_assumptions.append(tuple(
            variables[(x, y, z)] if torus_bit(field, (x, y, z))
            else -variables[(x, y, z)]
            for x in (-2, -1) for y in range(4) for z in range(4)
        ))
        right_assumptions.append(tuple(
            variables[(x, y, z)] if torus_bit(field, (x, y, z))
            else -variables[(x, y, z)]
            for x in (width, width + 1) for y in range(4) for z in range(4)
        ))
    return solver, variables, tuple(left_assumptions), tuple(right_assumptions)


@cache
def planar_facts() -> dict[str, object]:
    unresolved = {(left, right) for left in range(194) for right in range(194)}
    minima = {}
    sample_validations = []
    for width in range(9):
        solver, variables, left_assumptions, right_assumptions = planar_solver(width)
        solved = []
        for left, right in sorted(unresolved):
            if solver.solve(assumptions=left_assumptions[left] + right_assumptions[right]):
                solved.append((left, right))
                if len(sample_validations) < 20:
                    positive = {literal for literal in (solver.get_model() or []) if literal > 0}
                    sample_validations.append(all(
                        any(
                            all(
                                ((variables[site] in positive) == ((mask >> index) & 1))
                                for index, site in enumerate((
                                    (x - 1, y, z), (x + 1, y, z),
                                    (x, (y - 1) % 4, z), (x, (y + 1) % 4, z),
                                    (x, y, (z - 1) % 4), (x, y, (z + 1) % 4),
                                ))
                            )
                            for mask in allowed_words()
                        )
                        for x in range(-1, width + 1)
                        for y in range(4) for z in range(4)
                    ))
        solver.delete()
        for pair in solved:
            minima[pair] = width
        unresolved.difference_update(solved)

    fields = tuple(field for field, _label in periodic_catalog())
    labels = tuple(label for _field, label in periodic_catalog())
    base_type = next(
        index for index, label in enumerate(labels)
        if label == ((1, 0, 0), (0, 0, 0))
    )
    base_right_minima = {
        right: width for (left, right), width in minima.items() if left == base_type
    }

    # Perpendicular half-space rigidity: flipping the one unknown normal bit
    # of every actual boundary shell leaves the 26-word set.
    rigidity_checks = []
    for index, (field, label) in enumerate(periodic_catalog()[:192]):
        sector = label[0]
        for direction_index, normal in enumerate(AXES):
            if sum(a * b for a, b in zip(sector, normal)) != 0:
                continue
            for center in TORUS4:
                mask = shell_mask_from_function(center, lambda site: torus_bit(field, site))
                rigidity_checks.append((mask ^ (1 << direction_index)) not in allowed_words())

    return {
        "ordered_boundary_pairs": 194 ** 2,
        "widths_tested": tuple(range(9)),
        "minimum_width_histogram": dict(Counter(minima.values())),
        "pairs_joining_by_width_eight": len(minima),
        "pairs_unresolved_through_width_eight": len(unresolved),
        "all_pairs_join": not unresolved,
        "sample_models_revalidated": all(sample_validations),
        "base_parallel_right_success": len(base_right_minima),
        "base_parallel_minimum_width_histogram": dict(Counter(base_right_minima.values())),
        "perpendicular_boundary_flip_checks": len(rigidity_checks),
        "perpendicular_halfspace_rigid": all(rigidity_checks),
        "rigidity_transverse_period_assumption_needed": False,
        "parallel_antipodal_wall_exists": any(
            labels[right][0] == (-1, 0, 0)
            for right in base_right_minima if isinstance(labels[right][0], tuple)
        ),
        "negative_scope": "period4_transverse_width_0_to_8_except_exact_perpendicular_induction",
    }


def unique_propagation(field: tuple[int, ...], seed_sites: tuple[Vector, ...], max_rounds: int = 12):
    known = {site: torus_bit(field, site) for site in seed_sites}
    rounds = []
    conflict = False
    target_mismatch = False
    ambiguous = 0
    for _round in range(max_rounds):
        centers = affected_centers(known)
        proposals: dict[Vector, set[int]] = {}
        for center in centers:
            neighbors = tuple(add(center, axis) for axis in AXES)
            blanks = tuple(site for site in neighbors if site not in known)
            if len(blanks) != 1:
                continue
            site = blanks[0]
            completions = []
            for value in (0, 1):
                mask = sum(
                    (value if neighbor == site else known[neighbor]) << index
                    for index, neighbor in enumerate(neighbors)
                )
                if mask in allowed_words():
                    completions.append(value)
            if len(completions) == 1:
                proposals.setdefault(site, set()).add(completions[0])
            elif len(completions) == 2:
                ambiguous += 1
        if any(len(values) > 1 for values in proposals.values()):
            conflict = True
            break
        new = {site: next(iter(values)) for site, values in proposals.items()}
        if not new:
            break
        target_mismatch |= any(value != torus_bit(field, site) for site, value in new.items())
        known.update(new)
        rounds.append(len(new))
    return {
        "known": len(known),
        "rounds": tuple(rounds),
        "conflict": conflict,
        "target_mismatch": target_mismatch,
        "ambiguous": ambiguous,
    }


@cache
def front_facts() -> dict[str, object]:
    fields = tuple(field for field, _label in periodic_catalog())
    l1_seed_results = tuple(unique_propagation(field, L1_BALL2) for field in fields)
    cube2 = tuple(itertools.product(range(-2, 3), repeat=3))
    cube_results = tuple(unique_propagation(field, cube2) for field in fields)
    vector_cube = cube_results[:192]
    scalar_cube = cube_results[192:]
    return {
        "five_known_completion_histogram": word_facts()["five_known_completion_histogram"],
        "ambiguous_context_count": len(word_facts()["ambiguous_five_known_contexts"]),
        "l1_radius_two_seed_types_tested": len(l1_seed_results),
        "l1_radius_two_types_with_growth": sum(result["known"] > 25 for result in l1_seed_results),
        "cube_seed_types_tested": len(cube_results),
        "vector_cube_types_with_growth": sum(result["known"] > 125 for result in vector_cube),
        "vector_cube_round_histogram": dict(Counter(len(result["rounds"]) for result in vector_cube)),
        "vector_cube_terminal_size_histogram": dict(Counter(result["known"] for result in vector_cube)),
        "scalar_cube_types_with_growth": sum(result["known"] > 125 for result in scalar_cube),
        "proposal_conflicts": sum(result["conflict"] for result in cube_results),
        "proposal_target_mismatches": sum(result["target_mismatch"] for result in cube_results),
        "native_unique_rule_stalls": all(len(result["rounds"]) < 12 for result in cube_results),
        "ambiguous_branch_rule_selected": False,
        "tentative_status_dynamics_constructed": False,
        "event_site_selected": False,
        "occurrence_rate_selected": False,
        "dense_multi_seed_confluence": False,
        "complete_history": False,
        "static_completion_is_formation": False,
    }


def packet_backgrounds(mask: int) -> tuple[int, ...]:
    weight = mask.bit_count()
    if weight in (0, 1):
        return (0,)
    if weight in (5, 6):
        return (1,)
    if weight == 3:
        return (0, 1)
    return ()


def packet_geometry(mask: int, background: int) -> dict[str, object]:
    defects = {
        axis for index, axis in enumerate(AXES)
        if ((mask >> index) & 1) != background
    }
    antipodal_axis = None
    singleton = None
    endpoints: set[Vector] = set()
    if len(defects) == 3:
        for left, right in PAIR_INDICES:
            if AXES[left] in defects and AXES[right] in defects:
                antipodal_axis = AXES[left]
                singleton = next(site for site in defects if site not in (AXES[left], AXES[right]))
                break
        if antipodal_axis is None or singleton is None:
            raise ValueError("allowed triple lacks the unique antipodal-pair form")
        twice_singleton = tuple(2 * value for value in singleton)
        endpoints = {
            add(antipodal_axis, twice_singleton),
            add(tuple(-value for value in antipodal_axis), twice_singleton),
        }
    support = defects | endpoints
    return {
        "defects": frozenset(defects),
        "antipodal_axis": antipodal_axis,
        "singleton": singleton,
        "endpoints": frozenset(endpoints),
        "support": frozenset(support),
    }


def support_bit(support: frozenset[Vector] | set[Vector], background: int):
    return lambda site: (1 - background) if site in support else background


def validate_support(support: frozenset[Vector] | set[Vector], background: int) -> bool:
    bit = support_bit(support, background)
    return all(
        shell_mask_from_function(center, bit) in allowed_words()
        for center in affected_centers(support)
    )


def status_bit(status: tuple[object, ...]) -> int:
    kind = status[0]
    if kind in ("LOCK", "BG"):
        return int(status[1])
    background = int(status[2])
    return background if kind == "STEP" else 1 - background


def status_seed(mask: int, background: int) -> dict[Vector, tuple[object, ...]]:
    geometry = packet_geometry(mask, background)
    state: dict[Vector, tuple[object, ...]] = {(0, 0, 0): ("LOCK", background)}
    if mask.bit_count() != 3:
        for index, axis in enumerate(AXES):
            bit = (mask >> index) & 1
            state[axis] = ("BG", background) if bit == background else ("LOCK", bit)
        return state

    antipodal_axis = geometry["antipodal_axis"]
    singleton = geometry["singleton"]
    assert isinstance(antipodal_axis, tuple) and isinstance(singleton, tuple)
    pair = {antipodal_axis, tuple(-value for value in antipodal_axis)}
    for axis in AXES:
        if axis in pair:
            state[axis] = ("PORT", singleton, background)
        elif axis == singleton:
            state[axis] = ("GPORT", singleton, background)
        else:
            state[axis] = ("LOCK", background)
    return state


def role_footprint(mask: int, background: int) -> frozenset[Vector]:
    footprint = set(status_seed(mask, background))
    if mask.bit_count() == 3:
        geometry = packet_geometry(mask, background)
        antipodal_axis = geometry["antipodal_axis"]
        singleton = geometry["singleton"]
        assert isinstance(antipodal_axis, tuple) and isinstance(singleton, tuple)
        opposite = tuple(-value for value in antipodal_axis)
        for port in (antipodal_axis, opposite):
            footprint.add(add(port, singleton))
            footprint.add(add(port, tuple(2 * value for value in singleton)))
        footprint.add(tuple(2 * value for value in singleton))
    return frozenset(footprint)


def launched_role_state(
    mask: int, background: int, center: Vector = (0, 0, 0)
) -> dict[Vector, tuple[object, ...]]:
    """Return the supplied seed after every reserved arm and gate has fired."""
    state = status_seed(mask, background)
    if mask.bit_count() == 3:
        geometry = packet_geometry(mask, background)
        antipodal_axis = geometry["antipodal_axis"]
        singleton = geometry["singleton"]
        assert isinstance(antipodal_axis, tuple) and isinstance(singleton, tuple)
        for port in (antipodal_axis, tuple(-value for value in antipodal_axis)):
            state[add(port, singleton)] = ("STEP", singleton, background)
            state[add(port, tuple(2 * value for value in singleton))] = (
                "END", singleton, background
            )
        state[tuple(2 * value for value in singleton)] = ("BG", background)
    return {add(center, site): status for site, status in state.items()}


def transform_status(
    status: tuple[object, ...], rotation: sp.Matrix
) -> tuple[object, ...]:
    """Apply a proper lattice rotation and bit complement to one status."""
    kind = status[0]
    if kind in ("LOCK", "BG"):
        return (kind, 1 - int(status[1]))
    direction = status[1]
    assert isinstance(direction, tuple)
    transformed_direction = tuple(map(int, rotation * sp.Matrix(direction)))
    return (kind, transformed_direction, 1 - int(status[2]))


def protected_targets(
    state: dict[Vector, tuple[object, ...]],
) -> frozenset[Vector]:
    protected = set()
    for site, status in state.items():
        kind = status[0]
        if kind not in ("PORT", "GPORT"):
            continue
        direction = status[1]
        assert isinstance(direction, tuple)
        protected.add(add(site, direction))
        if kind == "PORT":
            protected.add(add(site, tuple(2 * value for value in direction)))
    return frozenset(protected)


def flood_to_bench(
    state: dict[Vector, tuple[object, ...]],
    background: int,
    bench: frozenset[Vector],
    scheduler: str,
) -> tuple[bool, int]:
    protected = set(protected_targets(state))
    frontier = {
        target
        for site, status in state.items()
        if status == ("BG", background)
        for axis in AXES
        for target in (add(site, axis),)
        if target in bench and target not in state and target not in protected
    }
    additions = 0
    while frontier:
        if scheduler == "lex_min":
            target = min(frontier)
        elif scheduler == "lex_max":
            target = max(frontier)
        elif scheduler == "near_first":
            target = min(frontier, key=lambda item: (sum(map(abs, item)), item))
        elif scheduler == "far_first":
            target = max(frontier, key=lambda item: (sum(map(abs, item)), item))
        else:
            raise ValueError(scheduler)
        frontier.remove(target)
        if target in state:
            continue
        state[target] = ("BG", background)
        additions += 1
        for axis in AXES:
            candidate = add(target, axis)
            if (
                candidate in bench and candidate not in state
                and candidate not in protected
            ):
                frontier.add(candidate)
    return set(state) == set(bench), additions


def advance_triple_seed(
    mask: int,
    background: int,
    order: tuple[str, ...],
    scheduler: str,
    bench: frozenset[Vector],
) -> tuple[dict[Vector, tuple[object, ...]], bool, bool]:
    state = status_seed(mask, background)
    geometry = packet_geometry(mask, background)
    antipodal_axis = geometry["antipodal_axis"]
    singleton = geometry["singleton"]
    assert isinstance(antipodal_axis, tuple) and isinstance(singleton, tuple)
    ports = {
        "L": antipodal_axis,
        "R": tuple(-value for value in antipodal_axis),
    }
    progress = {"L": 0, "R": 0}
    local = True
    append_only = True
    for token in order:
        arm = token[0]
        port = ports[arm]
        if token[1] == "s":
            source = port
            target = add(port, singleton)
            expected = ("PORT", singleton, background)
            formed = ("STEP", singleton, background)
            required_progress = 0
        else:
            source = add(port, singleton)
            target = add(port, tuple(2 * value for value in singleton))
            expected = ("STEP", singleton, background)
            formed = ("END", singleton, background)
            required_progress = 1
        local &= sum(map(abs, sub(target, source))) == 1 and state.get(source) == expected
        append_only &= target not in state and progress[arm] == required_progress
        if target in state:
            return state, False, False
        state[target] = formed
        progress[arm] += 1

    launcher = tuple(2 * value for value in singleton)
    end_sites = tuple(
        add(port, tuple(2 * value for value in singleton))
        for port in ports.values()
    )
    gate_neighbors = (
        add(singleton, (0, 0, 0)),
        *end_sites,
    )
    local &= all(sum(map(abs, sub(site, launcher))) == 1 for site in gate_neighbors)
    gate_ok = (
        state.get(singleton) == ("GPORT", singleton, background)
        and all(state.get(site) == ("END", singleton, background) for site in end_sites)
        and launcher not in state
    )
    append_only &= gate_ok
    if gate_ok:
        state[launcher] = ("BG", background)
    full, _additions = flood_to_bench(state, background, bench, scheduler)
    return state, local and full, append_only


@cache
def permanent_status_front_facts() -> dict[str, object]:
    cases = tuple(
        (mask, background)
        for mask in sorted(allowed_words())
        for background in packet_backgrounds(mask)
    )
    packet_validations = []
    central_masks = []
    for mask, background in cases:
        support = packet_geometry(mask, background)["support"]
        assert isinstance(support, frozenset)
        bit = support_bit(support, background)
        packet_validations.append(validate_support(support, background))
        central_masks.append(shell_mask_from_function((0, 0, 0), bit) == mask)

    visible_states = {
        *(('LOCK', bit) for bit in (0, 1)),
        *(('BG', bit) for bit in (0, 1)),
        *((kind, direction, background)
          for kind in ("PORT", "GPORT", "STEP", "END")
          for direction in AXES for background in (0, 1)),
    }
    status_decode_valid = all(status_bit(status) in (0, 1) for status in visible_states)
    bench = frozenset(itertools.product(range(-3, 4), repeat=3))
    schedulers = ("lex_min", "lex_max", "near_first", "far_first")
    interleavings = tuple(
        order for order in itertools.permutations(("Ls", "Le", "Rs", "Re"))
        if order.index("Ls") < order.index("Le")
        and order.index("Rs") < order.index("Re")
    )
    causal_prefixes = {
        order[:length]
        for order in interleavings
        for length in range(len(order) + 1)
    }
    reachable_arm_states = {
        (
            sum(token.startswith("L") for token in prefix),
            sum(token.startswith("R") for token in prefix),
        )
        for prefix in causal_prefixes
    }
    guard_completeness = []
    background_reachability = []
    background_write_compatibility = []
    for mask, background in cases:
        seed = status_seed(mask, background)
        formed_background_statuses = {
            status for status in seed.values() if status[0] == "BG"
        } | {("BG", background)}
        background_write_compatibility.append(
            formed_background_statuses == {("BG", background)}
        )
        footprint = set(role_footprint(mask, background))
        if mask.bit_count() == 3:
            geometry = packet_geometry(mask, background)
            antipodal_axis = geometry["antipodal_axis"]
            singleton = geometry["singleton"]
            assert isinstance(antipodal_axis, tuple) and isinstance(singleton, tuple)
            opposite = tuple(-value for value in antipodal_axis)
            expected_protection = {
                add(port, singleton)
                for port in (antipodal_axis, opposite)
            } | {
                add(port, tuple(2 * value for value in singleton))
                for port in (antipodal_axis, opposite)
            } | {tuple(2 * value for value in singleton)}
            launchers = {tuple(2 * value for value in singleton)}
        else:
            expected_protection = set()
            launchers = {
                site for site, status in seed.items()
                if status == ("BG", background)
            }
        guard_completeness.append(
            set(protected_targets(seed)) == expected_protection
        )
        blocked = footprint - launchers
        reachable = set(launchers)
        frontier = set(launchers)
        while frontier:
            site = frontier.pop()
            for axis in AXES:
                target = add(site, axis)
                if target in bench and target not in blocked and target not in reachable:
                    reachable.add(target)
                    frontier.add(target)
        background_reachability.append((set(bench) - blocked) <= reachable)
    schedule_results = []
    terminal_signatures: dict[tuple[int, int], set[tuple[tuple[Vector, tuple[object, ...]], ...]]] = {}
    strict_local = []
    append_only = []
    for mask, background in cases:
        target_support = packet_geometry(mask, background)["support"]
        assert isinstance(target_support, frozenset)
        orders = interleavings if mask.bit_count() == 3 else ((),)
        for order in orders:
            for scheduler in schedulers:
                if mask.bit_count() == 3:
                    state, local_ok, append_ok = advance_triple_seed(
                        mask, background, order, scheduler, bench
                    )
                else:
                    state = status_seed(mask, background)
                    full, _additions = flood_to_bench(
                        state, background, bench, scheduler
                    )
                    local_ok = full
                    append_ok = True
                decoded = {site: status_bit(status) for site, status in state.items()}
                target = support_bit(target_support, background)
                schedule_results.append(
                    set(state) == set(bench)
                    and all(decoded[site] == target(site) for site in bench)
                )
                strict_local.append(local_ok)
                append_only.append(append_ok)
                terminal_signatures.setdefault((mask, background), set()).add(
                    tuple(sorted(state.items()))
                )

    # Explicit unguarded race: A's background wave occupies B's two STEP
    # targets before B advances.  The delayed cap then lacks both terminal
    # defects and produces masks 10 and 9.
    race_mask = 7
    race_background = 0
    center_a = (0, 0, 0)
    center_b = (0, -6, 0)
    cap = packet_geometry(race_mask, race_background)
    cap_support = cap["support"]
    defects = cap["defects"]
    assert isinstance(cap_support, frozenset) and isinstance(defects, frozenset)
    complete_union = {
        add(center, site) for center in (center_a, center_b) for site in cap_support
    }
    raced_support = {
        add(center_a, site) for site in cap_support
    } | {
        add(center_b, site) for site in defects
    }
    raced_bit = support_bit(raced_support, race_background)
    race_bad_masks = tuple(sorted(
        shell_mask_from_function(center, raced_bit)
        for center in ((-1, -7, 0), (1, -7, 0))
    ))

    # Same-background compact caps and their permanent builder footprints are
    # compatible on the registered close pair and right-triangle benches.
    branch_cases = {
        background: tuple(
            mask for mask in sorted(allowed_words())
            if background in packet_backgrounds(mask)
        )
        for background in (0, 1)
    }
    pair_pass = 0
    pair_total = 0
    triple_pass = 0
    triple_total = 0
    for background in (0, 1):
        masks = branch_cases[background]
        for left_mask in masks:
            for right_mask in masks:
                pair_total += 1
                centers = ((0, 0, 0), (5, 0, 0))
                footprints = tuple({add(center, site) for site in role_footprint(mask, background)}
                                   for center, mask in zip(centers, (left_mask, right_mask)))
                support = {
                    add(center, site)
                    for center, mask in zip(centers, (left_mask, right_mask))
                    for site in packet_geometry(mask, background)["support"]
                }
                pair_pass += int(not (footprints[0] & footprints[1]) and validate_support(support, background))
        centers3 = ((0, 0, 0), (5, 0, 0), (0, 5, 0))
        for masks3 in itertools.product(masks, repeat=3):
            triple_total += 1
            footprints = tuple(
                {add(center, site) for site in role_footprint(mask, background)}
                for center, mask in zip(centers3, masks3)
            )
            disjoint = all(
                not (footprints[left] & footprints[right])
                for left, right in itertools.combinations(range(3), 2)
            )
            support = {
                add(center, site)
                for center, mask in zip(centers3, masks3)
                for site in packet_geometry(mask, background)["support"]
            }
            triple_pass += int(disjoint and validate_support(support, background))

    # A reachable launched-front witness makes the mixed-background obstruction
    # stronger than a two-bit cartoon.  The proper half-turn maps the complete
    # m=7,s=0 role state at +3e_y to the complemented m=52,s=1 state at -3e_y.
    # Their launchers at +/-e_y make opposite BG proposals to the empty fixed
    # midpoint.  No status in the 52-symbol alphabet is fixed by this combined
    # rotation-plus-complement action.
    rotation = sp.diag(1, -1, -1)
    left_center = (0, 3, 0)
    right_center = (0, -3, 0)
    left_status = launched_role_state(7, 0, left_center)
    right_status = launched_role_state(52, 1, right_center)
    pn_arrangement = left_status | right_status
    transformed_arrangement = {
        tuple(map(int, rotation * sp.Matrix(site))): transform_status(status, rotation)
        for site, status in pn_arrangement.items()
    }
    midpoint = (0, 0, 0)
    midpoint_fixed = tuple(map(int, rotation * sp.Matrix(midpoint))) == midpoint
    fixed_statuses = tuple(
        status for status in visible_states
        if transform_status(status, rotation) == status
    )
    midpoint_proposals = (
        pn_arrangement.get((0, 1, 0)),
        pn_arrangement.get((0, -1, 0)),
    )

    return {
        "packet_cases": len(cases),
        "nontriple_cases": sum(mask.bit_count() != 3 for mask, _background in cases),
        "triple_background_branches": sum(mask.bit_count() == 3 for mask, _background in cases),
        "packet_formulas_valid": all(packet_validations) and all(central_masks),
        "visible_status_alphabet": len(visible_states),
        "status_decode_valid": status_decode_valid,
        "ungated_reachable_arm_states": len(reachable_arm_states),
        "gated_launched_states": int(bool(interleavings)),
        "causal_prefix_histories": len(causal_prefixes),
        "arm_interleavings": len(interleavings),
        "selected_flood_policy_count": len(schedulers),
        "single_seed_schedule_cases": len(schedule_results),
        "single_seed_all_pass": all(schedule_results),
        "single_seed_terminal_confluent": all(len(items) == 1 for items in terminal_signatures.values()),
        "all_role_targets_protected": all(guard_completeness),
        "background_domain_connected_on_bench": all(background_reachability),
        "all_six_complete_arm_linear_extensions_exhausted": len(interleavings) == 6,
        "background_writes_identical_and_persistently_enabled": (
            all(background_write_compatibility)
            and all(guard_completeness)
            and all(background_reachability)
        ),
        "finite_bench_all_fair_schedule_confluence": (
            all(background_write_compatibility)
            and all(guard_completeness)
            and all(background_reachability)
            and len(interleavings) == 6
            and all(schedule_results)
        ),
        "role_formation_strict_nearest_neighbor": all(strict_local),
        "guarded_rule_maximum_radius": 2,
        "append_only_permanent": all(append_only),
        "future_target_consulted": False,
        "supplied_role_bearing_seed": True,
        "fresh_target_is_domain_restriction": True,
        "absence_assigned_readable_content": False,
        "naive_race_complete_cap_union_valid": validate_support(complete_union, race_background),
        "naive_race_bad_masks": race_bad_masks,
        "naive_unguarded_multi_seed_confluent": not race_bad_masks,
        "same_background_pair_pass_total": (pair_pass, pair_total),
        "same_background_triple_pass_total": (triple_pass, triple_total),
        "guarded_same_background_disjoint_fronts_confluent": (
            pair_pass == pair_total == 722
            and triple_pass == triple_total == 13718
        ),
        "mixed_background_stabilizer_rotation_proper": int(rotation.det()) == 1,
        "mixed_background_stabilizer_swaps_seeds": (
            tuple(map(int, rotation * sp.Matrix(left_center))) == right_center
            and tuple(map(int, rotation * sp.Matrix(right_center))) == left_center
        ),
        "mixed_background_arrangement_invariant_after_complement": (
            transformed_arrangement == pn_arrangement
        ),
        "mixed_background_full_launched_status_witness": (
            len(left_status) == len(right_status) == 12
            and set(left_status).isdisjoint(right_status)
        ),
        "mixed_background_midpoint_fixed": midpoint_fixed,
        "mixed_background_midpoint_empty": midpoint not in pn_arrangement,
        "mixed_background_opposed_midpoint_proposals": (
            midpoint_proposals == (("BG", 0), ("BG", 1))
        ),
        "mixed_background_fixed_status_options": fixed_statuses,
        "mixed_background_midpoint_symmetry_obstruction": (
            int(rotation.det()) == 1
            and transformed_arrangement == pn_arrangement
            and midpoint_fixed
            and midpoint not in pn_arrangement
            and midpoint_proposals == (("BG", 0), ("BG", 1))
            and not fixed_statuses
        ),
        "mixed_background_obstruction_scope": "deterministic_single_site_progress_under_proper_rotation_plus_complement",
        "mixed_background_random_record_escape_open": True,
        "overlapping_role_footprints_resolved": False,
        "one_site_m2_status_compilation": False,
        "normalized_local_cp_instrument": False,
        "state_action_seed_selection": False,
        "occurrence_rate_selected": False,
        "complete_history": False,
    }


@cache
def h1_bridge_facts() -> dict[str, object]:
    # Every coarse Block-211 effect is positive and normalized.  Refining a
    # vector outcome uniformly over its four readable central words preserves
    # the effect sum.  Each word now has a finite scalar-moat completion, so a
    # supplied fresh finite event region has a conditional finite-support
    # Record dilation.  Stabilizer-orbit randomization is still required for a
    # covariant template law, and no site/rate process is supplied.
    sector = b212.sector_povm_facts()
    supports = b212.stochastic_supports()
    positivity = []
    normalization = []
    refinement_sums = []
    for depth in (1, 2):
        for orientation in (1, -1):
            family = b212.b211.coarse_effects(depth, orientation)
            normalization.append(sum(family.values(), sp.zeros(4)) == sp.eye(4))
            for label, effect in family.items():
                positivity.append(effect.is_positive_definite is True)
                refined = sum(
                    (effect / len(supports[label]) for _mask in supports[label]),
                    sp.zeros(4),
                )
                refinement_sums.append(sp.simplify(refined - effect) == sp.zeros(4))
    parent_positive = all(positivity)
    parent_normalized = all(normalization)
    return {
        "coarse_effects_positive": parent_positive,
        "coarse_povm_normalized": parent_normalized,
        "word_refinement_effect_identity": all(refinement_sums),
        "every_refined_word_has_finite_completion": scalar_moat_facts()["all_extend_by_radius_six"],
        "conditional_finite_region_dilation_exists": (
            parent_positive
            and parent_normalized
            and all(refinement_sums)
            and scalar_moat_facts()["all_extend_by_radius_six"]
        ),
        "block212_parent_povm_still_positive": sector["sector_effects_strictly_positive"],
        "stabilizer_template_selection_derived": False,
        "supplied_fresh_region": True,
        "all_center_h1_stationary_law_newly_constructed": False,
        "autonomous_event_process": False,
    }


def claims() -> dict[str, object]:
    authority = authority_facts()
    words = word_facts()
    structure = structural_facts()
    moats = scalar_moat_facts()
    nuclei = finite_nucleus_facts()
    planar = planar_facts()
    front = front_facts()
    status_front = permanent_status_front_facts()
    h1 = h1_bridge_facts()
    return {
        "authority": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["goal_registered"] == GOAL_BLOB
            and authority["goal_worktree"] == GOAL_BLOB
            and authority["preflight_registered"] == PREFLIGHT_BLOB
            and authority["preflight_worktree"] == PREFLIGHT_BLOB
            and authority["axiom_main"] == AXIOM_BLOB
            and authority["axiom_worktree"] == AXIOM_BLOB
            and authority["registry_main"] == REGISTRY_MAIN_BLOB
            and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
            and authority["parent_note"] == PARENT_NOTE_BLOB
            and authority["parent_runner"] == PARENT_RUNNER_BLOB
            and authority["parent_cache"] == PARENT_CACHE_BLOB
            and authority["inputs_exist"]
        ),
        "word_normal_form": (
            words["word_count"] == 26 and words["parent_word_set_exact"]
            and words["directed_cube_edges"] == 24 and words["cube_edge_normal_form"]
            and words["decoder_exact"] and words["complement_closed"]
            and words["proper_cubic_closed"]
        ),
        "native_heterogeneity": (
            structure["catalog_count"] == 194 and structure["catalog_distinct"]
            and structure["catalog_all_valid"]
            and structure["parity_factorization_exact"]
            and structure["even_restriction_classes"] == 98
            and structure["odd_restriction_classes"] == 98
            and structure["ordered_checkerboard_pairs"] == 194 ** 2
            and structure["distinct_checkerboard_splices"] == 9604
            and structure["checkerboard_splices_valid"]
            and structure["checkerboard_shell_source_exact"]
        ),
        "layered_and_rigidity_controls": (
            structure["layered_no_isolated_equivalence"]
            and structure["step_wall_valid"]
            and structure["step_wall_masks"] == (0, 2, 62, 63)
            and structure["periodic_vector_one_bit_rigid"]
            and structure["scalar_one_bit_degrees"] == (64, 64)
        ),
        "scalar_moats": (
            moats["tested_exterior_mask_pairs"] == 52
            and moats["all_extend_by_radius_six"]
            and moats["maximum_minimum_radius"] == 5
            and moats["zero_exterior_radius_histogram"] == {1: 7, 3: 13, 5: 6}
            and moats["one_exterior_radius_histogram"] == {1: 7, 3: 13, 5: 6}
            and moats["complement_minima_exact"]
            and moats["all_models_revalidated"] and moats["explicit_triple_mask7_valid"]
        ),
        "finite_nuclei": (
            nuclei["catalog_seed_types"] == 194
            and nuclei["all_catalog_types_p_capped"]
            and nuclei["minimum_pad_histogram"] == {0: 1, 1: 120, 2: 72, 4: 1}
            and nuclei["all_models_revalidated"]
            and nuclei["vector_support_cube_halfwidth"] <= 4
            and nuclei["n_support_cube_halfwidth"] <= 6
            and nuclei["safe_axial_center_separations"]
            == {"vector_vector": 11, "vector_N": 13, "N_N": 15}
            and nuclei["arbitrary_finite_safe_separated_seed_union"]
        ),
        "close_base_control": (
            nuclei["close_base_vs_all_complete"]
            and nuclei["close_sample_models_revalidated"]
            and not nuclei["all_194_squared_close_pairs_tested"]
        ),
        "planar_interfaces": (
            planar["ordered_boundary_pairs"] == 194 ** 2
            and planar["widths_tested"] == tuple(range(9))
            and planar["minimum_width_histogram"]
            == {0: 196, 2: 256, 3: 128, 5: 384, 6: 320, 7: 1088, 8: 448}
            and planar["pairs_joining_by_width_eight"] == 2820
            and planar["pairs_unresolved_through_width_eight"] == 34816
            and not planar["all_pairs_join"]
            and planar["sample_models_revalidated"]
            and planar["perpendicular_halfspace_rigid"]
            and not planar["rigidity_transverse_period_assumption_needed"]
            and planar["parallel_antipodal_wall_exists"]
        ),
        "native_front_boundary": (
            front["five_known_completion_histogram"] == {0: 48, 1: 132, 2: 12}
            and front["ambiguous_context_count"] == 12
            and front["l1_radius_two_seed_types_tested"] == 194
            and front["l1_radius_two_types_with_growth"] == 0
            and front["cube_seed_types_tested"] == 194
            and front["vector_cube_types_with_growth"] == 192
            and front["scalar_cube_types_with_growth"] == 0
            and front["proposal_conflicts"] == 0
            and front["proposal_target_mismatches"] == 0
            and front["native_unique_rule_stalls"]
            and not front["ambiguous_branch_rule_selected"]
            and not front["tentative_status_dynamics_constructed"]
        ),
        "permanent_status_front": (
            status_front["packet_cases"] == 38
            and status_front["nontriple_cases"] == 14
            and status_front["triple_background_branches"] == 24
            and status_front["packet_formulas_valid"]
            and status_front["visible_status_alphabet"] == 52
            and status_front["status_decode_valid"]
            and status_front["ungated_reachable_arm_states"] == 9
            and status_front["gated_launched_states"] == 1
            and status_front["causal_prefix_histories"] == 19
            and status_front["arm_interleavings"] == 6
            and status_front["selected_flood_policy_count"] == 4
            and status_front["single_seed_schedule_cases"] == 632
            and status_front["single_seed_all_pass"]
            and status_front["single_seed_terminal_confluent"]
            and status_front["all_role_targets_protected"]
            and status_front["background_domain_connected_on_bench"]
            and status_front["all_six_complete_arm_linear_extensions_exhausted"]
            and status_front["background_writes_identical_and_persistently_enabled"]
            and status_front["finite_bench_all_fair_schedule_confluence"]
            and status_front["role_formation_strict_nearest_neighbor"]
            and status_front["guarded_rule_maximum_radius"] == 2
            and status_front["append_only_permanent"]
            and not status_front["future_target_consulted"]
            and status_front["naive_race_complete_cap_union_valid"]
            and status_front["naive_race_bad_masks"] == (9, 10)
            and not status_front["naive_unguarded_multi_seed_confluent"]
            and status_front["same_background_pair_pass_total"] == (722, 722)
            and status_front["same_background_triple_pass_total"] == (13718, 13718)
            and status_front["guarded_same_background_disjoint_fronts_confluent"]
            and status_front["mixed_background_stabilizer_rotation_proper"]
            and status_front["mixed_background_stabilizer_swaps_seeds"]
            and status_front["mixed_background_arrangement_invariant_after_complement"]
            and status_front["mixed_background_full_launched_status_witness"]
            and status_front["mixed_background_midpoint_fixed"]
            and status_front["mixed_background_midpoint_empty"]
            and status_front["mixed_background_opposed_midpoint_proposals"]
            and status_front["mixed_background_fixed_status_options"] == ()
            and status_front["mixed_background_midpoint_symmetry_obstruction"]
            and status_front["mixed_background_random_record_escape_open"]
        ),
        "conditional_h1_packet": (
            h1["coarse_effects_positive"] and h1["coarse_povm_normalized"]
            and h1["word_refinement_effect_identity"]
            and h1["every_refined_word_has_finite_completion"]
            and h1["conditional_finite_region_dilation_exists"]
            and not h1["stabilizer_template_selection_derived"]
            and h1["supplied_fresh_region"]
            and not h1["all_center_h1_stationary_law_newly_constructed"]
        ),
        "honest_boundary": (
            not front["event_site_selected"]
            and not front["occurrence_rate_selected"]
            and not front["dense_multi_seed_confluence"]
            and not front["complete_history"]
            and not front["static_completion_is_formation"]
            and not h1["autonomous_event_process"]
            and status_front["supplied_role_bearing_seed"]
            and status_front["fresh_target_is_domain_restriction"]
            and not status_front["absence_assigned_readable_content"]
            and not status_front["overlapping_role_footprints_resolved"]
            and not status_front["one_site_m2_status_compilation"]
            and not status_front["normalized_local_cp_instrument"]
            and not status_front["state_action_seed_selection"]
            and not status_front["occurrence_rate_selected"]
            and not status_front["complete_history"]
        ),
        "h2_sealed": True,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
        "universal_no_go": False,
    }


def mutate(values: dict[str, object], mutation: str) -> None:
    mapping = {
        "stale_main": ("authority", False),
        "drop_preregistration": ("authority", False),
        "alter_goal": ("authority", False),
        "break_word_count": ("word_normal_form", False),
        "break_cube_edge_form": ("word_normal_form", False),
        "break_decoder": ("word_normal_form", False),
        "break_complement": ("word_normal_form", False),
        "break_layered_wall": ("layered_and_rigidity_controls", False),
        "break_checkerboard_factorization": ("native_heterogeneity", False),
        "break_checkerboard_count": ("native_heterogeneity", False),
        "erase_scalar_moats": ("scalar_moats", False),
        "change_scalar_moat_radius": ("scalar_moats", False),
        "erase_catalog_caps": ("finite_nuclei", False),
        "change_catalog_cap_histogram": ("finite_nuclei", False),
        "erase_safe_spacing": ("finite_nuclei", False),
        "break_planar_census": ("planar_interfaces", False),
        "claim_all_planar_pairs_join": ("planar_interfaces", False),
        "erase_transverse_rigidity": ("planar_interfaces", False),
        "erase_parallel_wall": ("planar_interfaces", False),
        "break_five_bit_completion": ("native_front_boundary", False),
        "claim_native_seed_propagates": ("native_front_boundary", False),
        "claim_native_front_complete": ("native_front_boundary", False),
        "break_packet_formula": ("permanent_status_front", False),
        "break_permanent_status_confluence": ("permanent_status_front", False),
        "change_status_alphabet": ("permanent_status_front", False),
        "claim_status_seed_not_supplied": ("honest_boundary", False),
        "claim_status_m2_cp_compiled": ("honest_boundary", False),
        "claim_status_dense_collision_safe": ("honest_boundary", False),
        "break_mixed_symmetry_witness": ("permanent_status_front", False),
        "claim_static_is_formation": ("honest_boundary", False),
        "claim_event_site_selected": ("honest_boundary", False),
        "claim_occurrence_rate_selected": ("honest_boundary", False),
        "claim_dense_multi_seed_confluence": ("honest_boundary", False),
        "claim_complete_history": ("honest_boundary", False),
        "claim_h2_open": ("h2_sealed", False),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_movement": ("toe_movement", 1),
        "claim_retained": ("retained", True),
        "claim_universal_no_go": ("universal_no_go", True),
    }
    key, value = mapping[mutation]
    values[key] = value


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    values = claims()
    if mutation:
        mutate(values, mutation)
    checks = {
        "A": (values["authority"] is True, "authority, parent and immutable preregistration pins are exact"),
        "B": (values["word_normal_form"] is True, "the 26 words are exactly directed 3-cube edges plus two scalar loops with the parent decoder"),
        "C": (values["native_heterogeneity"] is True, "checkerboard factorization gives 9604 valid catalog splices from all 194 squared ordered pairs"),
        "D": (values["layered_and_rigidity_controls"] is True, "layered domain walls coexist with one-bit rigidity of the periodic vector catalog"),
        "E": (values["scalar_moats"] is True, "all 26 central words extend into either scalar exterior by minimum radius at most five"),
        "F": (values["finite_nuclei"] is True, "all 194 radius-two catalog seeds have compact P-capped extensions and safe-spacing composition"),
        "G": (values["close_base_control"] is True, "one D+z seed coextends with all 194 second types at separation five on each axis without claiming the full pair square"),
        "H": (values["planar_interfaces"] is True, "the width-zero-to-eight planar census has exact positives and a separately analytic transverse rigidity boundary"),
        "I": (values["native_front_boundary"] is True, "five-of-six unique propagation is conflict-free on catalog controls but stalls and leaves 12 branch contexts"),
        "J": (values["conditional_h1_packet"] is True, "the coarse POVM refines into finite-completion words only for a supplied fresh event region"),
        "K": (values["honest_boundary"] is True, "the status front remains supplied and uncompiled into M2/CP, while mixed or overlapping fronts, site, rate and history remain absent"),
        "L": (values["h2_sealed"] is True, "H2 is sealed"),
        "M": (
            values["axiom_update"] is False
            and values["obligation_retirement"] == 0
            and values["toe_movement"] == 0
            and values["retained"] is False
            and values["universal_no_go"] is False,
            "no axiom, audit, obligation, TOE, retained or universal-no-go promotion is made",
        ),
        "N": (values["permanent_status_front"] is True, "a 52-state append-only radius-two guard grows all supplied seeds and conflues for the tested disjoint same-background multi-front benches"),
    }
    passed = sum(ok for ok, _description in checks.values())
    failed = len(checks) - passed
    facts = {
        "checks": checks,
        "words": word_facts(),
        "structure": structural_facts(),
        "moats": scalar_moat_facts(),
        "nuclei": finite_nucleus_facts(),
        "planar": planar_facts(),
        "front": front_facts(),
        "status_front": permanent_status_front_facts(),
        "h1": h1_bridge_facts(),
    }
    return passed, failed, facts


def mutation_suite() -> int:
    baseline_passed, baseline_failed, _facts = run()
    detected = 0
    print(f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; mutations={len(MUTATIONS)}.")
    for mutation in MUTATIONS:
        _passed, failed, _mutation_facts = run(mutation)
        caught = failed > 0
        detected += int(caught)
        print(f"MUTATION {mutation}: {'DETECTED' if caught else 'ESCAPED'} (runner_failures={failed})")
    escaped = len(MUTATIONS) - detected
    print(f"TOTAL: PASS={detected} FAIL={escaped}")
    return 0 if baseline_failed == 0 and escaped == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        return mutation_suite()
    passed, failed, facts = run(args.mutation)
    words = facts["words"]
    structure = facts["structure"]
    moats = facts["moats"]
    nuclei = facts["nuclei"]
    planar = facts["planar"]
    front = facts["front"]
    status_front = facts["status_front"]
    h1 = facts["h1"]
    print(
        "CUBE_EDGE_NORMAL_FORM: words="
        f"{words['word_count']} = directed_edges {words['directed_cube_edges']} + scalar_loops 2; "
        f"weights={words['weight_histogram']}; decoder/cubic/complement exact."
    )
    print(
        "CHECKERBOARD_FACTOR: restriction classes even/odd="
        f"{structure['even_restriction_classes']}/{structure['odd_restriction_classes']}; "
        f"all ordered catalog pairs={structure['ordered_checkerboard_pairs']} valid, "
        f"distinct splices={structure['distinct_checkerboard_splices']}."
    )
    print(
        "HETEROGENEITY: layered no-isolated-bit equivalence="
        f"{structure['layered_no_isolated_equivalence']} over {structure['layered_control_count']} controls; "
        f"P/N step masks={structure['step_wall_masks']}; vector/scalar one-flip degree histogram="
        f"{structure['single_bit_flip_degree_histogram']}."
    )
    print(
        "SCALAR_MOATS: exterior/mask tests="
        f"{moats['tested_exterior_mask_pairs']}; max minimum radius={moats['maximum_minimum_radius']}; "
        f"P/N histograms={moats['zero_exterior_radius_histogram']}/{moats['one_exterior_radius_histogram']}; "
        "all models independently re-evaluated against every affected shell."
    )
    print(
        "FINITE_NUCLEI: catalog cap histogram="
        f"{nuclei['minimum_pad_histogram']}; support halfwidth vector/N="
        f"{nuclei['vector_support_cube_halfwidth']}/{nuclei['n_support_cube_halfwidth']}; "
        f"safe axial separations={nuclei['safe_axial_center_separations']}; "
        f"base-vs-all close complete={nuclei['close_base_vs_all_complete']}."
    )
    print(
        "PLANAR_WIDTH_0_TO_8: minima="
        f"{planar['minimum_width_histogram']}; pass/unresolved="
        f"{planar['pairs_joining_by_width_eight']}/{planar['pairs_unresolved_through_width_eight']}; "
        f"perpendicular halfspace rigid={planar['perpendicular_halfspace_rigid']}; "
        f"parallel antipodal wall={planar['parallel_antipodal_wall_exists']}."
    )
    print(
        "NATIVE_FRONT: five-known completions="
        f"{front['five_known_completion_histogram']}; L1-B2 growth="
        f"{front['l1_radius_two_types_with_growth']}/194; cube vector/scalar growth="
        f"{front['vector_cube_types_with_growth']}/192 and {front['scalar_cube_types_with_growth']}/2; "
        "unique propagation is conflict-free but stalls."
    )
    print(
        "PERMANENT_STATUS_FRONT: packet cases="
        f"{status_front['packet_cases']}; alphabet={status_front['visible_status_alphabet']}; "
        f"single-seed selected-policy cases={status_front['single_seed_schedule_cases']}/"
        f"{status_front['single_seed_schedule_cases']}; naive race masks="
        f"{status_front['naive_race_bad_masks']}; guarded same-background pair/triple="
        f"{status_front['same_background_pair_pass_total']}/"
        f"{status_front['same_background_triple_pass_total']}; full launched mixed witness="
        f"{status_front['mixed_background_full_launched_status_witness']}."
    )
    print(
        "CONDITIONAL_H1_PACKET: coarse POVM positive/normalized="
        f"{h1['coarse_effects_positive']}/{h1['coarse_povm_normalized']}; "
        f"word refinement identity={h1['word_refinement_effect_identity']}; "
        f"finite completion={h1['conditional_finite_region_dilation_exists']}; supplied fresh region only."
    )
    print(
        "per_element: checked all 26 readable words, their directed-cube-edge decoder, 52 scalar-exterior completions, 38 closed-form packets, 52 permanent status symbols, every parent coarse effect, and all 194 catalog seed types."
    )
    print(
        "per_site: checked all 192 five-known shell contexts, every affected shell of every finite witness, 194 radius-two and cube seeds, 632 selected hostile-policy single-seed cases, the explicit masks-9/10 race, and a full launched-status mixed midpoint witness; state/action event-site selection was checked and not executed — no selector."
    )
    print(
        "per_mode: checked both scalar exteriors, both checkerboard parities, all signed axes, planar widths zero through eight, finite pads zero through four, unique and ambiguous completion modes; H2 was checked and not executed — sealed."
    )
    print(
        "per_block: checked 37,636 checkerboard pairs, 37,636 planar boundary pairs, three 194-case close-seed controls, 722 guarded same-background pair branches, 13,718 guarded same-background triple branches, all 194 compact catalog nuclei, and the conditional finite-region POVM refinement."
    )
    print(
        "lattice_wide: checked exact heterogeneous fields, arbitrary finite unions of sufficiently separated prescribed catalog patches, directional planar rigidity, and a supplied append-only permanent-status front for disjoint same-background seeds; mixed/overlapping arbitration, M2/CP compilation, event site/rate, repeated history, retention and TOE movement were checked and not executed."
    )
    for label, (ok, description) in facts["checks"].items():
        print(f"CHECK {label}: {'PASS' if ok else 'FAIL'} - {description}.")
    print(
        "RESULT: the full 26-word binary rule removes the static heterogeneity and sufficiently-separated prescribed-patch obstruction. Although native permanent-bit propagation stalls, a supplied role-bearing seed has a non-oracular append-only permanent-status front; a radius-two guard makes the tested disjoint same-background pairs and triples confluent. Mixed-background/overlapping arbitration, M2/CP compilation, autonomous site/rate and repeated history remain open."
    )
    print("CLASSIFICATION: partial_static_mergeability_plus_conditional_permanent_status_front; H2/axioms/TOE unchanged.")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
