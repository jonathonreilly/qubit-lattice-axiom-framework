"""Sparse exact controls for the actual cubic compensated fast coefficient.

No imports from the author's model/control. Unit rotors and the exact spin-one
weights are separate runs. Geometry is a support check, not a proxy dynamics.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
from collections import defaultdict
from pathlib import Path
from itertools import product
import hashlib
import json
import resource
import time

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME / 'STOP_REQUESTED.json').exists()
assert time.time() < json.loads((RUNTIME / 'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU, (30, 31))
START = time.process_time()
WALL = time.monotonic()


class Cubic:
    def __init__(self, L, spin_one=False):
        self.L, self.spin_one = L, spin_one
        self.sites = list(product(range(L), repeat=3))
        self.A = [v for v in self.sites if sum(v) % 2 == 0]
        self.B = [v for v in self.sites if sum(v) % 2 == 1]
        self.adj = {}
        for v in self.sites:
            self.adj[v] = [tuple((v[j] + (s if j == i else 0)) % L
                                  for j in range(3))
                           for i in range(3) for s in (-1, 1)]
        self.near = {a: set(c for b in self.adj[a] for c in self.adj[b]) - {a}
                     for a in self.A}

    def at(self, v):
        return tuple(x % self.L for x in v)

    @staticmethod
    def default(v):
        return 1 - sum(v) % 2

    def pack(self, q, E):
        return (tuple(sorted((v, c) for v, c in q.items() if c != self.default(v))),
                tuple(sorted((a, b, e) for (a, b), e in E.items() if e)))

    @staticmethod
    def unpack(key):
        return dict(key[0]), {(a, b): e for a, b, e in key[1]}

    def q(self, q, v):
        return q.get(v, self.default(v))

    def edge(self, key, a, b, operation, sign=1):
        q, E = self.unpack(key)
        qa, qb = self.q(q, a), self.q(q, b)
        if operation == 'out':
            if qa == 0 or qb != 0:
                return None
            q[a], q[b], step = 0, qa, -qa
        elif operation == 'in':
            if qa != 0 or qb == 0:
                return None
            q[a], q[b], step = qb, 0, qb
        else:
            assert operation == 'birth'
            if qa != 0 or qb != 0:
                return None
            q[a], q[b], step = sign, -sign, sign
        old = E.get((a, b), 0)
        if self.spin_one and abs(old + step) > 1:
            return None
        E[a, b] = old + step
        return self.pack(q, E)

    def F(self, vector, centers=None, adjoint=False):
        result = defaultdict(int)
        for key, coefficient in vector.items():
            for a in self.A if centers is None else centers:
                for b in self.adj[a]:
                    out = self.edge(key, a, b, 'in' if adjoint else 'out')
                    if out is not None:
                        result[out] += coefficient
        return {s: c for s, c in result.items() if c}

    def J(self, vector, a, b, signs):
        result = defaultdict(int)
        for key, coefficient in vector.items():
            for sign in signs:
                out = self.edge(key, a, b, 'birth', sign)
                if out is not None:
                    result[out] += coefficient
        return dict(result)

    def holes(self, key):
        q, _ = self.unpack(key)
        return [a for a in self.A if self.q(q, a) == 0]

    def NB(self, key):
        q, _ = self.unpack(key)
        return sum(self.q(q, b) != 0 for b in self.B)

    def G(self, key):
        # Exact actual loss: orthogonal final charges make coherent and resolved
        # losses equal. Spin-one allowed link steps have squared weight one.
        return sum(self.edge(key, a, b, 'birth', sign) is not None
                   for a in self.holes(key) for b in self.adj[a] for sign in (-1, 1))

    def gauss(self, key):
        q, E = self.unpack(key)
        divergence = defaultdict(int)
        for (a, b), e in E.items():
            divergence[a] += e
            divergence[b] -= e
        return all(divergence[v] + self.default(v) - self.q(q, v) == 0
                   for v in self.sites)

    def compensation(self, vector):
        result = defaultdict(int)
        for key, coefficient in vector.items():
            q, _ = self.unpack(key)
            for a in self.A:
                if any(self.q(q, c) == 0 for c in self.near[a]):
                    continue
                for out, amplitude in self.F(self.F({key: 1}, [a]), [a], True).items():
                    result[out] += coefficient * amplitude
                if self.spin_one and self.q(q, a) != 0:
                    blocked = sum(self.q(q, b) == 0 and self.edge(key, a, b, 'out') is None
                                  for b in self.adj[a])
                    result[key] += coefficient * blocked
        return {s: c for s, c in result.items() if c}

    def literal_H2(self, vector):
        result = defaultdict(int, self.compensation(vector))
        for out, c in self.F(self.F(vector, adjoint=True)).items():
            result[out] += c
        for out, c in self.F(self.F(vector), adjoint=True).items():
            result[out] -= c
        return {s: c for s, c in result.items() if c}

    def one_hole_local(self, key):
        h, = self.holes(key)
        result = defaultdict(int, self.F(self.F({key: 1}, [h], True), [h]))
        for a in self.near[h]:
            for out, c in self.F(self.F({key: 1}, [a]), [a], True).items():
                result[out] -= c
            for out, c in self.F(self.F({key: 1}, [h], True), [a]).items():
                result[out] += c
            for out, c in self.F(self.F({key: 1}, [a]), [h], True).items():
                result[out] -= c
        if self.spin_one:
            q, _ = self.unpack(key)
            diagonal = 0
            for a in self.A:
                if self.q(q, a) and all(self.q(q, c) for c in self.near[a]):
                    diagonal += sum(self.q(q, b) == 0 and self.edge(key, a, b, 'out') is None
                                    for b in self.adj[a])
            result[key] += diagonal
        return {s: c for s, c in result.items() if c}


rows = []
for spin_one in (False, True):
    model = Cubic(6, spin_one)
    a, c, d = map(model.at, ((0, 0, 0), (1, 1, 0), (1, 0, 1)))
    key = ((), ())
    word = [(c, (1, 0, 0), 'out'), (c, (0, 1, 0), 'birth'),
            (d, (0, 0, 1), 'out'), (d, (2, 0, 1), 'birth'),
            (a, (0, -1, 0), 'out'), (a, (-1, 0, 0), 'birth'),
            (a, (0, 0, -1), 'out')]
    for aa, bb, op in word:
        key = model.edge(key, aa, model.at(bb), op)
        assert key is not None and model.gauss(key)
    assert model.holes(key) == [a] and model.NB(key) == 7 and model.G(key) == 0
    literal, local = model.literal_H2({key: 1}), model.one_hole_local(key)
    assert literal == local
    target = model.edge(model.edge(key, a, (1, 0, 0), 'in'), (2, 0, 0), (1, 0, 0), 'out')
    assert literal[target] == 1 and model.G(target) == 8
    assert all(model.gauss(s) and len(model.holes(s)) == 1 for s in literal)
    rows.append({'carrier': 'spin_one' if spin_one else 'rotor', 'L': 6,
                 'literal_vs_local_H2_exact': True, 'output_words': len(literal),
                 'dark_loss': model.G(key), 'selected_matrix_element': literal[target],
                 'selected_bright_loss': model.G(target)})


dense_rows = []
for spin_one in (False, True):
    model = Cubic(8, spin_one)
    key, births = ((), ()), 0
    # Disjoint B dimers along x. Omit the pair (1,0,0),(3,0,0).
    for y, z in product(range(8), repeat=2):
        parity = (1 - y - z) % 2
        for k in range(2):
            left = ((parity + 4*k) % 8, y, z)
            right = ((parity + 4*k + 2) % 8, y, z)
            center = ((parity + 4*k + 1) % 8, y, z)
            if (left, right) == ((1, 0, 0), (3, 0, 0)):
                continue
            key = model.edge(key, center, left, 'out')
            assert key is not None and model.gauss(key)
            key = model.edge(key, center, right, 'birth')
            assert key is not None and model.gauss(key)
            births += 1
    for aa, bb in (((2, 0, 0), (1, 0, 0)), ((4, 0, 0), (3, 0, 0))):
        key = model.edge(key, aa, bb, 'out')
        assert key is not None and model.gauss(key)
    assert births == 127 and model.NB(key) == len(model.B) and len(model.holes(key)) == 2
    assert model.G(key) == 0 and model.F({key: 1}) == {} and model.compensation({key: 1}) == {}
    Hkey = model.F(model.F({key: 1}, adjoint=True))
    assert all(model.NB(s) == len(model.B) and len(model.holes(s)) == 2
               and model.G(s) == 0 and model.gauss(s) for s in Hkey)
    selected = model.edge(model.edge(key, (2, 0, 0), (1, 0, 0), 'in'),
                          (0, 0, 0), (1, 0, 0), 'out')
    assert Hkey[selected] == 1
    field_edge = ((2, 0, 0), (1, 0, 0))
    assert model.unpack(key)[1][field_edge] == -1
    assert model.unpack(selected)[1].get(field_edge, 0) == 0
    field_projection_norm2 = sum(c*c for s, c in Hkey.items()
                                if model.unpack(s)[1].get(field_edge, 0) == 0)
    refilled = model.F({key: 1}, adjoint=True)
    dressed_first_loss = {}
    for coherent in (False, True):
        total = 0
        for a in model.holes(key):
            for b in model.adj[a]:
                for signs in ((-1, 1),) if coherent else ((-1,), (1,)):
                    output = model.J(refilled, a, b, signs)
                    assert all(len(model.holes(s)) == 0 and model.NB(s) == len(model.B)
                               and model.gauss(s) for s in output)
                    total += sum(c*c for c in output.values())
        dressed_first_loss['coherent' if coherent else 'resolved'] = total
    assert dressed_first_loss == {'coherent': 3 if spin_one else 4,
                                  'resolved': 3 if spin_one else 4}
    dense_rows.append({'carrier': 'spin_one' if spin_one else 'rotor', 'L': 8,
                       'actual_births_in_selected_word': births, 'A_holes': 2,
                       'B_occupied': model.NB(key), 'source_max_abs_E': max(abs(e) for _, _, e in key[1]),
                       'H2_output_words': len(Hkey), 'all_outputs_original_loss_zero': True,
                       'selected_field_matrix_element': Hkey[selected],
                       'first_dressed_jump_loss_in_units_kappa': dressed_first_loss,
                       'bounded_field_projection_second_derivative_in_delta_fast_units': 2*field_projection_norm2})


# Infinite-lattice occupancy support check. Not a field-carrier enumeration.
directions = [tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in (-1, 1)]
plus = lambda a, b: tuple(x+y for x, y in zip(a, b))
neighbors = lambda a: [plus(a, d) for d in directions]
two_step = {plus(d, e) for d in directions for e in directions} - {(0, 0, 0)}
assert len(two_step) == 18
assert sum(len(set(neighbors((0, 0, 0))) & set(neighbors(a))) for a in two_step) == 30
support_rows = []
for m in (1, 2, 3, 4, 8):
    R = 2*m + 3
    reachable = {(0, 0, 0)}
    for k in range(m+1):
        assert all(max(map(abs, h)) + 3 <= R for h in reachable)
        assert all(max(map(abs, b)) <= R for h in reachable for b in neighbors(h))
        if k < m:
            reachable |= {plus(h, d) for h in reachable for d in two_step}
    support_rows.append({'m': m, 'filled_cube_radius': R, 'reachable_hole_centers': len(reachable),
                         'three_neighborhood_contained': True})

result = {'literal_compensation_checks': rows, 'source_accessible_dense_fast_sector': dense_rows,
          'island_support_geometry_only': support_rows,
          'resource_price': {'cpu_cap_seconds': 30, 'rss_cap_bytes': 150*1024**2, 'threads': 1},
          'cpu_seconds': time.process_time()-START, 'wall_seconds': time.monotonic()-WALL,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['peak_rss_bytes'] < 150*1024**2
(HERE / 'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
