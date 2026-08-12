"""Independent completeness check for Cycle 744's finite incidence theorem.

This checker imports neither the Cycle 744 primary nor its refinement code. It
reconstructs the exact-cover table with the opposite uncovered-sample pivot,
consumes the exact Cycle 742 automorphism certificates, rebuilds the generated
group with tuple arithmetic, and implements partition refinement as explicit
cell splitting by overlap multisets.  The result concerns only the supplied
15800-by-192 role-preserving incidence structure.
"""

import copy
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05.py"
CHECKER_PATH = (
    "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_"
    "independent_check_2026_08_05.py"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05_"
    "receipt_2026-08-05.json"
)
C742_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md"
C742_PRIMARY_PATH = "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py"
C742_CHECKER_PATH = (
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_"
    "independent_check_2026_08_05.py"
)
C742_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_"
    "receipt_2026-08-05.json"
)
C742_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_"
    "2026_08_05_receipt_2026-08-05.json"
)
C743_NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md"
C743_PRIMARY_PATH = "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py"
C743_CHECKER_PATH = (
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05.py"
)
C743_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_"
    "receipt_2026-08-05.json"
)
C743_INDEPENDENT_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_full_symmetry_certified_cycle744_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05.py",
    "outputs/physical_cell_cutting_full_symmetry_certified_cycle744_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05.py",
    "scripts/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_sixteen_attained_cycle742_independent_check_2026_08_05_receipt_2026-08-05.json",
    "docs/PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05.py",
    "scripts/physical_cell_cutting_hidden_three_bit_geometry_cycle743_independent_check_2026_08_05.py",
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_2026_08_05_receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_hidden_three_bit_geometry_cycle743_independent_check_2026_08_05_receipt_2026-08-05.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "requirements.txt",
    "requirements-release.txt",
)


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def inputs_current(receipt):
    recorded = receipt.get("input_sha256", {})
    return bool(recorded) and all(
        (ROOT / path).is_file() and recorded[path] == sha256(path) for path in recorded
    )


def permutation_hash(permutation):
    payload = json.dumps([int(value) for value in permutation], separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


passed = 0
failed = 0
gates = []


def gate(condition, name, detail):
    global passed, failed
    ok = bool(condition)
    passed += int(ok)
    failed += int(not ok)
    gates.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + "  " + detail, flush=True)


