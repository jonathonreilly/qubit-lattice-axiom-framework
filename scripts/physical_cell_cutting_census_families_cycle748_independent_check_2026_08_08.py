"""Independent Cycle 748 census and family checker.

This executable imports no symbols from the primary.  It reconstructs the exact-cover
population with the opposite pivot convention, rebuilds the geometric column action,
validates the two extra generators against the incidence and the four target, and
independently re-derives the complete weight-sixteen census, its group families, the
weight-twenty XOR family, and the conditional weight-eighteen shape bound.
"""
import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = (
    "scripts/physical_cell_cutting_census_families_cycle748_"
    "independent_check_2026_08_08.py"
)
PRIMARY_PATH = "scripts/physical_cell_cutting_census_families_cycle748_2026_08_08.py"
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_CENSUS_FAMILIES_CYCLE748_NOTE_2026-08-08.md"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_census_families_cycle748_2026_08_08_"
    "receipt_2026-08-08.json"
)
C746_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md"
)
C746_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py"
)
C746_CHECKER_PATH = (
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08.py"
)
C746_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_"
    "receipt_2026-08-08.json"
)
C746_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
C747_NOTE_PATH = (
    "docs/PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_"
    "CYCLE747_NOTE_2026-08-08.md"
)
C747_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py"
)
C747_CHECKER_PATH = (
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "independent_check_2026_08_08.py"
)
C747_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "2026_08_08_receipt_2026-08-08.json"
)
C747_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_"
    "independent_check_2026_08_08_receipt_2026-08-08.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_census_families_cycle748_independent_check_"
    "2026_08_08_receipt_2026-08-08.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_CENSUS_FAMILIES_CYCLE748_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_census_families_cycle748_2026_08_08.py",
    "outputs/physical_cell_cutting_census_families_cycle748_2026_08_08_receipt_2026-08-08.json",
    "docs/PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py",
    "scripts/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08.py",
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08_receipt_2026-08-08.json",
    "outputs/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08_receipt_2026-08-08.json",
    "docs/PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md",
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py",
    "scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_independent_check_2026_08_08.py",
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08_receipt_2026-08-08.json",
    "outputs/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_independent_check_2026_08_08_receipt_2026-08-08.json",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == sha256(path)
        for path in recorded
    )


