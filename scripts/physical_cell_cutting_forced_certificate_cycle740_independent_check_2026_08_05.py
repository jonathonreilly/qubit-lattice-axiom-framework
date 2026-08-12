"""Independent reconstruction of Cycle 740's finite forced-subset theorem.

This checker imports and executes no primary implementation. It uses a Leibniz
determinant, the opposite exact-cover pivot, a least-significant-bit GF(2)
elimination, and a nullspace constructed from row reduced form. It reconstructs
the supplied 15,800 by 192 incidence system and exhausts every union of the
declared four quarters and eight lexicographic blocks. Failed gates write a
failing receipt and exit nonzero.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/PHYSICAL_CELL_CUTTING_FORCED_CERTIFICATE_CYCLE740_NOTE_2026-08-05.md"
PRIMARY_PATH = "scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py"
PRIMARY_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_forced_certificate_cycle740_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_RECEIPT_PATH = (
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json"
)
C737_PRIMARY_PATH = (
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py"
)
RECEIPT_PATH = ROOT / (
    "outputs/physical_cell_cutting_forced_certificate_cycle740_"
    "independent_check_2026_08_05_receipt_2026-08-05.json"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_CELL_CUTTING_FORCED_CERTIFICATE_CYCLE740_NOTE_2026-08-05.md",
    "scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py",
    "outputs/physical_cell_cutting_forced_certificate_cycle740_2026_08_05_"
    "receipt_2026-08-05.json",
    "outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_"
    "receipt_2026-08-05.json",
    "scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def file_sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


PRIMARY_RECEIPT = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
C737_RECEIPT = json.loads((ROOT / C737_RECEIPT_PATH).read_text(encoding="utf-8"))
PF = [0, 0]
GATES = []


def gate(ok, name, detail):
    passed = bool(ok)
    PF[0 if passed else 1] += 1
    GATES.append((name, passed))
    print(("PASS " if passed else "FAIL ") + name + "  " + detail, flush=True)


def det4_leibniz(matrices):
    result = np.zeros(len(matrices), dtype=np.int64)
    rows = np.arange(4)
    for permutation in itertools.permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        result += (-1 if inversions & 1 else 1) * np.prod(
            matrices[:, rows, permutation], axis=1, dtype=np.int64
        )
    return result


def cost(pieces, vertices):
    total = np.zeros(len(pieces), dtype=np.int64)
    for left, right in itertools.combinations(range(5), 2):
        distance = np.abs(
            vertices[pieces[:, left]] - vertices[pieces[:, right]]
        ).sum(axis=1)
        total += (distance > 1).astype(np.int64)
    return total


def low_basis(rows):
    pivots = {}
    for value in rows:
        row = int(value)
        while row:
            pivot = (row & -row).bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return pivots


def low_rref(rows):
    pivots = low_basis(rows)
    for pivot in sorted(pivots, reverse=True):
        for other in sorted(pivots):
            if other != pivot and ((pivots[other] >> pivot) & 1):
                pivots[other] ^= pivots[pivot]
    return pivots


def in_span(value, pivots):
    row = int(value)
    while row:
        pivot = (row & -row).bit_length() - 1
        if pivot not in pivots:
            return False
        row ^= pivots[pivot]
    return True


def span_values(values):
    pivots = low_basis(values)
    result = {0}
    for pivot in sorted(pivots):
        result |= {value ^ pivots[pivot] for value in tuple(result)}
    return sorted(result)


def parity(value):
    return int(value).bit_count() & 1


CORNERS = [
    (x, y, z, t)
    for x in (0, 1)
    for y in (0, 1)
    for z in (0, 1)
    for t in (0, 1)
]
VERTICES = np.array(CORNERS, dtype=np.int64)
SUBSETS = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
VOLUMES = np.abs(
    det4_leibniz(
        VERTICES[SUBSETS[:, 1:]] - VERTICES[SUBSETS[:, 0]][:, None, :]
    )
)
PIECES = SUBSETS[VOLUMES == 1]
PIECE_COUNT = len(PIECES)
COSTS = cost(PIECES, VERTICES)
FLOOR = int(COSTS.min())
MINIMUM_PIECES = [i for i in range(PIECE_COUNT) if int(COSTS[i]) == FLOOR]
MATRICES = np.stack(
    [(VERTICES[piece[1:]] - VERTICES[piece[0]]).T for piece in PIECES]
)
INVERSES = np.rint(np.linalg.inv(MATRICES.astype(float))).astype(np.int64)
gate(
    np.array_equal(
        MATRICES @ INVERSES,
        np.broadcast_to(np.eye(4, dtype=np.int64), MATRICES.shape),
    ),
    "independent.inverse",
    "every float-proposed simplex inverse is accepted only after exact integer "
    "multiplication",
)

CORNER_POSITION = {corner: index for index, corner in enumerate(CORNERS)}
ROTATIONS = []
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        rotation = np.zeros((3, 3), dtype=np.int64)
        for row, column in enumerate(permutation):
            rotation[row, column] = signs[row]
        if int(round(np.linalg.det(rotation.astype(float)))) == 1:
            ROTATIONS.append(rotation)
GROUP = []
center = np.array([1, 1, 1], dtype=np.int64)
for rotation in ROTATIONS:
    for tick_flip in (0, 1):
        image = []
        for x, y, z, tick in CORNERS:
            spatial = (
                rotation
                @ (2 * np.array([x, y, z], dtype=np.int64) - center)
                + center
            )
            key = (
                int(spatial[0]) // 2,
                int(spatial[1]) // 2,
                int(spatial[2]) // 2,
                1 - tick if tick_flip else tick,
            )
            image.append(CORNER_POSITION[key])
        GROUP.append((rotation, tick_flip, np.array(image, dtype=np.int64)))
piece_position = {
    tuple(int(corner) for corner in piece): index
    for index, piece in enumerate(PIECES)
}
orbit_labels = -np.ones(PIECE_COUNT, dtype=np.int64)
REPRESENTATIVES = []
for piece_index in range(PIECE_COUNT):
    if orbit_labels[piece_index] >= 0:
        continue
    orbit = len(REPRESENTATIVES)
    REPRESENTATIVES.append(piece_index)
    for _rotation, _tick_flip, image in GROUP:
        transformed = tuple(sorted(int(image[corner]) for corner in PIECES[piece_index]))
        orbit_labels[piece_position[transformed]] = orbit

OFFSETS = np.array([0, 1, 7, 49, 343], dtype=np.int64)
barycentric_bound = max(
    int(np.abs(np.einsum(
        "nij,nmj->nmi",
        INVERSES,
        VERTICES[None, :, :] - VERTICES[PIECES[:, 0]][:, None, :],
    )).max()),
    3,
)
WEIGHTS = 2 * (barycentric_bound * int(OFFSETS.sum()) + 1 + OFFSETS)
SCALE = int(WEIGHTS.sum())
spatial_center = np.array([SCALE // 2, SCALE // 2, SCALE // 2], dtype=np.int64)
labels = {}
collisions = 0
for orbit, piece_index in enumerate(REPRESENTATIVES):
    weighted = (WEIGHTS[:, None] * VERTICES[PIECES[piece_index]]).sum(axis=0)
    for rotation, tick_flip, _image in GROUP:
        spatial = rotation @ (weighted[:3] - spatial_center) + spatial_center
        key = (
            int(spatial[0]),
            int(spatial[1]),
            int(spatial[2]),
            SCALE - int(weighted[3]) if tick_flip else int(weighted[3]),
        )
        if labels.setdefault(key, orbit) != orbit:
            collisions += 1
points = sorted(labels)
POINTS = np.array(points, dtype=np.int64)
POINTS_T = POINTS.T
MASKS = []
MEMBERSHIP = np.zeros((PIECE_COUNT, len(POINTS)), dtype=np.uint8)
for index, piece in enumerate(PIECES):
    lam = INVERSES[index] @ (
        POINTS_T - (SCALE * VERTICES[piece[0]])[:, None]
    )
    total = lam.sum(axis=0)
    inside = (lam > 0).all(axis=0) & (total < SCALE)
    MEMBERSHIP[index] = inside.astype(np.uint8)
    mask = 0
    for point_index in np.flatnonzero(inside):
        mask |= 1 << int(point_index)
    MASKS.append(mask)
ALL_POINTS = (1 << len(POINTS)) - 1
gate(
    len(SUBSETS) == 4368
    and PIECE_COUNT == 2672
    and len(POINTS) == 2736
    and collisions == 0
    and len(GROUP) == 48,
    "base.cell",
    "the independent construction finds 2,672 normalized-volume-one pieces, "
    "2,736 labelled interior samples, and the declared 48 cell symmetries",
)
BY_POINT = {}
for piece_index in MINIMUM_PIECES:
    for point_index in np.flatnonzero(MEMBERSHIP[piece_index]):
        BY_POINT.setdefault(int(point_index), []).append(piece_index)

COVERS = []
NODES = [0]
SIZES = set()


def exact_covers(covered, chosen):
    NODES[0] += 1
    if covered == ALL_POINTS:
        SIZES.add(len(chosen))
        COVERS.append(tuple(sorted(chosen)))
        return
    remaining = ALL_POINTS & ~covered
    point_index = remaining.bit_length() - 1
    for piece_index in BY_POINT[point_index]:
        if MASKS[piece_index] & covered:
            continue
        chosen.append(piece_index)
        exact_covers(covered | MASKS[piece_index], chosen)
        chosen.pop()


exact_covers(0, [])
USED = sorted({piece for cover in COVERS for piece in cover})
POSITION = {piece: index for index, piece in enumerate(USED)}
candidate_normals = [
    np.array(value, dtype=np.int64)
    for value in itertools.product((-1, 0, 1), repeat=4)
    if any(value)
]


def separated(left_index, right_index):
    left_points = VERTICES[PIECES[left_index]]
    right_points = VERTICES[PIECES[right_index]]
    left_inverse = INVERSES[left_index]
    right_inverse = INVERSES[right_index]
    normals = (
        candidate_normals
        + [left_inverse[index] for index in range(4)]
        + [-left_inverse.sum(axis=0)]
        + [right_inverse[index] for index in range(4)]
        + [-right_inverse.sum(axis=0)]
    )
    for normal in normals:
        left = left_points @ normal
        right = right_points @ normal
        if int(left.max()) <= int(right.min()) or int(right.max()) <= int(left.min()):
            return True
    return False


cooccurring = {
    pair for cover in COVERS for pair in itertools.combinations(cover, 2)
}
exactly_separated = sum(separated(left, right) for left, right in cooccurring)
INCIDENCE = np.zeros((len(COVERS), len(USED)), dtype=np.uint8)
ROWS = []
for row_index, cover in enumerate(COVERS):
    row = 0
    for piece in cover:
        column = POSITION[piece]
        INCIDENCE[row_index, column] = 1
        row |= 1 << column
    ROWS.append(row)

gate(
    FLOOR == 6
    and len(MINIMUM_PIECES) == 400
    and NODES[0] == 496849
    and len(COVERS) == 15800
    and len(USED) == 192
    and SIZES == {24},
    "base.population",
    "the independent opposite-pivot exact-cover search reconstructs 15,800 "
    "24-piece rows over the same 192 used pieces",
)
gate(
    len(cooccurring) == 15168 and exactly_separated == len(cooccurring),
    "base.geometry",
    "all 15,168 co-occurring pairs have an exact integer separating plane, "
    "certifying every independently returned cover as a geometric dissection",
)

row_pivots = low_rref(ROWS)
pivot_columns = set(row_pivots)
free_columns = [column for column in range(192) if column not in pivot_columns]
KERNEL = []
for free in free_columns:
    word = 1 << free
    for pivot, row in row_pivots.items():
        if (row >> free) & 1:
            word |= 1 << pivot
    KERNEL.append(word)

kernel_zero = all(parity(row & word) == 0 for row in ROWS for word in KERNEL)
gate(
    len(row_pivots) == 88
    and len(KERNEL) == 104
    and kernel_zero
    and len(low_basis(KERNEL)) == 104,
    "algebra.kernel",
    "least-pivot row reduction gives rank 88 and an independently constructed "
    "104-dimensional exact kernel",
)

BLOCK_MASKS = [
    sum(1 << column for column in range(24 * block, 24 * block + 24))
    for block in range(8)
]
QUARTER_MASKS = [
    sum(1 << column for column in range(48 * quarter, 48 * quarter + 48))
    for quarter in range(4)
]


def block_parity(word):
    result = 0
    for block, mask in enumerate(BLOCK_MASKS):
        result |= parity(word & mask) << (7 - block)
    return result


def quarter_parity(word):
    result = 0
    for quarter, mask in enumerate(QUARTER_MASKS):
        result |= parity(word & mask) << (3 - quarter)
    return result


def union_mask(code, masks):
    count = len(masks)
    return sum(
        masks[index]
        for index in range(count)
        if (code >> (count - 1 - index)) & 1
    )


quarter_image = span_values(quarter_parity(word) for word in KERNEL)
block_image = span_values(block_parity(word) for word in KERNEL)
forced_quarters = [
    code
    for code in range(16)
    if in_span(union_mask(code, QUARTER_MASKS), row_pivots)
]
forced_blocks = [
    code
    for code in range(256)
    if in_span(union_mask(code, BLOCK_MASKS), row_pivots)
]
quarter_annihilator = [
    code
    for code in range(16)
    if all(parity(code & image) == 0 for image in quarter_image)
]
block_annihilator = [
    code
    for code in range(256)
    if all(parity(code & image) == 0 for image in block_image)
]

gate(
    quarter_image == [0, 12]
    and forced_quarters == quarter_annihilator
    and forced_quarters == [0, 1, 2, 3, 12, 13, 14, 15],
    "census.quarters",
    "the independently reconstructed quarter image is {0000,1100}, and exactly "
    "the same eight of all 16 quarter unions are forced",
)
expected_block_image = {
    int(word, 2)
    for word in PRIMARY_RECEIPT.get("block_partition", {}).get("image_words", [])
}
gate(
    len(block_image) == 32
    and len(low_basis(block_image)) == 5
    and forced_blocks == block_annihilator
    and len(forced_blocks) == 8
    and set(block_image) == expected_block_image,
    "census.blocks",
    "the independent block image has dimension five and 32 words, and exactly "
    "the same eight of all 256 declared block unions are forced",
)

expected_forced_masks = [
    int(word, 2)
    for word in PRIMARY_RECEIPT.get("block_partition", {}).get(
        "forced_union_masks", []
    )
]
gate(
    forced_blocks == expected_forced_masks
    and all(
        ((code >> (2 * pair)) & 1) == ((code >> (2 * pair + 1)) & 1)
        for code in forced_blocks
        for pair in range(4)
    ),
    "census.profile",
    "all eight exact forced-union masks match the primary and each is a union "
    "of the declared 48-piece quarters",
)

column_counts = INCIDENCE.astype(np.int64).sum(axis=0)
whole = (1 << 192) - 1
named = {
    "whole": whole,
    "L": QUARTER_MASKS[0] | QUARTER_MASKS[1],
    "R": QUARTER_MASKS[2] | QUARTER_MASKS[3],
    "Q2": QUARTER_MASKS[2],
    "Q3": QUARTER_MASKS[3],
}
gate(
    int(column_counts.min()) == int(column_counts.max()) == 1975
    and all(in_span(mask, row_pivots) for mask in named.values()),
    "certificate.named",
    "all 192 columns have odd count 1,975 and the independently reduced row "
    "space contains the same five named indicators",
)

free_named = {
    **{"E{0}".format(i): BLOCK_MASKS[i] for i in range(8)},
    "Q0": QUARTER_MASKS[0],
    "Q1": QUARTER_MASKS[1],
}
witnesses = {}
for name, mask in free_named.items():
    witness = next(word for word in KERNEL if parity(word & mask))
    witnesses[name] = witness
gate(
    all(not in_span(mask, row_pivots) for mask in free_named.values())
    and all(
        all(parity(row & witness) == 0 for row in ROWS)
        and parity(witness & free_named[name]) == 1
        for name, witness in witnesses.items()
    ),
    "certificate.free",
    "each of the ten named free indicators has an exact kernel witness odd on "
    "that indicator and zero on all 15,800 rows",
)

support_tuples = [tuple(sorted(int(corner) for corner in PIECES[piece])) for piece in USED]
packed_rows = [bytes(row) for row in np.packbits(INCIDENCE, axis=1)]
canonical_incidence_hash = hashlib.sha256(
    b"".join(sorted(packed_rows))
).hexdigest()
column_order_hash = hashlib.sha256(
    json.dumps(support_tuples, separators=(",", ":")).encode("utf-8")
).hexdigest()
c737_identity = C737_RECEIPT.get("reading_identity", {})
gate(
    C737_RECEIPT.get("schema")
    == "physical-cell-cutting-least-computing-sets-cycle737-v2"
    and C737_RECEIPT.get("status") == "pass"
    and C737_RECEIPT.get("gates", {}).get("fail") == 0
    and C737_RECEIPT.get("runner_sha256") == file_sha256(C737_PRIMARY_PATH)
    and c737_identity.get("canonical_incidence_rows_sha256")
    == canonical_incidence_hash
    and c737_identity.get("support_column_order_sha256") == column_order_hash,
    "dep.cycle737",
    "Cycle 737 binds exactly the independently reconstructed canonical population "
    "and support order",
)
primary_population = PRIMARY_RECEIPT.get("population", {})
primary_dep = PRIMARY_RECEIPT.get("direct_dependency", {})
primary_ok = (
    PRIMARY_RECEIPT.get("schema")
    == "physical-cell-cutting-forced-certificate-cycle740-v2"
    and PRIMARY_RECEIPT.get("status") == "pass"
    and PRIMARY_RECEIPT.get("gates", {}).get("fail") == 0
    and PRIMARY_RECEIPT.get("runner_sha256") == file_sha256(PRIMARY_PATH)
    and primary_population.get("geometric_cuttings") == len(COVERS)
    and primary_population.get("used_pieces") == len(USED)
    and primary_population.get("incidence_rank") == len(row_pivots)
    and primary_dep.get("canonical_incidence_rows_sha256")
    == canonical_incidence_hash
    and primary_dep.get("support_column_order_sha256") == column_order_hash
)
gate(
    primary_ok,
    "dep.primary_receipt",
    "the primary pass receipt binds the current primary bytes and exactly the "
    "independently reconstructed row-order-invariant population identity",
)

shifted_masks = [
    sum(1 << ((24 * block + offset + 1) % 192) for offset in range(24))
    for block in range(8)
]
shifted_forced = [
    code
    for code in range(256)
    if in_span(union_mask(code, shifted_masks), row_pivots)
]
gate(
    shifted_forced != forced_blocks,
    "hostile.order",
    "a cyclic shift of the declared support order changes the forced block "
    "profile, so the partition is load-bearing",
)
mutated = INCIDENCE.copy()
mutated[0, 0] ^= np.uint8(1)
gate(
    int(mutated[0].sum()) != 24 and int(mutated[:, 0].sum()) != 1975,
    "hostile.incidence",
    "one flipped incidence bit breaks both exact regularity checks",
)

print("")
print("per_element: checked -- all 192 used pieces enter the independent incidence, "
      "row-space, kernel, block, and witness checks", flush=True)
print("per_site: checked -- one supplied 16-corner coordinate cell only; no physical "
      "assembly-cell or framework site identification is executed", flush=True)
print("per_mode: checked and not executed -- the finite incidence system has no field, "
      "spectral, or momentum-mode decomposition", flush=True)
print("per_block: checked -- all 16 quarter unions and all 256 unions of the eight "
      "declared lexicographic 24-piece blocks", flush=True)
print("lattice_wide: checked and not executed -- no multi-cell, arbitrary-domain, "
      "thermodynamic, boundary, or continuum negative is asserted", flush=True)

receipt = {
    "schema": "physical-cell-cutting-forced-certificate-cycle740-independent-v1",
    "status": "pass" if PF[1] == 0 else "fail",
    "claim_type": "bounded_theorem",
    "audit_status_authority": "independent audit lane only",
    "runner_sha256": file_sha256(
        "scripts/physical_cell_cutting_forced_certificate_cycle740_"
        "independent_check_2026_08_05.py"
    ),
    "input_sha256": {path: file_sha256(path) for path in AUDIT_INPUT_PATHS},
    "independent_route": {
        "determinant": "Leibniz expansion",
        "exact_cover_pivot": "largest uncovered sample",
        "gf2_pivot": "least significant bit",
        "kernel": "constructed from row reduced form",
        "visited_exact_cover_nodes": NODES[0],
    },
    "population": {
        "geometric_cuttings": len(COVERS),
        "used_pieces": len(USED),
        "incidence_rank": len(row_pivots),
        "kernel_dimension": len(KERNEL),
        "canonical_incidence_rows_sha256": canonical_incidence_hash,
        "support_column_order_sha256": column_order_hash,
    },
    "complete_census": {
        "quarter_image_words": [format(value, "04b") for value in quarter_image],
        "forced_quarter_masks": [format(value, "04b") for value in forced_quarters],
        "block_image_words": [format(value, "08b") for value in block_image],
        "forced_block_masks": [format(value, "08b") for value in forced_blocks],
    },
    "gates": {
        "pass": PF[0],
        "fail": PF[1],
        "named": {name: "PASS" if passed else "FAIL" for name, passed in GATES},
    },
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print("RECEIPT " + str(RECEIPT_PATH.relative_to(ROOT)), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]), flush=True)
sys.exit(0 if PF[1] == 0 else 1)
