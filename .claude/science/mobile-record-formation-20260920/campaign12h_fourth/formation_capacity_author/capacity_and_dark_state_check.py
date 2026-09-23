"""Exact root controls from elementary rotor paths; no prior builder imports.

K=delta=kappa=1 in coefficient readouts. F is unsigned outward hopping;
B=+PjF is the common channel-phase convention, equivalent to -PjF.
This is finite algebra, not a long-time simulation or a volume proof.
"""
from pathlib import Path
from itertools import product, combinations
from collections import defaultdict, deque
from fractions import Fraction
import hashlib, json, time

HERE = Path(__file__).resolve().parent


class Graph:
    def __init__(self, coords, edges):
        self.coords = tuple(coords)
        self.edges = tuple(edges)
        self.n = len(coords)
        self.A = tuple(i for i, x in enumerate(coords) if sum(x) % 2 == 0)
        self.B = tuple(i for i in range(self.n) if i not in self.A)
        self.adj = defaultdict(list)
        for e, (u, v) in enumerate(edges):
            assert (u in self.A) != (v in self.A)
            self.adj[u].append((v, e, 1))
            self.adj[v].append((u, e, -1))
        self.pairs = tuple(sorted({tuple(sorted((a, c))) for b in self.B
                                   for (a, _, _), (c, _, _) in combinations(self.adj[b], 2)}))

    def gauss(self, state):
        q, field = state
        div = [0]*self.n
        for E, (u, v) in zip(field, self.edges):
            div[u] += E
            div[v] -= E
        return all(div[i] == q[i]-int(i in self.A) for i in range(self.n))

    def flow(self, q):
        charge = [q[i]-int(i in self.A) for i in range(self.n)]
        assert sum(charge) == 0
        parent = {0: None}
        order = [0]
        for v in order:
            for w, e, orient in self.adj[v]:
                if w not in parent:
                    parent[w] = (v, e, -orient)
                    order.append(w)
        assert len(order) == self.n
        fields = [0]*len(self.edges)
        for v in reversed(order[1:]):
            p, e, outsign = parent[v]
            fields[e] = outsign*charge[v]
            charge[p] += charge[v]
        state = (tuple(q), tuple(fields))
        assert self.gauss(state)
        return state

    def hop(self, state, a, reverse=False):
        q0, f0 = state
        out = {}
        for b, e, orient in self.adj[a]:
            if reverse:
                if q0[a] or not q0[b]:
                    continue
                charge = q0[b]
            else:
                if not q0[a] or q0[b]:
                    continue
                charge = q0[a]
            q, f = list(q0), list(f0)
            q[a], q[b] = (charge, 0) if reverse else (0, charge)
            f[e] += orient*charge*(1 if reverse else -1)
            key = (tuple(q), tuple(f))
            out[key] = out.get(key, 0)+1
        return out

    def birth(self, state, e, sigma, reverse=False):
        q0, f0 = state
        u, v = self.edges[e]
        a, b, orient = (u, v, 1) if u in self.A else (v, u, -1)
        if reverse:
            if (q0[a], q0[b]) != (sigma, -sigma):
                return {}
        elif q0[a] or q0[b]:
            return {}
        q, f = list(q0), list(f0)
        q[a], q[b] = (0, 0) if reverse else (sigma, -sigma)
        f[e] += orient*sigma*(-1 if reverse else 1)
        return {(tuple(q), tuple(f)): 1}

    def jump(self, state, e, sigma, adjoint=False):
        a = next(v for v in self.edges[e] if v in self.A)
        if adjoint:
            return apply(lambda s: self.hop(s, a, True), self.birth(state, e, sigma, True))
        return apply(lambda s: self.birth(s, e, sigma), self.hop(state, a))

    def magnetic(self, state):
        out = defaultdict(int)
        for a, c in self.pairs:
            v = apply(lambda s: self.hop(s, c), self.hop(state, a))
            v = apply(lambda s: self.hop(s, c, True), v)
            v = apply(lambda s: self.hop(s, a, True), v)
            for s, amp in v.items():
                out[s] -= 2*amp
        return {s: v for s, v in out.items() if v}

    def electric(self, state):
        q, field = state
        out = 0
        for E, (u, v) in zip(field, self.edges):
            a, b, orient = (u, v, 1) if u in self.A else (v, u, -1)
            if not q[b]:
                out += E*(E-orient*q[a])
        assert out >= 0
        return out


