#!/usr/bin/env python3
"""Author exploratory controls for parent transport at every matching cardinality.

This is not a proof of a mixing bound. Every output is explicitly scoped to
the routes, immutable labels, and finite congestion counts implemented here.
"""
from pathlib import Path
from collections import deque, Counter, defaultdict
import datetime, hashlib, itertools, json, random, sys


def edge(a, b):
    return (min(a, b), max(a, b))


def canonical(m):
    return frozenset(m)


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def connected(n, edges):
    adj = adjacency(n, edges)
    seen, queue = {0}, [0]
    for a in queue:
        for b in sorted(adj[a] - seen):
            seen.add(b)
            queue.append(b)
    return len(seen) == n


def matchings(n, edges, k):
    adj = adjacency(n, edges)

    def rec(left, need):
        if need == 0:
            yield frozenset()
            return
        if len(left) < 2 * need:
            return
        a = min(left)
        rest = left - {a}
        if len(rest) >= 2 * need:
            yield from rec(rest, need)
        for b in sorted(adj[a] & rest):
            for tail in rec(rest - {b}, need - 1):
                yield tail | {edge(a, b)}

    return list(rec(set(range(n)), k))


def transport(n, edges, reference, source, target):
    """Route T-source to T-target; T need not be perfect or maximum.

    Quotient vertices are the edges of T and its unmatched singleton vertices.
    A quotient path alternates arbitrarily between these two node types.
    The record pair is moved backwards down each intervening empty corridor.
    """
    assert source in reference and target in reference
    if source == target:
        return []
    occupied = {v for e in reference for v in e}
    nodes = sorted(reference) + [(v,) for v in range(n) if v not in occupied]
    node_of = {v: node for node in nodes for v in node}
    quotient = {node: {} for node in nodes}
    for a, b in sorted(edges):
        u, v = node_of[a], node_of[b]
        if u != v:
            quotient[u].setdefault(v, (a, b))
            quotient[v].setdefault(u, (b, a))
    parents = {source: None}
    queue = deque([source])
    while queue and target not in parents:
        u = queue.popleft()
        for v in sorted(quotient[u]):
            if v not in parents:
                parents[v] = u
                queue.append(v)
    assert target in parents
    path, u = [], target
    while u is not None:
        path.append(u)
        u = parents[u]
    path.reverse()
    ops = []
    start = 0
    for finish in range(1, len(path)):
        if len(path[finish]) == 1:
            continue
        segment = path[start:finish + 1]
        a = quotient[segment[0]][segment[1]][0]
        b = quotient[segment[-2]][segment[-1]][1]
        aprime = next(v for v in segment[0] if v != a)
        bprime = next(v for v in segment[-1] if v != b)
        corridor = [a] + [node[0] for node in segment[1:-1]] + [b]
        assert all(edge(x, y) in edges for x, y in zip(corridor, corridor[1:]))
        pair_front, pair_back = b, bprime
        for vacant in reversed(corridor[:-1]):
            ops.append((vacant, pair_front, pair_back))
            pair_front, pair_back = vacant, pair_front
        ops.append((aprime, pair_front, pair_back))
        start = finish
    assert len(ops) <= n - 2
    return ops


def replay(n, edges, reference, source, target, ops):
    state = reference - {source}
    labels = [-1] * n
    for i, (a, b) in enumerate(sorted(state)):
        labels[a], labels[b] = 2 * i, 2 * i + 1
    initial_labels = labels[:]
    initial = state
    micros = []
    for a, b, c in ops:
        before = state
        assert labels[a] == -1 and edge(b, c) in state and edge(a, b) in edges
        assert len({a, b, c}) == 3
        old = labels[:]
        labels[a], labels[b], labels[c] = old[b], old[c], -1
        state = (state - {edge(b, c)}) | {edge(a, b)}
        assert len(state) == len(reference) - 1
        assert sorted(v for v in labels if v >= 0) == list(range(2 * len(state)))
        for u, v in state:
            assert labels[u] ^ labels[v] == 1
        positions = {x: u for u, x in enumerate(labels) if x >= 0}
        for u, x in enumerate(old):
            if x >= 0:
                assert positions[x] == u or edge(u, positions[x]) in edges
        micro = frozenset([before, state])
        assert len(micro) == 2
        micros.append(micro)
    assert state == reference - {target}
    assert len(micros) == len(set(micros))
    for a, b, c in reversed(ops):
        assert labels[c] == -1
        labels[c], labels[b], labels[a] = labels[b], labels[a], -1
        state = (state - {edge(a, b)}) | {edge(b, c)}
    assert state == initial and labels == initial_labels
    return micros


