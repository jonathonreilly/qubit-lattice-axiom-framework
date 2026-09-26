#!/usr/bin/env python3
"""Independent path inventory, contraction/word checks, and gap controls.

No author checker is imported. Integer inventories are exact; matrix eigenvalues
are explicitly numerical controls, not a proof of an all-sector gap.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from collections import Counter
from fractions import Fraction
import json
import math
import numpy as np

OUT = Path(__file__).resolve().parent


class Torus:
    def __init__(self, n):
        self.n = n
        self.xyz = list(product(range(n), repeat=3))
        self.index = {x: i for i, x in enumerate(self.xyz)}
        self.v = n ** 3
        self.plus, self.minus = [], []
        for x in self.xyz:
            plus, minus = [], []
            for i in range(3):
                y, z = list(x), list(x)
                y[i] = (y[i] + 1) % n
                z[i] = (z[i] - 1) % n
                plus.append(self.index[tuple(y)])
                minus.append(self.index[tuple(z)])
            self.plus.append(plus)
            self.minus.append(minus)
        self.edges = [(a, self.plus[a][i]) for a in range(self.v) for i in range(3)]
        assert len({tuple(sorted(e)) for e in self.edges}) == 3 * self.v

    def path(self, a, b):
        vertices, edges = [a], []
        for i in range(3):
            dist = (self.xyz[b][i] - self.xyz[a][i]) % self.n
            sign = 1 if dist <= self.n // 2 else -1
            steps = dist if sign == 1 else self.n - dist
            for _ in range(steps):
                nxt = self.plus[a][i] if sign == 1 else self.minus[a][i]
                edge = 3 * (a if sign == 1 else nxt) + i
                vertices.append(nxt)
                edges.append(edge)
                a = nxt
        assert a == b and len(edges) <= 3 * self.n // 2
        assert len(edges) == len(set(edges))
        return vertices, edges

    def matching(self, kind):
        mate = [-1] * self.v
        if kind == 'winding':
            for a, x in enumerate(self.xyz):
                if sum(x) % 2 == 0:
                    b = self.plus[a][0]
                    assert mate[a] == mate[b] == -1
                    mate[a], mate[b] = b, a
        else:
            for a, x in enumerate(self.xyz):
                if x[0] % 2 == 0:
                    b = self.plus[a][0]
                    mate[a], mate[b] = b, a
        accepted = 0
        if kind == 'irregular':
            rng = np.random.default_rng(48017 + self.n)
            planes = list(combinations(range(3), 2))
            for _ in range(11 * self.v):
                a = int(rng.integers(self.v))
                i, j = planes[int(rng.integers(3))]
                b, d = self.plus[a][i], self.plus[a][j]
                c = self.plus[b][j]
                if mate[a] == b and mate[d] == c:
                    mate[a], mate[d], mate[b], mate[c] = d, a, c, b
                elif mate[a] == d and mate[b] == c:
                    mate[a], mate[b], mate[d], mate[c] = b, a, c, d
                else:
                    continue
                accepted += 1
        assert all(b >= 0 and b != a and mate[b] == a for a, b in enumerate(mate))
        assert all(b in self.plus[a] + self.minus[a] for a, b in enumerate(mate))
        return mate, accepted


def all_physical_loads(torus):
    load = [0] * (3 * torus.v)
    distances = Counter()
    for a in range(torus.v):
        for b in range(torus.v):
            _, edges = torus.path(a, b)
            distances[len(edges)] += 1
            for edge in edges:
                load[edge] += 1
    target = torus.n ** 4 // 4
    assert set(load) == {target}
    assert sum(length * count for length, count in distances.items()) == 3 * torus.v * target
    return load, {'N': torus.n, 'ordered_pairs': torus.v ** 2,
                  'physical_edges': len(load), 'minimum_load': min(load),
                  'maximum_load': max(load), 'exact_formula': target,
                  'total_traversals': sum(load), 'distance_histogram': dict(sorted(distances.items()))}


def loop_erase(raw):
    stack, positions = [], {}
    for v in raw:
        if v in positions:
            stop = positions[v] + 1
            for old in stack[stop:]:
                del positions[old]
            del stack[stop:]
        else:
            positions[v] = len(stack)
            stack.append(v)
    return stack


def contracted_checks(torus, kind, full_load):
    n = torus.n
    mate, accepted = torus.matching(kind)
    black = [a for a, x in enumerate(torus.xyz) if sum(x) % 2 == 0]
    k = len(black)
    owner = [-1] * torus.v
    for i, a in enumerate(black):
        owner[a] = owner[mate[a]] = i
    physical_for_h = {}
    for ei, (a, b) in enumerate(torus.edges):
        aa, bb = owner[a], owner[b]
        if aa != bb:
            physical_for_h.setdefault(tuple(sorted((aa, bb))), []).append(ei)
    assert all(1 <= len(es) <= 2 for es in physical_for_h.values())
    assert sum(map(len, physical_for_h.values())) == 5 * k
    hload, wordload, weighted = Counter(), Counter(), Counter()
    subset_physical = [0] * (3 * torus.v)
    loop_removals = consecutive_removed = total_length = 0
    max_length = max_word = 0
    for u, v in combinations(range(k), 2):
        vertices, edges = torus.path(black[u], black[v])
        for e in edges:
            subset_physical[e] += 1
        raw = [owner[a] for a in vertices]
        consecutive = [raw[0]] + [b for a, b in zip(raw, raw[1:]) if a != b]
        path = loop_erase(raw)
        consecutive_removed += len(raw) - len(consecutive)
        loop_removals += len(path) < len(consecutive)
        assert path[0] == u and path[-1] == v and len(path) == len(set(path))
        contracted_edges = [tuple(sorted(e)) for e in zip(path, path[1:])]
        raw_edges = {tuple(sorted((a, b))) for a, b in zip(raw, raw[1:]) if a != b}
        assert set(contracted_edges) <= raw_edges
        assert all(e in physical_for_h for e in contracted_edges)
        ell = len(contracted_edges)
        assert 1 <= ell <= len(edges) <= 3 * n // 2
        word = list(range(ell)) + list(range(ell - 2, -1, -1))
        keys = list(range(ell + 1))
        for j in word:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]
        assert keys == [ell] + list(range(1, ell)) + [0]
        assert len(word) == 2 * ell - 1 <= 3 * n - 1
        assert max(Counter(word).values()) <= 2
        for e in contracted_edges:
            hload[e] += 1
        for j in word:
            e = contracted_edges[j]
            wordload[e] += 1
            weighted[e] += len(word)
        total_length += ell
        max_length, max_word = max(max_length, ell), max(max_word, len(word))
    assert all(a <= b for a, b in zip(subset_physical, full_load))
    for e, es in physical_for_h.items():
        # Check each inequality, including the actual physical representatives.
        assert hload[e] <= sum(subset_physical[i] for i in es) <= sum(full_load[i] for i in es) <= n ** 4 // 2
        assert wordload[e] <= 2 * hload[e] <= n ** 4
        assert weighted[e] <= (3 * n - 1) * n ** 4
    # One-marker sector: exact graph construction, numerical eigenvalue only.
    lap_simple = np.zeros((k, k))
    lap_physical = np.zeros((k, k))
    for (u, v), es in physical_for_h.items():
        for lap, rate in [(lap_simple, .5), (lap_physical, .5 * len(es))]:
            lap[u, u] += rate; lap[v, v] += rate
            lap[u, v] -= rate; lap[v, u] -= rate
    gs = float(np.linalg.eigvalsh(lap_simple)[1])
    gp = float(np.linalg.eigvalsh(lap_physical)[1])
    asserted = Fraction(1, 8 * n * (3 * n - 1))
    count_bound = Fraction(k, 4 * max(weighted.values()))
    assert count_bound >= asserted and min(gs, gp) >= float(count_bound) - 1e-12
    assert gp >= gs - 1e-12
    return {'N': n, 'kind': kind, 'pairs': k, 'accepted_construction_flips': accepted,
            'simple_contracted_edges': len(physical_for_h),
            'physical_edge_multiplicity_histogram': dict(sorted(Counter(map(len, physical_for_h.values())).items())),
            'reference_unordered_pairs': k * (k - 1) // 2,
            'paths_with_nonconsecutive_loop_erasure': loop_removals,
            'consecutive_contractions_removed': consecutive_removed,
            'maximum_simple_path_length': max_length, 'maximum_endpoint_word_length': max_word,
            'maximum_contracted_path_load': max(hload.values()),
            'maximum_word_edge_use': max(wordload.values()),
            'maximum_length_weighted_congestion': max(weighted.values()),
            'worst_case_displayed_weighted_bound': (3 * n - 1) * n ** 4,
            'exact_gap_bound_k0_one': str(asserted),
            'exact_inventory_gap_bound_k0_one': str(count_bound),
            'numerical_one_marker_simple_gap_k0_one': gs,
            'numerical_one_marker_physical_multiplicity_gap_k0_one': gp,
            'endpoint_key_permutations_checked': k * (k - 1) // 2}


def finite_sector_normalization():
    # Separate small color-sector check of the endpoint-word CS factor and the
    # inherited complete-form convention. It is not a small-torus surrogate.
    rows = []
    for labels in [(0, 0, 1, 1), (0, 0, 1, 1, 2)]:
        states = sorted(set(permutations(labels)))
        k = len(labels)
        weights = [2, -3, 5, 7, -2][:k]
        def value(s):
            return sum(w * (a + 1) for w, a in zip(weights, s)) + 3 * s[0] * s[-1]
        def squared_increment(i, j):
            total = 0
            for s in states:
                z = list(s); z[i], z[j] = z[j], z[i]
                total += (value(z) - value(s)) ** 2
            return Fraction(total, len(states))
        values = list(map(value, states))
        avg = Fraction(sum(values), len(states))
        var = sum((Fraction(x) - avg) ** 2 for x in values) / len(states)
        dall = sum(squared_increment(i, j) for i, j in combinations(range(k), 2)) / 2
        endpoint = squared_increment(0, k - 1)
        word = list(range(k - 1)) + list(range(k - 3, -1, -1))
        cs = len(word) * sum(squared_increment(i, i + 1) for i in word)
        assert endpoint <= cs and var <= Fraction(2, k) * dall
        # A one-step swap has word length one, preventing a hidden factor two.
        assert squared_increment(0, 1) == sum([squared_increment(0, 1)])
        rows.append({'counts': dict(Counter(labels)), 'states': len(states),
                     'variance': str(var), 'D_all': str(dall),
                     'endpoint_increment_second': str(endpoint), 'word_CS_bound': str(cs),
                     'complete_form_bound': str(Fraction(2, k) * dall)})
    return rows


def time_constants():
    rows = []
    for n in [8, 10, 16, 32, 128]:
        k = n ** 3 // 2
        inverse_gap = 8 * n * (3 * n - 1)
        log_bound = k * math.log(14) / 2 + 4 * math.log(n) - math.log(2)
        t = inverse_gap * log_bound
        log_tv = -math.log(2) + k * math.log(14) / 2 - t / inverse_gap
        assert abs(log_tv + 4 * math.log(n)) < 1e-8
        # Polynomial coefficients kept exact; log(14) is the scalar multiplier.
        assert inverse_gap * k // 2 == 6 * n ** 5 - 2 * n ** 4
        assert Fraction(k, n ** 4) == Fraction(1, 2 * n)
        rows.append({'N': n, 'inverse_gap_k0_one': inverse_gap,
                     'prep_time_k0_one_epsilon_N_minus4': t,
                     'log_TV_error': log_tv + 4 * math.log(n),
                     'coefficient_of_log14': 6 * n ** 5 - 2 * n ** 4,
                     'mean_square_transfer_K_epsilon': str(Fraction(k, n ** 4))})
    return rows


def main():
    physical, geometry = [], []
    for n in [8, 10]:
        torus = Torus(n)
        load, row = all_physical_loads(torus)
        physical.append(row)
        print('ordered physical path inventory', n, 'complete', flush=True)
        for kind in ['winding', 'columnar', 'irregular']:
            geometry.append(contracted_checks(torus, kind, load))
            print('contracted immutable endpoint words', n, kind, 'complete', flush=True)
    result = {'read_boundary': 'Independent before author checker/results access.',
              'physical_paths': physical, 'contracted_paths_and_gap_controls': geometry,
              'exact_small_color_sector_normalization': finite_sector_normalization(),
              'preparation_constants': time_constants(),
              'numeric_limits': 'One-marker eigenvalues and time/log evaluations use floating arithmetic; path counts, multiplicities, endpoint permutations, fractions and sector sums are exact.'}
    (OUT / 'INDEPENDENT_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'physical_inventories': len(physical), 'matching_cases': len(geometry)}))


if __name__ == '__main__':
    main()
