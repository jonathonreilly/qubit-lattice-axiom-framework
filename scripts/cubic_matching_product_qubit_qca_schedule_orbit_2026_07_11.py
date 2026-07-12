#!/usr/bin/env python3
"""Exact 720-schedule classification for CZ and iSWAP cubic matching circuits."""

import itertools
from collections import Counter
from pathlib import Path


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def vertices(side: int) -> list[tuple[int, int, int]]:
    return list(itertools.product(range(side), repeat=3))


def matching(side: int, axis: int, parity: int) -> tuple[tuple[int, int], ...]:
    verts = vertices(side)
    index = {vertex: number for number, vertex in enumerate(verts)}
    edges = []
    for vertex in verts:
        if vertex[axis] % 2 != parity:
            continue
        neighbor = list(vertex)
        neighbor[axis] = (neighbor[axis] + 1) % side
        edges.append(tuple(sorted((index[vertex], index[tuple(neighbor)]))))
    return tuple(sorted(edges))


def all_nearest_neighbor_edges(side: int) -> set[tuple[int, int]]:
    verts = vertices(side)
    index = {vertex: number for number, vertex in enumerate(verts)}
    edges = set()
    for vertex in verts:
        for axis in range(3):
            neighbor = list(vertex)
            neighbor[axis] = (neighbor[axis] + 1) % side
            edges.add(tuple(sorted((index[vertex], index[tuple(neighbor)]))))
    return edges


def orientation(order: tuple[tuple[int, int], ...]) -> tuple[int, int, int]:
    positions = {label: index for index, label in enumerate(order)}
    return tuple(1 if positions[(axis, 0)] < positions[(axis, 1)] else -1 for axis in range(3))


def iswap_representation(
    side: int,
    signed_order: tuple[tuple[int, tuple[int, int]], ...],
    layers: dict[tuple[int, int], tuple[tuple[int, int], ...]],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[tuple[int, int], ...]]:
    """Return |x> -> i^q(x)|P x> as (P, linear q, quadratic q/2)."""
    count = side**3
    variable_at_site = list(range(count))
    linear = [0] * count
    quadratic = set()
    for sign, label in signed_order:
        for left, right in layers[label]:
            first, second = variable_at_site[left], variable_at_site[right]
            linear[first] = (linear[first] + sign) % 4
            linear[second] = (linear[second] + sign) % 4
            edge = tuple(sorted((first, second)))
            # sign * (-2) is 2 modulo 4 for either iSWAP or its adjoint.
            if edge in quadratic:
                quadratic.remove(edge)
            else:
                quadratic.add(edge)
        for left, right in layers[label]:
            variable_at_site[left], variable_at_site[right] = variable_at_site[right], variable_at_site[left]
    permutation = [0] * count
    for site, original_variable in enumerate(variable_at_site):
        permutation[original_variable] = site
    return tuple(permutation), tuple(linear), tuple(sorted(quadratic))


def plus_representation(side, order, layers):
    return iswap_representation(side, tuple((1, label) for label in order), layers)


def cz_representation(
    side: int,
    order: tuple[tuple[int, int], ...],
    layers: dict[tuple[int, int], tuple[tuple[int, int], ...]],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[tuple[int, int], ...]]:
    """Return the exact CZ monomial representation accumulated layer by layer."""
    quadratic = set()
    for label in order:
        for edge in layers[label]:
            if edge in quadratic:
                quadratic.remove(edge)
            else:
                quadratic.add(edge)
    return tuple(range(side**3)), tuple(0 for _ in range(side**3)), tuple(sorted(quadratic))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations():
    """Signed coordinate permutations with determinant +1, as old-axis -> new-axis maps."""
    rotations = []
    for axis_permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            determinant = permutation_sign(axis_permutation)
            for sign in signs:
                determinant *= sign
            if determinant == 1:
                rotations.append((axis_permutation, signs))
    return tuple(rotations)


def rotation_parity_flips(
    axis_permutation: tuple[int, int, int], signs: tuple[int, int, int]
) -> tuple[int, int, int]:
    flips = [0, 0, 0]
    for old_axis, new_axis in enumerate(axis_permutation):
        flips[new_axis] = int(signs[old_axis] == -1)
    return tuple(flips)


