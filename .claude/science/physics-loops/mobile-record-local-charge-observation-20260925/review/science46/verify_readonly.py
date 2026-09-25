#!/usr/bin/env python3
"""Genuinely read-only PRE46 verifier of frozen scientific data and sources.
No scientific program imports, subprocesses, or write operations.
"""
from collections import Counter
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent


def load(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ga(a, b): return a[0]+b[0], a[1]+b[1]
def gs(n, a): return n*a[0], n*a[1]
def gc(a): return a[0], -a[1]
def gm(a, b): return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def main():
    sources = load(BASE/'SOURCE_PINS.json')['sources']
    for row in sources:
        assert sha(Path(row['origin'])) == sha(BASE/row['snapshot']) == row['sha256']
    executions = []
    for folder, program in (('primitive_attempt01', 'charge_current_control.py'),
                            ('fourier_attempt01', 'fourier_charge_control.py')):
        path = BASE/folder
        receipt = load(path/'EXECUTION.json')
        assert receipt['exit_code'] == 0 and receipt['source_unchanged']
        assert receipt['source_sha256'] == sha(path/'source.py') == sha(BASE/program)
        assert receipt['stdout_sha256'] == sha(path/'stdout.json')
        assert receipt['stderr_sha256'] == sha(path/'stderr.txt')
        assert (path/'stderr.txt').read_bytes() == b''
        executions.append(dict(folder=folder, elapsed_seconds=receipt['elapsed_seconds'],
                               source_sha256=receipt['source_sha256'], stdout_sha256=receipt['stdout_sha256']))
    data = load(BASE/'primitive_attempt01/stdout.json')
    assert data['status'] == 'All exact primitive continuity and initial-noise controls passed'
    assert data['prior_or_author_code_imported'] is False
    fixture = data['fixture']
    edges = tuple((a, b) for a in (0, 1) for b in (2, 3, 4, 5))
    inc = tuple(tuple(int(x == a)-int(x == b) for a, b in edges) for x in range(6))
    assert fixture['edges'] == [list(e) for e in edges]
    assert fixture['incidence'] == [list(row) for row in inc]
    cycle = tuple(fixture['cycle'])
    assert [sum(s*e for s, e in zip(row, cycle)) for row in inc] == [0]*6
    cols = {tuple(row['q']): row for row in data['current_columns']}
    expected = {q for q in product((-1, 0, 1), repeat=6) if q[0] and q[1] and sum(q) == 2}
    assert set(cols) == expected and len(cols) == len(data['current_columns']) == 40
    mag_lookup, dis_lookup = {}, {}
    summaries = []
    for q, row in cols.items():
        N = sum(abs(x) for x in q)
        assert N == row['N'] and row['both_instruments_equal'] and row['current_flux_offset_independent']
        # Recover the explicitly specified tree solution, independently by divergence.
        E0 = [-q[2]-(q[1]-1), -q[3], -q[4], -q[5], q[1]-1, 0, 0, 0]
        assert [sum(s*e for s, e in zip(r, E0)) for r in inc] == [q[x]-int(x < 2) for x in range(6)]
        assert [r['circulation'] for r in row['energies']] == [0, -1000, 1001]
        for er in row['energies']:
            E = [a+er['circulation']*b for a, b in zip(E0, cycle)]
            D = sum(e*(e-q[a]) for (a, b), e in zip(edges, E) if q[b] == 0)
            assert D == er['D'] and D >= 0
        for term in row['magnetic_terms']:
            tq, shift = tuple(term['q']), tuple(term['shift'])
            coefficient = term['h4_coefficient']
            assert tq in cols and cols[tq]['N'] == N and coefficient < 0
            assert [sum(s*e for s, e in zip(r, shift)) for r in inc] == [y-x for x, y in zip(q, tq)]
            M = term['current_without_i_delta']
            Q = term['charge_generator_without_i_delta']
            assert M == [coefficient*e for e in shift]
            assert Q == [coefficient*(x-y) for x, y in zip(q, tq)]
            assert [Q[x]+sum(s*v for s, v in zip(inc[x], M)) for x in range(6)] == [0]*6
            key = q, tq, shift
            assert key not in mag_lookup
            mag_lookup[key] = term
        for term in row['dissipative_terms']:
            tq, shift = tuple(term['q']), tuple(term['shift'])
            assert tq in cols and cols[tq]['N'] == N
            assert [sum(s*e for s, e in zip(r, shift)) for r in inc] == [y-x for x, y in zip(q, tq)]
            M = term['minus_twice_current_over_kappa']
            Q = term['twice_charge_generator_over_kappa']
            assert Q == [sum(s*v for s, v in zip(r, M)) for r in inc]
            key = q, tq, shift
            assert key not in dis_lookup
            dis_lookup[key] = term
        summaries.append(dict(q=q, N=N, energies=row['energies'], magnetic_terms=len(row['magnetic_terms']),
                              dissipative_terms=len(row['dissipative_terms'])))
    for (q, tq, shift), term in mag_lookup.items():
        reverse = mag_lookup[tq, q, tuple(-s for s in shift)]
        assert reverse['h4_coefficient'] == term['h4_coefficient']
        assert reverse['current_without_i_delta'] == [-v for v in term['current_without_i_delta']]
    for (q, tq, shift), term in dis_lookup.items():
        reverse = dis_lookup[tq, q, tuple(-s for s in shift)]
        assert reverse['minus_twice_current_over_kappa'] == term['minus_twice_current_over_kappa']
        assert reverse['twice_charge_generator_over_kappa'] == term['twice_charge_generator_over_kappa']
    assert len(mag_lookup) == 553 and len(dis_lookup) == 217
    star_summaries = []
    branch_total = 0
    for star in data['star_initial']:
        d = star['degree']
        cases = set()
        mean = [0]*(d+1)
        C = [[0]*(d+1) for _ in range(d+1)]
        for r in star['branches']:
            b, c, sigma = r['mark'], r['hop'], r['sign_at_A']
            assert (b, c, sigma) not in cases
            cases.add((b, c, sigma))
            dq = [sigma-1]+[(-sigma if x == b else 1 if x == c else 0) for x in range(1, d+1)]
            de = [(sigma if x == b else -1 if x == c else 0) for x in range(1, d+1)]
            assert dq == r['charge_change'] and de == r['electric_shift']
            assert sum(dq) == 0 and dq[0] == sum(de) and dq[1:] == [-x for x in de]
            for x in range(d+1):
                mean[x] += dq[x]
                for y in range(d+1): C[x][y] += dq[x]*dq[y]
        assert cases == {(b, c, s) for b in range(1, d+1) for c in range(1, d+1) if b != c for s in (-1, 1)}
        assert mean == star['mean_derivative_over_kappa'] == [-2*d*(d-1)]+[2*(d-1)]*d
        assert C == star['covariance_derivative_over_kappa']
        for x in range(d+1):
            for y in range(d+1):
                expected_entry = 4*(d-1)*(d if x == y == 0 else 1 if x == y else -1 if (x == 0 or y == 0) else 0)
                assert C[x][y] == expected_entry
        assert len(cases) == star['intensity_over_kappa'] == 2*d*(d-1)
        branch_total += len(cases)
        star_summaries.append({key: value for key, value in star.items() if key != 'branches'})
    assert branch_total == 140 and len(star_summaries) == 7
    kernel = data['normal_field_initial_kernels']
    f, g = kernel['f'], kernel['g']
    mf = mg = cfg = (0, 0)
    for a, b in edges:
        df, dg = ga(f[b], gs(-1, f[a])), ga(g[b], gs(-1, g[a]))
        mf, mg = ga(mf, gs(6, df)), ga(mg, gs(6, dg))
        cfg = ga(cfg, gs(12, gm(gc(df), dg)))
    assert kernel['formula_values'] == dict(loss=48, mean_f=list(mf), mean_g=list(mg), covariance_fg=list(cfg))
    assert len(kernel['rows']) == 18
    for r in kernel['rows']:
        diagonal = r['left_cycle'] == r['right_cycle']
        assert r['loss'] == (48 if diagonal else 0)
        for name, expected_value in [('mean_f', mf), ('mean_g', mg), ('covariance_fg', cfg)]:
            assert r[name] == list(expected_value if diagonal else (0, 0))
    coherent = data['coherent_field_magnetic_current']
    q0 = (1, 1, 0, 0, 0, 0)
    numerator = [(0, 0)]*8
    alpha = {(0,)*8: (1, 0), cycle: (0, -1)}
    for source, coefficient in alpha.items():
        for term in cols[q0]['magnetic_terms']:
            target = tuple(x+y for x, y in zip(source, term['shift']))
            if tuple(term['q']) == q0 and target in alpha:
                weight = gm(gc(alpha[target]), coefficient)
                for e, M in enumerate(term['current_without_i_delta']):
                    numerator[e] = ga(numerator[e], gm(weight, (0, M)))
    assert coherent['norm_squared'] == 2 and coherent['mean_current_numerator_over_delta'] == [list(v) for v in numerator]
    assert numerator == [(4*c, 0) for c in cycle]

    fourier = load(BASE/'fourier_attempt01/stdout.json')
    assert fourier['status'] == 'All exact cubic Fourier normalization checks passed'
    assert fourier['prior_or_author_code_imported'] is False
    fourier_rows = []
    for group in fourier['groups']:
        L, V, h = group['L'], group['vertices'], group['L']//2
        assert L in (4, 8, 16) and V == L**3 and group['oriented_edges'] == 3*V
        modes = {tuple(r['k_index']) for r in group['mean_rows']}
        assert len(modes) == len(group['mean_rows']) == 6
        for r in group['mean_rows']:
            expected_mean = [-60*V]+[0]*(h-1) if tuple(r['k_index']) == (h,)*3 else [0]*h
            assert r['mean_times_sqrt_volume_over_kappa'] == expected_mean
        seen = set()
        for r in group['Hermitian_covariance_rows']:
            k, ell = tuple(r['k_index']), tuple(r['ell_index'])
            assert (k, ell) not in seen
            seen.add((k, ell))
            expected_poly = [0]*h
            if k == ell:
                expected_poly[0] = 120
                for ki in k:
                    for exponent in (ki, -ki):
                        reduced = exponent % L
                        expected_poly[reduced % h] += -20 if reduced < h else 20
            assert r['derivative_over_kappa_polynomial'] == expected_poly
        assert seen == {(k, ell) for k in modes for ell in modes}
        fourier_rows.append(group)
    print(json.dumps(dict(status='All read-only PRE46 evidence checks passed',
        verified_utc=datetime.now(timezone.utc).isoformat(), source_origins=len(sources), executions=executions,
        current_matter_groups=summaries, matter_count_by_N=dict(Counter(r['N'] for r in summaries)),
        magnetic_terms_checked=len(mag_lookup), dissipative_terms_checked=len(dis_lookup),
        all_current_terms_Gauss_and_Hermiticity_checked=True, star_groups=star_summaries,
        primitive_branch_rows_checked=branch_total, initial_complex_kernels=kernel,
        magnetic_coherence=coherent, complete_Fourier_groups=fourier_rows,
        raw_current_vectors_mechanically_checked=True, raw_current_vectors_manual_read_claim=False,
        mode='No program import or execution; read-only stored-data verification'), indent=2, sort_keys=True))


if __name__ == '__main__': main()
