#!/usr/bin/env python3
"""Exact finite checks for cycle-space conditioning and cocircuit forcing.

The three fixtures are finite connected graphs.  A bit on each edge is
allowed exactly when every vertex has even incident parity.  All arithmetic
is over F2 or fractions; there is no floating-point or random evidence.
"""

from fractions import Fraction
from itertools import combinations


PASS = 0
FAIL = 0


def check(label, condition):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def bit_count(x):
    return x.bit_count()


def f2_rank(vectors):
    basis = []
    for value in vectors:
        for pivot in basis:
            value = min(value, value ^ pivot)
        if value:
            basis.append(value)
            basis.sort(reverse=True)
    return len(basis), basis


def f2_span(basis):
    values = {0}
    for vector in basis:
        values |= {value ^ vector for value in values}
    return values


def grid_graph(rows, cols, pendant=False):
    index = {(r, c): cols * r + c for r in range(rows) for c in range(cols)}
    edges = []
    for r in range(rows):
        for c in range(cols):
            if c + 1 < cols:
                edges.append((index[(r, c)], index[(r, c + 1)]))
            if r + 1 < rows:
                edges.append((index[(r, c)], index[(r + 1, c)]))
    faces = [
        (index[(r, c)], index[(r, c + 1)], index[(r + 1, c + 1)], index[(r + 1, c)])
        for r in range(rows - 1)
        for c in range(cols - 1)
    ]
    vertices = rows * cols
    if pendant:
        edges.append((0, vertices))
        vertices += 1
    return vertices, sorted(edges), faces


def cube_graph():
    edges = sorted((s, s ^ bit) for s in range(8) for bit in (4, 2, 1) if s < (s ^ bit))
    faces = []
    for fixed_bit in (4, 2, 1):
        other = [bit for bit in (4, 2, 1) if bit != fixed_bit]
        for fixed_value in (0, fixed_bit):
            faces.append(
                (
                    fixed_value,
                    fixed_value | other[1],
                    fixed_value | other[0] | other[1],
                    fixed_value | other[0],
                )
            )
    return 8, edges, faces


def edge_index(edges):
    result = {}
    for q, (u, v) in enumerate(edges):
        result[(u, v)] = q
        result[(v, u)] = q
    return result


def vertex_stars(vertices, edges):
    stars = [0] * vertices
    for q, (u, v) in enumerate(edges):
        stars[u] |= 1 << q
        stars[v] |= 1 << q
    return stars


def face_masks(edges, faces):
    lookup = edge_index(edges)
    masks = []
    for face in faces:
        mask = 0
        for a, b in zip(face, face[1:] + face[:1]):
            mask |= 1 << lookup[(a, b)]
        masks.append(mask)
    return masks


def cycle_space(vertices, edges):
    stars = vertex_stars(vertices, edges)
    return {
        value
        for value in range(1 << len(edges))
        if all(bit_count(value & star) % 2 == 0 for star in stars)
    }


def cut_space(vertices, edges):
    cuts = set()
    for vertex_subset in range(1 << vertices):
        mask = 0
        for q, (u, v) in enumerate(edges):
            if ((vertex_subset >> u) & 1) != ((vertex_subset >> v) & 1):
                mask |= 1 << q
        cuts.add(mask)
    return cuts


def cocircuits(cuts):
    nonzero = sorted(cuts - {0}, key=lambda value: (bit_count(value), value))
    return [
        value
        for value in nonzero
        if not any(other != value and (other & value) == other for other in nonzero)
    ]


def odds(states, coordinate):
    return Fraction(sum((state >> coordinate) & 1 for state in states), len(states))


def condition(states, observations):
    return {
        state
        for state in states
        if all(((state >> coordinate) & 1) == value for coordinate, value in observations)
    }


def brute_forced(cycles, target, observed_mask):
    return not any(((difference >> target) & 1) and not (difference & observed_mask) for difference in cycles)


def cocircuit_forced(cocircuit_list, target, observed_mask):
    target_bit = 1 << target
    return any(
        (word & target_bit) and ((word & ~target_bit) & observed_mask) == (word & ~target_bit)
        for word in cocircuit_list
    )


