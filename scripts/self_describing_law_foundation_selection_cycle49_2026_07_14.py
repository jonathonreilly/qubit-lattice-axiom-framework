#!/usr/bin/env python3
"""Cycle 49: self-description versus foundation-level law selection.

This runner constructs two proper-cubic, translation-homogeneous local Boolean
response laws.  The same append-only universal-context apparatus makes each
law write a corpus from which the complete table is reconstructed.  It then
checks that self-reconstruction has two fixed points, and executes a bounded
positive singleton route in the affine-totalistic subclass.
"""

from __future__ import annotations

from dataclasses import dataclass, fields, replace
from itertools import permutations, product
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "SELF_DESCRIBING_LAW_FOUNDATION_SELECTION_CYCLE49_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE42 = REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
CYCLE45 = REVIEW / "COMPLETE_HISTORY_RECONSTRUCTION_CYCLE45_NOTE_2026-07-14.md"
CANONICAL = REVIEW / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"
UNIQUE_EXTENSION = REVIEW / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md"
EQUIVALENCE = REVIEW / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md"
FINAL_CENSUS = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


def markdown_subsection(text: str, number: int) -> str:
    lowered = text.lower()
    start_marker = f"### n{number} —"
    end_marker = f"### n{number + 1} —" if number < 8 else "## bottom line"
    start = lowered.index(start_marker)
    end = lowered.index(end_marker, start)
    return lowered[start:end]


# Direction order: +x, -x, +y, -y, +z, -z.
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
TOTALISTIC_CONTEXTS = tuple((central, count) for central in (0, 1) for count in range(7))


def permutation_sign(p: tuple[int, int, int]) -> int:
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def proper_cubic_rotation_permutations() -> tuple[tuple[int, ...], ...]:
    """Return the 24 determinant-+1 signed-axis rotations on six neighbors."""
    rotations: set[tuple[int, ...]] = set()
    direction_index = {vector: index for index, vector in enumerate(DIRECTIONS)}
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            determinant = permutation_sign(axis_permutation) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
                continue
            images = []
            for vector in DIRECTIONS:
                image = [0, 0, 0]
                for source_axis in range(3):
                    image[axis_permutation[source_axis]] = signs[source_axis] * vector[source_axis]
                images.append(direction_index[tuple(image)])
            rotations.add(tuple(images))
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_rotation_permutations()


def proper_cubic_neighbor_orbits() -> tuple[frozenset[tuple[int, ...]], ...]:
    remaining = set(product((0, 1), repeat=6))
    orbits: list[frozenset[tuple[int, ...]]] = []
    while remaining:
        representative = min(remaining)
        orbit = frozenset(
            tuple(representative[rotation[index]] for index in range(6))
            for rotation in ROTATIONS
        )
        orbits.append(orbit)
        remaining.difference_update(orbit)
    return tuple(orbits)


NEIGHBOR_ORBITS = proper_cubic_neighbor_orbits()


# Four explicit rank-one possibilities inside the shared M_2(C) site domain.
Site = tuple[int, int, int]
Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]
NeighborCondition = Matrix2 | None

PROJECTORS: dict[str, Matrix2] = {
    "P0": ((1.0 + 0.0j, 0.0j), (0.0j, 0.0j)),
    "P1": ((0.0j, 0.0j), (0.0j, 1.0 + 0.0j)),
    "PX": ((0.5 + 0.0j, 0.5 + 0.0j), (0.5 + 0.0j, 0.5 + 0.0j)),
    "PY": ((0.5 + 0.0j, -0.5j), (0.5j, 0.5 + 0.0j)),
}
ARBITRARY_M2: tuple[Matrix2, ...] = (
    ((2.0 + 3.0j, -0.25 + 1.5j), (4.0 - 0.5j, -7.0 + 0.25j)),
    ((-1.0j, 2.5 + 0.0j), (3.0j, 0.125 - 4.0j)),
)


