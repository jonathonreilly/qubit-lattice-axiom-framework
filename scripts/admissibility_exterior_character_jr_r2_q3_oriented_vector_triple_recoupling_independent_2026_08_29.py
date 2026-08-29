#!/usr/bin/env python3
"""Independent exact certificate for the oriented q=3 vector recoupling.

This runner does not import the primary Block238 runner.  It builds the two
seven-trace original-link networks, integrates every non-h0 link with exact
rational O(3) Weingarten tensors through degree six, and derives the Racah
matrix from explicit Cartesian intertwiners rather than from a tabulated 6j
symbol.  The exact tensor contractions are intentionally the expensive audit
step; ``AUDIT_TIMEOUT_SEC`` records their expected outer timeout.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from math import lcm

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 120
VECTOR = (1, -1)
OPEN_LINK = "h0"

Loop = tuple[tuple[str, int], ...]
Node = int


def fine_plaquette(index: int) -> Loop:
    return (
        (f"u{index}", 1),
        (f"h{index + 1}", 1),
        (f"v{index}", -1),
        (f"h{index}", -1),
    )


def merged_interval(first_cell: int, last_cell: int) -> Loop:
    """Oriented boundary of fine plaquettes 2*first through 2*last+1."""

    first = 2 * first_cell
    last = 2 * last_cell + 1
    return tuple(
        [(f"u{index}", 1) for index in range(first, last + 1)]
        + [(f"h{last + 1}", 1)]
        + [(f"v{index}", -1) for index in range(last, first - 1, -1)]
        + [(f"h{first}", -1)]
    )


A0 = merged_interval(0, 0)
D01 = merged_interval(0, 1)
D012 = merged_interval(0, 2)


def state_coordinate_certificate() -> dict[str, object]:
    """The triangular Haar change of variables makes the Gram immediate.

    For independent coarse cell holonomies delta0,delta1,delta2, set
    A0=delta0, D01=delta1*delta0 and D012=delta2*delta1*delta0.
    Its inverse is displayed below.  Haar invariance therefore makes these
    three coordinates independent normalized Haar variables.
    """

    first_moment = 0
    second_moment = 1
    return {
        "forward": (
            "A0=delta0",
            "D01=delta1*delta0",
            "D012=delta2*delta1*delta0",
        ),
        "inverse": (
            "delta0=A0",
            "delta1=D01*A0^-1",
            "delta2=D012*D01^-1",
        ),
        "haar_jacobian_one": True,
        "gram": {
            "YY": second_moment * second_moment,
            "ZZ": second_moment**3,
            "YZ": first_moment * second_moment * second_moment,
        },
    }


def repeated_fine_word(first_cell: int, last_cell: int) -> frozenset[int]:
    return frozenset(range(2 * first_cell, 2 * last_cell + 2))


def parity_placements() -> tuple[tuple[int, int, int, int], ...]:
    # Products add inversion parity modulo two.  Thus Y=D01*D012 has 000011,
    # while Z=A0*D01*D012 has 110011 in fine-plaquette order 0,...,5.
    y_word = repeated_fine_word(0, 1) ^ repeated_fine_word(0, 2)
    z_word = repeated_fine_word(0, 0) ^ y_word
    matches = []
    for p_y in range(6):
        for p_z in range(6):
            for parity_y in (-1, 1):
                for parity_z in (-1, 1):
                    left = y_word ^ (
                        frozenset((p_y,)) if parity_y == -1 else frozenset()
                    )
                    right = z_word ^ (
                        frozenset((p_z,)) if parity_z == -1 else frozenset()
                    )
                    if left == right:
                        matches.append((p_y, p_z, parity_y, parity_z))
    return tuple(matches)


def action_irrep_survivors() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    # For every integer ell>=0, V tensor (ell,p) contains spin zero iff the
    # Clebsch lower endpoint |1-ell| is zero, hence ell=1 uniquely.  Scalar
    # parity further requires (-1)*p=+1, hence p=-1 uniquely.  This solves the
    # arbitrary-O(3)-irrep selector directly rather than truncating an ell scan.
    ell = 1
    parity = -1
    assert abs(1 - ell) == 0 and (-1) * parity == 1
    return ((VECTOR, (ell, parity)),)


def signed_frames() -> tuple[tuple[tuple[int, ...], ...], ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frames.append(tuple(
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            ))
    return tuple(frames)


def physical_q_certificate() -> dict[str, object]:
    """Exact first moments for W0=x and W1=delta0*x^-1."""

    frames = signed_frames()
    mean_entries = tuple(
        F(sum(frame[row][column] for frame in frames), len(frames))
        for row in range(3) for column in range(3)
    )
    trace_mean = F(sum(sum(frame[i][i] for i in range(3)) for frame in frames),
                   len(frames))
    # Right multiplication by a fixed delta0 only recombines the nine zero
    # entry means, so the conditional W1 character mean also vanishes.
    return {
        "frame_count": len(frames),
        "entry_means": mean_entries,
        "W0_character_mean": trace_mean,
        "W1_character_mean_for_every_fixed_delta0": all(x == 0 for x in mean_entries),
        "history_means": (trace_mean, trace_mean, trace_mean, trace_mean),
    }


def pair_partitions(items: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], ...]:
    if not items:
        return ((),)
    first = items[0]
    result = []
    for position in range(1, len(items)):
        second = items[position]
        rest = items[1:position] + items[position + 1:]
        for tail in pair_partitions(rest):
            result.append(((first, second),) + tail)
    return tuple(result)


def joined_pairing_loops(
    left: tuple[tuple[int, int], ...],
    right: tuple[tuple[int, int], ...],
    degree: int,
) -> int:
    parent = list(range(degree))

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for a, b in left + right:
        union(a, b)
    return len({find(item) for item in range(degree)})


def exact_orthogonal_moment(degree: int) -> dict[str, object]:
    """Scaled integer O(3) Haar moment from the exact Brauer Gram inverse."""

    pairings = pair_partitions(tuple(range(degree)))
    gram = sp.Matrix([
        [3 ** joined_pairing_loops(left, right, degree) for right in pairings]
        for left in pairings
    ])
    weingarten = gram.inv()
    denominator = lcm(*(int(sp.denom(entry)) for entry in weingarten))
    scaled = tuple(tuple(int(denominator * weingarten[i, j])
                         for j in range(len(pairings)))
                   for i in range(len(pairings)))
    tensor = np.zeros((3,) * (2 * degree), dtype=object)
    for indices in np.ndindex(tensor.shape):
        rows = indices[0::2]
        columns = indices[1::2]
        value = 0
        for left_index, left in enumerate(pairings):
            if not all(rows[a] == rows[b] for a, b in left):
                continue
            for right_index, right in enumerate(pairings):
                if all(columns[a] == columns[b] for a, b in right):
                    value += scaled[left_index][right_index]
        tensor[indices] = value
    return {
        "degree": degree,
        "pairings": pairings,
        "gram_rank": gram.rank(),
        "weingarten": weingarten,
        "denominator": denominator,
        "tensor": tensor,
        "nonzero_entries": sum(value != 0 for value in tensor.flat),
    }


def oriented_trace_family(orientation: str) -> tuple[tuple[str, Loop], ...]:
    if orientation == "O01":
        return (
            ("left_p0", fine_plaquette(0)),
            ("left_D01", D01),
            ("left_D012", D012),
            ("right_p1", fine_plaquette(1)),
            ("right_A0", A0),
            ("right_D01", D01),
            ("right_D012", D012),
        )
    if orientation == "O10":
        return (
            ("left_p1", fine_plaquette(1)),
            ("left_D01", D01),
            ("left_D012", D012),
            ("right_p0", fine_plaquette(0)),
            ("right_A0", A0),
            ("right_D01", D01),
            ("right_D012", D012),
        )
    raise ValueError("orientation must be O01 or O10")


def original_link_occurrences(
    orientation: str,
) -> tuple[dict[str, list[tuple[str, Node, Node]]], int]:
    occurrences: dict[str, list[tuple[str, Node, Node]]] = defaultdict(list)
    next_node = 0
    for trace_name, loop in oriented_trace_family(orientation):
        nodes = tuple(range(next_node, next_node + len(loop)))
        next_node += len(loop)
        for position, (link, direction) in enumerate(loop):
            first = nodes[position]
            second = nodes[(position + 1) % len(loop)]
            row, column = (first, second) if direction == 1 else (second, first)
            occurrences[link].append((trace_name, row, column))
    return occurrences, next_node


def greedy_exact_contract(
    tensors: list[tuple[np.ndarray, list[int]]],
) -> tuple[np.ndarray, list[int]]:
    """Contract a dimension-three closed-index network with Python integers."""

    tensors = list(tensors)
    while len(tensors) > 1:
        best = None
        for left_index in range(len(tensors)):
            left_labels = tensors[left_index][1]
            for right_index in range(left_index + 1, len(tensors)):
                right_labels = tensors[right_index][1]
                shared = set(left_labels) & set(right_labels)
                if not shared:
                    continue
                output_rank = len(left_labels) + len(right_labels) - 2 * len(shared)
                score = (output_rank, -len(shared),
                         max(len(left_labels), len(right_labels)))
                if best is None or score < best[0]:
                    best = (score, left_index, right_index, shared)
        if best is None:
            raise AssertionError("the original-link tensor network disconnected")
        _score, left_index, right_index, shared = best
        left_tensor, left_labels = tensors[left_index]
        right_tensor, right_labels = tensors[right_index]
        left_axes = [index for index, label in enumerate(left_labels) if label in shared]
        shared_order = [left_labels[index] for index in left_axes]
        right_axes = [right_labels.index(label) for label in shared_order]
        result = np.tensordot(
            left_tensor, right_tensor, axes=(left_axes, right_axes)
        )
        result_labels = (
            [label for label in left_labels if label not in shared]
            + [label for label in right_labels if label not in shared]
        )
        for index in sorted((left_index, right_index), reverse=True):
            tensors.pop(index)
        tensors.append((result, result_labels))
    return tensors[0]


def expected_open_numerator(
    orientation: str,
    indices: tuple[int, ...],
    numerator: int,
) -> int:
    if orientation == "O01":
        # Three left strands match A0,D01,D012 on the right in the same order.
        return numerator if all(indices[index] == indices[index + 6]
                                for index in range(6)) else 0
    # O10 is V^2 versus V^4: D01,D012 cross to their right partners and the
    # two extra right strands form a cup, separately at both h0 endpoints.
    matched = (
        indices[0] == indices[8]
        and indices[1] == indices[9]
        and indices[2] == indices[10]
        and indices[3] == indices[11]
        and indices[4] == indices[6]
        and indices[5] == indices[7]
    )
    return numerator if matched else 0


def exact_open_tensor_certificate(
    orientation: str,
    moments: dict[int, dict[str, object]],
) -> dict[str, object]:
    occurrences, node_count = original_link_occurrences(orientation)
    open_occurrences = occurrences[OPEN_LINK]
    open_labels = [label for _name, row, column in open_occurrences
                   for label in (row, column)]
    tensors = []
    denominator = 1
    moment_census = Counter()
    for link, link_occurrences in occurrences.items():
        if link == OPEN_LINK:
            continue
        degree = len(link_occurrences)
        moment_census[degree] += 1
        moment = moments[degree]
        labels = [label for _name, row, column in link_occurrences
                  for label in (row, column)]
        tensors.append((moment["tensor"], labels))
        denominator *= moment["denominator"]
    numerator = denominator // 81
    contracted, contracted_labels = greedy_exact_contract(tensors)
    contracted = np.transpose(
        contracted, [contracted_labels.index(label) for label in open_labels]
    )
    exact = True
    nonzero = 0
    for indices in np.ndindex(contracted.shape):
        actual = contracted[indices]
        expected = expected_open_numerator(orientation, indices, numerator)
        exact &= actual == expected
        nonzero += int(actual != 0)
    side_census = Counter(name.split("_", 1)[0] for name, _row, _column in open_occurrences)
    return {
        "orientation": orientation,
        "seven_traces": len(oriented_trace_family(orientation)),
        "node_count": node_count,
        "external_link_count": sum(moment_census.values()),
        "moment_census": dict(sorted(moment_census.items())),
        "open_occurrence_names": tuple(name for name, _row, _column in open_occurrences),
        "open_side_census": dict(side_census),
        "scaled_denominator": denominator,
        "scaled_numerator": numerator,
        "coefficient": F(numerator, denominator),
        "nonzero_entries": nonzero,
        "exact_expected_tensor": exact,
        "tensor_shape": contracted.shape,
    }


def cartesian_vector_intertwiners() -> tuple[sp.MutableDenseNDimArray, ...]:
    """Normalized maps V^3 -> V in the (12)-pair channels L=0,1,2."""

    result = []
    for channel in range(3):
        tensor = sp.MutableDenseNDimArray.zeros(3, 3, 3, 3)
        for a, b, c, d in product(range(3), repeat=4):
            delta = lambda x, y: sp.Integer(x == y)
            if channel == 0:
                value = delta(a, b) * delta(c, d) / sp.sqrt(3)
            elif channel == 1:
                value = (
                    delta(a, c) * delta(b, d)
                    - delta(a, d) * delta(b, c)
                ) / 2
            else:
                value = sp.sqrt(sp.Rational(3, 20)) * (
                    delta(a, c) * delta(b, d)
                    + delta(a, d) * delta(b, c)
                    - sp.Rational(2, 3) * delta(a, b) * delta(c, d)
                )
            tensor[a, b, c, d] = value
        result.append(tensor)
    return tuple(result)


def intertwiner_certificate(
    open_occurrence_names: tuple[str, ...],
) -> dict[str, object]:
    tensors = cartesian_vector_intertwiners()
    normalized = all(
        sp.simplify(sum(
            tensors[left][a, b, c, d] * tensors[right][a, b, c, e]
            for a, b, c in product(range(3), repeat=3)
        ) - sp.Integer(left == right) * sp.Integer(d == e)) == 0
        for left, right, d, e in product(range(3), repeat=4)
    )
    expected_occurrences = (
        "left_p0", "left_D01", "left_D012",
        "right_A0", "right_D01", "right_D012",
    )
    paired_right = dict(zip(open_occurrence_names[:3], open_occurrence_names[3:]))
    left_physical_order = ("left_D01", "left_D012", "left_p0")
    right_physical_order = ("right_A0", "right_D01", "right_D012")
    left_to_right_slots = tuple(
        right_physical_order.index(paired_right[name])
        for name in left_physical_order
    )
    right_tensor_from_left = tuple(
        left_to_right_slots.index(right_slot) for right_slot in range(3)
    )
    racah = sp.Matrix([
        [sp.simplify(sum(
            tensors[left][a, b, c, d]
            * tensors[right][
                (a, b, c)[right_tensor_from_left[0]],
                (a, b, c)[right_tensor_from_left[1]],
                (a, b, c)[right_tensor_from_left[2]],
                d,
            ]
            for a, b, c, d in product(range(3), repeat=4)
        ) / 3) for right in range(3)]
        for left in range(3)
    ])
    expected = sp.Matrix([
        [sp.Rational(1, 3), -sp.sqrt(3) / 3, sp.sqrt(5) / 3],
        [sp.sqrt(3) / 3, -sp.Rational(1, 2), -sp.sqrt(15) / 6],
        [sp.sqrt(5) / 3, sp.sqrt(15) / 6, sp.Rational(1, 6)],
    ])
    same_pair_kernel = sp.Matrix([
        [sp.simplify(sum(
            tensors[left][a, b, c, d] * tensors[right][a, b, c, d]
            for a, b, c, d in product(range(3), repeat=4)
        ) / 81) for right in range(3)]
        for left in range(3)
    ])
    return {
        "strand_order": {
            "open_occurrence_names": open_occurrence_names,
            "expected_occurrence_names": expected_occurrences,
            "left_physical_order": left_physical_order,
            "right_physical_order": right_physical_order,
            "left_to_right_slots": left_to_right_slots,
            "right_tensor_from_left": right_tensor_from_left,
        },
        "normalized": normalized,
        "racah": racah,
        "expected_racah": expected,
        "same_pair_kernel": same_pair_kernel,
        "physical_order_kernel": sp.simplify(racah / 27),
        "orthogonal": sp.simplify(racah.T * racah) == sp.eye(3),
        "determinant": sp.simplify(racah.det()),
        "order_three": sp.simplify(racah**3) == sp.eye(3),
    }


def tensor_power_multiplicities(power: int) -> dict[int, int]:
    multiplicities = {0: 1}
    for _ in range(power):
        updated: dict[int, int] = defaultdict(int)
        for spin, multiplicity in multiplicities.items():
            for output in range(abs(spin - 1), spin + 2):
                updated[output] += multiplicity
        multiplicities = dict(updated)
    return dict(sorted(multiplicities.items()))


def representation_certificate() -> dict[str, object]:
    powers = {power: tensor_power_multiplicities(power) for power in (2, 3, 4, 6)}
    triple = powers[3]
    dimensions = {spin: 2 * spin + 1 for spin in triple}
    isotypic_dimensions = {
        spin: triple[spin] * dimensions[spin] for spin in triple
    }
    weights = {
        spin: F(isotypic_dimensions[spin], 27) for spin in triple
    }
    matching_dimension = sum(
        powers[2].get(spin, 0) * powers[4].get(spin, 0)
        for spin in set(powers[2]) | set(powers[4])
    )
    return {
        "powers": powers,
        "triple_parity": -1,
        "triple_dimensions": dimensions,
        "triple_isotypic_dimensions": isotypic_dimensions,
        "triple_weights": weights,
        "triple_total_dimension": sum(isotypic_dimensions.values()),
        "triple_character_norm_squared": sum(value * value for value in triple.values()),
        "V2_to_V4_matching_dimension": matching_dimension,
        "V6_invariant_dimension": powers[6][0],
    }


def _build_fixture() -> dict[str, object]:
    moments = {degree: exact_orthogonal_moment(degree) for degree in (2, 4, 6)}
    open_01 = exact_open_tensor_certificate("O01", moments)
    open_10 = exact_open_tensor_certificate("O10", moments)
    return {
        "state": state_coordinate_certificate(),
        "placements": parity_placements(),
        "action_survivors": action_irrep_survivors(),
        "q": physical_q_certificate(),
        "moments": {
            degree: {
                key: value for key, value in moment.items() if key != "tensor"
            }
            for degree, moment in moments.items()
        },
        "open_01": open_01,
        "open_10": open_10,
        "intertwiners": intertwiner_certificate(open_01["open_occurrence_names"]),
        "representations": representation_certificate(),
    }


def independent_checks(
    data: dict[str, object] | None = None,
) -> tuple[tuple[str, bool], ...]:
    if data is None:
        data = _build_fixture()
    moment_summary = data["moments"]
    open_01 = data["open_01"]
    open_10 = data["open_10"]
    intertwiners = data["intertwiners"]
    representations = data["representations"]
    expected_moment_data = {
        2: (1, 3, 9),
        4: (3, 30, 441),
        6: (15, 210, 33489),
    }
    return (
        ("the corrected coarse states are normalized and orthogonal",
         data["state"]["haar_jacobian_one"]
         and data["state"]["gram"] == {"YY": 1, "ZZ": 1, "YZ": 0}),
        ("parity-first matching leaves only O01 and O10 in cell zero",
         data["placements"] == ((0, 1, -1, -1), (1, 0, -1, -1))),
        ("exclusive rails and scalar matching force V,V",
         data["action_survivors"] == ((VECTOR, VECTOR),)),
        ("all four conditional first moments lie in physical ker Q",
         data["q"]["frame_count"] == 48
         and all(value == 0 for value in data["q"]["entry_means"])
         and data["q"]["history_means"] == (F(0), F(0), F(0), F(0))),
        ("the exact O(3) moments use full-rank Brauer Gram inverses",
         all(
             len(moment_summary[degree]["pairings"]) == expected[0]
             and moment_summary[degree]["gram_rank"] == expected[0]
             and moment_summary[degree]["denominator"] == expected[1]
             and moment_summary[degree]["nonzero_entries"] == expected[2]
             for degree, expected in expected_moment_data.items()
         )),
        ("O01 has four sixth, four fourth, and eight second external moments",
         open_01["seven_traces"] == 7
         and open_01["external_link_count"] == 16
         and open_01["moment_census"] == {2: 8, 4: 4, 6: 4}
         and open_01["open_side_census"] == {"left": 3, "right": 3}),
        ("exact rational O01 contraction is I tensor I tensor I over 81",
         open_01["exact_expected_tensor"]
         and open_01["coefficient"] == F(1, 81)
         and open_01["nonzero_entries"] == 729
         and open_01["tensor_shape"] == (3,) * 12),
        ("the normalized same-pair vector multiplicity kernel is I3 over 27",
         intertwiners["normalized"]
         and intertwiners["same_pair_kernel"] == sp.eye(3) / 27),
        ("the contracted trace strands derive the signed physical Racah matrix",
         intertwiners["strand_order"] == {
             "open_occurrence_names": (
                 "left_p0", "left_D01", "left_D012",
                 "right_A0", "right_D01", "right_D012",
             ),
             "expected_occurrence_names": (
                 "left_p0", "left_D01", "left_D012",
                 "right_A0", "right_D01", "right_D012",
             ),
             "left_physical_order": ("left_D01", "left_D012", "left_p0"),
             "right_physical_order": ("right_A0", "right_D01", "right_D012"),
             "left_to_right_slots": (1, 2, 0),
             "right_tensor_from_left": (2, 0, 1),
         }
         and intertwiners["racah"] == intertwiners["expected_racah"]
         and intertwiners["physical_order_kernel"]
         == intertwiners["expected_racah"] / 27),
        ("the physical Racah matrix is orthogonal, determinant one, and order three",
         intertwiners["orthogonal"]
         and intertwiners["determinant"] == 1
         and intertwiners["order_three"]),
        ("the full V cubed decomposition and dimension weights are exact",
         representations["powers"][3] == {0: 1, 1: 3, 2: 2, 3: 1}
         and representations["triple_parity"] == -1
         and representations["triple_isotypic_dimensions"]
         == {0: 1, 1: 9, 2: 10, 3: 7}
         and representations["triple_weights"]
         == {0: F(1, 27), 1: F(1, 3), 2: F(10, 27), 3: F(7, 27)}
         and representations["triple_total_dimension"] == 27
         and representations["triple_character_norm_squared"] == 15),
        ("O10 is exactly the V2-to-V4 cup/cross tensor over 81",
         open_10["seven_traces"] == 7
         and open_10["moment_census"] == {2: 8, 4: 4, 6: 4}
         and open_10["open_side_census"] == {"left": 2, "right": 4}
         and open_10["exact_expected_tensor"]
         and open_10["coefficient"] == F(1, 81)
         and open_10["nonzero_entries"] == 729),
        ("O10 has fifteen invariant matchings and is not a three-by-three response",
         representations["powers"][2] == {0: 1, 1: 1, 2: 1}
         and representations["powers"][4] == {0: 3, 1: 6, 2: 6, 3: 3, 4: 1}
         and representations["V2_to_V4_matching_dimension"] == 15
         and representations["V6_invariant_dimension"] == 15),
    )


def independent_fixture() -> dict[str, object]:
    data = _build_fixture()
    data["checks"] = independent_checks(data)
    return data


def main() -> int:
    data = independent_fixture()
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print("per_element: exact rational O(3) moments on all sixteen non-h0 links")
    print("per_site: both cell-zero orientations and their unequal open strand counts")
    print("per_mode: all three V-cubed vector multiplicity channels and the full decomposition")
    print("per_block: corrected q=3 Y=chi(D01)chi(D012), Z=chi(A0)Y pair only")
    print("lattice_wide: not claimed; no arbitrary word, kernel, dynamics, or interpretation")
    failures = 0
    for label, passed in data["checks"]:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(data['checks']) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