def rotate_vertex(
    side: int,
    vertex: tuple[int, int, int],
    axis_permutation: tuple[int, int, int],
    signs: tuple[int, int, int],
) -> tuple[int, int, int]:
    result = [0, 0, 0]
    for old_axis, new_axis in enumerate(axis_permutation):
        result[new_axis] = (signs[old_axis] * vertex[old_axis]) % side
    return tuple(result)


def act_order(
    order: tuple[tuple[int, int], ...],
    axis_permutation: tuple[int, int, int],
    parity_flips: tuple[int, int, int],
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (axis_permutation[axis], parity ^ parity_flips[axis_permutation[axis]])
        for axis, parity in order
    )


def torus_distance(side: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(min((left[axis] - right[axis]) % side, (right[axis] - left[axis]) % side) for axis in range(3))


def main() -> int:
    labels = tuple((axis, parity) for axis in range(3) for parity in range(2))
    orders = tuple(itertools.permutations(labels))
    check("G01", len(orders) == 720, "the six matching labels have exactly 6!=720 schedules")

    side = 6
    layers = {label: matching(side, *label) for label in labels}
    check("G02", all(len(layer) == side**3 // 2 for layer in layers.values()), "each L=6 layer is a perfect matching")
    union = set().union(*map(set, layers.values()))
    check("G03", union == all_nearest_neighbor_edges(side) and sum(map(len, layers.values())) == len(union), "the six layers partition every undirected nearest-neighbor edge")

    orientations = Counter(orientation(order) for order in orders)
    check("G04", len(orientations) == 8 and set(orientations.values()) == {90}, "the 720 schedules split into eight axis-pair orientations with 90 interleavings each")

    representations = {order: plus_representation(side, order, layers) for order in orders}
    products = Counter(representations.values())
    check("I01", len(products) == 8 and set(products.values()) == {90}, "the full iSWAP qubit unitaries collapse exactly to eight products, each realized by 90 schedules")
    by_orientation = {}
    for order, representation in representations.items():
        by_orientation.setdefault(orientation(order), set()).add(representation)
    check("I02", all(len(values) == 1 for values in by_orientation.values()) and len({next(iter(values)) for values in by_orientation.values()}) == 8, "axis-pair orientation is a complete invariant of the iSWAP schedule product")

    cross_axis_commute = True
    same_axis_noncommute = True
    for first in labels:
        for second in labels:
            if first >= second:
                continue
            forward = plus_representation(side, (first, second), layers)
            reverse = plus_representation(side, (second, first), layers)
            if first[0] != second[0]:
                cross_axis_commute &= forward == reverse
            elif first[1] != second[1]:
                same_axis_noncommute &= forward != reverse
    check("I03", cross_axis_commute, "all complete iSWAP matching layers on distinct axes commute exactly")
    check("I04", same_axis_noncommute, "the two parity layers on every common axis fail to commute at L=6")

    rotations = proper_cubic_rotations()
    check("I05", len(rotations) == 24, "the signed coordinate action contains exactly the 24 proper cubic rotations")

    rotation_orbit = set()
    symmetry_orbit = set()
    reference = orders[0]
    for axis_permutation, signs in rotations:
        rotation_flips = rotation_parity_flips(axis_permutation, signs)
        rotation_orbit.add(representations[act_order(reference, axis_permutation, rotation_flips)])
        for translation_flips in itertools.product((0, 1), repeat=3):
            parity_flips = tuple(
                rotation_flips[axis] ^ translation_flips[axis]
                for axis in range(3)
            )
            symmetry_orbit.add(representations[act_order(reference, axis_permutation, parity_flips)])
    check("I06", rotation_orbit == set(products) and symmetry_orbit == set(products), "all 24 proper cubic rotations already make the eight iSWAP ticks one orbit; translations preserve that space-group orbit")

    translation_invariant = []
    for order, representation in representations.items():
        invariant = all(
            representations[act_order(order, (0, 1, 2), tuple(1 if axis == moved_axis else 0 for axis in range(3)))] == representation
            for moved_axis in range(3)
        )
        if invariant:
            translation_invariant.append(representation)
    check("I07", not translation_invariant, "no fixed iSWAP macro-tick is invariant under all one-site translations")

    cyclic_edges = set()
    cyclic_exactly_changes = True
    for order in orders:
        shifted = order[1:] + order[:1]
        cyclic_exactly_changes &= representations[shifted] != representations[order]
        cyclic_edges.add(frozenset((orientation(order), orientation(shifted))))
    reached = {next(iter(orientations))}
    while True:
        enlarged = reached | {
            point
            for edge in cyclic_edges
            if edge & reached
            for point in edge
        }
        if enlarged == reached:
            break
        reached = enlarged
    check("I08", cyclic_exactly_changes and reached == set(orientations), "one-step cyclic shifts change the exact iSWAP product and generate one finite-depth-conjugacy orbit of all eight products")

    verts = vertices(side)
    exact_radii = set()
    for representation in products:
        permutation = representation[0]
        exact_radii.add(max(torus_distance(side, verts[source], verts[target]) for source, target in enumerate(permutation)))
    check("I09", exact_radii == {6}, "every iSWAP macro-tick moves a computational-basis local Z support by exact graph distance six")

    identity_representation = (tuple(range(side**3)), tuple(0 for _ in range(side**3)), tuple())
    reversed_same_gate_inverse_ok = True
    gatewise_adjoint_inverse_ok = True
    for order in orders:
        same_gate = tuple((1, label) for label in order) + tuple((1, label) for label in reversed(order))
        reversed_same_gate_inverse_ok &= iswap_representation(side, same_gate, layers) == identity_representation
        signed = tuple((1, label) for label in order) + tuple((-1, label) for label in reversed(order))
        gatewise_adjoint_inverse_ok &= iswap_representation(side, signed, layers) == identity_representation
    check("I10", reversed_same_gate_inverse_ok, "reversing all six layers with the same iSWAP gate gives the exact inverse because the six global parity factors cancel")
    check("I11", gatewise_adjoint_inverse_ok, "reversing the schedule with gatewise iSWAP-dagger is the general adjoint construction and also gives the inverse")

    side_four = 4
    layers_four = {label: matching(side_four, *label) for label in labels}
    products_four = {plus_representation(side_four, order, layers_four) for order in orders}
    check("I12", len(products_four) == 1, "L=4 collapses all eight orientations and is an explicit finite-size artifact")

    cz_products = {cz_representation(side, order, layers) for order in orders}
    cz_quadratic = next(iter(cz_products))[2]
    check("Z01", len(cz_products) == 1, "all 720 CZ schedules are the same exact qubit unitary")
    omitted_layer = cz_representation(side, orders[0][:-1], layers)
    check("Z02", omitted_layer != next(iter(cz_products)), "omitting one CZ layer fails the all-edge product mutation control")

    verts_index = {vertex: index for index, vertex in enumerate(verts)}
    cz_translation_invariant = True
    for translation in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        moved = {
            tuple(sorted((
                verts_index[tuple((verts[left][axis] + translation[axis]) % side for axis in range(3))],
                verts_index[tuple((verts[right][axis] + translation[axis]) % side for axis in range(3))],
            )))
            for left, right in cz_quadratic
        }
        cz_translation_invariant &= moved == set(cz_quadratic)
    check("Z03", cz_translation_invariant, "the all-edge CZ circuit is invariant under unit translations")

    cz_rotation_invariant = True
    for axis_permutation, signs in rotations:
        moved = {
            tuple(sorted((
                verts_index[rotate_vertex(side, verts[left], axis_permutation, signs)],
                verts_index[rotate_vertex(side, verts[right], axis_permutation, signs)],
            )))
            for left, right in cz_quadratic
        }
        cz_rotation_invariant &= moved == set(cz_quadratic)
    check("Z04", cz_rotation_invariant, "the all-edge CZ circuit is invariant under all 24 proper cubic rotations")
    check("Z05", all(torus_distance(side, verts[left], verts[right]) == 1 for left, right in cz_quadratic), "CZ conjugates a local X only onto its radius-one neighbor star")

    path = Path("docs/CUBIC_MATCHING_PRODUCT_QUBIT_QCA_SCHEDULE_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("N01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    for index, marker in enumerate(("genuine one-qubit-site circuit", "does not select iSWAP or CZ", "does not classify arbitrary qubit QCAs", "does not establish that an axiom update is necessary"), 2):
        check(f"N{index:02d}", marker in text, f"source contains boundary marker: {marker}")

    print("BOUNDARY: the six-layer macro-tick, gate choice, even periodic torus, supplied quasi-local extension, and schedule semantics are conditional inputs.")
    print("BOUNDARY: CZ closes schedule dependence conditionally; iSWAP leaves eight symmetry-related ticks and no one-site-invariant member.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