def is_m2(value: object) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(row, tuple) and len(row) == 2 for row in value)
        and all(
            isinstance(entry, (int, float, complex))
            for row in value
            for entry in row
        )
    )


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(2)) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_adjoint(matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def same_matrix(left: Matrix2, right: Matrix2) -> bool:
    return all(abs(left[row][column] - right[row][column]) < 1.0e-12 for row in range(2) for column in range(2))


def common_available(neighbors: tuple[NeighborCondition, ...], candidate: Matrix2) -> bool:
    """Total shared M_2(C) admissibility predicate for every neighbor state."""
    if len(neighbors) != 6 or any(item is not None and not is_m2(item) for item in neighbors):
        raise ValueError("each of six neighbors must be open or carry M_2(C) content")
    if not is_m2(candidate):
        raise ValueError("candidate must be M_2(C) content")
    forbidden = PROJECTORS["PY"] if sum(item is not None for item in neighbors) % 2 == 0 else PROJECTORS["PX"]
    return candidate != forbidden


def scalar_content_readout(content: Matrix2) -> float:
    """The total one-site scalar i(A)=Re Tr(P1 A) on M_2(C)."""
    if not is_m2(content):
        raise ValueError("readout content must lie in M_2(C)")
    product_matrix = matrix_multiply(PROJECTORS["P1"], content)
    return float((product_matrix[0][0] + product_matrix[1][1]).real)


def finite_readout(contents: tuple[Matrix2, ...]) -> float:
    return sum(scalar_content_readout(content) for content in contents)


def add_site(left: Site, right: Site) -> Site:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def nearest_neighbor_sites(site: Site) -> tuple[Site, ...]:
    return tuple(add_site(site, direction) for direction in DIRECTIONS)


def context_index(context: tuple[int, int]) -> int:
    return TOTALISTIC_CONTEXTS.index(context)


def context_center(context: tuple[int, int]) -> Site:
    return (100 * context_index(context), 0, 0)


def storage_target(context: tuple[int, int]) -> Site:
    return (100 * context_index(context), 20, 0)


def storage_block(context: tuple[int, int]) -> frozenset[Site]:
    target = storage_target(context)
    return frozenset((target, *nearest_neighbor_sites(target)))


@dataclass(frozen=True)
class AffineLaw:
    central_coefficient: int
    neighbor_parity_coefficient: int
    constant: int

    def respond(self, central: int, neighbors: tuple[int, ...]) -> int:
        if len(neighbors) != 6 or central not in (0, 1) or any(bit not in (0, 1) for bit in neighbors):
            raise ValueError("one central bit and six neighbor bits are required")
        parity = sum(neighbors) % 2
        return (
            self.central_coefficient * central
            ^ self.neighbor_parity_coefficient * parity
            ^ self.constant
        )

    def count_response(self, central: int, neighbor_ones: int) -> int:
        neighbors = (1,) * neighbor_ones + (0,) * (6 - neighbor_ones)
        return self.respond(central, neighbors)

    def table(self) -> dict[tuple[int, int], int]:
        return {context: self.count_response(*context) for context in TOTALISTIC_CONTEXTS}


LAW_A = AffineLaw(1, 1, 0)
LAW_B = AffineLaw(1, 1, 1)


@dataclass(frozen=True)
class SiteRecord:
    site: Site
    content: Matrix2


@dataclass(frozen=True)
class SpatialCausalRole:
    """Fixed apparatus/causal metadata, not additional onsite record content."""

    event_id: str
    parent_id: str | None
    context_center: Site


@dataclass(frozen=True)
class TableRecord:
    """One onsite M_2(C) content plus separately typed role metadata."""

    site: Site
    content: Matrix2
    role: SpatialCausalRole


@dataclass(frozen=True)
class WriterCorpus:
    apparatus: tuple[SiteRecord, ...]
    outputs: tuple[TableRecord, ...]


def context_block_records(context: tuple[int, int]) -> tuple[SiteRecord, ...]:
    central, neighbor_ones = context
    center = context_center(context)
    neighbors = tuple(
        SiteRecord(
            site=add_site(center, direction),
            content=PROJECTORS["P1" if index < neighbor_ones else "P0"],
        )
        for index, direction in enumerate(DIRECTIONS)
    )
    return (
        SiteRecord(center, PROJECTORS[f"P{central}"]),
        *neighbors,
    )


def context_apparatus_records() -> tuple[SiteRecord, ...]:
    records = tuple(
        record
        for context in TOTALISTIC_CONTEXTS
        for record in context_block_records(context)
    )
    if len({record.site for record in records}) != len(records):
        raise ValueError("far-separated context blocks must be disjoint")
    return records


def site_record_map(records: tuple[SiteRecord, ...]) -> dict[Site, Matrix2]:
    mapping = {record.site: record.content for record in records}
    if len(mapping) != len(records):
        raise ValueError("two apparatus records share a site")
    return mapping


def actual_neighbor_tuple(site: Site, occupancy: dict[Site, Matrix2]) -> tuple[NeighborCondition, ...]:
    return tuple(occupancy.get(neighbor) for neighbor in nearest_neighbor_sites(site))


def decode_context(occupancy: dict[Site, Matrix2], center: Site) -> tuple[int, int]:
    central_content = occupancy.get(center)
    if central_content == PROJECTORS["P0"]:
        central = 0
    elif central_content == PROJECTORS["P1"]:
        central = 1
    else:
        raise ValueError("context center must carry representative P0/P1 content")

    bits: list[int] = []
    for site in nearest_neighbor_sites(center):
        content = occupancy.get(site)
        if content == PROJECTORS["P0"]:
            bits.append(0)
        elif content == PROJECTORS["P1"]:
            bits.append(1)
        else:
            raise ValueError("each context neighbor must carry representative P0/P1 content")
    return central, sum(bits)


def binary_outcome(content: Matrix2) -> int:
    if content == PROJECTORS["P0"]:
        return 0
    if content == PROJECTORS["P1"]:
        return 1
    raise ValueError("a table output must lock P0 or P1")


def universal_writer_corpus(
    law: AffineLaw,
    schedule: tuple[tuple[int, int], ...] = TOTALISTIC_CONTEXTS,
) -> WriterCorpus:
    if len(schedule) != len(TOTALISTIC_CONTEXTS) or set(schedule) != set(TOTALISTIC_CONTEXTS):
        raise ValueError("the schedule must cover each totalistic count row exactly once")
    apparatus = context_apparatus_records()
    occupancy = site_record_map(apparatus)
    context_sites = set(occupancy)
    prior_storage_blocks: set[Site] = set()
    records: list[TableRecord] = []
    parent: str | None = None
    for central, neighbor_ones in schedule:
        context = (central, neighbor_ones)
        center = context_center(context)
        if decode_context(occupancy, center) != context:
            raise ValueError("physical context block does not encode its declared row")
        event_id = f"context-block-{context_index(context):02d}"
        outcome = law.count_response(central, neighbor_ones)
        storage_site = storage_target(context)
        block = storage_block(context)
        if storage_site in occupancy:
            raise ValueError("result target is not open before the write")
        if block & context_sites:
            raise ValueError("storage block overlaps an occupied context/apparatus site")
        if block & prior_storage_blocks:
            raise ValueError("storage block overlaps an earlier storage block")
        neighbor_conditions = actual_neighbor_tuple(storage_site, occupancy)
        content = PROJECTORS[f"P{outcome}"]
        if not common_available(neighbor_conditions, content):
            raise ValueError("output is not admissible under the target's actual neighbors")
        records.append(
            TableRecord(
                site=storage_site,
                content=content,
                role=SpatialCausalRole(
                    event_id=event_id,
                    parent_id=parent,
                    context_center=center,
                ),
            )
        )
        occupancy[storage_site] = content
        prior_storage_blocks.update(block)
        parent = event_id
    return WriterCorpus(apparatus=apparatus, outputs=tuple(records))


def ordered_chain(records: tuple[TableRecord, ...]) -> tuple[TableRecord, ...]:
    if not records:
        raise ValueError("empty corpus")
    by_id = {record.role.event_id: record for record in records}
    if len(by_id) != len(records):
        raise ValueError("duplicate event id")
    if len({record.site for record in records}) != len(records):
        raise ValueError("two records share a site")
    roots = [record for record in records if record.role.parent_id is None]
    if len(roots) != 1:
        raise ValueError("one genesis required")
    child_of: dict[str, TableRecord] = {}
    for record in records:
        if record.role.parent_id is None:
            continue
        if record.role.parent_id not in by_id:
            raise ValueError("missing parent")
        if record.role.parent_id in child_of:
            raise ValueError("forked corpus")
        child_of[record.role.parent_id] = record
    ordered = [roots[0]]
    seen = {roots[0].role.event_id}
    while ordered[-1].role.event_id in child_of:
        child = child_of[ordered[-1].role.event_id]
        if child.role.event_id in seen:
            raise ValueError("cycle")
        ordered.append(child)
        seen.add(child.role.event_id)
    if len(ordered) != len(records):
        raise ValueError("disconnected corpus")
    return tuple(ordered)


def decode_complete_table(corpus: WriterCorpus) -> dict[tuple[int, int], int]:
    ordered_chain(corpus.outputs)
    apparatus = site_record_map(corpus.apparatus)
    occupancy = dict(apparatus)
    for record in corpus.outputs:
        if record.site in occupancy:
            raise ValueError("output target overlaps an earlier physical record")
        occupancy[record.site] = record.content
    table: dict[tuple[int, int], int] = {}
    for record in corpus.outputs:
        context = decode_context(apparatus, record.role.context_center)
        outcome = binary_outcome(record.content)
        if not common_available(actual_neighbor_tuple(record.site, occupancy), record.content):
            raise ValueError("record content is not admissible at its physical target")
        if context in table and table[context] != outcome:
            raise ValueError("conflicting response rows")
        if context in table:
            raise ValueError("duplicate response row")
        table[context] = outcome
    if set(table) != set(TOTALISTIC_CONTEXTS):
        raise ValueError("incomplete response table")
    return table


def representative_neighbor_conditions() -> tuple[tuple[NeighborCondition, ...], ...]:
    return tuple(
        tuple(
            ARBITRARY_M2[index % len(ARBITRARY_M2)] if present else None
            for index, present in enumerate(mask)
        )
        for mask in product((False, True), repeat=6)
    )


def law_symmetry_checks() -> None:
    section("B - Proper cubic contexts and one shared foundation reduct")
    check("B proper cubic group has 24 rotations", len(ROTATIONS) == 24)
    check("B each rotation permutes all six neighbor slots", all(set(rotation) == set(range(6)) for rotation in ROTATIONS))
    check("B six binary neighbors have ten genuine proper-cubic orbits", len(NEIGHBOR_ORBITS) == 10)
    check("B adding the central bit gives twenty genuine proper-cubic contexts", 2 * len(NEIGHBOR_ORBITS) == 20)
    check("B supplied totalism has fourteen count contexts", len(TOTALISTIC_CONTEXTS) == 14)
    check(
        "B totalism is strictly stronger than proper-cubic covariance",
        len(TOTALISTIC_CONTEXTS) < 2 * len(NEIGHBOR_ORBITS),
    )

    exact_projectors: dict[str, Matrix2] = {
        "P0": ((1.0 + 0.0j, 0.0j), (0.0j, 0.0j)),
        "P1": ((0.0j, 0.0j), (0.0j, 1.0 + 0.0j)),
        "PX": ((0.5 + 0.0j, 0.5 + 0.0j), (0.5 + 0.0j, 0.5 + 0.0j)),
        "PY": ((0.5 + 0.0j, -0.5j), (0.5j, 0.5 + 0.0j)),
    }
    check("B four displayed M2 projectors have the exact declared entries", PROJECTORS == exact_projectors)
    check(
        "B shared M2 role possibilities are rank-one Hermitian projectors",
        all(
            same_matrix(matrix_multiply(projector, projector), projector)
            and same_matrix(matrix_adjoint(projector), projector)
            and abs(projector[0][0] + projector[1][1] - 1.0) < 1.0e-12
            for projector in PROJECTORS.values()
        ),
    )

    neighbor_conditions = representative_neighbor_conditions()
    candidate_contents = tuple(PROJECTORS.values()) + ARBITRARY_M2
    check("B representative conditions cover all sixty-four open/present masks", len(neighbor_conditions) == 64)
    check(
        "B common availability is a total exact predicate on arbitrary M2 contents",
        all(
            common_available(condition, candidate)
            == (
                candidate
                != (
                    PROJECTORS["PY"]
                    if sum(item is not None for item in condition) % 2 == 0
                    else PROJECTORS["PX"]
                )
            )
            for condition in neighbor_conditions
            for candidate in candidate_contents
        ),
    )
    even_condition: tuple[NeighborCondition, ...] = (None, None, None, None, None, None)
    odd_condition: tuple[NeighborCondition, ...] = (ARBITRARY_M2[0], None, None, None, None, None)
    check(
        "B common nearest-neighbor availability genuinely varies",
        common_available(even_condition, PROJECTORS["PX"])
        and not common_available(even_condition, PROJECTORS["PY"])
        and not common_available(odd_condition, PROJECTORS["PX"])
        and common_available(odd_condition, PROJECTORS["PY"]),
    )
    check(
        "B common availability always admits both binary record outputs",
        all(
            common_available(condition, PROJECTORS[label])
            for condition in neighbor_conditions
            for label in ("P0", "P1")
        ),
    )
    check(
        "B common availability depends on occupancy rather than M2 record value",
        all(
            common_available(condition, candidate)
            == common_available(
                tuple(PROJECTORS["P0"] if item is not None else None for item in condition),
                candidate,
            )
            for condition in neighbor_conditions
            for candidate in candidate_contents
        ),
    )
    check(
        "B common availability is proper-cubic covariant",
        all(
            common_available(condition, candidate)
            == common_available(tuple(condition[rotation[index]] for index in range(6)), candidate)
            for condition in neighbor_conditions
            for rotation in ROTATIONS
            for candidate in candidate_contents
        ),
    )
    check(
        "B common scalar readout is total on M2 and distinguishes P0 from P1",
        scalar_content_readout(PROJECTORS["P0"]) == 0.0
        and scalar_content_readout(PROJECTORS["P1"]) == 1.0
        and all(scalar_content_readout(matrix) == matrix[1][1].real for matrix in ARBITRARY_M2),
    )
    all_readout_samples = tuple(PROJECTORS.values()) + ARBITRARY_M2
    check(
        "B finite scalar readout is content-only additive with empty value zero",
        finite_readout(()) == 0.0
        and finite_readout(all_readout_samples)
        == finite_readout(all_readout_samples[:3]) + finite_readout(all_readout_samples[3:]),
    )

    apparatus = context_apparatus_records()
    apparatus_map = site_record_map(apparatus)
    context_blocks = tuple(frozenset(record.site for record in context_block_records(context)) for context in TOTALISTIC_CONTEXTS)
    storage_blocks = tuple(storage_block(context) for context in TOTALISTIC_CONTEXTS)
    check("B fourteen physical context blocks contain ninety-eight P0/P1 records", len(apparatus) == 14 * 7)
    check(
        "B every physical cubic block decodes its declared totalistic context",
        all(decode_context(apparatus_map, context_center(context)) == context for context in TOTALISTIC_CONTEXTS),
    )
    check(
        "B physical context blocks are pairwise disjoint and far separated",
        all(
            not (context_blocks[left] & context_blocks[right])
            and sum(
                abs(context_center(TOTALISTIC_CONTEXTS[left])[axis] - context_center(TOTALISTIC_CONTEXTS[right])[axis])
                for axis in range(3)
            )
            >= 100
            for left in range(len(context_blocks))
            for right in range(left + 1, len(context_blocks))
        ),
    )
    check(
        "B every open storage block is disjoint from context records and every other storage block",
        all(not (block & set(apparatus_map)) for block in storage_blocks)
        and all(
            not (storage_blocks[left] & storage_blocks[right])
            for left in range(len(storage_blocks))
            for right in range(left + 1, len(storage_blocks))
        ),
    )
    check(
        "B every physical storage target is absent with an explicit open neighbor tuple",
        all(
            storage_target(context) not in apparatus_map
            and actual_neighbor_tuple(storage_target(context), apparatus_map) == (None,) * 6
            for context in TOTALISTIC_CONTEXTS
        ),
    )
    check(
        "B every apparatus record is admissible under its own actual six-neighbor condition",
        all(common_available(actual_neighbor_tuple(record.site, apparatus_map), record.content) for record in apparatus),
    )

    labeled_contexts = tuple(product((0, 1), repeat=7))
    check("B all 128 labeled nearest-neighbor contexts are covered", len(labeled_contexts) == 128)
    for name, law in (("A", LAW_A), ("B", LAW_B)):
        rotation_invariant = True
        for context in labeled_contexts:
            central, neighbors = context[0], context[1:]
            expected = law.respond(central, neighbors)
            for rotation in ROTATIONS:
                rotated = tuple(neighbors[rotation[index]] for index in range(6))
                rotation_invariant &= law.respond(central, rotated) == expected
        check(f"B law {name} is invariant under all proper cubic rotations", rotation_invariant)

        flip_covariant = all(
            law.respond(1 - context[0], tuple(1 - bit for bit in context[1:]))
            == 1 - law.respond(context[0], context[1:])
            for context in labeled_contexts
        )
        check(f"B law {name} is globally bit-flip covariant", flip_covariant)
        check(
            f"B law {name} genuinely varies with nearest-neighbor conditions",
            any(
                law.respond(central, (0, 0, 0, 0, 0, 0))
                != law.respond(central, (1, 0, 0, 0, 0, 0))
                for central in (0, 1)
            ),
        )
        site_tables = tuple(
            # The law has no coordinate argument: translating the same local
            # context therefore returns the identical extensional table.
            tuple(law.count_response(central, count) for central, count in TOTALISTIC_CONTEXTS)
            for _site in ((0, 0, 0), (5, -2, 9), (-11, 4, 1))
        )
        check(f"B law {name} is translation homogeneous", len(set(site_tables)) == 1)
        check(
            f"B law {name} outputs are admissible in the shared reduct",
            all(
                common_available(
                    condition,
                    PROJECTORS[f"P{law.respond(central, neighbors)}"],
                )
                for central in (0, 1)
                for neighbors in product((0, 1), repeat=6)
                for condition in neighbor_conditions
            ),
        )

    differences = [context for context in TOTALISTIC_CONTEXTS if LAW_A.table()[context] != LAW_B.table()[context]]
    check("B laws A and B are extensionally distinct", LAW_A != LAW_B)
    check("B laws A and B disagree on every totalistic count row", len(differences) == len(TOTALISTIC_CONTEXTS), f"rows={len(differences)}")
    check("B the two tables are bitwise complements", all(LAW_B.table()[c] == 1 - LAW_A.table()[c] for c in TOTALISTIC_CONTEXTS))


def writer_geometry_predicates(corpus: WriterCorpus) -> dict[str, bool]:
    apparatus = site_record_map(corpus.apparatus)
    context_sites = set(apparatus)
    occupancy = dict(apparatus)
    prior_blocks: set[Site] = set()
    predicates = {
        "target_absent": True,
        "storage_context_disjoint": True,
        "storage_prior_disjoint": True,
        "actual_neighbor_tuple": True,
        "output_admissible": True,
        "role_context_physical": True,
    }
    for record in ordered_chain(corpus.outputs):
        context = decode_context(apparatus, record.role.context_center)
        block = frozenset((record.site, *nearest_neighbor_sites(record.site)))
        neighbors = actual_neighbor_tuple(record.site, occupancy)
        predicates["target_absent"] &= record.site not in occupancy
        predicates["storage_context_disjoint"] &= not bool(block & context_sites)
        predicates["storage_prior_disjoint"] &= not bool(block & prior_blocks)
        predicates["actual_neighbor_tuple"] &= neighbors == (None,) * 6
        predicates["output_admissible"] &= common_available(neighbors, record.content)
        predicates["role_context_physical"] &= (
            record.role.context_center == context_center(context)
            and record.site == storage_target(context)
        )
        occupancy[record.site] = record.content
        prior_blocks.update(block)
    return predicates


def self_description_checks() -> None:
    section("C - Two exact self-description fixed points")
    schedules = (
        TOTALISTIC_CONTEXTS,
        tuple(reversed(TOTALISTIC_CONTEXTS)),
        TOTALISTIC_CONTEXTS[5:] + TOTALISTIC_CONTEXTS[:5],
    )
    decoded_by_law: dict[str, set[tuple[tuple[tuple[int, int], int], ...]]] = {"A": set(), "B": set()}
    for name, law in (("A", LAW_A), ("B", LAW_B)):
        for schedule_index, schedule in enumerate(schedules):
            corpus = universal_writer_corpus(law, schedule)
            scrambled = replace(corpus, outputs=tuple(reversed(corpus.outputs)))
            decoded = decode_complete_table(scrambled)
            geometry = writer_geometry_predicates(corpus)
            decoded_by_law[name].add(tuple(sorted(decoded.items())))
            check(f"C law {name} schedule {schedule_index} reconstructs its own complete table", decoded == law.table())
            check(
                f"C law {name} schedule {schedule_index} has an open target before every write",
                geometry["target_absent"],
            )
            check(
                f"C law {name} schedule {schedule_index} storage blocks avoid all context/apparatus records",
                geometry["storage_context_disjoint"],
            )
            check(
                f"C law {name} schedule {schedule_index} storage blocks avoid every prior storage block",
                geometry["storage_prior_disjoint"],
            )
            check(
                f"C law {name} schedule {schedule_index} uses the target's actual open-neighbor tuple",
                geometry["actual_neighbor_tuple"],
            )
            check(
                f"C law {name} schedule {schedule_index} locks an admissible P0/P1 at the actual target",
                geometry["output_admissible"]
                and all(record.content in (PROJECTORS["P0"], PROJECTORS["P1"]) for record in corpus.outputs),
            )
            check(
                f"C law {name} schedule {schedule_index} role metadata points to the physical context and storage blocks",
                geometry["role_context_physical"],
            )
            check(
                f"C law {name} schedule {schedule_index} uses one fresh site per record",
                len({record.site for record in corpus.outputs}) == len(corpus.outputs),
            )
            check(
                f"C law {name} schedule {schedule_index} is append-only at every prefix",
                all(
                    corpus.outputs[:index]
                    == tuple(list(corpus.outputs[: index + 1])[:index])
                    for index in range(1, len(corpus.outputs))
                ),
            )
            check(
                f"C law {name} schedule {schedule_index} has additive content-only scalar readout",
                finite_readout(tuple(record.content for record in corpus.outputs))
                == finite_readout(tuple(record.content for record in corpus.outputs[:5]))
                + finite_readout(tuple(record.content for record in corpus.outputs[5:]))
                and finite_readout(()) == 0.0,
            )

    check("C scheduler and storage order do not change law A's decoded table", len(decoded_by_law["A"]) == 1)
    check("C scheduler and storage order do not change law B's decoded table", len(decoded_by_law["B"]) == 1)
    check("C self-description map has at least two fixed points", decoded_by_law["A"] != decoded_by_law["B"])
    check(
        "C onsite record schema contains only site and one M2 content plus typed role metadata",
        {field.name for field in fields(TableRecord)} == {"site", "content", "role"}
        and {field.name for field in fields(SpatialCausalRole)}
        == {"event_id", "parent_id", "context_center"},
    )
    check(
        "C record and role schemas contain no law identifier",
        "law"
        not in {
            *(field.name for field in fields(TableRecord)),
            *(field.name for field in fields(SpatialCausalRole)),
        },
    )

    corpus_a = universal_writer_corpus(LAW_A)
    corpus_b = universal_writer_corpus(LAW_B)
    same_headers_and_contexts = (
        corpus_a.apparatus == corpus_b.apparatus
        and all(
            (left.role, left.site) == (right.role, right.site)
            for left, right in zip(corpus_a.outputs, corpus_b.outputs)
        )
    )
    check("C both laws use the identical apparatus, headers, sites, and contexts", same_headers_and_contexts)
    check(
        "C only physical outcome content distinguishes the two corpora",
        all(
            binary_outcome(left.content) != binary_outcome(right.content)
            for left, right in zip(corpus_a.outputs, corpus_b.outputs)
        ),
    )

    missing = replace(corpus_a, outputs=corpus_a.outputs[:-1])
    try:
        decode_complete_table(missing)
        missing_rejected = False
    except ValueError:
        missing_rejected = True
    check("C missing context row is rejected", missing_rejected)

    last = corpus_a.outputs[-1]
    conflicting_record = replace(
        last,
        site=(10_000, 20, 0),
        content=PROJECTORS[f"P{1 - binary_outcome(last.content)}"],
        role=replace(
            last.role,
            event_id="extra",
            parent_id=last.role.event_id,
        ),
    )
    conflicting = replace(corpus_a, outputs=corpus_a.outputs + (conflicting_record,))
    try:
        decode_complete_table(conflicting)
        conflict_rejected = False
    except ValueError:
        conflict_rejected = True
    check("C conflicting duplicate context row is rejected", conflict_rejected)


def foundation_confluence_checks() -> None:
    section("D - Coverage plus confluence versus empirical identification")
    candidate_tables = {"A": LAW_A.table(), "B": LAW_B.table()}
    decoded_classes = {
        name: tuple(sorted(decode_complete_table(universal_writer_corpus(law)).items()))
        for name, law in (("A", LAW_A), ("B", LAW_B))
    }
    check("D each empirical corpus identifies one candidate inside the supplied two-law class", all(decoded_classes[name] == tuple(sorted(table.items())) for name, table in candidate_tables.items()))
    candidate_classes = set(decoded_classes.values())
    certified_image = set(decoded_classes.values())
    incomplete_image = {decoded_classes["A"]}
    check("D certified reconstruction covers the supplied two-law candidate class", certified_image == candidate_classes)
    check("D covered image is non-singleton so confluence fails for the two-law witness", len(certified_image) == 2)
    check("D singleton image without candidate-class coverage is insufficient", len(incomplete_image) == 1 and incomplete_image != candidate_classes)
    check("D same-context record readout separates the candidates", all(candidate_tables["A"][context] != candidate_tables["B"][context] for context in TOTALISTIC_CONTEXTS))
    check("D no record-faithful quotient preserving context and scalar content identifies A with B", decoded_classes["A"] != decoded_classes["B"])


def positive_singleton_checks() -> None:
    section("E - Positive collapse in a declared affine-totalistic subclass")
    affine_class = tuple(AffineLaw(a, b, d) for a, b, d in product((0, 1), repeat=3))
    check("E affine-totalistic candidate class has eight laws", len(affine_class) == 8)

    labeled_contexts = tuple(product((0, 1), repeat=7))
    flip_covariant = tuple(
        law
        for law in affine_class
        if all(
            law.respond(1 - context[0], tuple(1 - bit for bit in context[1:]))
            == 1 - law.respond(context[0], context[1:])
            for context in labeled_contexts
        )
    )
    check("E global bit-flip covariance reduces 8 laws to 4", len(flip_covariant) == 4)

    neighbor_sensitive = tuple(
        law
        for law in flip_covariant
        if any(
            law.respond(central, (0, 0, 0, 0, 0, 0))
            != law.respond(central, (1, 0, 0, 0, 0, 0))
            for central in (0, 1)
        )
    )
    check("E genuine nearest-neighbor variation reduces 4 laws to 2", len(neighbor_sensitive) == 2)
    check("E the surviving pair is exactly A and B", set(neighbor_sensitive) == {LAW_A, LAW_B})

    uniform_persistent = tuple(
        law
        for law in neighbor_sensitive
        if law.count_response(0, 0) == 0 and law.count_response(1, 6) == 1
    )
    check("E uniform-state persistence reduces 2 laws to 1", uniform_persistent == (LAW_A,))
    selected = uniform_persistent[0]
    decoded = decode_complete_table(universal_writer_corpus(selected))
    check("E the positively selected law remains exactly self-describing", decoded == selected.table())
    selected_candidate_classes = {tuple(sorted(selected.table().items()))}
    selected_certified_image = {tuple(sorted(decoded.items()))}
    check("E the restricted certified image covers the selected candidate class", selected_certified_image == selected_candidate_classes)
    check("E the covered restricted self-description image is a singleton", len(selected_certified_image) == 1)

    code_a = (LAW_A.central_coefficient, LAW_A.neighbor_parity_coefficient, LAW_A.constant)
    code_b = (LAW_B.central_coefficient, LAW_B.neighbor_parity_coefficient, LAW_B.constant)
    check("E symmetric three-bit affine encoding does not prefer A by length", len(code_a) == len(code_b))


def source_and_scope_contract() -> None:
    section("A - Source, authority, and scope contract")
    sources = (NOTE, AXIOMS, REALIZED, CYCLE42, CYCLE45, CANONICAL, UNIQUE_EXTENSION, EQUIVALENCE, FINAL_CENSUS)
    for path in sources:
        check(f"A source exists: {path.name}", path.is_file())

    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    realized = normalized(REALIZED)
    cycle45 = normalized(CYCLE45)
    canonical = normalized(CANONICAL)
    equivalence = normalized(EQUIVALENCE)

    check("A note is authority-free", "authority: none" in note)
    check("A note disclaims axiom and primitive edits", "does not amend an axiom, enlarge a primitive" in note)
    check("A note disclaims audit authority", "issue an audit verdict" in note)
    check("A note carries fresh N1-N8", all(f"n{i} —" in note for i in range(1, 9)))
    check("A live foundation says records form", "records form" in axioms)
    check("A live Admissibility remains non-dynamics", "admissibility is not a dynamics axiom" in axioms)
    check("A realized-state primitive remains pointwise", "derivations may evaluate at the realized state, pointwise" in realized)
    check("A Cycle 45 distinguishes reconstruction from foundation selection", "not selection of l* by the foundation" in cycle45)
    check("A canonical contract permits exact equivalence-class closure", "prove that all remaining rule representatives are physically equivalent" in canonical)
    check("A equivalence source requires record-preserving law equivalence", "preserving record labels, event order, and scalar readout" in equivalence)

    required = (
        "foundation-wide self-description confluence",
        "two fixed points",
        "10 neighbor-pattern orbits",
        "20 contexts",
        "supplies the stronger totalism",
        "same explicit, total reduct",
        "each eta_j is either open or carries arbitrary m_2(c) record content",
        "i(a)=re tr(p1 a)",
        "event and parent identifiers are fixed spatial/causal role metadata",
        "actual pre-write neighbor tuple is six open sites",
        "s_f=c_f",
        "singleton s_f alone is not sufficient",
        "conditional operational sector",
        "not a universal no-go",
        "affine-totalistic singleton theorem",
        "uniform-state persistence",
        "the current foundation does not supply",
        "no live axiom, primitive, registry, audit, commit, or pr surface is changed",
    )
    for phrase in required:
        check(f"A note contains: {phrase}", phrase in note)


def no_go_discipline_contract() -> None:
    section("F - Fresh N1-N8 no-go-discipline contract")
    raw = NOTE.read_text(encoding="utf-8")
    parts = {number: markdown_subsection(raw, number) for number in range(1, 9)}
    compact = {number: " ".join(part.split()) for number, part in parts.items()}

    attempted_rows = [line for line in parts[1].splitlines() if line.startswith("|") and "| attempted |" in line]
    check("F N1 marks at least eight routes ATTEMPTED", len(attempted_rows) >= 8, f"count={len(attempted_rows)}")
    for route in (
        "self-description alone",
        "lattice symmetry and covariance",
        "record-faithful quotient",
        "description-length selection",
        "canonical decoder fixed point",
        "empirical corpus selection",
        "affine uniform-persistence filter",
        "coverage plus foundation-wide confluence",
    ):
        check(f"F N1 includes route: {route}", route in parts[1])

    for wall in ("w_c", "w_p", "w_i", "w_e"):
        check(f"F N2 names {wall}", wall in parts[2])
    for pair in (
        "`w_c`, `w_p`",
        "`w_c`, `w_i`",
        "`w_c`, `w_e`",
        "`w_p`, `w_i`",
        "`w_p`, `w_e`",
        "`w_i`, `w_e`",
    ):
        check(f"F N2 tests pair {pair}", pair in parts[2])
    check("F N2 collapses to four walls", "collapsed wall set is {w_c,w_p,w_i,w_e}" in compact[2].replace("`", ""))

    for trigger in (
        "foundation-compatible",
        "self-describing",
        "complete",
        "same apparatus",
        "totalism",
        "common reduct",
        "neighbor condition",
        "event and parent identifiers",
        "fresh storage",
        "canonical",
        "uniform-state persistence",
        "record-faithful",
    ):
        check(f"F N3 classifies trigger: {trigger}", trigger in parts[3])
    check("F N3 reports zero hidden conditions", "unresolved hidden conditions: 0" in parts[3].replace("*", ""))

    for source in (
        CYCLE42.name.lower(),
        CYCLE45.name.lower(),
        CANONICAL.name.lower(),
        UNIQUE_EXTENSION.name.lower(),
        EQUIVALENCE.name.lower(),
    ):
        check(f"F N4 maps source: {source}", source in parts[4])
    check("F N4 labels positive comparator correctly", "positive comparator, not negative evidence" in parts[4])
    for locator in (
        "lines 99–118",
        "lines 95–113",
        "lines 13–26",
        "lines 175–195",
        "lines 61–69",
        "lines 19–48",
    ):
        check(f"F N4 gives exact locator: {locator}", locator in parts[4])

    for resolution in (
        "one totalistic count row",
        "complete 14-row totalistic table",
        "all 20 genuine proper-cubic contexts",
        "eight-law affine-totalistic class",
        "all proper-cubic boolean local rules",
        "full qubit/qca law space",
        "complete toe law",
    ):
        check(f"F N5 scopes resolution: {resolution}", resolution in parts[5])
    check("F N5 leaves three higher resolutions open", parts[5].count("not tested / open") >= 3)
    check("F N5 forbids universal no-go", "not a universal no-go" in parts[5])

    for path in (
        "affine-totalistic singleton theorem",
        "coverage plus foundation-wide confluence",
        "direct foundation uniqueness",
        "record-protocol equivalence",
        "self-testing corpus",
    ):
        check(f"F N6 includes path: {path}", path in parts[6])
    check("F N6 forces no axiom from the finite failure", "does not force a new axiom" in compact[6])

    for phrase in (
        "hostile steelman:",
        "strongest outcome:",
        "broad negative is not licensed",
        "bounded two-fixed-point result survives",
    ):
        check(f"F N7 contains: {phrase}", phrase in compact[7].replace("*", ""))

    n8_plain = compact[8].replace("*", "").replace("`", "")
    check("F N8 records docs phrase scan", "docs phrase scan" in n8_plain)
    check("F N8 records 67-ledger walk", "67 no_go_ledger.md files" in n8_plain)
    check("F N8 reports no exact prior closure", "no prior ledger entry with the exact self-description/foundation-selection residual" in n8_plain)
    check("F gate passes only bounded claim", "gate result: pass for the bounded two-fixed-point counterexample" in n8_plain)


def main() -> int:
    source_and_scope_contract()
    law_symmetry_checks()
    self_description_checks()
    foundation_confluence_checks()
    positive_singleton_checks()
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: self-description identifies each law from its supplied "
        "corpus, but foundation selection requires complete reconstruction "
        "coverage S_F=C_F plus a singleton certified image, or direct uniqueness |C_F|=1"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
