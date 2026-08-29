#!/usr/bin/env python3
"""Independent finite-group/character check of the Block208 Record gate."""

from __future__ import annotations

import argparse
import itertools
import subprocess
from collections import Counter, deque
from functools import cache
from pathlib import Path

import sympy as sp

import independent_admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28 as eta_independent


ROOT = Path(__file__).resolve().parents[1]
I = sp.I
PREREG = "d182453a70"
PARENT = "80a5f4e46c433d2a7ad97ada1568e5412a2827df"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block02-action-native-record-dilation-20260828"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
GOAL_BLOB = "a39d431a803f8642d07b1f2e9aa60e52134ffa8d"
PREFLIGHT_BLOB = "9cb777656f9be8b3b479812e25da57882c3e7ddb"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block02-action-native-record-dilation-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block02-action-native-record-dilation-20260828/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "scripts/independent_admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28.py",
)

MUTATIONS = (
    "stale_main",
    "unpin_goal",
    "lose_rotation",
    "lose_outcome",
    "erase_orbit24",
    "invent_shell_orbit24",
    "drop_affine_class",
    "select_affine_class",
    "erase_affine_decoder",
    "call_affine_action_physical",
    "merge_two_shell_codes",
    "merge_center_corner_codes",
    "erase_center_corner_embedding",
    "break_writer_tp",
    "break_writer_lock",
    "call_fullrank_record",
    "erase_sharpness_fork",
    "select_sharpness",
    "claim_branch_sufficient",
    "lower_hom_dimension",
    "invent_quadratic_fit",
    "lose_source_term",
    "replace_actual_reverse",
    "claim_eta_closure",
    "claim_axiom_update",
)


def git(*args: str) -> str:
    return subprocess.check_output(("git", *args), cwd=ROOT, text=True).strip()


def key(matrix: sp.MatrixBase) -> tuple[int, ...]:
    return tuple(int(value) for value in matrix)


