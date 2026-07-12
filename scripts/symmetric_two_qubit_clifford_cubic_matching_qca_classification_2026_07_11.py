#!/usr/bin/env python3
"""Exhaust symmetric two-qubit Clifford gates in the six-matching QCA grammar."""

import itertools
from collections import Counter, deque
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0


def check(name, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = (I, X, Y, Z)
PAULI2 = tuple(np.kron(left, right) for left in PAULI for right in PAULI)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.diag([1, 1j])
CNOT = np.array(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
    dtype=complex,
)
SWAP = np.array(
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
    dtype=complex,
)


def clifford_map(unitary):
    """Signed permutation of the 16 Hermitian two-qubit Paulis."""
    result = []
    for pauli in PAULI2:
        image = unitary @ pauli @ unitary.conj().T
        coefficients = [np.trace(candidate.conj().T @ image) / 4 for candidate in PAULI2]
        label = int(np.argmax(np.abs(coefficients)))
        coefficient = coefficients[label]
        assert abs(abs(coefficient) - 1) < 1e-9 and abs(coefficient.imag) < 1e-9
        result.append((label, int(coefficient.real < 0)))
    return tuple(result)


IDENTITY_MAP = tuple((label, 0) for label in range(16))


def compose(outer, inner):
    return tuple((outer[label][0], sign ^ outer[label][1]) for label, sign in inner)


def generated_group(generators):
    group = {IDENTITY_MAP}
    queue = deque([IDENTITY_MAP])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(generator, current)
            if candidate not in group:
                group.add(candidate)
                queue.append(candidate)
    return group


def inverse_map(element, finite_group):
    return next(candidate for candidate in finite_group if compose(element, candidate) == IDENTITY_MAP)


LABELS = tuple((axis, parity) for axis in range(3) for parity in range(2))
ORDERS = tuple(itertools.permutations(LABELS))
ORIGINS = tuple(itertools.product((0, 1), repeat=3))


def orientation(order):
    positions = {label: index for index, label in enumerate(order)}
    return tuple(1 if positions[(axis, 0)] < positions[(axis, 1)] else -1 for axis in range(3))


def apply_layer(state, axis, parity, gate):
    """Apply one infinite period-two matching layer to a finite Pauli string."""
    sign, support_items = state
    support = dict(support_items)
    edges = set()
    for site in support:
        first = list(site)
        if site[axis] % 2 != parity:
            first[axis] -= 1
        first = tuple(first)
        second = list(first)
        second[axis] += 1
        edges.add((first, tuple(second)))
    for first, second in edges:
        left = support.get(first, 0)
        right = support.get(second, 0)
        output, local_sign = gate[4 * left + right]
        sign ^= local_sign
        left_out, right_out = divmod(output, 4)
        if left_out:
            support[first] = left_out
        else:
            support.pop(first, None)
        if right_out:
            support[second] = right_out
        else:
            support.pop(second, None)
    return sign, tuple(sorted(support.items()))


def automorphism_representation(order, gate):
    """Images of X and Z at all eight parity origins determine the rule."""
    images = []
    for origin in ORIGINS:
        for generator in (1, 3):
            state = (0, ((origin, generator),))
            for axis, parity in order:
                state = apply_layer(state, axis, parity, gate)
            images.append(state)
    return tuple(images)


def forward_then_inverse_is_identity(order, gate, inverse_gate):
    for origin in ORIGINS:
        for generator in (1, 3):
            initial = (0, ((origin, generator),))
            state = initial
            for axis, parity in order:
                state = apply_layer(state, axis, parity, gate)
            for axis, parity in reversed(order):
                state = apply_layer(state, axis, parity, inverse_gate)
            if state != initial:
                return False
    return True


def graph_radius(representation):
    radius = 0
    for index, (_, support) in enumerate(representation):
        origin = ORIGINS[index // 2]
        for site, _ in support:
            radius = max(radius, sum(abs(site[axis] - origin[axis]) for axis in range(3)))
    return radius


def linfinity_radius(representation):
    radius = 0
    for index, (_, support) in enumerate(representation):
        origin = ORIGINS[index // 2]
        for site, _ in support:
            radius = max(radius, max(abs(site[axis] - origin[axis]) for axis in range(3)))
    return radius


def act_order(order, axis_permutation, parity_flips):
    return tuple(
        (axis_permutation[axis], parity ^ parity_flips[axis_permutation[axis]])
        for axis, parity in order
    )


def permutation_sign(permutation):
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_rotations():
    actions = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * int(np.prod(signs)) != 1:
                continue
            flips = [0, 0, 0]
            for old_axis, new_axis in enumerate(permutation):
                flips[new_axis] = int(signs[old_axis] < 0)
            actions.append((permutation, tuple(flips)))
    return tuple(actions)


ROTATIONS = proper_rotations()


def component_count(vertices, edges):
    adjacency = {vertex: set() for vertex in vertices}
    for edge in edges:
        for vertex in edge:
            adjacency[vertex].update(set(edge) - {vertex})
    remaining = set(vertices)
    count = 0
    while remaining:
        count += 1
        stack = [remaining.pop()]
        while stack:
            reached = adjacency[stack.pop()] & remaining
            remaining.difference_update(reached)
            stack.extend(reached)
    return count


def support_class(gate):
    def occupied_sites(label):
        left, right = divmod(label, 4)
        return bool(left), bool(right)

    images = [occupied_sites(gate[index][0]) for index in (4, 12, 1, 3)]
    if images[:2] == [(True, False)] * 2 and images[2:] == [(False, True)] * 2:
        return "product"
    if images[:2] == [(False, True)] * 2 and images[2:] == [(True, False)] * 2:
        return "swap_product"
    return "entangling"


def embedded_map(gate, first, second):
    """Full signed-Pauli map on three sites for a gate on one edge."""
    result = []
    for label in range(64):
        digits = [(label // (4 ** (2 - site))) % 4 for site in range(3)]
        pair_output, sign = gate[4 * digits[first] + digits[second]]
        digits[first], digits[second] = divmod(pair_output, 4)
        output = sum(digits[site] * 4 ** (2 - site) for site in range(3))
        result.append((output, sign))
    return tuple(result)


def main():
    generators = (
        clifford_map(np.kron(H, I)),
        clifford_map(np.kron(S, I)),
        clifford_map(np.kron(I, H)),
        clifford_map(np.kron(I, S)),
        clifford_map(CNOT),
    )
    clifford_group = generated_group(generators)
    check("G01", len(clifford_group) == 11520, "H, S, and CNOT generate all 11,520 projective two-qubit Clifford automorphisms")

    swap = clifford_map(SWAP)
    symmetric_gates = {
        gate for gate in clifford_group if compose(gate, swap) == compose(swap, gate)
    }
    check("G02", len(symmetric_gates) == 192, "exactly 192 projective Clifford automorphisms commute with endpoint SWAP")

    onsite_group = generated_group(
        (clifford_map(np.kron(H, H)), clifford_map(np.kron(S, S)))
    )
    onsite_inverse = {gate: inverse_map(gate, onsite_group) for gate in onsite_group}
    check("G03", len(onsite_group) == 24, "uniform onsite Clifford basis changes form the 24-element one-qubit projective Clifford group")

    remaining = set(symmetric_gates)
    conjugacy_orbits = []
    while remaining:
        representative = min(remaining)
        orbit = {
            compose(compose(frame, representative), onsite_inverse[frame])
            for frame in onsite_group
        }
        conjugacy_orbits.append(orbit)
        remaining.difference_update(orbit)
    orbit_sizes = Counter(map(len, conjugacy_orbits))
    check("G04", len(conjugacy_orbits) == 26 and orbit_sizes == Counter({6: 10, 3: 6, 12: 4, 1: 2, 8: 2, 24: 2}), "the 192 gates form 26 uniform-onsite-Clifford conjugacy classes")

    rows = []
    for orbit in conjugacy_orbits:
        gate = min(orbit)
        inverse_gate = inverse_map(gate, clifford_group)
        by_order = {order: automorphism_representation(order, gate) for order in ORDERS}
        product_counts = Counter(by_order.values())
        products = set(product_counts)

        by_orientation = {}
        for order, product in by_order.items():
            by_orientation.setdefault(orientation(order), set()).add(product)
        orientation_complete = (
            len(products) == 8
            and all(len(values) == 1 for values in by_orientation.values())
            and len({next(iter(values)) for values in by_orientation.values()}) == 8
        )

        spatial_edges = set()
        cyclic_edges = set()
        invariant_orders = 0
        translation_invariant_orders = 0
        rotation_invariant_orders = 0
        for order, product in by_order.items():
            cyclic_edges.add(frozenset((product, by_order[order[1:] + order[:1]])))
            rotation_targets = []
            for permutation, flips in ROTATIONS:
                target = by_order[act_order(order, permutation, flips)]
                spatial_edges.add(frozenset((product, target)))
                rotation_targets.append(target)
            translation_targets = []
            for axis in range(3):
                flips = tuple(int(index == axis) for index in range(3))
                target = by_order[act_order(order, (0, 1, 2), flips)]
                spatial_edges.add(frozenset((product, target)))
                translation_targets.append(target)
            rotation_invariant_orders += int(all(target == product for target in rotation_targets))
            translation_invariant_orders += int(all(target == product for target in translation_targets))
            invariant_orders += int(
                all(target == product for target in rotation_targets + translation_targets)
            )

        inverse_radii = set()
        inverse_linf = set()
        inverse_ok = True
        for order in ORDERS:
            inverse_representation = automorphism_representation(tuple(reversed(order)), inverse_gate)
            inverse_radii.add(graph_radius(inverse_representation))
            inverse_linf.add(linfinity_radius(inverse_representation))
            # Applying the forward and inverse sparse rules directly is checked
            # at the local gate level by exact tableau inversion above.
            inverse_ok &= (
                compose(gate, inverse_gate) == IDENTITY_MAP
                and forward_then_inverse_is_identity(order, gate, inverse_gate)
            )

        edge_01 = embedded_map(gate, 0, 1)
        edge_12 = embedded_map(gate, 1, 2)
        overlap_commutes = compose(edge_01, edge_12) == compose(edge_12, edge_01)

        rows.append(
            {
                "weight": len(orbit),
                "support_class": support_class(gate),
                "products": len(products),
                "multiplicities": set(product_counts.values()),
                "orientation_complete": orientation_complete,
                "spatial_components": component_count(products, spatial_edges),
                "cyclic_components": component_count(products, cyclic_edges),
                "invariant_orders": invariant_orders,
                "translation_invariant_orders": translation_invariant_orders,
                "rotation_invariant_orders": rotation_invariant_orders,
                "radii": {graph_radius(product) for product in products},
                "linf": {linfinity_radius(product) for product in products},
                "inverse_radii": inverse_radii,
                "inverse_linf": inverse_linf,
                "inverse_ok": inverse_ok,
                "overlap_commutes": overlap_commutes,
            }
        )

    representative_distribution = Counter(row["products"] for row in rows)
    weighted_distribution = Counter()
    for row in rows:
        weighted_distribution[row["products"]] += row["weight"]
    check("C01", representative_distribution == Counter({1: 10, 8: 10, 720: 6}), "the 26 basis classes split as 10 unique-product, 10 eight-product, and 6 fully order-faithful classes")
    check("C02", weighted_distribution == Counter({1: 48, 8: 48, 720: 96}), "the 192 gates split as 48/48/96 across 1, 8, and 720 exact schedule products")

    unique_rows = [row for row in rows if row["products"] == 1]
    check("C03", sum(row["weight"] for row in unique_rows if row["support_class"] == "product" and row["radii"] == {0}) == 24, "24 product gates give schedule-independent onsite automorphisms of graph radius zero")
    check("C04", sum(row["weight"] for row in unique_rows if row["support_class"] == "entangling" and row["radii"] == {1}) == 24, "24 entangling gates give schedule-independent graph-radius-one automorphisms")
    check("C05", all(row["translation_invariant_orders"] == 720 and row["rotation_invariant_orders"] == 720 for row in unique_rows), "every schedule-independent product is separately translation- and proper-cubic-invariant")

    eight_rows = [row for row in rows if row["products"] == 8]
    check("C06", sum(row["weight"] for row in eight_rows) == 48 and sum(row["weight"] for row in eight_rows if row["support_class"] == "swap_product") == 24 and sum(row["weight"] for row in eight_rows if row["support_class"] == "entangling") == 24 and all(row["multiplicities"] == {90} and row["orientation_complete"] for row in eight_rows), "48 gates, split 24 SWAP-product/24 entangling, give the eight-by-90 axis-orientation quotient")
    check("C07", all(row["spatial_components"] == 1 and row["cyclic_components"] == 1 and row["translation_invariant_orders"] == 0 and row["rotation_invariant_orders"] == 0 for row in eight_rows), "every eight-product class is one spatial and cyclic orbit with no member fixed by the full translation or proper-cubic group")
    check("C08", all(row["radii"] == {6} and row["linf"] == {2} for row in eight_rows), "all eight-product automorphisms have exact graph radius six and l-infinity radius two")

    faithful_rows = [row for row in rows if row["products"] == 720]
    check("C09", sum(row["weight"] for row in faithful_rows) == 96 and all(row["support_class"] == "entangling" and row["multiplicities"] == {1} for row in faithful_rows), "96 entangling gates make all 720 schedules distinct")
    check("C10", all(row["spatial_components"] == 15 and row["cyclic_components"] == 120 and row["translation_invariant_orders"] == 0 and row["rotation_invariant_orders"] == 0 for row in faithful_rows), "fully order-faithful classes have 15 spatial and 120 cyclic orbits and no member fixed by the full translation or proper-cubic group")
    check("C11", all(row["radii"] == {6} and row["linf"] == {2} for row in faithful_rows), "all fully order-faithful automorphisms have exact graph radius six and l-infinity radius two")
    check("C12", all(row["inverse_ok"] and row["inverse_radii"] == row["radii"] and row["inverse_linf"] == row["linf"] for row in rows), "reversed schedules with the inverse gate give exact inverse tableaus with matching forward/inverse radii")
    check("C13", sum(row["weight"] for row in rows if row["overlap_commutes"]) == 36 and all(row["products"] == 1 for row in rows if row["overlap_commutes"]), "local overlap commutation is sufficient and holds for 36 schedule-independent gates")
    check("C14", sum(row["weight"] for row in unique_rows if not row["overlap_commutes"]) == 12, "12 further gates are schedule-independent only after complete perfect-matching layers are assembled")

    path = Path("docs/SYMMETRIC_TWO_QUBIT_CLIFFORD_CUBIC_MATCHING_QCA_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("N01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    normalized_text = " ".join(text.split())
    for index, marker in enumerate((
        "Clifford-group automorphism, not the static Clifford algebra",
        "does not classify arbitrary qubit QCAs",
        "does not establish a common Hamiltonian",
        "does not establish that an axiom update is necessary",
    ), 2):
        check(f"N{index:02d}", marker in normalized_text, f"source contains boundary marker: {marker}")

    print("BOUNDARY: tensor carrier, symmetric Clifford gate class, parity matchings, exactly-once grammar, and macro-tick are supplied.")
    print("BOUNDARY: the exhaustive result is projective-automorphism level; global unitary phase and physical process selection remain open.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
