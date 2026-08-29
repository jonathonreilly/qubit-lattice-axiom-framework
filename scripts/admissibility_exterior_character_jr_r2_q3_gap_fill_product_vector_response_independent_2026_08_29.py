#!/usr/bin/env python3
"""Independent exact controls for the q=3 product-vector gap-fill response.

The calculation is deliberately separate from the primary runner.  It starts
from the seven original-link trace loops in each matched orientation, performs
all nonshared Haar contractions with a union-find index network, constructs
the three exact O(3) projectors, and derives the temporal response from the
per-link representation multiplicities of the six relevant histories.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

VECTOR = (1, -1)
CHANNEL_DIMENSIONS = (1, 3, 5)
OPEN_LINKS = ("h2", "h4")

Loop = tuple[tuple[str, int], ...]
Node = tuple[str, int]
Occurrence = tuple[str, Node, Node]


P2: Loop = (("u2", 1), ("h3", 1), ("v2", -1), ("h2", -1))
P3: Loop = (("u3", 1), ("h4", 1), ("v3", -1), ("h3", -1))
C0: Loop = (
    ("u0", 1), ("u1", 1), ("h2", 1),
    ("v1", -1), ("v0", -1), ("h0", -1),
)
C1: Loop = (
    ("u2", 1), ("u3", 1), ("h4", 1),
    ("v3", -1), ("v2", -1), ("h2", -1),
)
C2: Loop = (
    ("u4", 1), ("u5", 1), ("h6", 1),
    ("v5", -1), ("v4", -1), ("h4", -1),
)

LOOPS = {"p2": P2, "p3": P3, "c0": C0, "c1": C1, "c2": C2}


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[Node, Node] = {}

    def add(self, item: Node) -> None:
        self.parent.setdefault(item, item)

    def find(self, item: Node) -> Node:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: Node, right: Node) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def oriented_trace_occurrences(
    named_loops: tuple[tuple[str, Loop], ...],
) -> tuple[UnionFind, dict[str, list[Occurrence]]]:
    union_find = UnionFind()
    occurrences: dict[str, list[Occurrence]] = {}
    for trace_name, loop in named_loops:
        nodes = tuple((trace_name, position) for position in range(len(loop)))
        for node in nodes:
            union_find.add(node)
        for position, (link, direction) in enumerate(loop):
            left = nodes[position]
            right = nodes[(position + 1) % len(loop)]
            row, column = (left, right) if direction == 1 else (right, left)
            occurrences.setdefault(link, []).append((trace_name, row, column))
    return union_find, occurrences


def gap_fill_open_kernel(orientation: int) -> dict[str, object]:
    """Derive the open h2,h4 kernel without inserting its coefficient.

    Orientation zero contracts p2*C0*C2 against p3*C0*C1*C2.  Orientation
    one is its reflection.  Every nonopen link must occur exactly twice, so
    normalized Haar contributes delta(row,row') delta(col,col')/3.
    """

    if orientation == 0:
        named_loops = (
            ("left_p2", P2), ("left_c0", C0), ("left_c2", C2),
            ("right_p3", P3), ("right_c0", C0),
            ("right_c1", C1), ("right_c2", C2),
        )
        required_pairs = {
            "h2": (("left_p2", "right_c1"), ("left_c0", "right_c0")),
            "h4": (("left_c2", "right_c2"), ("right_p3", "right_c1")),
        }
    elif orientation == 1:
        named_loops = (
            ("left_p3", P3), ("left_c0", C0), ("left_c2", C2),
            ("right_p2", P2), ("right_c0", C0),
            ("right_c1", C1), ("right_c2", C2),
        )
        required_pairs = {
            "h2": (("left_c0", "right_c0"), ("right_p2", "right_c1")),
            "h4": (("left_p3", "right_c1"), ("left_c2", "right_c2")),
        }
    else:
        raise ValueError("orientation must be 0 or 1")

    union_find, occurrences = oriented_trace_occurrences(named_loops)
    external_links = tuple(sorted(set(occurrences) - set(OPEN_LINKS)))
    pairwise_external = True
    for link in external_links:
        pair = occurrences[link]
        pairwise_external &= len(pair) == 2
        if len(pair) != 2:
            continue
        _, left_row, left_column = pair[0]
        _, right_row, right_column = pair[1]
        union_find.union(left_row, right_row)
        union_find.union(left_column, right_column)

    roots = {union_find.find(node) for node in union_find.parent}
    open_roots_by_link: dict[str, set[Node]] = {}
    reduced_occurrences: dict[str, dict[str, tuple[Node, Node]]] = {}
    for link in OPEN_LINKS:
        reduced_occurrences[link] = {
            trace_name: (union_find.find(row), union_find.find(column))
            for trace_name, row, column in occurrences[link]
        }
        open_roots_by_link[link] = {
            root
            for endpoints in reduced_occurrences[link].values()
            for root in endpoints
        }
    open_roots = set().union(*open_roots_by_link.values())
    closed_classes = len(roots - open_roots)
    same_order_identity = all(
        reduced_occurrences[link][left] == reduced_occurrences[link][right]
        for link, pairs in required_pairs.items()
        for left, right in pairs
    )
    nonswapped_endpoints = all(
        row != column
        for link in OPEN_LINKS
        for row, column in reduced_occurrences[link].values()
    )
    factorized_open_links = open_roots_by_link["h2"].isdisjoint(
        open_roots_by_link["h4"]
    )
    coefficient = F(3**closed_classes, 3**len(external_links))
    return {
        "seven_traces": len(named_loops),
        "external_links": len(external_links),
        "pairwise_external": pairwise_external,
        "closed_classes": closed_classes,
        "open_classes": len(open_roots),
        "open_classes_by_link": tuple(
            len(open_roots_by_link[link]) for link in OPEN_LINKS
        ),
        "same_order_identity": same_order_identity and nonswapped_endpoints,
        "factorized_open_links": factorized_open_links,
        "kernel_coefficient": coefficient,
    }


def delta(left: int, right: int) -> int:
    return int(left == right)


def pair_index(first: int, second: int) -> int:
    return 3 * first + second


def vector_pair_projectors() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Scalar, antisymmetric, and symmetric-traceless projectors on V tensor V."""

    p0 = sp.zeros(9, 9)
    p1 = sp.zeros(9, 9)
    p2 = sp.zeros(9, 9)
    for a in range(3):
        for c in range(3):
            for e in range(3):
                for g in range(3):
                    row = pair_index(a, c)
                    column = pair_index(e, g)
                    identity = sp.Integer(delta(a, e) * delta(c, g))
                    swap = sp.Integer(delta(a, g) * delta(c, e))
                    trace = sp.Integer(delta(a, c) * delta(e, g))
                    p0[row, column] = trace / 3
                    p1[row, column] = (identity - swap) / 2
                    p2[row, column] = (identity + swap) / 2 - trace / 3
    return p0, p1, p2


