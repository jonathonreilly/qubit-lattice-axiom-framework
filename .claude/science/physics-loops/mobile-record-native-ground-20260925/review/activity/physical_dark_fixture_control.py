#!/usr/bin/env python3
"""Own exact cubic charge/flux fixture, with all original primitive outputs."""
from collections import Counter, defaultdict, deque
from itertools import product
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
tic = time.perf_counter()
L = 6
vertices = list(product(range(L), repeat=3))
index = {x: i for i, x in enumerate(vertices)}
A = [i for i, x in enumerate(vertices) if sum(x) % 2 == 0]
B = [i for i, x in enumerate(vertices) if sum(x) % 2 == 1]
Aset = set(A)


def neighbours(i):
    x = vertices[i]
    out = []
    for axis in range(3):
        for step in (-1, 1):
            y = list(x)
            y[axis] = (y[axis] + step) % L
            out.append(index[tuple(y)])
    return sorted(out)


nb = {i: neighbours(i) for i in range(len(vertices))}
edges = [(a, b) for a in A for b in nb[a]]
edge_index = {e: k for k, e in enumerate(edges)}
pairs = [(a, c) for j, a in enumerate(A) for c in A[j + 1:]
         if set(nb[a]) & set(nb[c])]
pair_degrees = Counter(x for p in pairs for x in p)
pair_overlaps = Counter(len(set(nb[a]) & set(nb[c])) for a, c in pairs)
assert set(pair_degrees.values()) == {18}
assert pair_overlaps == {1: 3 * len(A), 2: 6 * len(A)}

holes = {index[(1, 0, 0)], index[(3, 2, 0)]}
occupied_B = [b for b in B if b not in holes]
q0 = [0] * len(vertices)
for a in A:
    q0[a] = 1
for j, b in enumerate(occupied_B):
    q0[b] = -1 if j < len(occupied_B) // 2 else 1
q0 = tuple(q0)
assert sum(q0) == len(A)
assert all(sum(b in holes for b in nb[a]) <= 1 for a in A)

# Independent integer spanning-tree divergence solution, A-to-B orientation.
parents = {0: None}
order = []
queue = deque([0])
while queue:
    u = queue.popleft()
    order.append(u)
    for v in nb[u]:
        if v not in parents:
            parents[v] = u
            queue.append(v)
subtree = [q0[i] - int(i in Aset) for i in range(len(vertices))]
E0 = [0] * len(edges)
for v in reversed(order[1:]):
    u = parents[v]
    a, b = (v, u) if v in Aset else (u, v)
    E0[edge_index[(a, b)]] = subtree[v] if v == a else -subtree[v]
    subtree[u] += subtree[v]
assert subtree[0] == 0
div = [0] * len(vertices)
for (a, b), e in zip(edges, E0):
    div[a] += e
    div[b] -= e
assert div == [q0[i] - int(i in Aset) for i in range(len(vertices))]

seen_states = set()


def shifted(difference, k, amount):
    d = dict(difference)
    d[k] = d.get(k, 0) + amount
    return tuple(sorted((i, e) for i, e in d.items() if e))


def check(state):
    if state in seen_states:
        return
    q, difference = state
    residual = [q0[i] - q[i] for i in range(len(vertices))]
    for k, e in difference:
        a, b = edges[k]
        residual[a] += e
        residual[b] -= e
    assert not any(residual), (q, difference, residual)
    seen_states.add(state)


def outward(state, a):
    q, difference = state
    if not q[a]:
        return []
    out = []
    for b in nb[a]:
        if q[b]:
            continue
        r = list(q)
        r[a], r[b] = 0, q[a]
        result = tuple(r), shifted(difference, edge_index[(a, b)], -q[a])
        check(result)
        out.append(result)
    return out


def inward(state, a):
    q, difference = state
    if q[a]:
        return []
    out = []
    for b in nb[a]:
        if not q[b]:
            continue
        r = list(q)
        r[a], r[b] = q[b], 0
        result = tuple(r), shifted(difference, edge_index[(a, b)], q[b])
        check(result)
        out.append(result)
    return out


def born(state, a, b, sigma):
    q, difference = state
    if q[a] or q[b]:
        return None
    r = list(q)
    r[a], r[b] = sigma, -sigma
    result = tuple(r), shifted(difference, edge_index[(a, b)], sigma)
    check(result)
    return result