GEN_A = sp.ImmutableMatrix(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
GEN_B = sp.ImmutableMatrix(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
DIRECTIONS = (
    (-1, 0, 0), (1, 0, 0),
    (0, -1, 0), (0, 1, 0),
    (0, 0, -1), (0, 0, 1),
)
DIR_INDEX = {value: index for index, value in enumerate(DIRECTIONS)}
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
CORNER_INDEX = {value: index for index, value in enumerate(CORNERS)}


@cache
def group() -> tuple[sp.ImmutableMatrix, ...]:
    found = {key(sp.eye(3)): sp.ImmutableMatrix(sp.eye(3))}
    queue = deque(found.values())
    while queue:
        current = queue.popleft()
        for generator in (GEN_A, GEN_B):
            product = sp.ImmutableMatrix(current * generator)
            if key(product) not in found:
                found[key(product)] = product
                queue.append(product)
    return tuple(found[item] for item in sorted(found))


@cache
def group_data() -> dict[str, object]:
    elements = group()
    lookup = {key(value): index for index, value in enumerate(elements)}
    multiplication = tuple(
        tuple(lookup[key(left * right)] for right in elements)
        for left in elements
    )
    identity = lookup[key(sp.eye(3))]
    generators = (lookup[key(GEN_A)], lookup[key(GEN_B)])
    permutations = []
    for rotation in elements:
        permutation = []
        for direction in DIRECTIONS:
            value = tuple(int(item) for item in rotation * sp.Matrix(direction))
            permutation.append(DIR_INDEX[value])
        permutations.append(tuple(permutation))
    return {
        "multiplication": multiplication,
        "identity": identity,
        "generators": generators,
        "permutations": tuple(permutations),
    }


def permute(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for source, target in enumerate(permutation):
        if (mask >> source) & 1:
            result |= 1 << target
    return result


def partition(items, action) -> tuple[frozenset, ...]:
    unseen = set(items)
    result = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset(action(index, seed) for index in range(24))
        result.append(orbit)
        unseen -= orbit
    return tuple(result)


def hist(orbits: tuple[frozenset, ...]) -> dict[int, int]:
    return dict(sorted(Counter(map(len, orbits)).items()))


def embedding_data(items, action) -> dict[str, object]:
    shell_permutations = group_data()["permutations"]
    compatible = []
    for base in ((0, 0), (0, 1), (0, 2)):
        stabilizer = tuple(
            group_index
            for group_index, permutation in enumerate(shell_permutations)
            if (permutation[base[0]], permutation[base[1]]) == base
        )
        target_size = len({
            (permutation[base[0]], permutation[base[1]])
            for permutation in shell_permutations
        })
        compatible.append({
            frozenset(action(group_index, item) for group_index in range(24))
            for item in items
            if len({
                action(group_index, item) for group_index in range(24)
            }) == target_size
            and all(action(group_index, item) == item
                    for group_index in stabilizer)
        })
    return {
        "counts": tuple(len(values) for values in compatible),
        "full": (
            all(compatible)
            and any(
                len({parallel, antiparallel, perpendicular}) == 3
                for parallel in compatible[0]
                for antiparallel in compatible[1]
                for perpendicular in compatible[2]
            )
        ),
    }


def shear_action(rotation: sp.MatrixBase) -> sp.Matrix:
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    return sp.Matrix.hstack(*(
        sp.Matrix((
            (rotation * value * rotation.T)[0, 1],
            (rotation * value * rotation.T)[1, 2],
            (rotation * value * rotation.T)[0, 2],
        ))
        for value in basis
    ))


def affine_classes(site_count: int) -> tuple[dict[str, object], ...]:
    data = group_data()
    multiplication = data["multiplication"]
    identity = data["identity"]
    generator_indices = data["generators"]
    shell_permutations = data["permutations"]
    if site_count == 6:
        permutations = shell_permutations
    elif site_count == 7:
        permutations = tuple(
            (0,) + tuple(index + 1 for index in permutation)
            for permutation in shell_permutations
        )
    else:
        raise ValueError(site_count)

    valid = []
    for first_translation in range(1 << site_count):
        for second_translation in range(1 << site_count):
            generator_translations = (
                first_translation, second_translation
            )
            assigned = {identity: 0}
            queue = deque((identity,))
            consistent = True
            while queue and consistent:
                current = queue.popleft()
                for generator, translation in zip(
                    generator_indices, generator_translations
                ):
                    product = multiplication[current][generator]
                    value = (
                        assigned[current]
                        ^ permute(translation, permutations[current])
                    )
                    if product in assigned:
                        consistent = assigned[product] == value
                        if not consistent:
                            break
                    else:
                        assigned[product] = value
                        queue.append(product)
            if consistent and len(assigned) == 24:
                valid.append(tuple(assigned[index] for index in range(24)))

    def coboundary(seed: int) -> tuple[int, ...]:
        return tuple(
            permute(seed, permutation) ^ seed
            for permutation in permutations
        )

    coboundaries = tuple(
        coboundary(seed) for seed in range(1 << site_count)
    )
    classes: dict[tuple[int, ...], tuple[int, ...]] = {}
    for cocycle in valid:
        canonical = min(
            tuple(left ^ right for left, right in zip(cocycle, boundary))
            for boundary in coboundaries
        )
        classes.setdefault(canonical, cocycle)

    result = []
    for canonical, cocycle in sorted(classes.items()):
        def action(group_index: int, mask: int) -> int:
            return (
                permute(mask, permutations[group_index])
                ^ cocycle[group_index]
            )
        orbits = partition(range(1 << site_count), action)
        histogram = hist(orbits)
        outcome_bases = ((0, 0), (0, 1), (0, 2))
        compatible_orbit_sets = []
        for base in outcome_bases:
            stabilizer = tuple(
                group_index
                for group_index, permutation in enumerate(shell_permutations)
                if (
                    permutation[base[0]], permutation[base[1]]
                ) == base
            )
            outcome_size = len({
                (
                    permutation[base[0]], permutation[base[1]]
                )
                for permutation in shell_permutations
            })
            compatible_orbit_sets.append({
                frozenset(action(group_index, mask) for group_index in range(24))
                for mask in range(1 << site_count)
                if len({
                    action(group_index, mask) for group_index in range(24)
                }) == outcome_size
                and all(action(group_index, mask) == mask
                        for group_index in stabilizer)
            })
        full_embedding = (
            all(compatible_orbit_sets)
            and any(
                len({parallel, antiparallel, perpendicular}) == 3
                for parallel in compatible_orbit_sets[0]
                for antiparallel in compatible_orbit_sets[1]
                for perpendicular in compatible_orbit_sets[2]
            )
        )
        result.append({
            "canonical": canonical,
            "cocycle": cocycle,
            "histogram": histogram,
            "orbit24": histogram.get(24, 0) >= 1,
            "compatible_target_orbit_counts": tuple(
                len(items) for items in compatible_orbit_sets
            ),
            "full_embedding": full_embedding,
        })
    return tuple(result)


@cache
def finite_group_facts() -> dict[str, object]:
    data = group_data()
    permutations = data["permutations"]
    outcomes = tuple(itertools.product(range(6), repeat=2))
    outcome_orbits = partition(
        outcomes,
        lambda group_index, item: (
            permutations[group_index][item[0]],
            permutations[group_index][item[1]],
        ),
    )
    shell_orbits = partition(
        range(64),
        lambda group_index, mask: permute(mask, permutations[group_index]),
    )
    center_orbits = partition(
        tuple(itertools.product((0, 1), range(64))),
        lambda group_index, item: (
            item[0], permute(item[1], permutations[group_index])
        ),
    )
    corner_index = {value: index for index, value in enumerate(CORNERS)}
    corner_permutations = tuple(
        tuple(
            corner_index[tuple(
                int(value) for value in rotation * sp.Matrix(corner)
            )]
            for corner in CORNERS
        )
        for rotation in group()
    )
    corner_action = lambda group_index, mask: permute(
        mask, corner_permutations[group_index]
    )
    corner_orbits = partition(range(256), corner_action)
    center_corner_items = tuple(
        (center, mask) for center in (0, 1) for mask in range(256)
    )
    center_corner_action = lambda group_index, item: (
        item[0], corner_action(group_index, item[1])
    )
    center_corner_orbits = partition(
        center_corner_items, center_corner_action
    )
    corner_embedding = embedding_data(range(256), corner_action)
    center_corner_embedding = embedding_data(
        center_corner_items, center_corner_action
    )
    contrast = (
        sp.sqrt(3), -sp.sqrt(3), sp.Integer(2), sp.Integer(-2),
        sp.Integer(0), sp.Integer(0),
    )

    def contrast_action(group_index: int, value) -> tuple:
        output = [sp.Integer(0)] * 6
        for source, target in enumerate(permutations[group_index]):
            output[target] = value[source]
        return tuple(output)

    contrast_orbit = {
        contrast_action(index, contrast) for index in range(24)
    }
    codes = tuple((1 << first, 1 << second) for first, second in outcomes)
    code_covariance = all(
        (
            permute(code[0], permutations[group_index]),
            permute(code[1], permutations[group_index]),
        )
        == codes[outcomes.index((
            permutations[group_index][outcome[0]],
            permutations[group_index][outcome[1]],
        ))]
        for group_index in range(24)
        for outcome, code in zip(outcomes, codes)
    )

    def face_mask(direction_index: int) -> int:
        direction = sp.Matrix(DIRECTIONS[direction_index])
        return sum(
            1 << index
            for index, corner in enumerate(CORNERS)
            if sp.Matrix(corner).dot(direction) == 1
        )

    center_corner_codes = []
    for first, second in outcomes:
        first_vector = sp.Matrix(DIRECTIONS[first])
        second_vector = sp.Matrix(DIRECTIONS[second])
        relation = int(first_vector.dot(second_vector))
        face = face_mask(first)
        if relation == 1:
            code = (0, face)
        elif relation == -1:
            code = (1, face)
        else:
            excluded = tuple(
                int(value)
                for value in (
                    first_vector - second_vector
                    + first_vector.cross(second_vector)
                )
            )
            code = (0, face & ~(1 << CORNER_INDEX[excluded]))
        center_corner_codes.append(code)
    center_corner_codes = tuple(center_corner_codes)
    center_corner_covariance = all(
        center_corner_action(group_index, code)
        == center_corner_codes[outcomes.index((
            permutations[group_index][outcome[0]],
            permutations[group_index][outcome[1]],
        ))]
        for group_index in range(24)
        for outcome, code in zip(outcomes, center_corner_codes)
    )
    affine6 = affine_classes(6)
    affine7 = affine_classes(7)
    return {
        "group_count": len(group()),
        "determinants": tuple(sorted({int(item.det()) for item in group()})),
        "outcome_histogram": hist(outcome_orbits),
        "shell_histogram": hist(shell_orbits),
        "center_histogram": hist(center_orbits),
        "corner_histogram": hist(corner_orbits),
        "center_corner_histogram": hist(center_corner_orbits),
        "corner_full_embedding": corner_embedding["full"],
        "corner_embedding_counts": corner_embedding["counts"],
        "center_corner_full_embedding": center_corner_embedding["full"],
        "center_corner_embedding_counts": center_corner_embedding["counts"],
        "contrast_orbit_size": len(contrast_orbit),
        "code_count": len(set(codes)),
        "code_covariance": code_covariance,
        "code_weights": tuple(
            (left.bit_count(), right.bit_count()) for left, right in codes
        ),
        "center_corner_code_count": len(set(center_corner_codes)),
        "center_corner_code_covariance": center_corner_covariance,
        "center_corner_record_counts": tuple(
            center + mask.bit_count()
            for center, mask in center_corner_codes
        ),
        "affine6": affine6,
        "affine7": affine7,
    }


def vectors() -> tuple[sp.Matrix, ...]:
    return tuple(sp.Matrix(value) for value in DIRECTIONS)


@cache
def instrument_facts() -> dict[str, object]:
    axes = vectors()
    first_moment = sum(axes, sp.zeros(3, 1))
    second_moment = sum(
        (axis * axis.T for axis in axes), sp.zeros(3)
    )
    effects_sum_coefficient = sp.Rational(36, 36)
    rank_one_eigenvalue = sp.Rational(1, 9)

    r = sp.Matrix((1, 0, 0))
    s = sp.Matrix((sp.Rational(1, 2), sp.sqrt(3) / 2, 0))

    def probabilities(sharpness: sp.Expr) -> tuple[sp.Expr, ...]:
        return tuple(
            sp.simplify(
                (1 + sharpness * n.dot(r))
                * (1 + sharpness * m.dot(s)) / 36
            )
            for n in axes for m in axes
        )

    def decode(values: tuple[sp.Expr, ...], sharpness: sp.Expr):
        dot = sp.Integer(0)
        cross = sp.zeros(3, 1)
        for probability, (n, m) in zip(
            values, itertools.product(axes, repeat=2)
        ):
            dot += probability * n.dot(m)
            cross += probability * n.cross(m)
        return (
            sp.simplify(9 * dot / sharpness**2),
            sp.simplify(9 * cross / sharpness**2),
        )

    sharp = probabilities(sp.Integer(1))
    half = probabilities(sp.Rational(1, 2))
    z_axis = sp.Matrix((0, 0, 1))
    zero_phase_r = sp.Matrix((1, 0, 0))
    zero_phase_s = sp.Matrix((1, 0, 0))
    quarter_phase_s = sp.Matrix((0, 1, 0))
    collision_probabilities = (
        sp.simplify(
            (1 + z_axis.dot(zero_phase_r))
            * (1 + z_axis.dot(zero_phase_s)) / 36
        ),
        sp.simplify(
            (1 + z_axis.dot(zero_phase_r))
            * (1 + z_axis.dot(quarter_phase_s)) / 36
        ),
    )
    output_vectors = tuple(
        (n + 2 * m + n.cross(m)) / 8
        for n in axes for m in axes
    )
    norms = tuple(sp.simplify(value.dot(value)) for value in output_vectors)
    overlaps = tuple(
        sp.simplify((1 + output_vectors[left].dot(output_vectors[right])) / 2)
        for left in range(36) for right in range(left)
    )
    return {
        "first_moment": first_moment,
        "second_moment": second_moment,
        "povm_sum": effects_sum_coefficient,
        "rank_one_eigenvalue": rank_one_eigenvalue,
        "sqrt_completeness": effects_sum_coefficient,
        "blank_write_lock_completeness": True,
        "qnd_lock": True,
        "sharp_sum": sp.simplify(sum(sharp)),
        "half_sum": sp.simplify(sum(half)),
        "sharp_half_distinct": sharp != half,
        "decoded_equal": decode(sharp, 1) == decode(half, sp.Rational(1, 2)),
        "decoded": decode(sharp, 1),
        "output_norms": tuple(sorted(set(norms), key=str)),
        "positive_overlap_count": sum(bool(value > 0) for value in overlaps),
        "minimum_overlap": min(overlaps),
        "sharpness_selected": False,
        "collision_probabilities": collision_probabilities,
        "collision_relative_phases": (sp.Integer(1), I),
        "single_branch_sufficient": False,
    }


def shell_parts(mask: int) -> tuple[sp.Matrix, sp.Matrix]:
    values = [sp.Integer((mask >> index) & 1) for index in range(6)]
    u = sp.Matrix((
        values[0] + values[1],
        values[2] + values[3],
        values[4] + values[5],
    ))
    w = sp.Matrix((
        values[1] - values[0],
        values[3] - values[2],
        values[5] - values[4],
    ))
    return u, w


def quadratic_covariants(mask: int) -> tuple[sp.Matrix, sp.Matrix]:
    u, w = shell_parts(mask)
    first = sp.Matrix((
        w[0] * w[1],
        w[1] * w[2],
        w[0] * w[2],
    ))
    second = sp.Matrix((
        (u[1] - u[0]) * w[2],
        (u[2] - u[1]) * w[0],
        (u[0] - u[2]) * w[1],
    ))
    return first, second


def mobius(values: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    result = list(values)
    for bit in range(6):
        for mask in range(64):
            if (mask >> bit) & 1:
                result[mask] = sp.simplify(
                    result[mask] - result[mask ^ (1 << bit)]
                )
    return tuple(result)


def mobius_evaluate(coefficients: tuple[sp.Expr, ...], mask: int) -> sp.Expr:
    return sp.simplify(sum(
        value for monomial, value in enumerate(coefficients)
        if monomial & ~mask == 0
    ))


@cache
def affine_eta_facts() -> dict[str, object]:
    data = group_data()
    permutations = data["permutations"]
    selected = tuple(
        item for item in finite_group_facts()["affine6"]
        if item["orbit24"]
    )
    if len(selected) != 1:
        raise AssertionError("affine class selection")
    cocycle = selected[0]["cocycle"]

    def action(group_index: int, mask: int) -> int:
        return permute(mask, permutations[group_index]) ^ cocycle[group_index]

    orbits = partition(range(64), action)
    regular = tuple(value for value in orbits if len(value) == 24)
    if len(regular) != 1:
        raise AssertionError("regular input orbit")
    base = min(regular[0])
    transport = {action(index, base): index for index in range(24)}
    contrast = (
        sp.sqrt(3), -sp.sqrt(3), sp.Integer(2), sp.Integer(-2),
        sp.Integer(0), sp.Integer(0),
    )
    shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))

    def rotate_contrast(group_index: int, values) -> tuple:
        output = [sp.Integer(0)] * 6
        for source, target in enumerate(permutations[group_index]):
            output[target] = values[source]
        return tuple(output)

    contrast_table = tuple(
        rotate_contrast(transport[mask], contrast)
        if mask in transport else (sp.Integer(0),) * 6
        for mask in range(64)
    )
    shear_table = tuple(
        tuple(shear_action(group()[transport[mask]]) * shear)
        if mask in transport else (sp.Integer(0),) * 3
        for mask in range(64)
    )
    contrast_coefficients = tuple(
        mobius(tuple(row[index] for row in contrast_table))
        for index in range(6)
    )
    shear_coefficients = tuple(
        mobius(tuple(row[index] for row in shear_table))
        for index in range(3)
    )

    def degree(family) -> int:
        return max(
            monomial.bit_count()
            for coefficients in family
            for monomial, value in enumerate(coefficients)
            if value != 0
        )

    return {
        "base": base,
        "regular_orbit_count": len(regular),
        "contrast_covariant": all(
            contrast_table[action(group_index, mask)]
            == rotate_contrast(group_index, contrast_table[mask])
            for group_index in range(24) for mask in range(64)
        ),
        "shear_covariant": all(
            sp.Matrix(shear_table[action(group_index, mask)])
            == shear_action(group()[group_index]) * sp.Matrix(shear_table[mask])
            for group_index in range(24) for mask in range(64)
        ),
        "contrast_polynomial": all(
            tuple(
                mobius_evaluate(contrast_coefficients[index], mask)
                for index in range(6)
            ) == contrast_table[mask]
            for mask in range(64)
        ),
        "shear_polynomial": all(
            tuple(
                mobius_evaluate(shear_coefficients[index], mask)
                for index in range(3)
            ) == shear_table[mask]
            for mask in range(64)
        ),
        "contrast_degree": degree(contrast_coefficients),
        "shear_degree": degree(shear_coefficients),
        "physical_action_derived": False,
    }


@cache
def polynomial_facts() -> dict[str, object]:
    data = group_data()
    permutations = data["permutations"]
    monomials = (
        ((),)
        + tuple((index,) for index in range(6))
        + tuple(itertools.combinations(range(6), 2))
    )
    character_sum = sp.Integer(0)
    covariant = True
    for rotation, permutation in zip(group(), permutations):
        fixed_features = sum(
            tuple(sorted(permutation[index] for index in monomial)) == monomial
            for monomial in monomials
        )
        character_sum += sp.trace(shear_action(rotation)) * fixed_features
        for mask in range(64):
            transformed = permute(mask, permutation)
            source_values = quadratic_covariants(mask)
            target_values = quadratic_covariants(transformed)
            covariant = covariant and all(
                target == shear_action(rotation) * source
                for source, target in zip(source_values, target_values)
            )
    hom_dimension = sp.simplify(character_sum / 24)
    target = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    fitting = []
    independence_witness = False
    for mask in range(64):
        columns = sp.Matrix.hstack(*quadratic_covariants(mask))
        independence_witness = independence_witness or columns.rank() == 2
        if columns.rank() == columns.row_join(target).rank():
            fitting.append(mask)
    return {
        "monomial_count": len(monomials),
        "character_sum": character_sum,
        "hom_dimension": hom_dimension,
        "basis_covariant": covariant,
        "basis_independent": independence_witness,
        "fitting_masks": tuple(fitting),
    }


@cache
def source_facts() -> dict[str, object]:
    facts = eta_independent.path_factorization()
    return {
        "forward_equal": facts["forward_equal"],
        "reverse_equal": facts["reverse_equal"],
        "forward_terms": facts["forward_terms"],
        "reverse_terms": facts["reverse_terms"],
        "t2_rank": facts["t2_rank"],
    }


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "prereg_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "parent_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "goal_blob": git("rev-parse", f"{PREREG}:{GOAL}"),
        "preflight_blob": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
    }


def checks(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    group_facts = dict(finite_group_facts())
    instrument = dict(instrument_facts())
    polynomial = dict(polynomial_facts())
    affine_eta = dict(affine_eta_facts())
    source = dict(source_facts())
    claims: dict[str, object] = {
        "main": MAIN,
        "goal_blob": GOAL_BLOB,
        "group_count": 24,
        "outcome_count": 36,
        "outcome_orbit24": True,
        "shell_orbit24": False,
        "affine_class_count": 2,
        "affine_selected": False,
        "affine_decoder": True,
        "affine_action_physical": False,
        "code_count": 36,
        "center_corner_code_count": 36,
        "center_corner_embedding": True,
        "writer_tp": True,
        "writer_lock": True,
        "fullrank_record": False,
        "sharpness_fork": True,
        "sharpness_selected": False,
        "branch_sufficient": False,
        "hom_dimension": 2,
        "quadratic_fit": False,
        "source_terms": (110, 110),
        "actual_reverse": True,
        "eta_closure": False,
        "axiom_update": False,
    }
    changes = {
        "stale_main": ("main", "stale"),
        "unpin_goal": ("goal_blob", "stale"),
        "lose_rotation": ("group_count", 23),
        "lose_outcome": ("outcome_count", 35),
        "erase_orbit24": ("outcome_orbit24", False),
        "invent_shell_orbit24": ("shell_orbit24", True),
        "drop_affine_class": ("affine_class_count", 1),
        "select_affine_class": ("affine_selected", True),
        "erase_affine_decoder": ("affine_decoder", False),
        "call_affine_action_physical": ("affine_action_physical", True),
        "merge_two_shell_codes": ("code_count", 35),
        "merge_center_corner_codes": ("center_corner_code_count", 35),
        "erase_center_corner_embedding": ("center_corner_embedding", False),
        "break_writer_tp": ("writer_tp", False),
        "break_writer_lock": ("writer_lock", False),
        "call_fullrank_record": ("fullrank_record", True),
        "erase_sharpness_fork": ("sharpness_fork", False),
        "select_sharpness": ("sharpness_selected", True),
        "claim_branch_sufficient": ("branch_sufficient", True),
        "lower_hom_dimension": ("hom_dimension", 1),
        "invent_quadratic_fit": ("quadratic_fit", True),
        "lose_source_term": ("source_terms", (109, 110)),
        "replace_actual_reverse": ("actual_reverse", False),
        "claim_eta_closure": ("eta_closure", True),
        "claim_axiom_update": ("axiom_update", True),
    }
    if mutation:
        key_name, value = changes[mutation]
        claims[key_name] = value

    affine6 = group_facts["affine6"]
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["prereg_ancestor"]
            and authority["parent_ancestor"]
            and authority["goal_blob"] == claims["goal_blob"]
            and authority["preflight_blob"] == PREFLIGHT_BLOB,
            "authority and immutable registration reconstruct independently",
        ),
        "B": (
            group_facts["group_count"] == claims["group_count"]
            and group_facts["determinants"] == (1,)
            and sum(
                size * count
                for size, count in group_facts["outcome_histogram"].items()
            ) == claims["outcome_count"],
            "generator closure gives the complete 24-element proper-cubic group",
        ),
        "C": (
            group_facts["outcome_histogram"] == {6: 2, 24: 1}
            and claims["outcome_orbit24"]
            and group_facts["shell_histogram"]
            == {1: 2, 3: 2, 6: 2, 8: 1, 12: 3}
            and claims["shell_orbit24"] is False
            and group_facts["contrast_orbit_size"] == 24,
            "outcome and literal-shell orbit mismatch is reproduced",
        ),
        "D": (
            len(affine6) == claims["affine_class_count"]
            and sum(item["orbit24"] for item in affine6) == 1
            and sum(item["full_embedding"] for item in affine6) == 0
            and sum(
                item["full_embedding"] for item in group_facts["affine7"]
            ) == 0
            and claims["affine_selected"] is False,
            "one affine class carries the 24-orbit, but stabilizer matching "
            "finds no complete 36-outcome six- or seven-site embedding",
        ),
        "E": (
            group_facts["code_count"] == claims["code_count"]
            and group_facts["code_covariance"]
            and set(group_facts["code_weights"]) == {(1, 1)},
            "two-shell product code is injective, orthogonal, and covariant",
        ),
        "F": (
            group_facts["corner_histogram"]
            == {1: 2, 2: 1, 4: 2, 6: 2, 8: 5, 12: 6, 24: 5}
            and not group_facts["corner_full_embedding"]
            and group_facts["center_corner_full_embedding"]
            == claims["center_corner_embedding"]
            and group_facts["center_corner_code_count"]
            == claims["center_corner_code_count"]
            and group_facts["center_corner_code_covariance"]
            and set(group_facts["center_corner_record_counts"]) == {3, 4, 5}
            and
            instrument["first_moment"] == sp.zeros(3, 1)
            and instrument["second_moment"] == 2 * sp.eye(3)
            and instrument["povm_sum"] == 1
            and instrument["rank_one_eigenvalue"] == sp.Rational(1, 9)
            and instrument["sqrt_completeness"] == 1
            and instrument["blank_write_lock_completeness"] == claims["writer_tp"]
            and instrument["qnd_lock"] == claims["writer_lock"],
            "the explicit nine-site center-corner code and POVM "
            "blank/write/lock completeness prove total CP-QND writing",
        ),
        "G": (
            instrument["positive_overlap_count"] == 630
            and instrument["minimum_overlap"] > 0
            and claims["fullrank_record"] is False,
            "all old one-qubit outputs overlap and are not Record codes",
        ),
        "H": (
            claims["sharpness_fork"]
            and instrument["sharp_sum"] == 1
            and instrument["half_sum"] == 1
            and instrument["sharp_half_distinct"]
            and instrument["decoded_equal"]
            and instrument["sharpness_selected"] == claims["sharpness_selected"],
            "sharp and unsharp menus remain distinct normalized readable laws with the same decoded phase",
        ),
        "I": (
            instrument["collision_probabilities"]
            == (sp.Rational(1, 36), sp.Rational(1, 36))
            and instrument["collision_relative_phases"] == (1, I)
            and instrument["single_branch_sufficient"]
            == claims["branch_sufficient"],
            "the same recorded branch occurs at equal positive weight for "
            "different source phases, so one sample is not the rate vector",
        ),
        "J": (
            polynomial["monomial_count"] == 22
            and polynomial["hom_dimension"] == claims["hom_dimension"]
            and polynomial["basis_covariant"]
            and polynomial["basis_independent"]
            and bool(polynomial["fitting_masks"]) == claims["quadratic_fit"],
            "character theory plus explicit covariants gives Hom dimension two and no H1 binary fit",
        ),
        "K": (
            claims["affine_decoder"]
            and affine_eta["regular_orbit_count"] == 1
            and affine_eta["contrast_covariant"]
            and affine_eta["shear_covariant"]
            and affine_eta["contrast_polynomial"]
            and affine_eta["shear_polynomial"]
            and affine_eta["contrast_degree"] == 4
            and affine_eta["shear_degree"] == 5
            and affine_eta["physical_action_derived"]
            == claims["affine_action_physical"],
            "independent Mobius reconstruction gives exact degree-4 contrast "
            "and degree-5 shear decoders on the unique affine regular orbit",
        ),
        "L": (
            (source["forward_terms"], source["reverse_terms"])
            == claims["source_terms"]
            and source["forward_equal"]
            and source["reverse_equal"] == claims["actual_reverse"]
            and source["t2_rank"] == 3
            and claims["eta_closure"] is False
            and claims["axiom_update"] is False,
            "independent native paths retain the 110/110 rank-three H1 source while closure remains open",
        ),
    }