RECEIPT_PATH.write_text(json.dumps({
    "schema": "physical-cell-cutting-full-symmetry-certified-cycle744-independent-v1",
    "status": "fail",
    "claim_type": "bounded_theorem",
    "reason": "checker has not completed",
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def determinant(matrix):
    """Leibniz determinant, separate from the primary minor implementation."""
    rows = [[int(value) for value in row] for row in matrix]
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1 if column & 1 else 1) * value
        * determinant([row[:column] + row[column + 1:] for row in rows[1:]])
        for column, value in enumerate(rows[0])
    )


# Rebuild exact covers with the largest uncovered sample, opposite the primary.
CORNERS = list(itertools.product((0, 1), repeat=4))
VERTICES = np.array(CORNERS, dtype=np.int64)
PIECES = []
INVERSES = []
for subset in itertools.combinations(range(16), 5):
    matrix = (VERTICES[list(subset[1:])] - VERTICES[subset[0]]).T
    if abs(determinant(matrix.tolist())) != 1:
        continue
    inverse = np.rint(np.linalg.inv(matrix.astype(float))).astype(np.int64)
    if np.array_equal(matrix @ inverse, np.eye(4, dtype=np.int64)):
        PIECES.append(subset)
        INVERSES.append(inverse)
INVERSES = np.array(INVERSES, dtype=np.int64)
PAIRS = list(itertools.combinations(range(5), 2))


def piece_cost(piece):
    points = VERTICES[list(piece)]
    return sum(
        sum(abs(int(points[a, column]) - int(points[b, column])) for column in range(4)) > 1
        for a, b in PAIRS
    )


COSTS = np.array([piece_cost(piece) for piece in PIECES], dtype=np.int64)
MINIMUM = np.flatnonzero(COSTS == int(COSTS.min())).tolist()
corner_index = {corner: index for index, corner in enumerate(CORNERS)}
corner_actions = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for row, column in enumerate(permutation):
            rotation[row, column] = signs[row]
        if round(np.linalg.det(rotation.astype(float))) != 1:
            continue
        for tick_flip in (False, True):
            action = []
            for x, y, z, tick in CORNERS:
                image = rotation @ (2 * np.array((x, y, z), dtype=np.int64) - 1) + 1
                target = (int(image[0]) // 2, int(image[1]) // 2,
                          int(image[2]) // 2, 1 - tick if tick_flip else tick)
                action.append(corner_index[target])
            corner_actions.append(action)
piece_index = {piece: index for index, piece in enumerate(PIECES)}
labels = np.full(len(PIECES), -1, dtype=np.int64)
representatives = []
for index, piece in enumerate(PIECES):
    if labels[index] >= 0:
        continue
    orbit = len(representatives)
    representatives.append(index)
    for action in corner_actions:
        image = tuple(sorted(action[corner] for corner in piece))
        labels[piece_index[image]] = orbit
weights0 = np.array((0, 1, 7, 49, 343), dtype=np.int64)
weights = 2 * (3 * int(weights0.sum()) + 1 + weights0)
scale = int(weights.sum())
sample_set = set()
for index in representatives:
    piece = PIECES[index]
    for action in corner_actions:
        sample_set.add(tuple(int(value) for value in (
            weights[:, None] * VERTICES[[action[corner] for corner in piece]]
        ).sum(axis=0)))
samples = np.array(sorted(sample_set), dtype=np.int64)
sample_incidence = np.zeros((len(PIECES), len(samples)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    bary = INVERSES[index] @ (samples.T - (scale * VERTICES[piece[0]])[:, None])
    total = bary.sum(axis=0)
    sample_incidence[index] = (bary > 0).all(axis=0) & (total < scale)
active = np.flatnonzero(sample_incidence[MINIMUM].any(axis=0))
sample_incidence = sample_incidence[:, active]
by_sample = {}
mask_by_piece = {}
for piece in MINIMUM:
    mask = 0
    for sample in np.flatnonzero(sample_incidence[piece]):
        mask |= 1 << int(sample)
        by_sample.setdefault(int(sample), []).append(piece)
    mask_by_piece[piece] = mask
all_samples = (1 << len(active)) - 1
solutions = []


def covers(covered, chosen):
    if covered == all_samples:
        solutions.append(tuple(sorted(chosen)))
        return
    remaining = all_samples & ~covered
    sample = remaining.bit_length() - 1
    for piece in by_sample[sample]:
        mask = mask_by_piece[piece]
        if mask & covered:
            continue
        chosen.append(piece)
        covers(covered | mask, chosen)
        chosen.pop()


covers(0, [])
used = sorted({piece for solution in solutions for piece in solution})
position = {piece: index for index, piece in enumerate(used)}
incidence = np.zeros((len(solutions), len(used)), dtype=np.uint8)
for row, solution in enumerate(solutions):
    incidence[row, [position[piece] for piece in solution]] = 1
packed_rows = [bytes(row) for row in np.packbits(incidence, axis=1)]
canonical_incidence_hash = hashlib.sha256(b"".join(sorted(packed_rows))).hexdigest()
column_order = [[int(corner) for corner in PIECES[piece]] for piece in used]
column_order_hash = hashlib.sha256(
    json.dumps(column_order, separators=(",", ":")).encode("utf-8")
).hexdigest()
gate(len(PIECES) == 2672 and len(MINIMUM) == 400 and int(COSTS.min()) == 6
     and incidence.shape == (15800, 192)
     and bool((incidence.sum(axis=1) == 24).all()),
     "independent.population", "opposite-pivot reconstruction gives 15800 by 192")

C742 = load(C742_RECEIPT_PATH)
C742I = load(C742_INDEPENDENT_RECEIPT_PATH)
C743 = load(C743_RECEIPT_PATH)
C743I = load(C743_INDEPENDENT_RECEIPT_PATH)
PRIMARY = load(PRIMARY_RECEIPT_PATH)
certificates = C742.get("automorphism_certificates", {})
dependency_ok = (
    C742.get("schema") == "physical-cell-cutting-sixteen-attained-cycle742-v2"
    and C742.get("status") == "pass" and C742.get("gates", {}).get("fail") == 0
    and C742.get("runner_sha256") == sha256(C742_PRIMARY_PATH) and inputs_current(C742)
    and C742I.get("schema") == "physical-cell-cutting-sixteen-attained-cycle742-independent-v1"
    and C742I.get("status") == "pass" and C742I.get("gates", {}).get("fail") == 0
    and (C742I.get("checker_sha256") or C742I.get("runner_sha256"))
    == sha256(C742_CHECKER_PATH) and inputs_current(C742I)
    and C742.get("incidence_identity", {}).get("canonical_incidence_rows_sha256")
    == canonical_incidence_hash
    and C742.get("incidence_identity", {}).get("support_column_order_sha256")
    == column_order_hash
    and C743.get("schema") == "physical-cell-cutting-hidden-three-bit-geometry-cycle743-v2"
    and C743.get("status") == "pass" and C743.get("gates", {}).get("fail") == 0
    and C743.get("runner_sha256") == sha256(C743_PRIMARY_PATH) and inputs_current(C743)
    and C743I.get("schema")
    == "physical-cell-cutting-hidden-three-bit-geometry-cycle743-independent-v1"
    and C743I.get("status") == "pass" and C743I.get("gates", {}).get("fail") == 0
    and C743I.get("checker_sha256") == sha256(C743_CHECKER_PATH) and inputs_current(C743I)
    and C743.get("generated_group", {}).get("order") == 384
    and C743I.get("independent_reconstruction", {}).get("generated_group_order") == 384
)
gate(dependency_ok, "independent.dependencies",
     "Cycle 742 exact maps and Cycle 743 exact group package are current")


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(right)))


def closure(generators, degree=192):
    identity = tuple(range(degree))
    seen, frontier = {identity}, [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            product = compose(generator, current)
            if product not in seen:
                seen.add(product)
                frontier.append(product)
    return seen


row_lookup = {packed: row for row, packed in enumerate(packed_rows)}


def induced_row_permutation(permutation, table=incidence):
    if sorted(permutation) != list(range(192)):
        return None
    local_rows = {bytes(row): index for index, row in enumerate(np.packbits(table, axis=1))}
    result = []
    for row in table:
        image = np.zeros(192, dtype=np.uint8)
        image[np.asarray(permutation)[np.flatnonzero(row)]] = 1
        target = local_rows.get(bytes(np.packbits(image)))
        if target is None:
            return None
        result.append(target)
    return tuple(result) if len(set(result)) == len(table) else None


extra = []
certificates_ok = True
for name in ("b0", "b1"):
    certificate = certificates.get(name, {})
    permutation = tuple(int(value) for value in certificate.get("support_permutation", []))
    certificates_ok = (
        certificates_ok and induced_row_permutation(permutation) is not None
        and certificate.get("support_permutation_sha256") == permutation_hash(permutation)
        and compose(permutation, permutation) == tuple(range(192))
    )
    extra.append(permutation)
gate(certificates_ok, "independent.extra_automorphisms",
     "both predecessor permutations preserve every independently reconstructed row")

piece_permutations_48 = []
for action in corner_actions:
    permutation = []
    for piece in used:
        image = tuple(sorted(action[corner] for corner in PIECES[piece]))
        permutation.append(position[piece_index[image]])
    piece_permutations_48.append(tuple(permutation))
all_generator_automorphisms = all(
    induced_row_permutation(permutation) is not None
    for permutation in piece_permutations_48 + extra
)
E48 = closure(piece_permutations_48)
E96 = closure(piece_permutations_48 + [extra[0]])
E = closure(piece_permutations_48 + extra)
identity = tuple(range(192))
point_stabilizer = [permutation for permutation in E if permutation[0] == 0]
s0s = [permutation for permutation in point_stabilizer if permutation != identity]
group_ok = (
    all_generator_automorphisms and len(E48) == 48 and len(E96) == 96 and len(E) == 384
    and len({permutation[0] for permutation in E}) == 192
    and len(point_stabilizer) == 2 and len(s0s) == 1
    and sum(s0s[0][index] == index for index in range(192)) == 16
)
gate(group_ok, "independent.generated_group",
     "tuple closure is transitive of order 384 with point stabilizer two")
s0 = s0s[0]

# Independent explicit-cell refinement of the edge-coloured overlap graph.
gram = incidence.T.astype(np.int64) @ incidence.astype(np.int64)
gram_hash = hashlib.sha256(gram.astype("<i8", copy=False).tobytes()).hexdigest()


def refine_cells(individualized):
    fixed = [[int(value)] for value in individualized]
    remainder = sorted(set(range(192)) - set(individualized))
    cells = fixed + ([remainder] if remainder else [])
    rounds = 0
    while True:
        rounds += 1
        new_cells = []
        for cell in cells:
            buckets = {}
            for vertex in cell:
                signature = tuple(
                    tuple(sorted(int(gram[vertex, target]) for target in target_cell))
                    for target_cell in cells
                )
                buckets.setdefault(signature, []).append(vertex)
            for signature in sorted(buckets):
                new_cells.append(sorted(buckets[signature]))
        if len(new_cells) == len(cells):
            return new_cells, rounds
        cells = new_cells


base_cells, base_rounds = refine_cells([])
point_cells, point_rounds = refine_cells([0])
sizes = sorted(len(cell) for cell in point_cells)
cell_partition_ok = (
    len(base_cells) == 1 and base_rounds == 1
    and len(point_cells) == 104 and sizes.count(1) == 16 and sizes.count(2) == 88
    and all((len(cell) == 1 and s0[cell[0]] == cell[0]) or
            (len(cell) == 2 and {s0[cell[0]], s0[cell[1]]} == set(cell))
            for cell in point_cells)
)
gate(cell_partition_ok, "independent.point_partition",
     "explicit cell splitting gives 16 singleton and 88 two-element suborbits")

# Pick the lexicographically last pair, unlike the primary's first color cell.
pair = max(tuple(cell) for cell in point_cells if len(cell) == 2)
branch_a, rounds_a = refine_cells([0, pair[0]])
branch_b, rounds_b = refine_cells([0, pair[1]])
discrete = len(branch_a) == len(branch_b) == 192 and all(
    len(cell) == 1 for cell in branch_a + branch_b
)
candidate = [0] * 192
if discrete:
    for left_cell, right_cell in zip(branch_a, branch_b):
        candidate[left_cell[0]] = right_cell[0]
candidate = tuple(candidate)
branch_ok = (
    discrete and candidate == s0
    and induced_row_permutation(identity) is not None
    and induced_row_permutation(candidate) is not None
)
gate(branch_ok, "independent.exhaustive_stabilizer_branch",
     "the two discrete branches yield exactly identity and the known stabilizer map")

full_order = 192 * 2
gate(full_order == len(E) == 384, "independent.full_group",
     "orbit-stabilizer upper bound equals the contained generated group")


def primary_contract(receipt):
    certificate = receipt.get("full_automorphism_certificate", {})
    supplied = receipt.get("supplied_incidence", {})
    return (
        receipt.get("schema")
        == "physical-cell-cutting-full-symmetry-certified-cycle744-v2"
        and receipt.get("status") == "pass" and receipt.get("gates", {}).get("fail") == 0
        and receipt.get("runner_sha256") == sha256(PRIMARY_PATH)
        and set(receipt.get("input_sha256", {})) == set(AUDIT_INPUT_PATHS[3:]) | {
            NOTE_PATH, CHECKER_PATH
        }
        and inputs_current(receipt)
        and supplied.get("canonical_incidence_rows_sha256") == canonical_incidence_hash
        and supplied.get("support_column_order_sha256") == column_order_hash
        and supplied.get("overlap_gram_sha256") == gram_hash
        and certificate.get("candidate_stabilizer_size") == 2
        and certificate.get("full_automorphism_group_order") == 384
        and certificate.get("equals_generated_group") is True
        and receipt.get("no_go_discipline", {}).get("status") == "PASS"
    )


gate(primary_contract(PRIMARY), "independent.primary_contract",
     "primary receipt pins current sources and the independently rebuilt certificate")

bad_primary = copy.deepcopy(PRIMARY)
bad_primary["status"] = "fail"
gate(not primary_contract(bad_primary), "hostile.primary_status",
     "a failing primary receipt is rejected")
bad_primary = copy.deepcopy(PRIMARY)
bad_primary["full_automorphism_certificate"]["candidate_stabilizer_size"] = 3
gate(not primary_contract(bad_primary), "hostile.stabilizer_size",
     "an enlarged stabilizer cannot satisfy the certificate contract")
bad_extra = list(extra[0])
bad_extra[0], bad_extra[1] = bad_extra[1], bad_extra[0]
gate(induced_row_permutation(tuple(bad_extra)) is None, "hostile.automorphism",
     "a transposed image pair breaks exact incidence preservation")
gate(len(E96) == 96 and len(E96) != len(E), "hostile.omitted_generator",
     "omitting b1 collapses the generated group")
bad_incidence = incidence.copy()
bad_incidence[0, 0] ^= 1
bad_hash = hashlib.sha256(b"".join(sorted(
    bytes(row) for row in np.packbits(bad_incidence, axis=1)
))).hexdigest()
gate(bad_hash != canonical_incidence_hash, "hostile.incidence_identity",
     "one changed incidence bit invalidates the canonical table identity")

print("per_element: checked -- all 192 columns enter opposite-pivot incidence, "
      "group closure, and explicit-cell refinement", flush=True)
print("per_site: checked and not executed -- one supplied coordinate four-cube only", flush=True)
print("per_mode: checked and not executed -- no field or momentum modes are present", flush=True)
print("per_block: checked -- all 15800 rows and all 50 generators are tested", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell or continuum claim", flush=True)

receipt = {
    "schema": "physical-cell-cutting-full-symmetry-certified-cycle744-independent-v1",
    "status": "pass" if failed == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "checker_sha256": sha256(CHECKER_PATH),
    "input_sha256": {path: sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_reconstruction": {
        "cuttings": len(solutions),
        "support_columns": len(used),
        "canonical_incidence_rows_sha256": canonical_incidence_hash,
        "support_column_order_sha256": column_order_hash,
        "overlap_gram_sha256": gram_hash,
        "generated_group_order": len(E),
        "point_stabilizer_size": len(point_stabilizer),
        "point_partition_cells": len(point_cells),
        "selected_pair": list(pair),
        "branch_rounds": [rounds_a, rounds_b],
        "full_automorphism_group_order": full_order,
    },
    "gates": {
        "pass": passed,
        "fail": failed,
        "named": {name: "PASS" if ok else "FAIL" for name, ok in gates},
    },
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(passed, failed), flush=True)
sys.exit(0 if failed == 0 else 1)
