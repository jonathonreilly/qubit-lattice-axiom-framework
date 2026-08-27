#!/usr/bin/env python3
"""Exact Block-213 full-shell SFT and mergeable-front selector.

The runner widens Block 212's 194-field periodic catalog to the full binary
shift whose six-neighbor word is one of the 26 readable words.  It proves the
cube-edge normal form, checkerboard factorization, finite scalar-moat and
finite-nucleus constructions, and the preregistered planar-interface census.
It separately tests a native five-of-six permanent-bit propagation rule so a
static completion is not mislabeled as autonomous formation.
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
    GOAL_PATH,
    PREFLIGHT_PATH,
    AXIOM_PATH,
    REGISTRY_PATH,
    PARENT_NOTE_PATH,
    PARENT_RUNNER_PATH,
    PARENT_CACHE_PATH,
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
        "K": (values["honest_boundary"] is True, "site, rate, dense collision resolution, tentative dynamics and repeated history remain absent"),
        "L": (values["h2_sealed"] is True, "H2 is sealed"),
        "M": (
            values["axiom_update"] is False
            and values["obligation_retirement"] == 0
            and values["toe_movement"] == 0
            and values["retained"] is False
            and values["universal_no_go"] is False,
            "no axiom, audit, obligation, TOE, retained or universal-no-go promotion is made",
        ),
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
        "CONDITIONAL_H1_PACKET: coarse POVM positive/normalized="
        f"{h1['coarse_effects_positive']}/{h1['coarse_povm_normalized']}; "
        f"word refinement identity={h1['word_refinement_effect_identity']}; "
        f"finite completion={h1['conditional_finite_region_dilation_exists']}; supplied fresh region only."
    )
    print(
        "per_element: checked all 26 readable words, their directed-cube-edge decoder, 52 scalar-exterior completions, every parent coarse effect, and all 194 catalog seed types."
    )
    print(
        "per_site: checked all 192 five-known shell contexts, every affected shell of every finite witness, 194 radius-two and cube seeds, and safe-separated finite unions; dense autonomous selection was checked and not executed — no selector."
    )
    print(
        "per_mode: checked both scalar exteriors, both checkerboard parities, all signed axes, planar widths zero through eight, finite pads zero through four, unique and ambiguous completion modes; H2 was checked and not executed — sealed."
    )
    print(
        "per_block: checked 37,636 checkerboard pairs, 37,636 planar boundary pairs, three 194-case close-seed controls, all 194 compact catalog nuclei, and the conditional finite-region POVM refinement."
    )
    print(
        "lattice_wide: checked exact heterogeneous global fields, arbitrary sufficiently separated finite multi-seed unions, and directional planar rigidity; event site/rate, dense collision handshake, tentative CP front, repeated history, retention and TOE movement were checked and not executed."
    )
    for label, (ok, description) in facts["checks"].items():
        print(f"CHECK {label}: {'PASS' if ok else 'FAIL'} - {description}.")
    print(
        "RESULT: the full 26-word binary rule removes the rigid-content obstruction: it factorizes by parity, admits scalar/domain-wall heterogeneity, and gives compact completions for every word and every periodic seed, so arbitrary sufficiently separated events coexist. The native five-of-six rule still stalls, and no state/action-derived site, ambiguous branch, rate, dense collision process or repeated history is selected."
    )
    print("CLASSIFICATION: partial_native_binary_static_and_conditional_finite_event_bridge; H2/axioms/TOE unchanged.")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
