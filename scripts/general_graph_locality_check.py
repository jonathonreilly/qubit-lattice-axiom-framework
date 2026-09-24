"""Exact rotor path checks of the local compensation on distinct graph families."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/general_graph_locality_check.py',)
from pathlib import Path
from collections import defaultdict
from itertools import combinations
from datetime import datetime, timezone
import hashlib, json, time

HERE = Path(__file__).resolve().parent


def add(v, w, scale=1):
    out = defaultdict(int, v)
    for s, a in w.items():
        out[s] += scale * a
    return {s: a for s, a in out.items() if a}


class Graph:
    def __init__(self, n, edges, aset):
        self.n = n
        self.edges = sorted(tuple(sorted(e)) for e in edges)
        self.aset = set(aset)
        assert len(self.edges) == len(set(self.edges))
        assert all((u in self.aset) != (v in self.aset) for u, v in self.edges)
        self.neighbors = {a: [] for a in range(n)}
        for e, (u, v) in enumerate(self.edges):
            self.neighbors[u].append((v, e))
            self.neighbors[v].append((u, e))
        self.q0 = tuple(int(v in self.aset) for v in range(n))
        self.zero = (0,) * len(self.edges)

    def physical(self, state):
        q, E = state
        div = [0] * self.n
        for x, (u, v) in zip(E, self.edges):
            div[u] += x
            div[v] -= x
        return div == [q[v] - int(v in self.aset) for v in range(self.n)]

    def grade(self, q):
        return sum(q[a] == 0 for a in self.aset)

    def near(self, a, c):
        return bool({b for b, e in self.neighbors[a]} & {b for b, e in self.neighbors[c]})

    def F(self, v, a, outward=True):
        out = defaultdict(int)
        for (q, E), amp in v.items():
            for b, e in self.neighbors[a]:
                origin, dest = (a, b) if outward else (b, a)
                if not q[origin] or q[dest]:
                    continue
                u, w = self.edges[e]
                k = -q[origin] if origin == u else q[origin]
                qq, EE = list(q), list(E)
                qq[dest], qq[origin] = qq[origin], 0
                EE[e] += k
                state = tuple(qq), tuple(EE)
                assert self.physical(state)
                out[state] += amp
        return dict(out)

    def T(self, v, grade):
        out = {}
        for a in self.aset:
            for outward in (False, True):
                for s, amp in self.F(v, a, outward).items():
                    if self.grade(s[0]) == grade:
                        out[s] = out.get(s, 0) - amp
        return {s: a for s, a in out.items() if a}

    def C(self, v):
        out = {}
        for a in self.aset:
            gated = {s: amp for s, amp in v.items()
                     if all(s[0][c] for c in self.aset if c != a and self.near(a, c))}
            out = add(out, self.F(self.F(gated, a), a, False))
        return out

    def M(self, v):
        return self.T(self.T(v, 1), 0)

    def direct_H4_times2(self, v):
        # Literal canonical polynomial; integer factor 2 avoids fractions.
        out = add({}, self.M(self.M(v)), 2)
        out = add(out, self.M(self.C(v)), -1)
        out = add(out, self.C(self.M(v)), -1)
        out = add(out, self.T(self.C(self.T(v, 1)), 0), 2)
        z = v
        for grade in (1, 2, 1, 0):
            z = self.T(z, grade)
        return add(out, z, -1)

    def local_H4_times2(self, v):
        out = {}
        for a, c in combinations(sorted(self.aset), 2):
            if not self.near(a, c):
                continue
            term = self.F(self.F(v, a), c)
            term = self.F(self.F(term, c, False), a, False)
            out = add(out, term, -4)
        return out

    def first_outputs(self):
        seed = {(self.q0, self.zero): 1}
        for e, (u, v) in enumerate(self.edges):
            a = u if u in self.aset else v
            mid = self.F(seed, a)
            for sigma in (-1, 1):
                result = defaultdict(int)
                for (q, E), amp in mid.items():
                    if q[u] or q[v]:
                        continue
                    qq, EE = list(q), list(E)
                    qq[u], qq[v] = sigma, -sigma
                    EE[e] += sigma
                    state = tuple(qq), tuple(EE)
                    assert self.physical(state) and self.grade(qq) == 0
                    result[state] += amp
                if result:
                    yield (e, sigma), dict(result)

    def expected_initial(self):
        seed = (self.q0, self.zero)
        scalar, loops, out = 0, [], {}
        for a, c in combinations(sorted(self.aset), 2):
            common = sorted({b for b, e in self.neighbors[a]} & {b for b, e in self.neighbors[c]})
            if not common:
                continue
            scalar -= 2 * (len(self.neighbors[a]) * len(self.neighbors[c]) - len(common))
            for b, d in combinations(common, 2):
                E = [0] * len(self.edges)
                cycle = [a, b, c, d]
                for u, v in zip(cycle, cycle[1:] + cycle[:1]):
                    edge = tuple(sorted((u, v)))
                    E[self.edges.index(edge)] += 1 if u < v else -1
                loops.append(tuple(E))
                for sign in (-1, 1):
                    s = self.q0, tuple(sign * x for x in E)
                    assert self.physical(s)
                    out[s] = out.get(s, 0) - 4
        out[seed] = 2 * scalar
        return {s: amp for s, amp in out.items() if amp}, scalar, loops


def families():
    yield 'ring8', Graph(8, [(i, (i + 1) % 8) for i in range(8)], range(0, 8, 2))
    yield 'path8', Graph(8, [(i, i + 1) for i in range(7)], range(0, 8, 2))
    yield 'disjoint_two_stars', Graph(6, [(0, 1), (0, 2), (3, 4), (3, 5)], [0, 3])
    for x, y in [(2, 3), (3, 3)]:
        yield f'complete_bipartite_{x}_{y}', Graph(x + y, [(a, x + b) for a in range(x) for b in range(y)], range(x))
    for rows, cols in [(2, 4), (3, 3)]:
        edges, aset = [], []
        for i in range(rows):
            for j in range(cols):
                v = i * cols + j
                if (i + j) % 2 == 0:
                    aset.append(v)
                if i + 1 < rows:
                    edges.append((v, v + cols))
                if j + 1 < cols:
                    edges.append((v, v + 1))
        yield f'open_grid_{rows}_{cols}', Graph(rows * cols, edges, aset)
    for dimension in (3, 4):
        n = 2 ** dimension
        edges = [(v, v ^ (1 << j)) for v in range(n) for j in range(dimension) if v < (v ^ (1 << j))]
        yield f'hypercube_{dimension}', Graph(n, edges, [v for v in range(n) if v.bit_count() % 2 == 0])


def main():
    started = time.monotonic()
    results = []
    for name, g in families():
        seed = {(g.q0, g.zero): 1}
        seeds = [('initial', seed)]
        first = list(g.first_outputs())
        # Distinct actual signs and endpoint neighborhoods; no normalized-state fit.
        indexes = sorted(set([0, 1, max(0, len(first) // 2), max(0, len(first) - 1)]))
        for k in indexes:
            if k < len(first):
                mark, v = first[k]
                seeds.append((f'first_{mark}', v))
        checks = []
        for label, v in seeds:
            assert g.C(v) == g.M(v)
            direct = g.direct_H4_times2(v)
            local = g.local_H4_times2(v)
            assert direct == local, (name, label)
            checks.append({'seed': label, 'input_support': len(v), 'output_support': len(direct),
                           'canonical_equals_local_pair_form_exactly': True})
        expected, scalar, loops = g.expected_initial()
        assert g.direct_H4_times2(seed) == expected
        old_scalar = sum(len(g.neighbors[a]) ** 2 for a in g.aset)
        old_scalar += sum(len(g.neighbors[b]) * (len(g.neighbors[b]) - 1) for b in range(g.n) if b not in g.aset)
        original = add({}, g.M(g.M(seed)), 2)
        z = seed
        for grade in (1, 2, 1, 0):
            z = g.T(z, grade)
        original = add(original, z, -1)
        assert original == add(expected, seed, 2 * (old_scalar - scalar))
        row = {'graph': name, 'vertices': g.n, 'edges': g.edges, 'A': sorted(g.aset),
               'square_count': len(loops), 'initial_compensated_scalar': scalar,
               'initial_original_scalar': old_scalar, 'initial_four_cycle_formula_exact': True,
               'checks': checks}
        results.append(row)
        print(json.dumps({'graph': name, 'squares': len(loops), 'checked_seeds': len(checks), 'scalar': scalar}), flush=True)
    out = {'created_utc': datetime.now(timezone.utc).isoformat(),
           'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started, 'graphs': results,
           'scope': 'Exact integer rotor path controls for finite graph families; analytic identities and any volume theorem require their separate arguments.'}
    path = HERE / 'GENERAL_GRAPH_LOCALITY_RESULTS.json'
    assert not path.exists()
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