def apply(operator, vector):
    out = defaultdict(int)
    for state, amp in vector.items():
        for new, coefficient in operator(state).items():
            out[new] += amp*coefficient
    return {s: a for s, a in out.items() if a}


def norm2(vector):
    return sum(a*a for a in vector.values())


def number(state):
    return sum(q != 0 for q in state[0])


def box(d, L, periodic=False):
    coords = tuple(product(range(L), repeat=d))
    index = {x: i for i, x in enumerate(coords)}
    edges = []
    for v, x in enumerate(coords):
        for axis in range(d):
            if x[axis]+1 == L and not periodic:
                continue
            y = tuple((a+int(i == axis)) % L for i, a in enumerate(x))
            edges.append((v, index[y]))
    return Graph(coords, edges)


def all_physical_words(g):
    for aa in product((-1, 1), repeat=len(g.A)):
        for bb in product((-1, 0, 1), repeat=len(g.B)):
            q = [0]*g.n
            for i, value in zip(g.A, aa):
                q[i] = value
            for i, value in zip(g.B, bb):
                q[i] = value
            if sum(q) == len(g.A):
                yield g.flow(q)


def finite_balance(g, label):
    seeds = channels = outputs = 0
    numbers = defaultdict(int)
    for state in all_physical_words(g):
        seeds += 1
        N = number(state)
        numbers[N] += 1
        h = g.magnetic(state)
        assert all(number(s) == N and g.gauss(s) for s in h)
        g.electric(state)
        gamma = defaultdict(int)
        lhs_twice = defaultdict(int)
        for e in range(len(g.edges)):
            for sigma in (-1, 1):
                v = g.jump(state, e, sigma)
                assert all(number(s) == N+2 and g.gauss(s) for s in v)
                vv = apply(lambda s: g.jump(s, e, sigma, True), v)
                middle = apply(lambda s: g.jump(s, e, sigma, True),
                               {s: number(s)*a for s, a in v.items()})
                assert all(number(s) == N and g.gauss(s) for s in vv)
                assert vv.get(state, 0) == norm2(v)
                for s, a in vv.items():
                    gamma[s] += a
                    lhs_twice[s] -= (N+number(s))*a
                for s, a in middle.items():
                    lhs_twice[s] += 2*a
                channels += 1
                outputs += len(v)
        assert {s: a for s, a in lhs_twice.items() if a} == {s: 4*a for s, a in gamma.items() if a}
    return {'graph': label, 'vertices': g.n, 'edges': len(g.edges),
            'complete_Gauss_matter_words': seeds, 'number_sector_counts': dict(numbers),
            'jump_columns_checked': channels, 'legal_jump_outputs': outputs,
            'Hamiltonian_number_commutator_zero': True,
            'twice_generator_N_equals_four_Gamma': True,
            'scope': 'All allowed charge words with one exact spanning-tree Gauss field each; no claim of exhaustive electric-field testing. General identities are analytic.'}


def dark_word(d, vacancies):
    g = box(d, 6, True)
    index = {x: i for i, x in enumerate(g.coords)}
    holes = {index[x] for x in vacancies}
    assert holes <= set(g.B)
    occupied = sorted(set(g.B)-holes)
    assert len(occupied) % 2 == 0
    q = [int(v in g.A) for v in range(g.n)]
    for i, b in enumerate(occupied):
        q[b] = 1 if i < len(occupied)//2 else -1
    return g, g.flow(q), holes


