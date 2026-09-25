#!/usr/bin/env python3
"""Own released-source POST computation; inputs read-only, new reports written.

No author code is imported/executed. Uses full charge tuples and the blind PRE
star-loss identity, unlike the author's explicit forward/adjoint birth loop.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / 'post_sources' / 'author'
tic = time.perf_counter()
sha = lambda raw: hashlib.sha256(raw).hexdigest()
read = lambda name: json.loads((AUTHOR / name).read_text())
sealed = read('AUTHOR_SEAL.json')
for member in sealed['members']:
    raw = (AUTHOR / member['path']).read_bytes()
    assert len(raw) == member['bytes'] and sha(raw) == member['sha256']
execution = read('EXECUTION_ATTEMPT01.json')
assert execution['exit_code'] == 0
assert sha((AUTHOR / 'primitive_rate_energy_controls.py').read_bytes()) == execution['code_sha256']
for stream in ('stdout', 'stderr'):
    raw = (AUTHOR / ('CONTROL_ATTEMPT01.' + stream)).read_bytes()
    assert len(raw) == execution[stream + '_bytes'] and sha(raw) == execution[stream + '_sha256']
assert execution['stderr_bytes'] == 0
result = read('PRIMITIVE_RATE_ENERGY_RESULTS.json')
stdout = read('CONTROL_ATTEMPT01.stdout')
assert result['source_sha256'] == execution['code_sha256']
assert stdout['complete_result_sha256'] == sha((AUTHOR / 'PRIMITIVE_RATE_ENERGY_RESULTS.json').read_bytes())
assert {k: v for k, v in result.items() if k != 'columns'} == {
    k: v for k, v in stdout.items() if k not in ('rows', 'complete_result_sha256')}
assert stdout['rows'] == [{k: v for k, v in row.items() if k not in
                          ('initial_charge_word', 'one_exact_Gauss_flow', 'complete_affine_columns')}
                         for row in result['columns']]


class Primitive:
    """Generalize the own PRE full-word paths to cube and side-six inputs."""
    def __init__(self, side):
        self.side = side
        self.vertices = list(product(range(side), repeat=3))
        self.index = {x: i for i, x in enumerate(self.vertices)}
        self.A = [i for i, x in enumerate(self.vertices) if sum(x) % 2 == 0]
        self.Aset = set(self.A)
        self.B = [i for i in range(len(self.vertices)) if i not in self.Aset]
        self.nb = {}
        for i, x in enumerate(self.vertices):
            targets = set()
            for axis in range(3):
                for step in (-1, 1):
                    y = list(x)
                    y[axis] = (y[axis] + step) % side
                    targets.add(self.index[tuple(y)])
            self.nb[i] = sorted(targets)
        self.edges = [(a, b) for a in self.A for b in self.nb[a]]
        self.eid = {edge: k for k, edge in enumerate(self.edges)}
        self.pairs = [(a, c) for i, a in enumerate(self.A) for c in self.A[i + 1:]
                      if set(self.nb[a]) & set(self.nb[c])]
        self.degree = len(self.nb[0])
        assert all(len(v) == self.degree for v in self.nb.values())
        assert max(len(set(self.nb[a]) & set(self.nb[c])) for a, c in self.pairs) == 2

    @staticmethod
    def shifted(flow, edge, amount):
        data = dict(flow)
        data[edge] = data.get(edge, 0) + amount
        return tuple(sorted((k, x) for k, x in data.items() if x))

    def hop(self, state, a, reverse=False):
        q, flow = state
        if bool(q[a]) == reverse:
            return
        for b in self.nb[a]:
            if bool(q[b]) != reverse:
                continue
            charge = q[b] if reverse else q[a]
            r = list(q)
            r[a], r[b] = (charge, 0) if reverse else (0, charge)
            yield tuple(r), self.shifted(flow, self.eid[(a, b)], charge if reverse else -charge)

    def column(self, q):
        start = tuple(q), ()
        outward = {a: list(self.hop(start, a)) for a in self.A}
        Gamma, Q = Counter(), Counter()
        # Own PRE identity: Gamma_a = 2 F_a* v_intermediate F_a,
        # kappa=1. No original author birth/adjoint code is reused.
        for a in self.A:
            for middle in outward[a]:
                factor = 2 * sum(middle[0][b] == 0 for b in self.nb[a])
                if factor:
                    for target in self.hop(middle, a, reverse=True):
                        Gamma[target] += factor
        for a, c in self.pairs:
            for first in outward[a]:
                for second in self.hop(first, c):
                    for third in self.hop(second, c, reverse=True):
                        for target in self.hop(third, a, reverse=True):
                            Q[target] += 1
        return Gamma, Q

    def validate_gauss(self, q, electric):
        div = [0] * len(q)
        for (a, b), e in zip(self.edges, electric):
            assert type(e) is int
            div[a] += e
            div[b] -= e
        assert div == [x - int(i in self.Aset) for i, x in enumerate(q)]

    def electric_D(self, q, electric):
        return sum(e * (e - q[a]) for (a, b), e in zip(self.edges, electric) if not q[b])


graphs = {side: Primitive(side) for side in (2, 6)}
expected_cube = set()
cube = graphs[2]
for m in (0, 2, 4):
    for occupied in combinations(cube.B, m):
        sites = cube.A + list(occupied)
        for minus in combinations(sites, m // 2):
            expected_cube.add(tuple(-1 if i in minus else int(i in sites)
                                    for i in range(len(cube.vertices))))
observed_cube = {tuple(row['initial_charge_word']) for row in result['columns'] if row['side'] == 2}
assert expected_cube == observed_cube and len(expected_cube) == 65
assert len(result['columns']) == 72
summaries = []
total_entries = 0
normalized_coherent_wrong_entries = 0
cached_cube = {}
for row_number, row in enumerate(result['columns']):
    graph = graphs[row['side']]
    q = tuple(row['initial_charge_word'])
    assert all(q[a] for a in graph.A) and sum(q) == len(graph.A)
    m = sum(bool(q[b]) for b in graph.B)
    assert m == row['B_occupied'] and q.count(-1) == row['minus_charges'] == m // 2
    graph.validate_gauss(q, row['one_exact_Gauss_flow'])
    actual_Gamma, actual_Q = graph.column(q)
    if row['side'] == 2:
        cached_cube[q] = actual_Gamma, actual_Q
    stored_Gamma, stored_Q = {}, {}
    payload = row['complete_affine_columns']
    assert sha(json.dumps(payload, separators=(',', ':')).encode()) == row['complete_affine_columns_sha256']
    for charges, flow, gamma, magnetic in payload:
        r = list(q)
        for i, value in charges:
            assert value in (-1, 0, 1) and value != q[i]
            r[i] = value
        key = tuple(r), tuple(tuple(x) for x in flow)
        assert key not in stored_Gamma and key not in stored_Q
        assert type(gamma) is int and type(magnetic) is int and gamma >= 0 and magnetic >= 0
        assert all(r[a] for a in graph.A)
        assert sum(bool(x) for x in r) == len(graph.A) + m
        residual = [q[i] - r[i] for i in range(len(q))]
        for k, e in flow:
            a, b = graph.edges[k]
            residual[a] += e
            residual[b] -= e
        assert not any(residual)
        stored_Gamma[key] = gamma
        stored_Q[key] = magnetic
        assert (graph.degree - 1) * gamma <= 8 * magnetic
        if gamma:
            normalized_coherent_wrong_entries += 1
    assert {k: v for k, v in stored_Gamma.items() if v} == dict(actual_Gamma)
    assert {k: v for k, v in stored_Q.items() if v} == dict(actual_Q)
    own_payload = []
    for key in sorted(set(actual_Gamma) | set(actual_Q), key=lambda key:
                      (tuple((i, v) for i, v in enumerate(key[0]) if v != q[i]), key[1])):
        r, flow = key
        own_payload.append([[[i, v] for i, v in enumerate(r) if v != q[i]],
                            [list(x) for x in flow], actual_Gamma[key], actual_Q[key]])
    assert own_payload == payload
    vacancies = [sum(q[b] == 0 for b in graph.nb[a]) for a in graph.A]
    diagonal = 2 * sum(v * (v - 1) for v in vacancies)
    assert sum(vacancies) == graph.degree * (len(graph.B) - m)
    assert diagonal == row['Gamma_diagonal'] == actual_Gamma[(q, ())]
    assert diagonal >= 4 * (graph.degree * (len(graph.B) - m) - len(graph.A))
    assert actual_Q[(q, ())] == row['Q_diagonal']
    assert len(actual_Gamma) == row['Gamma_nonzero_entries']
    assert len(actual_Q) == row['Q_nonzero_entries']
    ratios = [Fraction(value, actual_Q[key]) for key, value in actual_Gamma.items() if key != (q, ())]
    ratio = str(max(ratios)) if ratios else None
    assert ratio == row['maximum_offdiagonal_Gamma_over_Q']
    summaries.append(dict(row=row_number, label=row['label'], side=row['side'], m=m,
                          minus=q.count(-1), Gamma_diagonal=diagonal,
                          Q_diagonal=actual_Q[(q, ())], Q_row_sum=sum(actual_Q.values()),
                          Gamma_entries=len(actual_Gamma), Q_entries=len(actual_Q),
                          union_entries=len(payload), max_offdiag_ratio=ratio,
                          own_affine_sha256=sha(json.dumps(own_payload, separators=(',', ':')).encode()),
                          full_payload_equal=True))
    total_entries += len(payload)
assert total_entries == 43970

# Bounded phase test on actual finite-electric physical cube vectors. This is
# a post-release test of the phase mechanism, not a new blind reconstruction.
seed_row = next(row for row in result['columns'] if row['side'] == 2 and row['B_occupied'] == 2)
qseed = tuple(seed_row['initial_charge_word'])
gseed, qseed_column = cached_cube[qseed]
support = [(qseed, ())] + [key for key in sorted(gseed) if key != (qseed, ())][:15]
dimension = len(support)
support_index = {key: i for i, key in enumerate(support)}
Qmat = [[0] * dimension for _ in support]
Gmat = [[0] * dimension for _ in support]
Ddiag = []
for j, (q, base_flow) in enumerate(support):
    Gamma, Q = cached_cube[q]
    electric = seed_row['one_exact_Gauss_flow'].copy()
    for k, e in base_flow:
        electric[k] += e
    cube.validate_gauss(q, electric)
    Ddiag.append(cube.electric_D(q, electric))
    for source, matrix in ((Gamma, Gmat), (Q, Qmat)):
        for (r, delta), value in source.items():
            final_flow = base_flow
            for k, e in delta:
                final_flow = cube.shifted(final_flow, k, e)
            i = support_index.get((r, final_flow))
            if i is not None:
                matrix[i][j] += value
assert all(Qmat[i][j] == Qmat[j][i] and Gmat[i][j] == Gmat[j][i]
           for i in range(dimension) for j in range(dimension))
phase_rows = []
for mode in range(4):
    z = []
    for i in range(dimension):
        amplitude = 1 + ((i + mode) % 2)
        if mode == 0:
            z.append((amplitude, 0))
        elif mode == 1:
            z.append((amplitude * (-1 if i % 2 else 1), 0))
        else:
            real, imag = ((1, 0), (0, 1), (-1, 0), (0, -1))[(i * (1 if mode == 2 else 3)) % 4]
            z.append((amplitude * real, amplitude * imag))
    absolute = [abs(real) + abs(imag) for real, imag in z]
    norm2 = sum(real * real + imag * imag for real, imag in z)
    deficits = [[absolute[i] * absolute[j] - z[i][0] * z[j][0] - z[i][1] * z[j][1]
                 for j in range(dimension)] for i in range(dimension)]
    assert all(x >= 0 for row in deficits for x in row)
    dq = Fraction(sum(Qmat[i][j] * deficits[i][j] for i in range(dimension) for j in range(dimension)), norm2)
    dg = Fraction(sum(Gmat[i][j] * deficits[i][j] for i in range(dimension) for j in range(dimension)), norm2)
    assert 0 <= dg <= 4 * dq
    direct_q = Fraction(sum(Qmat[i][j] * (z[i][0] * z[j][0] + z[i][1] * z[j][1])
                            for i in range(dimension) for j in range(dimension)), norm2)
    abs_q = Fraction(sum(Qmat[i][j] * absolute[i] * absolute[j]
                        for i in range(dimension) for j in range(dimension)), norm2)
    assert dq == abs_q - direct_q
    electric_mean = Fraction(sum(Ddiag[i] * absolute[i] ** 2 for i in range(dimension)), norm2)
    phase_rows.append(dict(mode=mode, integer_complex_amplitudes=z, norm_squared=norm2,
                           electric_mean=str(electric_mean), Q_mean=str(direct_q),
                           modulus_Q_mean=str(abs_q), Delta_Q=str(dq), Delta_Gamma=str(dg),
                           energy_phase_cost_at_delta_one=str(2 * dq),
                           cube_phase_margin=str(4 * dq - dg)))
assert any(Fraction(row['Delta_Gamma']) > 0 for row in phase_rows)

assert 2 * Fraction(1905, 2) - 2 * 3004 * Fraction(3, 10) == Fraction(513, 5)
assert 4 * (5 - 6 * Fraction(7, 10)) == Fraction(16, 5)
assert Fraction(16, 5) / Fraction(4, 5) == 4
report = dict(
    status='Exact bounded POST correspondence; no audit verdict',
    author_scientific_program_executed_or_imported=False,
    author_execution=execution, exact_result_stdout_and_source_correspondence=True,
    independently_recomputed_affine_columns=len(summaries), independently_recomputed_entries=total_entries,
    comparison_method='Own PRE full-charge-word hop rules; Gamma reconstructed by own PRE star identity, Q by complete outward-and-return primitives',
    all_columns=summaries,
    normalized_coherent_factor_one_half_rejected_entries=normalized_coherent_wrong_entries,
    physical_phase_control=dict(side=2, degree=3, kappa=1, dimension=dimension,
                                support=[dict(q=q, flux=list(flow)) for q, flow in support],
                                electric_diagonal=Ddiag, Q_matrix=Qmat, Gamma_matrix=Gmat,
                                rows=phase_rows,
                                limit='Physical finite-electric test of phase deficits with cube coefficient 4; not the all-volume proof or a sector infimum calculation'),
    exact_author_constants=dict(large_occupancy_gap='513/5', global_rate='16/5', stationary_gap='4'),
    source_scope='Root filling row/trial estimates remain provisional. No author35 controls/checker or other active packet accessed.',
    elapsed_seconds=time.perf_counter() - tic)
with (HERE / 'POST_PRIMITIVE_COMPARISON.json').open('x') as out:
    json.dump(report, out, indent=2)
    out.write('\n')
print(json.dumps(report, indent=2))
