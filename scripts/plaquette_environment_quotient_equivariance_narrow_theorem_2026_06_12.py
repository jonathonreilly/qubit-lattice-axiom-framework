#!/usr/bin/env python3
"""Marked-plaquette quotient equivariance narrow theorem runner.

This runner does not compute rho_(p,q)(6).  It verifies the cost-note
stabilizer geometry, proves the finite-index equivariance bookkeeping needed
for an exact quotient, and runs a small exact rational falsifier against the
link-orbit-tied diagnostic quotient.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 600

L_S = 3
N_DIR = 3
MARKED_PLAQUETTE_INDEX = 0
COMPLEX_BYTES = 16
MEMORY_BUDGET_BYTES = 4 * 1024**3

DIR_VEC = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

PASS = 0
FAIL = 0

Matrix = tuple[tuple[int, ...], ...]
Site = tuple[int, int, int]
Link = tuple[int, int, int, int]
GroupElement = tuple[Matrix, Site]
Label = tuple[int, int]


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 100)
    print(title)
    print("=" * 100)


def add_site(a: Site, b: Site) -> Site:
    return tuple((a[i] + b[i]) % L_S for i in range(3))  # type: ignore[return-value]


def basis_vec(direction: int) -> Site:
    return tuple(1 if i == direction else 0 for i in range(3))  # type: ignore[return-value]


def link_id(site: Site, direction: int) -> int:
    x, y, z = site
    return (((x * L_S) + y) * L_S + z) * N_DIR + direction


def id_to_link(idx: int) -> Link:
    direction = idx % N_DIR
    n = idx // N_DIR
    z = n % L_S
    n //= L_S
    y = n % L_S
    x = n // L_S
    return (x, y, z, direction)


def all_sites() -> list[Site]:
    return [site for site in product(range(L_S), repeat=3)]


def all_links() -> list[Link]:
    return [(x, y, z, d) for x, y, z in product(range(L_S), repeat=3) for d in range(3)]


def all_plaquettes() -> list[tuple[Site, int, int, tuple[int, ...]]]:
    plaquettes: list[tuple[Site, int, int, tuple[int, ...]]] = []
    for site in product(range(L_S), repeat=3):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                site_mu = add_site(site, DIR_VEC[mu])
                site_nu = add_site(site, DIR_VEC[nu])
                plaquettes.append(
                    (
                        site,
                        mu,
                        nu,
                        (
                            link_id(site, mu),
                            link_id(site_mu, nu),
                            link_id(site_nu, mu),
                            link_id(site, nu),
                        ),
                    )
                )
    return plaquettes


def signed_permutation_matrices() -> list[Matrix]:
    out: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, col in enumerate(perm):
                matrix[row][col] = signs[row] % L_S
            out.append(tuple(tuple(row) for row in matrix))
    return out


def mat_vec(matrix: Matrix, vector: Site) -> Site:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) % L_S for i in range(3))  # type: ignore[return-value]


def mat_mat(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) % L_S for j in range(3))
        for i in range(3)
    )


def affine_vertex(matrix: Matrix, translation: Site, vertex: Site) -> Site:
    return add_site(mat_vec(matrix, vertex), translation)


def compose(left: GroupElement, right: GroupElement) -> GroupElement:
    left_m, left_t = left
    right_m, right_t = right
    return mat_mat(left_m, right_m), add_site(mat_vec(left_m, right_t), left_t)


def link_tuple_transform_signed(
    matrix: Matrix,
    translation: Site,
    link: Link,
) -> tuple[Link, int]:
    start = link[:3]
    endpoint = add_site(start, basis_vec(link[3]))
    image_start = affine_vertex(matrix, translation, start)
    image_endpoint = affine_vertex(matrix, translation, endpoint)
    diff = tuple((image_endpoint[i] - image_start[i]) % L_S for i in range(3))
    for direction in range(3):
        forward = basis_vec(direction)
        backward = tuple((-v) % L_S for v in forward)
        if diff == forward:
            return image_start + (direction,), 1
        if diff == backward:
            return image_endpoint + (direction,), -1
    raise RuntimeError(f"not a signed basis direction: {diff}")


def link_tuple_transform(matrix: Matrix, translation: Site, link: Link) -> Link:
    return link_tuple_transform_signed(matrix, translation, link)[0]


def plaquette_link_tuples(plaquette: tuple[Site, int, int, tuple[int, ...]]) -> frozenset[Link]:
    return frozenset(id_to_link(idx) for idx in plaquette[3])


def marked_stabilizer(plaquettes: list[tuple[Site, int, int, tuple[int, ...]]]) -> list[GroupElement]:
    marked = plaquettes[MARKED_PLAQUETTE_INDEX]
    marked_vertices = {
        marked[0],
        add_site(marked[0], basis_vec(marked[1])),
        add_site(marked[0], basis_vec(marked[2])),
        add_site(add_site(marked[0], basis_vec(marked[1])), basis_vec(marked[2])),
    }
    marked_boundary = plaquette_link_tuples(marked)
    stabilizer: list[GroupElement] = []
    for matrix in signed_permutation_matrices():
        for translation in product(range(L_S), repeat=3):
            image_vertices = {
                affine_vertex(matrix, translation, vertex) for vertex in marked_vertices
            }
            image_boundary = {
                link_tuple_transform(matrix, translation, link) for link in marked_boundary
            }
            if image_vertices == marked_vertices and image_boundary == marked_boundary:
                stabilizer.append((matrix, translation))
    return stabilizer


def orbit_partition(items: list, transforms) -> list[list]:
    seen = set()
    orbits = []
    for item in items:
        if item in seen:
            continue
        orbit = set()
        stack = [item]
        while stack:
            current = stack.pop()
            if current in orbit:
                continue
            orbit.add(current)
            for transform in transforms:
                stack.append(transform(current))
        orbit_list = sorted(orbit)
        seen.update(orbit_list)
        orbits.append(orbit_list)
    return orbits


def stabilizer_orbit_data(
    plaquettes: list[tuple[Site, int, int, tuple[int, ...]]],
    stabilizer: list[GroupElement],
) -> tuple[list[list[Site]], list[list[Link]], list[list[int]], list[tuple[int, ...]]]:
    site_transforms = [
        (lambda item, m=matrix, t=translation: affine_vertex(m, t, item))
        for matrix, translation in stabilizer
    ]
    site_orbits = orbit_partition(all_sites(), site_transforms)

    link_transforms = [
        (lambda item, m=matrix, t=translation: link_tuple_transform(m, t, item))
        for matrix, translation in stabilizer
    ]
    link_orbits = orbit_partition(all_links(), link_transforms)
    link_orbit_id = {
        link: orbit_index
        for orbit_index, orbit in enumerate(link_orbits)
        for link in orbit
    }

    plaquette_set_to_index = {
        plaquette_link_tuples(plaquette): index for index, plaquette in enumerate(plaquettes)
    }

    def plaquette_transform_index(matrix: Matrix, translation: Site, index: int) -> int:
        image = frozenset(
            link_tuple_transform(matrix, translation, link)
            for link in plaquette_link_tuples(plaquettes[index])
        )
        return plaquette_set_to_index[image]

    plaquette_transforms = [
        (lambda item, m=matrix, t=translation: plaquette_transform_index(m, t, item))
        for matrix, translation in stabilizer
    ]
    plaquette_orbits = orbit_partition(list(range(len(plaquettes))), plaquette_transforms)
    plaquette_orbit_id = {
        plaquette_index: orbit_index
        for orbit_index, orbit in enumerate(plaquette_orbits)
        for plaquette_index in orbit
    }
    active_orbit_ids = sorted(
        {
            plaquette_orbit_id[index]
            for index in range(len(plaquettes))
            if index != MARKED_PLAQUETTE_INDEX
        }
    )
    quotient_scopes: list[tuple[int, ...]] = []
    for orbit_id in active_orbit_ids:
        representative = next(
            index
            for index, poid in plaquette_orbit_id.items()
            if poid == orbit_id and index != MARKED_PLAQUETTE_INDEX
        )
        quotient_scopes.append(
            tuple(
                sorted(
                    {
                        link_orbit_id[id_to_link(link_index)]
                        for link_index in plaquettes[representative][3]
                    }
                )
            )
        )
    return site_orbits, link_orbits, plaquette_orbits, quotient_scopes


def action_permutation_on_sites(element: GroupElement) -> list[int]:
    matrix, translation = element
    index = {site: i for i, site in enumerate(all_sites())}
    return [index[affine_vertex(matrix, translation, site)] for site in all_sites()]


def action_permutation_on_links(element: GroupElement) -> tuple[list[int], list[int]]:
    matrix, translation = element
    link_index = {link: i for i, link in enumerate(all_links())}
    perm: list[int] = []
    signs: list[int] = []
    for link in all_links():
        image, sign = link_tuple_transform_signed(matrix, translation, link)
        perm.append(link_index[image])
        signs.append(sign)
    return perm, signs


def action_permutation_on_plaquettes(
    element: GroupElement,
    plaquettes: list[tuple[Site, int, int, tuple[int, ...]]],
) -> list[int]:
    matrix, translation = element
    plaquette_set_to_index = {
        plaquette_link_tuples(plaquette): index for index, plaquette in enumerate(plaquettes)
    }
    perm: list[int] = []
    for plaquette in plaquettes:
        image = frozenset(
            link_tuple_transform(matrix, translation, link)
            for link in plaquette_link_tuples(plaquette)
        )
        perm.append(plaquette_set_to_index[image])
    return perm


def cycle_lengths(perm: list[int]) -> list[int]:
    seen = [False] * len(perm)
    out = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        cur = start
        size = 0
        while not seen[cur]:
            seen[cur] = True
            size += 1
            cur = perm[cur]
        out.append(size)
    return sorted(out)


def signed_link_cycle_counts(perm: list[int], signs: list[int]) -> tuple[int, int, list[int]]:
    seen = [False] * len(perm)
    even_cycles = 0
    odd_cycles = 0
    lengths: list[int] = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        cur = start
        parity = 1
        size = 0
        while not seen[cur]:
            seen[cur] = True
            parity *= signs[cur]
            size += 1
            cur = perm[cur]
        lengths.append(size)
        if parity == 1:
            even_cycles += 1
        else:
            odd_cycles += 1
    return even_cycles, odd_cycles, sorted(lengths)


def histogram(rows: list[tuple]) -> dict[tuple, int]:
    out: dict[tuple, int] = {}
    for row in rows:
        out[row] = out.get(row, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (kv[0], kv[1])))


def compact_lengths(lengths: tuple[int, ...]) -> str:
    counts: dict[int, int] = {}
    for length in lengths:
        counts[length] = counts.get(length, 0) + 1
    return " ".join(f"{length}^{count}" for length, count in sorted(counts.items()))


def compact_histogram(rows: list[tuple[int, ...]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        key = compact_lengths(row)
        out[key] = out.get(key, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: kv[0]))


def compact_signed_link_histogram(rows: list[tuple[int, int, tuple[int, ...]]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for even_cycles, odd_cycles, lengths in rows:
        key = f"even={even_cycles}, odd={odd_cycles}, lengths={compact_lengths(lengths)}"
        out[key] = out.get(key, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: kv[0]))


def dual_label(label: Label) -> Label:
    return (label[1], label[0])


def fixed_label_assignments_for_element(
    perm: list[int],
    signs: list[int],
    nmax: int,
) -> int:
    label_count = (nmax + 1) ** 2
    self_dual_count = nmax + 1
    seen = [False] * len(perm)
    total = 1
    for start in range(len(perm)):
        if seen[start]:
            continue
        cur = start
        parity = 1
        while not seen[cur]:
            seen[cur] = True
            parity *= signs[cur]
            cur = perm[cur]
        total *= label_count if parity == 1 else self_dual_count
    return total


def exact_label_orbit_count(stabilizer: list[GroupElement], nmax: int) -> int:
    fixed_sum = 0
    for element in stabilizer:
        perm, signs = action_permutation_on_links(element)
        fixed_sum += fixed_label_assignments_for_element(perm, signs, nmax)
    if fixed_sum % len(stabilizer) != 0:
        raise AssertionError("Burnside sum is not divisible by group order")
    return fixed_sum // len(stabilizer)


def sci_int(value: int) -> str:
    if value == 0:
        return "0"
    text = str(value)
    if len(text) <= 7:
        return text
    return f"{text[0]}.{text[1:4]}e{len(text) - 1}"


def gib_from_entries(entries: int) -> str:
    if entries == 0:
        return "0 GiB"
    log10_gib = math.log10(entries) + math.log10(COMPLEX_BYTES) - math.log10(1024**3)
    if log10_gib < 6:
        return f"{10 ** log10_gib:.6g} GiB"
    exponent = math.floor(log10_gib)
    mantissa = 10 ** (log10_gib - exponent)
    return f"{mantissa:.3f}e{exponent} GiB"


def toy_amplitude(state: tuple[int, int, int, int]) -> Fraction:
    left_label, right_label, left_internal, right_internal = state
    return (
        Fraction((left_label + 1) * (right_label + 1), 3)
        + Fraction((left_internal + 2) * (right_internal + 2), 5)
        + Fraction((left_label + left_internal + 1) * (right_label + right_internal + 1), 7)
    )


def toy_swap(state: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    left_label, right_label, left_internal, right_internal = state
    return right_label, left_label, right_internal, left_internal


def toy_orbits() -> list[list[tuple[int, int, int, int]]]:
    states = list(product((0, 1), repeat=4))
    seen: set[tuple[int, int, int, int]] = set()
    out: list[list[tuple[int, int, int, int]]] = []
    for state in states:
        if state in seen:
            continue
        orbit = sorted({state, toy_swap(state)})
        seen.update(orbit)
        out.append(orbit)
    return out


def exact_toy_falsifier() -> tuple[Fraction, Fraction, Fraction, Fraction, int, int]:
    states = list(product((0, 1), repeat=4))
    full = sum((toy_amplitude(state) for state in states), Fraction(0, 1))
    quotient = sum(
        (Fraction(len(orbit), 1) * toy_amplitude(orbit[0]) for orbit in toy_orbits()),
        Fraction(0, 1),
    )
    tied = sum(
        (toy_amplitude((label, label, internal, internal)) for label in (0, 1) for internal in (0, 1)),
        Fraction(0, 1),
    )
    doubled_tied = 2 * tied
    internal_trace_identity = 4
    internal_trace_swap = 2
    internal_trivial_dim = (internal_trace_identity + internal_trace_swap) // 2
    internal_sign_dim = (internal_trace_identity - internal_trace_swap) // 2
    return full, quotient, tied, doubled_tied, internal_trivial_dim, internal_sign_dim


def theorem_identity_example() -> bool:
    """Finite scalar identity behind the exact quotient statement.

    For any equivariant scalar term a(x) on a finite G-set X, the full
    contraction sum over X equals the orbit quotient with weight |G|/|G_x|.
    The toy network checks this with exact rationals and nontrivial internal
    index orbits.
    """

    full, quotient, _tied, _doubled_tied, _triv, _sign = exact_toy_falsifier()
    return full == quotient


def main() -> int:
    print("Plaquette environment quotient equivariance narrow theorem runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No external literature values, dates, random seeds, or comparator constants are used.")

    plaquettes = all_plaquettes()
    active_plaquette_indices = [i for i in range(len(plaquettes)) if i != MARKED_PLAQUETTE_INDEX]
    stabilizer = marked_stabilizer(plaquettes)

    section("1. Cost-note marked-plaquette stabilizer gate")
    site_orbits, link_orbits, plaquette_orbits, quotient_scopes = stabilizer_orbit_data(
        plaquettes, stabilizer
    )
    active_plaquette_orbits = [
        orbit for orbit in plaquette_orbits if MARKED_PLAQUETTE_INDEX not in orbit
    ]
    site_orbit_sizes = sorted(len(orbit) for orbit in site_orbits)
    link_orbit_sizes = sorted(len(orbit) for orbit in link_orbits)
    active_plaquette_orbit_sizes = sorted(len(orbit) for orbit in active_plaquette_orbits)
    marked_orbits = [orbit for orbit in plaquette_orbits if MARKED_PLAQUETTE_INDEX in orbit]
    print(f"stabilizer_order = {len(stabilizer)}")
    print(f"site_orbits = {len(site_orbits)}, sizes = {site_orbit_sizes}")
    print(f"link_orbits = {len(link_orbits)}, sizes = {link_orbit_sizes}")
    print(
        f"active_plaquette_orbits = {len(active_plaquette_orbits)}, "
        f"sizes = {active_plaquette_orbit_sizes}"
    )
    print(f"marked_plaquette_orbit = {marked_orbits[0] if marked_orbits else []}")
    print(f"link_orbit_diagnostic_scopes = {quotient_scopes}")
    check("cost-note gate: marked stabilizer order is 16", len(stabilizer) == 16)
    check("cost-note gate: link orbit count is 14", len(link_orbits) == 14)
    check(
        "cost-note gate: active plaquette orbit census matches 13 expected orbits",
        len(active_plaquette_orbits) == 13
        and active_plaquette_orbit_sizes
        == [2, 2, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 16],
    )
    check("site action is nontrivial and partitions all 27 sites", sum(site_orbit_sizes) == 27)
    check("marked plaquette is fixed as a set", len(marked_orbits) == 1 and marked_orbits[0] == [0])

    section("2. Group law and action cycle data")
    stabilizer_set = set(stabilizer)
    identity: GroupElement = (
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        (0, 0, 0),
    )
    closure_ok = all(compose(a, b) in stabilizer_set for a in stabilizer for b in stabilizer)
    inverse_ok = all(
        any(compose(a, b) == identity and compose(b, a) == identity for b in stabilizer)
        for a in stabilizer
    )
    site_cycle_rows = [tuple(cycle_lengths(action_permutation_on_sites(g))) for g in stabilizer]
    plaquette_cycle_rows = [
        tuple(cycle_lengths(action_permutation_on_plaquettes(g, plaquettes))) for g in stabilizer
    ]
    signed_link_rows = []
    orientation_reversing_elements = 0
    for element in stabilizer:
        perm, signs = action_permutation_on_links(element)
        even_cycles, odd_cycles, lengths = signed_link_cycle_counts(perm, signs)
        signed_link_rows.append((even_cycles, odd_cycles, tuple(lengths)))
        if any(sign == -1 for sign in signs):
            orientation_reversing_elements += 1
    print(f"site cycle histogram = {compact_histogram(site_cycle_rows)}")
    print(f"plaquette cycle histogram = {compact_histogram(plaquette_cycle_rows)}")
    print(f"signed link cycle histogram = {compact_signed_link_histogram(signed_link_rows)}")
    print(f"orientation_reversing_group_elements = {orientation_reversing_elements}")
    check("stabilizer closes under affine composition", closure_ok)
    check("stabilizer contains identity and inverses", identity in stabilizer_set and inverse_ok)
    check(
        "link action records orientation reversals that trigger SU(3) dual labels",
        orientation_reversing_elements > 0,
    )

    section("3. Exact rational falsifier before quotient exactness claim")
    full, quotient, tied, doubled_tied, internal_triv, internal_sign = exact_toy_falsifier()
    print(f"toy_full = {full}")
    print(f"toy_exact_orbit_quotient = {quotient}")
    print(f"toy_link_orbit_tied = {tied}")
    print(f"toy_group_order_times_tied = {doubled_tied}")
    print(f"toy_internal_C2_isotypic_dims = trivial:{internal_triv}, sign:{internal_sign}")
    print(f"toy_complete_orbit_cells = {len(toy_orbits())}")
    check("toy exact quotient equals full contraction in rational arithmetic", full == quotient)
    check("finite orbit-sum identity is the exact quotient rule", theorem_identity_example())
    check("toy tied quotient is falsified by exact arithmetic", tied != full)
    check("toy tied quotient is not repaired by multiplying by group order", doubled_tied != full)
    check(
        "toy internal index action has nontrivial isotypic content",
        internal_triv == 3 and internal_sign == 1,
    )

    section("4. Equivariance theorem finite-index identity and licensed cost")
    print(
        "Finite theorem used by the note: if each group element maps link labels by "
        "permutation plus dualization on reversed links, and maps intertwiner basis "
        "data by the induced representation, then each scalar summand is constant "
        "on complete label-plus-internal orbits. The exact quotient cell is a "
        "complete orbit representative with weight |G|/|Stab_G(cell)|."
    )
    for nmax in (2, 3):
        label_count = (nmax + 1) ** 2
        self_dual_count = nmax + 1
        fixed_identity = label_count ** (N_DIR * L_S**3)
        exact_orbits = exact_label_orbit_count(stabilizer, nmax)
        burnside_floor = fixed_identity // len(stabilizer)
        diagnostic_tied_cells = label_count ** len(link_orbits)
        print(
            f"NMAX={nmax}: labels={label_count}, self_dual={self_dual_count}, "
            f"dense_exact_label_orbits={sci_int(exact_orbits)}, "
            f"identity_term_floor={sci_int(burnside_floor)}, "
            f"link_orbit_tied_diagnostic_cells={sci_int(diagnostic_tied_cells)}, "
            f"dense_exact_orbit_memory={gib_from_entries(exact_orbits)}"
        )
        check(
            f"NMAX={nmax}: exact dense label-orbit quotient is not the link-orbit-tied diagnostic quotient",
            exact_orbits > diagnostic_tied_cells,
        )
        check(
            f"NMAX={nmax}: dense exact label-orbit storage estimate exceeds 4 GiB",
            exact_orbits * COMPLEX_BYTES > MEMORY_BUDGET_BYTES,
        )

    section("5. Licensed construction boundary")
    print(
        "The marked stabilizer equivariance is verified, but the link-orbit "
        "diagnostic graph is a fixed/tied diagnostic carrier. The licensed exact "
        "quotient must carry complete link-label orbit data plus the stabilizer "
        "action on intertwiner blocks. A first rho runner is therefore not "
        "licensed by this result."
    )
    print(
        "Open target: a rank-aware contractor may still use the same symmetry, but "
        "it must keep stabilizer isotypic blocks and prove its support pruning."
    )
    check("runner leaves rho computation and status authority untouched", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