def periodic_stationary(d):
    holes = [(1,)+(0,)*(d-1), (4, 3)+(0,)*(d-2)]
    g, state, hole_ids = dark_word(d, holes)
    distances = []
    for x in holes:
        for y in holes:
            for shift in product((-1, 0, 1), repeat=d):
                if x == y and not any(shift):
                    continue
                distances.append(sum(abs(a-b-6*s) for a, b, s in zip(x, y, shift)))
    assert min(distances) == 6
    vacant = {a: {b for b, _, _ in g.adj[a] if b in hole_ids} for a in g.A}
    birth_paths = sum(len(v)*(len(v)-1) for v in vacant.values())
    pair_paths = sum(sum(b != e for b in vacant[a] for e in vacant[c]) for a, c in g.pairs)
    assert birth_paths == pair_paths == 0
    assert g.gauss(state)
    return {'d': d, 'period': 6, 'vertices': g.n, 'edges': len(g.edges),
            'vacancies': holes, 'minimum_lifted_vacancy_distance': min(distances),
            'overlapping_A_pairs_checked': len(g.pairs), 'outward_pair_paths': pair_paths,
            'first_birth_paths': birth_paths, 'all_Gauss_constraints': True,
            'density_exact': str(Fraction(number(state), g.n)),
            'electric_D_per_cell': g.electric(state), 'largest_absolute_electric_field': max(map(abs, state[1])),
            'finite_electric_second_moment_per_vertex': str(Fraction(sum(e*e for e in state[1]), g.n)),
            'stationarity_reason': 'Every S_ac and jump annihilates this basis word, while electric H is diagonal.',
            'charge_word': state[0], 'integer_Gauss_field': state[1]}


def reactivation():
    g, state, holes = dark_word(2, [(5, 0), (2, 1)])
    assert all(not g.jump(state, e, sigma) for e in range(len(g.edges)) for sigma in (-1, 1))
    h = g.magnetic(state)
    assert all(g.gauss(s) and number(s) == number(state) for s in h)
    rows = []
    resolved = coherent = 0
    for e in range(len(g.edges)):
        pair = []
        for sigma in (-1, 1):
            v = apply(lambda s: g.jump(s, e, sigma), h)
            assert all(g.gauss(s) and number(s) == number(state)+2 for s in v)
            weight = norm2(v)
            resolved += weight
            pair.append(v)
            if weight:
                rows.append({'oriented_edge': [g.coords[x] for x in g.edges[e]],
                             'sigma': sigma, 'squared_norm_L_H_psi': weight,
                             'output_words': len(v)})
        combined = defaultdict(int, pair[0])
        for s, a in pair[1].items():
            combined[s] += a
        coherent += norm2(combined)
    assert resolved == coherent and resolved > 0
    return {'period': 6, 'd': 2, 'vacancies': [(5, 0), (2, 1)],
            'initial_all_channel_intensities_zero': True,
            'initial_density': str(Fraction(number(state), g.n)),
            'H_magnetic_output_words': len(h), 'H_magnetic_norm_squared': norm2(h),
            'sum_squared_norm_L_H_psi_over_kappa_delta_squared': resolved,
            'first_birth_t_cubed_coefficient_over_kappa_delta_squared': str(Fraction(resolved, 3)),
            'coherent_and_resolved_coefficients_equal': True, 'nonzero_channels': rows,
            'scope': 'Exact finite torus fixture and analytic short-time coefficient, not a time-evolution fit or a stationary-state accessibility theorem.'}


def main():
    started = time.monotonic()
    cube = box(3, 2)
    path = Graph([(i,) for i in range(8)], [(i, i+1) for i in range(7)])
    ring = Graph([(i,) for i in range(8)], [(i, (i+1) % 8) for i in range(8)])
    balances = [finite_balance(g, label) for g, label in [(path, 'path8'), (ring, 'ring8'), (cube, 'cubeQ3')]]
    stationary = [periodic_stationary(d) for d in (2, 3, 4)]
    active = reactivation()
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'finite_number_balance': balances, 'periodic_stationary_controls': stationary,
              'motion_reactivation': active, 'elapsed_seconds': time.monotonic()-started,
              'scope': 'Exact elementary rotor-path and integer-flow controls. No inherited builder, floating algebra, dynamical fit, relaxation proof or numerical volume proof.'}
    target = HERE/'CAPACITY_CONTROL_RESULTS.json'
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'periodic_stationary_controls'}, indent=2), flush=True)
    print(json.dumps({'stationary_summaries': [{k: v for k, v in row.items() if k not in ('charge_word', 'integer_Gauss_field')}
                                               for row in stationary]}, indent=2), flush=True)


if __name__ == '__main__':
    main()