def supports_sha256(supports):
    rows = sorted(tuple(sorted(int(value) for value in row)) for row in supports)
    return hashlib.sha256(
        json.dumps(rows, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def write_failure(reason):
    RECEIPT_PATH.write_text(json.dumps({
        "schema": "physical-cell-cutting-census-families-cycle748-independent-v1",
        "status": "fail",
        "claim_type": "bounded_theorem",
        "reason": reason,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


write_failure("checker has not completed")
PRIMARY = load(PRIMARY_RECEIPT_PATH)
C746 = load(C746_RECEIPT_PATH)
C746I = load(C746_INDEPENDENT_RECEIPT_PATH)
C747 = load(C747_RECEIPT_PATH)
C747I = load(C747_INDEPENDENT_RECEIPT_PATH)

passed = 0
failed = 0
gates = {}


def gate(name, condition, detail):
    global passed, failed
    ok = bool(condition)
    gates[name] = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    else:
        failed += 1
    compact = detail if len(detail) <= 100 else detail[:97] + "..."
    print(("PASS " if ok else "FAIL ") + name + "  " + compact, flush=True)


# Reconstruct the object independently.  The primary chooses the least uncovered
# sample; this checker deliberately chooses the greatest.
def det4(array):
    def minors(row0, row1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (
                    array[:, row0, i] * array[:, row1, j]
                    - array[:, row0, j] * array[:, row1, i]
                )
        return out

    left = minors(0, 1)
    right = minors(2, 3)
    return (
        left[(0, 1)] * right[(2, 3)]
        - left[(0, 2)] * right[(1, 3)]
        + left[(0, 3)] * right[(1, 2)]
        + left[(1, 2)] * right[(0, 3)]
        - left[(1, 3)] * right[(0, 2)]
        + left[(2, 3)] * right[(0, 1)]
    )


corners = [
    (x, y, z, t)
    for x in (0, 1)
    for y in (0, 1)
    for z in (0, 1)
    for t in (0, 1)
]
vectors = np.array(corners, dtype=np.int64)
pairs = list(itertools.combinations(range(5), 2))
subsets = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
volume = np.abs(det4(vectors[subsets[:, 1:]] - vectors[subsets[:, 0]][:, None, :]))
unimodular = subsets[volume == 1]


def adjacency_cost(pieces):
    total = np.zeros(len(pieces), dtype=np.int64)
    for left, right in pairs:
        distance = np.abs(
            vectors[pieces[:, left]] - vectors[pieces[:, right]]
        ).sum(axis=1)
        total += (distance > 1).astype(np.int64)
    return total


costs = adjacency_cost(unimodular)
least_cost = int(costs.min())
minimum_pieces = [
    index for index in range(len(unimodular)) if int(costs[index]) == least_cost
]
matrices = np.stack([
    (vectors[piece[1:]] - vectors[piece[0]]).T for piece in unimodular
])
inverse = np.rint(np.linalg.inv(matrices.astype(float))).astype(np.int64)
corner_position = {corner: index for index, corner in enumerate(corners)}
rotations = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(permutation):
            rotation[i, j] = signs[i]
        if int(round(np.linalg.det(rotation.astype(float)))) == 1:
            rotations.append(rotation)
center = np.array([1, 1, 1], dtype=np.int64)
geometry = []
for rotation in rotations:
    for time_flip in (0, 1):
        image = []
        for x, y, z, t in corners:
            point = rotation @ (
                2 * np.array([x, y, z], dtype=np.int64) - center
            ) + center
            key = (
                int(point[0]) // 2,
                int(point[1]) // 2,
                int(point[2]) // 2,
                (1 - t) if time_flip else t,
            )
            image.append(corner_position[key])
        geometry.append((rotation, time_flip, np.array(image, dtype=np.int64)))
piece_index = {
    tuple(int(corner) for corner in support): index
    for index, support in enumerate(unimodular)
}
orbit_label = -np.ones(len(unimodular), dtype=np.int64)
representatives = []
for index in range(len(unimodular)):
    if orbit_label[index] >= 0:
        continue
    label = len(representatives)
    representatives.append(index)
    for _rotation, _time_flip, image in geometry:
        transformed = tuple(sorted(int(image[corner]) for corner in unimodular[index]))
        orbit_label[piece_index[transformed]] = label
offsets = np.array([0, 1, 7, 49, 343], dtype=np.int64)
bound = max(
    int(np.abs(inverse).max()),
    int(np.abs(inverse.sum(axis=2) - 1).max()),
)
weights = 2 * (bound * int(offsets.sum()) + 1 + offsets)
scale = int(weights.sum())
spatial_center = np.array([scale // 2, scale // 2, scale // 2], dtype=np.int64)
samples = set()
for index in representatives:
    barycenter = (weights[:, None] * vectors[unimodular[index]]).sum(axis=0)
    for rotation, time_flip, _image in geometry:
        spatial = rotation @ (barycenter[:3] - spatial_center) + spatial_center
        samples.add((
            int(spatial[0]),
            int(spatial[1]),
            int(spatial[2]),
            scale - int(barycenter[3]) if time_flip else int(barycenter[3]),
        ))
sample_array = np.array(sorted(samples), dtype=np.int64)
sample_t = sample_array.T
inside_masks = [0] * len(unimodular)
by_sample = {}
for index in minimum_pieces:
    lam = inverse[index] @ (
        sample_t - (scale * vectors[unimodular[index, 0]])[:, None]
    )
    total = lam.sum(axis=0)
    inside = (lam > 0).all(axis=0) & (total < scale)
    mask = 0
    for sample in np.flatnonzero(inside):
        sample = int(sample)
        mask |= 1 << sample
        by_sample.setdefault(sample, []).append(index)
    inside_masks[index] = mask

all_samples = (1 << len(sample_array)) - 1
solutions = []


def exact_cover(covered, chosen):
    if covered == all_samples:
        solutions.append(tuple(sorted(chosen)))
        return
    remaining = all_samples & ~covered
    sample = remaining.bit_length() - 1
    for index in by_sample[sample]:
        mask = inside_masks[index]
        if mask & covered:
            continue
        chosen.append(index)
        exact_cover(covered | mask, chosen)
        chosen.pop()


exact_cover(0, [])
used = sorted(set(index for solution in solutions for index in solution))
piece_to_column = {piece: column for column, piece in enumerate(used)}
incidence = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    for piece in solution:
        incidence[row, piece_to_column[piece]] = 1
row_weight = sorted(set(int(value) for value in incidence.sum(axis=1)))
column_weight = sorted(set(int(value) for value in incidence.sum(axis=0)))
gate(
    "independent.population",
    len(solutions) == 15800
    and len(used) == 192
    and row_weight == [24]
    and column_weight == [1975],
    "opposite-pivot reconstruction gives 15800 rows, 192 columns, weights 24 and 1975",
)

target_identity = C746.get("direct_dependency", {}).get("target_identity", {})
targets = target_identity.get("targets", {})
four_support = targets.get("four", {}).get("witness_support")
four = (incidence[:, four_support].sum(axis=1) & 1).astype(np.uint8)
four_flip = four ^ 1
one = np.ones(len(solutions), dtype=np.uint8)
gate(
    "independent.targets",
    int(four.sum()) == 5664
    and int(four_flip.sum()) == 10136
    and targets.get("four", {}).get("ones") == 5664
    and targets.get("four-flip", {}).get("ones") == 10136,
    "the reconstructed four target and its complement reproduce the landed target identity",
)

# Enumerate the exact all-marked weight-eight family independently.
integer_incidence = incidence.astype(np.int32)
cooccurrence = integer_incidence.T @ integer_incidence
nonsharing = cooccurrence == 0
np.fill_diagonal(nonsharing, False)
adjacency = []
for column in range(192):
    mask = 0
    for other in range(192):
        if nonsharing[column, other]:
            mask |= 1 << other
    adjacency.append(mask)
all_marked = []


def extend_clique(chosen, candidates):
    if len(chosen) == 8:
        all_marked.append(tuple(chosen))
        return
    while candidates:
        low = candidates & -candidates
        column = low.bit_length() - 1
        candidates ^= low
        if len(chosen) + 1 + candidates.bit_count() < 8:
            return
        chosen.append(column)
        extend_clique(chosen, candidates & adjacency[column])
        chosen.pop()


extend_clique([], (1 << 192) - 1)
all_marked = sorted(set(all_marked))
all_marked_semantic = all(
    np.array_equal(
        (incidence[:, list(support)].sum(axis=1) & 1).astype(np.uint8), one
    )
    for support in all_marked
)
through_all_marked = sorted(set(
    sum(column in support for support in all_marked) for column in range(192)
))
gate(
    "independent.all_marked",
    8 * 1975 == 15800
    and len(all_marked) == 192
    and all_marked_semantic
    and through_all_marked == [8]
    and all_marked == sorted(
        tuple(row) for row in C747.get("all_marked_weight_eight", {}).get("carriers", [])
    ),
    "exact clique enumeration reproduces all 192 landed all-marked carriers",
)

# Rebuild the 48 geometric column permutations and verify their row/target actions.
column_permutations = []
for _rotation, _time_flip, image in geometry:
    permutation = []
    for piece in used:
        transformed = tuple(sorted(int(image[corner]) for corner in unimodular[piece]))
        permutation.append(piece_to_column[piece_index[transformed]])
    column_permutations.append(np.array(permutation, dtype=np.int64))
row_lookup = {
    tuple(int(value) for value in np.flatnonzero(incidence[row])): row
    for row in range(len(solutions))
}


def action_contract(permutation):
    if sorted(int(value) for value in permutation) != list(range(192)):
        return False
    for row in range(len(solutions)):
        support = np.flatnonzero(incidence[row])
        image = tuple(sorted(int(permutation[value]) for value in support))
        target_row = row_lookup.get(image)
        if target_row is None or four[target_row] != four[row]:
            return False
    return True


witness = PRIMARY.get("symmetry_witness", {})
b0 = np.array(witness.get("extra_generator_b0", []), dtype=np.int64)
b1 = np.array(witness.get("extra_generator_b1", []), dtype=np.int64)
actions_ok = (
    len(b0) == len(b1) == 192
    and all(action_contract(permutation) for permutation in column_permutations)
    and action_contract(b0)
    and action_contract(b1)
)
gate(
    "independent.symmetry_actions",
    actions_ok,
    "all 48 geometric maps and both extra generators preserve the incidence rows and four target",
)


def closure(generators):
    identity = tuple(range(192))
    seen = {identity}
    front = [identity]
    group = [np.arange(192, dtype=np.int64)]
    while front:
        following = []
        for element in front:
            element_array = np.array(element, dtype=np.int64)
            for generator in generators:
                product = tuple(int(value) for value in generator[element_array])
                if product not in seen:
                    seen.add(product)
                    following.append(product)
                    group.append(np.array(product, dtype=np.int64))
        front = following
    return group


def piece_orbits(generators):
    parent = list(range(192))

    def root(value):
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    for permutation in generators:
        for value in range(192):
            left, right = root(value), root(int(permutation[value]))
            if left != right:
                parent[left] = right
    counts = {}
    for value in range(192):
        counts[root(value)] = counts.get(root(value), 0) + 1
    return sorted(counts.values())


def family_sizes(family, group):
    universe = set(family)
    done = set()
    sizes = []
    for support in sorted(universe, key=lambda row: sorted(row)):
        if support in done:
            continue
        orbit = {
            frozenset(int(element[value]) for value in support) for element in group
        }
        if not orbit <= universe:
            return []
        done |= orbit
        sizes.append(len(orbit))
    return sorted(sizes)


geometric_orbits = piece_orbits(column_permutations)
generators = column_permutations + [b0, b1]
group = closure(generators)
generated_orbits = piece_orbits(generators)
gate(
    "independent.group",
    geometric_orbits == [48, 48, 48, 48]
    and len(group) == 384
    and generated_orbits == [192],
    "the independently rebuilt generators close to order 384 and are transitive only with b0 and b1",
)

anchored = sorted(
    tuple(int(value) for value in row)
    for row in C747.get("weight_twenty_construction", {}).get("four_carriers", [])
)
anchored_ok = len(anchored) == 11 and all(
    len(row) == 16
    and 144 in row
    and np.array_equal(
        (incidence[:, list(row)].sum(axis=1) & 1).astype(np.uint8), four
    )
    for row in anchored
)
census = sorted(
    {
        frozenset(int(element[value]) for value in support)
        for support in anchored
        for element in group
    },
    key=lambda row: sorted(row),
)
census_semantic = all(
    len(row) == 16
    and np.array_equal(
        (incidence[:, list(row)].sum(axis=1) & 1).astype(np.uint8), four
    )
    for row in census
)
census_through = sorted(set(
    sum(column in support for support in census) for column in range(192)
))
census_families = family_sizes(set(census), group)
gate(
    "independent.complete_census",
    anchored_ok
    and C747.get("exact_search_through_sixteen", {}).get("all_sweeps_complete") is True
    and len(census) == 132
    and census_semantic
    and census_through == [11]
    and census_families == [12, 12, 12, 24, 24, 48],
    "transitivity and the exact eleven-carrier anchor census give all 132 carriers in six families",
)

overlap_counts = {}
profiles = {}
twenty = set()
for carrier in census:
    profile = {}
    for all_one in all_marked:
        overlap = len(carrier & frozenset(all_one))
        overlap_counts[overlap] = overlap_counts.get(overlap, 0) + 1
        profile[overlap] = profile.get(overlap, 0) + 1
        if overlap == 2:
            twenty.add(carrier ^ frozenset(all_one))
    key = tuple(sorted(profile.items()))
    profiles[key] = profiles.get(key, 0) + 1
twenty_semantic = all(
    len(row) == 20
    and np.array_equal(
        (incidence[:, list(row)].sum(axis=1) & 1).astype(np.uint8), four_flip
    )
    for row in twenty
)
twenty_through = sorted(set(
    sum(column in support for support in twenty) for column in range(192)
))
twenty_families = family_sizes(twenty, group)
gate(
    "independent.overlaps_and_twenty",
    overlap_counts == {0: 14592, 1: 4608, 2: 6144}
    and sorted(profiles.values()) == [12, 12, 24, 36, 48]
    and len(twenty) == 6144
    and twenty_semantic
    and twenty_through == [640]
    and twenty_families.count(192) == 20
    and twenty_families.count(384) == 6
    and len(twenty_families) == 26,
    "all 25344 overlaps give five profiles and 6144 distinct semantic weight-twenty carriers in 26 families",
)

allowed_intersections = [
    overlap
    for overlap in range(9)
    if 26 - 2 * overlap >= 16
    and not (26 - 2 * overlap == 16 and 8 - overlap > 2)
]
gate(
    "independent.weight_eighteen_boundary",
    allowed_intersections == [0, 1, 2, 3, 4]
    and C747.get("minimum_bracket", {}).get("weight_eighteen_resolved") is False,
    "the weight-16 lower bound and system-wide overlap cap imply only the conditional k<=4 shape bound",
)


def cycle746_contract(primary, independent):
    supplied = primary.get("supplied_incidence", {})
    reconstructed = independent.get("independent_reconstruction", {})
    return (
        primary.get("schema") == "physical-cell-cutting-carrier-parity-law-cycle746-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C746_PRIMARY_PATH)
        and inputs_current(primary)
        and supplied.get("cuttings") == 15800
        and supplied.get("support_columns") == 192
        and supplied.get("processed_pair_rows") == 15800
        and independent.get("schema")
        == "physical-cell-cutting-carrier-parity-law-cycle746-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and (independent.get("checker_sha256") or independent.get("runner_sha256"))
        == sha256(C746_CHECKER_PATH)
        and inputs_current(independent)
        and reconstructed.get("cuttings") == 15800
        and reconstructed.get("support_columns") == 192
    )


def cycle747_contract(primary, independent):
    search = primary.get("exact_search_through_sixteen", {})
    bracket = primary.get("minimum_bracket", {})
    return (
        primary.get("schema")
        == "physical-cell-cutting-flip-partner-carrier-bracket-cycle747-v2"
        and primary.get("status") == "pass"
        and primary.get("gates", {}).get("fail") == 0
        and primary.get("runner_sha256") == sha256(C747_PRIMARY_PATH)
        and inputs_current(primary)
        and primary.get("supplied_incidence", {}).get("processed_pair_rows") == 15800
        and primary.get("all_marked_weight_eight", {}).get("carrier_count") == 192
        and search.get("all_sweeps_complete") is True
        and search.get("four_counts") == [0, 0, 0, 0, 0, 0, 0, 11]
        and search.get("four_flip_counts") == [0] * 8
        and bracket.get("weight_eighteen_resolved") is False
        and independent.get("schema")
        == "physical-cell-cutting-flip-partner-carrier-bracket-cycle747-independent-v1"
        and independent.get("status") == "pass"
        and independent.get("gates", {}).get("fail") == 0
        and (independent.get("checker_sha256") or independent.get("runner_sha256"))
        == sha256(C747_CHECKER_PATH)
        and inputs_current(independent)
        and independent.get("independent_reconstruction", {}).get("anchored_four_count") == 11
        and independent.get("dependency_boundary", {}).get("weight_eighteen_resolved") is False
    )


DEPENDENCIES_OK = cycle746_contract(C746, C746I) and cycle747_contract(C747, C747I)
gate(
    "independent.dependencies",
    DEPENDENCIES_OK,
    "exact current primary and independent receipts from landed Cycles 746 and 747 are bound fail-closed",
)


def primary_contract(receipt):
    supplied = receipt.get("supplied_incidence", {})
    symmetry = receipt.get("symmetry_witness", {})
    weight_sixteen = receipt.get("weight_sixteen_census", {})
    overlap = receipt.get("all_marked_overlap", {})
    weight_twenty = receipt.get("weight_twenty_construction", {})
    shape = receipt.get("weight_eighteen_shape_boundary", {})
    dependencies = receipt.get("direct_dependencies", {})
    primary_census = sorted(
        frozenset(int(value) for value in row)
        for row in weight_sixteen.get("complete_carriers", [])
    )
    return (
        receipt.get("schema") == "physical-cell-cutting-census-families-cycle748-v2"
        and receipt.get("status") == "pass"
        and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and inputs_current(receipt)
        and supplied == {
            "cuttings": 15800,
            "support_columns": 192,
            "pieces_per_cutting": 24,
            "cuttings_per_piece": 1975,
            "processed_pair_rows": 15800,
        }
        and symmetry.get("geometric_piece_orbits") == geometric_orbits
        and symmetry.get("extra_generator_b0") == b0.tolist()
        and symmetry.get("extra_generator_b1") == b1.tolist()
        and symmetry.get("generated_group_order") == len(group) == 384
        and symmetry.get("generated_piece_orbits") == generated_orbits == [192]
        and symmetry.get("all_marked_family_stable") is True
        and primary_census == census
        and weight_sixteen.get("complete_carrier_count") == len(census) == 132
        and weight_sixteen.get("complete_carriers_sha256") == supports_sha256(census)
        and weight_sixteen.get("carriers_through_each_piece") == 11
        and weight_sixteen.get("direct_recheck_failures") == 0
        and weight_sixteen.get("group_family_sizes") == census_families
        and weight_sixteen.get("overlap_profile_sizes") == sorted(profiles.values())
        and overlap.get("pair_count") == 25344
        and overlap.get("maximum") == 2
        and overlap.get("counts") == {"0": 14592, "1": 4608, "2": 6144}
        and weight_twenty.get("cap_overlap_pairs") == 6144
        and weight_twenty.get("distinct_carrier_count") == len(twenty) == 6144
        and weight_twenty.get("distinct_carriers_sha256") == supports_sha256(twenty)
        and weight_twenty.get("carriers_through_each_piece") == 640
        and weight_twenty.get("direct_recheck_failures") == 0
        and weight_twenty.get("group_family_sizes") == twenty_families
        and shape == {
            "existence_resolved": False,
            "maximum_intersection_with_all_marked_weight_eight": 4,
            "four_minimum": 16,
            "four_all_marked_overlap_cap": 2,
        }
        and dependencies.get("cycle746", {}).get("receipt_sha256")
        == sha256(C746_RECEIPT_PATH)
        and dependencies.get("cycle746", {}).get("independent_receipt_sha256")
        == sha256(C746_INDEPENDENT_RECEIPT_PATH)
        and dependencies.get("cycle747", {}).get("receipt_sha256")
        == sha256(C747_RECEIPT_PATH)
        and dependencies.get("cycle747", {}).get("independent_receipt_sha256")
        == sha256(C747_INDEPENDENT_RECEIPT_PATH)
    )


PRIMARY_OK = primary_contract(PRIMARY)
gate(
    "independent.primary_contract",
    DEPENDENCIES_OK and PRIMARY_OK,
    "the primary receipt equals the independent census, family, overlap, and conditional-bound derivations",
)

bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate("hostile.primary_status", not primary_contract(bad_primary), "a failing primary receipt is rejected")
bad_generator = copy.deepcopy(PRIMARY)
bad_generator["symmetry_witness"]["extra_generator_b0"][0] ^= 1
gate("hostile.generator", not primary_contract(bad_generator), "a changed symmetry generator is rejected")
bad_census = copy.deepcopy(PRIMARY)
bad_census["weight_sixteen_census"]["complete_carriers"][0][0] ^= 1
gate("hostile.census", not primary_contract(bad_census), "a changed census carrier is rejected")
bad_twenty = copy.deepcopy(PRIMARY)
bad_twenty["weight_twenty_construction"]["distinct_carriers_sha256"] = "0" * 64
gate("hostile.twenty", not primary_contract(bad_twenty), "a changed weight-twenty family digest is rejected")
bad_shape = copy.deepcopy(PRIMARY)
bad_shape["weight_eighteen_shape_boundary"]["existence_resolved"] = True
gate("hostile.shape_boundary", not primary_contract(bad_shape), "a false weight-eighteen resolution is rejected")
bad_c746 = copy.deepcopy(C746)
bad_c746["supplied_incidence"]["processed_pair_rows"] = 7900
gate(
    "hostile.predecessor_inventory",
    not cycle746_contract(bad_c746, C746I),
    "a predecessor receipt reverting to the half-row inventory is rejected",
)
bad_c747 = copy.deepcopy(C747)
bad_c747["exact_search_through_sixteen"]["all_sweeps_complete"] = False
gate(
    "hostile.predecessor_completeness",
    not cycle747_contract(bad_c747, C747I),
    "a predecessor receipt losing anchored completeness is rejected",
)

print("per_element: checked -- all 192 columns enter the independent incidence, group, census, and overlap calculations", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- the finite binary object has no modes", flush=True)
print("per_block: checked -- all 15800 rows and the exact landed anchored search are bound", flush=True)
print("lattice_wide: checked and not executed -- no multicell or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-census-families-cycle748-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(solutions),
        "support_columns": len(used),
        "pieces_per_cutting": row_weight[0],
        "cuttings_per_piece": column_weight[0],
        "exact_cover_pivot": "greatest uncovered sample",
        "all_marked_weight_eight_count": len(all_marked),
        "geometric_piece_orbits": geometric_orbits,
        "generated_group_order": len(group),
        "generated_piece_orbits": generated_orbits,
        "weight_sixteen_census_count": len(census),
        "weight_sixteen_family_sizes": census_families,
        "overlap_counts": {str(key): value for key, value in sorted(overlap_counts.items())},
        "overlap_profile_sizes": sorted(profiles.values()),
        "weight_twenty_count": len(twenty),
        "weight_twenty_family_sizes": twenty_families,
        "weight_eighteen_maximum_all_marked_intersection": max(allowed_intersections),
    },
    "dependency_boundary": {
        "cycle746_and_independent_bound": DEPENDENCIES_OK,
        "cycle747_and_independent_bound": DEPENDENCIES_OK,
        "weight_eighteen_resolved": False,
    },
    "no_go_discipline": {
        "status": "PASS",
        "n5_execution_certificate": [
            "per_element checked",
            "per_site checked and not executed",
            "per_mode checked and not executed",
            "per_block checked",
            "lattice_wide checked and not executed",
        ],
    },
    "gates": {"pass": passed, "fail": failed, "named": gates},
}
RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(0 if failed == 0 else 1)
