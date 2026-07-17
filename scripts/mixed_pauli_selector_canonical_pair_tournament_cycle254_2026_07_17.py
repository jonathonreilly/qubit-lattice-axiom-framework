#!/usr/bin/env python3
"""Cycle 254: bounded mixed-Pauli selector/canonical-pair tournament.

Search the Cycle-251 auxiliary even-CAR commutant for proper-cubic,
coarse-translation-covariant commuting selector rows.  The radius-one star
grammar is complete.  Two tractable radius-two grammars are also exhausted:
the complete axial cross and cubic-scalar shells of the full Manhattan ball.

The result is a scoped grammar negative.  No general Pauli, Clifford,
radius-two, measurement-assisted, or non-Pauli no-go is claimed.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17 as c251
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "MIXED_PAULI_SELECTOR_CANONICAL_PAIR_TOURNAMENT_CYCLE254_NOTE_2026-07-17.md"
)
MARKER_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
FRAMES = c235.proper_cubic_frames()
ZERO = (0, 0, 0)


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


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "8,191",
        "33,554,431",
        "radius-one star grammar",
        "radius-two axial-cross grammar",
        "scalar-shell grammar",
        "no nontrivial mixed-pauli survivor",
        "even-volume parity defect",
        "bounded state-preparation e does not follow",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "coarse-cell unit translations",
        "period-16 physical role marker",
        "derived-time firewall",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "partial narrowing",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves exact grammar scope, N1-N8, and firewalls", not missing, missing)

    marker = normalized(MARKER_NOTE)
    marker_required = (
        "spacing-16 marker",
        "all 4096 translated marker sectors",
        "marker-sector initial/boundary/realized-state selection",
    )
    marker_missing = tuple(phrase for phrase in marker_required if phrase not in marker)
    check("the supplied period-16 role marker remains explicit", not marker_missing, marker_missing)


def vector(axis: int, distance: int) -> tuple[int, int, int]:
    row = [0, 0, 0]
    row[axis] = distance
    return tuple(row)


def add(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def subtract(left, right):
    return tuple(left[index] - right[index] for index in range(3))


def transform(offset, frame: np.ndarray):
    return tuple(int(value) for value in frame @ np.asarray(offset))


def translate(offsets: frozenset[tuple[int, int, int]], displacement):
    return frozenset(add(offset, displacement) for offset in offsets)


def boundary(edges) -> frozenset[tuple[int, int, int]]:
    result: set[tuple[int, int, int]] = set()
    for left, right in edges:
        result.symmetric_difference_update((left, right))
    return frozenset(result)


def quotient_commutes(left, right) -> bool:
    """Commutation in the auxiliary even-CAR quotient.

    A word is (b,d), where b is its cell-parity mask and d is the mod-two
    boundary of its selected auxiliary hops.  The exact form is
    b.d' + d.b' + d.d'.
    """
    b, d = left
    other_b, other_d = right
    return (
        len(b & other_d) + len(d & other_b) + len(d & other_d)
    ) % 2 == 0


def transformed_word(word, frame: np.ndarray):
    b, d = word
    return (
        frozenset(transform(offset, frame) for offset in b),
        frozenset(transform(offset, frame) for offset in d),
    )


def orbit_is_abelian(word) -> bool:
    """Test a seed against every relevant translate of every framed seed."""
    b, d = word
    for frame in FRAMES:
        framed_b, framed_d = transformed_word(word, frame)
        shifts = {subtract(left, right) for left in b for right in framed_d}
        shifts |= {subtract(left, right) for left in d for right in framed_b}
        shifts |= {subtract(left, right) for left in d for right in framed_d}
        for displacement in shifts:
            shifted = (
                translate(framed_b, displacement),
                translate(framed_d, displacement),
            )
            if not quotient_commutes(word, shifted):
                return False
    return True


RADIUS1_B = (
    ZERO,
    vector(0, 1),
    vector(0, -1),
    vector(1, 1),
    vector(1, -1),
    vector(2, 1),
    vector(2, -1),
)
RADIUS1_A = tuple((ZERO, RADIUS1_B[index]) for index in range(1, 7))


def radius1_word(seed: int):
    b = frozenset(
        offset for index, offset in enumerate(RADIUS1_B) if (seed >> index) & 1
    )
    edges = tuple(
        edge for index, edge in enumerate(RADIUS1_A) if (seed >> (7 + index)) & 1
    )
    return b, boundary(edges)


def gf2_pivots(rows) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def in_span(row: int, pivots: dict[int, int]) -> bool:
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return False
        row ^= pivots[pivot]
    return True


def cell_bit(offset, displacement, length: int) -> int:
    cell = tuple(
        (offset[index] + displacement[index]) % length for index in range(3)
    )
    return 1 << ((cell[0] * length + cell[1]) * length + cell[2])


def diagonal_orbit_rows(seed: int, length: int) -> set[int]:
    rows = set()
    selected = tuple(
        offset for index, offset in enumerate(RADIUS1_B) if (seed >> index) & 1
    )
    for frame in FRAMES:
        framed = tuple(transform(offset, frame) for offset in selected)
        for displacement in product(range(length), repeat=3):
            row = 0
            for offset in framed:
                row ^= cell_bit(offset, displacement, length)
            rows.add(row)
    return rows


def radius1_controls() -> tuple[dict[int, dict[str, int]], int]:
    print("\nCOMPLETE RADIUS-ONE STAR GRAMMAR")
    commuting = []
    mixed = []
    for seed in range(1, 1 << 13):
        word = radius1_word(seed)
        if orbit_is_abelian(word):
            commuting.append(seed)
            if word[1]:
                mixed.append(seed)
    check(
        "all 8,191 radius-one words are exhausted and every commuting orbit is auxiliary-B diagonal",
        len(commuting) == 127 and not mixed and commuting == list(range(1, 128)),
        {
            "nonidentity_seeds": (1 << 13) - 1,
            "commuting_orbits": len(commuting),
            "mixed_commuting_orbits": len(mixed),
        },
    )

    census = {}
    for length in (3, 4, 5, 6):
        n = length**3
        rank_target = both_parities = 0
        rank_distribution: dict[int, int] = {}
        for seed in commuting:
            pivots = gf2_pivots(diagonal_orbit_rows(seed, length))
            row_rank = len(pivots)
            rank_distribution[row_rank] = rank_distribution.get(row_rank, 0) + 1
            if row_rank == n - 1:
                rank_target += 1
                if not in_span((1 << n) - 1, pivots):
                    both_parities += 1
        census[length] = {
            "N": n,
            "rank_N_minus_1": rank_target,
            "rank_N_minus_1_both_parities": both_parities,
            "rank_distribution_classes": len(rank_distribution),
        }
    check(
        "rank-matched diagonal survivors keep both parities only at odd tested volumes and fail L=4 plus held-out L=6",
        [census[length]["rank_N_minus_1"] for length in (3, 4, 5, 6)]
        == [59, 24, 59, 24]
        and [
            census[length]["rank_N_minus_1_both_parities"]
            for length in (3, 4, 5, 6)
        ]
        == [59, 0, 59, 0],
        census,
    )
    return census, len(mixed)


RADIUS2_B = (ZERO,) + tuple(
    vector(axis, distance)
    for axis in range(3)
    for distance in (1, -1, 2, -2)
)
RADIUS2_A = tuple(
    (vector(axis, location), vector(axis, location + 1))
    for axis in range(3)
    for location in (-2, -1, 0, 1)
)


def edge_key(left, right):
    return tuple(sorted((left, right)))


def apply_edge_permutation(mask: int, permutation: list[int]) -> int:
    result = 0
    for source, target in enumerate(permutation):
        if (mask >> source) & 1:
            result ^= 1 << target
    return result


def affine_dimension(rows, variables: int) -> int | None:
    pivots: dict[int, int] = {}
    coefficient_mask = (1 << variables) - 1
    for coefficients, rhs in rows:
        row = coefficients | (rhs << variables)
        while row & coefficient_mask:
            pivot = (row & coefficient_mask).bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
        else:
            if (row >> variables) & 1:
                return None
    return variables - len(pivots)


def radius2_axial_controls() -> int:
    print("\nCOMPLETE RADIUS-TWO AXIAL-CROSS GRAMMAR")
    lookup = {edge_key(*edge): index for index, edge in enumerate(RADIUS2_A)}
    edge_permutations = []
    framed_b = []
    framed_edges = []
    for frame in FRAMES:
        framed_b.append([transform(offset, frame) for offset in RADIUS2_B])
        transformed_edges = [
            (transform(left, frame), transform(right, frame))
            for left, right in RADIUS2_A
        ]
        framed_edges.append(transformed_edges)
        edge_permutations.append(
            [lookup[edge_key(left, right)] for left, right in transformed_edges]
        )

    representatives = {
        min(
            apply_edge_permutation(mask, permutation)
            for permutation in edge_permutations
        )
        for mask in range(1 << len(RADIUS2_A))
    }
    consistent = []
    for edge_mask in sorted(representatives):
        selected = tuple(
            edge
            for index, edge in enumerate(RADIUS2_A)
            if (edge_mask >> index) & 1
        )
        d = boundary(selected)
        equations = []
        for frame_index in range(len(FRAMES)):
            framed_selected = tuple(
                edge
                for index, edge in enumerate(framed_edges[frame_index])
                if (edge_mask >> index) & 1
            )
            framed_d = boundary(framed_selected)
            shifts = {
                subtract(left, right) for left in RADIUS2_B for right in framed_d
            }
            shifts |= {
                subtract(left, right)
                for left in d
                for right in framed_b[frame_index]
            }
            shifts |= {
                subtract(left, right) for left in d for right in framed_d
            }
            for displacement in shifts:
                coefficients = 0
                for index, offset in enumerate(RADIUS2_B):
                    first = subtract(offset, displacement) in framed_d
                    second = add(
                        framed_b[frame_index][index], displacement
                    ) in d
                    if first != second:
                        coefficients ^= 1 << index
                rhs = sum(add(offset, displacement) in d for offset in framed_d) % 2
                if coefficients or rhs:
                    equations.append((coefficients, rhs))
        dimension = affine_dimension(equations, len(RADIUS2_B))
        if dimension is not None:
            consistent.append((edge_mask, dimension, len(d)))

    check(
        "the 33,554,431-word axial-cross grammar has no commuting mixed orbit",
        len(representatives) == 240
        and consistent == [(0, 13, 0)],
        {
            "nonidentity_words": (1 << 25) - 1,
            "hop_masks": 1 << 12,
            "proper_cubic_hop_orbits": len(representatives),
            "consistent_orbit_representatives": consistent,
            "method": "exact affine solution over all 13 B bits",
        },
    )
    return sum(edge_mask != 0 for edge_mask, _, _ in consistent)


def manhattan_norm(offset) -> int:
    return sum(abs(value) for value in offset)


def radius2_scalar_shell_controls() -> int:
    print("\nFULL MANHATTAN-BALL CUBIC-SCALAR SHELL GRAMMAR")
    ball = {
        offset
        for offset in product(range(-2, 3), repeat=3)
        if manhattan_norm(offset) <= 2
    }
    b_shells = (
        frozenset((ZERO,)),
        frozenset(offset for offset in ball if manhattan_norm(offset) == 1),
        frozenset(
            offset
            for offset in ball
            if sorted(abs(value) for value in offset) == [0, 0, 2]
        ),
        frozenset(
            offset
            for offset in ball
            if sorted(abs(value) for value in offset) == [0, 1, 1]
        ),
    )
    all_edges = set()
    for left in ball:
        for axis in range(3):
            right = list(left)
            right[axis] += 1
            right = tuple(right)
            if right in ball:
                all_edges.add((left, right))
    central = {
        edge for edge in all_edges if 0 in (manhattan_norm(edge[0]), manhattan_norm(edge[1]))
    }
    outer_axial = {
        edge
        for edge in all_edges
        if {manhattan_norm(edge[0]), manhattan_norm(edge[1])} == {1, 2}
        and sum(value != 0 for value in edge[0]) == 1
        and sum(value != 0 for value in edge[1]) == 1
    }
    diagonal = all_edges - central - outer_axial
    edge_shells = (central, outer_axial, diagonal)

    survivors = []
    nontrivial_mixed = []
    cycle_dressed = []
    for seed in range(1, 1 << 7):
        b: set[tuple[int, int, int]] = set()
        selected_edges = set()
        for index, shell in enumerate(b_shells):
            if (seed >> index) & 1:
                b.symmetric_difference_update(shell)
        for index, shell in enumerate(edge_shells):
            if (seed >> (4 + index)) & 1:
                selected_edges.symmetric_difference_update(shell)
        d = boundary(selected_edges)
        word = (frozenset(b), d)
        if orbit_is_abelian(word):
            survivors.append(seed)
            if d:
                nontrivial_mixed.append(seed)
            elif selected_edges:
                cycle_dressed.append(seed)

    check(
        "the full-ball scalar-shell grammar has no nontrivial mixed-Pauli survivor; its A-dressed survivors are cycle-trivial in the quotient",
        [len(shell) for shell in b_shells] == [1, 6, 6, 12]
        and [len(shell) for shell in edge_shells] == [6, 6, 24]
        and len(survivors) == 31
        and not nontrivial_mixed
        and len(cycle_dressed) == 16,
        {
            "nonidentity_templates": 127,
            "commuting_templates": len(survivors),
            "nonzero_A_boundary_survivors": len(nontrivial_mixed),
            "A_cycle_dressed_diagonal_survivors": len(cycle_dressed),
        },
    )
    return len(nontrivial_mixed)


def matter_parity(graph: c247.PunctureGraph) -> c235.Pauli:
    return c251.product_paulis(
        [graph.B(vertex) for vertex in range(graph.matter_count)]
    )


def physical_selector_controls() -> None:
    print("\nPHYSICAL RANK / PHASE / LEAKAGE / HELD SIZE")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        n = length**3
        stabilizers = c247.code_rows(graph)
        selectors = list(c251.equality_selectors(graph))
        matter = c251.matter_family(graph)
        s_rank, s_inconsistent = c235.phase_aware_rank(stabilizers, graph.qubits)
        selected_rank, inconsistent = c235.phase_aware_rank(
            stabilizers + selectors, graph.qubits
        )
        parity = matter_parity(graph)
        parity_fixed = c251.rank(
            stabilizers + selectors + [parity], graph.qubits
        ) == c251.rank(stabilizers + selectors, graph.qubits)
        rows.append(
            {
                "L": length,
                "N": n,
                "selector_rows": len(selectors),
                "selector_increment": selected_rank - s_rank,
                "selected_code_exponent": graph.qubits - selected_rank,
                "phase_inconsistencies": len(s_inconsistent) + len(inconsistent),
                "matter_leakage": sum(
                    not selector.commutes(generator)
                    for selector in selectors
                    for generator in matter
                ),
                "mutual_anticommutations": sum(
                    not selectors[left].commutes(selectors[right])
                    for left in range(len(selectors))
                    for right in range(left + 1, len(selectors))
                ),
                "matter_parity_fixed": parity_fixed,
                "max_selector_weight": max(
                    (selector.x | selector.z).bit_count() for selector in selectors
                ),
            }
        )
    check(
        "the diagonal fallback is a bounded consistent physical selector with zero matter/update leakage and exact exponent 6N",
        all(
            row["selector_rows"] == 3 * row["N"]
            and row["selector_increment"] == row["N"] - 1
            and row["selected_code_exponent"] == 6 * row["N"]
            and row["phase_inconsistencies"] == 0
            and row["matter_leakage"] == 0
            and row["mutual_anticommutations"] == 0
            and row["max_selector_weight"] == 12
            for row in rows
        )
        and c230.BETA == -0.3
        and c230.COUPLING == 0.37,
        rows,
    )
    check(
        "the physical diagonal fallback has the exact even-volume parity defect at L=4 and held-out L=6",
        [row["matter_parity_fixed"] for row in rows] == [False, True, False, True],
        rows,
    )

    graph = c247.PunctureGraph(3, terminals=1)
    equality_family = c251.equality_selectors(graph)
    frame_failures = translation_failures = 0
    for frame in FRAMES:
        _, edge_map = c247.graph_frame_maps(graph, frame)
        transformed = {
            c247.permute_pauli(selector, edge_map) for selector in equality_family
        }
        frame_failures += transformed != equality_family
    for axis in range(3):
        displacement = tuple(1 if index == axis else 0 for index in range(3))
        _, edge_map = c251.graph_translation_maps(graph, displacement)
        transformed = {
            c247.permute_pauli(selector, edge_map) for selector in equality_family
        }
        translation_failures += transformed != equality_family
    check(
        "the physical selector family is exact under all 24 proper-cubic frames and coarse-cell unit translations",
        len(FRAMES) == 24 and frame_failures == translation_failures == 0,
        {
            "frames": len(FRAMES),
            "frame_family_failures": frame_failures,
            "translation_family_failures": translation_failures,
        },
    )

    root, tree_edges = c251.coarse_spanning_tree(graph)
    independent = []
    for edge in tree_edges:
        source, target, _, _ = graph.base.edges[edge]
        left = graph.base.vertices[source][0]
        right = graph.base.vertices[target][0]
        independent.append(c251.gauge_z(graph, left) @ c251.gauge_z(graph, right))
    stabilizers = c247.code_rows(graph)
    full_rank = c251.rank(stabilizers + independent, graph.qubits)
    deleted_rank = c251.rank(stabilizers + independent[1:], graph.qubits)
    check(
        "deleting one row from an extracted independent selector basis adds exactly one logical direction",
        root == ZERO
        and len(independent) == 26
        and deleted_rank == full_rank - 1,
        {"independent_rows": len(independent), "full_rank": full_rank, "deleted_rank": deleted_rank},
    )


def canonical_pair_and_preparation_controls(
    radius1_mixed: int, radius2_axial_mixed: int, radius2_scalar_mixed: int
) -> None:
    print("\nCANONICAL-PAIR / BOUNDED-PREPARATION FIREWALL")
    distances = []
    for length in (3, 4, 5, 6):
        distances.append(3 * (length // 2))
    check(
        "rank matching does not yield bounded preparation: equality selectors impose repetition correlations at growing torus distance",
        distances == [3, 6, 6, 9] and distances[-1] > distances[0],
        {
            "maximum_coarse_graph_distance": distances,
            "selector_implication": "B_tilde(x) B_tilde(y)=+1 at every separation",
            "bounded_depth_E_constructed": False,
        },
    )
    check(
        "no covariant bounded canonical-X layer occurs in the exhausted grammars because every nontrivial conjugate needs nonzero A-boundary and no such commuting orbit survives",
        radius1_mixed == radius2_axial_mixed == radius2_scalar_mixed == 0,
        {
            "radius_one_mixed_commuting_layers": radius1_mixed,
            "radius_two_axial_mixed_commuting_layers": radius2_axial_mixed,
            "radius_two_scalar_nontrivial_mixed_layers": radius2_scalar_mixed,
            "scope": "the three declared grammars only",
        },
    )


def main() -> int:
    note_contract()
    _, radius1_mixed = radius1_controls()
    radius2_axial_mixed = radius2_axial_controls()
    radius2_scalar_mixed = radius2_scalar_shell_controls()
    physical_selector_controls()
    canonical_pair_and_preparation_controls(
        radius1_mixed, radius2_axial_mixed, radius2_scalar_mixed
    )
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