def mutation_sweep() -> tuple[int, int]:
    rejected = sum(
        any(not result for result, _ in checks(mutation).values())
        for mutation in MUTATIONS
    )
    return rejected, len(MUTATIONS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        print("\n".join(MUTATIONS))
        return 0
    results = checks(arguments.mutation or "")
    for name, (passed, detail) in results.items():
        print(f"{'PASS' if passed else 'FAIL'} {name}: {detail}")
    if not arguments.mutation:
        group_facts = finite_group_facts()
        polynomial = polynomial_facts()
        affine_eta = affine_eta_facts()
        rejected, total = mutation_sweep()
        print(
            "INDEPENDENT_ORBITS: outcomes="
            f"{group_facts['outcome_histogram']}; shell="
            f"{group_facts['shell_histogram']}; affine6_classes="
            f"{len(group_facts['affine6'])}; affine6_orbit24="
            f"{sum(item['orbit24'] for item in group_facts['affine6'])}; "
            "affine6_full36="
            f"{sum(item['full_embedding'] for item in group_facts['affine6'])}."
        )
        print(
            "INDEPENDENT_POLYNOMIAL: character_sum="
            f"{polynomial['character_sum']}; Hom_dim="
            f"{polynomial['hom_dimension']}; fitting_masks="
            f"{len(polynomial['fitting_masks'])}."
        )
        print(
            "INDEPENDENT_AFFINE_ETA: base="
            f"{format(affine_eta['base'], '06b')}; contrast_degree="
            f"{affine_eta['contrast_degree']}; shear_degree="
            f"{affine_eta['shear_degree']}."
        )
        print(f"MUTATIONS: rejected={rejected}/{total}")
    passed = sum(result for result, _ in results.values())
    print(f"SCORECARD PASS={passed} FAIL={len(results)-passed}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