def all_births(vector):
    resolved = defaultdict(Counter)
    for state, coefficient in vector.items():
        for a in A:
            for intermediate in outward(state, a):
                for b in nb[a]:
                    for sigma in (-1, 1):
                        result = born(intermediate, a, b, sigma)
                        if result is not None:
                            resolved[(a, b, sigma)][result] += coefficient
    coherent = defaultdict(Counter)
    for (a, b, sigma), vector in resolved.items():
        coherent[(a, b)].update(vector)
    res_norm = sum(c * c for v in resolved.values() for c in v.values())
    coh_norm = sum(c * c for v in coherent.values() for c in v.values())
    assert res_norm == coh_norm
    return resolved, res_norm


def encoded(state, coefficient=1):
    q, difference = state
    return dict(q_changes=[[i, x] for i, x in enumerate(q) if x != q0[i]],
                E_changes=[list(x) for x in difference], coefficient=coefficient)


initial = (q0, ())
check(initial)
birth0, intensity0 = all_births({initial: 1})
assert intensity0 == 0
Qvector = Counter()
pair_rows = []
for a, c in pairs:
    intermediate = Counter(s for t in outward(initial, a) for s in outward(t, c))
    reverse_order = Counter(s for t in outward(initial, c) for s in outward(t, a))
    assert intermediate == reverse_order
    if not intermediate:
        continue
    for state, coefficient in intermediate.items():
        for t in inward(state, c):
            for result in inward(t, a):
                assert all(result[0][x] != 0 for x in A)
                Qvector[result] += coefficient
    pair_rows.append(dict(a=vertices[a], c=vertices[c],
                          overlap=len(set(nb[a]) & set(nb[c])),
                          norm_squared=sum(x * x for x in intermediate.values()),
                          intermediate=[encoded(s, x) for s, x in sorted(intermediate.items())]))
Qexpect = Qvector[initial]
assert Qexpect == sum(x['norm_squared'] for x in pair_rows) > 0
birthQ, intensityQ = all_births(Qvector)
assert intensityQ > 0
electric = sum(E0[k] * (E0[k] - q0[a]) for k, (a, b) in enumerate(edges) if not q0[b])
assert electric >= 0

data = dict(L=L, vertices=vertices, A=A, B=B, edges=edges, q0=q0, E0=E0,
            vacancies=[vertices[b] for b in sorted(holes)],
            active_pairs=pair_rows,
            Q_initial=[encoded(s, c) for s, c in sorted(Qvector.items())],
            B_Q_initial=[dict(channel=[a, b, sigma], output=encoded(s, c))
                         for (a, b, sigma), vec in sorted(birthQ.items())
                         for s, c in sorted(vec.items())])
data_path = HERE / 'DARK_FIXTURE_PATHS.json'
with data_path.open('x') as out:
    json.dump(data, out, separators=(',', ':'))
    out.write('\n')
result = dict(
    control="Independent L6 physical primitive fixture; integer paths and full electric shifts",
    L=L, A_sites=len(A), B_occupied=len(occupied_B), total_charge=sum(q0),
    edges=len(edges), pair_degree=18,
    pair_counts={str(k): v for k, v in sorted(pair_overlaps.items())},
    holes=[vertices[b] for b in sorted(holes)],
    Gauss_checked_unique_states=len(seen_states), initial_electric_D=electric,
    intensity_over_kappa_initial=intensity0, Q_expectation_initial=Qexpect,
    H4_expectation_initial=-2 * Qexpect,
    Q_initial_words=len(Qvector), Q_initial_norm_squared=sum(x * x for x in Qvector.values()),
    B_Q_nonzero_channels=len(birthQ),
    B_Q_output_words=sum(len(vec) for vec in birthQ.values()),
    B_Q_norm_squared_sum=intensityQ,
    sum_L_h_norm_squared_over_kappa_delta_squared=4 * intensityQ,
    original_resolved_and_unnormalized_coherent_intensities_equal=True,
    saturated_sector_formal_check="All B occupied makes each F, S, L and gated D zero, for any Gauss-legal color/field state.",
    data_sha256=hashlib.sha256(data_path.read_bytes()).hexdigest(),
    elapsed_seconds=time.perf_counter() - tic)
with (HERE / 'DARK_FIXTURE_RESULTS.json').open('x') as out:
    json.dump(result, out, indent=2)
    out.write('\n')
print(json.dumps(result, indent=2))