def fixture_inventory():
    cube = cube_graph()
    grid = grid_graph(3, 3)
    pendant = grid_graph(3, 3, pendant=True)
    return {"cube": cube, "grid3x3": grid, "grid3x3+pendant": pendant}


def main():
    fixtures = fixture_inventory()
    expected = {
        "cube": (5, 32, 5, 63),
        "grid3x3": (4, 16, 4, 53),
        "grid3x3+pendant": (4, 16, 4, 54),
    }
    expected_marginal_profiles = {
        "cube": {Fraction(1, 2)},
        "grid3x3": {Fraction(1, 2)},
        "grid3x3+pendant": {Fraction(0), Fraction(1, 2)},
    }
    data = {}

    for name, (vertices, edges, faces) in fixtures.items():
        cycles = cycle_space(vertices, edges)
        cuts = cut_space(vertices, edges)
        minimal_cuts = cocircuits(cuts)
        masks = face_masks(edges, faces)
        cycle_dimension, cycle_basis = f2_rank(cycles)
        face_rank, face_basis = f2_rank(masks)
        data[name] = (vertices, edges, cycles, cuts, minimal_cuts, masks)
        want_cycle_dim, want_support, want_face_rank, want_cocircuits = expected[name]

        check(
            f"A/{name} [exact] connected cycle space has dimension E-V+1={want_cycle_dim} and support {want_support}",
            cycle_dimension == len(edges) - vertices + 1 == want_cycle_dim
            and len(cycles) == want_support,
        )
        check(
            f"B/{name} [exact] face boundaries have rank {want_face_rank} and span the full cycle space",
            face_rank == want_face_rank and f2_span(face_basis) == f2_span(cycle_basis) == cycles,
        )
        check(
            f"C/{name} [exact] cut space has dimension V-1 and {want_cocircuits} inclusion-minimal nonzero cuts",
            f2_rank(cuts)[0] == vertices - 1
            and len(cuts) == 1 << (vertices - 1)
            and len(minimal_cuts) == want_cocircuits,
        )
        marginals = {odds(cycles, q) for q in range(len(edges))}
        check(
            f"D/{name} [exact] the complete coordinate-marginal profile is {sorted(expected_marginal_profiles[name])}",
            marginals == expected_marginal_profiles[name],
        )

    vertices, edges, cycles, cuts, minimal_cuts, masks = data["cube"]
    all_single_half = all(
        odds(condition(cycles, [(q, value)]), r) == Fraction(1, 2)
        for q in range(len(edges))
        for value in (0, 1)
        for r in range(len(edges))
        if r != q
    )
    check("E/cube [exact] one observed edge leaves every other edge marginal at 1/2", all_single_half)

    two_observation_tally = {}
    for q1, q2 in combinations(range(len(data["cube"][1])), 2):
        shared_vertex = bool(set(edges[q1]) & set(edges[q2]))
        for b1 in (0, 1):
            for b2 in (0, 1):
                remaining = condition(cycles, [(q1, b1), (q2, b2)])
                changed = sum(
                    odds(remaining, r) != Fraction(1, 2)
                    for r in range(len(edges))
                    if r not in (q1, q2)
                )
                key = (int(shared_vertex), changed)
                two_observation_tally[key] = two_observation_tally.get(key, 0) + 1
    check(
        "F/cube [exact] full two-observation census is 96 adjacent cases forcing one edge and 168 disjoint cases forcing none",
        two_observation_tally == {(1, 1): 96, (0, 0): 168},
    )

    total_masks = 0
    total_mismatches = 0
    for name, (_, edges, cycles, _, minimal_cuts, _) in data.items():
        full_mask = (1 << len(edges)) - 1
        for target in range(len(edges)):
            target_bit = 1 << target
            other_bits = full_mask ^ target_bit
            subset = other_bits
            while True:
                total_masks += 1
                if brute_forced(cycles, target, subset) != cocircuit_forced(minimal_cuts, target, subset):
                    total_mismatches += 1
                if subset == 0:
                    break
                subset = (subset - 1) & other_bits
    check(
        f"G/all [exact] all {total_masks} target/observed-set masks satisfy forcing iff a cocircuit through the target is contained",
        total_masks == 102400 and total_mismatches == 0,
    )

    lookup = edge_index(data["cube"][1])
    target = lookup[(0, 4)]
    remote = [lookup[(1, 5)], lookup[(2, 6)], lookup[(3, 7)]]
    nonlocal_ok = True
    for values in range(8):
        observations = [(q, (values >> i) & 1) for i, q in enumerate(remote)]
        remaining = condition(data["cube"][2], observations)
        nonlocal_ok &= len(remaining) == 4
        nonlocal_ok &= len({(state >> target) & 1 for state in remaining}) == 1
    check(
        "H/cube [exact] the three disjoint observed edges (1,5),(2,6),(3,7) force (0,4) in all eight value assignments",
        nonlocal_ok,
    )

    order_counts = {}
    order_ok = True
    for name, (_, edges, cycles, _, _, _) in data.items():
        count = 0
        for q1, q2 in combinations(range(len(edges)), 2):
            for b1 in (0, 1):
                for b2 in (0, 1):
                    first = condition(condition(cycles, [(q1, b1)]), [(q2, b2)])
                    second = condition(condition(cycles, [(q2, b2)]), [(q1, b1)])
                    order_ok &= first == second
                    order_ok &= Fraction(len(first), len(cycles)) == Fraction(len(second), len(cycles))
                    count += 1
        order_counts[name] = count
    check(
        "I/all [exact] coordinate-projector conditioning is order-independent for every ordered value pair",
        order_ok and order_counts == {"cube": 264, "grid3x3": 264, "grid3x3+pendant": 312},
    )

    pendant_edges = data["grid3x3+pendant"][1]
    pendant_cycles = data["grid3x3+pendant"][2]
    bridge = edge_index(pendant_edges)[(0, 9)]
    check(
        "J/pendant [exact] the bridge edge is fixed to zero while all other edge marginals are 1/2",
        odds(pendant_cycles, bridge) == 0
        and all(odds(pendant_cycles, q) == Fraction(1, 2) for q in range(len(pendant_edges)) if q != bridge),
    )

    cube_faces_mutated = list(data["cube"][5])
    cube_faces_mutated[0] ^= 1
    rank_mutation_caught = f2_span(f2_rank(cube_faces_mutated)[1]) != data["cube"][2]
    support_mutation_caught = set(sorted(data["cube"][2])[1:]) != data["cube"][2]
    marginal_mutation_caught = odds(data["cube"][2], 0) != Fraction(1, 3)
    grid_profile_mutation_caught = (
        {odds(data["grid3x3"][2], q) for q in range(len(data["grid3x3"][1]))}
        | {Fraction(0)}
    ) != expected_marginal_profiles["grid3x3"]

    q = 0
    q_cocircuits = [word for word in data["cube"][4] if word & (1 << q)]
    omitted = q_cocircuits[0]
    observed = omitted & ~(1 << q)
    cocircuit_mutation_caught = brute_forced(data["cube"][2], q, observed) and not cocircuit_forced(
        [word for word in data["cube"][4] if word != omitted], q, observed
    )

    order_mutation_caught = False
    for q1, q2 in combinations(range(len(data["cube"][1])), 2):
        exact = condition(data["cube"][2], [(q1, 0), (q2, 0)])
        last_only = condition(data["cube"][2], [(q2, 0)])
        if exact != last_only:
            order_mutation_caught = True
            break

    stars = vertex_stars(data["cube"][0], data["cube"][1])
    local_only = [star for star in stars if star]
    local_mutation_caught = brute_forced(data["cube"][2], target, sum(1 << q for q in remote)) and not cocircuit_forced(
        local_only, target, sum(1 << q for q in remote)
    )
    check(
        "K/mutations [exact] rank, support, marginal value/profile, cocircuit, order, and local-only forcing mutants are all rejected",
        all(
            (
                rank_mutation_caught,
                support_mutation_caught,
                marginal_mutation_caught,
                grid_profile_mutation_caught,
                cocircuit_mutation_caught,
                order_mutation_caught,
                local_mutation_caught,
            )
        ),
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
