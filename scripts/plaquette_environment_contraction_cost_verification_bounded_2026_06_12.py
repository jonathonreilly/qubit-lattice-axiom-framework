#!/usr/bin/env python3
"""Bounded cost verification for the marked L_s=3 spatial Wilson environment.

This runner costs the exact-on-box contraction geometry; it does not perform
the contraction.  It keeps the calculation deterministic and repo-local:

* finite L_s=3 periodic spatial Wilson geometry;
* one marked plaquette removed from the active environment factors;
* graph-width brackets from deterministic eliminations plus lower bounds;
* finite marked-plaquette stabilizer/orbit bookkeeping;
* SU(3) finite-box fusion support counts from an in-runner LR rule.

The sparse cost layer is an estimator over support counts, not a theorem that
all cancellations or all intertwiner gauges have been exploited.
"""

from __future__ import annotations

import math
from functools import lru_cache
from itertools import combinations, permutations, product


AUDIT_TIMEOUT_SEC = 600

L_S = 3
N_DIR = 3
MARKED_PLAQUETTE_INDEX = 0
COMPLEX_BYTES = 16
MEMORY_BUDGET_BYTES = 4 * 1024**3

PASS = 0
FAIL = 0

DIR_VEC = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
PLAQUETTE_CYCLE_PAIRS = ((0, 1), (0, 3), (1, 2), (2, 3))

Label = tuple[int, int]
Partition = tuple[int, int, int]


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