def graph_controls(n, edges):
    refs_by_micro = defaultdict(set)
    paths_by_micro = Counter()
    pair_counts, maxlen, reference_counts = Counter(), 0, Counter()
    for k in range(2, n // 2 + 1):
        for T in matchings(n, edges, k):
            reference_counts[k] += 1
            for e, f in itertools.permutations(sorted(T), 2):
                ops = transport(n, edges, T, e, f)
                micros = replay(n, edges, T, e, f, ops)
                maxlen = max(maxlen, len(ops))
                pair_counts[k] += 1
                for micro in micros:
                    refs_by_micro[micro].add(T)
                    paths_by_micro[micro] += 1
    m = len(edges)
    for micro, refs in refs_by_micro.items():
        # A micro-edge identifies the currently moving edge at each endpoint.
        # Each T is either an endpoint plus one edge, or that endpoint minus
        # its moving edge plus two graph edges. Count both orientations.
        endpoint, other = list(micro)
        moving = next(iter(endpoint - other))
        candidates = {endpoint | {e} for e in edges if e not in endpoint}
        candidates |= {(endpoint - {moving}) | {e, f}
                       for e, f in itertools.combinations(sorted(edges), 2)}
        moving2 = next(iter(other - endpoint))
        candidates |= {other | {e} for e in edges if e not in other}
        candidates |= {(other - {moving2}) | {e, f}
                       for e, f in itertools.combinations(sorted(edges), 2)}
        assert refs <= candidates
        assert len(refs) <= 2 * (m + m * m)
        k = len(endpoint) + 1
        assert paths_by_micro[micro] <= 2 * (m + m * m) * k * (k - 1)
    return {'vertices': n, 'edges': m,
            'reference_counts_by_cardinality': dict(reference_counts),
            'ordered_parent_pairs_by_cardinality': dict(pair_counts),
            'longest_route': maxlen, 'route_bound': n - 2,
            'largest_reference_multiplicity': max(map(len, refs_by_micro.values()), default=0),
            'largest_ordered_path_congestion': max(paths_by_micro.values(), default=0)}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: geometric_corridor_transport_check.py NEW_OUTPUT_DIRECTORY')
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    for n in [3, 4, 5]:
        possible = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = {e for i, e in enumerate(possible) if mask >> i & 1}
            if connected(n, edges):
                rows.append(graph_controls(n, edges))
        print(json.dumps({'exhaustive_vertices_through': n, 'graphs_done': len(rows)}), flush=True)
    rng = random.Random(9211646)
    for n in [6, 7, 8, 9, 10, 12]:
        for trial in range(12):
            edges = {edge(i, i + 1) for i in range(n - 1)}
            if trial:
                for e in itertools.combinations(range(n), 2):
                    if rng.random() < .12:
                        edges.add(e)
            rows.append(graph_controls(n, edges))
        print(json.dumps({'random_vertices': n, 'graphs_done': len(rows)}), flush=True)
    result = {'scope': 'Author all-cardinality parent transport and immutable slide controls; no mixing theorem asserted.',
              'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'graphs': len(rows), 'rows': rows,
              'parent_pairs': sum(sum(r['ordered_parent_pairs_by_cardinality'].values()) for r in rows)}
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'complete': True, 'graphs': len(rows), 'parent_pairs': result['parent_pairs']}))


if __name__ == '__main__':
    main()
