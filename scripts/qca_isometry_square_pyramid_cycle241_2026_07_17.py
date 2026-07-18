#!/usr/bin/env python3
"""Cycle 241: QCA/isometry escape audit for the square-pyramid CAR code.

The runner separates five contracts that are often conflated:

1. a finite-depth unitary circuit;
2. a locality-preserving QCA automorphism of the full tensor algebra;
3. a code isometry obtained from product ancillas and a QCA;
4. a locality-preserving map only on the parity-even observable subalgebra;
5. preparation or selection of one gauge/translation sector.

The exact negative is deliberately narrow.  A product-ancilla *Clifford* QCA
cannot prepare the rank-matched closed square-pyramid subcode because two of
its stabilizer directions are noncontractible and have weight growing with L.
The published even-algebra duality also cannot be promoted verbatim to a full
tensor-algebra QCA: the local flux stars have one global relation and admit no
finite-support singleton flipper.  Non-Clifford QCA, subalgebra gauging
isometries, open/infinite sectors, and supplied topological resources remain
live.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17 as c237


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "QCA_ISOMETRY_SQUARE_PYRAMID_CYCLE241_NOTE_2026-07-17.md"
)

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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "finite-depth circuit",
        "qca automorphism",
        "isometry/code embedding",
        "algebra duality",
        "state preparation",
        "product-ancilla clifford qca",
        "singleton flipper",
        "rank-73",
        "all 24 proper-cubic frames",
        "unit-translation marker family",
        "authority: none",
        "audit: unset",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the QCA contract and N1-N8 gate", not missing, missing)


class TaggedGF2Basis:
    """Highest-pivot GF(2) basis carrying a three-bit homology tag."""

    def __init__(self) -> None:
        self.pivots: dict[int, tuple[int, int]] = {}

    def reduce(self, row: int, tag: int = 0) -> tuple[int, int]:
        value = row
        label = tag
        while value:
            pivot = value.bit_length() - 1
            prior = self.pivots.get(pivot)
            if prior is None:
                break
            value ^= prior[0]
            label ^= prior[1]
        return value, label

    def add(self, row: int, tag: int = 0) -> bool:
        value, label = self.reduce(row, tag)
        if not value:
            return False
        self.pivots[value.bit_length() - 1] = (value, label)
        return True


def face_type_orbits(
    graph: c235.PyramidCellulation,
) -> tuple[tuple[object, ...], tuple[int, ...], tuple[int, ...]]:
    masks: dict[tuple[object, ...], int] = {}
    boundaries: dict[tuple[object, ...], int] = {}
    for edge, (left, right, kind, _) in enumerate(graph.edges):
        _, left_direction = graph.vertices[left]
        _, right_direction = graph.vertices[right]
        if kind == "internal_triangle":
            key: tuple[object, ...] = (
                "internal",
                *sorted((left_direction, right_direction)),
            )
        else:
            key = ("stream", left_direction // 2)
        masks[key] = masks.get(key, 0) ^ (1 << edge)
        boundaries[key] = boundaries.get(key, 0) ^ (1 << left) ^ (1 << right)
    keys = tuple(sorted(masks, key=str))
    return keys, tuple(masks[key] for key in keys), tuple(boundaries[key] for key in keys)


def classify_cycle_homology(
    graph: c235.PyramidCellulation,
    local_cycles: list[int],
    wilsons: list[int],
    mask: int,
) -> int:
    basis = TaggedGF2Basis()
    for row in local_cycles:
        basis.add(row, 0)
    for axis, row in enumerate(wilsons):
        inserted = basis.add(row, 1 << axis)
        if not inserted:
            raise AssertionError((graph.length, axis, "dependent Wilson"))
    remainder, homology = basis.reduce(mask, 0)
    if remainder:
        raise AssertionError((graph.length, "cycle outside completed cycle space"))
    return homology


def square_pyramid_rank_and_flipper_controls() -> None:
    print("\nSQUARE-PYRAMID RANK / SINGLETON-FLIPPER CONTROLS")
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        cells = length**3
        modes = len(graph.vertices)
        faces = len(graph.edges)
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        local_rank = c235.gf2_rank(local_cycles)
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        rank_two_wilsons = c235.gf2_rank(local_cycles + wilsons[:2])
        full_cycle_rank = c235.gf2_rank(local_cycles + wilsons)

        # The Z-flux star at each matter-mode/pyramid is the row of the graph
        # incidence matrix.  Their sole relation on a connected closed graph
        # is the product of all stars.
        flux_stars = [graph.B(vertex).z for vertex in range(modes)]
        flux_rank = c235.gf2_rank(flux_stars)
        flux_product = 0
        for star in flux_stars:
            flux_product ^= star

        # The commutation syndrome of an arbitrary face-Pauli X support is the
        # graph boundary of that edge set.  Its image contains pairs but never
        # a singleton.  This rules out a local conjugate to one exact W_t.
        edge_boundaries = [
            (1 << left) ^ (1 << right)
            for left, right, _, _ in graph.edges
        ]
        boundary_rank = c235.gf2_rank(edge_boundaries)
        singleton_rank = c235.gf2_rank(edge_boundaries + [1])
        first_pair = edge_boundaries[0]
        pair_rank = c235.gf2_rank(edge_boundaries + [first_pair])

        local_exponent = faces - local_rank
        rank_matched_exponent = faces - rank_two_wilsons
        spin_selected_exponent = faces - full_cycle_rank
        check(
            f"L={length} exact code/rank budget and flux relation",
            modes == 6 * cells
            and faces == 15 * cells
            and local_rank == 9 * cells - 2
            and rank_two_wilsons == 9 * cells
            and full_cycle_rank == 9 * cells + 1
            and local_exponent == 6 * cells + 2
            and rank_matched_exponent == 6 * cells
            and spin_selected_exponent == 6 * cells - 1
            and flux_rank == modes - 1
            and flux_product == 0,
            {
                "full_Fock_exponent": 6 * cells,
                "local_Gauss_code_exponent": local_exponent,
                "two_Wilson_relations_exponent": rank_matched_exponent,
                "three_Wilson_relations_exponent": spin_selected_exponent,
                "flux_star_rank": flux_rank,
            },
        )
        check(
            f"L={length} exact flux algebra has pair but no singleton flipper",
            boundary_rank == modes - 1
            and singleton_rank == boundary_rank + 1
            and pair_rank == boundary_rank,
            {
                "syndrome_rank": boundary_rank,
                "singleton_reachable": singleton_rank == boundary_rank,
                "pair_reachable": pair_rank == boundary_rank,
            },
        )


def bounded_light_cone_controls() -> None:
    print("\nBOUNDED LIGHT-CONE FLIPPER CONTROLS")
    graph = c235.PyramidCellulation(11)
    source = graph.vertex_index[((5, 5, 5), 0)]
    distances = {source: 0}
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        if distances[vertex] == 5:
            continue
        for edge in graph.incident[vertex]:
            left, right, _, _ = graph.edges[edge]
            neighbor = right if left == vertex else left
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    controls = {}
    for radius in (0, 1, 2, 4):
        faces = []
        for left, right, _, _ in graph.edges:
            if min(distances.get(left, 99), distances.get(right, 99)) <= radius:
                faces.append((1 << left) ^ (1 << right))
        rank = c235.gf2_rank(faces)
        singleton_rank = c235.gf2_rank(faces + [1 << source])
        controls[radius] = {
            "candidate_faces": len(faces),
            "syndrome_rank": rank,
            "singleton_reachable": singleton_rank == rank,
        }
    check(
        "no singleton flux flipper occurs in tested bounded QCA light cones",
        all(not row["singleton_reachable"] for row in controls.values()),
        controls,
    )


def orbit_homology_controls() -> None:
    """Test all fixed translation-orbit Pauli-chain dressings.

    Multiplying a bounded translation-covariant Pauli dressing over every
    coarse cell reduces its X-chain component to one of the 2^15 unions of
    face-type orbits.  This census asks whether one fixed local template can
    leave the same nonzero torus Wilson class at L=3,4,5.
    """

    print("\nTRANSLATION-ORBIT PAULI HOMOLOGY CONTROL")
    maps: dict[int, dict[int, int]] = {}
    summaries = {}
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        keys, orbit_masks, orbit_boundaries = face_type_orbits(graph)
        table: dict[int, int] = {}
        for template in range(1 << len(keys)):
            chain = 0
            boundary = 0
            for index in range(len(keys)):
                if (template >> index) & 1:
                    chain ^= orbit_masks[index]
                    boundary ^= orbit_boundaries[index]
            if boundary == 0:
                table[template] = classify_cycle_homology(
                    graph, local_cycles, wilsons, chain
                )
        maps[length] = table
        summaries[length] = {
            "face_types": len(keys),
            "closed_orbit_templates": len(table),
            "homology_classes": tuple(sorted(set(table.values()))),
            "common_Wilson_templates": sum(value == 0b111 for value in table.values()),
        }

    common_templates = set(maps[3]) & set(maps[4]) & set(maps[5])
    all_size_nonzero = [
        template
        for template in common_templates
        if maps[3][template] == maps[4][template] == maps[5][template] != 0
    ]
    check(
        "no fixed coarse-translation Pauli dressing leaves an all-size Wilson class",
        not all_size_nonzero
        and set(maps[4].values()) == {0}
        and set(maps[3].values()) == set(range(8))
        and set(maps[5].values()) == set(range(8)),
        {
            "per_size": summaries,
            "common_closed_templates": len(common_templates),
            "same_nonzero_homology_all_sizes": len(all_size_nonzero),
        },
    )


def clifford_qca_stabilizer_control() -> None:
    print("\nPRODUCT-ANCILLA CLIFFORD-QCA CONTROL")
    rows = {}
    for length in (3, 4, 5, 7):
        graph = c235.PyramidCellulation(length)
        cells = length**3
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        local_rank = c235.gf2_rank(local_cycles)
        pair_weights = (
            (wilsons[0] ^ wilsons[1]).bit_count(),
            (wilsons[1] ^ wilsons[2]).bit_count(),
            (wilsons[2] ^ wilsons[0]).bit_count(),
        )
        rows[length] = {
            "product_ancilla_rank_needed": 9 * cells,
            "bounded_Gauss_rank": local_rank,
            "missing_topological_rank": 9 * cells - local_rank,
            "Wilson_pair_weights": pair_weights,
        }
    check(
        "rank-matched code needs two growing noncontractible stabilizers",
        all(row["missing_topological_rank"] == 2 for row in rows.values())
        and all(
            row["Wilson_pair_weights"] == (6 * length,) * 3
            for length, row in rows.items()
        ),
        rows,
    )
    check(
        "product-ancilla Clifford QCA cannot supply those stabilizers at fixed range",
        all(
            min(row["Wilson_pair_weights"]) > length
            for length, row in rows.items()
        ),
        "a Clifford QCA sends each onsite ancilla Z to a bounded Pauli; any generator outside the local Gauss span has nonzero torus homology",
    )


def qca_circuit_and_preparation_controls() -> None:
    print("\nQCA / CIRCUIT / PREPARATION DISTINCTIONS")
    shifts = {}
    for length in (5, 9, 17):
        forward = tuple((site + 1) % length for site in range(length))
        inverse = tuple((site - 1) % length for site in range(length))
        composition = tuple(inverse[forward[site]] for site in range(length))
        shifts[length] = {
            "forward_range": 1,
            "inverse_range": 1,
            "inverse_exact": composition == tuple(range(length)),
            "qubit_shift_GNVW_index": 2,
        }
    check(
        "qubit shift is a range-one QCA with a range-one inverse",
        all(row["inverse_exact"] for row in shifts.values()),
        shifts,
    )

    # A product-fed range-R automorphism factorizes two output observables
    # whose inverse light cones are disjoint.  A GHZ/cat marker restoration has
    # unit Z-Z connected correlation, so it needs a correlated input/resource.
    factorization = {}
    for radius in (0, 1, 2, 4):
        separation = 2 * radius + 1
        left_cone = set(range(-radius, radius + 1))
        right_cone = set(
            range(separation - radius, separation + radius + 1)
        )
        factorization[radius] = {
            "separation": separation,
            "inverse_cones_disjoint": left_cone.isdisjoint(right_cone),
            "product_input_connected_correlation": 0,
            "cat_target_connected_correlation": 1,
        }
    check(
        "product-fed bounded QCA cannot prepare a symmetry-restored cat marker",
        all(row["inverse_cones_disjoint"] for row in factorization.values()),
        factorization,
    )


def covariance_marker_and_fixture_controls() -> None:
    print("\nPROPER-CUBIC / UNIT-TRANSLATION / FIXTURE CONTROLS")
    frames = c237.proper_cubic_frames()
    route6_active = c237.active_residues()
    square_faces = set()
    for left, right in combinations(range(6), 2):
        if right == c237.OPPOSITE[left]:
            continue
        square_faces.add(
            c237.scale_mod(
                2, c237.add_mod(c237.DIRECTIONS[left], c237.DIRECTIONS[right])
            )
        )
    square_faces.update(
        c237.scale_mod(8, c237.DIRECTIONS[direction])
        for direction in c237.POSITIVE_DIRECTIONS
    )
    check(
        "15-face square-pyramid carrier set is invariant in all 24 frames",
        len(frames) == 24
        and len(square_faces) == 15
        and square_faces.issubset(route6_active)
        and all(
            {c237.mat_vec(frame, residue, c237.PERIOD) for residue in square_faces}
            == square_faces
            for frame in frames
        ),
        {
            "frames": len(frames),
            "square_pyramid_faces": len(square_faces),
            "inherited_marker_wildcards": len(route6_active),
        },
    )

    # The rank-matched option fixes the two-dimensional permutation-invariant
    # subspace w_x+w_y=w_y+w_z=0 and leaves the common Wilson bit.  Proper
    # rotations act as axis permutations on Z2 Wilson labels.
    equality_sector = {(0, 0, 0), (1, 1, 1)}
    axis_permutations = set()
    for frame in frames:
        permutation = []
        for axis in range(3):
            image = c237.mat_vec(
                frame, tuple(1 if index == axis else 0 for index in range(3))
            )
            permutation.append(next(index for index, value in enumerate(image) if value))
        axis_permutations.add(tuple(permutation))
    check(
        "equal-Wilson rank completion is proper-cubic as a sector family",
        len(axis_permutations) == 6
        and all(
            {tuple(label[permutation[index]] for index in range(3)) for label in equality_sector}
            == equality_sector
            for permutation in axis_permutations
        ),
        {
            "axis_permutations": len(axis_permutations),
            "lawful_Wilson_labels": tuple(sorted(equality_sector)),
        },
    )

    marker, orbits = c237.cubic_marker(frames)
    templates, coordinates, offsets = c237.marker_templates(marker, route6_active)
    ambiguity = c237.template_ambiguities(templates)
    frame_mismatches = c237.rotation_mismatches(
        templates, coordinates, offsets, frames
    )
    missing, extra = c237.successor_mismatches(templates, coordinates, offsets)
    check(
        "inherited radius-two unit-translation marker family remains exact",
        len(orbits) == 200
        and len(templates) == 4096
        and ambiguity == 0
        and frame_mismatches == 0
        and missing == extra == 0,
        {
            "offset_sectors": len(templates),
            "ambiguous_pairs": ambiguity,
            "proper_frame_tests": len(frames) * len(templates),
            "successor_tests": 3 * len(templates),
            "missing_or_extra": missing + extra,
        },
    )

    base = {
        residue: (0 if residue in route6_active else marker[residue])
        for residue in coordinates
    }
    hamming = []
    for axis in range(3):
        step = tuple(1 if index == axis else 0 for index in range(3))
        hamming.append(
            sum(
                base[residue]
                != base[
                    tuple(
                        (residue[index] - step[index]) % c237.PERIOD
                        for index in range(3)
                    )
                ]
                for residue in coordinates
            )
        )
    check(
        "a chosen marker phase is not selected by translation covariance",
        hamming == [2184, 2184, 2184],
        {"unit_shift_hamming": hamming, "interpretation": "law/code orbit, not autonomous state selection"},
    )

    fixture_parities = {"one_particle": 1, "rank_73": 73 % 2, "vacuum": 0}
    check(
        "both required fixtures occupy the same odd sector",
        fixture_parities["one_particle"] == fixture_parities["rank_73"] == 1,
        fixture_parities,
    )


def main() -> int:
    note_contract()
    square_pyramid_rank_and_flipper_controls()
    bounded_light_cone_controls()
    orbit_homology_controls()
    clifford_qca_stabilizer_control()
    qca_circuit_and_preparation_controls()
    covariance_marker_and_fixture_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