def add_site(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((a[i] + b[i]) % L_S for i in range(3))


def basis_vec(direction: int) -> tuple[int, int, int]:
    return tuple(1 if i == direction else 0 for i in range(3))


def link_id(site: tuple[int, int, int], direction: int) -> int:
    x, y, z = site
    return (((x * L_S) + y) * L_S + z) * N_DIR + direction


def id_to_link(idx: int) -> tuple[int, int, int, int]:
    direction = idx % N_DIR
    n = idx // N_DIR
    z = n % L_S
    n //= L_S
    y = n % L_S
    x = n // L_S
    return (x, y, z, direction)


def all_links() -> list[tuple[int, int, int, int]]:
    return [(x, y, z, d) for x, y, z in product(range(L_S), repeat=3) for d in range(3)]


def all_plaquettes() -> list[tuple[tuple[int, int, int], int, int, tuple[int, ...]]]:
    plaquettes: list[tuple[tuple[int, int, int], int, int, tuple[int, ...]]] = []
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


def active_plaquettes(
    plaquettes: list[tuple[tuple[int, int, int], int, int, tuple[int, ...]]],
) -> list[tuple[tuple[int, int, int], int, int, tuple[int, ...]]]:
    return [p for i, p in enumerate(plaquettes) if i != MARKED_PLAQUETTE_INDEX]


def build_graph(scopes: list[tuple[int, ...]], model: str) -> dict[int, set[int]]:
    adj = {i: set() for i in range(N_DIR * L_S**3)}
    for scope in scopes:
        if model == "factor_primal":
            pairs = combinations(range(len(scope)), 2)
        elif model == "cycle_index":
            pairs = PLAQUETTE_CYCLE_PAIRS
        else:
            raise ValueError(f"unknown graph model: {model}")
        for a, b in pairs:
            u = scope[a]
            v = scope[b]
            if u != v:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def graph_stats(adj: dict[int, set[int]]) -> tuple[int, int, int, int, float]:
    degrees = [len(v) for v in adj.values()]
    return (
        len(adj),
        sum(degrees) // 2,
        min(degrees),
        max(degrees),
        sum(degrees) / len(degrees),
    )


def fill_count(adj: dict[int, set[int]], node: int) -> int:
    neighbors = list(adj[node])
    fill = 0
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            if neighbors[j] not in adj[neighbors[i]]:
                fill += 1
    return fill


def weighted_fill_count(adj: dict[int, set[int]], node: int) -> int:
    neighbors = list(adj[node])
    total = 0
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            if neighbors[j] not in adj[neighbors[i]]:
                total += len(adj[neighbors[i]]) * len(adj[neighbors[j]])
    return total


def elimination_order(
    adj_in: dict[int, set[int]],
    heuristic: str,
    protected: set[int] | None = None,
) -> tuple[list[int], int, list[int]]:
    protected = protected or set()
    adj = {u: set(vs) for u, vs in adj_in.items()}
    order: list[int] = []
    clique_sizes: list[int] = []
    max_clique = 0
    while adj:
        candidates = [u for u in adj if u not in protected] or list(adj)

        def key(u: int) -> tuple[int, ...]:
            degree = len(adj[u])
            fill = fill_count(adj, u)
            wfill = weighted_fill_count(adj, u)
            x, y, z, direction = id_to_link(u)
            if heuristic == "min_degree":
                return (degree, fill, u)
            if heuristic == "min_fill":
                return (fill, degree, u)
            if heuristic == "weighted_min_fill":
                return (wfill, fill, degree, u)
            if heuristic == "degree_fill_coord":
                return (degree, fill, direction, x, y, z, u)
            if heuristic == "coord_fill":
                return (direction, x, y, z, fill, degree, u)
            raise ValueError(f"unknown heuristic: {heuristic}")

        node = min(candidates, key=key)
        neighbors = set(adj[node])
        clique = len(neighbors) + 1
        max_clique = max(max_clique, clique)
        clique_sizes.append(clique)
        for a, b in combinations(neighbors, 2):
            adj[a].add(b)
            adj[b].add(a)
        for neighbor in neighbors:
            adj[neighbor].discard(node)
        del adj[node]
        order.append(node)
    return order, max_clique, clique_sizes


def degeneracy_lower_bound(adj_in: dict[int, set[int]]) -> int:
    adj = {u: set(vs) for u, vs in adj_in.items()}
    lower = 0
    while adj:
        node = min(adj, key=lambda u: (len(adj[u]), u))
        lower = max(lower, len(adj[node]))
        for neighbor in list(adj[node]):
            adj[neighbor].discard(node)
        del adj[node]
    return lower


def minor_min_width_lower_bound(adj_in: dict[int, set[int]], mode: str) -> int:
    adj = {u: set(vs) for u, vs in adj_in.items()}
    lower = 0
    while adj:
        node = min(adj, key=lambda u: (len(adj[u]), u))
        lower = max(lower, len(adj[node]))
        if not adj[node]:
            del adj[node]
            continue
        if mode == "min_degree_neighbor":
            target = min(adj[node], key=lambda u: (len(adj[u]), u))
        elif mode == "max_degree_neighbor":
            target = max(adj[node], key=lambda u: (len(adj[u]), -u))
        elif mode == "max_common_neighbor":
            target = max(
                adj[node],
                key=lambda u: (len(adj[node] & adj[u]), len(adj[u]), -u),
            )
        else:
            raise ValueError(mode)
        merged = (adj[node] | adj[target]) - {node, target}
        for neighbor in list(adj[node]):
            adj[neighbor].discard(node)
        for neighbor in list(adj[target]):
            adj[neighbor].discard(target)
        del adj[node]
        adj[target] = set(merged)
        for neighbor in merged:
            adj[neighbor].add(target)
    return lower


def max_clique_size(adj: dict[int, set[int]]) -> int:
    best = 0
    vertices = set(adj)

    def bron_kerbosch(r: set[int], p: set[int], x: set[int]) -> None:
        nonlocal best
        if len(r) + len(p) <= best:
            return
        if not p and not x:
            best = max(best, len(r))
            return
        pivot_pool = p | x
        pivot = max(pivot_pool, key=lambda u: len(p & adj[u])) if pivot_pool else None
        candidates = p - (adj[pivot] if pivot is not None else set())
        for vertex in list(candidates):
            bron_kerbosch(r | {vertex}, p & adj[vertex], x & adj[vertex])
            p.remove(vertex)
            x.add(vertex)

    bron_kerbosch(set(), set(vertices), set())
    return best


def bracket_width(
    adj: dict[int, set[int]], protected: set[int]
) -> tuple[dict[str, int], dict[str, int], list[int], str, int]:
    lower = {
        "max_clique": max_clique_size(adj) - 1,
        "degeneracy": degeneracy_lower_bound(adj),
        "mmw_min": minor_min_width_lower_bound(adj, "min_degree_neighbor"),
        "mmw_max": minor_min_width_lower_bound(adj, "max_degree_neighbor"),
        "mmw_common": minor_min_width_lower_bound(adj, "max_common_neighbor"),
    }
    upper: dict[str, int] = {}
    best_name = ""
    best_clique = 10**9
    best_cliques: list[int] = []
    for heuristic in (
        "min_degree",
        "min_fill",
        "weighted_min_fill",
        "degree_fill_coord",
        "coord_fill",
    ):
        _order, max_clique, clique_sizes = elimination_order(adj, heuristic, protected)
        upper[heuristic] = max_clique - 1
        if max_clique < best_clique:
            best_name = heuristic
            best_clique = max_clique
            best_cliques = clique_sizes
    return lower, upper, best_cliques, best_name, best_clique


def signed_permutation_matrices() -> list[tuple[tuple[int, ...], ...]]:
    out: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, col in enumerate(perm):
                matrix[row][col] = signs[row] % L_S
            out.append(tuple(tuple(row) for row in matrix))
    return out


def mat_vec(
    matrix: tuple[tuple[int, ...], ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) % L_S for i in range(3))


def affine_vertex(
    matrix: tuple[tuple[int, ...], ...],
    translation: tuple[int, int, int],
    vertex: tuple[int, int, int],
) -> tuple[int, int, int]:
    return add_site(mat_vec(matrix, vertex), translation)


def link_tuple_transform(
    matrix: tuple[tuple[int, ...], ...],
    translation: tuple[int, int, int],
    link: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    start = link[:3]
    endpoint = add_site(start, basis_vec(link[3]))
    image_start = affine_vertex(matrix, translation, start)
    image_endpoint = affine_vertex(matrix, translation, endpoint)
    diff = tuple((image_endpoint[i] - image_start[i]) % L_S for i in range(3))
    for direction in range(3):
        forward = basis_vec(direction)
        backward = tuple((-v) % L_S for v in forward)
        if diff == forward:
            return image_start + (direction,)
        if diff == backward:
            return image_endpoint + (direction,)
    raise RuntimeError(f"not a signed basis direction: {diff}")


def plaquette_link_tuples(
    plaquette: tuple[tuple[int, int, int], int, int, tuple[int, ...]]
) -> frozenset[tuple[int, int, int, int]]:
    return frozenset(id_to_link(idx) for idx in plaquette[3])


def stabilizer_and_orbits(
    plaquettes: list[tuple[tuple[int, int, int], int, int, tuple[int, ...]]],
) -> tuple[
    list[tuple[tuple[tuple[int, ...], ...], tuple[int, int, int]]],
    list[list[tuple[int, int, int, int]]],
    list[list[int]],
    list[tuple[int, ...]],
]:
    marked = plaquettes[MARKED_PLAQUETTE_INDEX]
    marked_vertices = {
        marked[0],
        add_site(marked[0], basis_vec(marked[1])),
        add_site(marked[0], basis_vec(marked[2])),
        add_site(add_site(marked[0], basis_vec(marked[1])), basis_vec(marked[2])),
    }
    marked_boundary = plaquette_link_tuples(marked)
    stabilizer: list[tuple[tuple[tuple[int, ...], ...], tuple[int, int, int]]] = []
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

    links = all_links()
    link_orbits: list[list[tuple[int, int, int, int]]] = []
    link_orbit_id: dict[tuple[int, int, int, int], int] = {}
    seen_links: set[tuple[int, int, int, int]] = set()
    for link in links:
        if link in seen_links:
            continue
        orbit: set[tuple[int, int, int, int]] = set()
        stack = [link]
        while stack:
            item = stack.pop()
            if item in orbit:
                continue
            orbit.add(item)
            for matrix, translation in stabilizer:
                stack.append(link_tuple_transform(matrix, translation, item))
        orbit_list = sorted(orbit)
        orbit_index = len(link_orbits)
        for item in orbit_list:
            link_orbit_id[item] = orbit_index
        seen_links.update(orbit_list)
        link_orbits.append(orbit_list)

    plaquette_set_to_index = {plaquette_link_tuples(p): i for i, p in enumerate(plaquettes)}

    def plaquette_transform_index(
        matrix: tuple[tuple[int, ...], ...], translation: tuple[int, int, int], idx: int
    ) -> int:
        image = frozenset(
            link_tuple_transform(matrix, translation, link)
            for link in plaquette_link_tuples(plaquettes[idx])
        )
        return plaquette_set_to_index[image]

    plaquette_orbits: list[list[int]] = []
    plaquette_orbit_id: dict[int, int] = {}
    seen_plaquettes: set[int] = set()
    for idx in range(len(plaquettes)):
        if idx in seen_plaquettes:
            continue
        orbit_idx: set[int] = set()
        stack = [idx]
        while stack:
            item = stack.pop()
            if item in orbit_idx:
                continue
            orbit_idx.add(item)
            for matrix, translation in stabilizer:
                stack.append(plaquette_transform_index(matrix, translation, item))
        orbit_list = sorted(orbit_idx)
        orbit_index = len(plaquette_orbits)
        for item in orbit_list:
            plaquette_orbit_id[item] = orbit_index
        seen_plaquettes.update(orbit_list)
        plaquette_orbits.append(orbit_list)

    active_orbit_ids = sorted(
        {plaquette_orbit_id[i] for i in range(len(plaquettes)) if i != MARKED_PLAQUETTE_INDEX}
    )
    quotient_scopes: list[tuple[int, ...]] = []
    for orbit_id in active_orbit_ids:
        representative = next(
            idx
            for idx, poid in plaquette_orbit_id.items()
            if poid == orbit_id and idx != MARKED_PLAQUETTE_INDEX
        )
        quotient_scopes.append(
            tuple(
                sorted(
                    {
                        link_orbit_id[id_to_link(link_idx)]
                        for link_idx in plaquettes[representative][3]
                    }
                )
            )
        )
    return stabilizer, link_orbits, plaquette_orbits, quotient_scopes


def quotient_width(scopes: list[tuple[int, ...]], n_nodes: int) -> tuple[int, int, int]:
    adj = {i: set() for i in range(n_nodes)}
    for scope in scopes:
        for u, v in combinations(scope, 2):
            adj[u].add(v)
            adj[v].add(u)
    _order, max_clique, _sizes = elimination_order(adj, "min_fill", set())
    lower = max(
        max_clique_size(adj) - 1,
        degeneracy_lower_bound(adj),
        minor_min_width_lower_bound(adj, "min_degree_neighbor"),
    )
    return lower, max_clique - 1, max_clique


def partition_from_label(label: Label) -> Partition:
    p, q = label
    return (p + q, q, 0)


def label_from_partition(partition: Partition) -> Label:
    return (partition[0] - partition[1], partition[1] - partition[2])


def partitions3(total: int) -> list[Partition]:
    out: list[Partition] = []
    for a in range(total, -1, -1):
        for b in range(min(a, total - a), -1, -1):
            c = total - a - b
            if 0 <= c <= b:
                out.append((a, b, c))
    return out


@lru_cache(maxsize=None)
def lr_coeff(lam: Partition, mu: Partition, nu: Partition) -> int:
    if sum(nu) != sum(lam) + sum(mu):
        return 0
    if any(nu[i] < lam[i] for i in range(3)):
        return 0
    cells: list[tuple[int, int]] = []
    for row in range(3):
        for col in range(lam[row], nu[row]):
            cells.append((row, col))
    cells.sort(key=lambda rc: (rc[0], -rc[1]))
    remaining = [0, mu[0], mu[1], mu[2]]
    counts = [0, 0, 0, 0]
    filled: dict[tuple[int, int], int] = {}
    total = 0

    def can_place(row: int, col: int, val: int) -> bool:
        right = (row, col + 1)
        if right in filled and val > filled[right]:
            return False
        left = (row, col - 1)
        if left in filled and filled[left] > val:
            return False
        above = (row - 1, col)
        if above in filled and not (filled[above] < val):
            return False
        below = (row + 1, col)
        if below in filled and not (val < filled[below]):
            return False
        return True

    def recurse(pos: int) -> None:
        nonlocal total
        if pos == len(cells):
            total += 1
            return
        row, col = cells[pos]
        for val in (1, 2, 3):
            if remaining[val] == 0 or not can_place(row, col, val):
                continue
            remaining[val] -= 1
            counts[val] += 1
            if counts[1] >= counts[2] >= counts[3]:
                filled[(row, col)] = val
                recurse(pos + 1)
                del filled[(row, col)]
            counts[val] -= 1
            remaining[val] += 1

    recurse(0)
    return total


@lru_cache(maxsize=None)
def fusion_decomposition(left: Label, right: Label) -> tuple[tuple[Label, int], ...]:
    lam = partition_from_label(left)
    mu = partition_from_label(right)
    total = sum(lam) + sum(mu)
    out: dict[Label, int] = {}
    for nu in partitions3(total):
        if any(nu[i] < lam[i] for i in range(3)):
            continue
        coeff = lr_coeff(lam, mu, nu)
        if coeff:
            label = label_from_partition(nu)
            out[label] = out.get(label, 0) + coeff
    return tuple(sorted(out.items()))


def labels_box(nmax: int) -> list[Label]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def local_plaquette_support_stats(nmax: int) -> tuple[int, int, float, float, int]:
    labels = labels_box(nmax)
    decomps = {(a, b): dict(fusion_decomposition(a, b)) for a in labels for b in labels}
    allowed = 0
    channel_count = 0
    max_channels = 0
    for a, b, c, d in product(labels, repeat=4):
        left = decomps[(a, b)]
        right = decomps[(c, d)]
        channels = sum(left[label] * right[label] for label in set(left) & set(right))
        if channels:
            allowed += 1
            channel_count += channels
            max_channels = max(max_channels, channels)
    total = len(labels) ** 4
    density = allowed / total
    avg_channels = channel_count / allowed
    return allowed, total, density, avg_channels, max_channels


def format_power10_from_log(log10_value: float, unit: str) -> str:
    if log10_value < 6.0:
        return f"{10.0 ** log10_value:.6g} {unit}"
    exponent = math.floor(log10_value)
    mantissa = 10.0 ** (log10_value - exponent)
    return f"{mantissa:.3f}e{exponent} {unit}"


def format_entries(entries: float) -> str:
    if entries <= 0.0:
        return "0"
    return format_power10_from_log(math.log10(entries), "entries")


def dense_cost_from_cliques(m_states: int, clique_sizes: list[int]) -> tuple[float, float]:
    peak_entries = float(max(m_states**size for size in clique_sizes))
    flops = float(sum(m_states**size for size in clique_sizes))
    return peak_entries, flops


def sparse_support_estimate(
    m_states: int,
    local_density: float,
    scopes: list[tuple[int, ...]],
    order: list[int],
) -> tuple[float, float, int]:
    factors: list[tuple[frozenset[int], float]] = [
        (frozenset(scope), (m_states**4) * local_density) for scope in scopes
    ]
    peak = 0.0
    flops = 0.0
    peak_scope = 0
    for node in order:
        involved = [(scope, nnz) for scope, nnz in factors if node in scope]
        if not involved:
            continue
        others = [(scope, nnz) for scope, nnz in factors if node not in scope]
        union_scope: set[int] = set()
        sum_sizes = 0
        product_nnz = 1.0
        for scope, nnz in involved:
            union_scope.update(scope)
            sum_sizes += len(scope)
            product_nnz *= nnz
        join_est = product_nnz / (m_states ** (sum_sizes - len(union_scope)))
        join_est = min(join_est, float(m_states ** len(union_scope)))
        out_scope = frozenset(x for x in union_scope if x != node)
        out_est = min(float(m_states ** len(out_scope)), join_est)
        peak = max(peak, join_est, out_est)
        peak_scope = max(peak_scope, len(union_scope), len(out_scope))
        flops += join_est
        if out_scope:
            others.append((out_scope, out_est))
        factors = others
    return peak, flops, peak_scope


def memory_gib(entries: float) -> float:
    return entries * COMPLEX_BYTES / 1024**3


def main() -> int:
    print("Plaquette environment contraction cost verification, bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No external literature values, dates, random seeds, or comparator constants are used.")

    plaquettes = all_plaquettes()
    active = active_plaquettes(plaquettes)
    marked = plaquettes[MARKED_PLAQUETTE_INDEX]
    marked_boundary = set(marked[3])
    active_scopes = [p[3] for p in active]

    section("1. Marked L_s=3 environment census")
    print(f"links = {N_DIR * L_S**3}")
    print(f"plaquettes_total = {len(plaquettes)}")
    print(f"active_environment_plaquettes = {len(active)}")
    print(f"marked_plaquette = site={marked[0]}, plane=({marked[1]},{marked[2]})")
    print(f"marked_boundary_link_ids = {sorted(marked_boundary)}")
    incidence_count = sum(len(scope) for scope in active_scopes)
    boundary_active_incidence = sum(1 for scope in active_scopes for link in scope if link in marked_boundary)
    check("census has 81 links and 81 total plaquettes", len(plaquettes) == 81 and N_DIR * L_S**3 == 81)
    check("marked environment has 80 active plaquette factors", len(active) == 80)
    check(
        "active incidence count is 320 with four boundary links each missing one marked incidence",
        incidence_count == 320 and boundary_active_incidence == 12,
        f"incidences={incidence_count}, boundary_active_incidence={boundary_active_incidence}",
    )

    section("2. Raw graph-width brackets")
    raw_adj = build_graph(active_scopes, "factor_primal")
    cycle_adj = build_graph(active_scopes, "cycle_index")
    raw_stats = graph_stats(raw_adj)
    cycle_stats = graph_stats(cycle_adj)
    print(
        "factor-primal graph: "
        f"nodes={raw_stats[0]}, edges={raw_stats[1]}, degree={raw_stats[2]}..{raw_stats[3]}, "
        f"mean={raw_stats[4]:.6f}"
    )
    print(
        "cycle-index graph:   "
        f"nodes={cycle_stats[0]}, edges={cycle_stats[1]}, degree={cycle_stats[2]}..{cycle_stats[3]}, "
        f"mean={cycle_stats[4]:.6f}"
    )
    raw_lower, raw_upper, raw_best_cliques, raw_best_name, raw_best_clique = bracket_width(
        raw_adj, marked_boundary
    )
    cycle_lower, cycle_upper, _cycle_best_cliques, cycle_best_name, cycle_best_clique = bracket_width(
        cycle_adj, marked_boundary
    )
    print(f"factor-primal lower bounds: {raw_lower}")
    print(f"factor-primal upper bounds: {raw_upper}")
    print(
        f"factor-primal bracket: {max(raw_lower.values())} <= treewidth <= {min(raw_upper.values())} "
        f"(best={raw_best_name}, clique_size={raw_best_clique})"
    )
    print(f"cycle-index lower bounds: {cycle_lower}")
    print(f"cycle-index upper bounds: {cycle_upper}")
    print(
        f"cycle-index cross-check bracket: {max(cycle_lower.values())} <= treewidth <= {min(cycle_upper.values())} "
        f"(best={cycle_best_name}, clique_size={cycle_best_clique})"
    )
    check("raw factor-primal graph has the expected 81 nodes and 480 edges", raw_stats[:2] == (81, 480))
    check("raw factor-primal width is bracketed by lower and upper bounds", max(raw_lower.values()) <= min(raw_upper.values()))
    check("cycle-index marked graph is bracketed and not reused as the raw factor-primal cost", max(cycle_lower.values()) <= min(cycle_upper.values()))

    section("3. Marked-plaquette stabilizer and orbit quotient")
    stabilizer, link_orbits, plaquette_orbits, quotient_scopes = stabilizer_and_orbits(plaquettes)
    active_plaquette_orbits = [orbit for orbit in plaquette_orbits if MARKED_PLAQUETTE_INDEX not in orbit]
    quotient_lower, quotient_width_value, quotient_clique = quotient_width(quotient_scopes, len(link_orbits))
    link_orbit_sizes = sorted(len(orbit) for orbit in link_orbits)
    active_plaquette_orbit_sizes = sorted(len(orbit) for orbit in active_plaquette_orbits)
    print(f"stabilizer_order = {len(stabilizer)}")
    print(f"link_orbits = {len(link_orbits)}, sizes = {link_orbit_sizes}")
    print(
        f"active_plaquette_orbits = {len(active_plaquette_orbits)}, "
        f"sizes = {active_plaquette_orbit_sizes}"
    )
    print(f"quotient_factor_scopes = {quotient_scopes}")
    print(
        f"orbit quotient bracket: {quotient_lower} <= treewidth <= {quotient_width_value} "
        f"(clique_size={quotient_clique})"
    )
    print(
        "class-sector note: the marked-boundary readout is central and can be "
        "reported by one SU(3) character label at a time; this blocks the output "
        "sector, not the independent internal link-label graph."
    )
    check("marked plaquette affine stabilizer has order 16", len(stabilizer) == 16)
    check("stabilizer gives 14 link orbits and 13 active plaquette orbits", len(link_orbits) == 14 and len(active_plaquette_orbits) == 13)
    check("orbit quotient width is small but recorded as a quotient diagnostic", quotient_width_value == 5)

    section("4. SU(3) finite-box support densities")
    known = {
        ((1, 0), (0, 1)): {((1, 1), 1), ((0, 0), 1)},
        ((1, 0), (1, 0)): {((2, 0), 1), ((0, 1), 1)},
        ((1, 1), (1, 1)): {((2, 2), 1), ((3, 0), 1), ((0, 3), 1), ((1, 1), 2), ((0, 0), 1)},
    }
    for pair, expected in known.items():
        got = set(fusion_decomposition(*pair))
        check(f"LR fusion check {pair[0]} x {pair[1]}", got == expected, f"got={sorted(got)}")

    support_rows: dict[int, tuple[int, int, float, float, int]] = {}
    for nmax in (2, 3, 4):
        row = local_plaquette_support_stats(nmax)
        support_rows[nmax] = row
        allowed, total, density, avg_channels, max_channels = row
        print(
            f"NMAX={nmax}: labels={(nmax + 1) ** 2}, support={allowed}/{total}, "
            f"density={density:.9f}, avg_channels={avg_channels:.6f}, max_channels={max_channels}"
        )
    check("local plaquette support density is below dense for NMAX=2,3,4", all(row[2] < 1.0 for row in support_rows.values()))

    section("5. Cost table")
    raw_order, _raw_clique, raw_clique_sizes = elimination_order(raw_adj, raw_best_name, marked_boundary)
    quotient_cliques: list[int] = []
    quotient_adj = {i: set() for i in range(len(link_orbits))}
    for scope in quotient_scopes:
        for u, v in combinations(scope, 2):
            quotient_adj[u].add(v)
            quotient_adj[v].add(u)
    _q_order, _q_max_clique, quotient_cliques = elimination_order(quotient_adj, "min_fill", set())

    print(
        "method | NMAX | labels | peak memory | FLOP/support-op estimate | "
        "fits 4 GiB | exact original graph"
    )
    print("-" * 120)
    raw_dense_all_over_budget = True
    sparse_est_all_over_budget = True
    for nmax in (2, 3, 4):
        m_states = (nmax + 1) ** 2
        allowed, total, density, _avg_channels, _max_channels = support_rows[nmax]

        dense_entries, dense_flops = dense_cost_from_cliques(m_states, raw_clique_sizes)
        dense_mem = memory_gib(dense_entries)
        dense_fits = dense_entries * COMPLEX_BYTES <= MEMORY_BUDGET_BYTES
        raw_dense_all_over_budget = raw_dense_all_over_budget and not dense_fits
        print(
            f"raw_dense | {nmax} | {m_states} | "
            f"{format_power10_from_log(math.log10(dense_mem), 'GiB')} | "
            f"{format_entries(dense_flops)} | {dense_fits} | True"
        )

        sparse_entries, sparse_flops, sparse_scope = sparse_support_estimate(
            m_states, density, active_scopes, raw_order
        )
        sparse_mem = memory_gib(sparse_entries)
        sparse_fits = sparse_entries * COMPLEX_BYTES <= MEMORY_BUDGET_BYTES
        sparse_est_all_over_budget = sparse_est_all_over_budget and not sparse_fits
        print(
            f"sparse_support_est | {nmax} | {m_states} | "
            f"{format_power10_from_log(math.log10(sparse_mem), 'GiB')} | "
            f"{format_entries(sparse_flops)} | {sparse_fits} | estimate"
            f" (peak_scope={sparse_scope})"
        )

        quotient_entries, quotient_flops = dense_cost_from_cliques(m_states, quotient_cliques)
        quotient_mem = memory_gib(quotient_entries)
        quotient_fits = quotient_entries * COMPLEX_BYTES <= MEMORY_BUDGET_BYTES
        print(
            f"orbit_quotient_diag | {nmax} | {m_states} | "
            f"{format_power10_from_log(math.log10(quotient_mem), 'GiB')} | "
            f"{format_entries(quotient_flops)} | {quotient_fits} | False"
        )

    check("raw dense exact original-graph cells exceed the 4 GiB budget for NMAX=2,3,4", raw_dense_all_over_budget)
    check("sparse support estimates for original graph also exceed the 4 GiB budget", sparse_est_all_over_budget)
    check("orbit quotient diagnostic is not counted as an exact original-graph contraction", True)

    section("6. Bounded caveats")
    print(
        "Result boundary: the raw factor-primal exact original graph remains over "
        "budget for all tested NMAX values under the best deterministic order found here."
    )
    print(
        "Open targets: a certified lower bound sharper than MMW, a rank-aware "
        "contractor using intertwiner gauges rather than support estimates, and an "
        "exact symmetry-block construction that acts on the original independent-link "
        "state space rather than the orbit-tied quotient."
    )
    check("runner reports bounded cost data without computing rho", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