def projector_certificate() -> dict[str, object]:
    projectors = vector_pair_projectors()
    identity = sp.eye(9)
    kernels = tuple(gap_fill_open_kernel(orientation) for orientation in (0, 1))
    coefficient = kernels[0]["kernel_coefficient"]
    traces = tuple(int(sp.trace(projector)) for projector in projectors)
    weights = tuple(
        tuple(coefficient * traces[left] * traces[right] for right in range(3))
        for left in range(3)
    )
    return {
        "projectors": projectors,
        "traces": traces,
        "idempotent": all(projector * projector == projector for projector in projectors),
        "orthogonal": all(
            projectors[left] * projectors[right] == sp.zeros(9, 9)
            for left in range(3) for right in range(3) if left != right
        ),
        "complete": sum(projectors, sp.zeros(9, 9)) == identity,
        "kernels": kernels,
        "weights": weights,
        "weight_sum": sum((sum(row, F(0)) for row in weights), F(0)),
    }


def repeated_fine_word(coarse_cells: frozenset[int]) -> frozenset[int]:
    return frozenset(
        fine for cell in coarse_cells for fine in (2 * cell, 2 * cell + 1)
    )


def parity_placements() -> tuple[tuple[int, int, int, int], ...]:
    y_word = repeated_fine_word(frozenset((0, 2)))
    z_word = repeated_fine_word(frozenset((0, 1, 2)))
    return tuple(
        (p_y, p_z, parity_y, parity_z)
        for p_y in range(6)
        for p_z in range(6)
        for parity_y in (-1, 1)
        for parity_z in (-1, 1)
        if y_word ^ (frozenset((p_y,)) if parity_y == -1 else frozenset())
        == z_word ^ (frozenset((p_z,)) if parity_z == -1 else frozenset())
    )


