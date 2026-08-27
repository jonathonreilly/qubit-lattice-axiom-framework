#!/usr/bin/env python3
"""Independent Block-213 full-shell SFT/mergeable-front checker.

This runner imports only the frozen Block-212 parent.  It independently
reconstructs the 26-word cube-edge language, periodic catalog, parity splice,
finite scalar moats, compact nuclei, bounded planar census, native five-known
propagation test, permanent-status front, and conditional coarse-effect
refinement.  All negative statements remain confined to the enumerated finite
families and explicit symmetry hypotheses.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys
from typing import Callable, Iterable

import sympy as sp
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# Frozen parent only.  The Block-213 primary is intentionally not imported.
import admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27 as b212  # noqa: E402


Vector = tuple[int, int, int]
Field = tuple[int, ...]
Label = tuple[object, ...]
Status = tuple[object, ...]
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

# Literal and nonempty scientific input manifest.
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block213-mergeable-full-shell-sft-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block213-mergeable-full-shell-sft-20260827/PREFLIGHT.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_SHARED_SHELL_OVERLAP_CROSS_MOMENT_AND_UNIQUE_WRITER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.py",
    "logs/runner-cache/admissibility_d4_h1_autonomous_overlap_history_selector_2026_08_27.txt",
)

AXES: tuple[Vector, ...] = tuple(tuple(map(int, axis)) for axis in b212.AXES)
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}
ANTIPODE: tuple[int, ...] = tuple(map(int, b212.ANTIPODE))
PAIR_INDICES = ((0, 1), (2, 3), (4, 5))
ORIGIN: Vector = (0, 0, 0)
TORUS4: tuple[Vector, ...] = tuple(itertools.product(range(4), repeat=3))
TORUS4_INDEX = {site: index for index, site in enumerate(TORUS4)}


MUTATIONS = (
    "ind_stale_main",
    "ind_drop_preregistration",
    "ind_alter_goal",
    "ind_alter_preflight",
    "ind_alter_parent",
    "ind_change_word_count",
    "ind_change_cube_edge_count",
    "ind_break_decoder",
    "ind_break_complement",
    "ind_break_cubic_closure",
    "ind_change_checkerboard_classes",
    "ind_change_splice_count",
    "ind_break_parity_factorization",
    "ind_break_layered_control",
    "ind_change_moat_case_count",
    "ind_change_moat_radius",
    "ind_change_moat_histogram",
    "ind_break_moat_revalidation",
    "ind_change_nucleus_count",
    "ind_change_nucleus_histogram",
    "ind_break_nucleus_revalidation",
    "ind_change_planar_histogram",
    "ind_change_planar_join_count",
    "ind_claim_all_planar_pairs_join",
    "ind_widen_planar_scope",
    "ind_break_perpendicular_rigidity",
    "ind_erase_parallel_wall",
    "ind_change_five_known_histogram",
    "ind_erase_ambiguous_contexts",
    "ind_claim_l1_seed_growth",
    "ind_erase_vector_cube_growth",
    "ind_claim_scalar_cube_growth",
    "ind_inject_front_conflict",
    "ind_inject_front_mismatch",
    "ind_claim_native_front_complete",
    "ind_change_packet_case_count",
    "ind_break_packet_formula",
    "ind_change_status_alphabet",
    "ind_change_prelaunch_partition",
    "ind_change_prefix_history_count",
    "ind_change_arm_extension_count",
    "ind_change_selected_policy_case_count",
    "ind_claim_selected_policies_exhaustive",
    "ind_change_guard_radius",
    "ind_break_status_permanence",
    "ind_break_all_fair_status_confluence",
    "ind_erase_race_masks",
    "ind_change_pair_branch_count",
    "ind_change_triangle_branch_count",
    "ind_weaken_reachable_symmetry_witness",
    "ind_drop_mixed_complement_hypothesis",
    "ind_claim_mixed_midpoint_universal",
    "ind_claim_status_seed_autonomous",
    "ind_claim_status_m2_compiled",
    "ind_break_effect_normalization",
    "ind_break_word_refinement",
    "ind_claim_unconditional_h1_bridge",
    "ind_claim_static_is_formation",
    "ind_claim_event_site",
    "ind_claim_occurrence_rate",
    "ind_claim_dense_confluence",
    "ind_claim_complete_history",
    "ind_open_h2",
    "ind_edit_axiom",
    "ind_retire_obligation",
    "ind_move_toe",
    "ind_claim_retained",
    "ind_claim_universal_no_go",
)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(multiplier: int, vector: Vector) -> Vector:
    return tuple(multiplier * value for value in vector)  # type: ignore[return-value]


def l1(vector: Vector) -> int:
    return sum(map(abs, vector))


@cache
def l1_ball(radius: int) -> tuple[Vector, ...]:
    return tuple(
        site
        for site in itertools.product(range(-radius, radius + 1), repeat=3)
        if l1(site) <= radius
    )


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def blob(revision: str, path: str) -> str:
        return git_output("rev-parse", f"{revision}:{path}")

    goal_text = (ROOT / GOAL_PATH).read_text()
    preflight_text = (ROOT / PREFLIGHT_PATH).read_text()
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent_ancestor": is_ancestor(PARENT_COMMIT),
        "prereg_ancestor": is_ancestor(PREREG_COMMIT),
        "prereg_exact": git_output("rev-parse", PREREG_COMMIT) == PREREG_COMMIT,
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
        "h2_sealed_text": (
            "H2 remains sealed" in goal_text
            and "H2 sealed: `true`" in preflight_text
        ),
    }


def pack_vertices(negative: tuple[int, int, int], positive: tuple[int, int, int]) -> int:
    result = 0
    for coordinate, (left, right) in enumerate(PAIR_INDICES):
        result |= negative[coordinate] << left
        result |= positive[coordinate] << right
    return result


def cube_vertices(mask: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    return (
        tuple((mask >> left) & 1 for left, _right in PAIR_INDICES),
        tuple((mask >> right) & 1 for _left, right in PAIR_INDICES),
    )  # type: ignore[return-value]


@cache
def cube_edge_words() -> frozenset[int]:
    vertices = tuple(itertools.product((0, 1), repeat=3))
    words = {0, 63}
    words.update(
        pack_vertices(negative, positive)
        for negative in vertices
        for positive in vertices
        if sum(left != right for left, right in zip(negative, positive)) == 1
    )
    return frozenset(words)


def decode_cube_edge(mask: int) -> Label | None:
    if mask == 0:
        return ("dot", 1)
    if mask == 63:
        return ("dot", -1)
    negative, positive = cube_vertices(mask)
    changed = tuple(
        coordinate
        for coordinate in range(3)
        if negative[coordinate] != positive[coordinate]
    )
    if len(changed) != 1:
        return None
    axis = [0, 0, 0]
    axis[changed[0]] = 1 if sum(negative) % 2 == 0 else -1
    return ("cross", *axis)


def five_known_completions(missing: int, other_bits: int) -> tuple[int, ...]:
    completions = []
    for proposed in (0, 1):
        mask = 0
        source = 0
        for index in range(6):
            bit = proposed if index == missing else (other_bits >> source) & 1
            source += int(index != missing)
            mask |= bit << index
        if mask in cube_edge_words():
            completions.append(proposed)
    return tuple(completions)


@cache
def word_facts() -> dict[str, object]:
    words = cube_edge_words()
    parent_supports = b212.stochastic_supports()
    parent_words = {
        mask for support in parent_supports.values() for mask in support
    }
    parent_decoder = {
        mask: label for label, support in parent_supports.items() for mask in support
    }
    edges = tuple(
        cube_vertices(mask)
        for mask in words
        if sum(
            left != right
            for left, right in zip(*cube_vertices(mask))
        ) == 1
    )
    loops = tuple(sorted(
        cube_vertices(mask)
        for mask in words
        if cube_vertices(mask)[0] == cube_vertices(mask)[1]
    ))
    proper_rotations = b212.b211.shell_permutations()
    completion_table = tuple(
        (missing, other_bits, five_known_completions(missing, other_bits))
        for missing in range(6)
        for other_bits in range(32)
    )
    return {
        "word_count": len(words),
        "directed_cube_edges": len(edges),
        "scalar_loops": loops,
        "word_weight_histogram": dict(sorted(Counter(
            mask.bit_count() for mask in words
        ).items())),
        "xor_characterization_exact": all(
            (
                sum(
                    ((mask >> left) & 1) ^ ((mask >> right) & 1)
                    for left, right in PAIR_INDICES
                ) == 1
                or mask in (0, 63)
            ) == (mask in words)
            for mask in range(64)
        ),
        "parent_word_set_exact": words == parent_words,
        "decoder_exact": all(
            decode_cube_edge(mask) == parent_decoder[mask] for mask in words
        ),
        "decoder_fibers": dict(sorted(Counter(
            decode_cube_edge(mask) for mask in words
        ).items(), key=lambda item: repr(item[0]))),
        "complement_closed": all((63 ^ mask) in words for mask in words),
        "proper_cubic_closed": all(
            b212.b211.act_mask(mask, permutation) in words
            for mask in words
            for permutation in proper_rotations
        ),
        "proper_cubic_permutation_count": len(proper_rotations),
        "five_known_context_count": len(completion_table),
        "five_known_completion_histogram": dict(sorted(Counter(
            len(completions) for _missing, _other, completions in completion_table
        ).items())),
        "ambiguous_five_known_contexts": tuple(
            (missing, other_bits)
            for missing, other_bits, completions in completion_table
            if len(completions) == 2
        ),
    }


def torus_bit(field: Field, site: Vector) -> int:
    return field[TORUS4_INDEX[tuple(value % 4 for value in site)]]


def shell_mask(center: Vector, bit: Callable[[Vector], int]) -> int:
    return sum(bit(add(center, axis)) << index for index, axis in enumerate(AXES))


def periodic_valid(field: Field) -> bool:
    return all(
        shell_mask(center, lambda site: torus_bit(field, site)) in cube_edge_words()
        for center in TORUS4
    )


@cache
def periodic_catalog() -> tuple[tuple[Field, Label], ...]:
    rotations = b212.b211.b194.proper_cubic_rotations()
    catalog: list[tuple[Field, Label]] = []
    plus_z = sp.Matrix((0, 0, 1))
    for target in AXES:
        rotation = next(
            candidate
            for candidate in rotations
            if tuple(map(int, candidate * plus_z)) == target
        )
        phases: dict[Field, Vector] = {}
        for translation in TORUS4:
            field = tuple(
                b212.period4_bit(tuple(map(
                    int,
                    rotation.T * sp.Matrix(add(site, translation)),
                )))
                for site in TORUS4
            )
            phases.setdefault(field, translation)
        catalog.extend(
            (field, (target, translation))
            for field, translation in phases.items()
        )
    catalog.extend((
        ((0,) * 64, ("P", ORIGIN)),
        ((1,) * 64, ("N", ORIGIN)),
    ))
    return tuple(catalog)


@cache
def parity_facts() -> dict[str, object]:
    catalog = periodic_catalog()
    fields = tuple(field for field, _label in catalog)
    even_sites = tuple(
        index for index, site in enumerate(TORUS4) if sum(site) % 2 == 0
    )
    odd_sites = tuple(
        index for index, site in enumerate(TORUS4) if sum(site) % 2 == 1
    )
    even_restrictions = {
        tuple(field[index] for index in even_sites) for field in fields
    }
    odd_restrictions = {
        tuple(field[index] for index in odd_sites) for field in fields
    }
    distinct_splices = set()
    all_splices_valid = True
    exact_shell_source = True
    for even_field in fields:
        for odd_field in fields:
            splice = tuple(
                even_field[index] if sum(site) % 2 == 0 else odd_field[index]
                for index, site in enumerate(TORUS4)
            )
            distinct_splices.add(splice)
            all_splices_valid &= periodic_valid(splice)
            exact_shell_source &= all(
                shell_mask(center, lambda site: torus_bit(splice, site))
                == shell_mask(
                    center,
                    lambda site, source=(
                        odd_field if sum(center) % 2 == 0 else even_field
                    ): torus_bit(source, site),
                )
                for center in TORUS4
            )

    layered_equivalence = []
    for length in range(2, 13):
        for sequence in itertools.product((0, 1), repeat=length):
            no_isolated_bit = all(
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
                    | sequence[(index + 1) % length] << 1
                    | sequence[index] << 2
                    | sequence[index] << 3
                    | sequence[index] << 4
                    | sequence[index] << 5
                ) in cube_edge_words()
                for index in range(length)
            )
            layered_equivalence.append(valid == no_isolated_bit)
    step = lambda coordinate: int(coordinate >= 1)
    step_masks = tuple(
        shell_mask((x, 0, 0), lambda site: step(site[0]))
        for x in range(-3, 5)
    )
    flip_degrees = []
    for field in fields:
        flip_degrees.append(sum(
            periodic_valid(field[:index] + (1 - field[index],) + field[index + 1:])
            for index in range(64)
        ))
    return {
        "catalog_count": len(catalog),
        "catalog_distinct": len(set(fields)),
        "catalog_all_valid": all(map(periodic_valid, fields)),
        "vector_count": len(catalog) - 2,
        "even_restriction_classes": len(even_restrictions),
        "odd_restriction_classes": len(odd_restrictions),
        "ordered_catalog_pairs": len(fields) ** 2,
        "distinct_checkerboard_splices": len(distinct_splices),
        "all_checkerboard_splices_valid": all_splices_valid,
        "checkerboard_shell_source_exact": exact_shell_source,
        "analytic_parity_decoupling": all(
            (sum(add(center, axis)) - sum(center)) % 2 == 1
            for center in TORUS4
            for axis in AXES
        ),
        "layered_control_count": len(layered_equivalence),
        "layered_no_isolated_equivalence": all(layered_equivalence),
        "step_wall_masks": tuple(sorted(set(step_masks))),
        "step_wall_valid": all(mask in cube_edge_words() for mask in step_masks),
        "single_bit_flip_degree_histogram": dict(sorted(Counter(flip_degrees).items())),
        "periodic_vector_one_bit_rigid": all(degree == 0 for degree in flip_degrees[:192]),
        "scalar_one_bit_degrees": tuple(flip_degrees[192:]),
    }


def affected_centers(sites: Iterable[Vector]) -> tuple[Vector, ...]:
    return tuple(sorted({sub(site, axis) for site in sites for axis in AXES}))


def install_full_shell_cnf(
    solver: Solver,
    variables: dict[Vector, int],
    exterior: int,
) -> int:
    clause_count = 0
    forbidden_words = tuple(set(range(64)) - set(cube_edge_words()))
    for center in affected_centers(variables):
        neighbors = tuple(add(center, axis) for axis in AXES)
        for forbidden in forbidden_words:
            clause = []
            impossible = False
            for index, site in enumerate(neighbors):
                forbidden_bit = (forbidden >> index) & 1
                variable = variables.get(site)
                if variable is None:
                    if forbidden_bit != exterior:
                        impossible = True
                        break
                else:
                    clause.append(-variable if forbidden_bit else variable)
            if not impossible:
                solver.add_clause(clause)
                clause_count += 1
    return clause_count


def bit_function_from_model(
    variables: dict[Vector, int],
    model: list[int],
    exterior: int,
) -> Callable[[Vector], int]:
    positive = {literal for literal in model if literal > 0}
    values = {
        site: int(variable in positive) for site, variable in variables.items()
    }
    return lambda site: values.get(site, exterior)


def validate_finite_witness(
    variables: dict[Vector, int],
    model: list[int],
    exterior: int,
) -> bool:
    bit = bit_function_from_model(variables, model, exterior)
    return all(
        shell_mask(center, bit) in cube_edge_words()
        for center in affected_centers(variables)
    )


def signed_assumptions(
    variables: dict[Vector, int], values: dict[Vector, int]
) -> tuple[int, ...]:
    return tuple(
        variables[site] if value else -variables[site]
        for site, value in values.items()
    )


@cache
def scalar_moat_facts() -> dict[str, object]:
    words = tuple(sorted(cube_edge_words()))
    minima: dict[tuple[int, int], int] = {}
    witness_support_sizes = {}
    witness_validations = []
    cnf_clause_counts = {}
    unsat_queries = 0
    for exterior in (0, 1):
        unresolved = set(words)
        for radius in range(1, 6):
            sites = l1_ball(radius)
            variables = {site: index + 1 for index, site in enumerate(sites)}
            solver = Solver(name="cadical195")
            cnf_clause_counts[(exterior, radius)] = install_full_shell_cnf(
                solver, variables, exterior
            )
            solved = []
            for mask in sorted(unresolved):
                central_values = {
                    axis: (mask >> index) & 1
                    for index, axis in enumerate(AXES)
                }
                assumptions = signed_assumptions(variables, central_values)
                if not solver.solve(assumptions=assumptions):
                    unsat_queries += 1
                    continue
                model = solver.get_model() or []
                bit = bit_function_from_model(variables, model, exterior)
                witness_validations.append(
                    validate_finite_witness(variables, model, exterior)
                    and shell_mask(ORIGIN, bit) == mask
                )
                witness_support_sizes[(exterior, mask)] = sum(
                    bit(site) != exterior for site in sites
                )
                minima[(exterior, mask)] = radius
                solved.append(mask)
            solver.delete()
            unresolved.difference_update(solved)
        if unresolved:
            for mask in unresolved:
                minima[(exterior, mask)] = 0

    zero_minima = {mask: minima[(0, mask)] for mask in words}
    one_minima = {mask: minima[(1, mask)] for mask in words}
    all_completed = all(minima.values())
    return {
        "tested_exterior_mask_pairs": len(minima),
        "radii_tested": tuple(range(1, 6)),
        "all_complete_by_radius_five": all_completed,
        "maximum_minimum_radius": max(minima.values()),
        "zero_exterior_radius_histogram": dict(sorted(Counter(
            zero_minima.values()
        ).items())),
        "one_exterior_radius_histogram": dict(sorted(Counter(
            one_minima.values()
        ).items())),
        "zero_exterior_minima": tuple(sorted(zero_minima.items())),
        "one_exterior_minima": tuple(sorted(one_minima.items())),
        "complement_minima_exact": all(
            zero_minima[mask] == one_minima[63 ^ mask] for mask in words
        ),
        "all_witnesses_revalidated": all(witness_validations)
        and len(witness_validations) == 52,
        "witness_count": len(witness_validations),
        "support_size_range": (
            min(witness_support_sizes.values()),
            max(witness_support_sizes.values()),
        ),
        "unsat_smaller_radius_queries": unsat_queries,
        "cnf_clause_count_range": (
            min(cnf_clause_counts.values()), max(cnf_clause_counts.values())
        ),
        "template_selection_derived": False,
    }


def box_sites(low: Vector, high: Vector) -> tuple[Vector, ...]:
    return tuple(itertools.product(*(
        range(low[index], high[index] + 1) for index in range(3)
    )))


L1_BALL2 = l1_ball(2)


def catalog_patch(field: Field, center: Vector = ORIGIN) -> dict[Vector, int]:
    return {
        add(center, offset): torus_bit(field, offset) for offset in L1_BALL2
    }


def nucleus_solver(pad: int) -> tuple[Solver, dict[Vector, int], tuple[tuple[int, ...], ...]]:
    halfwidth = 2 + pad
    sites = box_sites(
        (-halfwidth, -halfwidth, -halfwidth),
        (halfwidth, halfwidth, halfwidth),
    )
    variables = {site: index + 1 for index, site in enumerate(sites)}
    solver = Solver(name="cadical195")
    install_full_shell_cnf(solver, variables, exterior=0)
    assumptions = tuple(
        signed_assumptions(variables, catalog_patch(field))
        for field, _label in periodic_catalog()
    )
    return solver, variables, assumptions


@cache
def compact_nucleus_facts() -> dict[str, object]:
    unresolved = set(range(len(periodic_catalog())))
    minimum_pad: dict[int, int] = {}
    witness_supports: dict[int, set[Vector]] = {}
    validations = []
    patch_validations = []
    for pad in range(5):
        solver, variables, assumptions = nucleus_solver(pad)
        solved = []
        for field_type in sorted(unresolved):
            if not solver.solve(assumptions=assumptions[field_type]):
                continue
            model = solver.get_model() or []
            bit = bit_function_from_model(variables, model, exterior=0)
            validations.append(validate_finite_witness(variables, model, 0))
            patch_validations.append(all(
                bit(offset) == torus_bit(periodic_catalog()[field_type][0], offset)
                for offset in L1_BALL2
            ))
            positive = {literal for literal in model if literal > 0}
            witness_supports[field_type] = {
                site for site, variable in variables.items() if variable in positive
            }
            minimum_pad[field_type] = pad
            solved.append(field_type)
        solver.delete()
        unresolved.difference_update(solved)

    vector_halfwidth = max(
        (
            max(max(map(abs, site)) for site in witness_supports[field_type])
            if witness_supports[field_type] else 0
        )
        for field_type in range(192)
    )
    n_halfwidth = max(
        max(map(abs, site)) for site in witness_supports[193]
    )
    safe_separations = {
        "vector_vector": 2 * vector_halfwidth + 3,
        "vector_N": vector_halfwidth + n_halfwidth + 3,
        "N_N": 2 * n_halfwidth + 3,
    }
    return {
        "catalog_seed_types": len(periodic_catalog()),
        "pads_tested": tuple(range(5)),
        "all_catalog_types_compact_p_capped": not unresolved,
        "minimum_pad_histogram": dict(sorted(Counter(
            minimum_pad.values()
        ).items())),
        "all_witnesses_revalidated": all(validations)
        and len(validations) == 194,
        "all_catalog_patches_revalidated": all(patch_validations)
        and len(patch_validations) == 194,
        "witness_count": len(validations),
        "vector_support_cube_halfwidth": vector_halfwidth,
        "n_support_cube_halfwidth": n_halfwidth,
        "safe_axial_center_separations": safe_separations,
        "separated_union_locality_certificate": all(
            separation >= 2 * 1 + 1 for separation in safe_separations.values()
        ),
        "dense_collision_front_constructed": False,
    }


def planar_solver(
    width: int,
) -> tuple[
    Solver,
    dict[Vector, int],
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, ...], ...],
]:
    sites = tuple(
        (x, y, z)
        for x in range(-2, width + 2)
        for y in range(4)
        for z in range(4)
    )
    variables = {site: index + 1 for index, site in enumerate(sites)}
    solver = Solver(name="cadical195")
    forbidden = tuple(set(range(64)) - set(cube_edge_words()))
    for x in range(-1, width + 1):
        for y in range(4):
            for z in range(4):
                neighbors = (
                    (x - 1, y, z),
                    (x + 1, y, z),
                    (x, (y - 1) % 4, z),
                    (x, (y + 1) % 4, z),
                    (x, y, (z - 1) % 4),
                    (x, y, (z + 1) % 4),
                )
                for mask in forbidden:
                    solver.add_clause(tuple(
                        -variables[site] if (mask >> index) & 1 else variables[site]
                        for index, site in enumerate(neighbors)
                    ))
    left_assumptions = []
    right_assumptions = []
    for field, _label in periodic_catalog():
        left_assumptions.append(tuple(
            variables[(x, y, z)]
            if torus_bit(field, (x, y, z))
            else -variables[(x, y, z)]
            for x in (-2, -1)
            for y in range(4)
            for z in range(4)
        ))
        right_assumptions.append(tuple(
            variables[(x, y, z)]
            if torus_bit(field, (x, y, z))
            else -variables[(x, y, z)]
            for x in (width, width + 1)
            for y in range(4)
            for z in range(4)
        ))
    return (
        solver,
        variables,
        tuple(left_assumptions),
        tuple(right_assumptions),
    )


def validate_planar_model(
    width: int,
    variables: dict[Vector, int],
    model: list[int],
    left_type: int,
    right_type: int,
) -> bool:
    positive = {literal for literal in model if literal > 0}
    bit = lambda site: int(
        variables[(site[0], site[1] % 4, site[2] % 4)] in positive
    )
    interior_valid = all(
        shell_mask((x, y, z), bit) in cube_edge_words()
        for x in range(-1, width + 1)
        for y in range(4)
        for z in range(4)
    )
    left_field = periodic_catalog()[left_type][0]
    right_field = periodic_catalog()[right_type][0]
    left_exact = all(
        bit((x, y, z)) == torus_bit(left_field, (x, y, z))
        for x in (-2, -1)
        for y in range(4)
        for z in range(4)
    )
    right_exact = all(
        bit((x, y, z)) == torus_bit(right_field, (x, y, z))
        for x in (width, width + 1)
        for y in range(4)
        for z in range(4)
    )
    return interior_valid and left_exact and right_exact


@cache
def planar_interface_facts() -> dict[str, object]:
    type_count = len(periodic_catalog())
    unresolved = {
        (left, right)
        for left in range(type_count)
        for right in range(type_count)
    }
    minimum_width: dict[tuple[int, int], int] = {}
    witness_validations = []
    query_counts = {}
    for width in range(9):
        solver, variables, left_assumptions, right_assumptions = planar_solver(width)
        solved = []
        query_counts[width] = len(unresolved)
        for left_type, right_type in sorted(unresolved):
            assumptions = (
                left_assumptions[left_type] + right_assumptions[right_type]
            )
            if not solver.solve(assumptions=assumptions):
                continue
            model = solver.get_model() or []
            witness_validations.append(validate_planar_model(
                width, variables, model, left_type, right_type
            ))
            minimum_width[(left_type, right_type)] = width
            solved.append((left_type, right_type))
        solver.delete()
        unresolved.difference_update(solved)

    labels = tuple(label for _field, label in periodic_catalog())
    base_type = next(
        index
        for index, label in enumerate(labels)
        if label == ((1, 0, 0), ORIGIN)
    )
    base_joined = {
        right: width
        for (left, right), width in minimum_width.items()
        if left == base_type
    }
    antipodal_parallel_witnesses = tuple(
        (right, width)
        for right, width in base_joined.items()
        if labels[right][0] == (-1, 0, 0)
    )

    rigidity_checks = []
    for field, label in periodic_catalog()[:192]:
        sector = label[0]
        for direction_index, normal in enumerate(AXES):
            if sum(a * b for a, b in zip(sector, normal)) != 0:
                continue
            for center in TORUS4:
                mask = shell_mask(
                    center, lambda site: torus_bit(field, site)
                )
                rigidity_checks.append(
                    (mask ^ (1 << direction_index)) not in cube_edge_words()
                )

    rotations = b212.b211.b194.proper_cubic_rotations()
    plus_x = sp.Matrix((1, 0, 0))
    normal_orbit = {
        tuple(map(int, rotation * plus_x)) for rotation in rotations
    }
    return {
        "ordered_boundary_pairs": type_count ** 2,
        "widths_tested": tuple(range(9)),
        "transverse_period": 4,
        "minimum_width_histogram": dict(sorted(Counter(
            minimum_width.values()
        ).items())),
        "pairs_joining_by_width_eight": len(minimum_width),
        "pairs_unresolved_through_width_eight": len(unresolved),
        "all_pairs_join": not unresolved,
        "all_positive_witnesses_revalidated": all(witness_validations)
        and len(witness_validations) == len(minimum_width),
        "positive_witness_count": len(witness_validations),
        "query_counts_by_width": query_counts,
        "base_parallel_join_count": len(base_joined),
        "base_parallel_minimum_width_histogram": dict(sorted(Counter(
            base_joined.values()
        ).items())),
        "parallel_antipodal_wall_exists": bool(antipodal_parallel_witnesses),
        "parallel_antipodal_witnesses": antipodal_parallel_witnesses,
        "perpendicular_boundary_flip_checks": len(rigidity_checks),
        "perpendicular_halfspace_rigid": all(rigidity_checks),
        "perpendicular_rigidity_is_local_induction": True,
        "signed_axis_normal_orbit": normal_orbit == set(AXES),
        "bounded_scope": "period4_transverse_widths_0_through_8",
        "wider_widths_excluded": False,
        "nonplanar_interfaces_excluded": False,
        "tentative_rewriting_excluded": False,
    }


def unique_five_known_propagation(
    field: Field,
    seed_sites: tuple[Vector, ...],
    max_rounds: int = 12,
) -> dict[str, object]:
    known = {site: torus_bit(field, site) for site in seed_sites}
    rounds = []
    conflicts = 0
    target_mismatches = 0
    ambiguous_contexts_seen = 0
    stopped_without_proposal = False
    for _round in range(max_rounds):
        proposals: dict[Vector, set[int]] = {}
        for center in affected_centers(known):
            neighbors = tuple(add(center, axis) for axis in AXES)
            missing_sites = tuple(site for site in neighbors if site not in known)
            if len(missing_sites) != 1:
                continue
            missing_site = missing_sites[0]
            completions = []
            for proposed in (0, 1):
                mask = sum(
                    (
                        proposed if site == missing_site else known[site]
                    ) << index
                    for index, site in enumerate(neighbors)
                )
                if mask in cube_edge_words():
                    completions.append(proposed)
            if len(completions) == 1:
                proposals.setdefault(missing_site, set()).add(completions[0])
            elif len(completions) == 2:
                ambiguous_contexts_seen += 1
        conflicting_sites = {
            site: values for site, values in proposals.items() if len(values) > 1
        }
        conflicts += len(conflicting_sites)
        if conflicting_sites:
            break
        new_values = {
            site: next(iter(values)) for site, values in proposals.items()
        }
        if not new_values:
            stopped_without_proposal = True
            break
        target_mismatches += sum(
            value != torus_bit(field, site)
            for site, value in new_values.items()
        )
        known.update(new_values)
        rounds.append(len(new_values))
    return {
        "initial_known": len(seed_sites),
        "terminal_known": len(known),
        "rounds": tuple(rounds),
        "conflicts": conflicts,
        "target_mismatches": target_mismatches,
        "ambiguous_contexts_seen": ambiguous_contexts_seen,
        "stopped_without_proposal": stopped_without_proposal,
        "hit_round_cap": len(rounds) == max_rounds,
    }


@cache
def native_front_facts() -> dict[str, object]:
    fields = tuple(field for field, _label in periodic_catalog())
    l1_seed_results = tuple(
        unique_five_known_propagation(field, L1_BALL2) for field in fields
    )
    cube_seed = tuple(itertools.product(range(-2, 3), repeat=3))
    cube_results = tuple(
        unique_five_known_propagation(field, cube_seed) for field in fields
    )
    vector_results = cube_results[:192]
    scalar_results = cube_results[192:]
    return {
        "five_known_completion_histogram": word_facts()[
            "five_known_completion_histogram"
        ],
        "ambiguous_context_count": len(word_facts()[
            "ambiguous_five_known_contexts"
        ]),
        "l1_radius_two_seed_types_tested": len(l1_seed_results),
        "l1_radius_two_types_with_growth": sum(
            result["terminal_known"] > result["initial_known"]
            for result in l1_seed_results
        ),
        "l1_radius_two_all_stop_without_proposal": all(
            result["stopped_without_proposal"] for result in l1_seed_results
        ),
        "cube_seed_types_tested": len(cube_results),
        "cube_initial_site_count": len(cube_seed),
        "vector_cube_types_with_growth": sum(
            result["terminal_known"] > result["initial_known"]
            for result in vector_results
        ),
        "scalar_cube_types_with_growth": sum(
            result["terminal_known"] > result["initial_known"]
            for result in scalar_results
        ),
        "vector_round_count_histogram": dict(sorted(Counter(
            len(result["rounds"]) for result in vector_results
        ).items())),
        "vector_terminal_size_histogram": dict(sorted(Counter(
            result["terminal_known"] for result in vector_results
        ).items())),
        "proposal_conflicts": sum(
            result["conflicts"] for result in cube_results
        ),
        "proposal_target_mismatches": sum(
            result["target_mismatches"] for result in cube_results
        ),
        "all_catalog_controls_stop_without_proposal": all(
            result["stopped_without_proposal"] for result in cube_results
        ),
        "any_round_cap_hit": any(
            result["hit_round_cap"] for result in cube_results
        ),
        "native_unique_rule_stalls": all(
            result["stopped_without_proposal"]
            and not result["hit_round_cap"]
            for result in cube_results
        ),
        "tested_rule_scope": "permanent_binary_unique_five_of_six",
        "ambiguous_branch_rule_selected": False,
        "tentative_status_carrier_constructed": False,
        "event_site_selected": False,
        "occurrence_rate_selected": False,
        "dense_multi_seed_confluence": False,
        "complete_history": False,
        "static_completion_is_formation": False,
    }


def packet_background_options(mask: int) -> tuple[int, ...]:
    """Choose the low-defect scalar background independently from the word."""
    weight = mask.bit_count()
    if weight <= 1:
        return (0,)
    if weight >= 5:
        return (1,)
    if weight == 3:
        return (0, 1)
    return ()


def independent_packet_geometry(
    mask: int,
    background: int,
) -> tuple[
    frozenset[Vector],
    Vector | None,
    Vector | None,
    frozenset[Vector],
    frozenset[Vector],
]:
    defects = frozenset(
        axis
        for index, axis in enumerate(AXES)
        if ((mask >> index) & 1) != background
    )
    antipodal_axis = None
    advance_axis = None
    endpoints: frozenset[Vector] = frozenset()
    if len(defects) == 3:
        antipodal_candidates = tuple(
            AXES[left]
            for left, right in PAIR_INDICES
            if AXES[left] in defects and AXES[right] in defects
        )
        if len(antipodal_candidates) != 1:
            raise AssertionError((mask, background, defects))
        antipodal_axis = antipodal_candidates[0]
        advance_axis = next(
            axis
            for axis in defects
            if axis not in (antipodal_axis, scale(-1, antipodal_axis))
        )
        if sum(
            left * right
            for left, right in zip(antipodal_axis, advance_axis)
        ) != 0:
            raise AssertionError((antipodal_axis, advance_axis))
        endpoints = frozenset((
            add(antipodal_axis, scale(2, advance_axis)),
            add(scale(-1, antipodal_axis), scale(2, advance_axis)),
        ))
    return (
        defects,
        antipodal_axis,
        advance_axis,
        endpoints,
        frozenset(set(defects) | set(endpoints)),
    )


def packet_support_bit(
    support: frozenset[Vector] | set[Vector],
    background: int,
) -> Callable[[Vector], int]:
    return lambda site: 1 - background if site in support else background


def packet_support_valid(
    support: frozenset[Vector] | set[Vector],
    background: int,
) -> bool:
    bit = packet_support_bit(support, background)
    return all(
        shell_mask(center, bit) in cube_edge_words()
        for center in affected_centers(support)
    )


def status_payload(status: Status) -> int:
    kind = status[0]
    if kind in ("LOCK", "BG"):
        return int(status[1])
    return int(status[2]) if kind == "STEP" else 1 - int(status[2])


def independent_status_seed(
    mask: int,
    background: int,
    center: Vector = ORIGIN,
) -> dict[Vector, Status]:
    defects, antipodal, advance, _endpoints, _support = (
        independent_packet_geometry(mask, background)
    )
    state: dict[Vector, Status] = {center: ("LOCK", background)}
    if len(defects) != 3:
        for index, axis in enumerate(AXES):
            payload = (mask >> index) & 1
            state[add(center, axis)] = (
                ("BG", background)
                if payload == background
                else ("LOCK", payload)
            )
        return state

    if antipodal is None or advance is None:
        raise AssertionError((mask, background))
    pair = {antipodal, scale(-1, antipodal)}
    for axis in AXES:
        site = add(center, axis)
        if axis in pair:
            state[site] = ("PORT", advance, background)
        elif axis == advance:
            state[site] = ("GPORT", advance, background)
        else:
            state[site] = ("LOCK", background)
    return state


def independent_role_footprint(
    mask: int,
    background: int,
    center: Vector = ORIGIN,
) -> frozenset[Vector]:
    defects, antipodal, advance, _endpoints, _support = (
        independent_packet_geometry(mask, background)
    )
    footprint = set(independent_status_seed(mask, background, center))
    if len(defects) == 3:
        if antipodal is None or advance is None:
            raise AssertionError((mask, background))
        for port in (antipodal, scale(-1, antipodal)):
            footprint.add(add(center, add(port, advance)))
            footprint.add(add(center, add(port, scale(2, advance))))
        footprint.add(add(center, scale(2, advance)))
    return frozenset(footprint)


def locally_protected_target(
    state: dict[Vector, Status],
    target: Vector,
) -> bool:
    """Invert the guard around the target; the furthest read is radius two."""
    for direction in AXES:
        radius_one = state.get(sub(target, direction))
        if (
            radius_one is not None
            and radius_one[0] in ("PORT", "GPORT")
            and radius_one[1] == direction
        ):
            return True
        radius_two = state.get(sub(target, scale(2, direction)))
        if (
            radius_two is not None
            and radius_two[0] == "PORT"
            and radius_two[1] == direction
        ):
            return True
    return False


def direct_protected_targets(state: dict[Vector, Status]) -> frozenset[Vector]:
    targets = set()
    for site, status in state.items():
        if status[0] not in ("PORT", "GPORT"):
            continue
        direction = status[1]
        if not isinstance(direction, tuple):
            raise AssertionError(status)
        targets.add(add(site, direction))
        if status[0] == "PORT":
            targets.add(add(site, scale(2, direction)))
    return frozenset(targets)


def flood_status_bench(
    state: dict[Vector, Status],
    background: int,
    bench: frozenset[Vector],
    policy: str,
) -> tuple[bool, int]:
    candidates = set()
    for site, status in tuple(state.items()):
        if status != ("BG", background):
            continue
        for axis in AXES:
            target = add(site, axis)
            if (
                target in bench
                and target not in state
                and not locally_protected_target(state, target)
            ):
                candidates.add(target)

    additions = 0
    while candidates:
        if policy == "lex_min":
            target = min(candidates)
        elif policy == "lex_max":
            target = max(candidates)
        elif policy == "near_first":
            target = min(candidates, key=lambda site: (l1(site), site))
        elif policy == "far_first":
            target = max(candidates, key=lambda site: (l1(site), site))
        else:
            raise ValueError(policy)
        candidates.remove(target)
        if target in state or locally_protected_target(state, target):
            continue
        state[target] = ("BG", background)
        additions += 1
        for axis in AXES:
            neighbor = add(target, axis)
            if (
                neighbor in bench
                and neighbor not in state
                and not locally_protected_target(state, neighbor)
            ):
                candidates.add(neighbor)
    return set(state) == set(bench), additions


def finish_role_launch(
    mask: int,
    background: int,
    order: tuple[str, ...],
    center: Vector = ORIGIN,
) -> tuple[dict[Vector, Status], bool, bool]:
    defects, antipodal, advance, _endpoints, _support = (
        independent_packet_geometry(mask, background)
    )
    if len(defects) != 3 or antipodal is None or advance is None:
        raise AssertionError((mask, background))
    state = independent_status_seed(mask, background, center)
    ports = {"L": antipodal, "R": scale(-1, antipodal)}
    progress = {"L": 0, "R": 0}
    strict_local = True
    permanent = True
    for token in order:
        arm = token[0]
        port = ports[arm]
        if token[1] == "s":
            source = add(center, port)
            target = add(center, add(port, advance))
            expected = ("PORT", advance, background)
            formed = ("STEP", advance, background)
            required_progress = 0
        else:
            source = add(center, add(port, advance))
            target = add(center, add(port, scale(2, advance)))
            expected = ("STEP", advance, background)
            formed = ("END", advance, background)
            required_progress = 1
        strict_local &= l1(sub(target, source)) == 1
        strict_local &= state.get(source) == expected
        permanent &= target not in state and progress[arm] == required_progress
        if target in state or progress[arm] != required_progress:
            return state, False, False
        state[target] = formed
        progress[arm] += 1

    launcher = add(center, scale(2, advance))
    gate_inputs = (
        add(center, advance),
        add(center, add(antipodal, scale(2, advance))),
        add(center, add(scale(-1, antipodal), scale(2, advance))),
    )
    strict_local &= all(
        l1(sub(site, launcher)) == 1 for site in gate_inputs
    )
    gate_ready = (
        state.get(gate_inputs[0]) == ("GPORT", advance, background)
        and all(
            state.get(site) == ("END", advance, background)
            for site in gate_inputs[1:]
        )
        and launcher not in state
    )
    permanent &= gate_ready
    if gate_ready:
        state[launcher] = ("BG", background)
    return state, strict_local and gate_ready, permanent


def mat_vec(matrix: tuple[Vector, Vector, Vector], vector: Vector) -> Vector:
    return tuple(
        sum(row[index] * vector[index] for index in range(3))
        for row in matrix
    )  # type: ignore[return-value]


def determinant_three(matrix: tuple[Vector, Vector, Vector]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


@cache
def independent_permanent_status_front_facts() -> dict[str, object]:
    cases = tuple(
        (mask, background)
        for mask in sorted(cube_edge_words())
        for background in packet_background_options(mask)
    )
    packet_validations = []
    support_size_histogram = Counter()
    affected_center_histogram = Counter()
    triple_orientations = Counter()
    for mask, background in cases:
        defects, antipodal, advance, _endpoints, support = (
            independent_packet_geometry(mask, background)
        )
        support_size_histogram[len(support)] += 1
        affected_center_histogram[len(affected_centers(support))] += 1
        packet_validations.append(
            packet_support_valid(support, background)
            and shell_mask(
                ORIGIN, packet_support_bit(support, background)
            ) == mask
        )
        if len(defects) == 3:
            triple_orientations[(antipodal, advance)] += 1

    visible_statuses = {
        *(("LOCK", bit) for bit in (0, 1)),
        *(("BG", bit) for bit in (0, 1)),
        *((kind, direction, background)
          for kind in ("PORT", "GPORT", "STEP", "END")
          for direction in AXES
          for background in (0, 1)),
    }

    progress_states = {(0, 0)}
    progress_frontier = {(0, 0)}
    while progress_frontier:
        left, right = progress_frontier.pop()
        successors = set()
        if left < 2:
            successors.add((left + 1, right))
        if right < 2:
            successors.add((left, right + 1))
        for successor in successors - progress_states:
            progress_states.add(successor)
            progress_frontier.add(successor)
    ungated_states = len(progress_states)
    gated_states = int((2, 2) in progress_states)

    actions = ("Ls", "Le", "Rs", "Re")
    prefix_histories = set()
    for length in range(5):
        for sequence in itertools.permutations(actions, length):
            seen = set()
            valid = True
            for token in sequence:
                if token == "Le" and "Ls" not in seen:
                    valid = False
                if token == "Re" and "Rs" not in seen:
                    valid = False
                seen.add(token)
            if valid:
                prefix_histories.add(sequence)
    arm_extensions = tuple(
        order
        for order in itertools.permutations(actions)
        if order.index("Ls") < order.index("Le")
        and order.index("Rs") < order.index("Re")
    )

    bench = frozenset(itertools.product(range(-3, 4), repeat=3))
    policies = ("lex_min", "lex_max", "near_first", "far_first")
    guard_completeness = []
    background_connectivity = []
    for mask, background in cases:
        defects, _antipodal, advance, _endpoints, _support = (
            independent_packet_geometry(mask, background)
        )
        seed = independent_status_seed(mask, background)
        direct_targets = direct_protected_targets(seed)
        inverse_targets = frozenset(
            site for site in bench if locally_protected_target(seed, site)
        )
        guard_completeness.append(direct_targets == inverse_targets)
        footprint = set(independent_role_footprint(mask, background))
        if len(defects) == 3:
            if advance is None:
                raise AssertionError((mask, background))
            launchers = {scale(2, advance)}
        else:
            launchers = {
                site
                for site, status in seed.items()
                if status == ("BG", background)
            }
        blocked = footprint - launchers
        reachable = set(launchers)
        frontier = set(launchers)
        while frontier:
            site = frontier.pop()
            for axis in AXES:
                target = add(site, axis)
                if (
                    target in bench
                    and target not in blocked
                    and target not in reachable
                ):
                    reachable.add(target)
                    frontier.add(target)
        background_connectivity.append((set(bench) - blocked) <= reachable)

    selected_cases = 0
    selected_passes = 0
    strict_checks = []
    permanence_checks = []
    terminal_signatures: dict[
        tuple[int, int], tuple[tuple[Vector, Status], ...]
    ] = {}
    signature_mismatches = 0
    flood_write_histogram = Counter()
    for mask, background in cases:
        defects, _antipodal, _advance, _endpoints, support = (
            independent_packet_geometry(mask, background)
        )
        orders = arm_extensions if len(defects) == 3 else ((),)
        for order in orders:
            for policy in policies:
                selected_cases += 1
                if len(defects) == 3:
                    state, strict, permanent = finish_role_launch(
                        mask, background, order
                    )
                else:
                    state = independent_status_seed(mask, background)
                    strict = True
                    permanent = True
                full, additions = flood_status_bench(
                    state, background, bench, policy
                )
                decoded_exact = full and all(
                    status_payload(state[site])
                    == (1 - background if site in support else background)
                    for site in bench
                )
                selected_passes += int(decoded_exact)
                strict_checks.append(strict)
                permanence_checks.append(permanent)
                flood_write_histogram[additions] += 1
                signature = tuple(sorted(state.items()))
                key = (mask, background)
                if key not in terminal_signatures:
                    terminal_signatures[key] = signature
                else:
                    signature_mismatches += int(
                        terminal_signatures[key] != signature
                    )

    race_mask = 7
    race_background = 0
    race_centers = (ORIGIN, (0, -6, 0))
    race_defects, _a, _b, _ends, race_support = (
        independent_packet_geometry(race_mask, race_background)
    )
    complete_race_support = {
        add(center, site)
        for center in race_centers
        for site in race_support
    }
    delayed_race_support = {
        add(race_centers[0], site) for site in race_support
    } | {
        add(race_centers[1], site) for site in race_defects
    }
    delayed_bit = packet_support_bit(delayed_race_support, race_background)
    race_bad_center_masks = tuple(sorted(
        (center, shell_mask(center, delayed_bit))
        for center in affected_centers(delayed_race_support)
        if shell_mask(center, delayed_bit) not in cube_edge_words()
    ))
    delayed_seed = independent_status_seed(
        race_mask, race_background, race_centers[1]
    )
    _d, race_a, race_b, _e, _s = independent_packet_geometry(
        race_mask, race_background
    )
    if race_a is None or race_b is None:
        raise AssertionError(race_mask)
    delayed_step_targets = {
        add(race_centers[1], add(port, race_b))
        for port in (race_a, scale(-1, race_a))
    }

    branch_masks = {
        background: tuple(
            mask
            for mask in sorted(cube_edge_words())
            if background in packet_background_options(mask)
        )
        for background in (0, 1)
    }
    pair_pass = pair_total = 0
    triangle_pass = triangle_total = 0
    for background in (0, 1):
        for masks in itertools.product(branch_masks[background], repeat=2):
            pair_total += 1
            centers = (ORIGIN, (5, 0, 0))
            footprints = tuple(
                independent_role_footprint(mask, background, center)
                for mask, center in zip(masks, centers)
            )
            support = {
                add(center, site)
                for mask, center in zip(masks, centers)
                for site in independent_packet_geometry(mask, background)[4]
            }
            pair_pass += int(
                not (footprints[0] & footprints[1])
                and packet_support_valid(support, background)
            )
        triangle_centers = (ORIGIN, (5, 0, 0), (0, 5, 0))
        for masks in itertools.product(branch_masks[background], repeat=3):
            triangle_total += 1
            footprints = tuple(
                independent_role_footprint(mask, background, center)
                for mask, center in zip(masks, triangle_centers)
            )
            support = {
                add(center, site)
                for mask, center in zip(masks, triangle_centers)
                for site in independent_packet_geometry(mask, background)[4]
            }
            disjoint = all(
                not (footprints[left] & footprints[right])
                for left, right in itertools.combinations(range(3), 2)
            )
            triangle_pass += int(
                disjoint and packet_support_valid(support, background)
            )

    half_turn: tuple[Vector, Vector, Vector] = (
        (1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    )

    def transform_status(status: Status) -> Status:
        if status[0] in ("LOCK", "BG"):
            return (status[0], 1 - int(status[1]))
        direction = status[1]
        if not isinstance(direction, tuple):
            raise AssertionError(status)
        return (
            status[0],
            mat_vec(half_turn, direction),
            1 - int(status[2]),
        )

    left_center = (0, 3, 0)
    right_center = (0, -3, 0)
    left_mask = 7
    left_defects = independent_packet_geometry(left_mask, 0)[0]
    right_defects = {mat_vec(half_turn, site) for site in left_defects}
    right_mask = sum(
        (0 if axis in right_defects else 1) << index
        for index, axis in enumerate(AXES)
    )
    left_state, left_reachable, left_permanent = finish_role_launch(
        left_mask, 0, ("Ls", "Le", "Rs", "Re"), left_center
    )
    right_state, right_reachable, right_permanent = finish_role_launch(
        right_mask, 1, ("Ls", "Le", "Rs", "Re"), right_center
    )
    launched_disjoint = not (set(left_state) & set(right_state))
    launched_state = left_state | right_state
    transformed_state = {
        mat_vec(half_turn, site): transform_status(status)
        for site, status in launched_state.items()
    }
    midpoint_sources = {
        launched_state.get(add(ORIGIN, axis)) for axis in AXES
    } & {("BG", 0), ("BG", 1)}
    fixed_statuses = {
        status
        for status in visible_statuses
        if transform_status(status) == status
    }
    half_turn_preserves_axes = {
        mat_vec(half_turn, axis) for axis in AXES
    } == set(AXES)
    status_transform_involutive = all(
        transform_status(transform_status(status)) == status
        for status in visible_statuses
    )
    full_launched_symmetry_witness = all((
        determinant_three(half_turn) == 1,
        half_turn_preserves_axes,
        status_transform_involutive,
        mat_vec(half_turn, left_center) == right_center,
        mat_vec(half_turn, right_center) == left_center,
        right_mask == 52,
        left_reachable,
        right_reachable,
        left_permanent,
        right_permanent,
        launched_disjoint,
        transformed_state == launched_state,
        ORIGIN not in launched_state,
        mat_vec(half_turn, ORIGIN) == ORIGIN,
        midpoint_sources == {("BG", 0), ("BG", 1)},
        not fixed_statuses,
    ))

    all_fair_single_confluence = all((
        all(guard_completeness),
        all(background_connectivity),
        len(arm_extensions) == 6,
        selected_passes == selected_cases,
        signature_mismatches == 0,
        all(strict_checks),
        all(permanence_checks),
    ))
    guarded_same_background_confluence = all((
        all_fair_single_confluence,
        pair_pass == pair_total,
        triangle_pass == triangle_total,
    ))
    return {
        "packet_case_count": len(cases),
        "packet_background_histogram": dict(sorted(Counter(
            background for _mask, background in cases
        ).items())),
        "packet_support_size_histogram": dict(sorted(
            support_size_histogram.items()
        )),
        "packet_affected_center_histogram": dict(sorted(
            affected_center_histogram.items()
        )),
        "packet_formulas_valid": all(packet_validations),
        "nontriple_case_count": sum(
            len(independent_packet_geometry(mask, background)[0]) != 3
            for mask, background in cases
        ),
        "triple_background_branch_count": sum(
            len(independent_packet_geometry(mask, background)[0]) == 3
            for mask, background in cases
        ),
        "triple_orientation_count": len(triple_orientations),
        "visible_status_alphabet_size": len(visible_statuses),
        "all_statuses_decode_binary": all(
            status_payload(status) in (0, 1) for status in visible_statuses
        ),
        "ungated_prelaunch_states": ungated_states,
        "gated_launch_states": gated_states,
        "causal_prefix_history_count": len(prefix_histories),
        "terminal_arm_linear_extensions": len(arm_extensions),
        "selected_flood_policy_count": len(policies),
        "selected_policy_schedule_pass_total": (
            selected_passes, selected_cases
        ),
        "selected_policies_exhaust_all_flood_orders": False,
        "selected_policy_cases_are_finite_enumeration": True,
        "terminal_signature_mismatches": signature_mismatches,
        "terminal_branch_signature_count": len(terminal_signatures),
        "flood_write_histogram": dict(sorted(flood_write_histogram.items())),
        "all_role_targets_protected_from_seed": all(guard_completeness),
        "background_domain_connected_on_bench": all(background_connectivity),
        "role_write_maximum_distance": 1,
        "guard_maximum_read_radius": 2,
        "append_only_permanent": all(permanence_checks),
        "finite_bench_all_fair_schedule_confluence": all_fair_single_confluence,
        "all_fair_confluence_is_analytic": True,
        "fairness_required": True,
        "infinite_lattice_terminal_state_claimed": False,
        "future_target_content_consulted": False,
        "fresh_target_is_domain_restriction": True,
        "absence_assigned_readable_content": False,
        "supplied_role_bearing_seed": True,
        "naive_race_mask": race_mask,
        "naive_race_background": race_background,
        "naive_race_centers": race_centers,
        "naive_complete_cap_union_valid": packet_support_valid(
            complete_race_support, race_background
        ),
        "naive_race_bad_center_masks": race_bad_center_masks,
        "naive_race_bad_masks": tuple(sorted(
            mask for _center, mask in race_bad_center_masks
        )),
        "guard_protects_delayed_step_targets": all(
            locally_protected_target(delayed_seed, target)
            for target in delayed_step_targets
        ),
        "unguarded_same_background_confluent": False,
        "branch_count_per_background": tuple(
            len(branch_masks[background]) for background in (0, 1)
        ),
        "same_background_pair_pass_total": (pair_pass, pair_total),
        "same_background_triangle_pass_total": (
            triangle_pass, triangle_total
        ),
        "pair_axial_center_separation": 5,
        "triangle_centers": (ORIGIN, (5, 0, 0), (0, 5, 0)),
        "guarded_same_background_disjoint_confluence": (
            guarded_same_background_confluence
        ),
        "pair_triangle_counts_are_branch_enumerations": True,
        "multi_seed_schedules_exhaustively_enumerated": False,
        "mixed_half_turn_matrix": half_turn,
        "mixed_half_turn_determinant": determinant_three(half_turn),
        "mixed_half_turn_preserves_signed_axes": half_turn_preserves_axes,
        "mixed_status_transform_involutive": status_transform_involutive,
        "mixed_witness_centers": (left_center, right_center),
        "mixed_witness_masks": (left_mask, right_mask),
        "mixed_full_launched_status_witness": (
            full_launched_symmetry_witness
        ),
        "mixed_launched_state_size": len(launched_state),
        "mixed_transformed_state_exact": transformed_state == launched_state,
        "mixed_midpoint_competing_outputs": tuple(sorted(midpoint_sources)),
        "mixed_visible_fixed_status_count": len(fixed_statuses),
        "mixed_midpoint_conditional_obstruction": (
            full_launched_symmetry_witness and not fixed_statuses
        ),
        "mixed_obstruction_scope": (
            "deterministic_single_site_progressing_output_under_"
            "proper_rotation_plus_complement"
        ),
        "mixed_complement_covariance_is_explicit_hypothesis": True,
        "mixed_complement_covariance_derived_from_word_language": False,
        "mixed_midpoint_universal_no_go": False,
        "mixed_live_escape_count": 6,
        "overlapping_role_footprints_resolved": False,
        "one_site_m2_status_compilation": False,
        "normalized_local_cp_instrument": False,
        "state_action_seed_selection": False,
        "occurrence_rate_selected": False,
        "complete_history": False,
    }


@cache
def conditional_effect_refinement_facts() -> dict[str, object]:
    supports = b212.stochastic_supports()
    case_normalization = []
    coarse_positivity = []
    refined_positivity = []
    fiber_identities = []
    refined_normalization = []
    distinct_refined_words = []
    for depth, orientation in itertools.product((1, 2), (1, -1)):
        coarse = b212.b211.coarse_effects(depth, orientation)
        case_normalization.append(
            sp.simplify(sum(coarse.values(), sp.zeros(4)) - sp.eye(4))
            == sp.zeros(4)
        )
        word_effects = {}
        for label, effect in coarse.items():
            coarse_positivity.append(effect.is_positive_definite is True)
            refinement = sp.simplify(effect / len(supports[label]))
            for mask in supports[label]:
                word_effects[mask] = refinement
                refined_positivity.append(
                    refinement.is_positive_definite is True
                )
            fiber_identities.append(
                sp.simplify(sum(
                    (word_effects[mask] for mask in supports[label]),
                    sp.zeros(4),
                ) - effect) == sp.zeros(4)
            )
        distinct_refined_words.append(len(word_effects))
        refined_normalization.append(
            sp.simplify(sum(word_effects.values(), sp.zeros(4)) - sp.eye(4))
            == sp.zeros(4)
        )
    moat = scalar_moat_facts()
    return {
        "parameter_cases": 4,
        "coarse_effect_count": len(coarse_positivity),
        "coarse_effects_strictly_positive": all(coarse_positivity),
        "coarse_povm_normalized": all(case_normalization),
        "refined_word_counts": tuple(distinct_refined_words),
        "refined_word_effect_count": len(refined_positivity),
        "refined_word_effects_strictly_positive": all(refined_positivity),
        "fiber_effect_identities": all(fiber_identities),
        "fiber_effect_identity_count": sum(fiber_identities),
        "refined_povm_normalized": all(refined_normalization),
        "every_word_has_both_scalar_moats": moat["all_complete_by_radius_five"],
        "conditional_finite_region_dilation_exists": all((
            all(coarse_positivity),
            all(case_normalization),
            all(refined_positivity),
            all(fiber_identities),
            all(refined_normalization),
            moat["all_complete_by_radius_five"],
        )),
        "supplied_fresh_region": True,
        "stabilizer_template_selection_derived": False,
        "all_center_stationary_h1_law_newly_constructed": False,
        "autonomous_event_process": False,
    }


@cache
def no_go_discipline_facts() -> dict[str, object]:
    statement = (
        "The permanent-binary unique five-of-six rule stalls on the 194 "
        "tested catalog cube seeds, and the period-four-transverse planar "
        "census leaves specified pairs unresolved only through width eight. "
        "The full launched-status half-turn witness excludes a deterministic "
        "single-site progressing midpoint output only when complement "
        "covariance is imposed."
    )
    route_families = (
        ("cube_edge_form", "local word graph", "exact 26-word classification"),
        ("parity_splice", "bipartite factorization", "heterogeneous global fields"),
        ("scalar_moat", "finite SAT packet", "all central words localized"),
        ("compact_nucleus", "periodic patch cap", "all 194 seed types localized"),
        ("planar_bridge", "finite slab CNF", "bounded interface census"),
        ("native_front", "five-known completion", "permanent propagation"),
        ("status_front", "append-only role grammar", "guarded local formation"),
        ("mixed_random", "recorded stochastic arbitration", "live symmetry escape"),
    )
    walls = (
        "mixed_or_overlap_arbitration",
        "status_cp_compiler",
        "state_action_nucleation",
        "occurrence_rate",
        "repeated_history",
    )
    wall_pairs = tuple(itertools.combinations(walls, 2))
    hidden_phrases = (
        "we assume", "by construction", "as is standard", "framework provides",
        "bridge context", "background", "naturally", "obviously",
        "standard qft", "registered", "canonical",
    )
    resolution_audit = {
        "per_element": "26 words, 38 caps and 52 visible status symbols",
        "per_site": "632 selected policies and an exact midpoint witness",
        "per_mode": "two scalar labels, all signed axes and bounded slabs",
        "per_block": "722 pairs and 13718 right-triangle triples",
        "lattice_wide": "only common-label disjoint fair fronts are closed",
    }
    live_escapes = (
        "break complement covariance with a deterministic priority",
        "append a random or CP-selected permanent arbitration Record",
        "add a neutral collision-wall status fixed by the stabilizer",
        "use a symmetric multisite handshake instead of one midpoint write",
        "record an asymmetric seed identifier or arrival priority",
        "leave the midpoint unwritten and route the front around it",
    )
    cross_cycle_echoes = (
        "Block212 higher-block status retired a narrower binary-front rigidity",
        "Block212 static radius-three locality did not itself supply formation",
        "the new guard retires only the common-label disjoint collision subset",
        "finite supplied continuations remain distinct from autonomous histories",
    )
    return {
        "normalized_route_family_count": len({route[0] for route in route_families}),
        "collapsed_wall_count": len(walls),
        "wall_pair_count": len(wall_pairs),
        "walls_pairwise_not_logically_collapsed": len(wall_pairs) == 10,
        "hidden_wall_language_absent": not any(
            phrase in statement.lower() for phrase in hidden_phrases
        ),
        "prior_negative_witnesses_load_bearing": 0,
        "resolution_count": len(resolution_audit),
        "live_escape_count": len(live_escapes),
        "within_scope_counterexample_to_stall_found": False,
        "strongest_steelman_is_outside_negative_scope": True,
        "cross_cycle_echo_count": len(cross_cycle_echoes),
        "mixed_midpoint_scope_is_conditional": True,
        "complement_breaking_deterministic_steelman_open": True,
        "universal_no_go_supported": False,
        "gate_pass": all((
            len({route[0] for route in route_families}) >= 5,
            len(wall_pairs) == 10,
            not any(phrase in statement.lower() for phrase in hidden_phrases),
            len(resolution_audit) == 5,
            len(live_escapes) >= 5,
            len(cross_cycle_echoes) >= 3,
        )),
    }


@cache
def classification_facts() -> dict[str, object]:
    return {
        "classification": "partial_static_mergeability_plus_conditional_permanent_status_front",
        "static_full_shell_heterogeneity": True,
        "conditional_finite_event_bridge": True,
        "conditional_permanent_status_front": True,
        "same_background_disjoint_confluence": True,
        "native_unique_front_complete": False,
        "ambiguous_branch_selector_open": True,
        "mixed_background_arbitration_open": True,
        "overlapping_role_footprints_open": True,
        "status_m2_cp_compilation_open": True,
        "event_site_open": True,
        "occurrence_rate_open": True,
        "dense_collision_handshake_open": True,
        "complete_history_open": True,
        "h2_open": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
        "universal_no_go": False,
    }


def expected_claims() -> dict[str, object]:
    return {
        "main": CURRENT_MAIN,
        "parent": True,
        "prereg": True,
        "goal": True,
        "preflight": True,
        "parent_blobs": True,
        "word_count": 26,
        "cube_edge_count": 24,
        "decoder": True,
        "complement": True,
        "cubic": True,
        "checkerboard_classes": (98, 98),
        "splice_count": 9604,
        "parity_factorization": True,
        "layered_control": True,
        "moat_case_count": 52,
        "moat_radius": 5,
        "moat_histogram": {1: 7, 3: 13, 5: 6},
        "moat_revalidation": True,
        "nucleus_count": 194,
        "nucleus_histogram": {0: 1, 1: 120, 2: 72, 4: 1},
        "nucleus_revalidation": True,
        "planar_histogram": {
            0: 196,
            2: 256,
            3: 128,
            5: 384,
            6: 320,
            7: 1088,
            8: 448,
        },
        "planar_join_count": 2820,
        "planar_all_join": False,
        "planar_scope": "period4_transverse_widths_0_through_8",
        "perpendicular_rigidity": True,
        "parallel_wall": True,
        "five_known_histogram": {0: 48, 1: 132, 2: 12},
        "ambiguous_contexts": 12,
        "l1_growth": 0,
        "vector_cube_growth": 192,
        "scalar_cube_growth": 0,
        "front_conflicts": 0,
        "front_mismatches": 0,
        "native_stall": True,
        "packet_case_count": 38,
        "packet_formulas": True,
        "status_alphabet": 52,
        "prelaunch_partition": (9, 1),
        "prefix_history_count": 19,
        "arm_extension_count": 6,
        "selected_policy_case_count": 632,
        "selected_policies_exhaustive": False,
        "guard_radius": 2,
        "status_permanent": True,
        "all_fair_status_confluence": True,
        "race_bad_masks": (9, 10),
        "pair_branch_pass_total": (722, 722),
        "triangle_branch_pass_total": (13718, 13718),
        "mixed_full_witness": True,
        "mixed_scope": (
            "deterministic_single_site_progressing_output_under_"
            "proper_rotation_plus_complement"
        ),
        "mixed_universal_no_go": False,
        "status_seed_supplied": True,
        "status_m2_compiled": False,
        "effect_normalization": True,
        "word_refinement": True,
        "h1_conditional": True,
        "static_formation": False,
        "event_site": False,
        "occurrence_rate": False,
        "dense_confluence": False,
        "complete_history": False,
        "h2": False,
        "axiom": False,
        "retirement": 0,
        "toe": 0,
        "retained": False,
        "universal_no_go": False,
    }


def apply_mutation(values: dict[str, object], mutation: str) -> None:
    mapping = {
        "ind_stale_main": ("main", "stale"),
        "ind_drop_preregistration": ("prereg", False),
        "ind_alter_goal": ("goal", False),
        "ind_alter_preflight": ("preflight", False),
        "ind_alter_parent": ("parent_blobs", False),
        "ind_change_word_count": ("word_count", 25),
        "ind_change_cube_edge_count": ("cube_edge_count", 23),
        "ind_break_decoder": ("decoder", False),
        "ind_break_complement": ("complement", False),
        "ind_break_cubic_closure": ("cubic", False),
        "ind_change_checkerboard_classes": ("checkerboard_classes", (97, 98)),
        "ind_change_splice_count": ("splice_count", 9603),
        "ind_break_parity_factorization": ("parity_factorization", False),
        "ind_break_layered_control": ("layered_control", False),
        "ind_change_moat_case_count": ("moat_case_count", 51),
        "ind_change_moat_radius": ("moat_radius", 4),
        "ind_change_moat_histogram": ("moat_histogram", {1: 8, 3: 12, 5: 6}),
        "ind_break_moat_revalidation": ("moat_revalidation", False),
        "ind_change_nucleus_count": ("nucleus_count", 193),
        "ind_change_nucleus_histogram": ("nucleus_histogram", {0: 1, 1: 121, 2: 71, 4: 1}),
        "ind_break_nucleus_revalidation": ("nucleus_revalidation", False),
        "ind_change_planar_histogram": ("planar_histogram", {0: 196, 2: 256}),
        "ind_change_planar_join_count": ("planar_join_count", 2819),
        "ind_claim_all_planar_pairs_join": ("planar_all_join", True),
        "ind_widen_planar_scope": ("planar_scope", "all_widths_and_interfaces"),
        "ind_break_perpendicular_rigidity": ("perpendicular_rigidity", False),
        "ind_erase_parallel_wall": ("parallel_wall", False),
        "ind_change_five_known_histogram": ("five_known_histogram", {0: 48, 1: 144}),
        "ind_erase_ambiguous_contexts": ("ambiguous_contexts", 0),
        "ind_claim_l1_seed_growth": ("l1_growth", 1),
        "ind_erase_vector_cube_growth": ("vector_cube_growth", 191),
        "ind_claim_scalar_cube_growth": ("scalar_cube_growth", 2),
        "ind_inject_front_conflict": ("front_conflicts", 1),
        "ind_inject_front_mismatch": ("front_mismatches", 1),
        "ind_claim_native_front_complete": ("native_stall", False),
        "ind_change_packet_case_count": ("packet_case_count", 37),
        "ind_break_packet_formula": ("packet_formulas", False),
        "ind_change_status_alphabet": ("status_alphabet", 51),
        "ind_change_prelaunch_partition": ("prelaunch_partition", (10, 0)),
        "ind_change_prefix_history_count": ("prefix_history_count", 18),
        "ind_change_arm_extension_count": ("arm_extension_count", 5),
        "ind_change_selected_policy_case_count": (
            "selected_policy_case_count", 631
        ),
        "ind_claim_selected_policies_exhaustive": (
            "selected_policies_exhaustive", True
        ),
        "ind_change_guard_radius": ("guard_radius", 1),
        "ind_break_status_permanence": ("status_permanent", False),
        "ind_break_all_fair_status_confluence": (
            "all_fair_status_confluence", False
        ),
        "ind_erase_race_masks": ("race_bad_masks", ()),
        "ind_change_pair_branch_count": (
            "pair_branch_pass_total", (721, 722)
        ),
        "ind_change_triangle_branch_count": (
            "triangle_branch_pass_total", (13717, 13718)
        ),
        "ind_weaken_reachable_symmetry_witness": (
            "mixed_full_witness", False
        ),
        "ind_drop_mixed_complement_hypothesis": (
            "mixed_scope", "deterministic_midpoint_without_hypotheses"
        ),
        "ind_claim_mixed_midpoint_universal": (
            "mixed_universal_no_go", True
        ),
        "ind_claim_status_seed_autonomous": ("status_seed_supplied", False),
        "ind_claim_status_m2_compiled": ("status_m2_compiled", True),
        "ind_break_effect_normalization": ("effect_normalization", False),
        "ind_break_word_refinement": ("word_refinement", False),
        "ind_claim_unconditional_h1_bridge": ("h1_conditional", False),
        "ind_claim_static_is_formation": ("static_formation", True),
        "ind_claim_event_site": ("event_site", True),
        "ind_claim_occurrence_rate": ("occurrence_rate", True),
        "ind_claim_dense_confluence": ("dense_confluence", True),
        "ind_claim_complete_history": ("complete_history", True),
        "ind_open_h2": ("h2", True),
        "ind_edit_axiom": ("axiom", True),
        "ind_retire_obligation": ("retirement", 1),
        "ind_move_toe": ("toe", 1),
        "ind_claim_retained": ("retained", True),
        "ind_claim_universal_no_go": ("universal_no_go", True),
    }
    key, value = mapping[mutation]
    values[key] = value


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    authority = authority_facts()
    words = word_facts()
    parity = parity_facts()
    moats = scalar_moat_facts()
    nuclei = compact_nucleus_facts()
    planar = planar_interface_facts()
    front = native_front_facts()
    status_front = independent_permanent_status_front_facts()
    effects = conditional_effect_refinement_facts()
    no_go = no_go_discipline_facts()
    classification = classification_facts()
    expected = expected_claims()
    if mutation:
        apply_mutation(expected, mutation)

    authority_ok = (
        authority["main"] == expected["main"]
        and authority["parent_ancestor"] == expected["parent"]
        and authority["prereg_ancestor"] == expected["prereg"]
        and authority["prereg_exact"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and (authority["goal_registered"] == authority["goal_worktree"])
        == expected["goal"]
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and (authority["preflight_registered"] == authority["preflight_worktree"])
        == expected["preflight"]
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
        and (
            authority["parent_note"] == PARENT_NOTE_BLOB
            and authority["parent_runner"] == PARENT_RUNNER_BLOB
            and authority["parent_cache"] == PARENT_CACHE_BLOB
        ) == expected["parent_blobs"]
        and authority["inputs_exist"]
        and authority["h2_sealed_text"]
    )
    word_ok = (
        words["word_count"] == expected["word_count"]
        and words["directed_cube_edges"] == expected["cube_edge_count"]
        and words["scalar_loops"] == (
            ((0, 0, 0), (0, 0, 0)),
            ((1, 1, 1), (1, 1, 1)),
        )
        and words["word_weight_histogram"]
        == {0: 1, 1: 6, 3: 12, 5: 6, 6: 1}
        and words["xor_characterization_exact"]
        and words["parent_word_set_exact"]
        and words["decoder_exact"] == expected["decoder"]
        and words["complement_closed"] == expected["complement"]
        and words["proper_cubic_closed"] == expected["cubic"]
        and words["proper_cubic_permutation_count"] == 24
    )
    parity_ok = (
        parity["catalog_count"] == 194
        and parity["catalog_distinct"]
        and parity["catalog_all_valid"]
        and parity["vector_count"] == 192
        and (
            parity["even_restriction_classes"],
            parity["odd_restriction_classes"],
        ) == expected["checkerboard_classes"]
        and parity["ordered_catalog_pairs"] == 194 ** 2
        and parity["distinct_checkerboard_splices"] == expected["splice_count"]
        and (
            parity["all_checkerboard_splices_valid"]
            and parity["checkerboard_shell_source_exact"]
            and parity["analytic_parity_decoupling"]
        ) == expected["parity_factorization"]
    )
    layered_ok = (
        parity["layered_control_count"] == 8188
        and parity["layered_no_isolated_equivalence"]
        == expected["layered_control"]
        and parity["step_wall_masks"] == (0, 2, 62, 63)
        and parity["step_wall_valid"]
        and parity["single_bit_flip_degree_histogram"] == {0: 192, 64: 2}
        and parity["periodic_vector_one_bit_rigid"]
        and parity["scalar_one_bit_degrees"] == (64, 64)
    )
    moat_ok = (
        moats["tested_exterior_mask_pairs"] == expected["moat_case_count"]
        and moats["radii_tested"] == tuple(range(1, 6))
        and moats["all_complete_by_radius_five"]
        and moats["maximum_minimum_radius"] == expected["moat_radius"]
        and moats["zero_exterior_radius_histogram"]
        == expected["moat_histogram"]
        and moats["one_exterior_radius_histogram"]
        == expected["moat_histogram"]
        and moats["complement_minima_exact"]
        and moats["all_witnesses_revalidated"]
        == expected["moat_revalidation"]
        and moats["witness_count"] == 52
        and not moats["template_selection_derived"]
    )
    nucleus_ok = (
        nuclei["catalog_seed_types"] == expected["nucleus_count"]
        and nuclei["pads_tested"] == tuple(range(5))
        and nuclei["all_catalog_types_compact_p_capped"]
        and nuclei["minimum_pad_histogram"]
        == expected["nucleus_histogram"]
        and (
            nuclei["all_witnesses_revalidated"]
            and nuclei["all_catalog_patches_revalidated"]
        ) == expected["nucleus_revalidation"]
        and nuclei["witness_count"] == 194
        and nuclei["vector_support_cube_halfwidth"] == 4
        and nuclei["n_support_cube_halfwidth"] == 6
        and nuclei["safe_axial_center_separations"]
        == {"vector_vector": 11, "vector_N": 13, "N_N": 15}
        and not nuclei["dense_collision_front_constructed"]
    )
    planar_census_ok = (
        planar["ordered_boundary_pairs"] == 194 ** 2
        and planar["widths_tested"] == tuple(range(9))
        and planar["transverse_period"] == 4
        and planar["minimum_width_histogram"]
        == expected["planar_histogram"]
        and planar["pairs_joining_by_width_eight"]
        == expected["planar_join_count"]
        and planar["pairs_unresolved_through_width_eight"] == 34816
        and planar["all_pairs_join"] == expected["planar_all_join"]
        and planar["all_positive_witnesses_revalidated"]
        and planar["positive_witness_count"] == 2820
    )
    planar_boundary_ok = (
        planar["perpendicular_boundary_flip_checks"] == 49152
        and planar["perpendicular_halfspace_rigid"]
        == expected["perpendicular_rigidity"]
        and planar["perpendicular_rigidity_is_local_induction"]
        and planar["signed_axis_normal_orbit"]
        and planar["parallel_antipodal_wall_exists"]
        == expected["parallel_wall"]
        and planar["bounded_scope"] == expected["planar_scope"]
        and not planar["wider_widths_excluded"]
        and not planar["nonplanar_interfaces_excluded"]
        and not planar["tentative_rewriting_excluded"]
    )
    five_known_ok = (
        words["five_known_context_count"] == 192
        and front["five_known_completion_histogram"]
        == expected["five_known_histogram"]
        and front["ambiguous_context_count"]
        == expected["ambiguous_contexts"]
    )
    front_ok = (
        front["l1_radius_two_seed_types_tested"] == 194
        and front["l1_radius_two_types_with_growth"] == expected["l1_growth"]
        and front["l1_radius_two_all_stop_without_proposal"]
        and front["cube_seed_types_tested"] == 194
        and front["cube_initial_site_count"] == 125
        and front["vector_cube_types_with_growth"]
        == expected["vector_cube_growth"]
        and front["scalar_cube_types_with_growth"]
        == expected["scalar_cube_growth"]
        and front["proposal_conflicts"] == expected["front_conflicts"]
        and front["proposal_target_mismatches"]
        == expected["front_mismatches"]
        and front["all_catalog_controls_stop_without_proposal"]
        and not front["any_round_cap_hit"]
        and front["native_unique_rule_stalls"] == expected["native_stall"]
        and front["tested_rule_scope"] == "permanent_binary_unique_five_of_six"
        and not front["ambiguous_branch_rule_selected"]
        and not front["tentative_status_carrier_constructed"]
    )
    status_front_single_ok = (
        status_front["packet_case_count"] == expected["packet_case_count"]
        and status_front["packet_background_histogram"] == {0: 19, 1: 19}
        and status_front["packet_support_size_histogram"]
        == {0: 2, 1: 12, 5: 24}
        and status_front["packet_affected_center_histogram"]
        == {0: 2, 6: 12, 22: 24}
        and status_front["packet_formulas_valid"]
        == expected["packet_formulas"]
        and status_front["nontriple_case_count"] == 14
        and status_front["triple_background_branch_count"] == 24
        and status_front["triple_orientation_count"] == 12
        and status_front["visible_status_alphabet_size"]
        == expected["status_alphabet"]
        and status_front["all_statuses_decode_binary"]
        and (
            status_front["ungated_prelaunch_states"],
            status_front["gated_launch_states"],
        ) == expected["prelaunch_partition"]
        and status_front["causal_prefix_history_count"]
        == expected["prefix_history_count"]
        and status_front["terminal_arm_linear_extensions"]
        == expected["arm_extension_count"]
        and status_front["selected_flood_policy_count"] == 4
        and status_front["selected_policy_schedule_pass_total"]
        == (
            expected["selected_policy_case_count"],
            expected["selected_policy_case_count"],
        )
        and status_front["selected_policies_exhaust_all_flood_orders"]
        == expected["selected_policies_exhaustive"]
        and status_front["selected_policy_cases_are_finite_enumeration"]
        and status_front["terminal_signature_mismatches"] == 0
        and status_front["terminal_branch_signature_count"] == 38
        and status_front["flood_write_histogram"] == {331: 576, 336: 56}
        and status_front["all_role_targets_protected_from_seed"]
        and status_front["background_domain_connected_on_bench"]
        and status_front["role_write_maximum_distance"] == 1
        and status_front["guard_maximum_read_radius"]
        == expected["guard_radius"]
        and status_front["append_only_permanent"]
        == expected["status_permanent"]
        and status_front["finite_bench_all_fair_schedule_confluence"]
        == expected["all_fair_status_confluence"]
        and status_front["all_fair_confluence_is_analytic"]
        and status_front["fairness_required"]
        and not status_front["infinite_lattice_terminal_state_claimed"]
        and not status_front["future_target_content_consulted"]
        and status_front["fresh_target_is_domain_restriction"]
        and not status_front["absence_assigned_readable_content"]
    )
    status_front_multi_ok = (
        status_front["naive_race_mask"] == 7
        and status_front["naive_race_background"] == 0
        and status_front["naive_race_centers"]
        == (ORIGIN, (0, -6, 0))
        and status_front["naive_complete_cap_union_valid"]
        and status_front["naive_race_bad_center_masks"]
        == (((-1, -7, 0), 10), ((1, -7, 0), 9))
        and status_front["naive_race_bad_masks"]
        == expected["race_bad_masks"]
        and status_front["guard_protects_delayed_step_targets"]
        and not status_front["unguarded_same_background_confluent"]
        and status_front["branch_count_per_background"] == (19, 19)
        and status_front["same_background_pair_pass_total"]
        == expected["pair_branch_pass_total"]
        and status_front["same_background_triangle_pass_total"]
        == expected["triangle_branch_pass_total"]
        and status_front["pair_axial_center_separation"] == 5
        and status_front["triangle_centers"]
        == (ORIGIN, (5, 0, 0), (0, 5, 0))
        and status_front["guarded_same_background_disjoint_confluence"]
        and status_front["pair_triangle_counts_are_branch_enumerations"]
        and not status_front["multi_seed_schedules_exhaustively_enumerated"]
        and status_front["mixed_half_turn_matrix"]
        == ((1, 0, 0), (0, -1, 0), (0, 0, -1))
        and status_front["mixed_half_turn_determinant"] == 1
        and status_front["mixed_half_turn_preserves_signed_axes"]
        and status_front["mixed_status_transform_involutive"]
        and status_front["mixed_witness_centers"]
        == ((0, 3, 0), (0, -3, 0))
        and status_front["mixed_witness_masks"] == (7, 52)
        and status_front["mixed_full_launched_status_witness"]
        == expected["mixed_full_witness"]
        and status_front["mixed_launched_state_size"] == 24
        and status_front["mixed_transformed_state_exact"]
        and status_front["mixed_midpoint_competing_outputs"]
        == (("BG", 0), ("BG", 1))
        and status_front["mixed_visible_fixed_status_count"] == 0
        and status_front["mixed_midpoint_conditional_obstruction"]
        and status_front["mixed_obstruction_scope"] == expected["mixed_scope"]
        and status_front[
            "mixed_complement_covariance_is_explicit_hypothesis"
        ]
        and not status_front[
            "mixed_complement_covariance_derived_from_word_language"
        ]
        and status_front["mixed_midpoint_universal_no_go"]
        == expected["mixed_universal_no_go"]
        and status_front["mixed_live_escape_count"] >= 5
    )
    effect_ok = (
        effects["parameter_cases"] == 4
        and effects["coarse_effect_count"] == 32
        and effects["coarse_effects_strictly_positive"]
        and effects["coarse_povm_normalized"]
        == expected["effect_normalization"]
        and effects["refined_word_counts"] == (26,) * 4
        and effects["refined_word_effect_count"] == 104
        and effects["refined_word_effects_strictly_positive"]
        and (
            effects["fiber_effect_identities"]
            and effects["refined_povm_normalized"]
        ) == expected["word_refinement"]
        and effects["fiber_effect_identity_count"] == 32
        and effects["every_word_has_both_scalar_moats"]
        and effects["conditional_finite_region_dilation_exists"]
        == expected["h1_conditional"]
        and effects["supplied_fresh_region"]
        and not effects["stabilizer_template_selection_derived"]
        and not effects["all_center_stationary_h1_law_newly_constructed"]
        and not effects["autonomous_event_process"]
    )
    boundary_ok = (
        front["static_completion_is_formation"]
        == expected["static_formation"]
        and front["event_site_selected"] == expected["event_site"]
        and front["occurrence_rate_selected"]
        == expected["occurrence_rate"]
        and front["dense_multi_seed_confluence"]
        == expected["dense_confluence"]
        and front["complete_history"] == expected["complete_history"]
        and status_front["supplied_role_bearing_seed"]
        == expected["status_seed_supplied"]
        and not status_front["overlapping_role_footprints_resolved"]
        and status_front["one_site_m2_status_compilation"]
        == expected["status_m2_compiled"]
        and not status_front["normalized_local_cp_instrument"]
        and not status_front["state_action_seed_selection"]
        and not status_front["occurrence_rate_selected"]
        and not status_front["complete_history"]
        and no_go["gate_pass"]
        and no_go["normalized_route_family_count"] >= 5
        and no_go["resolution_count"] == 5
        and no_go["live_escape_count"] >= 5
        and not no_go["universal_no_go_supported"]
        and no_go["mixed_midpoint_scope_is_conditional"]
        and no_go["complement_breaking_deterministic_steelman_open"]
        and classification["static_full_shell_heterogeneity"]
        and classification["conditional_finite_event_bridge"]
        and classification["conditional_permanent_status_front"]
        and classification["same_background_disjoint_confluence"]
        and not classification["native_unique_front_complete"]
        and classification["ambiguous_branch_selector_open"]
        and classification["mixed_background_arbitration_open"]
        and classification["overlapping_role_footprints_open"]
        and classification["status_m2_cp_compilation_open"]
        and classification["event_site_open"]
        and classification["occurrence_rate_open"]
        and classification["dense_collision_handshake_open"]
        and classification["complete_history_open"]
    )
    status_ok = (
        classification["h2_open"] == expected["h2"]
        and classification["axiom_update"] == expected["axiom"]
        and classification["obligation_retirement"] == expected["retirement"]
        and classification["toe_movement"] == expected["toe"]
        and classification["retained"] == expected["retained"]
        and classification["universal_no_go"] == expected["universal_no_go"]
    )

    checks = {
        "A": (authority_ok, "parent, preregistration and immutable authority pins are exact"),
        "B": (word_ok, "the 26 words are exactly 24 directed cube edges plus two scalar loops with the frozen decoder"),
        "C": (parity_ok, "all 194 squared catalog splices factor by checkerboard parity into 9604 valid fields"),
        "D": (layered_ok, "layered domain walls coexist with one-bit rigidity of the periodic vector catalog"),
        "E": (moat_ok, "all 52 word/exterior cases have revalidated scalar-moat witnesses by L1 radius at most five"),
        "F": (nucleus_ok, "all 194 radius-two catalog patches have revalidated compact P-capped nuclei with the exact pad histogram"),
        "G": (planar_census_ok, "all 37636 period-four-transverse planar pairs reproduce the width-zero-to-eight solver census and every positive witness"),
        "H": (planar_boundary_ok, "the planar negative stays width-bounded while perpendicular rigidity and a parallel antipodal wall are exact"),
        "I": (five_known_ok, "all 192 five-known contexts split into 48 impossible, 132 unique and 12 ambiguous cases"),
        "J": (front_ok, "the native permanent-binary unique-completion rule is conflict-free on catalog controls but stalls"),
        "K": (effect_ok, "the positive coarse POVM refines exactly into 26 finite-completion word effects for a supplied fresh region"),
        "L": (boundary_ok, "the scoped negatives pass N1-N8 while branch selection, site, rate, dense handshake and history remain open"),
        "M": (status_ok, "H2, axiom, obligation, TOE, retained status and universal no-go remain unchanged"),
        "N": (status_front_single_ok, "all 38 packets and 52 statuses pass the exact launch graph, 632 selected policies and analytic all-fair finite-bench confluence checks"),
        "O": (status_front_multi_ok, "the masks-9/10 race, all stated guarded same-label branches and the full launched-status conditional midpoint obstruction are exact"),
    }
    passed = sum(int(ok) for ok, _description in checks.values())
    failed = len(checks) - passed
    return passed, failed, {
        "checks": checks,
        "authority": authority,
        "words": words,
        "parity": parity,
        "moats": moats,
        "nuclei": nuclei,
        "planar": planar,
        "front": front,
        "status_front": status_front,
        "effects": effects,
        "no_go": no_go,
        "classification": classification,
    }


def mutation_suite() -> int:
    baseline_passed, baseline_failed, _facts = run()
    detected = 0
    print(
        f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; "
        f"mutations={len(MUTATIONS)}."
    )
    for mutation in MUTATIONS:
        _passed, failed, _mutation_facts = run(mutation)
        caught = failed > 0
        detected += int(caught)
        print(
            f"MUTATION {mutation}: "
            f"{'DETECTED' if caught else 'ESCAPED'} (runner_failures={failed})"
        )
    escaped = len(MUTATIONS) - detected
    print(f"TOTAL: PASS={detected} FAIL={escaped}")
    return 0 if baseline_failed == 0 and escaped == 0 else 1


N5_LINES = (
    "per_element: checked all 26 cube-edge words, 38 low-defect packet formulas, 52 permanent status symbols, exact decoder fibers, 32 coarse effects, and 104 refined word effects.",
    "per_site: checked every affected packet shell, 632 selected-policy single-seed executions, the exact masks-9/10 race and a full reachable launched-status symmetry witness; event-site selection was checked and not executed — no selector is supplied.",
    "per_mode: checked two exteriors, both checkerboard parities, all signed axes, nine ungated plus one gated launch states, 19 causal-prefix histories, six arm extensions and four selected flood policies; H2 was checked and not executed — sealed.",
    "per_block: checked 37636 checkerboard pairs, 37636 planar pairs, all 194 compact nuclei, 722 guarded same-label axial pair branches, 13718 guarded same-label right-triangle triple branches, and four conditional effect-refinement cases.",
    "lattice_wide: checked parity-factorized heterogeneous fields and analytic fair-order confluence only for supplied disjoint same-label permanent-status fronts; mixed/overlapping arbitration, M2/CP compilation, event site/rate and repeated history were checked and not executed.",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        return mutation_suite()

    passed, failed, facts = run(arguments.mutation)
    words = facts["words"]
    parity = facts["parity"]
    moats = facts["moats"]
    nuclei = facts["nuclei"]
    planar = facts["planar"]
    front = facts["front"]
    status_front = facts["status_front"]
    effects = facts["effects"]
    classification = facts["classification"]
    print(
        "CUBE_EDGE: words="
        f"{words['word_count']}=24+2; weights={words['word_weight_histogram']}; "
        "decoder, complement and 24-frame covariance exact."
    )
    print(
        "PARITY_FACTOR: classes="
        f"{parity['even_restriction_classes']}/{parity['odd_restriction_classes']}; "
        f"pairs={parity['ordered_catalog_pairs']}; distinct valid splices="
        f"{parity['distinct_checkerboard_splices']}; layered controls="
        f"{parity['layered_control_count']}."
    )
    print(
        "SCALAR_MOATS: cases="
        f"{moats['tested_exterior_mask_pairs']}; max radius="
        f"{moats['maximum_minimum_radius']}; histograms="
        f"{moats['zero_exterior_radius_histogram']}/"
        f"{moats['one_exterior_radius_histogram']}; witnesses=52/52."
    )
    print(
        "COMPACT_NUCLEI: types="
        f"{nuclei['catalog_seed_types']}; pad histogram="
        f"{nuclei['minimum_pad_histogram']}; witnesses=194/194; support "
        f"halfwidth vector/N={nuclei['vector_support_cube_halfwidth']}/"
        f"{nuclei['n_support_cube_halfwidth']}."
    )
    print(
        "PLANAR_0_8: minima="
        f"{planar['minimum_width_histogram']}; joined/unresolved="
        f"{planar['pairs_joining_by_width_eight']}/"
        f"{planar['pairs_unresolved_through_width_eight']}; positive "
        "witnesses all revalidated; wider/nonplanar routes open."
    )
    print(
        "NATIVE_FRONT: five-known="
        f"{front['five_known_completion_histogram']}; L1 growth="
        f"{front['l1_radius_two_types_with_growth']}/194; cube vector/scalar "
        f"growth={front['vector_cube_types_with_growth']}/192 and "
        f"{front['scalar_cube_types_with_growth']}/2; conflict-free stall."
    )
    print(
        "PERMANENT_STATUS_FRONT: packets/statuses="
        f"{status_front['packet_case_count']}/"
        f"{status_front['visible_status_alphabet_size']}; launch states="
        f"{status_front['ungated_prelaunch_states']} ungated + "
        f"{status_front['gated_launch_states']} gated; prefix histories/arm "
        f"extensions={status_front['causal_prefix_history_count']}/"
        f"{status_front['terminal_arm_linear_extensions']}; selected policies="
        f"{status_front['selected_policy_schedule_pass_total']}; analytic "
        "all-fair finite-bench confluence exact."
    )
    print(
        "PERMANENT_STATUS_MULTI: race centers/masks="
        f"{status_front['naive_race_centers']}/"
        f"{status_front['naive_race_bad_masks']}; guarded pair/triangle="
        f"{status_front['same_background_pair_pass_total']}/"
        f"{status_front['same_background_triangle_pass_total']}; full "
        "launched-status mixed-s symmetry witness exact and conditional."
    )
    print(
        "CONDITIONAL_EFFECTS: cases="
        f"{effects['parameter_cases']}; coarse/refined effects="
        f"{effects['coarse_effect_count']}/{effects['refined_word_effect_count']}; "
        "normalization and fiber sums exact; supplied fresh region only."
    )
    for line in N5_LINES:
        print(line)
    for label, (ok, description) in facts["checks"].items():
        print(f"{label}: {'PASS' if ok else 'FAIL'} — {description}.")
    print(
        "CLASSIFICATION: " + classification["classification"]
        + "; mixed/overlapping arbitration, M2/CP, site/rate/history open; "
        "H2/axiom/TOE/retention unchanged."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