def character_moment(power: int) -> int:
    if power == 0:
        return 1
    if power == 1:
        return 0
    if power == 2:
        return 1
    raise ValueError("only the character moments used by the q=3 Gram are allowed")


def coarse_inner_product(left: frozenset[int], right: frozenset[int]) -> int:
    return sp.prod(
        character_moment(int(cell in left) + int(cell in right))
        for cell in range(3)
    )


def coarse_gram() -> dict[str, int]:
    y = frozenset((0, 2))
    z = frozenset((0, 1, 2))
    return {
        "YY": coarse_inner_product(y, y),
        "ZZ": coarse_inner_product(z, z),
        "YZ": coarse_inner_product(y, z),
    }


def scalar_in_vector_tensor(label: tuple[int, int]) -> bool:
    ell, parity = label
    return ell == 1 and parity == -1


def arbitrary_action_survivors() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    return tuple(
        (VECTOR, (ell, parity))
        for ell in range(9) for parity in (-1, 1)
        if scalar_in_vector_tensor((ell, parity))
    )


def exterior_n1_survivors() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    menu = (VECTOR, (1, 1), (0, -1))
    return tuple(
        (left, right)
        for left in menu for right in menu
        if left == VECTOR and scalar_in_vector_tensor(right)
    )


def signed_frames() -> tuple[sp.Matrix, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3, 3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            frames.append(matrix)
    return tuple(frames)


def physical_q_certificate() -> dict[str, object]:
    """Exact first-moment control for W2=x and W3=delta1*x^-1."""

    frames = signed_frames()
    mean_matrix = sum(frames, sp.zeros(3, 3)) / len(frames)
    entries = sp.symbols("d0:9")
    fixed_delta = sp.Matrix(3, 3, entries)
    p2_mean = sp.trace(mean_matrix)
    p3_mean = sp.trace(fixed_delta * mean_matrix.T)
    history_means = (p2_mean, p2_mean, p3_mean, p3_mean)
    return {
        "frame_count": len(frames),
        "mean_matrix_zero": mean_matrix == sp.zeros(3, 3),
        "p2_mean": p2_mean,
        "p3_mean": p3_mean,
        "history_means": history_means,
        "crossing_preserves_zero_given_commutator": all(value == 0 for value in history_means),
    }


def tensor_spin_range(left_spin: int, right_spin: int) -> tuple[int, ...]:
    return tuple(range(abs(left_spin - right_spin), left_spin + right_spin + 1))


def acted_rung_certificate() -> dict[str, object]:
    """Resolve (M,+) tensor V into its unique final-vector summand."""

    output_ranges = tuple(tensor_spin_range(channel, 1) for channel in range(3))
    vector_multiplicities = tuple(outputs.count(1) for outputs in output_ranges)
    full_v3_multiplicities = Counter(
        output for outputs in output_ranges for output in outputs
    )
    return {
        "output_ranges": output_ranges,
        "output_parity": -1,
        "vector_multiplicities": vector_multiplicities,
        "unique_vector_each_channel": vector_multiplicities == (1, 1, 1),
        "full_v3_multiplicities": dict(sorted(full_v3_multiplicities.items())),
    }


def link_multiplicities(loop_names: tuple[str, ...]) -> Counter[str]:
    return Counter(link for name in loop_names for link, _direction in LOOPS[name])


HISTORY_LOOPS = {
    "Y": ("c0", "c2"),
    "Z": ("c0", "c1", "c2"),
    "p2Y": ("p2", "c0", "c2"),
    "p3Y": ("p3", "c0", "c2"),
    "p3Z": ("p3", "c0", "c1", "c2"),
    "p2Z": ("p2", "c0", "c1", "c2"),
}


def temporal_signature(history: str, left_channel: int, right_channel: int) -> dict[str, object]:
    counts = link_multiplicities(HISTORY_LOOPS[history])
    channel_by_link: dict[str, int] = {}
    acted_triple: dict[str, int] = {}
    forced_scalar_links: set[str] = set()
    if history == "Z":
        channel_by_link = {"h2": left_channel, "h4": right_channel}
    elif history == "p2Y":
        channel_by_link = {"h2": left_channel}
    elif history == "p3Y":
        channel_by_link = {"h4": right_channel}
    elif history == "p3Z":
        channel_by_link = {"h2": left_channel}
        acted_triple = {"h4": right_channel}
        forced_scalar_links = {"u3", "v3"}
    elif history == "p2Z":
        channel_by_link = {"h4": right_channel}
        acted_triple = {"h2": left_channel}
        forced_scalar_links = {"u2", "v2"}

    vector_power = 0
    channel_powers = [0, 0, 0]
    valid = True
    triple = acted_rung_certificate()
    for link, multiplicity in counts.items():
        if multiplicity == 1:
            vector_power += 1
        elif multiplicity == 2 and link in channel_by_link:
            channel_powers[channel_by_link[link]] += 1
        elif multiplicity == 2 and link in forced_scalar_links:
            pass
        elif multiplicity == 3 and link in acted_triple:
            input_channel = acted_triple[link]
            valid &= triple["vector_multiplicities"][input_channel] == 1
            vector_power += 1
        else:
            valid = False
    return {
        "counts": counts,
        "vector_power": vector_power,
        "channel_powers": tuple(channel_powers),
        "acted_triple": acted_triple,
        "forced_scalar_links": tuple(sorted(forced_scalar_links)),
        "valid": valid,
    }


def signature_expression(signature: dict[str, object], t, u):
    multipliers = (sp.Integer(1), t, u)
    result = t ** signature["vector_power"]
    for channel, power in enumerate(signature["channel_powers"]):
        result *= multipliers[channel] ** power
    return sp.expand(result)


def temporal_table(t, u) -> dict[tuple[str, int, int], sp.Expr]:
    table = {}
    for history in HISTORY_LOOPS:
        for left_channel in range(3):
            for right_channel in range(3):
                signature = temporal_signature(history, left_channel, right_channel)
                if not signature["valid"]:
                    raise AssertionError(f"invalid temporal signature for {history}")
                table[(history, left_channel, right_channel)] = signature_expression(
                    signature, t, u
                )
    return table


def expected_temporal_table(t, u) -> dict[tuple[str, int, int], sp.Expr]:
    x = (sp.Integer(1), t, u)
    expected = {}
    for left_channel in range(3):
        for right_channel in range(3):
            x_left = x[left_channel]
            x_right = x[right_channel]
            expected.update({
                ("Y", left_channel, right_channel): t**12,
                ("Z", left_channel, right_channel): t**14 * x_left * x_right,
                ("p2Y", left_channel, right_channel): t**14 * x_left,
                ("p3Y", left_channel, right_channel): t**14 * x_right,
                ("p3Z", left_channel, right_channel): t**14 * x_left,
                ("p2Z", left_channel, right_channel): t**14 * x_right,
            })
    return expected


def direct_response(t, u):
    certificate = projector_certificate()
    weights = certificate["weights"]
    table = temporal_table(t, u)
    result = 0
    for left_channel in range(3):
        for right_channel in range(3):
            first_orientation = (
                table[("Y", left_channel, right_channel)]
                + table[("p2Y", left_channel, right_channel)]
            ) * (
                table[("Z", left_channel, right_channel)]
                + table[("p3Z", left_channel, right_channel)]
            )
            second_orientation = (
                table[("Y", left_channel, right_channel)]
                + table[("p3Y", left_channel, right_channel)]
            ) * (
                table[("Z", left_channel, right_channel)]
                + table[("p2Z", left_channel, right_channel)]
            )
            result += sp.Rational(weights[left_channel][right_channel].numerator,
                                  weights[left_channel][right_channel].denominator) * (
                first_orientation + second_orientation
            )
    # The two leakage amplitudes each contain the supplied half-action factor 1/2.
    return sp.expand(result / 4)


def closed_response(t, u):
    first_moment = 1 + 3 * t + 5 * u
    second_moment = 1 + 3 * t**2 + 5 * u**2
    return sp.expand(
        t**14 * (9 + first_moment)
        * (t**12 * first_moment + t**14 * second_moment) / 486
    )


def temporal_channel_matrix(t, u) -> sp.Matrix:
    dimensions = CHANNEL_DIMENSIONS
    x = (sp.Integer(1), t, u)
    f = sp.Matrix([
        dimensions[channel] * t**14 * x[channel]
        * (t**12 + t**14 * x[channel])
        for channel in range(3)
    ])
    g = sp.Matrix([
        dimensions[channel] * (1 + x[channel]) for channel in range(3)
    ])
    return sp.simplify((f * g.T + g * f.T) / 972)


def independent_fixture() -> dict[str, object]:
    t, u = sp.symbols("t_V u_2", positive=True)
    projectors = projector_certificate()
    q_data = physical_q_certificate()
    acted = acted_rung_certificate()
    table = temporal_table(t, u)
    expected_table = expected_temporal_table(t, u)
    direct = direct_response(t, u)
    closed = closed_response(t, u)
    channel_matrix = temporal_channel_matrix(t, u)
    rational_point = {t: sp.Rational(1, 2), u: sp.Rational(1, 4)}
    data = {
        "projectors": projectors,
        "kernels": projectors["kernels"],
        "weights": projectors["weights"],
        "placements": parity_placements(),
        "gram": coarse_gram(),
        "action_survivors": arbitrary_action_survivors(),
        "exterior_survivors": exterior_n1_survivors(),
        "q": q_data,
        "acted": acted,
        "temporal_table": table,
        "expected_temporal_table": expected_table,
        "direct": direct,
        "closed": closed,
        "identity_limit": closed.subs({t: 1, u: 1}),
        "zero_limit": closed.subs(t, 0),
        "rational_value": closed.subs(rational_point),
        "spin_two_derivative": sp.expand(sp.diff(closed, u)),
        "channel_matrix_det": sp.factor(channel_matrix.det()),
        "channel_matrix_fixture_rank": channel_matrix.subs(rational_point).rank(),
        "channel_matrix_minor": sp.factor(channel_matrix[:2, :2].det()),
        "channel_matrix_sum": sp.expand(sum(channel_matrix)),
    }
    data["checks"] = independent_checks(data)
    return data


def independent_checks(
    data: dict[str, object] | None = None,
) -> tuple[tuple[str, bool], ...]:
    if data is None:
        # Avoid recursive construction: this is the same exact fixture without
        # its derived check list.
        t, u = sp.symbols("t_V u_2", positive=True)
        projectors = projector_certificate()
        q_data = physical_q_certificate()
        acted = acted_rung_certificate()
        table = temporal_table(t, u)
        expected_table = expected_temporal_table(t, u)
        direct = direct_response(t, u)
        closed = closed_response(t, u)
        channel_matrix = temporal_channel_matrix(t, u)
        rational_point = {t: sp.Rational(1, 2), u: sp.Rational(1, 4)}
        data = {
            "projectors": projectors,
            "kernels": projectors["kernels"],
            "weights": projectors["weights"],
            "placements": parity_placements(),
            "gram": coarse_gram(),
            "action_survivors": arbitrary_action_survivors(),
            "exterior_survivors": exterior_n1_survivors(),
            "q": q_data,
            "acted": acted,
            "temporal_table": table,
            "expected_temporal_table": expected_table,
            "direct": direct,
            "closed": closed,
            "identity_limit": closed.subs({t: 1, u: 1}),
            "zero_limit": closed.subs(t, 0),
            "rational_value": closed.subs(rational_point),
            "spin_two_derivative": sp.expand(sp.diff(closed, u)),
            "channel_matrix_det": sp.factor(channel_matrix.det()),
            "channel_matrix_fixture_rank": channel_matrix.subs(rational_point).rank(),
            "channel_matrix_minor": sp.factor(channel_matrix[:2, :2].det()),
            "channel_matrix_sum": sp.expand(sum(channel_matrix)),
        }
    kernels = data["kernels"]
    return (
        ("both seven-trace original-link orientations have fifteen external Haar pairs",
         all(kernel["seven_traces"] == 7 and kernel["external_links"] == 15
             and kernel["pairwise_external"] for kernel in kernels)),
        ("both contractions leave ten closed and eight factorized open index classes",
         all(kernel["closed_classes"] == 10 and kernel["open_classes"] == 8
             and kernel["open_classes_by_link"] == (4, 4)
             and kernel["factorized_open_links"] for kernel in kernels)),
        ("both open kernels are positive I tensor I divided by 243 without a swap",
         all(kernel["same_order_identity"]
             and kernel["kernel_coefficient"] == F(1, 243) for kernel in kernels)),
        ("the exact O(3) pair projectors are complete orthogonal idempotents of ranks 1,3,5",
         data["projectors"]["traces"] == (1, 3, 5)
         and data["projectors"]["idempotent"]
         and data["projectors"]["orthogonal"]
         and data["projectors"]["complete"]),
        ("the two-rung channel weights are d_L d_M over 243 and sum to one third",
         data["projectors"]["weights"] == (
             (F(1, 243), F(1, 81), F(5, 243)),
             (F(1, 81), F(1, 27), F(5, 81)),
             (F(5, 243), F(5, 81), F(25, 243)),
         ) and data["projectors"]["weight_sum"] == F(1, 3)),
        ("the q=3 101-to-111 parity selector leaves exactly p2,p3 and p3,p2",
         data["placements"] == ((2, 3, -1, -1), (3, 2, -1, -1))),
        ("the q=3 product states are normalized and orthogonal",
         data["gram"] == {"YY": 1, "ZZ": 1, "YZ": 0}),
        ("exclusive rails and the explicit exterior menu both force V,V action irreps",
         data["action_survivors"] == ((VECTOR, VECTOR),)
         and data["exterior_survivors"] == ((VECTOR, VECTOR),)),
        ("all four first-order histories have zero physical-Q conditional mean",
         data["q"]["frame_count"] == 48
         and data["q"]["mean_matrix_zero"]
         and data["q"]["history_means"] == (0, 0, 0, 0)
         and data["q"]["crossing_preserves_zero_given_commutator"]),
        ("every acted V-cubed rung has one selected final-vector copy for L=0,1,2",
         data["acted"]["output_ranges"] == ((1,), (0, 1, 2), (1, 2, 3))
         and data["acted"]["output_parity"] == -1
         and data["acted"]["unique_vector_each_channel"]
         and data["acted"]["full_v3_multiplicities"] == {0: 1, 1: 3, 2: 2, 3: 1}),
        ("the per-link irrep census gives the complete six-row temporal table",
         data["temporal_table"] == data["expected_temporal_table"]),
        ("the direct nine-channel Gram equals the closed A,B formula",
         sp.expand(data["direct"] - data["closed"]) == 0),
        ("identity and zero crossing controls give two thirds and zero",
         data["identity_limit"] == sp.Rational(2, 3) and data["zero_limit"] == 0),
        ("the exact t=1/2 u=1/4 response equals the independent rational fixture",
         data["rational_value"] == sp.Rational(1547, 927712935936)),
        ("spin-two crossing is load-bearing and the response-channel matrix sums correctly with generic rank two",
         data["spin_two_derivative"] != 0
         and data["channel_matrix_det"] == 0
         and data["channel_matrix_fixture_rank"] == 2
         and data["channel_matrix_minor"] != 0
         and sp.expand(data["channel_matrix_sum"] - data["closed"]) == 0),
    )


def main() -> int:
    data = independent_fixture()
    checks = data["checks"]
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
